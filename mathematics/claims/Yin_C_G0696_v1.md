---
author: Yin
---

# A localized actual weighted phase gives an inverse-square width bound

Human author Yin.
Phase_bands developed the exact localized probe, every-translated-circle contact count, complete L2 return and original-function multiplication bound.
The fixed curved patch and its finite localized power mass are reused from adopted C693v2, whose root and phase_bands contributors and bounded source scope remain unchanged.
This is author development, not an independent review.
The original polynomial family, full2d projection and prime schedule are exactly C684's; no family parameter is replaced and no two-factor law is imported.

## Statement

For integers j>=4K use the SAME actual weighted family

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K}, L_j=K+a_j+2, M_j=floor(a_j/4),
    n_j=ceil((L_j+1)^(17/8)), ell_j=ceil(log_2(L_j+1)),
    c_j=min{p prime:p>n_j ell_j}, d_j=c_j+L_j-2,
    e=(K,a_j,c_j), w=(1,1,2),
    P_j(x)=[(x^2-1)product_(i=1)^3(x^e_i-1)
       -(x/2)sum_(i=1)^3 w_i(x^e_i+1)product_(l!=i)(x^e_l-1)]/(x-1)^2.

The last prime is selected after forming the integer product n_j ell_j.
C684 proves that these are actual monic integral irreducible Salem minimal polynomials of even degree d_j and trace0, with log2<m(P_j)<log4.
All d_j relation columns in the ORIGINAL2d_j coefficient coordinates are retained:

    A_rel,j=[P_j,xP_j,...,x^(d_j-1)P_j],
    G_j=A_rel,j^T A_rel,j, Pi_j=A_rel,j G_j^-1 A_rel,j^T,
    v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig,j=v_(2d_j)^*Pi_j v_(2d_j)/(2d_j),
    f_(j,tau)=(1-h_orig,j/tau)_+, tau>0.                  (LP1)

All Haar measures have mass1 and Fourier coefficients use negative exponentials.
Write ||f||_A=sum_(n in Z)abs(fhat(n)) and W_*(f)=sum_(n!=0)abs(fhat(n)).
For fixed j,tau the original cap has finite A norm.
Its circle-root value is1 and its margin above mean is at least1/2 for tau<=1, as proved in the unchanged actual-family input.

Define the same weighted torus data

    R(z,u)=(z^K-1)(u-1), S(z,u)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    U=Acal/Bcal off common zeros, U=0 at common zeros,
    V(z,u)=U(z^-1,u^-1), h(z,u,w)=(1+Re(wV(z,u)))/2,
    F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+c_j gamma_2.

For every t in T^3, mu_(j,t) denotes the pushforward of circle Haar under z to t*iota_j(z).
These are the actual correlated laws.

### Fixed actual patch and an exact localized probe

Use the fixed C693v2 angular patch around x_*=(pi/K,pi), with

    D(t,s)=4sin t+cot(Kt/2)+cot(s/2),
    phi(t,s)=2arctan(D(t,s)/2), U(exp(it),exp(is))=exp(i phi(t,s)),
    -Hess(phi)>=lambda I on closed B_(4delta)(x_*),
    0<delta<min{pi/(8K),pi/8}.

The negative-definite Hessian at x_* and existence of such fixed lambda,delta are the actual accepted C693 facts.
Take its same nonnegative smooth bump

    chi(x)=exp[-1/(1-abs(x-x_*)^2/delta^2)] on B_delta(x_*),
    chi=0 elsewhere, periodically extended,
    s_chi=||chi||_2^2>0,
    D_phi,l=sup_(B_delta(x_*)) abs(partial_l phi), l=1,2,
    C_chi=||(1-Delta)^2 chi||_1, Delta=partial_t^2+partial_s^2,
    A_chi=13C_chi>0,
    B_der=[sum_(l=1)^2 (||partial_l chi||_2+D_phi,l||chi||_2)^2]^(1/2).

C693 supplies the fixed finite C_osc>=1 and the integer

    C_0=ceil(max{2,2B_der/sqrt(s_chi),
                             24sqrt(3)C_osc C_chi/s_chi}),

for which

    abs((chi U^k)hat(n))<=C_osc/k for every k>=1,n in Z^2,
    sum_(abs(p),abs(q)<=C_0 k)abs((chi U^k)hat(p,q))
                              >=a_loc k,
    a_loc=3s_chi/(4C_osc), sum_r abs(chihat(r))<=A_chi.    (LP2)

The middle inequality is its complete argument(CB15), before removing chi; it retains the entire closed square.
No new stationary-phase theorem or numerical value for its implicit constant is asserted.

Set

    b(z,u)=chi(z^-1,u^-1), b_j(z)=b(z,z^a_j),
    Phi_tau(z,u,w)=b(z,u)F_tau(z,u,w),
    f_loc,j,tau(z)=b_j(z)f_(j,tau)(z),
    B_chi=||chi||_infinity,
    S_loc=sum_(l=1)^2||partial_l chi||_infinity
                         +B_chi(D_phi,1+D_phi,2+1),
    C_sm=3pi sqrt(2) S_loc.                              (LP3)

The localized torus function is zero in a whole neighborhood of every common zero.
For each tau>0 it is globally Lipschitz, with smooth phase on its entire amplitude support.
For example extend the local real phase of V from a slightly larger inverse patch by a fixed cutoff, then form the global cap of that extension and multiply by b; the result is exactly Phi_tau.
The probe changes neither the actual original projection nor its cap; multiplication is paid explicitly when returning to f_(j,tau).

### Every translated law and the complete finite L2 comparison

For every actual j, every t in T^3 and0<eta<=1, the UNREGULARIZED phase satisfies

    mu_(j,t){h<=eta}<=2sqrt(eta).                         (LP4)

Finite common-zero values affect none of these integrals.
Product Haar obeys the same bound, with the smaller constant1.

Suppress j in a,c,d,L,M and use the exact adopted original errors

    epsilon_j=(4L-3)/(2d)+[1+pi L(5+2log c)]/(2c),
    E_bal=4(3+3pi), epsilon_j<=E_bal M^(-9/8),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3.

For M>=2,0<tau<=1/64 define the exact positive finite smoothing

    Fej_N(s)=N^-1 abs(sum_(r=0)^(N-1)exp(irs))^2,
    P_M=Fej_N^2/[(2N^2+1)/(3N)], N=floor(M/2)+1,
    Q_tau=Phi_tau*(three-coordinate product of P_M),
    B_loc(j,tau)=B_chi min{1,sqrt(C_stab epsilon_j)}
                                 +2C_sm M^-1 tau^(-1/4).

Then

    ||f_loc,j,tau-Q_tau composed with iota_j||_2
                      +||Phi_tau-Q_tau||_2<=B_loc(j,tau). (LP5)

The first norm is on the original circle and the second on the full torus.
For EVERY finite Gamma in the closed integer box[-M,M]^3,

    sum_(gamma in Gamma)
      abs(fhat_loc,j,tau(H_j(gamma))-Phihat_tau(gamma))
                  <=sqrt(card(Gamma))B_loc(j,tau).        (LP6)

Empty sets, all signs, zero and all endpoints are included.
All original characters are distinct.
The five-cost decomposition consists of the actual original comparison, TWO identically zero regularization terms for this exact localized phase, and TWO paid smoothings.
No zero regularization expense is claimed for the unlocalized F_tau.

### Full local band, original-function return and sharper critical strip

For0<tau<=1/64 set

    L_tau=floor(1/(4sqrt(tau))),
    Gamma_tau={(p,q,k):1<=k<=L_tau,abs(p),abs(q)<=C_0 k},
    N_tau=sum_(k=1)^(L_tau)(2C_0 k+1)^2
                                      <=(2C_0+1)^2 L_tau^3,
    C_mass=3a_loc/(1024pi)>0,
    C_err=(2C_0+1)/8 max{B_chi sqrt(C_stab E_bal),2C_sm},
    H=M^2 tau.

Whenever M>=2 and

    C_0 L_tau<=M,                                       (LP7)

the whole original image of Gamma_tau is positive and distinct, and

    W_*(f_(j,tau))>=tau^(-1/2)/A_chi
       *[C_mass-C_err(M^(-1/16)H^(-1/4)+H^(-1/2))]-1.    (LP8)

The ENTIRE selected set and the entire multiplication norm are paid.

Define fixed thresholds

    H_*=max{1,C_0^2/16,(4C_err/C_mass)^2},
    M_*=ceil(max{2,8sqrt(H_*),(4C_err/C_mass)^16}),
    j_*=max{4K,ceil(4M_*/K)}.

For EVERY actual j with M_j>=M_* and EVERY width in the nonempty strip

    H_* M_j^-2<=tau<=1/64,

one has

    W_*(f_(j,tau))>=C_mass tau^(-1/2)/(2A_chi)-1.         (LP9)

Every j>=j_* meets the actual M threshold.
In particular for every fixed H>=H_*, tau_j=H M_j^-2 gives

    W_*(f_(j,tau_j))>=C_mass M_j/(2A_chi sqrt(H))-1
                                                   ->infinity. (LP10)

The previous critical scale now admits EVERY fixed h>0, including arbitrarily small ones:

    tau_j=h M_j^(-3/2)
    implies W_*(f_(j,tau_j))
              >=C_mass M_j^(3/4)/(2A_chi sqrt(h))-1
                                                   ->infinity. (LP11)

This last assertion is eventual for each h, without an h-independent entry time.

For the genuine degree put Z_j=d_j/(1+log d_j), and D_*=2^(240/17)H_*.
Every positive shrinking sequence tau_j->0 with

    Z_j^(16/17)tau_j>=D_* eventually

obeys(LP9) eventually and therefore has divergent W_*.
For every fixed h>=D_*, the actual widths tau_j=h Z_j^(-16/17) give

    W_*(f_(j,tau_j))
               >=C_mass Z_j^(8/17)/(2A_chi sqrt(h))-1
                                                   ->infinity. (LP12)

All constants are fixed independently of j,tau and the selected frequencies.
The entire actual2d window, prime schedule, source depths and log2<m(P_j)<log4 remain.
This does not prove every smaller H at the NEW inverse-square scale, sharpness, a near-one family, an upper bound over all inputs or unrestricted G0001 completion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Complete argument

### 1. Exact accepted inputs and what is changed

The actual family, a,c,d,L,M and full projection in(LP1) coincide with adopted C684.
Its source/killer, weighted integrality, parity, cyclotomic removal, Salem minimality, exterior root, trace and degree therefore apply without a parameter substitution.
Its original strong cap comparison is valid for every tau>0 and follows from the full raw/cyclic/missing-sample/Gram-pole/observability argument.
In particular

    ||f_(j,tau)-F_tau composed with iota_j||_1
                              <=min{1,C_stab epsilon_j}.

The pullback convention differs from its smooth cancelled phase only on a finite set.
The difference of the two caps has modulus at most1, so its L2 norm is at most min{1,sqrt(C_stab epsilon_j)}.
Multiplying by b_j gives the first term of B_loc.
Neither a lower bound on the full Gram ratio nor an independent reference distribution is assumed.

The actual C693 patch, bump and constants are unchanged.
Its probability-Haar localized coefficient estimate, derivative Bessel tail and Parseval argument prove precisely(LP2), before its later torus deconvolution.
The fixed bump is supported away from every common zero.
Here it is retained in the torus cap, rather than removed before paying the original approximation error.
This is the essential changed comparison and the reason that its regularization cost can disappear legitimately.

The reuse check also distinguishes C714's globally smooth ONE-coordinate phase and C723's fixed-width ceiling for that two-factor family.
Their original laws and conclusions are not transferred to this weighted family.
Only their already established elementary coordinate-path/L2/finite-Bessel method informs the calculation below; all weighted translated-law premises are proved directly.

### 2. The unregularized contact law on every actual translated circle

Write a translate as

    z=exp(i(t+alpha)), u=exp(i(at+beta)), w=exp(i(ct+gamma)).

Off the two cotangent pole families, the exact weighted formula gives

    V(z,u)=(2-iD_(alpha,beta)(t))/(2+iD_(alpha,beta)(t)),
    D_(alpha,beta)=4sin(t+alpha)
                 +cot(K(t+alpha)/2)+cot((at+beta)/2).

This uses the inversion of BOTH phase coordinates in the definition of V.
For every regular t,

    D'_(alpha,beta)=4cos(t+alpha)
       -(K/2)csc^2(K(t+alpha)/2)-(a/2)csc^2((at+beta)/2)<0,

because K+a>8.
There are N distinct poles in one circle, with N<=K+a.
Each pole is simple with a positive residue:2/K,2/a, or their sum when the two pole locations coincide.
Thus on each open complementary interval D decreases from positive infinity to negative infinity.

The inverse Cayley phase has local derivative

    psi'=-4D'/(4+D^2)>0.

At a pole with residue r>0, its phase extends smoothly through the value -1 and its derivative has the positive limit4/r.
One can see smoothness by writing the Cayley quotient in terms of1/D near that pole.
Following the continuous phase lift across the intervals gives a total increase2pi N.
Coincident poles count once, with their summed positive residue; no extra branch turn or missing interval is inserted.
At a simultaneous torus common zero, the initially declared V=0 changes only that isolated point of this translated curve, and the smooth extension just described supplies the same almost-everywhere phase law.

For Theta(t)=ct+gamma+psi(t),

    Theta'>=c, Theta(t+2pi)-Theta(t)=2pi(c+N),
    c+N<=c+K+a=d<2c.

Changing the increasing phase variable over its integer number of turns gives for0<eta<=1

    mu_(j,t){h<=eta}
      <=[(c+N)/c]*(2/pi)arcsin(sqrt(eta))
      <=2sqrt(eta).                                     (LP13)

The interval boundaries and isolated changed values have measure zero.
Every alpha,beta,gamma is included, including all coincident-pole cases.
Under product Haar ONLY, the conditional w phase is uniform and gives the constant1.
This proves(LP4) without a regularizer, an amplitude mean approximation, or original-coordinate independence.

### 3. Exact localization and both complete smoothing expenses

On the support of b, the phase V is smooth and its two coordinate angular derivatives are bounded by D_phi,1 and D_phi,2 in modulus.
For the scalar h=(1+cos Theta)/2,

    abs(partial_l h)<=D_phi,l sqrt(h), l=1,2,
    abs(partial_3 h)<=sqrt(h).

For0<tau<=1/64, along every coordinate path the localized clipped function Phi_tau is absolutely continuous.
Its derivative envelopes are

    [||partial_l chi||_infinity+B_chi D_phi,l]
                           tau^(-1/2)1_(h<=tau), l=1,2,
    B_chi tau^(-1/2)1_(h<=tau), l=3.                    (LP14)

The amplitude-derivative term is supported in the contact set and costs its supremum; tau^-1/2>=1 pays that term in the same envelope.
Outside the local phase patch b and its derivatives vanish, and Phi_tau is identically zero near every global singularity.
The open contact intervals, their endpoints and the flat bump boundary justify pathwise FTC; no ambient a.e. derivative is restricted to a singular curve.

By(LP13), each envelope's L2 norm under EVERY intermediate translated circle is at most sqrt(2) times its displayed constant times tau^-1/4.
The same bound holds on the torus.
Each positive P_M has mass1, closed Fourier support[-M,M], and first shortest-angle moment at most3pi/M.
Telescope the three coordinate paths, integrate their L2 bounds and then the positive kernels, to obtain

    ||Phi_tau-Q_tau||_(L2(nu_3))<=C_sm M^-1 tau^-1/4,
    ||Phi_tau composed with iota_j-Q_tau composed with iota_j||_2
                                  <=C_sm M^-1 tau^-1/4. (LP15)

The L2 integral triangle inequality follows from Cauchy--Schwarz after expanding its square as a double integral, so it is valid for these bounded functions and probability kernels.
All translations created by the telescoping paths are covered by Section2.
The third coordinate and both amplitude-derivative coordinates are included in S_loc.

No phase regularization is taken: in the five-term comparison insert Phi_tau itself as each of the two regularized intermediate functions, making BOTH associated differences identically zero.
This is justified by its global localized Lipschitz property and the preceding complete derivative estimate.
It makes no assertion that regularizing the original unlocalized F_tau has zero cost.
Combining the actual original comparison with the TWO(LP15) proves(LP5).

### 4. Closed-box return and exact removal of the original probe

For the unchanged family C684 proves a>2M and c>a^2>2M(1+a).
Thus H_j(delta)!=0 on the punctured closed[-2M,2M]^3 box.
Q_tau is a finite polynomial supported in the closed-M box, and finite expansion gives

    (Q_tau composed with iota_j)hat(H_j(gamma))=Qhat_tau(gamma)

for every gamma in that box.
The original returned characters are distinct and orthonormal, as are the torus characters.
Finite Bessel applied to the two errors in(LP5), followed by the triangle inequality for their finite l2 vectors and finite Cauchy--Schwarz, proves(LP6).
This pays every coefficient of Gamma, with all signs, zero and endpoints, and is zero for an empty set.

The smooth Fourier series of b is absolutely summable and has sum at most A_chi by(LP2) and inversion.
After substituting u=z^a, all aliases may be grouped absolutely, giving

    ||b_j||_A<=sum_(p,q)abs(bhat(p,q))<=A_chi.            (LP16)

No injectivity of these infinitely many probe frequencies is assumed.
Since f_(j,tau) already has finite A norm, coefficient convolution gives

    W_*(f_loc,j,tau)<=||b_j f_(j,tau)||_A
           <=A_chi||f_(j,tau)||_A
           <=A_chi[W_*(f_(j,tau))+1].                   (LP17)

The final step uses0<=f_(j,tau)<=1 and hence abs(fhat_(j,tau)(0))<=1.
This is the full expense for removing the probe on the ACTUAL original circle, including its possible zero-frequency aliases.

### 5. Full localized curvature mass and all returned errors

Under product Haar, the exact positive w-coefficient identity is

    Phihat_tau(p,q,k)=ghat_tau(k)(b V^k)hat(p,q),
    g_tau(exp(i theta))=(1-(1+cos theta)/(2tau))_+.

At common zeros b=0 in a neighborhood, so there is no exceptional contribution.
The function b V^k is the simultaneous inversion of chi U^k, so the full symmetric localized band in(LP2) applies unchanged.
C681's direct scalar calculation supplies

    abs(ghat_tau(k))>=3sqrt(tau)/(8pi), 1<=k<=L_tau.

Consequently the ENTIRE Gamma_tau has mass at least

    [3a_loc sqrt(tau)/(8pi)]sum_(k=1)^(L_tau) k
       >=[3a_loc sqrt(tau)/(16pi)]L_tau^2
       >=C_mass tau^-1/2,                              (LP18)

using L_tau>=1/(8sqrt(tau)) when tau<=1/64.
Different k give disjoint triples.
The exact full count satisfies N_tau<=(2C_0+1)^2 sum_(k=1)^(L_tau)k^2<=(2C_0+1)^2 L_tau^3, with all square endpoints retained.

Under(LP7), all three coordinates lie in the closed-M box.
Every original image is positive because

    H_j(p,q,k)>=c-M(1+a)>0,

and every pair is distinct by the closed2M result.
Apply(LP6) to the entire Gamma_tau, subtract its full error from(LP18), and then use(LP17).
The count and L_tau<=1/(4sqrt(tau)) give

    sqrt(N_tau)<=(2C_0+1)L_tau^(3/2)
                           <=(2C_0+1)/(8tau^(3/4)).

The complete error before division by A_chi is therefore at most

    (2C_0+1)/8
      *[B_chi sqrt(C_stab E_bal)M^-9/16 tau^-3/4
                                      +2C_sm M^-1 tau^-1]. (LP19)

Relative to tau^-1/2 and with H=M^2tau, the two factors are exactly

    M^-9/16 tau^-1/4=M^-1/16 H^-1/4,
    M^-1 tau^-1/2=H^-1/2.

The definition of C_err now proves(LP8), including the full multiplication loss -1.

### 6. Explicit thresholds, old small heights and actual degree

If H>=H_*, then C_0 L_tau<=C_0 M/(4sqrt(H))<=M, paying the entire support at the NEW critical equality.
The same H threshold gives C_err H^-1/2<=C_mass/4.
For M>=M_*, one has C_err M^-1/16<=C_mass/4, and H^-1/4<=1.
Thus(LP8) proves(LP9) throughout the stated strip.
Its nonemptiness follows from M>=8sqrt(H_*), and the finite-kernel premise follows from M>=2.
If j>=j_*, then a_j>(j+1)K>4M_*, so floor(a_j/4)>=M_*.
For fixed H>=H_*, the widths H M_j^-2 tend to zero and eventually lie in the strip; substitution proves(LP10).

For ANY fixed h>0 at the previous scale tau_j=h M_j^-3/2, the new enlargement is H_j=h M_j^1/2.
It eventually exceeds H_* even when h is arbitrarily small.
For example M_j>=max{M_*,(H_*/h)^2,(64h)^(2/3)} suffices for all finite-strip conditions.
This proves(LP11) and explains its h-dependent onset.

Finally C684's actual-degree bounds are

    M_j^(17/8)/16<Z_j<2^15 M_j^(17/8).

Raising to16/17 gives

    16^(-16/17)M_j^2<Z_j^(16/17)<2^(240/17)M_j^2.

Thus Z_j^(16/17)tau_j>=D_* implies M_j^2tau_j>H_*.
For every positive shrinking sequence with that eventual lower bound, its M_j and tau_j eventually meet the other finite-strip conditions, so(LP9) holds eventually and tends to infinity.
For a fixed h>=D_*, direct substitution tau_j=h Z_j^-16/17 yields(LP12).
There is no universal sequence-entry time, and no change of degree normalization or hidden prime logarithm.

## Source, reuse and remaining boundary

The fixed source-supported stationary-phase work is exactly C693v2 and its selected Tao26-U003v2 primary-statement/applicability scope, not a new original-proof audit.
Its local estimate and full localized square are used before deconvolution; the present proof instead pays a fixed A-norm multiplication expense on the original circle.
C684's original full2d comparison, genuine Gram pole, every input parameter, source/killer eligibility and positive Mahler interval are unchanged.
Its unlocalized contact-weighted weak norm theorem is not silently promoted to L2; the new exact localized path estimates and all translated unregularized contact laws are proved here.
C637 supplies the same finite positive kernel and its exact normalization, support and moment.
The one-coordinate two-factor C714/C723 results were read to distinguish their mechanism and family boundary; no two-factor family conclusion or fixed-width ceiling is an input to this weighted theorem.
The former weak-budget height loss is therefore an obstruction to that particular return estimate, not an obstruction to these same actual inputs.
The inverse-square small-height range, optimality, sharper prime schedules and near-one realization remain separate obligations.
The actual log2<m(P_j)<log4 interval prevents interpreting this analytic improvement as a solution of the unrestricted Mahler problem.

## Assessment history

### Decision localized-inverse-square-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:18 |
| status | open |
| reason | Register the complete exact local probe on the unchanged weighted actual family, every-translated-circle unregularized contact law, original L2 comparison, two justified zero regularization differences and two paid smoothings, full finite curved support and entire original probe-removal cost. The new inverse-square strip and actual16/17 degree criterion include every positive fixed height at the previous3/2 scale. Fresh independent whole review remains required, with all source-depth, actual-window, positive-Mahler and unrestricted-realization boundaries retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Localized actual inverse-square theorem](#statement) | LP1--LP12: unchanged actual weighted family/full2d projection, fixed local probe, every translated contact law, complete finite L2 return, full support and original probe expense, explicit inverse-square thresholds and actual-degree/sequence conclusions. |
| argument | [Complete localized original comparison](#complete-argument) | Sections1--6/LP13--LP19: exact phase orientation, all separate/coincident poles and winding, every translated coordinate path, the five expenses with two exact zero terms, full original Fourier return and multiplication, entire band count and all support/degree quantifiers. |
| dependency | [Adopted actual weighted family](Yin_C_G0684_v1.md#decision-whole-reviewed-2026-10-24) | Exact same17/8-log prime schedule and actual Salem polynomial, all original2d raw/cyclic/sample/Gram-pole/observability comparison, every-width cap L1 stability, closed2M aliases, genuine degree and log2..log4 interval. |
| dependency | [Adopted actual curved local phase](Yin_C_G0693_v2.md#decision-whole-reviewed-2026-10-24) | Fixed actual patch and smooth bump, all-linear-frequency C_osc bound, integer C_0, localized full-square mass CB15 and bump A-norm bound before its later deconvolution; no reuse of its weaker original-cost conclusion as a new L2 theorem. |
| dependency | [Exact scalar cap harmonics](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | The direct scalar harmonic lower bound for1<=k<=floor(1/(4sqrt(tau))) and tau<=1/64 under product Haar. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, positivity, closed integer support and first shortest-angle moment; finite Bessel/Cauchy and path costs are explicitly reapplied here. |
| support | [Retained stationary-phase source depth](../audits/literature/Tao26/Yin_U003.md#tao26-u003) | Same retained primary Lemma3.3 and uniform-parameter scope selected by C693, at checked statement/applicability depth without new source proof inspection or numerical implicit constant. |
| support | [Source and remaining boundary](#source-reuse-and-remaining-boundary) | Exact unchanged-family scope versus new localized comparison, distinction from two-factor ceilings, positive Mahler interval and still-open inverse-square smaller heights/optimality/near-one boundary. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:30 |
| status | proved |
| reason | Adopt the independent whole review of all LP1--LP19 and Sections1--6 on the unchanged actual C684 weighted family. Every translated contact law, exact localized regularity, both zero regularization terms, two L2 smoothings, full finite band and original probe-removal expense are checked. The inverse-square strip, all positive fixed heights at the old three-halves scale and actual16/17 degree criterion are proved, retaining the accepted source depths and positive Mahler interval; no near-one or unrestricted conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Localized actual inverse-square theorem](#statement) | LP1--LP12: unchanged actual weighted family/full2d projection, fixed local probe, every translated contact law, complete finite L2 return, full support and original probe expense, explicit inverse-square thresholds and actual-degree/sequence conclusions. |
| argument | [Complete localized original comparison](#complete-argument) | Sections1--6/LP13--LP19: exact phase orientation, all separate/coincident poles and winding, every translated coordinate path, the five expenses with two exact zero terms, full original Fourier return and multiplication, entire band count and all support/degree quantifiers. |
| dependency | [Adopted actual weighted family](Yin_C_G0684_v1.md#decision-whole-reviewed-2026-10-24) | Exact same17/8-log prime schedule and actual Salem polynomial, all original2d raw/cyclic/sample/Gram-pole/observability comparison, every-width cap L1 stability, closed2M aliases, genuine degree and log2..log4 interval. |
| dependency | [Adopted actual curved local phase](Yin_C_G0693_v2.md#decision-whole-reviewed-2026-10-24) | Fixed actual patch and smooth bump, all-linear-frequency C_osc bound, integer C_0, localized full-square mass CB15 and bump A-norm bound before its later deconvolution; no reuse of its weaker original-cost conclusion as a new L2 theorem. |
| dependency | [Exact scalar cap harmonics](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | The direct scalar harmonic lower bound for1<=k<=floor(1/(4sqrt(tau))) and tau<=1/64 under product Haar. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Squared-Fejer normalization, positivity, closed integer support and first shortest-angle moment; finite Bessel/Cauchy and path costs are explicitly reapplied here. |
| support | [Retained stationary-phase source depth](../audits/literature/Tao26/Yin_U003.md#tao26-u003) | Same retained primary Lemma3.3 and uniform-parameter scope selected by C693, at checked statement/applicability depth without new source proof inspection or numerical implicit constant. |
| support | [Source and remaining boundary](#source-reuse-and-remaining-boundary) | Exact unchanged-family scope versus new localized comparison, distinction from two-factor ceilings, positive Mahler interval and still-open inverse-square smaller heights/optimality/near-one boundary. |
| review | [Fresh isolated whole review](../audits/reviews/Yin_R_G0918_v1.md#whole-localized-inverse-square-finding) | Entire fixed statement and argument, exact direct-input applications, all quantifiers and declared limitations; independently reviewed. |

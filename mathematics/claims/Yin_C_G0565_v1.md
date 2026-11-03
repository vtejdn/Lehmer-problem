---
author: Yin
---

# Complete paid first-band transfer for the actual moving Salem contact layer

The complete original mathematical argument is retained from [L426](../ledger/Yin_L_G0426_v1.md#moving-band-question).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The [original review](../audits/reviews/Yin_R_G0439_v1.md#moving-band-whole-independent-finding) keeps its actual original L/J/source bindings, date, relationship declaration and checked scope; it is not retrospectively bound to this C.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Fix the same even integer K as the actual four-exponent construction,
K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))).
On the three-torus define the explicit polynomials
    R=(z^K-1)(u-1)(v-1),
    S=(z^K+1)(u-1)(v-1)+(z^K-1)(u+1)(v-1)+(z^K-1)(u-1)(v+1),
    Acal=-(z^2-1)R-zR/2+zS/2,
    Bcal=(z^2-1)R-zR/2-zS/2.
Set U=Acal/Bcal off their common-zero set and0 on that set, g=abs(Acal)^2+abs(Bcal)^2 and Ncal=2Acal conjugate(Bcal).
All Haar measures have mass1, Fourier coefficients use exp(-i gamma dot theta), and angular derivatives use radians.
Define
    A_K=1+||g||_infinity+||Ncal||_infinity
        +sum_(l=1)^3(||partial_l g||_infinity+||partial_l Ncal||_infinity),
    D_K=8pi A_K^2.
For an actual degree-d_j Salem P_j of the specified schedule, set N_j=2d_j and let A_rel,j be the N_j-by-d_j full coefficient matrix of P_j,tP_j,...,t^(d_j-1)P_j.
The original rank-d_j residual projection and its actual single-circle symbol are
    R_j=I-A_rel,j(A_rel,j^T A_rel,j)^-1 A_rel,j^T,
    v_j(t)=(1,t,...,t^(2d_j-1))^T,
    k_j(t)=(2d_j)^-1 v_j(t^-1)^T R_j v_j(t).
Thus the kernel below uses every original coefficient, with no cyclic or conjugate-distribution replacement.

Keep L402's fixed K and actual primes

    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    c_j=min{p prime:p>(K+a_j+b_j+3)^2},
    L_j=K+a_j+b_j+2, d_j=c_j+L_j-3.

The actual monic irreducible Salem P_j is unchanged, with log2<m(P_j)<log4.
Let k_j be C158/C172's original residual kernel in the SAME2d_j coefficient coordinates.
It takes values in[0,1] and has circle mean1/2.
Set f_(j,tau)=psi_tau(k_j) and use the full signed nonconstant norm

    W_*(f)=sum_(h in Z, h!=0) |fhat(h)|.

For each fixed j,tau this norm is finite by C174's periodic Lipschitz argument.
The actual contact value remains1 and its contact-minus-Haar margin is at least1/2, for every tau in(0,1].
Nothing below changes the input, degree, projection or contact convention.

Use C171's fixed three-torus phase U=Acal/Bcal off its common-zero set and0 on that set.
Put V(z,u,v)=U(z^-1,u^-1,v^-1) and

    Kcal(z,u,v,w)=(1-Re(w V(z,u,v)))/2,
    F_tau=psi_tau(Kcal),
    iota_j(z)=(z,z^(a_j),z^(b_j),z^(c_j)),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3. (1)

All Fourier coefficients on T^q use the character exp(-i gamma dot theta) and probability Haar measure.
C172's complete original-window comparison gives

    ||k_j-Kcal composed with iota_j||_1<=epsilon_j,
    epsilon_j=(4L_j-5)/(2d_j)+E_j/2,
    E_j=[1+pi L_j(5+2log c_j)]/c_j ->0.                 (2)

The removable single point on the actual circle affects no Haar norm.

The explicit constant D_K below depends only on the fixed torus polynomials and K.
For all sufficiently large j define

    M_j=floor(a_j/4)>=2,
    omega_j=(1+log M_j)/M_j,
    delta_j=omega_j^(1/13),
    beta_j=epsilon_j+(64+3D_K)delta_j ->0,
    Gamma_(j,tau)=3 sqrt(beta_j/tau)+beta_j/tau.          (3)

The symbol beta_j in(3) is an approximation budget, not the exterior Salem root.
For a finite set E subset [-M_j,M_j]^3 intersection Z^3 put

    N=|E|,
    S(E)=sum_(eta in E)|Uhat(-eta)|,
    h_j(eta)=c_j+eta_0+a_j eta_1+b_j eta_2.

For EVERY such E and EVERY0<tau<=1/4, the full original norm satisfies

    W_*(f_(j,tau))
      >=[3/(8pi)] sqrt(tau) S(E)
        -min{N beta_j/tau, sqrt(N) Gamma_(j,tau)}.       (4)

For the empty set this reads0<=W_*.
The frequencies h_j(eta) are distinct and strictly positive; only this paid positive first band is used for the lower bound on the full two-sided norm.
No optimality of E or completeness of the selected band is asserted.

Consequently a precise sufficient condition for a moving tau_j->0 is the existence of these finite E_j such that

    sqrt(tau_j) S(E_j) ->infinity,
    min{N_j beta_j/tau_j, sqrt(N_j)Gamma_(j,tau_j)}
                    =o(sqrt(tau_j)S(E_j)).              (5)

Condition(5) implies actual W_*(f_(j,tau_j))->infinity.
It is a sufficient condition, not an assumption supplied by the original family theorem.
The rest of this account proves(4), identifies its paid inputs and gives an explicit regime where this particular certificate cannot establish divergence.
The fixed phase also satisfies sum_eta|Uhat(eta)|^2<=1 and sup_(|E|=N)S(E)/sqrt(N)->0.
For any simultaneous tau_j->0 with liminf beta_j/tau_j^2>0, neither displayed certificate can yield divergent lower bounds uniformly over finite E: the individual-error certificate is at most [3/(8pi)]^2 tau_j^2/(4beta_j), and a positive Bessel certificate can use only uniformly bounded N.
This is a limitation of these sufficient estimates, not an upper bound on actual W_*, an actual bounded-Wiener construction or a necessary condition for actual divergence.
Beta_j/tau_j^2->0 alone is not asserted sufficient.
The fixed-input thin limit and fixed-Lipschitz regime retain their separate limit orders.

## Current assessment

[Selected decision](#decision-complete-fixed-registration-open)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:24 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Entire original L426 Sections1–7, all16 formulas/11 input rows: exact finite alias box and complete original2d kernel, explicit phase/regularization/Fejer/Bessel costs, every finite set and width, sufficient moving criterion and certificate-only limitation. |
| argument | [Entire complete argument](#argument) | Entire original L426 Sections1–7, all16 formulas/11 input rows: exact finite alias box and complete original2d kernel, explicit phase/regularization/Fejer/Bessel costs, every finite set and width, sufficient moving criterion and certificate-only limitation. |
| dependency | [Exact fixed input](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-schedule) | Fixed K, separated-prime schedule, genuine original irreducible Salem factors, complete cyclotomic removal/full degree and log2<m<log4; source scopes reused without new proof audit. |
| dependency | [Exact fixed input](Yin_C_G0158_v1.md#statement) | Actual rank-d residual projection in2d coordinates, single-Haar range and mean only. |
| dependency | [Exact fixed input](Yin_C_G0171_v1.md#two-block-torus-phase) | Exact fixed Acal/Bcal, equal moduli, common-zero set and inverse phase orientation. |
| dependency | [Exact fixed input](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Complete original-window L1 epsilon with actual rank, boundary and missing-mode terms. |
| dependency | [Exact fixed input](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Full elementary probability-Haar Fejer moment; product and alias estimates are proved locally. |
| dependency | [Exact fixed input](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual finite full Wiener norm and contact margin; no fixed-input thin-limit exchange. |
| support | [Exact fixed input](Yin_C_G0174_v1.md#narrow-contact-source-interface) | Existing probability-Haar attribution only; finite Bessel is proved locally. |

## Complete original argument

<a id="argument"></a>

### Original account: Paid first-band bounds for a moving contact layer

Date: 2026-10-18T17:33.
Human author Yin.
Root supplied the question about quantitative Fourier-band control in the corridor left open by C174.
The angular_envelope_review agent authors the new quantitative transfer and method-boundary analysis below.
This is a separate author extension; accepted C174 and its independent review are not modified.
No width scan, prime enumeration, numerical integration or new input family is selected.

<a id="moving-band-question"></a>
## Exact question and reuse

Keep the SAME original L402/C171 family and C174 clipped transform psi_tau(s)=(1-(1-s)/tau)_+, with0<tau<=1.
C174 pays the fixed-input thin-peak limit but supplies no uniform threshold for an arbitrary moving tau_j.
C173 handles tau bounded below through a fixed Lipschitz class.
The question is whether the first Fourier band of the exact C171 torus phase supplies a sufficient quantitative condition on the remaining moving corridor, and which parts of that condition follow from the actual L402 schedule.

The bounded screen inspected C171's exact character separation and singular regularization, C172's original-kernel Haar L1 return and finite Fejer first moment, L179's positive-modulus quantitative averaging and C137's finite no-alias constant-coefficient mechanism.
L179 Section4 has a full-torus modulus lower bound1 and the explicit error2pi D(D+1)/n.
C137 uses a fixed polynomial with support |i|<=3J, |j|<=J and N>3J to eliminate every nonconstant alias.
Those exact mechanisms do not remove the present phase singularity or the1/tau composition cost.
The needed regularization and finite-band estimates are instead proved completely below.
No new external quantitative equidistribution theorem is a premise.

The responsible narrow-layer theorem is [C174](Yin_C_G0174_v1.md#narrow-contact-fixed-statement), including its original two-limit qualification.
The present author contributed C171/C172/C173/C174 and reuses their accepted independent scopes without claiming a new independent review.
All means below are single normalized Haar integrals on the stated circle or torus; no distribution of conjugates is substituted.

<a id="moving-band-target"></a>
## 1. Complete finite-band statement

Keep L402's fixed K and actual primes

    a_j=min{p prime:p>(j+1)K},
    b_j=min{p prime:p>(K+a_j+3)^2},
    c_j=min{p prime:p>(K+a_j+b_j+3)^2},
    L_j=K+a_j+b_j+2, d_j=c_j+L_j-3.

The actual monic irreducible Salem P_j is unchanged, with log2<m(P_j)<log4.
Let k_j be C158/C172's original residual kernel in the SAME2d_j coefficient coordinates.
It takes values in[0,1] and has circle mean1/2.
Set f_(j,tau)=psi_tau(k_j) and use the full signed nonconstant norm

    W_*(f)=sum_(h in Z, h!=0) |fhat(h)|.

For each fixed j,tau this norm is finite by C174's periodic Lipschitz argument.
The actual contact value remains1 and its contact-minus-Haar margin is at least1/2, for every tau in(0,1].
Nothing below changes the input, degree, projection or contact convention.

Use C171's fixed three-torus phase U=Acal/Bcal off its common-zero set and0 on that set.
Put V(z,u,v)=U(z^-1,u^-1,v^-1) and

    Kcal(z,u,v,w)=(1-Re(w V(z,u,v)))/2,
    F_tau=psi_tau(Kcal),
    iota_j(z)=(z,z^(a_j),z^(b_j),z^(c_j)),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3. (1)

All Fourier coefficients on T^q use the character exp(-i gamma dot theta) and probability Haar measure.
C172's complete original-window comparison gives

    ||k_j-Kcal composed with iota_j||_1<=epsilon_j,
    epsilon_j=(4L_j-5)/(2d_j)+E_j/2,
    E_j=[1+pi L_j(5+2log c_j)]/c_j ->0.                 (2)

The removable single point on the actual circle affects no Haar norm.

The explicit constant D_K below depends only on the fixed torus polynomials and K.
For all sufficiently large j define

    M_j=floor(a_j/4)>=2,
    omega_j=(1+log M_j)/M_j,
    delta_j=omega_j^(1/13),
    beta_j=epsilon_j+(64+3D_K)delta_j ->0,
    Gamma_(j,tau)=3 sqrt(beta_j/tau)+beta_j/tau.          (3)

The symbol beta_j in(3) is an approximation budget, not the exterior Salem root.
For a finite set E subset [-M_j,M_j]^3 intersection Z^3 put

    N=|E|,
    S(E)=sum_(eta in E)|Uhat(-eta)|,
    h_j(eta)=c_j+eta_0+a_j eta_1+b_j eta_2.

For EVERY such E and EVERY0<tau<=1/4, the full original norm satisfies

    W_*(f_(j,tau))
      >=[3/(8pi)] sqrt(tau) S(E)
        -min{N beta_j/tau, sqrt(N) Gamma_(j,tau)}.       (4)

For the empty set this reads0<=W_*.
The frequencies h_j(eta) are distinct and strictly positive; only this paid positive first band is used for the lower bound on the full two-sided norm.
No optimality of E or completeness of the selected band is asserted.

Consequently a precise sufficient condition for a moving tau_j->0 is the existence of these finite E_j such that

    sqrt(tau_j) S(E_j) ->infinity,
    min{N_j beta_j/tau_j, sqrt(N_j)Gamma_(j,tau_j)}
                    =o(sqrt(tau_j)S(E_j)).              (5)

Condition(5) implies actual W_*(f_(j,tau_j))->infinity.
It is a sufficient condition, not an assumption supplied by the original family theorem.
The rest of this account proves(4), identifies its paid inputs and gives an explicit regime where this particular certificate cannot establish divergence.

<a id="moving-band-exact-alias"></a>
## 2. Exact growing frequency box from the original schedule

Write a,b,c,M for a fixed j.
If gamma is a nonzero integer vector with ||gamma||_infinity<=2M, then H_j(gamma)!=0.
Indeed, if gamma_3!=0, its c contribution dominates the remaining three because

    c>2M(1+a+b).

This follows from2M<=a/2 and c>(K+a+b+3)^2.
If gamma_3=0 and gamma_2!=0, use b>2M(1+a), which follows from b>(K+a+3)^2.
If only gamma_0,gamma_1 remain, use a>2M.
The final case gamma_0!=0 is immediate.
Thus for every trigonometric polynomial Q supported in[-M+1,M-1]^4 and every gamma in[-M,M]^4,

    integral Q(iota_j(z)) z^(-H_j(gamma)) dHaar(z)
                              =Qhat(gamma).             (6)

Every possible support difference lies in the just-proved2M box, and no nonzero one aliases to zero.
This includes exact equality of the circle and four-torus means.
For gamma=(eta,1), positivity of h_j(eta) follows from c>M(1+a+b); distinct eta give distinct frequencies by the same box argument.
No assertion about arbitrary original frequencies or a growing unbounded Fourier series is being made.
No upper prime-gap estimate is needed for(6).

<a id="moving-band-denominator"></a>
## 3. An explicit sublevel and regularization budget

Use C171's exact polynomials

    R=(z^K-1)(u-1)(v-1),
    Acal+Bcal=-zR,
    g=|Acal|^2+|Bcal|^2, Ncal=2 Acal conjugate(Bcal).

All are functions on the three-torus; g is real nonnegative and |Ncal|<=g.
The elementary square inequality gives g>=|R|^2/2.
If g<=s, at least one of the three factors in R has modulus at most(2s)^(1/6).
For a uniform circle point, the probability of distance at most t from1 is at most t for every t>=0.
For0<=t<=2 this follows from2 arcsin(t/2)/pi<=t, and for t>=2 it is immediate.
The map z to z^K preserves Haar measure, so the union bound proves

    nu_3{g<=s}<=3(2s)^(1/6), s>0.                    (7)

The bound may exceed1; this causes no problem.
It also directly confirms that {g=0} has Haar measure zero.
For0<rho<=1 put

    U_rho=Ncal/(g+rho), r_rho=rho/(g+rho), |U_rho|<=1.

On {g>0}, U=Ncal/g by equal modulus, and hence |U-U_rho|=r_rho.
On {g=0}, both phases are0 and the same inequality still holds.
Splitting into {g<=rho} and the shells2^k rho<g<=2^(k+1)rho, k>=0, gives

    integral r_rho dnu_3
      <=3*2^(1/6) rho^(1/6)
           [1+2^(1/6)/(1-2^(-5/6))]
      <=64 rho^(1/6).                                (8)

For the last convenient bound,3*2^(1/6)<=6,2^(1/6)<=2 and2^(-5/6)<=3/4 make the bracketed product at most54.
The infinite shell sum is convergent even when the sublevel estimate exceeds1.
No actual root-separation estimate or varying-dimensional source theorem is hidden in(8).

<a id="moving-band-fejer-budget"></a>
## 4. Finite Fejer approximation and complete composition costs

Angular derivatives use radians and are taken only in the first three torus coordinates.
Define the finite fixed constant

    A_K=1+||g||_infinity+||Ncal||_infinity
           +sum_(l=1)^3 (||partial_l g||_infinity
                                  +||partial_l Ncal||_infinity),
    D_K=8pi A_K^2.                                    (9)

These are supremum norms of fixed explicit trigonometric polynomials; no numerical value or unproved uniformity in K is needed.
Quotient differentiation gives sum_l ||partial_l U_rho||_infinity<=2 A_K^2/rho^2 and sum_l ||partial_l r_rho||_infinity<=A_K/rho.
Inversion of the three variables preserves these bounds.
Let Kcal_rho=(1-Re(w U_rho(z^-1,u^-1,v^-1)))/2 and F_(tau,rho)=psi_tau(Kcal_rho).
Both Kcal_rho and F_(tau,rho) take values in[0,1].
Including the w derivative, the sum of the coordinate Lipschitz constants for F_(tau,rho) is at most2 A_K^2/(tau rho^2).
The possible corner of psi_tau causes no difficulty because its global Lipschitz constant on[0,1] is1/tau.

For M>=2 let F_M be the probability-Haar Fejer kernel of degree M-1 and take its product in four variables.
C172's elementary first-moment bound, with c=M, is

    integral |t| F_M(t) dt/(2pi)
                         <=pi(1/2+log M)/M.

Successively changing the four coordinates and integrating the Lipschitz differences therefore bounds the uniform convolution error by D_K omega/(tau rho^2), where omega=(1+log M)/M.
The same argument bounds the convolution error of r_rho composed with inversion, independent of w, by D_K omega/rho^2.
These constants are deliberately larger than the coordinate sum requires.
If Q is the product Fejer convolution of F_(tau,rho), then

    0<=Q<=1,
    ||Q-F_(tau,rho)||_infinity<=D_K omega/(tau rho^2).

Write mu_j for circle Haar pushed forward by iota_j and nu for four-torus Haar.
Apply(6) to the product Fejer convolution of r_rho composed with inversion, then pay both uniform errors.
Equation(8) yields

    integral r_rho(z^-1,u^-1,v^-1) dmu_j
               <=64 rho^(1/6)+2D_K omega/rho^2.          (10)

Moreover |F_tau-F_(tau,rho)|<=r_rho(z^-1,u^-1,v^-1)/(2tau).
The original error(2), the1/tau Lipschitz constant, the two regularization terms and both Q approximation errors now give, for every gamma in[-M,M]^4,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=[epsilon_j+64 rho^(1/6)+3D_K omega/rho^2]/tau.  (11)

Here M=M_j; the intermediate Q coefficient is EXACTLY the same in both spaces by(6).
Thus(11) pays a full-function comparison before summing any coefficients.
With rho=omega^(6/13), which lies in(0,1) for M>=2, both rho^(1/6) and omega/rho^2 equal delta=omega^(1/13).
This proves the individual beta_j/tau bound in(3).

There is a useful finite quadratic improvement.
For E as in Section1, the characters at h_j(eta) are orthonormal on the original circle and those at(eta,1) are orthonormal on the four-torus.
The finite Bessel inequality follows directly by subtracting the corresponding finite orthogonal projection and taking its nonnegative squared norm.
For classical attribution, this is the finite orthogonality inequality underlying the probability-Haar Parseval interface already checked in [C174](Yin_C_G0174_v1.md#narrow-contact-source-interface).
Only the displayed finite projection calculation is required here; no new complete-basis or original-source proof claim is made.
Apply it separately to f_(j,tau)-Q composed with iota_j and F_tau-Q, then use the triangle inequality in the finite coefficient space.
All actual and regularized functions take values in[0,1], so a difference has its L2 norm squared bounded by its L1 norm.
The original composition term has L2 norm at most sqrt(epsilon_j/tau); the two regularization terms have L2 norms bounded by the square roots of the respective bounds in(8),(10) after division by2tau inside each square root.
The two Q errors retain their uniform bounds.
After the same rho choice this gives

    [sum_(eta in E)
       |fhat_(j,tau)(h_j(eta))-Fhat_tau(eta,1)|^2]^(1/2)
       <=sqrt(epsilon_j/tau)
          +2sqrt([64+2D_K]delta_j/(2tau))
          +2D_K delta_j/tau
       <=3sqrt(beta_j/tau)+beta_j/tau.                 (12)

Cauchy--Schwarz then bounds the total absolute coefficient error by sqrt(N)Gamma_(j,tau).
Summing(11) instead bounds it by N beta_j/tau.
Both are valid finite estimates, so the smaller may be selected without any limiting exchange.

<a id="moving-band-scalar-coefficient"></a>
## 5. Exact first phase band and its shrinking coefficient

Let a_1(tau) be the first Fourier coefficient of theta mapped to psi_tau((1-cos theta)/2).
Translation to u=theta-pi gives the cap

    g_tau(u)=(1-sin(u/2)^2/tau)_+.

For0<tau<=1/4 its support is |u|<=2 arcsin sqrt(tau)<=pi/3, so cos u>=1/2 on that support.
Thus a_1(tau) is negative real.
On |u|<=sqrt(tau), sin(u/2)^2<=tau/4 and g_tau>=3/4.
The normalized integral over this smaller interval proves

    3sqrt(tau)/(8pi)<=|a_1(tau)|<=sqrt(tau).            (13)

For the upper bound use |a_1|<=a_0 and the support measure2 arcsin sqrt(tau)/pi<=sqrt(tau).
For almost every three-torus point, |V|=1.
Changing the w angle by the phase of V and integrating the w character gives

    Fhat_tau(eta,1)=a_1(tau) Vhat(eta)
                             =a_1(tau) Uhat(-eta).     (14)

The minus sign in the phase index is essential for the retained inverse orientation.
The common-zero set has Haar measure zero and does not alter(14).
Combining(11)--(14), and retaining the distinct positive original frequencies supplied by(6), proves(4) with no additional factor of2.
The full W_* includes these coefficients and their negative counterparts; using only one band is sufficient for this lower bound.

<a id="moving-band-method-boundary"></a>
## 6. What the original schedule supplies and an explicit limitation of this certificate

The actual L402 schedule supplies M_j->infinity, exact alias exclusion(6), epsilon_j->0 and therefore beta_j->0.
The remaining quantity S(E) is a finite coefficient sum of ONE FIXED three-torus phase, with K fixed.
C171 proves its full l1 sum infinite by failure of a continuous representative and Fourier uniqueness.
It supplies no quantitative growth rate of the partial sums that would imply(5) for an arbitrary moving tau_j.
The present estimate likewise does not produce that rate.
Even after a rate is available, the number of selected coefficients and the two displayed error prices must still be paid.

A precise method boundary follows without any new arithmetic input.
Since |U|=1 almost everywhere, finite Bessel and monotone limits give

    sum_(eta in Z^3)|Uhat(eta)|^2<=1,
    S(E)<=sqrt(N),
    sup_(|E|=N) S(E)/sqrt(N) ->0 as N->infinity.        (15)

Only Bessel is needed; equality in Parseval is unnecessary.
For the last limit, choose a fixed finite coefficient set whose squared tail sum is below epsilon^2.
Every N-element set contributes at most the fixed core's l1 sum plus epsilon sqrt(N).
Divide by sqrt(N), let N grow, then epsilon decrease to zero.

Consider a diagonal tau_j->0 with liminf beta_j/tau_j^2>0.
Write c_*=3/(8pi).
The right side of(4) is the maximum of its two separate lower certificates.
The coefficient-by-coefficient one satisfies, uniformly over E,

    c_* sqrt(tau_j) S(E)-N beta_j/tau_j
       <=c_* sqrt(tau_j) sqrt(N)-N beta_j/tau_j
       <=c_*^2 tau_j^2/(4beta_j).                     (16)

It is therefore bounded above along this diagonal.
For the Bessel certificate, positivity would require

    S(E)/sqrt(N)>Gamma_(j,tau_j)/(c_* sqrt(tau_j))
                              >=3sqrt(beta_j)/(c_* tau_j).

The last term is bounded below by a fixed positive constant for all sufficiently large j.
By(15), only uniformly bounded N can satisfy that requirement.
For those N, its positive part is at most c_*sqrt(tau_j N), which tends to zero.
Thus the Bessel certificate also cannot establish divergent lower bounds in this regime.
The maximum of the two certificates in(4) consequently cannot prove divergence when liminf beta_j/tau_j^2>0.
This is a rigorous limitation of THESE displayed sufficient estimates, not an upper bound on actual W_*, a bounded-Wiener construction, or a necessary condition for actual divergence.

In particular the present explicit error scale separates a potentially accessible slow corridor from a remaining faster one, but is not an asserted physical transition width.
Even beta_j/tau_j^2->0 alone does not prove(5); quantitative static phase mass and its support expense remain additional obligations.
C174's fixed-j then tau-to-zero result can handle suitably chosen very thin widths by a different order of limits, and C173 covers widths bounded below.
Neither is silently exchanged with the simultaneous regime here.
The actual margin stays at least1/2 throughout, but it does not pay the Fourier expenses.
No near-one counterexample or unrestricted Mahler conclusion follows from this bounded-positive-measure family.

<a id="moving-band-inputs"></a>
## Exact inputs and author limits

| Input | Actual role |
| --- | --- |
| [L402 original schedule](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-schedule) | Fixed K, actual primes and original irreducible P_j, original degree d and2d window and positive total-measure boundary; no schedule acceleration or new prime theorem. |
| [C158 original kernel](Yin_C_G0158_v1.md#statement) | Actual residual projection, range and Haar mean; no cyclic replacement of the original norm. |
| [C171 exact phase](Yin_C_G0171_v1.md#two-block-torus-phase) | Fixed Acal/Bcal, equal modulus, common zeros, inverse-oriented phase and qualitative non-l1 conclusion; no quantitative partial-sum rate. |
| [C172 L1 return](Yin_C_G0172_v1.md#moving-cubic-original-l1-return) | Exact epsilon_j including original rank-three, boundary, missing mode and normalization costs; reused before nonlinear composition. |
| [C172 Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Complete elementary probability-Haar first-moment estimate; new product approximation and alias box are proved here. |
| [C174 contact limits](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Fixed-input full-Wiener limit, finite norm, automatic contact margin and explicit arbitrary-diagonal boundary; no uniform thin threshold. |
| [C174 Parseval attribution](Yin_C_G0174_v1.md#narrow-contact-source-interface) | Existing selected Tao09 probability-Haar scope supplies classical attribution; the finite orthogonal projection inequalities used here are proved directly, without a new source-proof audit. |
| [C173 scalar theorem](Yin_C_G0173_v1.md#scalar-transform-statement) | Comparison for a fixed lower width only; unbounded1/tau is not passed through its uniform-Lipschitz theorem. |
| [L179 quantitative comparison](../ledger/Yin_L_G0179_v1.md) | Section4's strict full-torus modulus and explicit finite averaging bound; comparison only, not a singular-phase rate premise. |
| [C137 finite no-alias comparison](Yin_C_G0137_v1.md#argument) | Fixed finite support and N>3J exact constant-coefficient mechanism; comparison only, not the present growing-box statement. |
| [R417](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding), [R420](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding), [R430](../audits/reviews/Yin_R_G0430_v1.md#scalar-transform-whole-independent-finding), [R434](../audits/reviews/Yin_R_G0434_v1.md#narrow-contact-whole-independent-finding) | Actual independent scopes for this author's upstream contributions; not a review of the present quantitative extension. |

The proof of(4) and the limitation of that particular certificate are complete author results; condition(5) for arbitrary moving widths remains unresolved.
No computation or new external source theorem is used.

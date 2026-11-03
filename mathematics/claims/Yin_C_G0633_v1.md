---
author: Yin
---

# Exact phase integration and a two-sevenths original contact corridor

Human author Yin.
Root supplied the exact one-coordinate integral and the central/noncancellation/cancellation decomposition.
Paid_comparison checked the phase identity and developed the explicit constants, the uniform treatment of the correlated shift, the balanced regularization budget and the complete original finite-support consumer.
Both are contributors, not independent reviewers.
The accepted C632 amplitude-derivative and original-window interfaces and C629v3 finite unequal-cutoff theorem retain their exact source and review scopes.
The new probability, regularization and original finite-support argument is supplied completely below.
No numerical experiment, new external theorem or source acquisition is used.

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
For every actual j with M_j>=2 put omega_j=(1+log M_j)/M_j.
Define the fixed original-polynomial constants

    A_der,K=1+sum_(l=1)^3(||partial_l Acal||_infinity
                                  +||partial_l Bcal||_infinity),
    D_reg,K=4pi A_der,K.

All logarithms are natural and log_+(s)=max(0,log s).
Write nu_3 for normalized three-torus Haar measure.
For every 0<rho<=1 put r_rho=rho/(g+rho).
Fix regular z=exp(i theta),u and, for regular v, define

    x=cot(K theta/2), y=cot(arg(u)/2), t=cot(arg(v)/2),
    b_theta=4sin theta, A0=(1+x^2)(1+y^2), q=rho A0,
    D=x+y+b_theta.

Then the exact normalized v integral is

    average_v r_rho
      =q/sqrt((32+q)^2+32qD^2).                                  (EI1)

The shift b_theta is generally correlated with x.
No independence between them is assumed.
For every 0<rho<=1 and every s>0,

    integral r_rho dnu_3<=5rho^(2/3)[1+log(1/rho)],
    nu_3{g<=s}<=min{1,10s^(2/3)[1+log_+(1/s)]}.                   (EI2)

The derivative constants from the same actual polynomial amplitudes remain exactly A_der,K and D_reg,K defined above.
Put

    U_rho=Ncal/(g+rho), V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),
    f_(j,tau)=psi_tau(k_j), iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

For every actual j with M_j>=2, every 0<tau<=1, every 0<rho<=1 and every gamma in [-M_j,M_j]^4 intersect Z^4,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
      <=[epsilon_j+5rho^(2/3)(1+log(1/rho))
                    +3D_reg,K omega_j/sqrt(rho)]/tau.             (EI3)

Both Fourier coefficients use probability Haar measure, the stated sign convention and the same complete original 2d_j window.
Set

    h_j=1+log(1/omega_j), rho_j=(omega_j/h_j)^(6/7),
    beta_int,j=epsilon_j+(60/7+3D_reg,K)omega_j^(4/7)h_j^(3/7).

Here h_j is only a scalar logarithmic budget, not an original frequency.
Then (EI3) is at most beta_int,j/tau throughout the complete same box, and

    beta_int,j=O_K(M_j^(-4/7)(1+log M_j)).                          (EI4)

For the finite original Wiener consumer, put delta_0=pi/(4K) and, for integers R_z,R_u>=2,J>=2,L>=1, define

    T_K(R_z,R_u,J,L)
      =8192pi J(L+J)(1/2+log R_u)/R_u
         +pi(K+4)(1/2+log R_z)/R_z+2pi J/(R_z delta_0).

For every sufficiently large actual j and every 0<tau<=1/64 use L_tau=floor(1/(4sqrt(tau))).
Whenever R_z,R_u,J,L_tau<=M_j and T_K(R_z,R_u,J,L_tau)<=1/16, the complete original kernel satisfies

    W_*(psi_tau(k_j))
      >=3log(J+1)/(1024pi)-R_z R_u J beta_int,j/tau^(3/2).          (EI5)

Consequently fix any real eta with 0<eta<2/7 and put

    Delta=4/7-2eta>0, zeta=Delta/10>0.

There exist j0 and C depending only on eta,K such that for every j>=j0 and every width M_j^(-eta)<=tau<=1/64,

    W_*(psi_tau(k_j))
      >=[3zeta/(1024pi)]log M_j
           -C M_j^(-Delta/2)(1+log M_j).                           (EI6)

In particular every sequence tau_j->0 satisfying tau_j>=M_j^(-eta) eventually has W_*(psi_(tau_j)(k_j))->infinity.
Entry into the upper cutoff may have a sequence-dependent index, while (EI6) is uniform throughout the stated strip.
All actual fixed-j norms remain finite, the original contact-minus-Haar margin remains at least 1/2, and the same original input family has log2<m(P_j)<log4.
No assertion is made at eta=2/7, below all such corridors, about an arbitrary simultaneous thin-width limit, or about a near-one family or the unrestricted Mahler gap.
The exponent 2/7 is sufficient for these estimates, not a necessary transition or an optimality claim.

## Reuse and source boundary

Before deriving the new bound, the complete actual C632 statement and proof, C629v3 original phase and finite unequal-cutoff theorem, C565v2 denominator/alias/return chain and C569v2 original schedule costs were read.
A focused local search for cotangent coordinates, one-coordinate integration and cancellation tails found the exact elementary cotangent-Haar substitution in C629v3 but no existing bound at this scope.
The new exact quadratic integral, regions, logarithmic bounds and constants are proved directly below.
The accepted C632 amplitude-derivative estimates and C629v3 finite coefficient-sum theorem supply their exact previously checked interfaces.
Their classical source and historical SELF/UNKNOWN review scopes are unchanged.
No independent original-circle coordinates, external convolution theorem, general sublevel theorem or unproved root-separation estimate is used.

## Complete argument

### 1. Exact original phase and normalized one-coordinate integration

Away from the null sets z^K=1,u=1,v=1, put C(w)=(w+1)/(w-1).
The actual polynomial definitions give

    Acal+Bcal=-zR,
    Acal-Bcal=zR[-2(z-z^-1)+C(z^K)+C(u)+C(v)].

For unit-circle points C(exp(i alpha))=-i cot(alpha/2) and z-z^-1=2i sin theta.
Thus the bracket is -i(x+y+t+b_theta).
The parallelogram identity and |z|=1 imply

    g=(|Acal+Bcal|^2+|Acal-Bcal|^2)/2
      =|R|^2[1+(t+D)^2]/2
      =32[1+(t+D)^2]/[A0(1+t^2)].                                (EI7)

The last step retains all three factors |exp(i alpha)-1|^2=4/(1+cot^2(alpha/2)).
The ignored coordinate sets have product Haar measure zero.
The continuous function r_rho is still defined there, so this restriction changes no integral.

Under normalized v-circle Haar, t=cot(arg(v)/2) has density 1/[pi(1+t^2)] by direct angular substitution.
The factor 1+t^2 in r_rho cancels this density exactly, giving

    average_v r_rho
      =(q/pi) integral_R dt/[32(1+(t+D)^2)+q(1+t^2)].

Let a=32+q and V=a^2+32qD^2>0.
The denominator is

    a t^2+64Dt+32(1+D^2)+q
      =a(t+32D/a)^2+V/a.

The change of variable s=(a t+32D)/sqrt(V) reduces its integral to pi/sqrt(V), using the antiderivative arctan(s).
This proves (EI1) without an external integral or convolution theorem.

Under product z,u Haar, x=cot(K theta/2) and y=cot(arg(u)/2) are independent with the density p(t)=1/[pi(1+t^2)].
Indeed z to z^K preserves circle Haar, and u is an independent coordinate.
The shift b_theta depends on theta and need not be determined by x alone.
All bounds below either remove b_theta pointwise or hold uniformly in it for fixed theta before integrating in theta.
Only |b_theta|<=4 is used.
No such product law is assigned to the pushed original circle.

### 2. An explicit two-region tail estimate

Write

    H(q,D)=q/sqrt((32+q)^2+32qD^2).

For q>0, H<=1, H<=q/32 and, when D!=0,

    H<=sqrt(q)/(sqrt(32)|D|).

For fixed D the function H is increasing in q because

    partial_q H
      =[1024+32q+16qD^2]/[(32+q)^2+32qD^2]^(3/2)>0.              (EI8)

Fix any T>=16.
In the central square |x|,|y|<=T, the bound H<=rho(1+x^2)(1+y^2)/32 cancels the two probability densities.
Consequently its contribution is at most

    rho T^2/(8pi^2).                                               (EI9)

In the remaining region put M=max(|x|,|y|)>=T and D=x+y+b_theta.
First consider |D|>=M/4.
Pointwise, uniformly in theta and its shift,

    H<=sqrt(rho)(1+x^2)^(1/2)(1+y^2)^(1/2)/(sqrt(2)M).

After inserting the independent x,y densities this has integral at most

    sqrt(rho)/(sqrt(2)pi^2)
      integral_(M>=T) dx dy/[M sqrt(1+x^2)sqrt(1+y^2)]
      =4sqrt(2)sqrt(rho)/pi^2
          integral_T^infinity asinh(x) dx/[x sqrt(1+x^2)]
      <=4sqrt(2)sqrt(rho)[1+log(3T)]/(pi^2 T).                    (EI10)

To obtain the equality, split into the two regions where |x| or |y| is maximal and their two signs, and use integral_(-x)^x (1+y^2)^(-1/2)dy=2asinh(x).
For x>=T>=1, asinh(x)<=log(3x), x sqrt(1+x^2)>=x^2 and integral_T^infinity log(3x)x^-2 dx=[1+log(3T)]/T.
The bounded shift no longer appears, so the product-density integration is justified despite its correlation with x.

It remains to bound the cancellation region |D|<M/4.
Since |b_theta|<=4<=M/4, one has |x+y|<M/2.
Hence x and y have opposite signs, min(|x|,|y|)>M/2, and in particular

    |x|>=T/2, |x|/2<=|y|<=2|x|, |D|<=|x|/2.                     (EI11)

Fix theta, so x and b_theta are fixed while y varies.
The y density is at most 4/(pi x^2).
Moreover q=rho(1+x^2)(1+y^2)<=10rho x^4=:Q because |x|>=T/2>=8.
By (EI8), replacing q by Q can only increase H.
The change of variable D=x+y+b_theta has derivative one, and enlarging the allowed interval of D gives

    integral_(cancellation y) H(q,D) p(y)dy
       <=4/(pi x^2) integral_(-|x|/2)^(|x|/2) H(Q,D)dD.           (EI12)

Direct integration of this last square root yields

    integral_(-s)^s H(Q,D)dD
       =2sqrt(Q/32) asinh(s sqrt(32Q)/(32+Q)).

The inequality 32+Q>=2sqrt(32Q) bounds the argument, for s=|x|/2, by |x|/4.
Thus (EI12) is at most

    [2sqrt(5)/pi]sqrt(rho) asinh(|x|/4).

This bound holds for every theta and every corresponding b_theta.
Only now push theta Haar through x and use its Cauchy density.
Since |x|>=T/2, the total cancellation contribution is at most

    4sqrt(5)sqrt(rho)/pi^2
        integral_(T/2)^infinity asinh(x/4)/(1+x^2) dx
       <=8sqrt(5)sqrt(rho)[1+log(T/2)]/(pi^2 T).                  (EI13)

Here asinh(x/4)<=log(1+x/2)<=log x for x>=T/2>=8, and 1+x^2>=x^2.
No symmetry or independence of the actual shift has been used in this step.

Combining (EI9)--(EI13), and using

    (4sqrt(2)+8sqrt(5))/pi^2<3,

gives the complete estimate

    integral r_rho dnu_3
      <=rho T^2/(8pi^2)
            +3sqrt(rho)[1+log(3T)]/T, T>=16.                     (EI14)

The displayed constant follows already from sqrt(2)<3/2, sqrt(5)<9/4 and pi>3.
Choose T=16rho^(-1/6), legal for every 0<rho<=1.
Then (EI14) is at most

    rho^(2/3){32/pi^2+(3/16)[1+log48]+(1/32)log(1/rho)}
       <=5rho^(2/3)[1+log(1/rho)].

For the last numerical inequality, pi>3 and log48<4 give the constant part at most 32/9+15/16=647/144<5, while 1/32<=5.
One elementary check of log48<4 is exp(1)>1+1+1/2+1/6=8/3 and (8/3)^4>48.
This proves the first part of (EI2) with an absolute constant independent of K.
For 0<s<=1, r_s>=1/2 on g<=s, so the second part follows with factor two and the trivial probability upper bound one.
For s>1 the displayed minimum is one.
This also confirms that g=0 has product Haar measure zero.

### 3. Complete original coefficient return and the balanced parameter

Use the adopted C632 amplitude estimate on the SAME actual Acal,Bcal:

    sum_l ||partial_l U_rho||_infinity,
    sum_l ||partial_l r_rho||_infinity
        <=2A_der,K/sqrt(rho).

These are the three angular derivative sums and include all common-zero points.
Under inversion the bounds are unchanged.
The associated F_(tau,rho)=psi_tau((1-Re(w U_rho(inverse coordinates)))/2) has sum of its four coordinate Lipschitz constants at most (A_der,K+1/2)/(tau sqrt(rho)).
The fourth coordinate is included.
The normalized product Fejer convolution of degree M_j-1 consequently has errors at most

    D_reg,K omega_j/(tau sqrt(rho)) for F_(tau,rho),
    D_reg,K omega_j/sqrt(rho) for r_rho.

These are exactly the accepted constants and finite kernels of C632, using C172's normalized first moment.

Let B_rho=5rho^(2/3)[1+log(1/rho)] and E_rho=D_reg,K omega_j/sqrt(rho).
The same exact C565 no-alias theorem identifies the mean of the r_rho Fejer polynomial under original-circle pushforward and product Haar.
Paying both uniform errors gives

    integral r_rho(inverse coordinates)dmu_j<=B_rho+2E_rho.

The product-Haar integral is at most B_rho.
The two differences between F_tau and F_(tau,rho) have combined Fourier error at most

    [(B_rho+2E_rho)+B_rho]/(2tau)
       =(B_rho+E_rho)/tau.

The two F_(tau,rho) Fejer approximation errors contribute another 2E_rho/tau.
The intermediate finite polynomial coefficients agree exactly for every gamma in the original complete box.
Finally the original full-window estimate ||k_j-Kcal composed with iota_j||_1<=epsilon_j and the 1/tau Lipschitz constant of psi_tau contribute epsilon_j/tau.
Their sum is (EI3).
In particular no product independence has been assigned to mu_j.

For M_j>=2 one has 0<omega_j<1; the function (1+log M)/M is decreasing for M>1 and its value at2 is below1.
Let h=1+log(1/omega)>=1 and rho=(omega/h)^(6/7).
This rho lies in (0,1).
Since log h<=h-1,

    1+log(1/rho)
       =1+(6/7)[log(1/omega)+log h]
       <=(12/7)h.

Therefore

    5rho^(2/3)[1+log(1/rho)]
       <=(60/7)omega^(4/7)h^(3/7),
    3D_reg,K omega/sqrt(rho)
       =3D_reg,K omega^(4/7)h^(3/7).

This proves the explicit beta_int budget.
Also h=1+log M-log(1+log M)<=1+log M, so

    omega^(4/7)h^(3/7)<=M^(-4/7)(1+log M).

The actual square-separated schedule has epsilon_j=O_K((1+log M_j)/M_j^2), by the adopted C569v2 calculation.
It uses no upper prime-gap estimate.
This proves (EI4); no optimality of the balancing parameter or logarithmic factor is asserted.

### 4. Every selected coefficient and the uniform original width strip

Use the adopted C629v3 unequal-cutoff theorem with the unchanged explicit T_K in the statement.
Under T_K<=1/16 its negative-v band coefficients satisfy, for every 1<=k<=L_tau,

    sum_(|p|<=R_z-1,|q|<=R_u-1,1<=m<=J)
         |(U^k)hat(p,q,-m)|>=log(J+1)/16.

The same scalar cap coefficients obey |a_k(tau)|>=3sqrt(tau)/(8pi), L_tau sqrt(tau)>=1/8 and 4L_tau<=1/sqrt(tau).
The exact inverse-phase identity is Fhat_tau(eta,k)=a_k(tau)(U^k)hat(-eta).
Select all four-dimensional frequencies

    G={(eta,k): -eta=(p,q,-m),
          |p|<=R_z-1, |q|<=R_u-1, 1<=m<=J, 1<=k<=L_tau}.

There are at most 4L_tau R_z R_u J coefficients.
All lie in the original four-box when the stated cutoffs do.
Their H_j frequencies are pairwise distinct by the complete 2M_j no-alias difference box, and all are strictly positive because c_j>M_j(1+a_j+b_j) and k>=1.
Thus none is the omitted zero coefficient of W_*.
Summing the triangle inequality with the full beta_int,j/tau cost for EVERY member gives

    W_*(psi_tau(k_j))
       >=[3/(8pi)]sqrt(tau)L_tau log(J+1)/16
             -4L_tau R_z R_u J beta_int,j/tau
       >=3log(J+1)/(1024pi)
             -R_z R_u J beta_int,j/tau^(3/2).

This is (EI5), and no infinite Fourier sum was compared termwise.
No extra factor from unused negative frequencies is claimed.

Fix 0<eta<2/7 with Delta,zeta as stated and choose the scalar cutoffs

    Q_z,j=floor(M_j^(2zeta)),
    Q_u,j=floor(M_j^(eta/2+2zeta)),
    J_j=floor(M_j^zeta).

Set R_z=Q_z,j, R_u=Q_u,j, J=J_j and L=L_tau.
These scalars do not rename the original projection R_j or the schedule length L_j.
Uniformly for M_j^(-eta)<=tau<=1/64, one has L_tau<=M_j^(eta/2)/4.
All cutoff exponents are positive and below one; in particular eta/2+2zeta=4/35+eta/10<1.
The scalar cutoffs eventually satisfy their lower bounds and remain at most M_j, as does L_tau.

Using floor x>=x/2 for x>=2, the three terms of T_K are bounded by fixed multiples of

    [M_j^-zeta+M_j^(-eta/2)](1+log M_j),
    M_j^(-2zeta)(1+log M_j),
    M_j^-zeta,

respectively.
For the first term the two differences of exponents are -zeta and -eta/2.
All tend to zero, uniformly over the width strip, so T_K<=1/16 after a threshold depending only on eta,K.
The entire original coefficient price satisfies

    Q_z,j Q_u,j J_j beta_int,j/tau^(3/2)
       =O_K(M_j^(2eta+5zeta-4/7)(1+log M_j))
       =O_K(M_j^(-Delta/2)(1+log M_j)).

Here 2eta-4/7=-Delta and 5zeta=Delta/2.
All numerator floors only decrease this upper bound.
Since J_j+1>M_j^zeta, (EI5) proves (EI6) with uniform constants.
Every stated shrinking sequence eventually enters the upper cutoff, and its assumed lower inequality then places it in that same strip.

The phase and coefficient improvements do not change the original arithmetic family, original contact margin or finite fixed-input Wiener norms.
The logarithm in (EI2), the optimal decay rate and endpoint eta=2/7 are not resolved by this argument.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision exact-phase-integration-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:01 |
| status | open |
| reason | Register the complete original one-coordinate integral, uniform correlated-shift tail estimate with explicit constant5, all-rho original4box return, balanced M^(-4/7)(1+logM) budget and fully paid unequal-cutoff corridor for every fixed exponent below2/7. Root and paid_comparison are contributors. Fresh isolated whole review and adoption remain separate. No original-circle independence, endpoint/optimality conclusion, near-one family or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | EI1--EI6 with every actual original input and degree, normalized Haar law, finite coefficient box, regularization constant, width quantifier and limit. |
| argument | [Complete phase-integral and original-return proof](#complete-argument) | Exact cotangent substitution and quadratic integral, central/noncancellation/cancellation estimates with the correlated shift handled conditionally, all constants, derivative and five comparison costs, finite frequency selection and uniform strip. |
| dependency | [Actual polynomial amplitudes and regularization](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same Acal,Bcal,g,Ncal, A_der,K,D_reg,K and complete rho^(-1/2) angular derivative/Fejer bounds, including zeros and inversion. |
| dependency | [Complete original input and projection](Yin_C_G0565_v2.md#statement) | Actual fixed K and prime schedule, monic irreducible Salem P_j, full degree and 2d_j coefficient residual projection/kernel. |
| dependency | [Original denominator and inverse phase](Yin_C_G0565_v2.md#moving-band-denominator) | Same polynomial identity, equal modulus, U=Ncal/g off the common-zero set and original phase conventions; the new exact integral is proved here. |
| dependency | [Complete finite original return interface](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Original epsilon_j, both regularization comparisons, both product-Fejer errors and exact Fourier signs, with new probability and derivative budgets supplied explicitly here. |
| dependency | [Every original finite alias](Yin_C_G0565_v2.md#moving-band-exact-alias) | Exact full4box coefficient equality, complete2M_j difference exclusion and positivity of selected original frequencies. |
| dependency | [Adopted unequal-cutoff phase theorem](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Same actual witness phase, finite T_K condition and band coefficient lower bound (D), with the whole original frequency selection (26); no enlarged scope of any historical source proof. |
| dependency | [Scalar harmonics and inverse-phase coefficients](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bound, L_tau bounds, Fourier phase inversion and finite coefficient sum, with every selected coefficient paid by the new EI3. |
| dependency | [Actual schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K((1+log M_j)/M_j^2) using only lower square prime separations, without an upper prime-gap estimate. |
| dependency | [Normalized finite Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Probability-Haar kernels and their first moment at the accepted interface already used by C632. |
| dependency | [Original contacts and fixed-input norm limits](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual margin at least1/2 and finite Wiener norm at every fixed original j,tau, with the original order-of-limits restriction retained. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:09 |
| status | proved |
| reason | Adopt the entire exact phase-integral and original-return theorem after main reading of the fixed C and independent whole R838. The conditional correlated-shift argument, constant5, every original4box coefficient cost and entire unequal-cutoff consumer support the stated strict two-sevenths corridor. All original-family, source-review, sequence-entry and full2d normalization boundaries remain; no endpoint, optimality or unrestricted Mahler conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | EI1--EI6 with every actual original input and degree, normalized Haar law, finite coefficient box, regularization constant, width quantifier and limit. |
| argument | [Complete phase-integral and original-return proof](#complete-argument) | Exact cotangent substitution and quadratic integral, central/noncancellation/cancellation estimates with the correlated shift handled conditionally, all constants, derivative and five comparison costs, finite frequency selection and uniform strip. |
| dependency | [Actual polynomial amplitudes and regularization](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same Acal,Bcal,g,Ncal, A_der,K,D_reg,K and complete rho^(-1/2) angular derivative/Fejer bounds, including zeros and inversion. |
| dependency | [Complete original input and projection](Yin_C_G0565_v2.md#statement) | Actual fixed K and prime schedule, monic irreducible Salem P_j, full degree and 2d_j coefficient residual projection/kernel. |
| dependency | [Original denominator and inverse phase](Yin_C_G0565_v2.md#moving-band-denominator) | Same polynomial identity, equal modulus, U=Ncal/g off the common-zero set and original phase conventions; the new exact integral is proved here. |
| dependency | [Complete finite original return interface](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Original epsilon_j, both regularization comparisons, both product-Fejer errors and exact Fourier signs, with new probability and derivative budgets supplied explicitly here. |
| dependency | [Every original finite alias](Yin_C_G0565_v2.md#moving-band-exact-alias) | Exact full4box coefficient equality, complete2M_j difference exclusion and positivity of selected original frequencies. |
| dependency | [Adopted unequal-cutoff phase theorem](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Same actual witness phase, finite T_K condition and band coefficient lower bound (D), with the whole original frequency selection (26); no enlarged scope of any historical source proof. |
| dependency | [Scalar harmonics and inverse-phase coefficients](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bound, L_tau bounds, Fourier phase inversion and finite coefficient sum, with every selected coefficient paid by the new EI3. |
| dependency | [Actual schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K((1+log M_j)/M_j^2) using only lower square prime separations, without an upper prime-gap estimate. |
| dependency | [Normalized finite Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Probability-Haar kernels and their first moment at the accepted interface already used by C632. |
| dependency | [Original contacts and fixed-input norm limits](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual margin at least1/2 and finite Wiener norm at every fixed original j,tau, with the original order-of-limits restriction retained. |
| review | [Independent whole exact-phase finding](../audits/reviews/Yin_R_G0838_v1.md#exact-phase-integration-whole-independent-finding) | Entire EI1--EI6 and EI7--EI14 proof, actual normalized cotangent integral and correlated shift, every regional constant and five comparison costs, complete original support and uniform width/sequence quantifiers; exact upstream source-original, SELF and UNKNOWN limits retained. |


---
author: Yin
---

# Finite quadratic Fourier return at the contact scale

Human author Yin.
Root proposed the contact-scale regularization and complete finite quadratic comparison.
The phase_bands contributor checked and developed every pointwise, original-law, finite-projection and support estimate below.
Both are contributors; this initial fixed material is open pending an independent whole review.
The exact adopted C633v2 logarithm-free probability interface and the earlier source/review boundaries are retained.
No numerical experiment, new source acquisition or formal verification is used.

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

For 0<s<=1 put r_s=s/(g+s), and set U_s=Ncal/(g+s).
Define, with all Fourier conventions as above,

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal(z,u,v,w)=(1-Re(wV(z,u,v)))/2,
    F_tau=psi_tau(Kcal), f_(j,tau)=psi_tau(k_j),
    iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

For EVERY actual j with M_j>=2, EVERY 0<tau<=1/64, EVERY 0<lambda<=1 and EVERY finite set Gamma contained in [-M_j,M_j]^4 intersection Z^4, put rho=tau lambda.
Then the complete finite coefficient-error vector satisfies

    [sum_(gamma in Gamma)
       |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|^2]^(1/2)
       <=E_2(j,tau,lambda),                                      (Q1)

where the explicit bound is

    E_2(j,tau,lambda)
       =sqrt(epsilon_j/tau)+8lambda^(1/3)
          +2sqrt(D_reg,K)sqrt(omega_j)lambda^(-1/4)
          +2D_reg,K omega_j/(tau sqrt(rho)).                      (Q2)

This bound includes the empty Gamma case.
The original frequencies H_j(gamma) are distinct for every such set, including sets using several positive, negative or zero fourth-coordinate harmonics.
No infinite coefficient sum or first-harmonic restriction is used.

If omega_j<=tau^(3/2), the legal choice

    lambda_bal=(omega_j/tau^(3/2))^(6/5), rho_bal=tau lambda_bal

gives the explicit bound

    E_2(j,tau,lambda_bal)
       <=sqrt(epsilon_j/tau)
          +(8+2D_reg,K)omega_j^(2/5)tau^(-3/5)
          +2sqrt(D_reg,K)omega_j^(1/5)tau^(9/20)
       =:E_bal(j,tau).                                           (Q3)

The term sqrt(epsilon_j/tau) uses the true original L1 comparison, not a pointwise original-kernel error.

For the finite original Wiener consumer, let delta_0=pi/(4K), and for integers R_z,R_u>=2,J>=2,L>=1 put

    T_K(R_z,R_u,J,L)
       =8192pi J(L+J)(1/2+log R_u)/R_u
          +pi(K+4)(1/2+log R_z)/R_z
          +2pi J/(R_z delta_0).

Use L_tau=floor(1/(4sqrt(tau))).
For every sufficiently large actual j, every 0<tau<=1/64 and every 0<lambda<=1, if
R_z,R_u,J,L_tau<=M_j and T_K(R_z,R_u,J,L_tau)<=1/16, then

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)
          -2sqrt(L_tau R_z R_u J)E_2(j,tau,lambda).               (Q4)

All coefficients in the actual selected rectangle are paid.
When omega_j<=tau^(3/2), the same estimate holds with E_bal(j,tau) in place of E_2 and the balanced choice of lambda.

Consequently fix ANY real 0<theta<4/11, and define

    Delta_theta=2/5-11theta/10>0,
    zeta_theta=Delta_theta/10>0,
    sigma_theta=min(3Delta_theta/4,1/10)>0.

There exist j0 and C_error depending only on theta,K such that, for EVERY j>=j0 and EVERY width M_j^-theta<=tau<=1/64,

    W_*(psi_tau(k_j))
       >=[3zeta_theta/(1024pi)]log M_j
          -C_error M_j^-sigma_theta(1+log M_j)^(1/2).              (Q5)

Thus every sequence tau_j->0 eventually satisfying tau_j>=M_j^-theta has actual original Wiener norms tending to infinity.
The entry index into the strip may depend on the sequence; (Q5) is uniform within the strip.
For example theta=1/3 is included and exceeds the previously established strict range eta<2/7 from C633v2.
The equality theta=4/11, arbitrary faster thinning and optimality of this sufficient exponent are not asserted.
Every original fixed-j Wiener norm remains finite and the actual contact-minus-Haar margin remains at least 1/2.
The family still has log 2<m(P_j)<log 4, so this does not supply a near-one family or solve the unrestricted G0001 contract.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Complete argument

<a id="argument"></a>

<a id="quadratic-return-inputs"></a>
### Exact fixed inputs and source scope

The complete C633v2 fixed statement and logarithm-free probability argument were read for this consumer.
Only its upper probability interface

    integral r_s dnu_3<=8s^(2/3), 0<s<=1,                         (1)

is used in the new quadratic return.
Its matching lower bounds and amplitude-exponent sharpness are not used to infer a Fourier lower or upper rate.
The actual correlated-shift conditioning and distinction between product Haar and the pushed original circle remain as in the fixed input.

The [C632 amplitude derivative theorem](Yin_C_G0632_v1.md#square-root-regularization-derivative) gives for every 0<s<=1

    sum_l ||partial_l U_s||_infinity,
    sum_l ||partial_l r_s||_infinity
       <=2A_der,K/sqrt(s),                                       (2)

including common zeros and inversion.
For

    Kcal_s=(1-Re(w U_s(z^-1,u^-1,v^-1)))/2,
    F_(tau,s)=psi_tau(Kcal_s),

its product Fejer polynomial Q of degree M_j-1 in each coordinate satisfies

    ||Q-F_(tau,s)||_infinity
       <=D_reg,K omega_j/(tau sqrt(s)).                           (3)

The fourth-coordinate derivative is included.
The same Fejer convolution of r_s composed with inversion has uniform error at most D_reg,K omega_j/sqrt(s).

The exact [C565 full-box alias theorem](Yin_C_G0565_v2.md#moving-band-exact-alias) applies to these finite polynomials and to every gamma in [-M_j,M_j]^4.
It identifies their selected original-circle and four-torus coefficients exactly.
Every nonzero difference in the 2M_j box has nonzero H_j, so the associated original-circle characters are pairwise distinct.

The true original-window comparison remains

    ||k_j-Kcal composed with iota_j||_1<=epsilon_j,               (4)

on the original circle with the full 2d_j coefficient dimension.
The scalar transform is 1/tau-Lipschitz and all actual or regularized transforms take values in [0,1].
Only (4), not an unprovided uniform error, is used for its L2 conversion.

Finite Bessel below is proved by expanding the norm of a finite orthogonal projection.
Its classical probability-Haar attribution is the exact finite orthogonality interface already used in [C565](Yin_C_G0565_v2.md#moving-band-fejer-budget), with the [C174 source scope](Yin_C_G0174_v1.md#narrow-contact-source-interface).
No new completeness theorem, infinite Parseval identity or original source-proof audit is claimed.
The finite proof is repeated for the full selected box because the old first-band conclusion alone would not supply that scope.

<a id="contact-scale-square-majorant"></a>
### Squared regularization error at the actual contact scale

Fix 0<tau<=1/64, 0<lambda<=1 and rho=tau lambda.
The exact pointwise phase comparison gives

    |F_tau-F_(tau,rho)|<=r_rho(inverse coordinates)/(2tau).

Since both functions take values in [0,1], their squared difference is bounded by

    min{1,[rho/(2tau(g+rho))]^2}.                                (5)

Here and below g is evaluated at the inverted three coordinates when inside a four-torus function.
The comparison also holds at a common zero, where U and U_rho are both defined to be zero.

Put t_scale=tau(g/rho+1)=g/lambda+tau>0.
For 0<t_scale<=1/2, 2/(1+t_scale)>=1.
For t_scale>=1/2, the function (1+t_scale)/(4t_scale^2) decreases and is 3/2 at t_scale=1/2.
Therefore

    min{1,1/(4t_scale^2)}<=2/(1+t_scale)
       <=2/(1+g/lambda)=2r_lambda.                               (6)

The last inequality has the stated direction because 1+t_scale>=1+g/lambda.
Equations (5)--(6) give the scale-sensitive pointwise bound

    |F_tau-F_(tau,rho)|^2<=2r_lambda(inverse coordinates).         (7)

This retains the clipping at one before integration.
It does not use the coarser squared upper bound r_rho/(2tau) from the old return.

<a id="original-circle-quadratic-cost"></a>
### Both probability spaces and all five L2 costs

Write nu for normalized four-torus Haar and mu_j for original circle Haar pushed through iota_j.
The function r_lambda is independent of w.
By the exact logarithm-free input (1),

    integral r_lambda(inverse coordinates)dnu<=8lambda^(2/3).

Let Q_lambda be its four-coordinate product Fejer convolution, with a trivial constant w factor.
Its two probability-space means agree by the actual finite alias theorem.
Paying the uniform error between r_lambda and Q_lambda on each space gives

    integral r_lambda(inverse coordinates)dmu_j
       <=8lambda^(2/3)+2D_reg,K omega_j/sqrt(lambda).              (8)

This explicitly pays both Fejer errors.
No independence of the pushed-circle coordinates has been assumed.

Using (7), the torus and original-circle regularization L2 costs satisfy, respectively,

    ||F_tau-F_(tau,rho)||_(L2(nu))<=4lambda^(1/3),
    ||F_tau-F_(tau,rho)||_(L2(mu_j))
       <=4lambda^(1/3)
          +2sqrt(D_reg,K)sqrt(omega_j)lambda^(-1/4).               (9)

For the second estimate, apply sqrt(a+b)<=sqrt(a)+sqrt(b) to twice (8).
Their sum is exactly the two regularization contributions in (Q2).

The original composition contribution obeys

    ||f_(j,tau)-F_tau composed with iota_j||_2
       <=sqrt(epsilon_j/tau).                                   (10)

Indeed its absolute value is at most one, so its squared L2 norm is at most its L1 norm.
The latter is at most epsilon_j/tau by (4) and the scalar Lipschitz constant.
No pointwise epsilon_j estimate or stronger square conversion is used.

Take Q to be the product Fejer convolution of F_(tau,rho).
By (3), its uniform error on either probability space is at most D_reg,K omega_j/(tau sqrt(rho)).
These are the remaining two contributions.
Thus the triangle inequality in the two L2 spaces yields

    ||f_(j,tau)-Q composed with iota_j||_2+||F_tau-Q||_(L2(nu))
       <=sqrt(epsilon_j/tau)+8lambda^(1/3)
          +2sqrt(D_reg,K)sqrt(omega_j)lambda^(-1/4)
          +2D_reg,K omega_j/(tau sqrt(rho)).                      (11)

All five costs are present: original composition, two regularizations and two finite approximations.

<a id="whole-box-finite-projection"></a>
### Finite orthogonality on every selected set

Let Gamma be any finite subset of the stated box.
The characters indexed by Gamma are orthonormal on the four-torus, and the original-circle characters at H_j(gamma) are orthonormal because those integers are distinct.
For either finite orthonormal set and any L2 function h, expanding the square of the difference from its finite Fourier projection gives

    ||h-sum_(gamma in Gamma) hhat(gamma)chi_gamma||_2^2
       =||h||_2^2-sum_(gamma in Gamma)|hhat(gamma)|^2>=0.           (12)

On the circle use its corresponding integer characters and coefficients.
This is the complete finite projection calculation needed here.

The intermediate Q coefficients agree exactly between the original circle and four-torus for every gamma in the box.
Hence the coefficient difference in (Q1) is the difference of the two finite coefficient vectors of f-Q composed with iota_j and F_tau-Q.
Apply (12) to each, then the triangle inequality in their finite Euclidean coefficient space.
Equation (11) proves (Q1)--(Q2).
This proof permits several harmonics and zero or negative fourth coordinates.
The empty set gives zero on the left, so it is included.
No assertion concerning an infinite Fourier vector or the l1 norm of all coefficient differences is made.

If omega_j<=tau^(3/2), set lambda_bal=(omega_j/tau^(3/2))^(6/5).
This lies in (0,1], and rho_bal=tau lambda_bal is legal.
Direct substitution gives

    lambda_bal^(1/3)=omega_j^(2/5)tau^(-3/5),
    omega_j/(tau sqrt(rho_bal))=omega_j^(2/5)tau^(-3/5),
    sqrt(omega_j)lambda_bal^(-1/4)
       =omega_j^(1/5)tau^(9/20).

These three identities prove (Q3).
The notation bal identifies a balancing choice, not a proved optimal choice.

<a id="quadratic-full-support-consumer"></a>
### Complete multi-harmonic support payment

Under the displayed finite T_K condition, the adopted [C629 unequal-cutoff theorem](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) gives, for each 1<=k<=L_tau,

    sum_(|p|<=R_z-1,|q|<=R_u-1,1<=m<=J)
       |(U^k)hat(p,q,-m)|>=log(J+1)/16.

Its original scalar cap coefficients and inverse-phase identity are

    |a_k(tau)|>=3sqrt(tau)/(8pi),
    Fhat_tau(eta,k)=a_k(tau)(U^k)hat(-eta),
    L_tau sqrt(tau)>=1/8.

Select the full set

    G={(eta,k): -eta=(p,q,-m),
           |p|<=R_z-1, |q|<=R_u-1, 1<=m<=J, 1<=k<=L_tau}.

Its exact cardinality is

    N=(2R_z-1)(2R_u-1)J L_tau<=4L_tau R_z R_u J.                  (13)

All its coordinates belong to the original box under the stated cutoff assumptions.
The corresponding H_j frequencies are distinct, and they are positive since c_j>M_j(1+a_j+b_j) and k>=1.
Therefore none is the constant coefficient omitted from W_*.
Its total exact torus coefficient mass is at least 3log(J+1)/(1024pi).

For this entire set, Cauchy--Schwarz and (Q1) bound the sum of absolute coefficient errors by sqrt(N)E_2.
Insert (13) to obtain precisely (Q4).
This pays every coefficient in the rectangle.
No sparsity reduction, optimal-support assumption or unused negative-frequency factor is introduced.
The balanced version follows from (Q3) when its extra scale condition holds.

<a id="quadratic-uniform-width-strip"></a>
### Uniform strict powers below 4/11

Fix 0<theta<4/11, Delta_theta=2/5-11theta/10 and zeta_theta=Delta_theta/10.
Use the scalar cutoffs

    J_j=floor(M_j^zeta_theta),
    Q_z,j=floor(M_j^(2zeta_theta)),
    Q_u,j=floor(M_j^(theta/2+2zeta_theta)),

with J=J_j,R_z=Q_z,j,R_u=Q_u,j and L=L_tau.
These do not rename the original residual projection R_j.
For every M_j^-theta<=tau<=1/64, L_tau<=M_j^(theta/2)/4.
All cutoff exponents are positive and less than one.
The floor lower bounds show that the three T_K terms are bounded uniformly by fixed multiples of

    [M_j^-zeta_theta+M_j^(-theta/2)](1+log M_j),
    M_j^(-2zeta_theta)(1+log M_j),
    M_j^-zeta_theta.

All tend to zero.
Thus the finite condition, lower cutoff requirements and entire box containment hold uniformly beyond a threshold depending only on theta,K.
Moreover

    omega_j/tau^(3/2)
       <=M_j^(-1+3theta/2)(1+log M_j)->0,

because theta<4/11<2/3.
The balanced choice is therefore legal uniformly throughout the strip.

Using L_tau<=tau^(-1/2)/4, the complete square-root support factor in (Q4) satisfies

    2sqrt(L_tau R_z R_u J)
       <=M_j^(theta/4+5zeta_theta/2)tau^(-1/4).                   (14)

The actual epsilon_j=O_K((1+log M_j)/M_j^2) is retained from the original square-separated schedule.
Multiply each of the three terms of E_bal by (14).
For the original-composition term, use tau^(-3/4)<=M_j^(3theta/4).
For the middle term, use tau^(-17/20)<=M_j^(17theta/20).
For the last term, the remaining power is positive: tau^(9/20-1/4)=tau^(1/5)<=1.
In particular the lower width is not substituted in the wrong direction into that last factor.

The three complete errors are bounded, uniformly in the strip, by constants times

    M_j^e1(1+log M_j)^(1/2),
    M_j^e2(1+log M_j)^(2/5),
    M_j^e3(1+log M_j)^(1/5),                                    (15)

where

    e1=-1+theta+5zeta_theta/2=-9/10+29theta/40<-7/11,
    e2=-2/5+11theta/10+5zeta_theta/2=-3Delta_theta/4,
    e3=-1/5+theta/4+5zeta_theta/2=-1/10-theta/40.

Each is strictly negative.
Set sigma_theta=min(3Delta_theta/4,1/10).
Since the largest logarithmic exponent in (15) is 1/2, their sum is at most
C_error M_j^-sigma_theta(1+log M_j)^(1/2), with C_error depending only on theta,K.
Finally J_j+1>M_j^zeta_theta, so log(J_j+1)>zeta_theta log M_j.
Inserting this into (Q4) proves (Q5) with a uniform j0 and C_error.

Every stated sequence eventually enters its upper width cutoff and satisfies its assumed lower inequality.
The same uniform strip bound then gives divergence, without a universal entry index for arbitrary sequences.
The example theta=1/3 lies strictly between 2/7 and 4/11.
At theta=4/11 the present Delta_theta and growing-band exponent vanish, so no endpoint assertion is made.
The proof uses no numerical experiment or new external theorem.

### Original input and Task boundary

The original P_j, actual coefficient matrix, full 2d_j window and probability law remain unchanged throughout.
C174 supplies finite Wiener norms for each fixed j,tau and contact-minus-Haar margin at least 1/2.
The family stays in log 2<m(P_j)<log 4.
Neither sharpness of the C633 amplitude exponent nor this sufficient Fourier-width exponent resolves the original unrestricted Mahler-gap contract.
The quadratic comparison is a separate improved finite-error theorem, not a reclassification of a first-band result or an assertion about an infinite coefficient sum.

## Assessment history

### Decision finite-quadratic-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:22 |
| status | open |
| reason | Register the complete contact-scale squared regularization majorant, original-circle mean comparison, all five L2 costs and finite projection theorem on arbitrary subsets of the original four-box. The full multi-harmonic support price gives the strict width range theta<4/11 with explicit uniform error. The exact C633v2 probability input is adopted; this new contributor theorem awaits independent whole review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | Every actual j,M,tau,lambda and finite Gamma in Q1--Q3, all finite cutoffs/support costs in Q4, every width in Q5 for each fixed0<theta<4/11, empty/zero-harmonic cases, actual input and all limits. |
| argument | [Whole complete proof](#argument) | Pointwise clipping with correct majorant direction, torus and original-circle regularization at lambda, both finite mean errors, true sqrt(epsilon/tau), full finite projections, legal balancing, complete selected support and every uniform exponent. |
| dependency | [Adopted logarithm-free original probability](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Exact integral r_s<=8s^(2/3) for every0<s<=1 on the same original g; no lower-bound or amplitude-sharpness inference about Fourier errors. |
| dependency | [Actual amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same g,Ncal,A_der,K,D_reg,K, all common-zero/inversion derivative bounds and four-coordinate Fejer errors at both lambda and rho. |
| dependency | [Original complete function comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Original epsilon_j L1 error, scalar Lipschitz cost, normalized Fejer construction and finite-orthogonality source interface; arbitrary multi-band projection is proved here. |
| dependency | [All exact original aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Entire four-box coefficient identity and 2M_j difference injectivity, including arbitrary finite Gamma and positive selected consumer frequencies. |
| dependency | [Adopted unequal-cutoff theorem](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Same actual power witnesses, derivative estimates, finite T_K and all rectangular phase coefficients. |
| dependency | [All cap harmonics and inverse phase](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bounds, L_tau normalization and Fhat_tau(eta,k)=a_k(U^k)hat(-eta), retaining complete finite support. |
| dependency | [Actual schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K((1+log M_j)/M_j^2) from original lower prime separations; no upper prime-gap theorem. |
| dependency | [Normalized Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Actual probability-Haar finite kernels and first moment, with all approximation errors paid. |
| dependency | [Actual contacts and source scope](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Fixed-j Wiener finiteness, actual margin and preserved thin-limit order; existing probability-Haar source scope is reused without a new original-proof audit. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:32 |
| status | proved |
| reason | Adopt the entire finite quadratic theorem after main reading of complete C635 and isolated whole R842. The contact-scale clipped square, both original-circle mean errors, genuine sqrt(epsilon/tau) and complete finite projections support every finite original4box coefficient vector. All multi-harmonic support costs and uniform exponents establish every fixed theta<4/11. Original full2d/Haar/source/sequence boundaries remain; no endpoint, optimality, near-one family or unrestricted Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | Every actual j,M,tau,lambda and finite Gamma in Q1--Q3, all finite cutoffs/support costs in Q4, every width in Q5 for each fixed0<theta<4/11, empty/zero-harmonic cases, actual input and all limits. |
| argument | [Whole complete proof](#argument) | Pointwise clipping with correct majorant direction, torus and original-circle regularization at lambda, both finite mean errors, true sqrt(epsilon/tau), full finite projections, legal balancing, complete selected support and every uniform exponent. |
| dependency | [Adopted logarithm-free original probability](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Exact integral r_s<=8s^(2/3) for every0<s<=1 on the same original g; no lower-bound or amplitude-sharpness inference about Fourier errors. |
| dependency | [Actual amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same g,Ncal,A_der,K,D_reg,K, all common-zero/inversion derivative bounds and four-coordinate Fejer errors at both lambda and rho. |
| dependency | [Original complete function comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Original epsilon_j L1 error, scalar Lipschitz cost, normalized Fejer construction and finite-orthogonality source interface; arbitrary multi-band projection is proved here. |
| dependency | [All exact original aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Entire four-box coefficient identity and 2M_j difference injectivity, including arbitrary finite Gamma and positive selected consumer frequencies. |
| dependency | [Adopted unequal-cutoff theorem](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Same actual power witnesses, derivative estimates, finite T_K and all rectangular phase coefficients. |
| dependency | [All cap harmonics and inverse phase](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bounds, L_tau normalization and Fhat_tau(eta,k)=a_k(U^k)hat(-eta), retaining complete finite support. |
| dependency | [Actual schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K((1+log M_j)/M_j^2) from original lower prime separations; no upper prime-gap theorem. |
| dependency | [Normalized Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Actual probability-Haar finite kernels and first moment, with all approximation errors paid. |
| dependency | [Actual contacts and source scope](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Fixed-j Wiener finiteness, actual margin and preserved thin-limit order; existing probability-Haar source scope is reused without a new original-proof audit. |
| review | [Independent whole finite-quadratic finding](../audits/reviews/Yin_R_G0842_v1.md#whole-finite-quadratic-finding) | Entire Q1--Q5, actual logarithm-free input proof, every clipping/zero/finiteGamma case, both probability laws and all five L2 costs, complete original support and all cutoff/balancing/uniform exponents; historical reviews and source scope retained. |


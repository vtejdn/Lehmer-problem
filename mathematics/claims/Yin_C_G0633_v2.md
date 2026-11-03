---
author: Yin
---

# Two-sided phase sublevels and logarithm-free original return

Human author Yin.
This physical v2 retains the entire unchanged v1 statement, proof and source boundary, and adds the logarithm-free upper bound, matching original-phase lower bounds and complete improved coefficient and finite-support consumers.
The exact adopted v1 assessment and its review remain at [the physical predecessor](Yin_C_G0633_v1.md#decision-whole-reviewed-2026-10-23).
Root supplied the complete two-region refinement with constant8 and the matching conditional lower-event construction.
Paid_comparison checked and developed all integrals, explicit constants, original probability conditioning, full comparison costs and uniform finite-support consumers.
Both are contributors and neither is the independent reviewer of this extension.
The earlier R838 finding applies only to its exact physical-v1 scope.
The new whole review must inspect the retained argument and all additions below.

Root and paid_comparison retain their v1 contribution roles for the exact one-coordinate integral, correlated-shift estimate and original return.
The accepted C632, C565 and C629v3 interfaces keep their actual source-proof and historical review boundaries.
The retained v1 statements about its then-unresolved logarithm or amplitude decay describe that earlier proof's limits.
The new matching bounds settle the two-thirds exponent only for the original sublevel probability and regularization integral.
They do not establish optimality of any Fourier error rate or Wiener-width exponent.
No general critical-logarithmic corridor, new native computation, external-source acquisition or source-proof recertification is used.

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

### Additional two-sided and logarithm-free conclusions


Retain the entire original input family, phase, probability normalization, derivative constants, full 2d_j coefficient window and all EI1--EI6 statements of C633v1.
For every 0<rho<=1 and every s>0, the same original g and r_rho satisfy

    integral r_rho dnu_3<=8rho^(2/3),
    nu_3{g<=s}<=min{1,16s^(2/3)}.                               (LF1)

The same actual phase has the matching lower estimates

    nu_3{g<=s}>=s^(2/3)/(166400pi^3), 0<s<=1,
    integral r_rho dnu_3>=rho^(2/3)/(332800pi^3), 0<rho<=1.        (LF1L)

Thus its sublevel probability and regularization integral both have exact order two-thirds as their parameters tend to zero, with the displayed absolute constants.
In particular neither admits a uniform upper bound C times that parameter to any fixed power greater than2/3 for finite C.
This sharpness concerns only those two original amplitude quantities, not the original Fourier budget or the width exponent2/7.

For every actual j with M_j>=2, every 0<tau<=1, every 0<rho<=1 and every integer gamma in [-M_j,M_j]^4,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
      <=[epsilon_j+8rho^(2/3)
                    +3D_reg,K omega_j/sqrt(rho)]/tau.             (LF2)

Choose rho_j=omega_j^(6/7) and define

    beta_free,j=epsilon_j+(8+3D_reg,K)omega_j^(4/7).

Then the entire same-box error is at most beta_free,j/tau, and

    beta_free,j=O_K(M_j^(-4/7)(1+log M_j)^(4/7)).                  (LF3)

For every sufficiently large actual j, every 0<tau<=1/64 and all integer cutoffs R_z,R_u>=2,J>=2 satisfying the unchanged conditions R_z,R_u,J,L_tau<=M_j and T_K(R_z,R_u,J,L_tau)<=1/16,

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)
            -R_z R_u J beta_free,j/tau^(3/2).                     (LF4)

For any fixed 0<eta<2/7, put Delta=4/7-2eta and zeta=Delta/10 as before.
There exist j1 and C depending only on eta,K such that for every j>=j1 and every width M_j^(-eta)<=tau<=1/64,

    W_*(psi_tau(k_j))
      >=[3zeta/(1024pi)]log M_j
           -C M_j^(-Delta/2)(1+log M_j)^(4/7).                    (LF5)

Thus the same eventual shrinking-width sequences have actual Wiener norms tending to infinity, with the improved uniform error logarithm.
The strict exponent range eta<2/7, possible sequence-dependent strip-entry index, actual margin at least1/2, fixed-input finiteness and original log2<m(P_j)<log4 range remain unchanged.
No pointwise ordering of beta_free,j and the earlier beta_int,j is asserted.
No endpoint eta=2/7, critical-logarithmic corridor, Fourier-rate or width-exponent optimality, or unrestricted Mahler conclusion is supplied.

## Reuse and source boundary


Before deriving the new bound, the complete actual C632 statement and proof, C629v3 original phase and finite unequal-cutoff theorem, C565v2 denominator/alias/return chain and C569v2 original schedule costs were read.
A focused local search for cotangent coordinates, one-coordinate integration and cancellation tails found the exact elementary cotangent-Haar substitution in C629v3 but no existing bound at this scope.
The new exact quadratic integral, regions, logarithmic bounds and constants are proved directly below.
The accepted C632 amplitude-derivative estimates and C629v3 finite coefficient-sum theorem supply their exact previously checked interfaces.
Their classical source and historical SELF/UNKNOWN review scopes are unchanged.
No independent original-circle coordinates, external convolution theorem, general sublevel theorem or unproved root-separation estimate is used.

The v2 refinement uses the exact integral and elementary probability densities already retained in physical v1.
The complete candidate was checked against that actual proof before retention.
The noncancellation minimum, conditional cancellation integral and matching lower event are direct calculations supplied below; no new external integration or sublevel theorem is invoked.
The original-return consumer uses only the accepted amplitude derivatives and the adopted C629v3 finite unequal-cutoff theorem, not a developing general critical-logarithmic theorem.
Every new source-role claim is confined to these unchanged interfaces.

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

## Additional complete logarithm-free and two-sided argument

Let 0<rho<=1, T=16rho^(-1/6), X_0=T/2=8rho^(-1/6), and keep C633's exact H(q,D), q and correlated b_theta.
Use the same three regions and the same conditional-y integration before substituting the marginal Cauchy law of x in the cancellation region.

The central square contributes at most rho T^2/(8pi^2)=32rho^(2/3)/pi^2.
For noncancellation, retain both H<=q/32 and H<=sqrt(q)/(sqrt(2)M), where M=max(abs(x),abs(y)) and abs(D)>=M/4.
The two maximal-coordinate sectors and four signs therefore give

    I_nc <= (8/pi^2) integral_(x=T)^infinity integral_(y=0)^x
             min{rho/32, sqrt(rho)/(sqrt(2)x^2 sqrt(1+y^2))} dy dx.

This bound is pointwise in the bounded shift and may be integrated against the product marginal Cauchy laws.
The factor8 comes from two maximal-coordinate sectors and the four choices of signs of x,y; the dominating integrand is even in both coordinates.
In the sector |x|>=|y|, the inequality |x|sqrt(1+x^2)>=x^2 gives the displayed second term, while the first term cancels both original Cauchy densities exactly.
Swap these nonnegative integrals.
For 0<=y<=T, enlarge the x-domain from [T,infinity) to (0,infinity), and use integral_0^infinity min(a,b/x^2)dx=2sqrt(ab).
With a=rho/32 and b=sqrt(rho)/(sqrt(2)sqrt(1+y^2)), its y-integral is at most

    4rho^(3/4)sqrt(T)/sqrt(32sqrt(2))
      =16rho^(2/3)/sqrt(32sqrt(2)).

Here integral_0^T(1+y^2)^(-1/4)dy<=2sqrt(T).
This follows by comparison with y^(-1/2) for y>0, whose integrable singularity at0 causes no difficulty.
The identity integral_0^infinity min(a,b/x^2)dx=2sqrt(ab) follows by splitting at sqrt(b/a), for positive a,b.
For y>=T, retain only b/x^2 and integrate x from y to infinity.
The resulting tail is at most sqrt(rho)/(sqrt(2)T)=rho^(2/3)/(16sqrt(2)).
Consequently

    I_nc <= (8/pi^2)[16/sqrt(32sqrt(2))+1/(16sqrt(2))]rho^(2/3)
         <3rho^(2/3).

The final numerical comparison follows already from pi^2>9, sqrt(32sqrt(2))>5 and sqrt(2)>1, since 128/45+1/18<3.
The swap gives x>=max(T,y) in both cases, so no portion of either maximal-coordinate sector has been dropped.

For cancellation, retain the exact conditional integral from C633 rather than its coarse argument bound.
It gives

    I_c <= (4sqrt(5)/pi^2)sqrt(rho) integral_(X_0)^infinity
      asinh(x sqrt(32Q)/(2(32+Q)))/(1+x^2) dx,
    Q=10rho x^4.

The asinh argument is at most (sqrt(5)/8)sqrt(rho)x^3=64sqrt(5)(x/X_0)^3.
Here only the lower bound 32+Q>=32 has been used; it is valid throughout the unbounded x integral.
For v=x/X_0>=1,

    asinh(argument)<=log(1+2argument)
      <=log(1+128sqrt(5))+3log(v)<6+3log(v).

Indeed sqrt(1+z^2)<=1+z for z>=0, and 1+128sqrt(5)<289<exp(6).
For the last exact constants, sqrt(5)<9/4 gives the first inequality, while exp(1)>8/3 gives exp(6)>(8/3)^6>289.
The latter rational inequality is 262144>289*729=210681.
Since 1+x^2>=x^2, integral_(X_0)^infinity (6+3log(x/X_0))/x^2 dx=9/X_0 gives

    I_c <=36sqrt(5)/(8pi^2)rho^(2/3)<(9/8)rho^(2/3).

Here sqrt(5)<9/4 and pi^2>9 suffice.
Adding all three regions gives

    integral r_rho dnu_3
      <(32/9+3+9/8)rho^(2/3)
      =(553/72)rho^(2/3)<8rho^(2/3).

It follows that nu_3{g<=s}<=min{1,16s^(2/3)} for every s>0, using r_s>=1/2 on g<=s when s<=1 and the trivial bound when s>1.
This proves (LF1) and retains all common-zero points through their already defined continuous r_rho.
The exact phase and every conditional-y step are unchanged from the retained argument; no independence of b_theta and x has been used.

### Matching lower event for the same original amplitude

Fix 0<s<=1 and put T=4s^(-1/6)>=4.
Restrict the actual theta,u coordinates to x,y in [T,2T].
For each such fixed theta,u, define D=x+y+b_theta and restrict the independent v coordinate through t=cot(arg(v)/2) to the interval [-D,-D+1].
The shift b_theta remains its actual value, and |b_theta|<=4 is the only bound used.
Then |t+D|<=1 and, because D>=2T-4>=4, every such t is negative and

    |t|>=D-1>=2T-5>=3T/4,
    |t|<=D<=4T+4<=5T.

The exact original formula (EI7) therefore gives

    g=32[1+(t+D)^2]/[(1+x^2)(1+y^2)(1+t^2)]
       <=64/[T^4(9T^2/16)]
       =1024/(9T^6)=s/36<=s.

Each of the x,y marginal events has probability

    integral_T^(2T) du/[pi(1+u^2)]
       >=T/[pi(1+4T^2)]>=1/(5pi T).

The x law follows by pushing theta Haar through z to z^K and cotangent, and the y law is independent of theta.
For every fixed actual theta,u satisfying the restrictions, the t interval has length one and |t|<=5T.
Its conditional probability is at least

    1/[pi(1+25T^2)]>=1/(26pi T^2).

Integrate this uniform conditional bound first in v, then over the actual theta,u event.
Its probability is at least

    1/[(5pi T)^2(26pi T^2)]
       =1/(650pi^3 T^4)=s^(2/3)/(166400pi^3).

The whole event lies in g<=s, so this proves the first inequality of (LF1L).
On g<=rho one has r_rho>=1/2; taking s=rho proves its second inequality.
No independence between b_theta and x is required by this conditional construction.
The positive lower constants and (LF1) prove the two exact orders as the parameters tend to zero.
If an upper bound C s^alpha or C rho^alpha held for some alpha>2/3 and finite C, division by the parameter to power2/3 would contradict these positive lower constants in the limit.
This proves only amplitude-exponent sharpness and supplies no converse bound on original Fourier errors or Wiener divergence corridors.

### Complete original return and finite-support consumer

Reuse C632's full pointwise amplitude derivative on the same Acal,Bcal, including their common zeros and coordinate inversion.
The product Fejer errors remain E_rho=D_reg,K omega_j/sqrt(rho) for r_rho and E_rho/tau for F_(tau,rho), including the fourth-coordinate derivative.
Put B_rho=8rho^(2/3).
The exact no-alias mean identity for the finite r_rho convolution, with both uniform errors paid, gives its original pushed-circle integral at most B_rho+2E_rho.
The product-Haar integral is at most B_rho by (LF1).
The two phase-regularization comparisons therefore cost at most [(B_rho+2E_rho)+B_rho]/(2tau)=(B_rho+E_rho)/tau.
The two F_(tau,rho) convolution errors add 2E_rho/tau, and the full original-window function comparison adds epsilon_j/tau.
The intermediate finite coefficients agree exactly for every gamma in the same original four-dimensional box.
Consequently their total error is

    [epsilon_j+8rho^(2/3)+3D_reg,K omega_j/sqrt(rho)]/tau,

which is (LF2), with all five comparison costs retained.
For M_j>=2, choose rho=omega_j^(6/7), which lies in (0,1), to get

    beta_free,j=epsilon_j+(8+3D_reg,K)omega_j^(4/7)
      =O_K(M_j^(-4/7)(1+log M_j)^(4/7)).

Indeed rho^(2/3)=omega_j^(4/7) and omega_j/sqrt(rho)=omega_j^(4/7).
The exact original epsilon_j=O_K((1+log M_j)/M_j^2) is smaller asymptotically, so (LF3) follows without a prime-gap upper bound.

Under the unchanged finite T_K condition, retain the entire original frequency set G from the v1 finite-support proof, of cardinality at most 4L_tau R_z R_u J.
Its frequencies remain distinct and strictly positive, and all lie in the original box.
The adopted C629v3 band sum and scalar harmonic lower bounds remain unchanged.
Summing the full beta_free,j/tau comparison over every selected coefficient gives

    W_*(psi_tau(k_j))
      >=[3/(8pi)]sqrt(tau)L_tau log(J+1)/16
           -4L_tau R_z R_u J beta_free,j/tau
      >=3log(J+1)/(1024pi)
           -R_z R_u J beta_free,j/tau^(3/2).

This proves (LF4), with no extra contribution claimed from unused negative frequencies or an infinite Fourier comparison.

For (LF5), take the same Q_z,j=floor(M_j^(2zeta)), Q_u,j=floor(M_j^(eta/2+2zeta)) and J_j=floor(M_j^zeta) as in the retained v1 proof, and use L=L_tau.
For every width M_j^(-eta)<=tau<=1/64, the unchanged bound L_tau<=M_j^(eta/2)/4 holds.
All cutoff exponents remain positive and below one, the floors eventually meet their lower bounds, and all four cutoffs lie at most M_j.
Exactly as in the complete earlier check, the three T_K terms are bounded uniformly by fixed multiples of

    [M_j^-zeta+M_j^(-eta/2)](1+log M_j),
    M_j^(-2zeta)(1+log M_j), M_j^-zeta.

They tend to zero, so the finite cutoff condition holds after a threshold depending only on eta,K.
Every selected coefficient is still included in the error

    Q_z,j Q_u,j J_j beta_free,j/tau^(3/2)
       =O_K(M_j^(2eta+5zeta-4/7)(1+log M_j)^(4/7))
       =O_K(M_j^(-Delta/2)(1+log M_j)^(4/7)).

Here 2eta-4/7=-Delta and 5zeta=Delta/2 as before.
Since J_j+1>M_j^zeta, insertion into (LF4) proves (LF5).
The same sequence-entry qualification and uniform strip quantifiers apply.
The strict power range eta<2/7 is unchanged; only the error logarithm improves from exponent one to four-sevenths.
No Fourier-rate or width-exponent sharpness, endpoint critical-logarithmic application, numerical evidence or general Lehmer gap is asserted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision two-sided-logarithm-free-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:14 |
| status | open |
| reason | Retain the whole adopted v1 mathematics and add complete two-sided original phase estimates of exact exponent2/3, the explicit upper constant8, all-rho full4box coefficient comparison, beta_free=epsilon+(8+3D_reg,K)omega^(4/7), and every original finite-support/uniform-strip cost with logarithmic error exponent4/7. Root and paid_comparison are contributors. Fresh isolated whole review and adoption remain separate. Sharpness is confined to the two amplitude quantities; no Fourier-rate, width-exponent or endpoint optimality, near-one family or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire expanded statement](#statement) | Entire unchanged EI1--EI6 plus LF1,LF1L and LF2--LF5, every original domain and normalization, matching lower ranges and strict strip/sequence quantifiers. |
| argument | [Whole retained and extended proof](#complete-argument) | Complete unchanged EI1--EI14 and new two-region integrals, all constants, correlated-shift conditioning, matching lower event, full five comparison costs and all original finite-support/strip estimates. |
| dependency | [Adopted exact physical v1](Yin_C_G0633_v1.md#complete-argument) | Same exact normalized H(q,D), original cotangent densities and conditional region geometry, full original-return and finite-support setup; old review is not enlarged to the additions. |
| dependency | [Actual amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same Acal,Bcal,g,Ncal,A_der,K,D_reg,K and complete rho^(-1/2) angular derivative/Fejer bounds, including zeros and inversion. |
| dependency | [Complete original input and projection](Yin_C_G0565_v2.md#statement) | Actual fixed K and prime schedule, monic irreducible Salem P_j, full degree and 2d_j coefficient projection/kernel. |
| dependency | [Original denominator and inverse phase](Yin_C_G0565_v2.md#moving-band-denominator) | Same polynomial identity, equal modulus, U=Ncal/g off the common-zero set and original phase conventions, retained in the exact integral proof. |
| dependency | [Complete finite original return interface](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Original epsilon_j, both regularization comparisons, both product-Fejer errors and Fourier signs, with the new probability budget explicitly paid. |
| dependency | [Every original finite alias](Yin_C_G0565_v2.md#moving-band-exact-alias) | Complete4box equality, 2M_j difference exclusion and positivity of selected actual frequencies. |
| dependency | [Adopted unequal-cutoff phase theorem](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Same actual witnesses, finite T_K condition and coefficient lower bound, without a general critical-logarithmic input. |
| dependency | [Scalar harmonics and inverse-phase coefficients](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bound, L_tau bounds and phase inversion; every finite selected coefficient is paid by LF2. |
| dependency | [Actual schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | Original epsilon_j asymptotic from lower square prime separations, with no upper prime-gap estimate. |
| dependency | [Normalized finite Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Probability-Haar finite kernels and first moment at their accepted interface. |
| dependency | [Original contacts and fixed-input limits](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual margin at least1/2 and finite Wiener norms for fixed original j,tau, with the original order-of-limits restriction. |
| support | [Exact v1 whole finding](../audits/reviews/Yin_R_G0838_v1.md#exact-phase-integration-whole-independent-finding) | Independent review of physical v1 only, with no prospective review of the new logarithm-free bounds, matching lower event or improved consumers. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:20 |
| status | proved |
| reason | Adopt the complete physicalv2 after main reading of all new mathematics, exact retained-v1 comparison and isolated whole R841. The logarithm-free upper constant8 and both conditional lower events prove exact two-thirds amplitude order. Every original4box comparison, finite support and strict two-sevenths strip cost remains paid with logarithmic error exponent4/7. The sharpness claim concerns only the two amplitude quantities; no Fourier/width optimality, original-circle independence, endpoint or unrestricted Mahler conclusion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire expanded statement](#statement) | Entire unchanged EI1--EI6 plus LF1,LF1L and LF2--LF5, every original domain and normalization, matching lower ranges and strict strip/sequence quantifiers. |
| argument | [Whole retained and extended proof](#complete-argument) | Complete unchanged EI1--EI14 and new two-region integrals, all constants, correlated-shift conditioning, matching lower event, full five comparison costs and all original finite-support/strip estimates. |
| dependency | [Adopted exact physical v1](Yin_C_G0633_v1.md#complete-argument) | Same exact normalized H(q,D), original cotangent densities and conditional region geometry, full original-return and finite-support setup; old review is not enlarged to the additions. |
| dependency | [Actual amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same Acal,Bcal,g,Ncal,A_der,K,D_reg,K and complete rho^(-1/2) angular derivative/Fejer bounds, including zeros and inversion. |
| dependency | [Complete original input and projection](Yin_C_G0565_v2.md#statement) | Actual fixed K and prime schedule, monic irreducible Salem P_j, full degree and 2d_j coefficient projection/kernel. |
| dependency | [Original denominator and inverse phase](Yin_C_G0565_v2.md#moving-band-denominator) | Same polynomial identity, equal modulus, U=Ncal/g off the common-zero set and original phase conventions, retained in the exact integral proof. |
| dependency | [Complete finite original return interface](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Original epsilon_j, both regularization comparisons, both product-Fejer errors and Fourier signs, with the new probability budget explicitly paid. |
| dependency | [Every original finite alias](Yin_C_G0565_v2.md#moving-band-exact-alias) | Complete4box equality, 2M_j difference exclusion and positivity of selected actual frequencies. |
| dependency | [Adopted unequal-cutoff phase theorem](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Same actual witnesses, finite T_K condition and coefficient lower bound, without a general critical-logarithmic input. |
| dependency | [Scalar harmonics and inverse-phase coefficients](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bound, L_tau bounds and phase inversion; every finite selected coefficient is paid by LF2. |
| dependency | [Actual schedule costs](Yin_C_G0569_v2.md#static-phase-original-return) | Original epsilon_j asymptotic from lower square prime separations, with no upper prime-gap estimate. |
| dependency | [Normalized finite Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Probability-Haar finite kernels and first moment at their accepted interface. |
| dependency | [Original contacts and fixed-input limits](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual margin at least1/2 and finite Wiener norms for fixed original j,tau, with the original order-of-limits restriction. |
| support | [Exact v1 whole finding](../audits/reviews/Yin_R_G0838_v1.md#exact-phase-integration-whole-independent-finding) | Independent review of physical v1 only, with no prospective review of the new logarithm-free bounds, matching lower event or improved consumers. |
| review | [Independent whole two-sided finding](../audits/reviews/Yin_R_G0841_v1.md#two-sided-logarithm-free-whole-independent-finding) | Complete retained EI chain after exact comparison plus all LF1/LF1L/LF2--LF5, regional integrals/constants, correlated conditional lower event, amplitude-only sharpness, all original costs and uniform width/sequence quantifiers; prior reviews and source limits retain exact scope. |


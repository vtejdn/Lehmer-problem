---
author: Yin
---

# Positive-kernel quadratic return at the critical four-elevenths scale

Human author Yin.
Root supplied the squared positive kernel, endpoint-inclusive witness payment and arbitrary diverging critical enlargement.
Paid_comparison checked and developed the normalization, explicit moments and tail, closed-box alias extension, complete quadratic comparisons, all support costs and uniform enlargement estimates.
Both are contributors, not independent reviewers.
The reused contact-scale finite-projection mechanism was developed by root and phase_bands in [C635v1](Yin_C_G0635_v1.md#argument).
Its full necessary argument with the changed kernel is given below; no unresolved author draft or prospective review is invoked as an accepted premise.
The preceding exact phase and two-sided amplitude work is retained in adopted [C633v2](Yin_C_G0633_v2.md#decision-whole-reviewed-2026-10-23).
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
Define the fixed original-polynomial constant

    A_der,K=1+sum_(l=1)^3(||partial_l Acal||_infinity
                                  +||partial_l Bcal||_infinity).

For 0<s<=1 put r_s=s/(g+s), U_s=Ncal/(g+s), and define

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),
    F_(tau,s)=psi_tau((1-Re(w U_s(z^-1,u^-1,v^-1)))/2),
    f_(j,tau)=psi_tau(k_j),
    iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

### Exact positive kernel and closed support

For every integer N>=1 use normalized circle Haar, represent angular moments and tails by t in [-pi,pi], and define

    F_N(t)=N^-1 abs(sum_(l=0)^(N-1)exp(ilt))^2,
    c_N=integral F_N(t)^2 dt/(2pi)=(2N^2+1)/(3N),
    J_N(t)=F_N(t)^2/c_N.

The kernel J_N is even, nonnegative, has integral one and degree at most2N-2.
Every Fourier coefficient belongs to [0,1].
It satisfies

    integral |t|J_N(t)dt/(2pi)<=3pi/(2N),
    integral_(|t|>=delta)J_N(t)dt/(2pi)
          <=pi^3/(2N^3 delta^3), 0<delta<=pi.                     (PK1)

For every integer support radius R>=2 set N_R=floor(R/2)+1 and P_R=J_(N_R).
Then the Fourier support of P_R is contained in the CLOSED integer interval [-R,R], with first angular moment at most3pi/R and tail at most4pi^3/(R^3 delta^3).
Put D_J,K=6pi A_der,K.
For every integer M>=2, every 0<s<=1 and every 0<tau<=1, the four-coordinate product P_M smoothing has errors at most

    D_J,K/(M sqrt(s)) for r_s composed with inversion,
    D_J,K/(M tau sqrt(s)) for F_(tau,s).                         (PK2)

The first function is independent of the fourth coordinate.
For the actual M=M_j, the entire closed-box coefficient identity is valid for every finite polynomial Q supported in [-M,M]^4 and every gamma in [-M,M]^4 intersect Z^4:

    integral Q(iota_j(z))z^(-H_j(gamma))dHaar(z)=Qhat(gamma).      (PK3)

### Complete linear and quadratic original return

For every actual j with M_j>=2, every 0<tau<=1, every 0<rho<=1 and every integer gamma in the same closed box,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=[epsilon_j+8rho^(2/3)
                       +3D_J,K/(M_j sqrt(rho))]/tau.             (PK4)

The legal choice rho=M_j^(-6/7) supplies the complete individual-coefficient budget
epsilon_j+(8+3D_J,K)M_j^(-4/7).

For every actual j with M_j>=2, every 0<tau<=1/64, every 0<lambda<=1 and every finite Gamma subset of the entire closed box, put rho=tau lambda.
Then

    [sum_(gamma in Gamma)
        |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|^2]^(1/2)
       <=Gamma_J(j,tau,lambda),                                 (PK5)

where

    Gamma_J(j,tau,lambda)
      =sqrt(epsilon_j/tau)+8lambda^(1/3)
         +2sqrt(D_J,K)M_j^(-1/2)lambda^(-1/4)
         +2D_J,K/[M_j tau sqrt(rho)].

This includes Gamma empty and any positive, negative or zero fourth-coordinate indices.
If M_j^-1<=tau^(3/2), the choice

    lambda_bal=(M_j^-1/tau^(3/2))^(6/5), rho_bal=tau lambda_bal

is legal and gives

    Gamma_J<=sqrt(epsilon_j/tau)
        +(8+2D_J,K)M_j^(-2/5)tau^(-3/5)
        +2sqrt(D_J,K)M_j^(-1/5)tau^(9/20)
       =:Gamma_J,bal(j,tau).                                    (PK6)

### Complete witness support and original Wiener bound

Let delta_0=pi/(4K).
For integers R_z,R_u>=2,J>=2,L>=1 define

    T_J,K(R_z,R_u,J,L)
       =24576pi J(L+J)/R_u+3pi(K+4)/R_z
           +8pi^3 J/(R_z^3 delta_0^3).

If T_J,K<=1/16, then for every 1<=k<=L the SAME actual phase satisfies

    sum_(|p|<=R_z,|q|<=R_u,1<=m<=J)
         |(U^k)hat(p,q,-m)|>=log(J+1)/16.                        (PK7)

The endpoints are included.
For every sufficiently large actual j and 0<tau<=1/64 let L_tau=floor(1/(4sqrt(tau))).
If R_z,R_u,J,L_tau<=M_j and T_J,K(R_z,R_u,J,L_tau)<=1/16, then for every 0<lambda<=1,

    W_*(psi_tau(k_j))
       >=3log(J+1)/(1024pi)
           -3sqrt(L_tau R_z R_u J)Gamma_J(j,tau,lambda).          (PK8)

The exact selected cardinality is
(2R_z+1)(2R_u+1)J L_tau<=9L_tau R_z R_u J.
Every selected original frequency is positive and distinct.
When M_j^-1<=tau^(3/2), (PK8) also holds with Gamma_J,bal and its balanced choice.

### Critical scale with every diverging enlargement

There exist H_0>=1, M_0>=2 and C>0 depending only on K such that for every actual j with M=M_j>=M_0, every real scalar H and every width tau satisfying

    H_0<=H<=M^(4/11)/64,
    M^(-4/11)H<=tau<=1/64,

one has

    W_*(psi_tau(k_j))
       >=3log H/(4096pi)
          -C[H^(-29/40)+M^(-1/55)(1+log M)^(1/2)].               (PK9)

The scalar H is distinct from the frequency map H_j(gamma).
One concrete choice starts with

    C_Kern=64*24576pi,
    J_0=ceil(max{2,192pi(K+4),sqrt(512pi^3/delta_0^3)}),
    H_0=J_0^4.

An adequately large M_0 then supplies all original schedule and box conditions.
The actual cutoffs used in the proof are

    J=floor(H^(1/4)), R_z=J,
    L_max=M^(2/11)H^(-1/2)/4,
    R_u=ceil(C_Kern J(L_max+J)).                                  (PK10)

Consequently EVERY sequence of actual widths tau_j->0 satisfying
M_j^(4/11)tau_j->infinity has W_*(psi_(tau_j)(k_j))->infinity.
There is no prescribed logarithmic rate of divergence for the enlargement.
An arbitrary sequence enters the stated strip at its own possible index.
The unmodified critical width, bounded enlargements, arbitrary faster thinning and optimality of 4/11 remain unresolved.
The actual original2d_j window, normalized circle law, fixed-j finite Wiener norms, contact-minus-Haar margin at least1/2 and log2<m(P_j)<log4 input family are unchanged.
No amplitude-sharpness statement is converted into a Fourier or width optimality claim, and no unrestricted Mahler conclusion is asserted.

## Source and reuse boundary

The complete adopted C633v2 amplitude interface, C632 derivatives, C565 closed2M alias proof and original comparison, and C629v3 witness and harmonic arguments were read.
The fixed C635v1 finite quadratic argument was also read as actual prior author work; the complete required proof with the new kernel is reproduced below, rather than assuming its then-open assessment as a proved premise.
A local search through relevant Claims, source units, searchable contents and bibliography found no retained squared-Fejer/Jackson account at this scope.

The classical squared-Fejer construction was then checked in the primary Cambridge DAMTP course document [Part III, Lent Term 2005, Approximation Theory, Lecture9](https://www.damtp.cam.ac.uk/user/na/PartIIIat/b09.pdf), printed/PDF p.2, Definition9.5 and Lemma9.6.
Its kernel is the normalized square of a Fejer kernel, with degree and first-moment order at scale1/n.
For its n=2N the displayed m equals N; its mass-one dt kernel is J_N/(2pi) in the probability-Haar convention used here.
This citation supplies attribution to the classical Jackson construction, not a new proof premise.
All exact constants and finite identities needed below are proved directly.
The full course, historical Jackson proofs and general approximation theorems were not audited or invoked.
No local source artifact or new source-proof verdict is asserted by this bounded online passage inspection.
The original source and review scopes of the existing project interfaces remain unchanged.

## Complete argument

### 1. Exact mass, moment, tail and coefficient multipliers

The finite geometric expansion of F_N has coefficients
(1-|k|/N) for |k|<N and zero otherwise.
Finite probability-Haar orthogonality therefore gives

    c_N=1+2sum_(k=1)^(N-1)(1-k/N)^2
       =1+(2/N^2)sum_(l=1)^(N-1)l^2
       =(2N^2+1)/(3N)>=2N/3.

The formulas include N=1 with an empty sum.
The square has degree at most2N-2 and nonnegative Fourier coefficients, since those are the finite convolutions of the nonnegative coefficients of F_N.
Division by c_N preserves that sign.
Nonnegativity of J_N as a function and its integral one give
|Jhat_N(k)|<=integral J_N=1.
Thus all its Fourier multipliers belong to [0,1].

For 0<|t|<=pi, the finite sum and |sin(t/2)|>=|t|/pi give

    F_N(t)<=min{N,pi^2/(N t^2)},
    J_N(t)<=(3/2)min{N,pi^4/(N^3 t^4)}.

The values at0 follow by continuity.
By evenness the normalized first moment is pi^-1 integral_0^pi t J_N(t)dt.
On [0,pi/N] its unnormalized half-axis integral is at most3pi^2/(4N).
On [pi/N,pi], comparison with t^-3 gives the same upper bound.
Their sum divided by pi proves the first inequality of (PK1).
For the tail, evenness and integration of t^-4 give

    pi^-1 integral_delta^pi J_N(t)dt
       <=[3pi^3/(2N^3)]integral_delta^infinity t^-4 dt
       =pi^3/(2N^3 delta^3).

This proves (PK1).
For N_R=floor(R/2)+1, one has 2N_R-2<=R and N_R>=R/2.
Hence the support, first moment3pi/R and tail4pi^3/(R^3 delta^3) all follow.

Product convolution with the P_M kernels preserves positivity and integral one.
A telescoping coordinate change bounds its approximation error by the sum of coordinate Lipschitz constants times the corresponding first moment.
C632 supplies sums at most2A_der,K/sqrt(s) for r_s and
(A_der,K+1/2)/(tau sqrt(s)) for F_(tau,s), including the w coordinate.
Since A_der,K>=1, multiplication by3pi/M bounds both by (PK2), with D_J,K=6pi A_der,K.
The possible corner of psi_tau is covered by its global Lipschitz constant.
All common-zero and inversion qualifications remain those of the accepted amplitude derivative result.

### 2. Closed endpoints and original linear comparison

The actual original schedule satisfies H_j(delta)!=0 for every nonzero integer delta with ||delta||_infinity<=2M_j.
This is the CLOSED inequality already proved in C565 from the strict prime separations.
If Q is supported in [-M_j,M_j]^4 and gamma belongs to that same closed box, every support difference lies in the closed2M_j box.
Expanding the finite polynomial and integrating each character therefore proves (PK3).
It also proves pairwise distinctness of all H_j(gamma) for distinct gamma in that box.
No endpoint coefficient has been discarded.

For the linear comparison, put E_rho=D_J,K/(M_j sqrt(rho)) and B_rho=8rho^(2/3).
C633v2 gives the product-Haar integral of r_rho at most B_rho.
Smoothing r_rho with the new product kernel and using (PK3) for its mean gives the original-circle pushed mean at most B_rho+2E_rho.
Both uniform errors are paid.
The two phase-regularization differences cost at most
[(B_rho+2E_rho)+B_rho]/(2tau)=(B_rho+E_rho)/tau.
The two finite approximations of F_(tau,rho) cost another2E_rho/tau.
Finally the full original comparison ||k_j-Kcal composed with iota_j||_1<=epsilon_j and scalar Lipschitz constant1/tau cost epsilon_j/tau.
This proves (PK4) for every closed-box gamma.
Putting rho=M_j^(-6/7) gives the stated complete individual budget.
This proof assigns no independent coordinates to the original pushed-circle law.

### 3. Contact-scale squared error and every finite Fourier projection

Fix 0<tau<=1/64, 0<lambda<=1 and rho=tau lambda.
All original and regularized transforms take values in [0,1].
The actual pointwise phase comparison consequently implies

    |F_tau-F_(tau,rho)|^2
       <=min{1,[rho/(2tau(g+rho))]^2}.

Here g is evaluated at the inverse coordinates.
Write t_scale=g/lambda+tau>0.
For t_scale<=1/2, 2/(1+t_scale)>=1.
For t_scale>=1/2, (1+t_scale)/(4t_scale^2) is decreasing and has value3/2 at1/2, so it is at most2.
Thus

    min{1,1/(4t_scale^2)}
       <=2/(1+t_scale)<=2/(1+g/lambda)=2r_lambda.                  (PK11)

The last direction uses 1+t_scale>=1+g/lambda.
This pointwise estimate also holds at common zeros, where both original and regularized phases are zero.

The product-Haar mean of r_lambda is at most8lambda^(2/3) by adopted C633v2.
Its new product-kernel approximation and (PK3), with both errors, bound its original pushed-circle mean by

    8lambda^(2/3)+2D_J,K/(M_j sqrt(lambda)).

By (PK11), the torus regularization L2 cost is at most4lambda^(1/3), and the original-circle cost is at most

    4lambda^(1/3)+2sqrt(D_J,K)M_j^(-1/2)lambda^(-1/4).

For the second bound use sqrt(a+b)<=sqrt(a)+sqrt(b).
The original composition cost is at most sqrt(epsilon_j/tau), since its difference is bounded by one and has L1 norm at most epsilon_j/tau.
This does not presume a pointwise epsilon_j error.
For Q, the product P_M smoothing of F_(tau,rho), the two approximation costs are each at most D_J,K/(M_j tau sqrt(rho)).
The resulting sum of all five L2 costs is exactly Gamma_J.

For completeness, for any finite orthonormal character set E and any L2 function h, direct expansion gives

    ||h-sum_(gamma in E)hhat(gamma)chi_gamma||_2^2
       =||h||_2^2-sum_(gamma in E)|hhat(gamma)|^2>=0.

Apply this finite identity to the Gamma characters on the four-torus and their distinct actual H_j(Gamma) characters on the original circle.
The selected Q coefficients agree exactly by (PK3).
Their difference vector is therefore bounded by the two L2 norms
||f_(j,tau)-Q composed with iota_j||_2 and ||F_tau-Q||_2.
The complete five-cost bound proves (PK5), including Gamma empty and all fourth-coordinate signs.
No infinite Parseval identity or first-harmonic restriction is used.

When M_j^-1<=tau^(3/2), lambda_bal belongs to (0,1].
Direct substitution gives

    lambda_bal^(1/3)=M_j^(-2/5)tau^(-3/5),
    [M_j tau sqrt(tau lambda_bal)]^-1
        =M_j^(-2/5)tau^(-3/5),
    M_j^(-1/2)lambda_bal^(-1/4)
        =M_j^(-1/5)tau^(9/20).

These identities prove (PK6).
The choice is a legal balance, not a proved optimum.

### 4. New witness smoothing and every endpoint-inclusive coefficient

Use the same adopted C629v3 positive witness z_0=exp(i pi/K), u_(k,m) and neighborhood |arg z-pi/K|<=delta_0.
Its negative-v coefficient F_(k,m) of U^k has
|F_(k,m)(z_0,u_(k,m))|>=1/(8m).
Throughout that z interval the u derivative is at most8192(k+m) for every u, and at the fixed witness u the z derivative is at most(K+4)/m.
Globally |F_(k,m)|<=1 almost everywhere.

Convolve in z,u with P_(R_z),P_(R_u).
For z displacement within delta_0, first change u at the shifted z, then change z at the fixed witness u.
The two moment bounds give errors at most
24576pi(k+m)/R_u and 3pi(K+4)/(mR_z).
For z displacement outside the neighborhood, the unsplit difference is at most2, and its tail costs at most8pi^3/(R_z^3 delta_0^3).
This uses no u derivative in the exceptional z region and includes periodic arcs through u=1 via the same original rational formula.
Multiplying by m and maximizing over 1<=k<=L,1<=m<=J gives exactly T_J,K.
If this is at most1/16, the convolved witness has modulus at least1/(16m).

Its Fourier support is contained in the closed rectangle |p|<=R_z,|q|<=R_u, and the entire rectangle is retained in the following sum.
Every coefficient multiplier is in [0,1], so its value is at most the sum of the absolute original coefficients on that rectangle.
Summing over the disjoint m bands and using sum_(m=1)^J 1/m>=log(J+1) proves (PK7).

For the Wiener consumer retain the exact scalar harmonics and inverse phase from C629v3:

    |a_k(tau)|>=3sqrt(tau)/(8pi), 1<=k<=L_tau,
    L_tau sqrt(tau)>=1/8,
    Fhat_tau(eta,k)=a_k(tau)(U^k)hat(-eta).

Select the entire set

    G={(eta,k): -eta=(p,q,-m),
         |p|<=R_z, |q|<=R_u, 1<=m<=J, 1<=k<=L_tau}.

Its cardinality is exactly (2R_z+1)(2R_u+1)J L_tau and at most9L_tau R_z R_u J.
All its coordinates lie in the original closed box under the stated hypotheses.
The actual H_j frequencies are distinct by (PK3) and positive because c_j>M_j(1+a_j+b_j) and k>=1.
Thus none is the omitted zero coefficient of W_*.
Their total torus coefficient mass is at least3log(J+1)/(1024pi).
Finite Cauchy--Schwarz bounds the entire l1 error by sqrt(|G|)Gamma_J.
This proves (PK8), paying all endpoint coefficients and without an unused-negative-frequency factor.

### 5. Uniform arbitrary enlargement at the four-elevenths scale

Take C_Kern,J_0,H_0 as in the statement and let
H_0<=H<=M^(4/11)/64.
Define the cutoffs in (PK10).
Then J>=J_0>=2, R_z=J and L_max>=2.
For every tau in the strip, L_tau<=L_max.
The first T_J,K term is at most24576pi/C_Kern=1/64.
The next is at most3pi(K+4)/J_0<=1/64.
The tail term is at most8pi^3/(J_0^2 delta_0^3)<=1/64.
Their sum is at most3/64<1/16.

All closed support conditions hold uniformly for sufficiently large actual M.
Indeed

    J=R_z<=H^(1/4)<=M^(1/11),
    L_tau<=L_max<=M^(2/11)/4,
    R_u<=C_Kern[(1/4)M^(2/11)H^(-1/4)+H^(1/2)]+1
        <=(3C_Kern/8)M^(2/11)+1.

The last step uses H>=1 and H<=M^(4/11)/64.
Each is at most M after a threshold depending only on K.
The original schedule also supplies
epsilon_j<=C_epsilon M^-2(1+log M) beyond such a threshold.
Increase M_0 to satisfy these requirements and nonemptiness of the stated H range.

The balancing condition is uniform as well:

    M^-1/tau^(3/2)<=M^(-5/11)H^(-3/2)<=1.

Use (PK6) in (PK8).
Since J(L_max+J)>=1, the ceiling gives
R_u<=(C_Kern+1)J(L_max+J).
Since L_tau<=tau^-1/2/4, the full square-root support price obeys

    3sqrt(L_tau R_z R_u J)
      <=(3/2)sqrt(C_Kern+1)
          [J^(3/2)sqrt(L_max)+J^2]tau^(-1/4)
      <=C_support [M^(1/11)H^(1/8)+H^(1/2)]tau^(-1/4).           (PK12)

Here C_support depends only on the displayed fixed constants.
This is a bound on the entire selected support, not on a subset of its bands.

Multiply (PK12) by each of the three terms of Gamma_J,bal.
For its middle term use tau^(-17/20)<=M^(17/55)H^(-17/20).
The two resulting factors are

    H^(-29/40),
    M^(-1/11)H^(-7/20).                                          (PK13)

For the original-composition term use the complete epsilon_j bound and
tau^(-3/4)<=M^(3/11)H^(-3/4).
The resulting factors are

    M^(-7/11)H^(-5/8)(1+log M)^(1/2),
    M^(-8/11)H^(-1/4)(1+log M)^(1/2).                            (PK14)

For the remaining original-circle mean term, the residual width power is positive:
tau^(9/20-1/4)=tau^(1/5)<=1.
It must not be bounded above using the lower width.
The resulting factors are

    M^(-6/55)H^(1/8)<=M^(-7/110),
    M^(-1/5)H^(1/2)<=M^(-1/55).                                 (PK15)

The two last inequalities use H<=M^(4/11)/64 and absorb only fixed constants.
Every power in (PK13)--(PK15) follows from the complete support price and the three separate Gamma terms.
Using H>=1 and M>=2, all terms except H^(-29/40) are at most a constant multiple of M^(-1/55)(1+log M)^(1/2).
Their sum has exactly the error shape in (PK9).

Finally J+1>H^(1/4), so the unchanged main term is strictly greater than3log H/(4096pi).
This proves (PK9), with constants depending only on K and uniform over the full allowed H,tau region.

For any actual sequence tau_j->0 with H_enl,j=M_j^(4/11)tau_j->infinity, eventually H_enl,j>=H_0 and tau_j<=1/64.
Thus H_enl,j<=M_j^(4/11)/64 and the theorem applies with H=H_enl,j.
Its main term tends to infinity and both error terms tend to zero.
This proves the stated arbitrary-enlargement conclusion, without prescribing a logarithmic rate or asserting the case of bounded H.
All original family, normalization, contact and fixed-input boundaries remain unchanged.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision positive-kernel-critical-enlargement-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:31 |
| status | open |
| reason | Register the complete normalized positive squared kernel, exact moment/tail and closed-endpoint alias extension, all linear and quadratic original-return costs, endpoint-inclusive witness rectangle and arbitrary diverging enlargement at the original4/11 scale. Root and paid_comparison are contributors, with the reused finite-projection contribution of root/phase_bands retained. The classical Jackson construction is attributed at its inspected source scope; exact constants and all consumers are proved here. Fresh isolated whole review and adoption remain separate. Bounded enlargements, optimality, near-one inputs and unrestricted completion are not asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | PK1--PK10 and every actual original family, closed support, scalar parameter, finite coefficient set, full window and uniform H,tau/sequence quantifier, including empty Gamma and all harmonic signs. |
| argument | [Complete positive-kernel and original-return proof](#complete-argument) | Exact mass/moments/tails, Fourier multipliers and endpoint aliases, contact-scale majorant and five L2 costs, full finite projections, every witness coefficient, complete9L rectangle price, explicit cutoffs and six enlargement error powers. |
| dependency | [Adopted logarithm-free original probability](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Exact integral r_s<=8s^(2/3) for all0<s<=1 for the same original g; no inference from amplitude sharpness to Fourier or width optimality. |
| dependency | [Actual complete amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same Acal,Bcal,g,Ncal,A_der,K, both regularized derivative sums, common zeros, inversion and fourth-coordinate Lipschitz cost; new finite kernels and constants proved here. |
| dependency | [Original input and full residual kernel](Yin_C_G0565_v2.md#statement) | Actual fixed K and prime schedule, monic irreducible Salem polynomial, complete degree and original2d coefficient window. |
| dependency | [True original function comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Exact epsilon_j L1 error and scalar Lipschitz/range conversion; no uniform pointwise original-kernel estimate. |
| dependency | [Closed original2M alias exclusion](Yin_C_G0565_v2.md#moving-band-exact-alias) | Nonzero H_j on every nonzero closed2M integer difference; new closed-M polynomial and full-box coefficient identity explicitly deduced here. |
| dependency | [Original witnesses and separate derivatives](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Actual positive witness amplitude1/(8m), fixed z interval, uniform u derivative8192(k+m), fixed-witness z derivative(K+4)/m, global amplitude bound and original rational endpoint scope. |
| dependency | [Scalar harmonic and inverse-phase interface](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bounds, L_tau normalization and Fhat_tau(eta,k)=a_k(U^k)hat(-eta), reused with every new endpoint-inclusive coefficient paid. |
| dependency | [Actual schedule error](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K(M_j^-2(1+log M_j)) from original lower square separations, without an upper prime-gap estimate. |
| dependency | [Original contacts and fixed-input boundary](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual contact-minus-Haar margin, finite fixed-j Wiener norms and original two-limit restrictions, with the existing finite-orthogonality source scope unchanged. |
| support | [Classical kernel attribution and inspection limits](#source-and-reuse-boundary) | Exact Cambridge Lecture9 Definition9.5/Lemma9.6 passage, probability-normalization conversion and bounded original-proof inspection; attribution only, with no imported general approximation theorem. |
| support | [Prior finite quadratic author argument](Yin_C_G0635_v1.md#argument) | Actual root/phase_bands contact-scale and finite-projection development, repeated completely with the changed kernel; its review or adoption is not used prospectively as a proof premise. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:42 |
| status | proved |
| reason | Adopt the entire positive-kernel theorem after main reading of complete C637 and isolated whole R843, including direct main verification of the bounded classical kernel attribution. The exact mass/moments/tails and closed-box aliases support every original linear and quadratic cost. The full endpoint-inclusive witness rectangle and six paid error terms prove divergence for every shrinking sequence with M_j^(4/11)tau_j tending to infinity. Bounded enlargements, optimality and the unrestricted Mahler contract remain unresolved; all original2d/source/sequence boundaries remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact theorem](#statement) | PK1--PK10 and every actual original family, closed support, scalar parameter, finite coefficient set, full window and uniform H,tau/sequence quantifier, including empty Gamma and all harmonic signs. |
| argument | [Complete positive-kernel and original-return proof](#complete-argument) | Exact mass/moments/tails, Fourier multipliers and endpoint aliases, contact-scale majorant and five L2 costs, full finite projections, every witness coefficient, complete9L rectangle price, explicit cutoffs and six enlargement error powers. |
| dependency | [Adopted logarithm-free original probability](Yin_C_G0633_v2.md#additional-complete-logarithm-free-and-two-sided-argument) | Exact integral r_s<=8s^(2/3) for all0<s<=1 for the same original g; no inference from amplitude sharpness to Fourier or width optimality. |
| dependency | [Actual complete amplitude derivatives](Yin_C_G0632_v1.md#square-root-regularization-derivative) | Same Acal,Bcal,g,Ncal,A_der,K, both regularized derivative sums, common zeros, inversion and fourth-coordinate Lipschitz cost; new finite kernels and constants proved here. |
| dependency | [Original input and full residual kernel](Yin_C_G0565_v2.md#statement) | Actual fixed K and prime schedule, monic irreducible Salem polynomial, complete degree and original2d coefficient window. |
| dependency | [True original function comparison](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Exact epsilon_j L1 error and scalar Lipschitz/range conversion; no uniform pointwise original-kernel estimate. |
| dependency | [Closed original2M alias exclusion](Yin_C_G0565_v2.md#moving-band-exact-alias) | Nonzero H_j on every nonzero closed2M integer difference; new closed-M polynomial and full-box coefficient identity explicitly deduced here. |
| dependency | [Original witnesses and separate derivatives](Yin_C_G0629_v3.md#witness-specific-anisotropic-refinement) | Actual positive witness amplitude1/(8m), fixed z interval, uniform u derivative8192(k+m), fixed-witness z derivative(K+4)/m, global amplitude bound and original rational endpoint scope. |
| dependency | [Scalar harmonic and inverse-phase interface](Yin_C_G0629_v3.md#many-harmonic-transfer) | Exact a_k lower bounds, L_tau normalization and Fhat_tau(eta,k)=a_k(U^k)hat(-eta), reused with every new endpoint-inclusive coefficient paid. |
| dependency | [Actual schedule error](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K(M_j^-2(1+log M_j)) from original lower square separations, without an upper prime-gap estimate. |
| dependency | [Original contacts and fixed-input boundary](Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Actual contact-minus-Haar margin, finite fixed-j Wiener norms and original two-limit restrictions, with the existing finite-orthogonality source scope unchanged. |
| support | [Classical kernel attribution and inspection limits](#source-and-reuse-boundary) | Exact Cambridge Lecture9 Definition9.5/Lemma9.6 passage, probability-normalization conversion and bounded original-proof inspection; attribution only, with no imported general approximation theorem. |
| support | [Prior finite quadratic author argument](Yin_C_G0635_v1.md#argument) | Actual root/phase_bands contact-scale and finite-projection development, repeated completely with the changed kernel; its review or adoption is not used prospectively as a proof premise. |
| review | [Independent whole positive-kernel finding](../audits/reviews/Yin_R_G0843_v1.md#positive-kernel-critical-whole-independent-finding) | Entire PK1--PK15, every kernel/support endpoint and finiteGamma case, all original probability/projection/regularization costs, explicit uniformH cutoffs and six error powers, plus bounded primary attribution; previous reviews and source-proof limits retained. |


---
author: Yin
---

# Product tails and square-root regularization for the actual original coefficient return

Human author Yin.
Root derived and checked the new product-tail, amplitude-derivative and original-return bounds below.
This fixed author theorem requires fresh isolated whole review.
The accepted C565/C569 source interfaces and their historical SELF/UNKNOWN scopes are reused without an original-proof upgrade.
No numerical experiment, new source acquisition or new external theorem is used.

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
Define

    A_K=1+||g||_infinity+||Ncal||_infinity
        +sum_(l=1)^3(||partial_l g||_infinity+||partial_l Ncal||_infinity),
    D_K=8pi A_K^2.
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

Use natural logarithms and log_+(x)=max{0,log x}.
For normalized three-torus Haar nu, EVERY s>0 and EVERY0<rho<=1 satisfy

    nu{g<=s}<=min{1,2sqrt(s)[1+log_+(1/s)]^2},
    r_rho=rho/(g+rho),
    integral r_rho dnu<=12sqrt(rho)[1+log(1/rho)]^2.

For U_rho=Ncal/(g+rho), the sum of its three angular derivative suprema and the corresponding sum for r_rho are each at most2A_der,K/sqrt(rho).
The bounds include common zeros of Acal,Bcal and are retained under coordinate inversion.
Put

    V(z,u,v)=U(z^-1,u^-1,v^-1),
    Kcal=(1-Re(wV))/2, F_tau=psi_tau(Kcal),
    f_(j,tau)=psi_tau(k_j),
    iota_j(z)=(z,z^a_j,z^b_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+b_j gamma_2+c_j gamma_3.

For EVERY such j, EVERY0<tau<=1, EVERY0<rho<=1 and EVERY gamma in[-M_j,M_j]^4 intersection Z^4,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=[epsilon_j+12sqrt(rho)[1+log(1/rho)]^2
                           +3D_reg,K omega_j/sqrt(rho)]/tau.

Both coefficients use the specified original normalized Haar conventions and full original2d_j window.
Taking rho=omega_j defines

    beta_new,j=epsilon_j+12sqrt(omega_j)[1+log(1/omega_j)]^2
                                +3D_reg,K sqrt(omega_j),

which supplies error beta_new,j/tau throughout the SAME complete4box and obeys

    beta_new,j=O_K(M_j^-1/2(1+log M_j)^(5/2)).

All constants are independent of j,tau,gamma, except for the explicitly displayed actual quantities.
The proof uses independent coordinates only on the product three-torus, never on the original pushed-circle law.
No infinite Fourier sum is controlled by this individual-coefficient estimate alone.
The original family remains in log2<m(P_j)<log4; no arbitrary-width Wiener theorem, near-one input or unrestricted Mahler conclusion is asserted.

## Reuse and source boundary

The directly used C565v2 Sections3--4, exact original domain and universal4box comparison were read before the refinement.
C569v2 supplies the original schedule asymptotic, while the same fixed C172 Fejer moment supplies the existing normalized finite-kernel interface.
Those accepted arguments do not supply the new complete product tail or amplitude-sensitive derivative estimates.
The proof supplies the generalized-inverse comparison, direct three-product integration, complete shell sum and every differentiated polynomial inequality locally.
The original coarse regularization theorem remains valid and fixed.
No classical original-proof review or historical SELF/UNKNOWN relationship is enlarged here.

## Complete argument

<a id="argument"></a>

<a id="independent-product-sublevel"></a>
## Complete product sublevel estimate

On the normalized three-torus, R=(z^K-1)(u-1)(v-1), g=|Acal|^2+|Bcal|^2 and g>=|R|^2/2 as in C565.
Put X1=min(1,|z^K-1|), X2=min(1,|u-1|), X3=min(1,|v-1|).
These variables are independent, and for0<=t<=1 each satisfies Pr(Xi<=t)<=t, because the same original circle-distance estimate applies and z to z^K preserves Haar.
Thus each Xi stochastically dominates a uniform[0,1] variable.
This last implication can be proved without a theorem by its generalized inverse distribution function: for a uniformU the inverse Fi^(-1)(U) is at leastU, with endpoint choices irrelevant to probability, and has the law of Xi.
Use three independent uniforms for the product comparison.
For0<t<=1, direct successive integration over[0,1]^3 gives

    Pr(U1 U2 U3<=t)=t[1+log(1/t)+(log(1/t))^2/2].

Since |R|>=X1 X2 X3, the event g<=s implies X1 X2 X3<=sqrt(2s).
For0<s<=1/2 this yields the explicit product bound at t=sqrt(2s).
For all s>0, extending by the trivial probability bound1, it in particular gives

    nu{g<=s}<=min{1,2sqrt(s)[1+log_+(1/s)]^2}.        (PR1)

No common-zero geometry or uniform root separation is assumed.
The bound uses all three independent Haar coordinates of the actual fixed phase.

For0<rho<=1 retain r_rho=rho/(g+rho).
On g<=rho use (PR1); on2^k rho<g<=2^(k+1)rho use r_rho<=2^-k and (PR1) at the upper endpoint.
The logarithmic bracket at every such endpoint is at most L_rho=1+log(1/rho).
Therefore

    integral r_rho dnu
       <=[2+2sqrt(2)/(1-2^-1/2)]sqrt(rho)L_rho^2
       =(6+4sqrt(2))sqrt(rho)L_rho^2
       <=12sqrt(rho)L_rho^2.                       (PR2)

The convergent shell estimate remains valid after its probability upper bound exceeds1.

<a id="square-root-regularization-derivative"></a>
## Regularization derivatives from the actual polynomial amplitudes

Define the fixed finite original-polynomial constant

    A_der,K=1+sum_l(||partial_l Acal||_infinity
                              +||partial_l Bcal||_infinity),
    D_reg,K=4pi A_der,K,

where l ranges over the three angular coordinates.
For D_l=(|partial_l Acal|^2+|partial_l Bcal|^2)^(1/2), the pointwise Cauchy--Schwarz inequality gives

    |partial_l g|<=2D_l sqrt(g),
    |partial_l Ncal|<=2D_l sqrt(g), |Ncal|<=g.

With U_rho=Ncal/(g+rho), quotient differentiation gives

    |partial_l U_rho|
       <=4D_l sqrt(g)/(g+rho)<=2D_l/sqrt(rho).

For r_rho, the same calculation gives

    |partial_l r_rho|<=2D_l rho sqrt(g)/(g+rho)^2
                              <=2D_l/sqrt(rho).

The last bound uses sqrt(t)/(1+t)^2<=1 for t>=0, with t=g/rho.
These hold at g=0 by the displayed polynomial derivative identities as well.
Summing the complete angular derivatives costs at most2A_der,K/sqrt(rho) for either regularized function.
Inversion of coordinates preserves the bounds.

For the same Kcal_rho=(1-Re(w U_rho(inverse coordinates)))/2 and F_(tau,rho)=psi_tau(Kcal_rho), its sum of four coordinate Lipschitz constants is at most (A_der,K+1/2)/(tau sqrt(rho)).
The w derivative is at most1/(2tau), and rho<=1 pays it in the displayed bound.
All functions still take values in[0,1], and |F_tau-F_(tau,rho)|<=r_rho/(2tau) with the SAME original inverse phase.
Product Fejer convolution of degreeM-1, with omega=(1+logM)/M, therefore has uniform errors bounded by

    D_reg,K omega/(tau sqrt(rho)) for F_(tau,rho),
    D_reg,K omega/sqrt(rho) for r_rho.               (PR3)

This follows from the existing normalized first moment and the full coordinate sum, without dropping a coordinate or replacing the actual phase.

<a id="improved-universal-coefficient-return"></a>
## Every coefficient in the same original four-dimensional box

Retain C565v2's exact original schedule, M_j and epsilon_j, with M_j>=2.
The original no-alias theorem applies to the entire product Fejer polynomial and every gamma in[-M_j,M_j]^4.
Applying it to the r_rho convolution, then paying its two uniform errors, gives the actual pushed-circle bound

    integral r_rho(inverse coordinates) dmu_j
       <=12sqrt(rho)L_rho^2+2D_reg,K omega_j/sqrt(rho).

The exact same complete function-comparison chain as C565 equation(11) now yields, for EVERY0<tau<=1 and EVERY gamma in that full box,

    |fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma)|
       <=[epsilon_j+12sqrt(rho)L_rho^2
                         +3D_reg,K omega_j/sqrt(rho)]/tau.    (PR4)

Both regularization terms, both Fejer errors, the original epsilon_j and every probability normalization are present.
Take rho=omega_j, which lies in(0,1) for M_j>=2, and define

    beta_new,j=epsilon_j+12sqrt(omega_j)[1+log(1/omega_j)]^2
                              +3D_reg,K sqrt(omega_j).

Then (PR4) is beta_new,j/tau, and the original schedule gives

    beta_new,j=O_K(M_j^-1/2(1+log M_j)^(5/2)).        (PR5)

This changes no original input, coordinate dimension, Haar law, finite alias box or contact convention.
The constants are fixed by K and independent of j,tau,gamma.
No uniform infinite-series comparison is inferred from the individual coefficients.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:46 |
| status | open |
| reason | Register the complete original product-sublevel bound, amplitude-sensitive regularization derivatives and universal4box coefficient comparison with explicit square-root budget. Root is contributor. The entire source law, finite alias box, every regularization/Fejer cost and actual input are retained. Fresh isolated whole review and adoption remain separate; no thin-width or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire explicit theorem](#statement) | Every s>0,rho in(0,1],tau in(0,1] and actual4box gamma, full original family/window, derivative constants and complete budget asymptotic, with exact uniformity and limits. |
| argument | [Complete PR1--PR5 proof](#argument) | Three independent Haar factors, inverse-distribution product comparison, direct integration, complete shell sum, all amplitude derivatives and original-circle costs. |
| dependency | [Actual denominator identity](Yin_C_G0565_v2.md#moving-band-denominator) | Same explicit R,Acal,Bcal,g,Ncal, g>=abs(R)^2/2 and equal-modulus phase identity; the old coarse tail is not substituted for the new proof. |
| dependency | [Complete original return chain](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Full original error epsilon_j, all regularization/product Fejer comparisons, normalization and universal4box coefficient scope. |
| dependency | [Exact original aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Exact finite product means/coefficient identities for every gamma in the4box; no independence of pushed-circle coordinates. |
| dependency | [Actual complete family/projection](Yin_C_G0565_v2.md#statement) | Fixed K/prime schedule, actual monic irreducible Salem P_j, original d_j and full2d_j matrix/kernel. |
| dependency | [Original schedule asymptotic](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K((1+log M_j)/M_j^2) from actual lower square separations, without an upper prime-gap estimate. |
| dependency | [Normalized Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Probability-Haar normalization, finite degree and first moment, paying every coordinate of both regularized functions at the existing source scope. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:53 |
| status | proved |
| reason | Adopt the complete product-tail and amplitude-sensitive regularization theorem after main reading of the entire fixed C and isolated whole R836. The independent three-torus product bound, all shell constants, common-zero derivative conditions and all four-coordinate/original-circle costs support the exact universal4box comparison and square-root budget. No independence is assigned to the pushed-circle law, and no infinite Fourier sum or unrestricted Task conclusion follows from the coefficient estimate alone. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire explicit theorem](#statement) | Every s>0,rho in(0,1],tau in(0,1] and actual4box gamma, full original family/window, derivative constants and complete budget asymptotic, with exact uniformity and limits. |
| argument | [Complete PR1--PR5 proof](#argument) | Three independent Haar factors, inverse-distribution product comparison, direct integration, complete shell sum, all amplitude derivatives and original-circle costs. |
| dependency | [Actual denominator identity](Yin_C_G0565_v2.md#moving-band-denominator) | Same explicit R,Acal,Bcal,g,Ncal, g>=abs(R)^2/2 and equal-modulus phase identity; the old coarse tail is not substituted for the new proof. |
| dependency | [Complete original return chain](Yin_C_G0565_v2.md#moving-band-fejer-budget) | Full original error epsilon_j, all regularization/product Fejer comparisons, normalization and universal4box coefficient scope. |
| dependency | [Exact original aliases](Yin_C_G0565_v2.md#moving-band-exact-alias) | Exact finite product means/coefficient identities for every gamma in the4box; no independence of pushed-circle coordinates. |
| dependency | [Actual complete family/projection](Yin_C_G0565_v2.md#statement) | Fixed K/prime schedule, actual monic irreducible Salem P_j, original d_j and full2d_j matrix/kernel. |
| dependency | [Original schedule asymptotic](Yin_C_G0569_v2.md#static-phase-original-return) | epsilon_j=O_K((1+log M_j)/M_j^2) from actual lower square separations, without an upper prime-gap estimate. |
| dependency | [Normalized Fejer moment](Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Probability-Haar normalization, finite degree and first moment, paying every coordinate of both regularized functions at the existing source scope. |
| review | [Independent whole product-return finding](../audits/reviews/Yin_R_G0836_v1.md#product-return-whole-independent-finding) | Entire statement and PR1--PR5, every finite parameter, original family/window, capped-factor atom, complete shell sum, amplitude derivatives, exact aliases/phase orientation and all five comparison costs; existing current SELF, historical UNKNOWN and source-original proof limits retained. |


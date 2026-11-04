---
author: Yin
---

# Complete zero-correction canonical families with doubled support and gate precision

Human author Yin.
Root derived this complete parameter family, negative-character whole factor, exact extended finite target, doubled local identities and paid global costs as sole contributor.
This is an author-checked candidate under the [active G0001 Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23), initially open for fresh isolated whole review.
The adopted C665 complete-character certificate, C668v2 exact zero-correction formal calibration, C664 all-depth kernel and C667 global representative construction were directly inspected.
The C643v2 endpoint proof supplies its exact simultaneous approximation order, not an assumed arbitrary extension of the old gate.
No native prime search, coefficient construction, parameter enumeration or new external source is used.
The new parameter range and extended finite class have no existing responsible fixed theorem; older families and their costs remain unchanged.

## Statement

Work over F_2 with phi=X^2+X+1, chi=Xphi^2 and Psi=phi(chi).
Use B_n and W_n for the complete nonidentity and primitive odd-order trace polynomials, and ell for the calibrated character on1+tF_2[[t]], with ell(1+t)=1.
Let

    S_13={3,7,11,19,23,31,43,47,59,67,71,79,83},
    n_-=103 product_(p in S_13)p,
    A=(1/4)product_(p in S_13)(p+1),
    D=(1/2)product_(p in S_13)(p-1),
    A_-=104A, D_-=102D.

For EVERY integer s>=82 and k>=0 put

    Q=2^s, m=Q/4-2, q=2^k,
    k_m=ceil(m/(2A_-)), b_m=k_m A_--m/2,
    H=W_(n_-)^(k_m)W_3^(b_m),
    B=X^(Q-m)H(chi), S=0.                              (DG1)

The indices s and k are independent; Q is the homogeneous endpoint exponent and q is the raised Frobenius power.
Then H is a monic complete polynomial with H(0)=1 and

    ell(H)=-m/2,
    degH<(m-8)/5,
    2m<4m<Q=4m+8<5m,
    degB=Q-m+5degH<4m.                                (DG2)

Define the full formal low unit, using the compositional inverse x of chi at0,

    h_Q(X)=1+sum_(i=0)^(s-1)X^(Q-2^i),
    Ltilde(t)=[phi(t)^(7m)H(t)h_Q(x(t))]^(-1).

Put N=8m=2Q-16, and prescribe the extended class c in
R_N=F_2[X]/(X^N phi^(2N)) by

    c=Ltilde(X)^2 modulo X^N,
    c=X^(-2m)B^(-7) modulo phi^(2N).                    (DG3)

The low inverse has constant1; every high inverse is a phi-unit.
Its exact original-quotient finite character vanishes:

    Pi_N(c)=0 in Z/(Q).                                (DG4)

There is consequently a monic complete Y prime to Xphi representing DG3, with every occurring irreducible multiplicity at least2, with Y|Y(chi) and Y|Y(X^3+X), and with Y and YB globally nonsquare.
Set the actual global polynomials

    H_0=X^(2m)Y, U_0=H_0phi^(14m),
    R_0=H_0phi^(12m)B, V_0=H_0B,
    C_00=X^(2m)Y(chi)Psi^(14m), D_0=V_0+C_00^3.

They satisfy the complete original characteristic-two identities

    R_0=rem_(U_0)(U_0(chi)^3),
    U_0|U_0(X^3+X), X^N|Y',                           (DG5)

and the STRONGER local identities

    H_0=B^(-7), C_00=beta^2B^(-2), D_0=0,
    H_0^6=C_00^21                                  modulo phi^(16m),
    Z_0=beta^2B^(-1), Z_0^11=H_0C_00^2,
    Z_0D_0=0                                      modulo phi^(16m). (DG6)

Here beta is the unique cube-one unit with residue X^Q at phi, used at the full displayed precision; it can concretely be represented by X^(2^a) with2^a>=16m and2^a congruent Q modulo3.
The eleventh root is the unique unit root at this precision.
The old gate at8m and root at6m are retained as restrictions, not replaced.

Both U_0 and R_0 are nonsquares with a shared fresh factor of exact multiplicity3.
Thus U=U_0^q,R=R_0^q have actual maximal Frobenius power q separately, with R=rem_U(U(chi)^3) and U|U(X^3+X).
All DG6 precisions raise by q.
The sole unsaturated factor remains phi, with orders14mq and12mq.

Use the ACTUAL integer layers a_0=12mq and a_b=0 for b>=1.
Their total weight is12mq and their strict-window correction is exactly zero.
Because H and Y are complete, write

    V_0=X^(m+Q) product_(ell odd,ell>1,ell!=5)W_ell^(nu_ell).

With F_4=X and the monic integer trace polynomials F_ell defined by
Phi_ell(z)=z^(varphi(ell)/2)F_ell(z+z^(-1)), the actual integer polynomial

    G_int=F_4^(q(m+Q)) product_ell F_ell^(q nu_ell)
                                  F_5^(12mq)            (DG7)

has reduction R, full degree degR, and zero normalized circle Haar integral of log(G_int(z+z^(-1))^2), with the integrable logarithm convention at its zeros.
Every full primitive factor and coincidence is retained.
This synthetic integer polynomial is not identified with the canonical G_can of an integer T.

One may choose Y with the explicit full bounds

    degY<=14400Q^3+1206Q^2+120Q,
    r_deg=q(30m+degY), w_deg=q(26m+degY+degB),
    r_deg-w_deg=q(m-8-5degH)>5qm/256,
    r_deg<=q(14400Q^3+1206Q^2+128Q).                    (DG8)

A reciprocal original realization would have degree2r_deg, not the finite dimension5N.
These new doubled-precision inputs do not assert same-polynomial modulo16 residual solvability, characteristic-zero equations, G_int=G_can, irreducibility or original realization.
The separate adopted C686 construction applies at q>=256 through the unchanged strong-forward/old-support hypotheses, giving its stated modulo8 conclusion only.

## Argument

### 1. An explicit negative whole character with all costs paid

The adopted C665 certificate gives that all thirteen primes are distinct,3 modulo4, and

    ell(W_(product S_13))=A>0,
    A<2^63,
    1/5-D/(2A)>1/128.

The additional103 is prime: sqrt(103)<11, so only2,3,5,7 need be tested; it is odd and has respective nonzero remainders1,3,5 modulo3,5,7.
It is3 modulo4, is different from every old prime, and is prime to5.
Thus n_- is squarefree with fourteen3-modulo4 prime factors.
The exact C665 divisor formula gives

    ell(W_(n_-))=-(1/4)product_(p|n_-)(p+1)=-104A=-A_-,
    degW_(n_-)=102D=D_-.

Since102/104<1,

    1/5-D_-/(2A_-)>1/128.

The complete factors have constant1 and are monic.
The ceiling in DG1 gives0<=b_m<A_-, and

    ell(H)=-k_m A_-+b_m=-m/2,
    degH=k_m D_-+b_m
         <(D_-/(2A_-))m+D_-+A_-
         <m/5-m/128+D_-+A_-.                           (DG9)

All multiplicities are nonnegative integers; no negative polynomial exponent is used in H.
From D<2A/5 one obtains

    A_-+D_-<146A<2^71.

For Q>=2^82, m>=2^80-2, hence

    m/256>2^71+2>A_-+D_-+8/5.

It follows that degH<(m-8)/5 and, more strongly,

    m-8-5degH>5m/128-5(A_-+D_-)-8>5m/256.

The stated endpoint inequalities follow from Q=4m+8 and m>8.
The actual complete pullbacks W_n(chi)=W_n W_(5n) apply because n_- and3 are prime to5, and retain both5n_- and15.
This proves all of DG2 and the gap estimate without computing any enormous polynomial.

### 2. Exact extended finite character

Take the completed pair

    u(X)=Ltilde(X)^2,
    v(X)=X^(5m-7Q)H(chi(X))^(-7).

It lifts exactly DG3 because v=X^(-2m)B^(-7).
Use the directly checked zero-correction calibration of C668v2, which follows from C652's formal identities and applies to this explicitly specified pair, without assuming an original T.
To show every term, those identities are

    ell(phi)=-1,
    ell(h_Q)=Q/2,
    ell(f(x(t)))=ell(f)/5,
    ell(Ltilde)=7m-ell(H)-Q/10,
    ell(N_high(X))=-2/5,
    N_high(H(t))=H(t)^4.

Thus for Phi(u,v)=ell(N_high(v))-(4/5)ell(u),

    Phi(u,v)=(-330m+74Q-660ell(H))/25.

Indeed the high contribution is-(10m-14Q)/5-28ell(H), and the subtracted low contribution is(8/5)(7m-ell(H)-Q/10); their sum is the displayed formula.
With ell(H)=-m/2 it becomes

    Phi(u,v)=74Q/25,
    Pi(u,v)=Phi(u,v)/2=37Q/25.                          (DG10)

The denominator25 is a2-adic unit, so Pi is divisible by Q.
For N=2Q-16 and Q>=32 one has Q<=N<2Q, hence2^floor(log_2 N)=Q.
The adopted C654 character is lift-independent at exactly this modulus on R_N.
Therefore DG10 proves DG4 for the complete prescribed finite class, including its true low and high precision.
There is no factor-of-two substitution between Phi and Pi and no unknown higher coefficient is supplied as evidence.

### 3. Global complete representative and canonical identity

Apply the adopted C664 equality G_N=kerPi_N at this N.
Use C667 FC1--FC3 at this actual precision: its exact coprime-three ordinary/divided rows give a complete Y_pre with both global forward divisibilities.
Replace every row exponent1 by e+1, where e is its safe exponent, to enforce multiplicity at least2 without changing the finite class.
Multiply by B_n^3 for the explicitly chosen invisible fresh odd order n described in Section5.
That factor is1 in R_N, preserves both global forward divisibilities, and supplies a common exact triple irreducible outside the entire B.
Thus Y represents DG3, all its multiplicities are at least2, and both Y and YB are nonsquares.

Restriction of DG3 to R_(4m) is exactly C667 C1 with S=0.
For its low component, reducing Ltilde(X)^2 modulo X^(4m) is the same as the prescribed degree<2m L_0(X^2), since the coefficient field is F_2.
The high component is precisely X^(-2m)B^(-7) modulo phi^(8m).
Consequently the all-primary argument C667 FC4 applies to this SAME Y, not a newly substituted representative.
It proves DG5's canonical identity, the single unsaturated phi component, original degree formulas, and the maximal-q statements from the fresh triple factor.
The stronger derivative assertion follows directly from DG3: its low jet is square and N=8m is even, so differentiating Y=Ltilde(X)^2 modulo X^N gives X^N|Y'.
The complete polynomial lift is finite, although the defining target is specified by a formal series.

### 4. The actual doubled local precision

Let t=chi(X) in the phi-adic completion and put

    R_f=X^Q/h_Q(x(t)).

The C643v2 sharp endpoint proof gives the stronger explicit approximation used here.
At every primitive fifth root write z=xi^j v, w=v-1 and X_0=v+v^(-1).
Its exact identities SC13--SC14 state

    ord_w(v^Q+h_Q(X_0))=2Q-1,
    X(z)^Q=gamma_j v^Q+xi^(-jQ)X_0^Q,
    chi(X(z))=chi(X_0),

where gamma_j is the nontrivial cube-one constant with the appropriate residue, X_0 has order2, and the second displayed summand has order2Q.
The inverse identity x(chi(X_0))=X_0 therefore gives

    R_f=gamma_j modulo w^(2Q-1)

at all four roots.
The substitution preserves the phi-local order because both phi(X(z)) and X(z)-X(xi^j) have simple zeros there.
The constants gamma_j give precisely the Teichmuller unit beta at the two trace roots.
It follows in the actual high completion that

    R_f=beta modulo phi^(2Q-1).                         (DG11)

This is the explicit approximation order, not a claim at the forbidden next endpoint2Q.

DG3's low jet determines Y(chi) modulo phi^(2N).
Its high jet directly gives H_0=B^(-7) modulo phi^(2N).
Substituting the full low expression and cancelling Psi^(14m) yields

    C_00=X^(2m)H(t)^(-2)h_Q(x(t))^(-2)
         =R_f^2 B^(-2) modulo phi^(2N).

Since2N=16m=4Q-32<4Q-2, squaring DG11 proves

    C_00=beta^2 B^(-2) modulo phi^(16m).

Every extra low coefficient is multiplied by chi^N and has phi-order at least2N; none was dropped too early.
Now H_0B=B^(-6)=C_00^3, and H_0^6=B^(-42)=C_00^21, because beta^3=1.
Thus D_0=0 and the strengthened old relation hold at16m.
Finally

    (beta^2 B^(-1))^11=beta B^(-11)=H_0 C_00^2

at that same precision.
The eleventh-power map is an automorphism of the unit group, whose order is3*4^(16m-1), so the root is unique.
Its product with D_0 vanishes at16m.
This proves every DG6 assertion and its scaled-q version.
No unrestricted original field equation follows from these characteristic-two equalities.

### 5. Explicit complete degree and fresh-factor expenses

Here N=2Q-16, so C664/C667's safe parameters are EXACTLY

    L=4Q, e=12Q,

because L is the least power of2 at least2N+1=4Q-31, and e is3 times the least power of2 at least2N=4Q-32.
The support-floor adjustment costs at most75L^2(e+1).
Let D_B=degB<Q, and K_bound=max(30L,4D_B^2).
Since Q>30, K_bound<4Q^2.
The C667 construction chooses an odd n=1 modulo10L, coprime15, with

    K_bound<n<=K_bound+20L+1<4Q^2+80Q+1.

Its whole B_n is1 in R_N.
Every previous primitive support order is below30L, and the elementary totient bound degW_n>=sqrt(n)/2>D_B supplies a fresh irreducible outside B.
The exact triple multiplicity and global nonsquareness therefore hold at this extended precision, not merely after a smaller projection.
All costs give

    degY<=75(4Q)^2(12Q+1)+3(n-1)/2
          <=14400Q^3+1206Q^2+120Q.

The actual r_deg adds30m<15Q/2, giving the displayed conservative128Q linear coefficient.
The gap was already proved in Section1.
This accounts for every row, support-floor change and invisible factor.

### 6. Integer layers and the precise residual boundary

The specified integers a_0=12mq and all other a_b=0 have the required original weight; lambda_0=1 is below8mq and outside the strict correction window.
They therefore give S_star=0 with no normalized multiplicity reassignment.
The whole H assumption, retained complete Y, and complete substituted factors give the exact V_0 factorization in DG7.
Apply the C667/C199 integer trace-factor interface to every factor and these actual layers.
It gives reduction R_0^q, degree w_deg and the zero probability-Haar logarithmic integral, without discarding scalar, endpoint, repeated or higher-five contributions.

The normalized data a=2m,Y_b=Y meet C686's strong-forward and old-support assumptions.
Its degree margin follows from the same fresh-factor lower degree used in C667, so C686 applies at q>=256 at its stated scope.
That theorem yields both actual canonical residuals modulo8 and no higher precision.
The present stronger characteristic-two data are additional possible inputs to a subsequent actual coefficient analysis.
They do not make integer halves or changing-divisor terms vanish automatically and do not identify G_int with G_can.
All original characteristic-zero and unrestricted Task obligations remain.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:30 |
| status | open |
| reason | Register the complete new Q=4m+8 zero-correction canonical family, explicit negative whole character and strict degree margin, exact extended Pi_N=0, actual doubled16m support/root/gate, all-primary canonical/maximal-q data, integer zero-Haar layers and fully paid degree bound. Root is sole contributor; fresh isolated whole review is required. No modulo16 residual or original characteristic-zero solution is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire doubled-precision family](#statement) | DG1--DG8, every s>=82 and q, all actual parameters, full complete representative and canonical data, doubled local identities, integer layers and degree costs, with the higher-residual boundary. |
| argument | [Complete construction and expense](#argument) | DG9--DG11 and all six sections, explicit negative factor, exact Phi/Pi distinction and finite depth, global row/padding/fresh construction, simultaneous actual high approximation, full degree and integer-layer accounting. |
| dependency | [Explicit positive whole-character certificate](Yin_C_G0665_v1.md#large-dyadic-complete-h-statement) | Thirteen exact primes, A,D and strict1/128 margin, complete character formula; the additional103 and negative ceiling construction are proved here. |
| dependency | [Exact all-depth complete kernel](Yin_C_G0664_v1.md#statement) | Every N finite equality, safe rows/periods/exponent and exact original quotient; applied at N=8m. |
| dependency | [Complete global representative mechanism](Yin_C_G0667_v1.md#argument) | FC1--FC4 row multiplicities, both forward divisibilities, support floor, invisible fresh triple factor and all-primary canonical proof, with the new N costs paid here. |
| dependency | [Finite normalized character](Yin_C_G0654_v1.md#statement) | Pi=Phi/2, integrality and lift-independent modulus2^floor(log_2 N) on the actual quotient. |
| dependency | [Exact zero-correction formal calibration](Yin_C_G0668_v2.md#argument) | SY2 and SY9 full Ltilde/high pair and calibrated Phi formula, applied to explicitly supplied formal data without an original T; no old family target success is transferred. |
| dependency | [Sharp simultaneous high approximation](Yin_C_G0643_v2.md#argument) | SC13--SC14 exact order2Q-1 and all four fifth-root substitutions, with actual trace-local order preservation; the next endpoint is not asserted. |
| dependency | [Original integer trace-factor interface](Yin_C_G0667_v1.md#statement) | C8 and its retained C199 source depth, full monic integer factors, original layer indices, reduction, degree and zero Haar mean under whole H. |
| support | [Actual modulo8 construction](Yin_C_G0686_v1.md#decision-whole-reviewed-2026-10-24) | Applies through the proved strong-forward and old-support data at q>=256, with its original degree margin; supplies no modulo16 or characteristic-zero conclusion. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:42 |
| status | proved |
| reason | The complete fixed DG1--DG11 statement and six-section argument were directly read, followed by all of fresh isolated R911. Adopt the actual Q=4m+8 family with negative whole character, extended finite Pi_N=0, same global complete Y, doubled16m support/root/gate, exact maximal q, full integer zero-Haar layers and all paid degree bounds. C686 applies only at its separately stated q>=256 modulo8 scope; no modulo16 residual or original characteristic-zero realization is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire doubled-precision family](#statement) | DG1--DG8, every s>=82 and q, all actual parameters, full complete representative and canonical data, doubled local identities, integer layers and degree costs, with the higher-residual boundary. |
| argument | [Complete construction and expense](#argument) | DG9--DG11 and all six sections, explicit negative factor, exact Phi/Pi distinction and finite depth, global row/padding/fresh construction, simultaneous actual high approximation, full degree and integer-layer accounting. |
| dependency | [Explicit positive whole-character certificate](Yin_C_G0665_v1.md#large-dyadic-complete-h-statement) | Thirteen exact primes, A,D and strict1/128 margin, complete character formula; the additional103 and negative ceiling construction are proved here. |
| dependency | [Exact all-depth complete kernel](Yin_C_G0664_v1.md#statement) | Every N finite equality, safe rows/periods/exponent and exact original quotient; applied at N=8m. |
| dependency | [Complete global representative mechanism](Yin_C_G0667_v1.md#argument) | FC1--FC4 row multiplicities, both forward divisibilities, support floor, invisible fresh triple factor and all-primary canonical proof, with the new N costs paid here. |
| dependency | [Finite normalized character](Yin_C_G0654_v1.md#statement) | Pi=Phi/2, integrality and lift-independent modulus2^floor(log_2 N) on the actual quotient. |
| dependency | [Exact zero-correction formal calibration](Yin_C_G0668_v2.md#argument) | SY2 and SY9 full Ltilde/high pair and calibrated Phi formula, applied to explicitly supplied formal data without an original T; no old family target success is transferred. |
| dependency | [Sharp simultaneous high approximation](Yin_C_G0643_v2.md#argument) | SC13--SC14 exact order2Q-1 and all four fifth-root substitutions, with actual trace-local order preservation; the next endpoint is not asserted. |
| dependency | [Original integer trace-factor interface](Yin_C_G0667_v1.md#statement) | C8 and its retained C199 source depth, full monic integer factors, original layer indices, reduction, degree and zero Haar mean under whole H. |
| support | [Actual modulo8 construction](Yin_C_G0686_v1.md#decision-whole-reviewed-2026-10-24) | Applies through the proved strong-forward and old-support data at q>=256, with its original degree margin; supplies no modulo16 or characteristic-zero conclusion. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0911_v1.md#whole-doubled-precision-zero-correction-family-finding) | Entire DG1--DG11 and all six sections, every s>=82 and q, negative whole factor and strict costs, full extended character/representative/precision chain, all primary components and actual integer layers. |

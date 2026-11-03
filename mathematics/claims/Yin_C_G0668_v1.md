---
author: Yin
---
# Full synthetic canonical families at every sufficiently large dyadic multiplicity

Human author Yin.
Root supplied and checked the present synthesis, explicit formal determinant/character calculation, full parameter construction and polynomial degree bounds.
The complete-H construction of root and original_law and the global representative theorem of root and same_trace are reused only through their actual adopted fixed Claims.
These are author contributions, not independent review of this new result.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes the continuation.
The [D5 synthesis](../drafts/Yin_D_G0005.md#large-dyadic-full-canonical-synthesis) is development provenance, not a logical premise.
No native computation, parameter scan, new source acquisition or original-source proof audit is used.
The exact formal norm calculation is redone below; C655's theorem about an actual original input is not applied to a synthetic object without proving its needed algebra.
This complete new theorem is initially open for fresh isolated whole review.

## Statement

Work over F_2 with phi=X^2+X+1, chi=Xphi^2 and C_3=X^3+X.
Let B_n and W_n be the complete nonidentity and primitive odd-order trace polynomials, and ell the adopted character on1+tF_2[[t]], normalized by ell(1+t)=1.
Let

    S_primes={3,7,11,19,23,31,43,47,59,67,71,79,83},
    n_0=product_(p in S_primes)p,
    A=(1/4)product_(p in S_primes)(p+1),
    D=(1/2)product_(p in S_primes)(p-1).

For EVERY pair of integers j>=70 and k>=0 set

    m=2^j, q=2^k, Q=4m,
    k_m=floor(m/(2A)), b_m=m/2-k_mA,
    H(t)=W_(n_0)(t)^(k_m) W_3(t)^(b_m),
    B=X^(3m)H(chi), S=X^(4m)(X+1)^(8m)phi^(4m).

Then H is a monic finite complete product with H(0)=1, ell(H)=m/2 and degH<m/5.
The entire B is monic, prime to phi and has degree3m+5degH<4m.
Use the original integer layer data

    a_(k+j+4)=a_(k+j+3)=1, all other a_b=0,
    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2.

Their total weight is12mq, their largest weight is8mq, and S is exactly the normalized strict-window correction; the integer a_b and their indices are not divided by q.

Let x(t) be the inverse of chi at0 and set

    h_Q(X)=1+sum_(i=0)^(log_2Q-1)X^(Q-2^i),
    L_0(t)=[(1+t+t^2)^(7m)H(t)h_Q(x(t))]^(-1)
                              modulo t^(2m), degL_0<2m.

Choose beta=X^(2^a) modulo phi^(8m), with2^a>=8m and2^a=Q modulo3.
The full CRT class c in R_(4m)=F_2[X]/(X^(4m)phi^(8m)) is

    c=L_0(X^2) modulo X^(4m),
    c=X^(-2m)B^(-7)+beta X^(-2m)B^(-13)S
                                         modulo phi^(8m).

Every inverse has its specified low or high unit domain.
The exact finite character of this class vanishes:

    Pi_(4m)(c)=0 in Z/(4m).                              (SY5)

Consequently there exists a monic complete Y prime to Xphi representing c with all occurring irreducible multiplicities at least2, with Y dividing both Y(chi) and Y(C_3), and with Y and YB globally nonsquare.
For

    H_0=X^(2m)Y, U_0=H_0phi^(14m),
    R_0=H_0phi^(12m)B, V_0=H_0B,
    C_00=X^(2m)Y(chi)phi(chi)^(14m), D_0=V_0+C_00^3,

the SAME Y gives every exact identity

    R_0=rem_(U_0)(U_0(chi)^3), U_0 divides U_0(C_3),
    X^(4m)|Y', D_0 in phi^(4m),
    H_0^6=C_00^21 modulo phi^(8m),
    Z_0^11=H_0C_00^2 modulo phi^(6m),
    Z_0D_0+H_0V_0S=0 modulo phi^(8m),
    Z_0=beta^2B^(-1)(1+beta B^(-6)S) modulo phi^(6m).      (SY6)

The eleventh root is the unique high unit root, with its correction retained.
Both U_0 and R_0 are globally nonsquare, witnessed by a common fresh irreducible of exact multiplicity3.
Thus U=U_0^q and R=R_0^q have actual maximal Frobenius power q separately, and R=rem_U(U(chi)^3), U divides U(C_3).
Their unique unsaturated factor is phi, with orders14mq and12mq.
The root/gate equations raise with all their ingredients to6mq/8mq and correction S^q.
The separately defined nonconstant squarefree odd parts of Y and V_0 have derivative divisibility X^(4m) and phi^(8m), and degrees at least4m+1 and16m+1 respectively.

Write the complete V_0 as X^v product_(ell odd,ell>1,ell!=5)W_ell^(nu_ell).
For the monic integer trace polynomial F_ell defined by
Phi_ell(z)=z^(varphi(ell)/2)F_ell(z+z^(-1)), with varphi Euler's totient, and F_4=X, set

    G_int=F_4^(qv) product_ell F_ell^(q nu_ell)
               F_(2^(k+j+4)*5)F_(2^(k+j+3)*5).           (SY7)

This actual monic INTEGER polynomial reduces to R and satisfies

    integral_(circle) log(G_int(z+z^(-1))^2)dnu_1=0,

with probability Haar and the integrable-logarithm convention at zeros.
This is a synthetic integer polynomial, not the canonical residual of a constructed T.

The complete actual polynomial costs are

    degY<=460800m^3+19296m^2+480m,
    r_deg=degU=q(30m+degY),
    w_deg=degR=degG_int=q(29m+degY+5degH),
    r_deg-w_deg=q(m-5degH)>0,
    r_deg<=q(460800m^3+19296m^2+510m).                   (SY8)

For m>=2^71 the gap additionally exceeds5qm/256.
Every support-floor and invisible-factor expense is included.
A reciprocal original realization would have degree2r_deg, not the dimension20m of the finite target.

The theorem realizes all these specified characteristic-two canonical and integer-Haar conditions simultaneously at every stated m,q.
It does NOT supply one monic integer T with T mod2=U whose actual theta_p=rem_T(T(C_p))/p satisfy both original residual equations and produce G_int=G_can.
SAME-T modulo4/modulo8, characteristic-zero residuals, irreducibility, total reality and the original nonzero field values remain unresolved.
No original A_0=2m is realized or excluded, and no unrestricted Lehmer conclusion follows.

## Argument

### SY1. Exact input for every large dyadic parameter

Fix m=2^j with j>=70 and any q=2^k with k>=0.
Use the fixed thirteen-prime n_0 and positive integers A,D of C665, and define

    k_m=floor(m/(2A)), b_m=m/2-k_m A,
    H=W_(n_0)^(k_m) W_3^(b_m), Q=4m,
    B=X^(3m)H(chi), phi=X^2+X+1, chi=Xphi^2.

C665 proves H(0)=1, ell(H)=m/2 exactly, degH<m/5 and degB=3m+5degH<4m.
The complete factorization of H and B is retained, including W_3 and W_15.
Choose the actual INTEGER layer data

    a_(k+j+4)=a_(k+j+3)=1, all other a_b=0,
    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2.

Their weights are8mq and4mq, so their sum is12mq and no layer exceeds8mq.
Only the former lies in the strict interval(4mq,12mq), giving the specified normalized correction

    S=X^(4m)(X+1)^(8m)phi^(4m).

This is a square class modulo phi^(8m), and all integer indices and multiplicities remain unchanged.

### SY2. Direct formal norm evaluation of this exact CRT target

Let c be the full C649/C667 class in R_(4m), using this H,B,Q and S and both prescribed primary jets.
Define the full formal unit

    Ltilde(t)=[(1+t+t^2)^(7m)H(t)h_Q(x(t))]^(-1),

where x is the inverse of chi at0 and h_Q=1+sum_(i=0)^(log_2Q-1)X^(Q-2^i).
Let tau be the high cube-one unit with residue X^2 modulo phi, and put t=chi(X) on the high branch.
An explicit completed pair lifting c is

    u(X)=Ltilde(X)^2,
    v(X)=X^(5m-7Q)H(t)^(-7)(1+t^(2m)a),
    a=tau^(2Q)X^(-6Q)H(t)^(-6).

Indeed X^(6m)S=chi^(2m) modulo phi^(12m), since
X^(6m)S=chi^(2m)[X(X+1)]^(8m)=chi^(2m)(1+phi^(8m)).
Thus the high correction agrees with the full specified target modulo phi^(8m), and the low component agrees modulo X^(4m).
Every inverse is in its stated unit domain.
No unknown coefficient of an original T is assigned by choosing this lift.

Here is the complete determinant contribution, at exactly the needed precision.
The adopted high trace algebra gives Tr_high(a) in t^(2Q)=t^(8m), by the Frobenius power of Tr_high(tau X^(-3)) in t.
Modulo t the rank-four high algebra has two F_4 residue blocks, and a has the nontrivial cube-root residue X^Q.
Each block has characteristic polynomial Z^2+Z+1, so the complete characteristic polynomial is Z^4+Z^2+1 and e_2(a)=1 modulo t.
Consequently

    N_high(1+t^(2m)a)
       =1+t^(2m)e_1(a)+t^(4m)e_2(a)
                      +t^(6m)e_3(a)+t^(8m)e_4(a)
       =1+t^(4m) modulo t^(4m+1).

The linear term has order at least10m, the cubic term at least6m and the quartic term at least8m, all strictly beyond4m.
Since4m is dyadic, ell(1+t^(4m))=4m exactly.
The adopted finite conductor rule makes its correction4m modulo8m; no higher unknown norm coefficient can affect that residue.

For clarity the entire base character is also evaluated, rather than importing an original-input vanishing assertion.
The formal calibration gives

    N_high(X)=phi(x(t))^2,
    ell(phi)=-1, ell(h_Q)=Q/2,
    ell(f(x))=ell(f)/5,
    ell(Ltilde)=7m-ell(H)-Q/10.

For Phi(u,v)=ell(N_high(v))-(4/5)ell(u), the contribution before the correction is therefore

    2(1/5-1)(7m-ell(H)-Q/10)
        -(10m-14Q)/5-28ell(H)
       =(-330m+74Q-660ell(H))/25.

Using Q=4m and ell(H)=m/2 and adding the determinant correction yields

    Phi(c) congruent (-330m+296m-330m)/25+4m
          =-264m/25=8m*(-33/25)=0 modulo8m.

The denominator25 is an odd2-adic unit.
C654's integral lift-independent character then gives Pi_(4m)(c)=0 modulo4m.
This calculation uses only the explicit formal pair, not existence of an actual original residual input or the conclusion being constructed.
It is the decisive additional bridge beyond C665's isolated necessary congruence.

### SY3. Complete characteristic-two canonical data and synthetic integer layers

Apply the actually adopted C667 theorem to the now proved zero-character class.
It gives a monic complete Y prime to Xphi with every extra irreducible multiplicity at least2, Y dividing both Y(chi) and Y(C_3), and Y and YB globally nonsquare.
For

    H_0=X^(2m)Y, U_0=H_0phi^(14m),
    R_0=H_0phi^(12m)B, V_0=H_0B,
    C_00=X^(2m)Y(chi)phi(chi)^(14m), D_0=V_0+C_00^3,

it proves the exact all-primary identity

    R_0=rem_(U_0)(U_0(chi)^3), U_0 divides U_0(C_3),

and all full root/gate relations

    X^(4m)|Y', D_0 in phi^(4m),
    H_0^6=C_00^21 modulo phi^(8m),
    Z_0^11=H_0C_00^2 modulo phi^(6m),
    Z_0D_0+H_0V_0S=0 modulo phi^(8m),
    Z_0=beta^2 B^(-1)(1+beta B^(-6)S) modulo phi^(6m).

The selected beta is the actual cube-one high unit with residue X^Q; its admissible Frobenius representative is as in C649.
The correction is retained and the unit root is unique.
Both U_0 and R_0 are nonsquare, with a fixed fresh irreducible of exact multiplicity3.
Hence U=U_0^q and R=R_0^q have ACTUAL maximal Frobenius power q, retain the exact canonical remainder and C_3 divisibility, and their unique unsaturated factor is phi with multiplicities14mq and12mq.
The formal root/gate equations raise to their full6mq/8mq precisions with S^q; no integer layer exponent is divided.
The two nonconstant squarefree odd parts of Y and V_0 separately have derivative divisibility X^(4m) and phi^(8m), and degree at least4m+1 and16m+1, respectively.

Because this H is a proved whole-factor product, C667's conditional integer construction now applies.
If V_0=X^v product_(ell odd,ell>1,ell!=5)W_ell^(nu_ell), define

    G_int=F_4^(qv) product_ell F_ell^(q nu_ell)
             F_(2^(k+j+4)*5) F_(2^(k+j+3)*5),

where F_4=X and the other F_ell are the monic integer cyclotomic-trace polynomials.
This actual integer polynomial has reduction R, the full degree w_deg below, and normalized circle Haar integral of log(G_int(z+z^(-1))^2) equal to0.
All its factors are explicit complete trace factors; the two indicated integer5-layers are exactly the chosen a_b.

### SY4. Complete degree costs and the remaining same-input obstruction

For N=4m, C667's least safe dyadic L is16m and e=24m.
Writing D_B=degB<4m, its fresh-order threshold satisfies

    K_bound=max(480m,4D_B^2)<=64m^2,
    n_fresh<=64m^2+320m+1.

The latter bounds use m>=2^70, hence m>=8.
The full source and invisible-factor construction gives

    degY<=75*(16m)^2*(24m+1)+3(n_fresh-1)/2
         <=460800m^3+19296m^2+480m.

The exact costs are

    r_deg=degU=q(30m+degY),
    w_deg=degR=degG_int=q(29m+degY+5degH),
    r_deg-w_deg=q(m-5degH)>0,
    r_deg<=q(460800m^3+19296m^2+510m).

For m>=2^71 the retained C665 margin delta_deg>1/128 and A<2^63<=m/256 additionally give r_deg-w_deg>5qm/256.
No degree of a target quotient or a finite norm image replaces these actual polynomial degrees.

This constructs full characteristic-two canonical data and a compatible synthetic integer zero-Haar polynomial for EVERY dyadic m>=2^70 and every q=2^k.
It does NOT construct one monic integer T whose actual theta_p=rem_T(T(C_p))/p produce G_int as G_can or satisfy both original residual equations.
In particular SAME-T modulo4 and modulo8, characteristic-zero residuals, irreducibility and total reality remain unsolved.
The construction therefore limits exclusion by this specified collection of formal conditions; it does not refute any original Lehmer or C655 exclusion and does not realize an original A_0=2m.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:53 |
| status | open |
| reason | Register the complete explicit all-large-dyadic synthetic canonical family. The formal determinant and calibrated character are evaluated directly on the prescribed pair, proving Pi_(4m)=0 without assuming an original input; adopted global generation then supplies every all-primary, normalization and integer-Haar property with the full cubic degree bound. This new synthesis is author-checked and requires fresh isolated whole review. SAME-T modulo4/modulo8 and characteristic-zero realization remain unsolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire synthetic family](#statement) | SY5--SY8, every dyadic m>=2^70 and every q, explicit complete H/B and integer layers, full target membership, all-primary canonical pair/root/gate, global normalization, integer Haar lift and full degree costs, with the SAME-T boundary. |
| argument | [Complete synthesis](#argument) | SY1--SY4: explicit chosen layer and legal completed pair, full determinant and calibrated finite character, genuine application of global representative theorem, all original integer layers and polynomial costs. |
| dependency | [Adopted complete H family](Yin_C_G0665_v1.md#decision-whole-reviewed-2026-10-24) | Whole explicit thirteen-prime construction, exact ell(H)=m/2, strict degree and margin, complete substituted B; its isolated condition is not treated as target sufficiency. |
| dependency | [Adopted global canonical construction](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Exactly zero-character targets give strong complete representatives, multiplicity floor, both forward divisibilities, actual nonsquareness/maximal q, canonical remainder and corrected gate, conditional integer lift and paid costs. |
| dependency | [Formal homogeneous CRT](Yin_C_G0649_v1.md#statement) | Exact specified target and all-representative formal gate, not an original characteristic-zero existence theorem. |
| dependency | [Calibrated high norm and trace algebra](Yin_C_G0652_v1.md#argument) | ell(phi), ell(h_Q), inverse-composition scaling, full high norm of X and trace divisibility; applied to the explicitly chosen completed formal pair. |
| dependency | [Exact finite norm character](Yin_C_G0654_v1.md#statement) | Integrality, every-lift independence and the original finite quotient/modulus; no unproved higher coefficient is assigned. |
| support | [Earlier actual top-layer calculation](Yin_C_G0655_v1.md#argument) | Comparison with the earlier rank-four residue blocks and calibration; the necessary formal calculation is fully redone here, without importing the existence of an original input. |
| dependency | [Integer trace/Haar interface](Yin_C_G0199_v2.md#statement) | Complete integer trace factors and exact reductions/degrees, at the accepted C199 chain depth invoked in C667. |
| support | [Original same-coefficient lift boundary](Yin_C_G0202_v1.md#coupled-layer-statement) | Actual coupled residual errors still require one shared integer T; synthetic G_int is not an input satisfying those hypotheses. |
| support | [Actual first-error boundary](Yin_C_G0603_v1.md#statement) | No same-T coefficient error is made zero by the present formal construction. |

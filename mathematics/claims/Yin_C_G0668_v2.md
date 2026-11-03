---
author: Yin
---
# Full synthetic canonical families at multiplicity28 and large dyadic multiplicities

Human author Yin.
Root supplied and checked the full synthesis, explicit formal determinant/character calculations, both parameter constructions and polynomial degree bounds.
Original_law identified H=W_3W_21 during the bounded J131 author exploration; root supplied the independent hand proof and full canonical/degree construction for the separate m=14 branch.
Both are contributors to that extension, not its independent reviewers.
The entire physical v1 statement and SY1--SY4 proof remain at their original large-dyadic scope; this physical v2 adds SY9--SY12 and the separate final hand argument.
The complete-H construction of root and original_law and the global representative theorem of root and same_trace are reused only through their actual adopted fixed Claims.
These are author contributions, not independent review of this new result.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes the continuation.
The [D5 synthesis](../drafts/Yin_D_G0005.md#large-dyadic-full-canonical-synthesis) is development provenance, not a logical premise.
The m=14 candidate was noticed during [J131 exploration](../computations/programs/Yin_J_G0131/readme.md), which is discovery provenance only.
No native count, factorization output, certificate or classification conclusion is a premise of either proof here; the new finite example is proved directly below.
No new source acquisition or original-source proof audit is used.
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


### Additional finite branch at normalized multiplicity28

There is also a SEPARATE synthetic family at m=14, Q=32 and every q=2^k, k>=0.
Set

    H=W_3 W_21, B=X^18 H(chi), S=0,
    a_0=168q, a_b=0 for b>=1.                           (SY9)

Here H is a complete monic degree7 polynomial with ell(H)=-7, and B is a complete phi-unit of degree53<56.
The total original layer weight is168q=12mq, all occurring layers lie below8mq, and their strict-window correction is exactly zero.
Use the same formal definitions of L_0,x,h_Q and the CRT class, now with m=14,Q=32 and beta=X^128 modulo phi^112:

    c=L_0(X^2) modulo X^56,
    c=X^(-28)B^(-7) modulo phi^112,
    Pi_56(c)=0 in Z/(32).                              (SY10)

There exists a complete Y with every extra irreducible multiplicity at least2, both global forward divisibilities, and a fresh exact triple factor proving Y and YB nonsquare.
Use the same H_0,U_0,R_0,V_0,C_00,D_0 definitions with THIS m=14.
All canonical identities, unique unsaturated phi, actual maximal q, odd-part constraints and full root/gate assertions in SY6 hold with root precision84 and gate precision112, with S=0 and Z_0=beta^2B^(-1).
Their q-th powers retain their exact scaled precisions.
Since V_0=X^46 Y W_3 W_15 W_21 W_105 is complete, its integer lift is

    G_int=F_4^(46q) product_(ell odd,ell>1,ell!=5)F_ell^(q nu_ell)
                                      F_5^(168q),       (SY11)

where product W_ell^(nu_ell)=Y W_3 W_15 W_21 W_105 includes ALL coincidences and multiplicities.
It reduces to R_0^q, has zero normalized logarithmic Haar mean of its square, and has full degree

    r_deg=q(420+degY), w_deg=q(417+degY),
    r_deg-w_deg=3q,
    degY<=473105280, r_deg<=473105700q.                 (SY12)

These are synthetic canonical data at the remaining normalized multiplicity28.
They are not an original input, and no SAME-T modulo4/modulo8 or characteristic-zero residual solution is supplied.
The proof is the exact hand calculation in SY9 below; it uses no native candidate count, factorization output or exhaustive-classification conclusion.

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

### SY9. A hand-verified full synthetic branch at m=14

The complete polynomial W_3 has degree1 and character1.
For the squarefree order21=3*7, the independently adopted C665 divisor formula gives

    ell(W_21)=-(1/4)(chi_4(3)*3-1)(chi_4(7)*7-1)
              =-(1/4)(-4)(-8)=-8,
    deg W_21=varphi(21)/2=(2*6)/2=6.

Therefore H=W_3W_21 has constant1, degree7 and ell(H)=-7.
For m=14,Q=32, the required endpoint inequalities are28<32<70 and5degH=35<70-32=38.
Thus B=X^18H(chi) is monic, phi-unit and has degree18+35=53<4m=56.
The exact complete pullback identity gives H(chi)=W_3W_15W_21W_105; no irreducible factor or repeated order is omitted.
These are direct complete-group identities and character arithmetic, independent of the native process that first pointed to this example.

For every q=2^k, choose a_0=168q and all other a_b=0.
Its lambda_0=1 gives total weight168q, which equals12mq.
The lone occurring layer1 is below8mq and outside the strict window(4mq,12mq), so S_star=0 exactly.
No exponent is divided by q.
This supplies the integer factor F_5^(168q), not a prescribed parity without an integer lift.

Let Ltilde be the full low unit defined in SY2 with this m,Q,H.
The full target in R_56 has low component Ltilde(X)^2 modulo X^56 and high component X^(-28)B^(-7)=X^(-154)H(chi)^(-7) modulo phi^112.
There is no correction term because S=0.
Take the corresponding completed pair u=Ltilde(X)^2, v=X^(-154)H(t)^(-7).
The same exact formal norm calibration, valid on this explicitly defined pair without an original T, gives

    Phi(u,v)=(-330m+74Q-660ell(H))/25
             =(-4620+2368+4620)/25
             =2368/25=64*(37/25).

This is an exact completed-character equality, not merely a numerical approximation.
C654's finite character at N=56 is Phi/2 modulo32, so Pi_56(c)=0.
The use of the formal calculation does not assume that C655's original-input hypotheses have been realized.

Apply adopted C667 to this now-proved zero-character class.
It gives every global support, multiplicity, canonical remainder, corrected root/gate, maximal-q and conditional integer-Haar conclusion stated for this branch.
Here beta=X^128 is admissible because128>=112 and128=32 modulo3.
The root and gate precisions are6m=84 and8m=112; S=0 makes the exact root beta^2B^(-1), while the old relation and D_0 order are retained.
The unique unsaturated phi has orders196q and168q in U and R.
All outside factors and the original endpoint remain saturated.

The costs can be made entirely numerical without constructing an enormous coefficient list.
For N=56, C667's safe L is128 and e is384.
The full complement degree D_B is53, so

    K_bound=max(30*128,4*53^2)=max(3840,11236)=11236,
    k_0=floor(11236/1280)+1=9,
    n_fresh=1+1280*9=11521.

This n is odd,1 modulo5 and1 modulo3, so no further step is needed.
It exceeds every old primitive support order and4D_B^2.
The adopted fresh-factor proof therefore gives an irreducible of exact multiplicity3 in both Y and YB, while every occurring Y factor has multiplicity at least2.
The complete bound is

    degY<=75*128^2*(384+1)+3*(11521-1)/2
         =473088000+17280=473105280.

Because degB=53, the exact canonical degrees are420+degY and364+53+degY=417+degY before the q-th power.
This proves SY12, including the gap3q and upper bound473105700q for r_deg.
The integer trace product in SY11 includes the endpoint46q, every factor in the complete Y and H(chi), and all168q copies of F_5.
Its reduction, degree and zero Haar mean are precisely the already proved complete cyclotomic-product interface, with no degree drop or omitted scalar.

The entire m=14 branch is a synthetic solution of the listed formal and integer-Haar conditions.
It does not supply a shared integer T with the actual divided remainders, and hence does not settle original multiplicity28 or any part of the unrestricted Lehmer contract.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision bounded-28-extension-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:57 |
| status | open |
| reason | Retain the complete all-large-dyadic synthetic family and add a separate hand-proved m14, normalized multiplicity28 family. H=W3W21 has degree7 and exact character-7; its zero-correction target has Phi=64*37/25, so the actual finite character vanishes. The complete global canonical construction then supplies every formal and integer-Haar condition, all q, exact degree gap3q and numerical full representative bound. Native discovery is disclosed but not used as a proof premise. Fresh isolated whole review is required; SAME-T and original characteristic-zero realization remain unsolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire synthetic family](#statement) | Entire retained SY5--SY8 and new SY9--SY12, every dyadic m>=2^70 and every q plus the separate m14 branch, explicit complete H/B and integer layers, full target membership, all-primary canonical pair/root/gate, global normalization, integer Haar lift and full degree costs, with the SAME-T boundary. |
| argument | [Complete synthesis](#argument) | Entire retained SY1--SY4 and added SY9 hand proof: explicit chosen layer and legal completed pair, full determinant and calibrated finite character, genuine application of global representative theorem, all original integer layers and polynomial costs. |
| dependency | [Adopted complete H family](Yin_C_G0665_v1.md#decision-whole-reviewed-2026-10-24) | Whole explicit thirteen-prime construction, exact ell(H)=m/2, strict degree and margin, complete substituted B; its isolated condition is not treated as target sufficiency. |
| dependency | [Adopted global canonical construction](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Exactly zero-character targets give strong complete representatives, multiplicity floor, both forward divisibilities, actual nonsquareness/maximal q, canonical remainder and corrected gate, conditional integer lift and paid costs. |
| dependency | [Formal homogeneous CRT](Yin_C_G0649_v1.md#statement) | Exact specified target and all-representative formal gate, not an original characteristic-zero existence theorem. |
| dependency | [Calibrated high norm and trace algebra](Yin_C_G0652_v1.md#argument) | ell(phi), ell(h_Q), inverse-composition scaling, full high norm of X and trace divisibility; applied to the explicitly chosen completed formal pair. |
| dependency | [Exact finite norm character](Yin_C_G0654_v1.md#statement) | Integrality, every-lift independence and the original finite quotient/modulus; no unproved higher coefficient is assigned. |
| support | [Earlier actual top-layer calculation](Yin_C_G0655_v1.md#argument) | Comparison with the earlier rank-four residue blocks and calibration; the necessary formal calculation is fully redone here, without importing the existence of an original input. |
| dependency | [Integer trace/Haar interface](Yin_C_G0199_v2.md#statement) | Complete integer trace factors and exact reductions/degrees, at the accepted C199 chain depth invoked in C667. |
| support | [Original same-coefficient lift boundary](Yin_C_G0202_v1.md#coupled-layer-statement) | Actual coupled residual errors still require one shared integer T; synthetic G_int is not an input satisfying those hypotheses. |
| support | [Actual first-error boundary](Yin_C_G0603_v1.md#statement) | No same-T coefficient error is made zero by the present formal construction. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:12 |
| status | proved |
| reason | Adopt the entire physical v2 through fresh isolated whole R890 after reading the actual statement, preserved proof, new hand branch and complete review. Every dyadic m>=2^70 and the separate m14 branch have an exact zero-character target, simultaneous all-primary canonical data, actual maximal q, full corrected gate and a compatible integer zero-Haar polynomial with all costs paid. The integer polynomial is not proved to be G_can of one actual T. No original multiplicity is realized or excluded and the unrestricted Task remains active. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire synthetic family](#statement) | Entire retained SY5--SY8 and new SY9--SY12, every dyadic m>=2^70 and every q plus the separate m14 branch, explicit complete H/B and integer layers, full target membership, all-primary canonical pair/root/gate, global normalization, integer Haar lift and full degree costs, with the SAME-T boundary. |
| argument | [Complete synthesis](#argument) | Entire retained SY1--SY4 and added SY9 hand proof: explicit chosen layer and legal completed pair, full determinant and calibrated finite character, genuine application of global representative theorem, all original integer layers and polynomial costs. |
| dependency | [Adopted complete H family](Yin_C_G0665_v1.md#decision-whole-reviewed-2026-10-24) | Whole explicit thirteen-prime construction, exact ell(H)=m/2, strict degree and margin, complete substituted B; its isolated condition is not treated as target sufficiency. |
| dependency | [Adopted global canonical construction](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Exactly zero-character targets give strong complete representatives, multiplicity floor, both forward divisibilities, actual nonsquareness/maximal q, canonical remainder and corrected gate, conditional integer lift and paid costs. |
| dependency | [Formal homogeneous CRT](Yin_C_G0649_v1.md#statement) | Exact specified target and all-representative formal gate, not an original characteristic-zero existence theorem. |
| dependency | [Calibrated high norm and trace algebra](Yin_C_G0652_v1.md#argument) | ell(phi), ell(h_Q), inverse-composition scaling, full high norm of X and trace divisibility; applied to the explicitly chosen completed formal pair. |
| dependency | [Exact finite norm character](Yin_C_G0654_v1.md#statement) | Integrality, every-lift independence and the original finite quotient/modulus; no unproved higher coefficient is assigned. |
| support | [Earlier actual top-layer calculation](Yin_C_G0655_v1.md#argument) | Comparison with the earlier rank-four residue blocks and calibration; the necessary formal calculation is fully redone here, without importing the existence of an original input. |
| dependency | [Integer trace/Haar interface](Yin_C_G0199_v2.md#statement) | Complete integer trace factors and exact reductions/degrees, at the accepted C199 chain depth invoked in C667. |
| support | [Original same-coefficient lift boundary](Yin_C_G0202_v1.md#coupled-layer-statement) | Actual coupled residual errors still require one shared integer T; synthetic G_int is not an input satisfying those hypotheses. |
| support | [Actual first-error boundary](Yin_C_G0603_v1.md#statement) | No same-T coefficient error is made zero by the present formal construction. |
| review | [Fresh independent whole finding](../audits/reviews/Yin_R_G0890_v1.md#synthetic-canonical-v2-whole) | Entire SY1--SY12, both legal completed norms and finite conductors, both full synthetic families and all q/layers/degrees, with actual shared-T and characteristic-zero boundaries. |


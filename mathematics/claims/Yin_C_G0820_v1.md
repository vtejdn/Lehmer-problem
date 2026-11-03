---
author: Yin
---

# An exact modulo-eight cofactor character and additive kernel correction for the doubled endpoint family

Human author Yin.
Provenance: project deduction from the adopted actual canonical, doubled-profile and endpoint-family interfaces selected below.
Root proposed the single-F_960 ramified quotient, its possible unit-ratio target, the alternative genuine half-remainder correction and the initial period question.
Primitive_second_eight derived and checked the direct cardinality/annihilator proof, the necessary original monic cancellation, every normalization ambiguity, the exact character equivalence, the full additive correction and all sufficient periods below.
Root and primitive_second_eight are substantive contributors, not independent reviewers.
The candidate was fixed OPEN before cold whole review and separate adoption; the [current assessment](#current-assessment) owns its present status.
No native image, selected word, numerical residual array, computed kernel rank or assumed target attainment is a premise.

## Statement

### A. Exact actual inputs and original canonical conventions

For j>=1 use the integer trace polynomial C_j defined by C_j(z+z^(-1))=z^j+z^(-j).
For n>2 let F_n be the complete monic integer primitive trace factor given by z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z).
For odd n>1 put B_n=1+sum_(j=1..(n-1)/2)C_j.
Fix

    P=F_15=X^4-X^3-4X^2+4X+1,
    f=Pbar=X^4+X^3+1,
    V=F_960, J=P^4 V, deg V=128, deg J=144,
    H_0=(X-2)^2 F_3^2 F_5^3 F_9^4 B_187,
    T_0=JH_0^2, deg T_0=374.

Let M be the actual monoid of all finite products

    Q=(X-2)^k product_(n,u,v) B_n(C_(3^u5^v))^(e_(n,u,v)),
    k>=0, n>1 odd, gcd(n,15)=1, u,v>=0,
    e_(n,u,v)>=0 with finite support.

The empty product, all repetitions and all overlapping complete divisor orders are allowed.
Set H_Q=H_0^2Q and T_Q=JH_Q.
The actual degrees, with every factor and multiplicity retained, are

    deg Q=k+sum e_(n,u,v)3^u5^v(n-1)/2,
    deg T_Q=374+deg Q,
    full reciprocal degree=2deg T_Q.                    (ST1)

The integer endpoint remains X-2 and the high factor remains the single actual F_960, not F_480^2.
For every Q define the OWN original canonical polynomials

    a_Q=rem_(T_Q)(T_Q(C_2))/2,
    b_Q=rem_(T_Q)(T_Q(C_3))/3,
    c_Q=rem_(T_Q)(T_Q(C_5))/5,
    F_Q=rem_(T_Q)(2c_Q^2-3a_Q^5),
    G_Q=rem_(T_Q)(c_Q^3-2b_Q^5),
    X_(epsilon,Q)=rem_(T_Q)(b_Q^2-a_Q^3+epsilon G_Q),
    epsilon in{1,-1}.                                  (ST2)

Each prime division is a genuine integer coefficient division before reduction, and every remainder in ST2 uses the same original T_Q.
The subscript Q never denotes the own unweighted residuals of Q, J or V.
Put A=Z[X]/J, R_j=F_2[X]/f^j and

    Rcal_m=(Z/2^m)[X]/V for m=1,2,3,
    delta=(V-P^32)/2 in Z[X],
    deltabar=X^48(X+1)^64,
    P^32=-2delta in Rcal_m.

The half defining delta is formed over Z.
It is a unit in each Rcal_m.
The direct ring calculation in the proof gives

    Ann_(Rcal_m)(P^r)=(P^(32m-r)), 0<=r<=32m,
    Ann_(Rcal_3)(2P^4)=(P^60),
    B=Rcal_3/(P^60)
      =Rcal_2/(P^60)
      =(Z/4)[X]/(V,2P^28).                            (ST3)

In the middle expression Rcal_3 is first reduced modulo4; the proof establishes that4 already lies in(P^60), so these are canonical quotient identifications.
No chain-ring theorem is assumed without its explicit finite filtration argument.

### B. Definition and exact full first-eighth character

Let a_J,c_J be the canonical degree-below144 integer representatives of [a_Q]_J,[c_Q]_J.
They are divisible by P^4 over Z.
Define

    atilde_Q=a_J/P^4, C_Q=c_J/P^4

as genuine integer polynomials of degree below128 and then view them in Rcal_3.
There is a unit Ahat_Q in Rcal_3 with atilde_Q=P^4 Ahat_Q.
Its ambiguity is exactly(P^92), and its class in B is intrinsic.
Equivalently one can solve atilde_Q=P^4 Ahat_Q in Rcal_2, where the ambiguity is(P^60), and obtain that same class in B.
This distinction between the modulo8 normalization and its smaller required quotient is part of the statement.
The class C_Q is a unit in Rcal_3 and B.
Subscript0 below means the fixed actual base Q=1.

<a id="full-eighth-cofactor-character"></a>
**Definition (full first-eighth cofactor character).**
For the stated actual monoid M and ring B, define

    Omega(Q)=Q(C_5)^2 Q(C_2)^(-5) in B^times,
    kappa_8=-3delta Ahat_0^5 C_0^(-2) in B^times.     (ST4)

The full integer compositions are formed before restriction, and the negative exponents in B invert specified units only.
They are not inverse integer cofactors and do not change the positive cofactor domain.
Omega is a multiplicative monoid homomorphism.
Every Q in M satisfies the EXACT GLOBAL equivalence

    F_Q=0 modulo8 iff Omega(Q)=kappa_8 in B.          (ST5)

No F4 or X2 hypothesis is needed for ST5 itself.
The original global factor coverage and the actual monic P^4 cancellation are part of its proof.
In particular ST5 is stronger than checking the original residual only at the factor V without accounting for P^4.
The character does not test either X4 gate and does not by itself impose X2.
The finite ring B has cardinality2^240, its unit group has cardinality15*2^236, and its unit-group exponent divides960.
The image of Omega is not assumed to be this whole group, or to consist entirely of squares.

### C. Exact additive correction on the actual augmented kernel

Put p(Y)=Y^2+Y+1, lambda=X^3+X and chi=Xp(X)^2.
Using the [fixed source-map conventions](Yin_C_G0815_v1.md#source-jet-substitution-maps), define

    Xi_16(Q)=(Qbar mod f^16,
              Qbar(Y) mod(Y+1)^24,
              Qbar(Y) mod p(Y)^12).

All components are units.
Let N_16={K in M: Xi_16(K)=(1,1,1)}; this is the ACTUAL positive kernel, not an independently chosen local-coordinate space.
For K in N_16 form the full integer polynomial

    d_K=K(C_5)^2-K(C_2)^5,
    E_K=rem_V(d_K)/2 in Z[X], deg E_K<128,
    A_K=E_Kbar in R_32.                              (ST6)

The canonical V remainder is coefficientwise even, so the half in ST6 is genuine.
The map K -> A_K is additive:

    A_(KL)=A_K+A_L in R_32 for K,L in N_16.           (ST7)

Suppose Q in M passes the original F4 and X2 gates, and define the genuine integer quarter

    q_Q=[F_Q/4]_J in A

as in the [normalized-quarter convention](Yin_C_G0819_v1.md#normalized-first-quarter-derivative-class).
Every K in N_16 preserves both lower gates in both directions.
With gamma_Q=(C_Q)bar in R_32, if q_Qbar is divisible by f^8 in R_36 then

    q_(QK)bar-q_Qbar=f^8 gamma_Q^2 A_K in R_36,

    F_(QK)=0 modulo8
       iff A_K=gamma_Q^(-2)(q_Qbar/f^8) in R_28.    (ST8)

The quotient q_Qbar/f^8 is taken before projection to R_28.
All inversions in ST8 are of stated units at that exact precision.
This is a full first-eighth equivalence, unlike the earlier cancellation of only the lowest normalized quarter.
Its right side has112 binary coordinates, but no claim that an actual kernel word attains it is made.
The square gamma_Q^2 modulo f^28 is constant on each Xi_16 fiber.
In B one also has

    Omega(K)=1+2E_K for K in N_16,                  (ST9)

where R_28 maps injectively to the subgroup1+2B by a -> 1+2a using any integer lift.
Thus ST8 is consistent with the additive restriction of the character, and the attainable projected A_K form an F_2 subspace of R_28.
Its rank, actual generators and target membership are not determined here.

### D. Proven sufficient periods and exact limitations

For the actual rectangle factors W_(n,q)=B_n(C_q), n>1 odd prime to15 and q=3^u5^v, the following are proven sufficient periods of Omega ALONE:

    Omega(W_(n+480,q))=Omega(W_(n,q)),
    Omega(W_(n,q+480))=Omega(W_(n,q))                (ST10)

whenever the expressions are used as polynomial evaluations; representatives of the actual family must still be actual smooth q values with their actual degree q(n-1)/2.
The algebraic period identities hold for odd q; they do not authorize replacing an integer factor by an arbitrary residue-labelled non-smooth cofactor.
They are not asserted to be least periods.
For the JOINT data (Omega,Xi_16), n-period960 and q-period480 suffice.
No joint480 n-period, value of Omega((X-2)^240), complete joint alphabet, generator image or native enumeration is asserted.
The proof explicitly retains the possible nonunit denominator z^(5q)-1.

This theorem gives an exact finite group criterion and an exact additive kernel criterion, not a passing cofactor, a kernel-attainment result or a higher-modulus construction.
All actual positive words retain ST1's costs; no formal inverse or period reduction grants a cost-free integer realization.
It does not assert joint F8/X4 feasibility, an unrestricted cyclotomic-cofactor classification or completion of G0001.

## Complete argument

### FE1. Adopted actual coverage, normalized coefficients and source precision

The actual monoid and full input in ST1 are exactly the endpoint/rectangle family of [adopted C817 ES1](Yin_C_G0817_v1.md#decision-whole-reviewed-2026-10-26).
Its complete integer proof, using [C815 RC1--RC2](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26), retains every rectangle predecessor, endpoint exponent4+k and exceptional base exponent4,6,8 at orders3,5,9.
It proves

    H_Q|a_Q,c_Q,b_Q^2,b_Q^5,F_Q,G_Q,X_(+,Q),X_(-,Q)
                                                   over Z. (FE1)

Every residual divided by H_Q has degree below144, and H_Qbar is prime to f.
C817's explicit finite geometric-sum inverse modulo8 consequently makes each original global gate modulo2,4 or8 equivalent to the ACTUAL restriction at J.
This implication uses FE1 and that degree bound; it is not inheritance from an unweighted factor residual.

The same accepted proof supplies P^4|a_J,c_J over Z, with every original scalar division performed before restriction.
The fixed binary orders at f are8,6,4 for a_J,b_J,c_J.
For every allowed Q the true weights Q(C_2),Q(C_3),Q(C_5) are units at f, so these orders persist by [adopted C736](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25).
After the genuine P^4 divisions, atilde_Q has binary f-order4 in R_32 and C_Q is a binary unit there.
Different integer representatives of a_J or c_J differ by multiples of J; after P^4 division their differences are multiples of V, so their classes modulo V are intrinsic.

The actual single-factor carry from C817 ES2 is

    V=P^32+2delta,
    deltabar=X^48(X+1)^64.                            (FE2)

The latter is prime to f, so delta is a unit modulo(2,V).
An inverse lifts modulo4 and8 by a finite geometric sum in the coefficient-even error.
Neither a binary jet nor the different factor F_480^2 replaces this integer identity.

### FE2. Direct filtration and every annihilator used

Fix m in{1,2,3} and put R=Rcal_m.
Because V is monic of degree128, R is a free coefficient module of rank128 and

    |R|=2^(128m)=16^(32m).

FE2 gives2=-P^32 delta^(-1), and therefore P^(32m)=0.
Modulo P, delta is still a unit: its reduction modulo(2,P) is nonzero, and coefficient2 is nilpotent before this further quotient.
Thus imposing V=0 modulo P imposes2=0, giving

    R/(P)=F_2[X]/f=F_16.

An element outside(P) is a unit: lift its inverse from this residue field and sum the finite geometric series in the nilpotent ideal(P).
For every0<=j<32m, multiplication by P^j gives a surjection

    R/(P) -> (P^j)/(P^(j+1)).

Each quotient consequently has at most16 elements.
The product of their cardinalities is |R|=16^(32m), since P^(32m)=0.
Hence EVERY displayed quotient has exactly16 elements, and no earlier P power vanishes.
If x is nonzero, let j be the unique filtration level with x in(P^j) but not(P^(j+1)); then x=P^j u with u outside(P), hence with u a unit.
It follows directly that

    P^r x=0 iff r+j>=32m,
    Ann_R(P^r)=(P^(32m-r)).                          (FE3)

This proves the needed annihilators without assuming the conclusion from a chain-ring classification.
It also proves that every ideal is a P power if that terminology is desired, but no extra classification theorem is used.

In Rcal_3, the element2P^4 is a unit times P^36, so its annihilator is(P^60).
Also P^60=-2P^28 delta, and P^64=4delta^2.
The ideal(P^60) contains4 because it contains P^64 and delta is a unit.
Thus

    Rcal_3/(P^60)
       =Rcal_2/(P^60)
       =(Z/4)[X]/(V,2P^28)=B.                        (FE4)

The finite filtration of B has60 nonzero successive F_16 quotients.
It gives |B|=16^60=2^240 and |B^times|=15*16^59=15*2^236.
For any unit u, u^15=1+Pv in B.
In characteristic4, the only nonendpoint coefficient of(1+Pv)^64 that can survive is the middle coefficient2 at exponent32: for0<j<64, v_2(binomial(64,j))=6-v_2(j).
The same elementary binomial identity is explicitly justified in adopted C817 ES2.
Consequently

    (1+Pv)^64=1+2P^32v^32+P^64v^64=1 in B,

because2P^28=0 and P^60=0.
Hence the unit-group exponent divides15*64=960.
This is an upper bound, not a claim that Omega has this exponent or is a square-valued map.

### FE3. Correct monic cancellation and intrinsic Ahat normalization

Work first with the actual integer canonical representatives at J.
Since a_J=P^4 atilde_Q and c_J=P^4 C_Q, the actual residual has P^4 as an integer factor.
Write F_J=P^4 Ftilde_Q, where F_J=[F_Q]_J is represented in degree below144, so deg Ftilde_Q<128.
Taking the original residual and its J remainder gives the EXACT congruence

    Ftilde_Q=2P^4 C_Q^2-3P^16 atilde_Q^5 modulo V.  (FE5)

Indeed the difference before cancellation is a multiple of J=P^4V, and the common monic P^4 cancels over Z.
Monic multiplication by P^4 is injective in(Z/8)[X], even though its coefficient ring has zero divisors.
Together with the original global/J equivalence from FE1, this proves

    F_Q=0 modulo8
      iff 2P^4 C_Q^2-3P^16 atilde_Q^5=0 in Rcal_3.  (FE6)

This is the required P^4 cancellation BEFORE replacing the divisor J by V.
A restriction of F_Q to V alone would not justify FE6.

The binary f-order4 of atilde_Q allows an integer lift A of its binary quotient by f^4.
The canonical V remainder of atilde_Q-P^4 A is coefficientwise even.
Divide that remainder over Z by2 to obtain an integer B_0, so atilde_Q=P^4 A+2B_0 modulo V.
Using FE2 in Rcal_3 gives the explicit normalization

    Ahat_Q=A-P^28 delta^(-1)B_0,
    atilde_Q=P^4 Ahat_Q in Rcal_3.                  (FE7)

It is a unit because A has nonzero residue at f and the correction lies in(P).
By FE3 its ambiguity in Rcal_3 is exactly Ann(P^4)=(P^92).
Only its image in B is needed, where that ambiguity vanishes.
If instead one computes ANY solution in Rcal_2, FE3 gives ambiguity(P^60), again zero in B.
The projection of an Rcal_3 solution is one such Rcal_2 solution; thus both procedures give the same intrinsic B class.
No arbitrary precision extension of a modulo4 solution to a particular modulo8 solution is assumed.

Insert FE7 into FE6 and use P^36=-2P^4 delta in Rcal_3:

    2P^4 C_Q^2-3P^16 atilde_Q^5
       =2P^4 C_Q^2-3P^36 Ahat_Q^5
       =2P^4(C_Q^2+3delta Ahat_Q^5).                (FE8)

By FE3--FE4, FE8 vanishes exactly when

    C_Q^2+3delta Ahat_Q^5=0 in B.                   (FE9)

Every division and annihilator is now at its correct original or quotient domain.
In particular the passage from a modulus8 residual to a modulus4 target is paid by the actual factor2P^4 and its exact annihilator, not by dropping one bit informally.

### FE4. The full eighth gate is a multiplicative cofactor equation

Apply C736 to T_Q=T_0 Q, keeping the actual integer canonical values at T_0.
After restriction to J, then the genuine P^4 divisions and reduction modulo V, it gives

    atilde_Q=Q(C_2)atilde_0,
    C_Q=Q(C_5)C_0 in Rcal_3.                        (FE10)

The weights are units.
A valid normalization is Ahat_Q=Q(C_2)Ahat_0; any alternative differs by(P^92), hence has the same image in B.
Therefore FE9 is precisely

    C_0^2 Q(C_5)^2+3delta Ahat_0^5 Q(C_2)^5=0 in B.

Cancel only the unit C_0^2 Q(C_2)^5 to obtain ST4--ST5.
The target is fixed by the actual base T_0 and the single V; it is not chosen to fit an image.
For actual Q,L, the full integer identities(QL)(C_p)=Q(C_p)L(C_p) prove Omega(QL)=Omega(Q)Omega(L).
No composition on an arbitrary residue representative is used.
This proves the exact global F8 equivalence for every Q in M, without requiring lower gates in advance.

### FE5. Genuine half-remainders give an additive kernel map

Take K in N_16 and form d_K as an integer polynomial before reduction.
The fixed source identities p(lambda)=p(X)f and chi+1=(X+1)f imply

    K(C_2)bar=Kbar(X)^2=1 modulo f^32,
    K(C_3)bar=1 modulo f^12,
    K(C_5)bar=1 modulo f^24.                         (FE11)

Consequently d_Kbar=0 modulo f^32=Vbar.
Monic coefficient reduction commutes with reduction modulo2, so rem_V d_K is coefficientwise even.
There are genuine integer polynomials L_K,E_K with deg E_K<128 and

    d_K=V L_K+2E_K.                                 (FE12)

This proves ST6 without dividing in a ring with2-torsion.

For K,L in N_16 the exact integer identity is

    d_(KL)=K(C_5)^2 d_L+L(C_2)^5 d_K.

Reduce modulo V and divide the resulting equality by2 in the free integer quotient Z[X]/V.
Then reduce modulo2.
Both displayed weights are1 in R_32 by FE11, giving

    A_(KL)=A_K+A_L in R_32.                         (FE13)

This is actual additivity, with no independently prescribed local-cofactor realization assumption.

### FE6. Exact quarter transport and the complete remaining first-eighth target

Let Q pass the original F4/X2 gates.
C736 gives in A=Z[X]/J

    F_(QK)=K(C_2)^5 F_Q+2d_K c_Q^2.

Use c_Q=P^4 C_Q in A and the full integer FE12.
The term2V L_K P^8 C_Q^2 vanishes exactly, since J=P^4V divides it over Z.
Thus

    F_(QK)=K(C_2)^5 F_Q+4P^8 E_K C_Q^2 in A.       (FE14)

The unit K(C_2) modulo(J,4) and FE1 show that the original F4 gate is preserved in both directions.
The second lower gate is preserved as well: modulo2 its three weighted difference terms have f-orders at least24+12,32+24,24+12, respectively, all at least36.
This follows from FE11 and the original binary orders8,6,4; FE1 transfers the resulting J equality to the global X2 gate for both signs.
It is also the special Xi_16 case of adopted C819's lower-gate invariance.

Form the genuine GLOBAL integer quarters and only then restrict to J.
The free integer quotient A permits division of FE14 by4, yielding

    q_(QK)=K(C_2)^5 q_Q+P^8 E_K C_Q^2 in A.         (FE15)

Assume q_Qbar lies in(f^8) inside R_36.
The binary first weight differs from1 by a multiple of f^32, so its product with q_Qbar differs from q_Qbar by a multiple of f^40, which is zero in R_36.
Reducing FE15 therefore proves

    q_(QK)bar-q_Qbar=f^8 gamma_Q^2 A_K in R_36.     (FE16)

Only the projection A_K modulo f^28 is needed.
The square gamma_Q^2 is a unit there.
The map R_28 -> (f^8) in R_36 given by multiplication by f^8 is injective, so FE16 vanishes exactly at the target in ST8.
By FE1 and genuine coefficientwise division by4, q_(QK)bar=0 in R_36 is equivalent to the ORIGINAL F_(QK)=0 modulo8.
Thus ST8 is the full eighth-gate criterion, not merely a necessary low-coordinate test.
It makes no assertion about X4.

For two Q values with the same Xi_16, the actual C736 formula gives gamma_Q=gamma_0 Qbar(chi) in R_32.
Their Qbar(chi) agree modulo f^24, so their gamma squares agree modulo f^48 and in particular modulo f^28.
This proves the coefficient constancy claimed in the statement.

Finally in Rcal_2, FE12 and FE11 give

    Omega(K)=1+2E_K K(C_2)^(-5)=1+2E_K,

because K(C_2)^5 is1 modulo2 at V, and multiplication by2 kills the resulting coefficient-even error.
Passing to B proves ST9.
Since2 is a unit times P^32 and B has P-length60, Ann_B(2)=(P^28).
Equivalently2 times an integer lift vanishes in B exactly when its binary class vanishes modulo f^28.
Hence a -> 1+2a identifies the additive R_28 injectively with1+2B; products add because4=0.
The projected actual A_K image is an F_2 subspace, but no dimension or membership conclusion follows without examining the actual allowed words.

### FE7. Faithful Laurent proof of the sufficient Omega periods

Use the full ring Rcal_2 and its free rank-two extension

    L_4=Rcal_2[z]/(z^2-Xz+1)
       =(Z/4)[z,z^(-1)]/Phi_960(z).

The equality follows from X=z+z^(-1) and the exact identity z^128 V(z+z^(-1))=Phi_960(z).
The monic quadratic makes Rcal_2 -> L_4 injective.
After quotienting by2P^28 the extension remains free rank two over B, so B is still faithfully embedded in L_B=L_4/(2P^28).
The integer cyclotomic divisibilities give

    z^960=1, z^480=-1 in L_4.

For odd n and any invertible w, put S_n(w)=sum_(j=0..n-1)w^j.
The full centered identity is

    B_n(w+w^(-1))=w^(-(n-1)/2) S_n(w).              (FE17)

No denominator is used in FE17.

For p=2 and odd q, take w=z^(2q).
Then w^240=-1, and S_480(w)=(1+w^240)S_240(w)=0 exactly in L_4.
The n->n+480 centered shift consequently gives

    B_(n+480)(C_(2q))=-B_n(C_(2q)).                 (FE18)

For p=5 put w=z^(5q), so w^480=-1.
We need the precise two vanishing statements

    2S_480(w)=0, S_480(w)^2=0 in L_B.               (FE19)

Here is a proof covering the possible nonunit w-1.
Modulo2, L_4 becomes F_2[z]/Phi_15bar^32.
If3 does not divide q, the residue of w has order3, so w-1 is a unit and(w-1)S_480(w)=w^480-1=0 proves that S_480(w) is even in L_4.
Then both parts of FE19 follow from4=0.
If3 divides q, write5q=15d with d odd.
Modulo2 one has w^32=1 and

    S_480(w)=S_32(w)S_15(w^32)=(w-1)^31.

The polynomial w-1 is divisible by Phi_15bar, so S_480(w)bar lies in(P^31), using Phi_15bar=z^4 f(X).
Thus S_480(w)=P^31 A+2D for actual classes A,D in L_4.
Now2P^28=0 in L_B proves2S_480(w)=0, and

    S_480(w)^2=P^62 A^2=0 in L_B,

because P^60=0 there.
This proves FE19 without cancelling a nonunit in the second case.

Apply FE17 and S_(n+480)=S_n+w^n S_480.
The square of the centered shift contributes w^(-480)=-1, while both remaining error terms vanish by FE19.
Therefore

    B_(n+480)(C_(5q))^2=-B_n(C_(5q))^2 in B.       (FE20)

The numerator of Omega acquires the minus sign in FE20.
Its denominator acquires exactly the same minus sign from the fifth power of FE18.
All weights are units for the stated actual family, so their quotient is unchanged.
This proves the sufficient n-period480 of Omega alone.

For q->q+480, the identity z^480=-1 gives

    C_(2(q+480))=C_(2q),
    C_(5(q+480))=-C_(5q) in Rcal_2.

For ANY integer polynomial W, write W=W_even+W_odd.
Then W(-X)^2-W(X)^2=-4W_even W_odd, so these squares agree modulo4.
The numerator square of Omega is therefore unchanged, and the denominator is unchanged exactly.
This proves the sufficient q-period480, including all allowed smooth q values.
No least-period claim is needed.

### FE8. Joint-data boundary and actual costs

For Xi_16 the full binary period argument of [adopted C818 FI2--FI3](Yin_C_G0818_v1.md#decision-whole-reviewed-2026-10-26) works in the faithful Laurent quotient F_2[z]/Phi_15bar^24.
Its argument treats all k=q,3q,5q, and in the case15|k uses S_32(z^k)=0 without cancelling z^k-1.
That full precision projects to R_16 as well as R_14.
The injective source maps into R_24 and R_12 still recover the entire source coordinates(Y+1)^24 and p(Y)^12.
Thus n-period960 and q-period480 hold for Xi_16 with exactly the same proof.
Combining them with FE7 gives these sufficient periods for(Omega,Xi_16).

At n->n+480 the binary triple still has the nontrivial multiplier

    c=(1,1+(Y+1)^16,1).

Indeed z^240-1 is divisible by Phi_15bar^16, so its first projection is1 even in R_16, while the full source-of-order3 calculation remains nontrivial at depth24.
Omega alone has trivial480 transition by FE18--FE20.
It follows in particular that the separate Omega-only period is not a joint480 n-period.
No claim is made that the old endpoint power(X-2)^240 supplies this joint transition: its Omega value requires an additional calculation.
A safe joint960 n-period needs no such claim.

The ambient Xi_16 exponent divides480 by residue orders15,1,3 and nilpotent powers16,32,16 in its three coordinates.
Combined with FE2's bound960, the joint ambient exponent divides960.
This finite bound does not identify the image or certify any target.
If a finite family of actual generator images is later selected, a positive representative may reduce each nonnegative exponent modulo960, but its integer cost is still the sum of those actual generator degrees with their retained exponents.
No generator family, image, target decision or positive cofactor word is computed here.
In particular no arbitrary congruence representative may replace the actual smooth q in ST1's degree formula.
The full cofactor-attainment problem and both X4 gates remain outside the present conclusion.

## Source and evidence boundaries

The argument uses the selected adopted claims only at their explicit algebraic scopes.
C817 supplies the actual complete endpoint family, original integer factor coverage, P^4 factors, base unit/order interface, true single-F_960 carry and modulo8 global equivalence.
C736 supplies actual cofactor weights before restriction and the original first-residual defect.
C815 supplies complete rectangle factorization and exact source-map precisions; its local enumeration is not used.
C819 supplies the fixed normalized-quarter convention and the already adopted lower-kernel invariance, which FE6 also derives at the present precision.
C818 supplies only the faithful full binary period argument FI2--FI3; its native image, selected word and residual arrays are not inputs.
The new ramified quotient, its complete direct annihilator proof, the Omega target, additive correction and mixed-characteristic Omega periods are proved here.
No mutable Draft or native program/output is a premise, and no attainment or native-verification conclusion is inferred from the finite group formulations.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision full-eighth-character-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T22:48 |
| status | open |
| reason | Fix the exact actual-family global F8 cofactor character and full additive Xi16-kernel correction, with direct finite-filtration/annihilator proof, original monic P4 cancellation before changing to V, intrinsic modulo8 normalization and its required P60 quotient, all genuine integer halves/quarters, sufficient Omega-only480/480 and joint960/480 periods, complete nonunit-denominator and sign bookkeeping, and actual positive-cost boundaries. Root and primitive_second_eight are substantive contributors. No native image, selected word, target attainment, joint X4 result or mutable Draft is a premise. Fresh cold whole review and separate adoption remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full-eighth character and additive correction](#statement) | ST1--ST10: actual monoid/costs/canonical definitions, direct annihilators, intrinsic Ahat and B quotient, exact global F8 iff, additive actual-kernel map and112-bit full target, correct source precision, sufficient periods and all non-attainment/X4 limits. |
| argument | [Complete FE1--FE8 proof](#complete-argument) | Full global-to-J-to-V interfaces, direct cardinality filtration, scalar and monic divisions, actual cofactor homomorphism, genuine half-remainder additivity, full quarter transport, faithful mixed-characteristic Laurent periods and joint-data/cost boundary. |
| dependency | [Adopted actual endpoint family and modulo8 interface](Yin_C_G0817_v1.md#decision-whole-reviewed-2026-10-26) | ES1--ES2 complete integer H coverage, P4 original canonical factors, actual binary orders8/6/4, unit weights, true delta32 and explicit binary unit, global/J equivalence through modulo8. Its special endpoint480 conclusion is not extrapolated to arbitrary cofactors. |
| dependency | [Adopted exact canonical cofactor transfer](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Full integer prime divisions, same-divisor monic remainders and weighted F defect; applied only to actual products before J/V restrictions. |
| dependency | [Adopted rectangle and source-map precision](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | RC1--RC2 complete primitive factorization and paid degrees; LJ1 injective source substitutions at depths24/12. No10240 enumeration or64-target numerical data is used. |
| dependency | [Adopted quarter convention and actual-kernel lower gates](Yin_C_G0819_v1.md#decision-whole-reviewed-2026-10-26) | Genuine original F/4 before J reduction, normalized-quarter scope and lower-gate preservation; FE5--FE6 derive the stronger Xi16 correction without assuming its attainable image. |
| dependency | [Adopted full binary source periods](Yin_C_G0818_v1.md#decision-whole-reviewed-2026-10-26) | FI2--FI3 proof in faithful Phi15bar^24, all nonunit-denominator cases, source3 depth24 and source5 depth12, projected here also to first-coordinate depth16. No native image, selected word, endpoint240 Omega value or residual array is a premise. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T22:57 |
| status | proved |
| reason | Adopt the unchanged entire ST1--ST10 theorem and FE1--FE8 proof after whole independent R1040 and main-agent reading of the full fixed statement, argument and finding. Both original global directions, the exact ramified quotient and annihilators, intrinsic normalization, full F8 character, genuine additive kernel correction, sufficient periods and positive degree costs are covered. The112-bit target remains an actual attainment problem; no native image, passing cofactor, X4 conclusion or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full-eighth character and additive correction](#statement) | ST1--ST10: actual monoid/costs/canonical definitions, direct annihilators, intrinsic Ahat and B quotient, exact global F8 iff, additive actual-kernel map and112-bit full target, correct source precision, sufficient periods and all non-attainment/X4 limits. |
| argument | [Complete FE1--FE8 proof](#complete-argument) | Full global-to-J-to-V interfaces, direct cardinality filtration, scalar and monic divisions, actual cofactor homomorphism, genuine half-remainder additivity, full quarter transport, faithful mixed-characteristic Laurent periods and joint-data/cost boundary. |
| dependency | [Adopted actual endpoint family and modulo8 interface](Yin_C_G0817_v1.md#decision-whole-reviewed-2026-10-26) | ES1--ES2 complete integer H coverage, P4 original canonical factors, actual binary orders8/6/4, unit weights, true delta32 and explicit binary unit, global/J equivalence through modulo8. Its special endpoint480 conclusion is not extrapolated to arbitrary cofactors. |
| dependency | [Adopted exact canonical cofactor transfer](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Full integer prime divisions, same-divisor monic remainders and weighted F defect; applied only to actual products before J/V restrictions. |
| dependency | [Adopted rectangle and source-map precision](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | RC1--RC2 complete primitive factorization and paid degrees; LJ1 injective source substitutions at depths24/12. No10240 enumeration or64-target numerical data is used. |
| dependency | [Adopted quarter convention and actual-kernel lower gates](Yin_C_G0819_v1.md#decision-whole-reviewed-2026-10-26) | Genuine original F/4 before J reduction, normalized-quarter scope and lower-gate preservation; FE5--FE6 derive the stronger Xi16 correction without assuming its attainable image. |
| dependency | [Adopted full binary source periods](Yin_C_G0818_v1.md#decision-whole-reviewed-2026-10-26) | FI2--FI3 proof in faithful Phi15bar^24, all nonunit-denominator cases, source3 depth24 and source5 depth12, projected here also to first-coordinate depth16. No native image, selected word, endpoint240 Omega value or residual array is a premise. |
| review | [Whole independent R1040](../audits/reviews/Yin_R_G1040_v1.md#whole-finding) | Entire fixed ST1--ST10 and FE1--FE8, all five adopted interfaces, original monic/scalar divisions and both global directions, full annihilator/normalization proof, genuine half/quarter transport, all sufficient mixed-characteristic periods and exact non-attainment limits. |


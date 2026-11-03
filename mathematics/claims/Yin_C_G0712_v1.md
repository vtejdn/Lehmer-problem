---
author: Yin
---

# Same-degree simultaneous modulo-sixteen residuals with preserved derivative and next-error powers

Human author Yin.
Provenance: project deduction from the exact adopted finite-precision constructions named below.
Root proposed strengthening the original power parameter before C706's first repair and C708's paired low clearing.
Salem_completion read the complete fixed C706 and C708 proofs, C689's exact high-square map, C707's unchanged-root source mechanism and C710's actual error definition, and derived the compatible power, factor and degree budgets below.
These are substantive contributor roles, not independent review.
The adequate existing mechanisms are reused at those exact scopes; no native coefficient search, new source or new external theorem is used.
The full earlier-bit modulo32 question and its possible obstruction elimination remain a separate argument.
This complete author proof is registered open pending fresh isolated whole review.

## Statement

### PS1. Complete input and useful outputs

Take the complete old8a C708 source: a>=2 even, phi=X^2+X+1 over F_2, chi=Xphi^2, Psi=phi(chi), and monic Y_b prime to Xphi with Y_b dividing both Y_b(chi) and Y_b(X^3+X).
Put H_b0=X^aY_b, h_b=degH_b0 and C_b0=X^aY_b(chi)Psi^(7a), with

    H_b0^6=C_b0^21 modulo phi^(8a), h_b>=34a.

Choose the same fixed monic integer lift of every full irreducible factor of H_b0, with P_X=X, to form H_b.
For EVERY separately chosen dyadic q>=65536 set

    A=aq, H_0=H_b0^q, h=qh_b, d=h+14A,
    U=H_0phi^(7A), C_0=C_b0^q, Phi=X^2+X+1 over Z,
    S=(H_bPhi^(7a))^(q/2), J_2=H_b^(q/2),
    J_3=H_b^(3q/4), nu_j=q/2^(11+j), 0<=j<=4.       (PS1)

At the smallest allowed q these five powers are32,16,8,4,2.
Every full multiplicity remains; the parameter q is an originally chosen power, not assumed maximal without a proved source premise.
Fix one sign s in{1,-1}, and for every actual monic T use

    a_T=rem_T T(X^2-2)/2,
    b_T=rem_T T(X^3-3X)/3,
    c_T=rem_T T(X^5-5X^3+5X)/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)).

There exist ACTUAL integer polynomials T_2 and T_16 of the SAME degree d, both of the form S^2+2Phi^A K+4W with the SAME original C699 K, such that

    degK<d-2A, degW<d, J_3|K, J_2|W over Z,
    k=Kbar is a global q/128-th power,
    k^11=H_0C_0^2 modulo phi^(4A), X^(3A/2)|k,
    ord_phi Wbar>=A,
    T_2'=T_16'=0 coefficientwise modulo q/2048.    (PS2)

For T_2,

    F(T_2)=0 modulo16, X_s(T_2)=0 modulo8,
    e=(X_s(T_2)/8)bar in F_2[X^(nu_3)],
    e=0 modulo H_0 and modulo phi^(4A),
    f=(F(T_2)/16)bar in F_2[X^(nu_4)].              (PS3)

Both residuals are already zero modulo16 at every full H_0-primary.
In fact C710's unchanged original-factor argument also gives f=0 modulo H_0; no second residual modulo32 is inferred.
The first object T_2 is an actual C708 paired-step output before any final16 coefficient correction or trace pullback.
There is an ACTUAL J_2-divisible integer R, itself a nu_4-th power, of degree<h/2+3A such that

    T_16=T_2+16R,
    F(T_16)=X_s(T_16)=0 coefficientwise modulo16.   (PS4)

Its two actual coefficient-sixteenths belong globally to F_2[X^(nu_4)].
No trace pullback or degree multiplier is used in PS4.
For this chosen T_2, the unrestricted successful final16R family modulo32 has2^(d-3A) classes, and all successful lifts above T_2 modulo8 have C689's count2^(2d-47A/4).
These are the unrestricted C689 counts, not counts of the additional actual-power or integer-factor subclass constructed here.

There is also a degree<d binary error quotient b in F_2[X^(nu_3)] with

    e=alpha^2 b in F_2[X]/U, alpha=a_(T_2)bar.

Consequently C710's representative-independent original-degree obstruction

    O=f^2+phi^(4A)k^18 b^2/H_0^2
                  +phi^(6A)k^20 b/H_0^2 modulo phi^(9A) (PS5)

has a representative in F_2[X^(nu_3)].
Thus at q=65536 it is a fourth power at that full precision.
This conclusion does NOT assert O=0, a first32 repair, the next second-error ideal condition or simultaneous32.

For C691's complete original source, use Q=2^ell, ell>=82, m=Q/4-2, a=2m, its full Y and H_aux, and B=X^(Q-m)H_aux(chi).
Both T_2 and T_16 have

    degT=q(30m+degY)<=q(14400Q^3+1206Q^2+128Q),
    Tbar=U_0^q, G(T)bar=R_0^q,
    degT-deg(G(T)bar)
             =q(m-8-5degH_aux)>5qm/256,            (PS6)

where G(T)=rem_T(c_T^3-2b_T^5), U_0=X^(2m)Yphi^(14m), and R_0=X^(2m)Yphi^(12m)B.
The complete source's fresh triple factor proves actual common maximal q.
The reciprocal degree is2d; the separate synthetic integer layer is a_0=12mq and a_j=0 for j>=1, with its retained zero-Haar meaning.
It is not identified with actual G(T).
The sufficient minimum q is eight times C708's8192: this proves no degree doubling at the selected q, NOT an absolute minimum-degree improvement over C708's smaller-q doubled construction.
There is no coefficient-height, Mahler, root-location, irreducibility, characteristic-zero identity or unrestricted Task conclusion here.

## Complete argument

### PS2. Root-subring convention and actual initial derivative budget

For a power nu of2, Frobenius sends F_2[X]/phi^N injectively onto the nu-th-power classes in F_2[X]/phi^(nu N).
This follows from full phi-orders, since phi^(nu N) divides A^nu exactly when phi^N divides A.
The same statement holds for any polynomial modulus raised to nu.
A class expressed using nu-th-power polynomials, multiplication and inverses of unit nu-th-power classes therefore has a nu-th-power representative when its modulus is a nu-th power.
Its unique ordinary representative below the full modulus degree is also a nu-th power: divide the root representative by the root modulus first, then raise the resulting division to nu.
All lower CRTs below use this elementary fact and coprime moduli.
For an exact required integer factor, lift the quotient AFTER binary factorization and multiply by the displayed integer factor; a coefficient0/1 lift is not presumed to retain that factor.

Use the ACTUAL original C699 CP6 choices retained in C706 DP9:

    T_*=F_0^q+2F_1^q+4F_2^(q/2)+2F_3^(q/4)
                   +4F_4^(q/128)+2F_5^(q/128)
                   +8F_6^(q/2048).                (PS7)

Its F_i are the actual integer polynomials specified in C706, including the H_b^1024-divisible final root, with all original degree and J_2/J_3 costs.
Differentiating those seven weighted powers gives respective divisors

    q,2q,2q,q/2,q/32,q/64,q/256.

Thus T_*' is divisible by q/256=8nu_0.
C706's actual canonical derivative lemma applies at ell=log_2(q/256) and n=3, so BOTH actual coefficient-eighths are GLOBAL nu_0-th powers.
The same lemma states generally: if actual T' is divisible by2^ell and an actual residual by2^n, then its coefficient quotient reduced modulo2 belongs to F_2[X^(2^(ell-n))].
Its proof uses actual monic division and Delta(T)'=X T'(X^2-2)-TT', so no extra dyadic-half loss is introduced.
The initial k is a global p=q/128-th power, by the same C699 construction.

### PS3. The first earlier-bit repair with all powers and factors preserved

Use the exact C702/C706 targets

    rho^2=k/H_0 modulo phi^(3A),
    D_*=k^11/H_0^2+phi^(3A)k^10rho/H_0
                                     modulo phi^(7A/2),
    m=(E_F/phi^A)/D_* modulo phi^(7A/2),
    m=0 modulo j_2 X^(3A/2), j_2=J_2bar.            (PS8)

C702 gives the exact polynomial divisibility phi^A|E_F.
Because E_F is globally a nu_0-th power and nu_0 divides A, its quotient by phi^A is such a power.
C706's rho can be chosen a p/2-th power, and p/2=8nu_0.
Every other coefficient and modulus in the high target is a nu_0-th power, and D_* is a unit, so m's high class is a nu_0-th power.
Solve its root CRT with moduli

    phi^(7A/(2nu_0)), H_b0^(q/(2nu_0))X^(3A/(2nu_0)).

Lift the root with actual factor H_b^(q/(2nu_0))X^(3A/(2nu_0)), then raise it to nu_0, obtaining M=M_b^(nu_0).
This gives actual J_2X^(3A/2)|M and degM<h/2+17A/2.
For z=phi^A rho m modulo phi^(3A/2), z=0 modulo j_2, solve the root CRT at nu_0 with moduli phi^(3A/(2nu_0)) and H_b0^(q/(2nu_0)).
Lifting with the latter actual integer factor gives Z=Z_b^(nu_0), J_2|Z and degZ<h/2+3A.
Every displayed exponent is an integer since A=aq and the nu_j divide q/2.

The actual C702 correction

    T_a=T_*+4Phi^(4A)M+8Z

preserves both residuals modulo8 and makes its first eighth divisible by phi^(9A/2).
Its arbitrary integer lifts are legitimate by C702's proved lift invariance, including the actual halves and canonical carries.
The added first term is4 times an actual nu_0-th power and the second is8 times such a power.
Therefore T_a' is divisible by4nu_0, and its actual first eighth E_a is globally a nu_1-th power, since4nu_0/8=nu_1.

For the C689 first-high inverse put

    r_a=H_0E_a/(phi^(9A/2)k^10),
    t=phi^(A/2)/k,
    u_a=r_a+t r_a^2+t^3r_a^4 modulo phi^(5A/2).

All displayed exact divisors, units and moduli are nu_1-th powers, as is E_a.
The high class u_a is therefore a nu_1-th power.
Solve its root CRT with moduli phi^(5A/(2nu_1)) and H_b0^(q/(2nu_1)), high value the root of u_a and low value zero.
Lifting with the actual latter factor gives U_a=(U_ab)^(nu_1), J_2|U_a, and degU_a<h/2+5A.
The actual polynomial

    T_dagger=T_a+8Phi^(3A/2)U_a

has F16/X8, unchanged K and degree, exact J_2|W and J_3|K.
The last term is8 times an actual nu_1-th power, so T_dagger' is divisible by8nu_1=4nu_0=q/512.
Its actual second eighth E is globally a nu_1-th power.
The first-repair W change modulo2 is only phi^(4A)m, so the complete C707 old8a source still gives ord_phi w_dagger>=A.
Both non-phi residuals16 follow from the unchanged exact C694 factors.
All new full correction degrees are respectively<h/2+33A/2, h/2+3A and h/2+8A, each below d because h>=34A.

### PS4. An actual high-power paired low correction

C708 LF1 applies to this SAME T_dagger and gives E=w_dagger^6 modulo phi^A.
The right side has phi-order at least6A, so phi^A divides the entire actual coefficient polynomial E.
The target

    y=(E/phi^A) H_0^3/k^7 modulo phi^(3A)

is a nu_1-th-power class: E is globally such a power, nu_1 divides A, and k,H_0 have stronger global power exponents.
Take its square root z modulo phi^(3A/2), which is a nu_2-th-power class.
Set c=phi^(A/2)/H_0 and

    n=z+c z^2 modulo phi^(3A/2).

This is a nu_2-th-power class.
Indeed c is such a power, and the additive map N(v)=cv^2 has N^2(v)=c^3v^4=0 in this root quotient, since c^3 has order3A/2.
Hence n+cn^2=z and n^2+(phi^A/H_0^2)n^4=y at the full low precision.

Impose the full low polynomial condition n=0 modulo j_2X^(3A).
Its nu_2-root CRT has the coprime moduli

    phi^(3A/(2nu_2)), H_b0^(q/(2nu_2))X^(3A/nu_2).

Lift the root with actual factor H_b^(q/(2nu_2))X^(3A/nu_2), and raise to nu_2 to obtain N=N_b^(nu_2).
Then J_2X^(3A)|N over Z and degN<h/2+6A<h-A.
C708 LF3 applies literally to

    T_1=T_dagger+4Phi^(15A/2)N.

It preserves F8/X8 and the second eighth below phi^(4A), while its ACTUAL full first eighth on phi is phi^(9A/2)k^11 n/H_0^2, with zero H_0 component.
Its restoring first-high inverse has r=kn/H_0 and

    u=r+t r^2+t^3r^4 modulo phi^(5A/2),
    t=phi^(A/2)/k.

The explicit r,t and moduli are nu_2-th powers, so u is a nu_2-th-power class.
No power of an arbitrarily chosen error coordinate is assumed.
Solve the root CRT with moduli phi^(5A/(2nu_2)) and H_b0^(q/(2nu_2)); the actual factored lift gives U_btilde=U_b^(nu_2), J_2|U_btilde and degU_btilde<h/2+5A.
Set

    T_2=T_1+8Phi^(3A/2)U_btilde.

The exact C708 second-low change is

    phi^A k^7 n^2/H_0^3+phi^(2A)k^7 n^4/H_0^5=E
                                      modulo phi^(4A).

Thus T_2 has F16/X8 and its second eighth is zero below phi^(4A); every non-phi16 component remains zero under the actual J_2/J_3 factors.
The first paired term is4 times an actual nu_2-th power, while the second is8 times one, because nu_2 divides15A/2 and3A/2.
Together with the stronger derivative of T_dagger this proves T_2' divisible by4nu_2=q/2048>=32.
Its actual second eighth is globally a nu_3-th power and its first sixteenth globally a nu_4-th power by C706's coefficient lemma.
The full paired degrees are<h/2+21A and h/2+8A, both strictly below d; the first inequality uses h>14A, already paid by h>=34A.
The reduction of W changes from W_daggerbar only by phi^(15A/2)n, so its order remains at least A.
No factor, multiplicity or original degree has been dropped.

### PS5. The actual same-degree final square and exact count scope

At phi define

    g=e/(phi^(4A)k^4) modulo phi^(3A).

The divisor phi^(4A) divides the actual polynomial e, and its exponent and unit denominator are nu_3-th powers.
Therefore g is a nu_3-th-power class.
Its square root v modulo phi^(3A/2) is a nu_4-th-power class.
Impose v=0 modulo j_2 and solve its nu_4-root CRT using phi^(3A/(2nu_4)) and H_b0^(q/(2nu_4)).
After lifting the quotient with actual factor H_b^(q/(2nu_4)), set R=R_b^(nu_4).
Then J_2|R, degR<h/2+3A<d, and alpha^2 Rbar^2=e on BOTH components of B: this is the high equation at phi and the zero equation on H_0.
C689's ACTUAL SX19 map proves PS4 with F16 unchanged and X16 cleared.
The correction16R has derivative divisible by16nu_4=4nu_2, so T_16 retains that derivative divisibility.
Both actual sixteenths are consequently global nu_4-th powers.
Its W is changed by4R, retaining the exact J_2 factor and degree; K is unchanged.

The first error of T_2 at the modulo8 layer is already zero, so C689's first inverse is zero.
Its high quotient g is a power and hence a square, so the derivative-image condition is satisfied with zero derivative.
The non-phi and low tests were proved in PS4.
C689 SX19--SX20 therefore gives the complete final16R fiber2^(d-3A), and SX9 gives the entire count2^(2d-47A/4) above this chosen T_2 modulo8.
The additional integer-factor and nu_4-power representative supplies existence within this full fiber, not an equality of that restricted subset with the full fiber.

### PS6. Exact next-error power interface and original costs

For the PRE-final T_2, take b to be the unique degree<6A representative of g from PS5, without a zero condition on H_0.
That representative is a nu_3-th power by PS2 and has degree<d.
It satisfies e=alpha^2 b on phi, and the same equality is zero on H_0 because e and alpha are both zero there.
This is precisely C710's error quotient, distinct from the canonical odd divided remainder b_T.
In the obstruction O of equation(PS5), f^2 is globally a nu_3-th power because2nu_4=nu_3.
The two other terms have nu_3-th-power coefficients, b has that power, and the modulus phi^(9A) is also such a power.
Thus O has a nu_3-th-power representative at its complete declared precision.
The denominator H_0 is inverted only at phi, where it is a unit.
The original-factor improvement f=0 on H_0 follows from C710 NF2 with the retained actual J_3/K and J_2/W, not from differentiating a binary class.
No argument here forces the actual O to vanish.

C691 supplies exactly the initial old8a source, complete strong-forward factors and h_b>=34a already used by C708.
Every correction in this argument is even, preserves T modulo2, and preserves the canonical binary G because its odd divided remainders commute with reduction.
The unchanged original data are therefore U_0^q and R_0^q; the fresh triple factor retains their maximal q and all stated degree/gap costs.
No composition multiplies this degree or maximal exponent.
The separate original synthetic integer polynomial and its12mq layer remain at their earlier scope, without equality to actual G.
The larger sufficient original q is paid in every PS6 quantity before the construction.
These are actual same-degree finite residual solutions and a next-error power interface, with no omitted high-coefficient, analytic or characteristic-zero conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision power-preserving-sixteen-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T14:22 |
| status | open |
| reason | Register the full actual construction at every separately selected q>=65536: all root CRTs preserve the stated integer factors and higher powers through first repair and paired low clearing, giving pre-final derivative q/2048, global eighth/sixteenth powers and same-degree simultaneous16 via an actual factorized highest square. The complete C689 fiber counts retain their unrestricted scope. The C710 obstruction is a global nu3-power class, not proved zero. Every original source degree, maximality, gap and synthetic cost is paid at the larger sufficient q; fresh independent whole review and acceptance remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual power-preserving construction](#statement) | PS1--PS6, full old8a source, every original q>=65536 and fixed sign, exact K/W factors and degrees, derivative q/2048, all actual residual powers, pre-final quotient and obstruction power, same-degree16 existence, unrestricted counts and all original costs and exclusions. |
| argument | [Complete root-CRT and integer argument](#complete-argument) | PS2--PS6 and PS7--PS8: actual seven powers, coefficient derivative lemma use, every lower CRT and integer factor, higher-power first repair, exact paired inverse and low clearing, same-degree final square, error-quotient representative and full cost comparison. |
| dependency | [Adopted derivative-preserving first repair](Yin_C_G0706_v1.md#decision-whole-reviewed-2026-10-25) | DP9 actual weighted powers for every allowed q, full canonical derivative lemma, rho/D-star construction, exact factorized CRT and degree interfaces. The larger power choices and paired-stage preservation are proved here. |
| dependency | [Adopted paired low image and source compatibility](Yin_C_G0708_v1.md#decision-whole-reviewed-2026-10-25) | LF0a full input, LF1 low invariant, LF3 actual first-error formula and exact second-low map, original integer-lift/factor/degree conditions. Its degree-two final pullback is not used to obtain the new same-degree16 conclusion. |
| dependency | [Adopted actual earlier-bit repair](Yin_C_G0702_v1.md#decision-whole-reviewed-2026-10-25) | EB3--EB17 actual low first-error cancellation, exact phiA divisibility, admissible M/Z targets and integer-lift invariance with canonical carries, at the retained full factor input. |
| dependency | [Adopted original factor-compatible power construction](Yin_C_G0699_v1.md#decision-whole-reviewed-2026-10-25) | CP2--CP6 actual source and chosen integer F_i, full q/128 power of k, final H_b^1024 factor and all original degree/J2/J3 properties, without assuming higher residual success. |
| dependency | [Adopted unchanged-root low-W control](Yin_C_G0707_v1.md#decision-whole-reviewed-2026-10-25) | Original4A root under old8a support, actual sign halves and ord_phi Wbar>=A through all compatible first-repair choices; no stronger source or renormalized q is introduced. |
| dependency | [Adopted final high square and all-lift counts](Yin_C_G0689_v1.md#decision-whole-reviewed-2026-10-24) | SX4--SX9 and SX19--SX20 on the actual prepared T2: zero first inverse, exact high square image, non-phi and low tests, full16R count and complete count above the chosen modulo8 class. |
| dependency | [Adopted full original primary control](Yin_C_G0694_v1.md#decision-whole-reviewed-2026-10-24) | NP7 on every original multiplicity with actual J3 dividing K and J2 dividing W after each correction, supplying both non-phi16 components. |
| dependency | [Adopted original first-sixteenth obstruction](Yin_C_G0710_v1.md#decision-whole-reviewed-2026-10-25) | NF1--NF2 precise pre-final error quotient, representative-independent O at phi9A and original full-primary F32 result. Only its power class is derived here; no vanishing or simultaneous32 conclusion is imported. |
| dependency | [Adopted complete source and costs](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 complete original Q/m/Y/H_aux source, binary U0/R0 and fresh triple factor, all degree/gap bounds and separate synthetic12mq integer layer and zero-Haar scope. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T14:32 |
| status | proved |
| reason | Adopt the entire fixed PS1--PS6 statement and PS2--PS6 proof after complete main-agent reading and fresh isolated whole R933. Every higher-power integer lift, exact factor and original degree is preserved through the paired low correction and same-degree final16R; the pre-final e, f, quotient b and full obstruction O have their stated global powers. The derivative divisor q/2048, unrestricted fiber counts and complete original costs are supported at q>=65536. This larger sufficient q is paid explicitly; no absolute minimum-degree improvement, vanishing O, simultaneous32 or characteristic-zero realization follows from this Claim. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual power-preserving construction](#statement) | PS1--PS6, full old8a source, every original q>=65536 and fixed sign, exact K/W factors and degrees, derivative q/2048, all actual residual powers, pre-final quotient and obstruction power, same-degree16 existence, unrestricted counts and all original costs and exclusions. |
| argument | [Complete root-CRT and integer argument](#complete-argument) | PS2--PS6 and PS7--PS8: actual seven powers, coefficient derivative lemma use, every lower CRT and integer factor, higher-power first repair, exact paired inverse and low clearing, same-degree final square, error-quotient representative and full cost comparison. |
| dependency | [Adopted derivative-preserving first repair](Yin_C_G0706_v1.md#decision-whole-reviewed-2026-10-25) | DP9 actual weighted powers for every allowed q, full canonical derivative lemma, rho/D-star construction, exact factorized CRT and degree interfaces. The larger power choices and paired-stage preservation are proved here. |
| dependency | [Adopted paired low image and source compatibility](Yin_C_G0708_v1.md#decision-whole-reviewed-2026-10-25) | LF0a full input, LF1 low invariant, LF3 actual first-error formula and exact second-low map, original integer-lift/factor/degree conditions. Its degree-two final pullback is not used to obtain the new same-degree16 conclusion. |
| dependency | [Adopted actual earlier-bit repair](Yin_C_G0702_v1.md#decision-whole-reviewed-2026-10-25) | EB3--EB17 actual low first-error cancellation, exact phiA divisibility, admissible M/Z targets and integer-lift invariance with canonical carries, at the retained full factor input. |
| dependency | [Adopted original factor-compatible power construction](Yin_C_G0699_v1.md#decision-whole-reviewed-2026-10-25) | CP2--CP6 actual source and chosen integer F_i, full q/128 power of k, final H_b^1024 factor and all original degree/J2/J3 properties, without assuming higher residual success. |
| dependency | [Adopted unchanged-root low-W control](Yin_C_G0707_v1.md#decision-whole-reviewed-2026-10-25) | Original4A root under old8a support, actual sign halves and ord_phi Wbar>=A through all compatible first-repair choices; no stronger source or renormalized q is introduced. |
| dependency | [Adopted final high square and all-lift counts](Yin_C_G0689_v1.md#decision-whole-reviewed-2026-10-24) | SX4--SX9 and SX19--SX20 on the actual prepared T2: zero first inverse, exact high square image, non-phi and low tests, full16R count and complete count above the chosen modulo8 class. |
| dependency | [Adopted full original primary control](Yin_C_G0694_v1.md#decision-whole-reviewed-2026-10-24) | NP7 on every original multiplicity with actual J3 dividing K and J2 dividing W after each correction, supplying both non-phi16 components. |
| dependency | [Adopted original first-sixteenth obstruction](Yin_C_G0710_v1.md#decision-whole-reviewed-2026-10-25) | NF1--NF2 precise pre-final error quotient, representative-independent O at phi9A and original full-primary F32 result. Only its power class is derived here; no vanishing or simultaneous32 conclusion is imported. |
| dependency | [Adopted complete source and costs](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 complete original Q/m/Y/H_aux source, binary U0/R0 and fresh triple factor, all degree/gap bounds and separate synthetic12mq integer layer and zero-Haar scope. |
| review | [Independent whole power-preserving sixteen review](../audits/reviews/Yin_R_G0933_v1.md#whole-power-preserving-sixteen-finding) | Entire exact PS1--PS6 statement, PS2--PS6 argument and PS7--PS8 equations, every actual root CRT/factor/degree and derivative step, same-degree16 construction, complete unrestricted counts, next-error power interface and full original cost comparison, with accepted ancestor limits disclosed. |


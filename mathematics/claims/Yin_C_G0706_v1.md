---
author: Yin
---
# Derivative-preserving first repair and a single remaining modulo-sixteen test

Human author Yin.
The [current all-strategy continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
The [D1 derivative-preserving section](../drafts/Yin_D_G0001.md#derivative-preserving-earlier-bit-repair) is development provenance, not a logical premise.
This is a complete author argument awaiting fresh isolated whole review, not an adoption or a claim that the remaining test passes.

Root proposed extracting fourth-power eighth-errors from the actual high-power construction and preserving the integer derivative through the earlier-bit repair.
Same_trace checked the exact q threshold, weighted powers and canonical derivative lemma, all three factorized CRT lifts, every degree bound and the complete remaining iff below.
The adopted [C699 construction](Yin_C_G0699_v1.md#statement), its exact CP6 argument, [C686 coefficient and monic-division lemmas](Yin_C_G0686_v1.md#argument), and the [now adopted C702 earlier-bit theorem](Yin_C_G0702_v1.md#decision-whole-reviewed-2026-10-25) supply the reused interfaces.
A focused local search found no separate earlier fixed derivative32/fourth-eighth refinement; the actual C699 power structure is sufficient for this new derivation.
No native computation, q scan, second-low evaluation or independent-review claim is made here.

## Statement

### DP1: full normalized input, actual construction and single-test conclusion

Let a>=2 be even, phi=X^2+X+1 over F_2, chi=Xphi^2 and Psi=phi(chi).
Let Y_b be monic, prime to Xphi, and satisfy both Y_b|Y_b(chi) and Y_b|Y_b(X^3+X).
Set H_b0=X^aY_b, h_b=degH_b0, C_b0=X^aY_b(chi)Psi^(7a), and assume

    H_b0^6=C_b0^21 modulo phi^(4a), h_b>=34a.        (DP1)

Choose fixed monic integer lifts of every irreducible of H_b0, with P_X=X, and retain all its full multiplicities to define H_b=X^a mathcal_Y_b.
Let q be a power of2 with q>=8192 and put

    A=aq, H_0=H_b0^q, h=qh_b, d=h+14A,
    U=H_0phi^(7A), C_0=C_b0^q, Phi=X^2+X+1 over Z,
    S=(H_bPhi^(7a))^(q/2),
    J_2=H_b^(q/2), J_3=H_b^(3q/4), j_2=J_2bar.     (DP2)

For each separately fixed sign s in{1,-1}, choose the actual C699 CP2--CP6 construction

    T_*=S^2+2Phi^A K+4W_*,
    degK<d-2A, degW_*<d,
    J_3|K and J_2|W_* over Z.                       (DP3)

That construction has F(T_*)=X_s(T_*)=0 modulo8 and k=Kbar a GLOBAL p-th power, where p=q/128.
It also has k^11=H_0C_0^2 modulo phi^(4A), j_2|k and X^(3A/2)|k.
The actual canonical polynomials at every monic T below are

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3, c_T=rem_T(T(C_5))/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)).

The particular C699 choices in its CP6 can be made so that T_*' is coefficientwise divisible by32.
The ACTUAL integer coefficient eighths then satisfy

    E_F=(F(T_*)/8)bar, E_X=(X_s(T_*)/8)bar
                       belong to F_2[X^4].         (DP4)

There exist actual integer M_b,Z_b,U_b, constructed by the exact lower CRTs below, such that

    M=M_b^4, Z=Z_b^4, U_1=U_b^2,
    T_a=T_*+4Phi^(4A)M+8Z,
    T_dagger=T_a+8Phi^(3A/2)U_1
              =S^2+2Phi^AK+4W_dagger,              (DP5)

with SAME K and

    degW_dagger<d, J_2|W_dagger over Z,
    W_daggerbar=W_*bar modulo phi^(4A),
    T_dagger=T_* modulo4,
    T_dagger'=0 coefficientwise modulo16,
    F(T_dagger)=0 modulo16, X_s(T_dagger)=0 modulo8. (DP6)

Both residuals of T_dagger already vanish modulo16 on every H_0-primary, and its actual E_dagger=(X_s(T_dagger)/8)bar is a GLOBAL square polynomial.
The ENTIRE same-degree simultaneous modulo16 question above this CHOSEN T_dagger modulo8 is therefore equivalent to the single actual test

    ord_phi E_dagger>=4A.                           (DP7)

If it passes, a correction T_dagger+16R alone suffices; exactly2^(d-3A) reductions Rbar of degree<d work.
The full set of all monic lifts modulo32 above T_dagger modulo8 has C689's count2^(2d-47A/4).
If DP7 fails, neither such final16R nor any other lift above this fixed T_dagger modulo8 works.
These counts are for ALL coefficient lifts in their stated classes, not only the ones retaining the additional integer factors.
The theorem does not evaluate DP7 or assert that every earlier first-repair choice has the same low error.

The bound q>=8192 is sufficient, not asserted optimal.
It is a condition on the initially selected actual q, not a silent increase of a fixed smaller input or a claim that high q alone solves the residuals.
For the C667/C668/C691 input families, a=2m and the already paid representative gives h_b>181a.
For each selected q>=8192 the unchanged costs are

    A=2mq, d=q(30m+degY_0),
    original integer layer weight=12mq,
    canonical degree gap=q(5m-Q-5degH_aux),          (DP8)

with gap q(m-8-5degH_aux) for C691.
Actual maximal q is inherited only where the original normalized nonsquare input proves it.
No new support, enlarged degree for that q, characteristic-zero residual identity, original realization or Mahler estimate is supplied.


## Argument

### DP2: actual weighted powers, the precise threshold and canonical eighths

Use exactly the C699 CP6 choices, rather than an arbitrary modulo8 solution from its existential statement.
Its complete integer polynomial has the form

    T_*=F_0^q+2F_1^q+4F_2^(q/2)+2F_3^(q/4)
                       +4F_4^p+2F_5^p+8F_6^r,
    p=q/128, r=q/2048,                              (DP9)

where the F_i are actual integer polynomials.
More precisely, using the actual source choices of C699 CP2--CP6,

    F_0=H_bPhi^(7a), F_1=Phi^aK_b, F_2=R_b,
    F_3=Phi^(20a)L_b, F_4=Phi^(192a)R_v,
    F_5=Phi^(960a)M_b^(old), F_6=Z_b^(old).

The superscript old distinguishes those already constructed polynomials from the new correction roots in DP5.
In C699 the final root F_6 is an ACTUAL H_b^1024-divisible lift.
It is obtained from the true canonical quarter, not from freely specified error coordinates.
The needed precision is its adopted CP6 derivation: the six-term polynomial before the final8F_6^r belongs modulo16 to Z_16[X^(q/512)], its actual canonical quarter belongs to F_2[X^(q/1024)], and the final square-root class is a q/2048-th power.
These facts use C686 HP14--HP16, including the numerator precision before the dyadic half and actual monic division in the coefficient subring.
The lower final-root CRT has moduli phi^(3072a) and H_b0^1024, so the degree and actual J_2 factor of8F_6^r are those already paid in C699.

The derivatives of the seven displayed terms in DP9 are respectively divisible by

    q, 2q, 2q, q/2, q/32, q/64, q/256.

Thus T_*' is divisible by q/256, which is divisible by32 exactly in the stated sufficient range q>=8192.
The threshold is derived from the actual last power; no higher residual congruence is inferred merely from this derivative.

We use the following coefficient lemma at both32 and16.
For any monic integer T with T' divisible by2^ell, actual monic division B=QT+R preserves that derivative divisibility whenever B' has it.
Indeed R'=-Q'T modulo2^ell and degR'<degT; taking the monic remainder of this congruence forces R'=0 coefficientwise modulo2^ell.
For the dyadic quotient, use the integral polynomial Delta(T)=(T(C_2)-T^2)/2, whose exact derivative is

    Delta(T)'=X T'(C_2)-TT'.

Thus the actual a_T has the same derivative divisibility without losing a factor2.
For b_T,c_T, differentiating T(C_p) and applying the remainder lemma gives the result after division by the odd unit p.
Their integral divided remainders exist because C_p=X^p modulo p.
Both raw residual numerators then have derivatives divisible by2^ell, and one more actual monic division gives this property for F and X_s.

If such an actual residual is coefficientwise divisible by2^n with n<ell, write it as2^n R.
Then every coefficient of R' is divisible by2^(ell-n).
For an exponent i not divisible by2^(ell-n), the relation i R_i=0 modulo2^(ell-n) forces R_i even.
Consequently Rbar belongs to F_2[X^(2^(ell-n))].
Taking ell=5,n=3 proves the GLOBAL fourth-power assertion DP4.
Taking ell=4,n=3 will prove the later GLOBAL square assertions.

### DP3: fourth-power earlier-bit targets and actual factorized CRT lifts

C702 EB16 proves E_F is divisible by phi^A as a binary polynomial.
Since E_F is globally a fourth power and A is divisible by4, the exact quotient E_F/phi^A is also a fourth power.
Let rho be the root class

    rho^2=k/H_0 modulo phi^(3A),
    rho modulo phi^(3A/2),
    D_*=k^11/H_0^2+phi^(3A)k^10rho/H_0
                                      modulo phi^(7A/2). (DP10)

All denominators are units at phi.
Because k is a global p-th power and H_0 is a q-th power, rho can be chosen as a p/2-th-power polynomial representative.
Explicitly take the lower p-th root of k/H_0 in the quotient by phi^(3A/p) and then its p/2-th power.
The resulting square is the required class, and the square-root precision is exactly phi^(3A/2).
Since p/2>=32, rho is in particular a fourth power.
The exponents3A and7A/2 are divisible by4, so D_* is a fourth-power UNIT class at its specified precision.
Its definition is independent of the representative beyond the rho precision, as already checked in C702.

The C702 low-error repair prescribes

    m=(E_F/phi^A)/D_* modulo phi^(7A/2),
    m=0 modulo j_2 X^(3A/2).                        (DP11)

The first target and both moduli are fourth powers.
Solve their fourth-root CRT with moduli

    phi^(7A/8), H_b0^(q/8) X^(3A/8).

Its representative m_b has degree<h/8+17A/8 and is divisible by the second displayed modulus.
Lift the quotient after that binary factorization and multiply by the ACTUAL integer factor H_b^(q/8)X^(3A/8), obtaining M_b of the same degree.
Set M=M_b^4.
Then M reduces to m, is exactly divisible over Z by J_2 X^(3A/2), and has degree<h/2+17A/2.
No coefficient0/1 lift is assumed to preserve this integer factor.

Now prescribe

    z=phi^A rho m modulo phi^(3A/2),
    z=0 modulo j_2.                                (DP12)

This high target and both moduli are fourth powers.
The lower CRT moduli are phi^(3A/8) and H_b0^(q/8).
Choose its representative z_b, lift it with ACTUAL factor H_b^(q/8), and use Z=Z_b^4.
Then J_2 divides Z over Z and degZ<h/2+3A.
All CRTs are coprime because phi is prime to H_b0X, and their exponents are integers in the selected q range.

The actual polynomial T_a in DP5 preserves both residuals modulo8 and satisfies phi^(9A/2)|(F(T_a)/8)bar by the adopted C702 calculation.
Its arbitrary actual factor lifts are valid there: changing M by an even polynomial adds8Phi^(4A) times that polynomial, in the exact first-error kernel, while changing Z by an even polynomial adds16 times a polynomial.
C702 proves this lift invariance with the actual halves and canonical-divisor carries, rather than treating the residue classes as independent coordinates.

The first correction4Phi^(4A)M is4 times the ACTUAL fourth power (Phi^A M_b)^4, so its derivative is divisible by16.
The second correction8Z is8 times an actual fourth power, so its derivative is divisible by32.
Together with T_*' divisible by32, this proves T_a' divisible by16.
The actual coefficient lemma above therefore makes E_a=(F(T_a)/8)bar a GLOBAL square polynomial.
No fourth-power assertion about this new eighth is needed or presumed.

### DP4: square high inverse, restoration and all original degree bounds

In R=F_2[X]/phi^(5A/2), use the actual E_a just obtained and define

    r_a=H_0 E_a/(phi^(9A/2)k^10),
    t=phi^(A/2)/k,
    u=r_a+t r_a^2+t^3r_a^4.                        (DP13)

The division by phi^(9A/2) is exact by the preceding C702 repair.
That divisor, H_0, k^10 and the modulus are squares, while E_a is globally square.
Thus r_a is square in R.
The coefficient t is square because A/2 is even and k is a p-th power.
Therefore u is a square class in the exact modulus phi^(5A/2).

Impose u=0 modulo j_2 as a second CRT condition.
Solve the square-root CRT with moduli phi^(5A/4) and H_b0^(q/4), lift its representative with ACTUAL factor H_b^(q/4), and put U_1=U_b^2.
Then degU_1<h/2+5A and J_2 divides U_1 over Z.
The high congruence is precisely the C689 first-error inverse, so the actual T_dagger in DP5 has F=0 modulo16 and X_s=0 modulo8.
This inverse is used on the actual T_a, not on its unrepaired predecessor.
The correction is8 times the ACTUAL square (Phi^(3A/4)U_b)^2 and hence has derivative divisible by16.
This proves T_dagger'=0 modulo16.

For clarity, the complete change in W is

    W_dagger=W_*+Phi^(4A)M+2Z+2Phi^(3A/2)U_1.

Every summand is exactly J_2-divisible over Z.
Its reduction changes W_*bar only by phi^(4A)m, so the displayed low-W congruence also holds.
K is unchanged, so its original J_3 factor and full root/low conditions persist.
The three new terms in T have degrees bounded respectively by

    h/2+33A/2, h/2+3A, h/2+8A,

all strictly below d=h+14A because h>=34A.
The initial K and W_* retain C699's stated degrees.
Thus W_dagger has degree<d, T_dagger is monic of the SAME degree d and reduction U, and C694 NP7 applies to every full H_0-primary.
It makes both residuals modulo16 zero there.
The coefficient lemma at ell=4,n=3 makes E_dagger a global square from the actual X_s(T_dagger)=0 modulo8.
This proves all DP6 assertions and the stated support compatibility.

### DP5: the one remaining test and its exact limitations

Apply C689 to this actual T_dagger, whose K, support, root, low conditions and degree hypotheses are unchanged.
Its first error is zero, so the prescribed first inverse is zero.
Its non-phi second error is zero by NP7.
If DP7 holds, the exact quotient

    E_dagger/(phi^(4A)k^4) modulo phi^(3A)

is square, because E_dagger is a global square and both the divisor and unit denominator are squares.
Therefore the C689 high derivative-image condition is automatically satisfied with zero derivative.
The final16R square map, of rank3A, removes it without affecting F modulo16.
Conversely C689 SX7 proves the low condition DP7 necessary for EVERY lift above this chosen T_dagger modulo8, not merely for the final16R family.
The exact counts in DP1 now follow from C689 SX19--SX20 and SX9.
One may additionally choose the final R to be actually J_2-divisible, using the high root modulo phi^(3A/2) and the zero condition modulo j_2, with degree<h/2+3A; this gives a factor-preserving solution when DP7 passes but does not change the unrestricted counts quoted above.

The integer derivative argument is a statement about the complete canonical coefficients and does not replace the unevaluated DP7 by a local square assertion.
In particular it cannot force divisibility by phi^(4A).
The new threshold selects an actual allowed q before the construction; all degree/layer/gap quantities in DP8 are paid at that q.
No claim about q<8192 or about a characteristic-zero realization is inferred.
Evaluation or adjustment of the actual second low error remains a distinct mathematical obligation.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:55 |
| status | open |
| reason | Register the actual q>=8192 derivative-preserving refinement: the seven weighted integer powers yield derivative32 and global fourth-power eighths; bounded actual fourth-power and square factor CRT lifts perform the complete earlier-bit first16 repair while preserving derivative16, same K, degree and J2W. The constructed input has a global-square second eighth and all non-phi residuals16, so its full same-degree modulo16 question is equivalent to the one unevaluated second-low condition. No passing low error or original realization is claimed; fresh independent whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Derivative-preserving refinement](#statement) | DP1--DP8, all normalized and actual hypotheses, selected q>=8192, same-K/degree/factor construction, low-W congruence, global-square second eighth, precise single-test iff/counts and all original costs and remaining limits. |
| argument | [Complete power and canonical proof](#argument) | DP9--DP13 and DP2--DP5: actual seven powers and threshold, monic coefficient derivative lemma at32/16, fourth-power targets and exact root CRTs, actual factors/degrees, square high inverse and all-primary final criterion. |
| dependency | [Actual factor-compatible construction](Yin_C_G0699_v1.md#argument) | CP2--CP6 with the specified actual integer lifts, seven-term power representation after its final correction, global k power, legitimate canonical quarter/subring and final-root precision; CP1--CP4 supply the chosen actual inputs and costs. |
| dependency | [Coefficient and canonical subring lemmas](Yin_C_G0686_v1.md#argument) | HP14--HP16 and HP6, actual power-coefficient precision before division, monic subring division and the derivative mechanism, explicitly extended here to32 and fourth-power eighths. |
| dependency | [Complete earlier-bit first repair](Yin_C_G0702_v1.md#statement) | EB3--EB17 and full argument, exact earlier-bit map and integer-lift invariance, automatic phi^A membership, high inverse and actual J2 factor/degree constraints; new power compatibility is proved here. |
| dependency | [Full next-layer criterion and final square map](Yin_C_G0689_v1.md#statement) | SX4--SX9 and SX19--SX20, actual first inverse at the repaired base, necessity of the second low condition, automatic high-square specialization, both exact stated fiber counts. |
| dependency | [Actual non-phi factor theorem](Yin_C_G0694_v1.md#statement) | NP7 with all full multiplicities divisible by4 and the maintained ACTUAL J3/K and J2/W factors, giving both residuals16 on every non-phi primary. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T07:05 |
| status | proved |
| reason | Adopt the entire derivative-preserving first repair after main reading of complete C706 and fresh isolated whole R927. The actual seven weighted powers establish the q>=8192 threshold, the canonical derivative lemma supplies global fourth-power eighths, and all three factored root CRTs preserve the same K, original degree, J2W and derivative16 through actual F16/X8 repair. The second eighth is globally square with all non-phi components zero, so the whole same-degree lift question above this chosen modulo8 base is equivalent to its one unevaluated low phi4A test. Both counts, original costs and absence of a passing input or characteristic-zero conclusion remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Derivative-preserving refinement](#statement) | DP1--DP8, all normalized and actual hypotheses, selected q>=8192, same-K/degree/factor construction, low-W congruence, global-square second eighth, precise single-test iff/counts and all original costs and remaining limits. |
| argument | [Complete power and canonical proof](#argument) | DP9--DP13 and DP2--DP5: actual seven powers and threshold, monic coefficient derivative lemma at32/16, fourth-power targets and exact root CRTs, actual factors/degrees, square high inverse and all-primary final criterion. |
| dependency | [Actual factor-compatible construction](Yin_C_G0699_v1.md#argument) | CP2--CP6 with the specified actual integer lifts, seven-term power representation after its final correction, global k power, legitimate canonical quarter/subring and final-root precision; CP1--CP4 supply the chosen actual inputs and costs. |
| dependency | [Coefficient and canonical subring lemmas](Yin_C_G0686_v1.md#argument) | HP14--HP16 and HP6, actual power-coefficient precision before division, monic subring division and the derivative mechanism, explicitly extended here to32 and fourth-power eighths. |
| dependency | [Complete earlier-bit first repair](Yin_C_G0702_v1.md#statement) | EB3--EB17 and full argument, exact earlier-bit map and integer-lift invariance, automatic phi^A membership, high inverse and actual J2 factor/degree constraints; new power compatibility is proved here. |
| dependency | [Full next-layer criterion and final square map](Yin_C_G0689_v1.md#statement) | SX4--SX9 and SX19--SX20, actual first inverse at the repaired base, necessity of the second low condition, automatic high-square specialization, both exact stated fiber counts. |
| dependency | [Actual non-phi factor theorem](Yin_C_G0694_v1.md#statement) | NP7 with all full multiplicities divisible by4 and the maintained ACTUAL J3/K and J2/W factors, giving both residuals16 on every non-phi primary. |
| review | [Fresh independent whole derivative-preserving finding](../audits/reviews/Yin_R_G0927_v1.md#whole-derivative-preserving-repair-finding) | Entire fixed DP1--DP13 statement and proof, exact actual powers and canonical coefficient precision, all factorized CRTs and degrees, same-input primary/derivative conclusions, complete iff/counts and actual original costs. |


---
author: Yin
---

# Necessary multiplicity and valuation ties at fifteen-divisible cyclotomic primaries

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the true modulo4 quotient lemma and the subsequent necessary multiplicity and valuation conditions.
The characteristic_zero_bridge agent checked every quotient/representative step, local root/place evaluation, strict endpoint and parity branch, and derived the final actual b-evaluation.
Root read the entire saved FM1--FM15 argument, including the generic lemma and all source/remaining-scope boundaries.
Both agents are substantive contributors; fresh isolated whole review and separate adoption were still outstanding at author registration.
No native coefficient scan, disposable experiment, Hensel theorem, new source reading or assumed ramification index is a premise.
The complete proof is fixed below, without a D proof dependency.

## Statement

### A. General nilpotence lemma in the actual monic modulo4 quotient

Let f be a monic nonconstant polynomial in F_2[X], E>=1 an integer, and J a monic integer polynomial with Jbar=f^E.
Choose ANY monic integer lift fhat of f and write the ACTUAL integer identity

    J=fhat^E+2K, K in Z[X].

In S=(Z/4)[X]/(J), one has

    fhat^(2E)=0, 2fhat^E=0.

Let a_0,c_0 be arbitrary classes in S satisfying2c_0^2-3a_0^5=0.
If either abar_0=0 in S/2S or, for an integer t>=0, abar_0 is divisible by f^t and5t>=2E, then

    cbar_0^2=0 in F_2[X]/f^E.

The statement uses the genuine monic quotient, whose underlying Z/4 module is free.
It neither divides by2 in that quotient nor asserts any canonical-remainder inheritance by J.

### B. Complete original cyclotomic domain and three multiplicities

Let T be ANY monic integer polynomial of degree d such that

    P_T(z)=z^dT(z+z^(-1))

is a COMPLETE product of cyclotomic polynomials, retaining every factor and actual multiplicity.
Use C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X, with its OWN original canonical system

    a=rem_T T(C_2)/2, b=rem_T T(C_3)/3,
    c=rem_T T(C_5)/5,
    F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5),
    X_epsilon=rem_T(b^2-a^3+epsilon G),
    epsilon in{1,-1}.

All scalar divisions and monic remainders are actual integer operations at the SAME T before reduction.
Assume coefficientwise

    F=0 modulo4, X_epsilon=0 modulo2

for one, hence either, sign.
No irreducibility or nontorsion assumption is imposed.

For n>2 let F_n be the full integer primitive-order trace factor defined by

    z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z).

Indexed F_n is distinct from the canonical residual F.
For every integer j>=1, C_j is the monic integer trace polynomial satisfying C_j(z+z^(-1))=z^j+z^(-j).
By adopted C760 the binary factorization is

    U=Tbar=X^A product_(r>1 odd)f_r^(E_r),
    f_r=F_rbar, A>=0, E_r>=0,

with squarefree, possibly reducible, pairwise coprime f_r and all complete exponents retained.
Fix any odd h divisible by15 such that E=E_h>0 and the actual Gbar component modulo f_h^E is nonzero.
Set

    k=h/5>1, l=h/3>1,
    B=E_k, D=E_l.

Here D is an integer multiplicity, not a polynomial cofactor.
The three odd orders h,k,l are distinct.
The nonzero-G condition is exactly E>3B.
At every irreducible psi|f_h the actual gamma=cbar has order B, and beta=bbar has order D if D<E, or is zero at full precision when D>=E.

### C. Necessary arithmetic, unique factor and parity branches

For EVERY such component there are integers u>0 and w>=8, with w a power of2, such that

    E=w+u,
    ord_psi(abar)=t=2u for EVERY psi|f_h,
    E/5<=t<2E/5,
    V_w=F_(2wh)=F_(2h)(C_w)
          occurs EXACTLY ONCE in T.

Its dyadic weight w is the largest weight with odd actual factor multiplicity in C760's full Delta expansion.
No binary irreducible component is selected in place of the complete f_h.
The further NECESSARY equalities and inequalities are

    w=10u-2B, B=5u-w/2,
    28u/5<w<=9u,
    B>=u/2>0, B!=2u,
    2D=3 min(2u,B)<E.

They give precisely the following branches:

| Branch | Necessary interval and multiplicities | Parity conclusion |
| --- | --- | --- |
| B<2u | 6u<w<=9u; D=3B/2 | B and u are both even. |
| B>2u | 28u/5<w<6u; D=3u | No additional parity restriction is obtained here. |

There is no blanket even-u conclusion.
The endpoints u=0 and B=0 are excluded by the necessary original residual conditions.
No assertion is made that every arithmetic profile satisfying this table is realized.

### D. Actual cofactor model and all three canonical local values

Let R=T/V_w be the ACTUAL monic integer cofactor.
Its complete binary factorization can be written

    Rbar=f_h^u f_k^B f_l^D Z,
    gcd(Z,f_h f_k f_l)=1.

For any monic integer lift Z_tilde, the genuine same-binary model is

    M=F_h^u F_k^B F_l^D Z_tilde,
    R=M+2H, H in Z[X].

This is not a claim that the integer factors of R equal those chosen lifts.
For ANY primitive2wh root zeta, theta=zeta+zeta^(-1), and ANY normalized dyadic valuation v with v(2)=1, the ORIGINAL canonical values satisfy

    v(R(C_2(theta)))=v(a(theta))=2u/w<1/2,
    v(R(C_5(theta)))=v(c(theta))=B/w<5/12,
    v(R(C_3(theta)))=v(b(theta))=D/w<15/28.

All model values are below1 and the actual integral error2H has value at least1, so it cannot cancel them.
The complete factor V_w(C_3(theta)) is a UNIT in this domain, in contrast with C760's zero-beta case.
The first-residual terms must have EQUAL values:

    v(2c(theta)^2)=1+2B/w
                 =10u/w=v(3a(theta)^5)<2.

These equalities only force a valuation tie.
They do not prove the leading units cancel to the needed precision, or that F is coefficientwise divisible by4.
Likewise the second-residual order comparison does not prove its required unit equality.

The modulo4 lemma is applied to the actual full h-factor T_h of T, with T_hbar=f_h^E.
The polynomials mapped to (Z/4)[X]/(T_h) remain the ORIGINAL a_T and c_T.
They are not replaced by the own canonical remainders of T_h; only the original equation is reduced through an actual divisor.

The original reciprocal degree remains2d.
The removed single factor has trace degree w varphi(h)/2 and full reciprocal degree w varphi(h), with the remaining actual cofactor and all other multiplicities retained.
No field degree, relative norm or total measure is divided by these quantities.

By C760 every nonzero Gbar component of a fully cyclotomic input with these residual hypotheses already lies at15|h; the present theorem constrains each such remaining component.
It does not establish an integer realization, either leading-unit cancellation, a compatible nonzero-G example, or the exclusion of every fifteen-divisible profile.
No characteristic-zero identity, quantitative Mahler bound or unrestricted G0001 conclusion is asserted.

## Complete argument

<a id="fifteen-primary-first-four-necessary-multiplicities"></a>
### Necessary multiplicity and valuation ties at the remaining fifteen-divisible primaries

This is the complete fixed author argument by root and characteristic_zero_bridge.
Root proposed the modulo4 nilpotence argument and the resulting local valuation/multiplicity constraints.
Characteristic_zero_bridge checked the true factor quotient, every actual integer representative and evaluation, the strict endpoints and the separate parity branches, and derived the corresponding b-evaluation after the necessary constraints.
The direct mathematical inputs are [adopted C760 Parts A--B and OT1--OT11](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) and [C736's actual canonical/Delta identities](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25).
C760's exact Bel17/The26b inspection limits remain in force; no new source reading, Hensel theorem, ramification index or nontorsion lemma is imported.
No numerical scan, disposable trial or native coefficient computation is evidence for the statements below.
The initial assessment is OPEN pending fresh isolated whole review and separate adoption; the remaining fifteen-divisible domain is not settled.

#### Full original input and the three complete multiplicities

Let T be monic integral of degree d, with the COMPLETE reciprocal P_T=z^dT(z+z^(-1)) cyclotomic.
Retain all full trace factors and actual multiplicities.
Use the SAME original canonical a,b,c,F,G,X_epsilon as in C760, with actual integer prime divisions and monic remainders.
Assume coefficientwise

    F=0 modulo4, X_epsilon=0 modulo2,
    epsilon in{1,-1}.                          (FM1)

The binary second-residual condition is the same for both signs.
Write C760's complete binary factorization

    U=Tbar=X^A product_(r>1 odd)f_r^(E_r),
    f_r=F_rbar,

where each f_r is the full squarefree primitive odd-order trace polynomial and may split over F_2.
Fix an odd h divisible by15 with E=E_h>0 and a NONZERO Gbar component at that order.
Put

    k=h/5>1, l=h/3>1,
    B=E_k>=0, D=E_l>=0.                        (FM2)

The letter D in this section is an INTEGER multiplicity, never the polynomial cofactor used below.
All full f_h components have the same exponent E, as guaranteed by the complete cyclotomic trace factorization.

On each irreducible psi|f_h, the C_5 map has image of primitive odd order k.
Its binary derivative is (X^2+X+1)^2=f_5^2, nonzero at h traces since h>5.
Therefore gamma=cbar has exact order B when B<E and is zero modulo f_h^E when B>=E.
Similarly C_3 has image of primitive odd order l and derivative(X+1)^2, nonzero here because h>3.
Thus beta=bbar has exact order D when D<E and is zero when D>=E.
These are orders of the original actual canonical classes: the odd integer divisions are units modulo2, and reduction by U retains every full exponent.
Since Gbar=gamma^3, the nonzero-G assumption is EXACTLY

    E>3B.                                     (FM3)

In particular gamma^2 is nonzero modulo every psi^E and hence modulo the full f_h^E.
The element alpha=abar will be constrained without assuming beta=0.

#### A true modulo4 quotient lemma

Let J be ANY monic integer polynomial with Jbar=f^E, where f is monic binary, and choose any monic integer lift fhat of f.
There is an ACTUAL integer K with

    J=fhat^E+2K.

Work in the free finite-rank Z/4 module and ring

    S=(Z/4)[X]/(J).

The defining relation gives the two exact nilpotence relations

    fhat^(2E)=0 and 2fhat^E=0 in S.            (FM4)

Indeed fhat^E=-2K in S and its square is4K^2.
Let a_0,c_0 be arbitrary classes in S satisfying2c_0^2-3a_0^5=0.
If abar_0=0 in S/2S, write a_0=2v; then a_0^5=0.
More generally, if abar_0 is divisible by f^t and5t>=2E, choose actual representatives so that a_0=fhat^t A_0+2B_0 in S.
The ordinary binomial expansion modulo4 is

    a_0^5=fhat^(5t)A_0^5+
                      2fhat^(4t)A_0^4 B_0=0.  (FM5)

All terms with at least two copies of2B_0 vanish modulo4.
The first surviving term vanishes by5t>=2E, and the second by4t>=E and2fhat^E=0; the latter inequality follows from5t>=2E.
Thus in either case2c_0^2=0.
Because J is monic, S is free as a Z/4 module on the degree-bounded monomials, so the kernel of multiplication by2 is precisely2S.
Consequently

    cbar_0^2=0 in F_2[X]/f^E.                  (FM6)

No division by2 in a quotient ring, cancellation of a nonunit or Hensel lifting is used in this lemma.

#### Apply the lemma to the actual h-factor, without inheriting its canonical system

Let T_h be the COMPLETE actual integer product of all trace factors of T whose odd part is h.
It is a genuine monic divisor of T, and T_hbar=f_h^E.
Every other odd-order factor is a binary f_h-unit, but no integral coprimality between T_h and its cofactor is needed.

The original identity F=rem_T(2c^2-3a^5), together with FM1 and T_h|T, implies

    2c^2-3a^5=0 in (Z/4)[X]/(T_h).

Here a and c are the ORIGINAL canonical polynomials of T, only mapped to this factor quotient.
They are NOT replaced by the own canonical remainders of T_h.
The reduction gamma^2 is nonzero by FM3, so FM6 excludes alpha=0 modulo f_h^E.

C760's general largest-weight alternative now applies to the original fully cyclotomic T and gives

    t=ord_psi(alpha)=2(E-w)=2u for EVERY psi|f_h,
    E=w+u, 0<=u<w,
    w a power of2,
    V_w=F_(2wh)=F_(2h)(C_w) occurs once in T.  (FM7)

The quotient lemma also excludes5t>=2E.
On the other hand the reduction of the ORIGINAL F congruence modulo2 is alpha^5=0 modulo f_h^E, so5t>=E.
Combining these exact inequalities yields

    E/5<=t<2E/5,
    u>0, 4u<w<=9u, w>=8.                     (FM8)

In particular u=0 cannot occur: alpha would be a unit and F would not even be zero modulo2 on this component.
This argument handles that endpoint before making any valuation comparison.

#### Actual cofactor values and the mandatory first-residual tie

Put R=T/V_w, a genuine monic integer cofactor.
Its full binary exponents at odd orders h,k,l are respectively u,B,D; these three orders are distinct.
Thus there is an ACTUAL monic Z prime to f_h f_k f_l such that

    Rbar=f_h^u f_k^B f_l^D Z.

Choose any monic integral lift Z_tilde and form

    M=F_h^u F_k^B F_l^D Z_tilde,
    R=M+2H, H in Z[X].                        (FM9)

The identity is valid because both polynomials have the same actual binary reduction, not because their integer factors are asserted equal.

Take ANY primitive2wh root zeta, theta=zeta+zeta^(-1), and ANY normalized dyadic place with v(2)=1.
C760's general root/unit result applies since w>=8.
At C_2(theta) the reduced odd order is h, so only F_h contributes to the model valuation and v(F_h(C_2(theta)))=2/w.
At C_5(theta) the reduced odd order is k, so only F_k contributes and v(F_k(C_5(theta)))=1/w.
The other displayed factors are units in each respective evaluation.
FM3 and FM8 give

    2u/w<1/2,
    B/w<(w+u)/(3w)<5/12.

Hence both model values are below1, while the actual error2H has value at least1 at these integral arguments.
It cannot cancel either model value.
C760's dyadic half-unit for V_w and the fact that V_w(C_5(theta)) is a unit (odd order k rather than h) then give the ORIGINAL actual canonical values

    v(R(C_2(theta)))=v(a(theta))=2u/w,
    v(R(C_5(theta)))=v(c(theta))=B/w.           (FM10)

All divisions by2 and5 come from the actual integer canonical identities evaluated at T(theta)=0.

The two terms2c(theta)^2 and3a(theta)^5 have valuations1+2B/w and10u/w.
The first is strictly below11/6 and hence below2.
If the valuations differed, their difference F(theta) would have value below2, contradicting coefficientwise F=0 modulo4 and integrality of theta.
Therefore equality is NECESSARY:

    1+2B/w=10u/w,
    w=10u-2B, B=5u-w/2.                      (FM11)

This is only equality of valuations.
It does not assert that the two leading units cancel to the precision required by F modulo4.

Substituting FM11 into E=w+u>3B gives w>28u/5.
Together with FM8,

    28u/5<w<=9u,
    B=5u-w/2>=u/2>0.                         (FM12)

Thus B=0 is also excluded, without imposing any new source condition.
These inequalities leave positive arithmetic possibilities and do not themselves contradict a dyadic w.

#### The exact second-residual multiplicity and its two parity branches

Reducing the actual second residual modulo2 gives

    alpha^3+gamma^3=beta^2 modulo f_h^E.

The two left-hand candidate orders are6u and3B.
They cannot be equal: B=2u together with FM11 would force w=6u, impossible for a positive integer u and a power of2 w.
Since3B<E by FM3, the smaller of6u and3B is below E.
It cannot be canceled by the other term, and this holds at EVERY irreducible component of f_h.
Therefore beta is nonzero in that component and its true order satisfies

    2D=3 min(2u,B)<E,
    D=(3/2)min(2u,B).                          (FM13)

This is an ordinary integer equality, not a modular division by2.

The two possibilities are precisely:

    B<2u: 6u<w<=9u,
           B is even, D=3B/2, and u is even;
    B>2u: 28u/5<w<6u,
           D=3u, with no additional parity
           restriction obtained here.        (FM14)

For the first branch, integrality of D forces B even.
Since w>=8 makes w/2 even, B=5u-w/2 has the same parity as u, so u is even as well.
The second branch does not justify imposing B even or u even.
No uniform even-u conclusion is claimed.

One further actual evaluation follows AFTER these constraints.
FM12--FM13 give0<D/w<=3u/w<15/28<1.
At C_3(theta), the reduced odd order is l=h/3, so the model FM9 has exact valuation D/w; all the other-order factors are units.
The integer error still has value at least1.
Also V_w(C_3(theta)) is now a UNIT, not zero, since its reduced odd order after C_w is l rather than h.
The actual odd division by3 therefore gives

    v(R(C_3(theta)))=v(b(theta))=D/w.           (FM15)

This distinguishes the remaining15-divisible domain from C760's zero-beta case.
No assertion about cancellation of units in the second residual follows merely from the displayed orders.

#### Exact scope and remaining problem

Every nonzero binary G component of a fully cyclotomic input satisfying FM1 must already have15|h by adopted C760.
For each such component, the complete multiplicities E=E_h,B=E_(h/5),D=E_(h/3) must satisfy ALL FM7--FM15, with one actual single factor V_w and all original factors retained.
The original reciprocal degree stays2d; the single factor has trace degree w varphi(h)/2 and full reciprocal degree w varphi(h), with the remaining actual cofactor R retained.
No field degree, relative norm or total measure is divided by these quantities.

These are NECESSARY constraints on a potential full input, not a sufficiency theorem for a binary multiplicity profile, an integer coefficient lift or either residual congruence.
They do not establish either leading-unit cancellation, coefficientwise F modulo4, a full integer X condition, an example with nonzero Gbar, or the exclusion of every15-divisible profile.
The remaining15-divisible-order problem remains open beyond this constrained arithmetic and valuation interface.
No disposable experimental trial, native computation, characteristic-zero identity, Mahler bound or unrestricted G0001 conclusion is used or asserted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision fifteen-multiplicity-ties-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T23:16 |
| status | open |
| reason | Register the complete FM1--FM15 author theorem after root read the entire genuine modulo4 quotient lemma, actual canonical application, same-binary cofactor model, strict local bounds, forced valuation tie, exact second-residual multiplicities and separate parity branches. Every remaining nonzero binary G component of a fully cyclotomic F4/X2 input must satisfy the displayed arithmetic constraints at every irreducible component of its complete odd-order trace factor, with original degree and multiplicities retained. Root and characteristic_zero_bridge are contributors, not independent reviewers; fresh isolated whole review and separate adoption were still outstanding at author registration. These are necessary conditions only: no leading-unit cancellation, realizable profile, nonzero-G example, fifteen-domain exclusion or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete modulo4 lemma and necessary multiplicity theorem](#statement) | Parts A--D: generic actual monic quotient lemma, complete original cyclotomic F4/X2 domain, every15-divisible nonzero-G component, three true multiplicities, unique dyadic factor, exact strict bounds and two parity branches, all actual root/place evaluations and remaining realization/unit limits. |
| argument | [Entire FM1--FM15 proof](#complete-argument) | Full free-module modulo4 nilpotence and binomial argument, mapping the ORIGINAL canonical equation through T_h without canonical inheritance, general largest-weight input, actual three-order integer model with error2H, forced first-residual tie, exact second-residual comparison and later b-value, all endpoints/full degree/unknown-unit boundaries. |
| dependency | [Adopted full odd-order trace and support theorem](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) | Parts A--B and OT1--OT11: complete cyclotomic trace/endpoint factorization and uniform exponents, every split binary component, actual largest odd dyadic weight and single factor, general primitive-root valuations and dyadic half-unit, and localization of nonzero G to15-divisible orders. Its zero-beta h-prime-to3 conclusion is NOT applied to the present domain. Bel17/The26b inspection and normalization limits are retained through this exact adopted interface. |
| dependency | [Adopted actual canonical integer product and division interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Actual prime-divisible monic remainders and integral canonical/Delta identities, including repeated/shared factors. The present proof reduces the original residual identity modulo a genuine monic divisor; it never substitutes that divisor's own canonical system or divides by2 in a modular quotient. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T23:27 |
| status | proved |
| reason | Adopt the whole Parts A--D and FM1--FM15 through fresh independent whole R983, whose entire finding root read. The generic actual monic modulo4 quotient lemma, original-canonical factor mapping, all complete split-primary multiplicities, unique actual weight, real cofactor model, every root/place value and strict endpoint, necessary first-residual tie and both exact parity branches passed without substantive repair. Every possible nonzero binary G component at odd order divisible by15 must obey E=w+u, t=2u, w=10u-2B, 28u/5<w<=9u and 2D=3min(2u,B)<E, with the stated branch-specific parity and all three true canonical values. The minor undefined phi shorthand identified in the finding was expanded to the identical derivative (X^2+X+1)^2=f_5^2; the proof and source scope are unchanged. Root and characteristic_zero_bridge remain contributors. Equality of valuations is necessary only; no leading-unit cancellation, coefficientwise realization, compatible example, exclusion of all remaining profiles, Mahler bound or unrestricted Task completion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete modulo4 lemma and necessary multiplicity theorem](#statement) | Parts A--D: generic actual monic quotient lemma, complete original cyclotomic F4/X2 domain, every15-divisible nonzero-G component, three true multiplicities, unique dyadic factor, exact strict bounds and two parity branches, all actual root/place evaluations and remaining realization/unit limits. |
| argument | [Entire FM1--FM15 proof](#complete-argument) | Full free-module modulo4 nilpotence and binomial argument, mapping the ORIGINAL canonical equation through T_h without canonical inheritance, general largest-weight input, actual three-order integer model with error2H, forced first-residual tie, exact second-residual comparison and later b-value, all endpoints/full degree/unknown-unit boundaries. |
| dependency | [Adopted full odd-order trace and support theorem](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) | Parts A--B and OT1--OT11: complete cyclotomic trace/endpoint factorization and uniform exponents, every split binary component, actual largest odd dyadic weight and single factor, general primitive-root valuations and dyadic half-unit, and localization of nonzero G to15-divisible orders. Its zero-beta h-prime-to3 conclusion is NOT applied to the present domain. Bel17/The26b inspection and normalization limits are retained through this exact adopted interface. |
| dependency | [Adopted actual canonical integer product and division interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Actual prime-divisible monic remainders and integral canonical/Delta identities, including repeated/shared factors. The present proof reduces the original residual identity modulo a genuine monic divisor; it never substitutes that divisor's own canonical system or divides by2 in a modular quotient. |
| review | [Fresh independent whole multiplicity-tie finding](../audits/reviews/Yin_R_G0983_v1.md#whole-finding) | Entire standalone A--D and FM1--FM15 including the generic quotient lemma, full original factor mapping, all exact inequalities/branches/values and precise accepted-input/realization limits. |


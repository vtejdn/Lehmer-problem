---
author: Yin
---

# A normalized first-jet parity obstruction at the fifteenth-order lower-multiplicity branch

Human author Yin.
Provenance: project deduction under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the actual single-factor modulo4 quotient and normalized character argument.
Earlier_bit_obstruction checked the arbitrary remaining oddpart15 factors, all representative precisions, full polynomial compositions, scalar annihilator and genuine binary roots.
Root read the entire saved NFJ1--NFJ6 argument and checked its complete original-domain and normalization scope before this registration.
Both agents are substantive contributors; their author-side checking is not independent review.
The full necessary argument is fixed here, with no mutable Draft or native computation as a proof premise.
The initial open decision and subsequent whole review and adoption are retained below.

The adopted inputs are [C763's full original cyclotomic profile](Yin_C_G0763_v1.md#decision-whole-reviewed-2026-10-25), [C809's maximal binary normalization](Yin_C_G0809_v1.md#decision-whole-reviewed-2026-10-26), and the precise [C760 complete-factor](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) and [C736 integer canonical](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) interfaces they use.
The complete-factor character is taken from [C812's definition and TJ2 proof](Yin_C_G0812_v1.md#first-jet-trace-character) at its [adopted decision](Yin_C_G0812_v1.md#decision-whole-reviewed-2026-10-26).
Only that full character formula is consumed; C812's fixed-base no-additional-oddpart15 theorem is not applied to this changed profile.
The accepted source-inspection limits of those inputs remain in force; no new external theorem, source audit or priority claim is asserted.

## Statement

### NFJ1. Original domain, normalized conclusion and precise limits

Let T be a monic integer polynomial of degree d whose complete reciprocal z^d T(z+z^(-1)) is cyclotomic, with all actual factors and multiplicities retained.
Use its OWN original canonical system

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a=rem_T(T(C_2))/2,
    b=rem_T(T(C_3))/3, c=rem_T(T(C_5))/5,
    F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5),
    X_epsilon=rem_T(b^2-a^3+epsilon G),
    epsilon in{1,-1}.

Every scalar division and monic remainder is over Z at this SAME original T before coefficient reduction.
For j>=1, C_j is the monic integer trace polynomial characterized by C_j(z+z^(-1))=z^j+z^(-j).
For n>2, F_n is the complete primitive trace factor defined by z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z); indexed F_n is distinct from the canonical residual F.
For odd r>1 put f_r=F_rbar.
These are exactly the accepted C763 canonical and full-factor conventions, including every endpoint, dyadic conductor and actual multiplicity.
Assume coefficientwise F=0 modulo4 and X_epsilon=0 modulo2, and assume the original Gbar is nonzero on the complete oddpart15 primary.
Write the full binary factorization and the relevant three exponents as

    U=Tbar=X^A product_(r>1 odd) f_r^(E_r),
    f=f_15=X^4+X^3+1,
    E=E_15, B=E_3, D=E_5.

Here D is a multiplicity, not a cofactor polynomial.
Let q be the MAXIMAL dyadic integer for which U=U_*^q in F_2[X].
C763 and C809 give actual positive integers u,w and normalized integers

    E=w+u, w dyadic, V=F_(30w)=F_30(C_w)
         an actual factor occurring once in T,
    w=10u-2B, E>3B,
    w_*=w/q>=8, u_*=u/q>0,
    B_*=B/q, D_*=D/q,
    u_* and B_* even.

The factor q divides all full binary exponents, including A when nonzero.
Assume the C763 branch B<2u, equivalently

    6u_*<w_*<=9u_*, D_*=3B_*/2.              (NFJ1)

Then the necessary additional first-jet condition is

    D_* is even;
    B_*=0 modulo4 and u_*=0 modulo4.          (NFJ2)

In particular D_* is a multiple of6.
These are necessary conditions only, not sufficient unit equations or realizability assertions.
The normalized pairs (w_*,u_*)=(16,2) and(64,10) are excluded, while the normalized pair(32,4) is not excluded by NFJ2.
A literal multiplication of ALL binary exponents by2 also multiplies their maximal common dyadic q by2; it preserves the normalized profile and does not evade an exclusion.
No integer polynomial T_* with T_*bar=U_* and inherited canonical congruences is asserted or needed.
The result is confined to h=15 and the indicated branch; no exclusion of every fifteen-divisible order or every fully cyclotomic F4/X2 profile follows.

## Complete argument

### NFJ2. Retain every actual smaller fifteenth-order factor

Put P=F_15=X^4-X^3-4X^2+4X+1 and write the ACTUAL factorization

    T=V W H,
    Wbar=f^u, gcd(Hbar,f)=1.                 (NFJ3)

Here W contains ALL remaining complete trace factors whose exact odd part is15, with their actual dyadic conductors and multiplicities; H contains all other actual factors, including endpoints and pure2 factors.
No equality W=P^u over Z is imposed.
Since the total remaining weight u is less than w, every actual oddpart15 factor in W has smaller binary weight than w.
The original full degree remains d; V has trace degree4w, W has trace degree4u and H has trace degree d-4(w+u).
Their reciprocal degrees are twice these values, with no degree or multiplicity discarded in the proof.

Use only the actual finite free ring

    S=(Z/4)[X]/(V),
    delta_w=(V-P^w)/2 in Z[X].               (NFJ4)

The displayed half is integral because Vbar=f^w.
For every dyadic w>=8 the integer trace recurrence gives C_w=X^w+2 modulo4.
Indeed it holds for C_4=X^4-4X^2+2, and C_(2j)=C_j^2-2 preserves it by induction.
Substitution into F_30=P(-X) and repeated squaring of P give

    V=X^(4w)+X^(3w)+2X^(2w)+1 modulo4,
    P^w=X^(4w)+X^(3w)+1
          +2[X^(7w/2)+X^(2w)+X^(3w/2)] modulo4.

In the second formula the only mixed contributions surviving repeated squaring are twice the pair products at the preceding half-exponents; w/2 is even, so the sign in P modulo4 has no residual effect.
Taking the actual even difference yields

    deltabar_w=X^(7w/2)+X^(3w/2),
    Delta(V)bar=X^(7w)+X^(3w)=deltabar_w^2,
    Delta(V)=(V(C_2)-V^2)/2.                 (NFJ5)

For the second identity, V(C_2) modulo4 is X^(8w)+X^(6w)+2X^(4w)+1, whereas V^2 has the additional terms2X^(7w)+2X^(3w) and the same2X^(4w) term.
Thus its genuinely even difference, divided over Z and then reduced, is exactly the claimed square.
For any root x of f, x^4+1=x^3, so deltabar_w(x)=[x^3(x^4+1)]^(w/2)=x^(3w) is nonzero.
All these displayed delta classes are therefore units at f.

The defining relation in S is P^w=-2delta_w and hence2P^w=0.
Since V is monic, S is free over Z/4 and Ann_S(2)=2S.
For 0<=j<w it follows exactly that

    Ann_S(2P^j)=(2,P^(w-j)).                 (NFJ6)

Indeed 2P^j Z=0 is equivalent to f^j Zbar=0 in F_2[X]/f^w, and that annihilator is the ideal(f^(w-j)).
No division by2 or cancellation of P in a nonreduced ring is being assumed.

### NFJ3. Actual canonical representatives and all remaining half carries

Map the ORIGINAL a and c to S through the genuine divisor V of T.
C736's integer Delta identity gives a=rem_T Delta(T), so the full binary product identity and NFJ3--NFJ5 give

    abar=f^(2u) t^2 modulo f^w,
    t=Hbar deltabar_w.                       (NFJ7)

The omitted term Vbar^2 Delta(WH)bar has f-order at least2w and is zero at this stated precision, regardless of the actual factors and integer coefficients of W.
The odd canonical division gives cbar=U(chi) modulo f^w, where

    chi=C_5bar=X(X^2+X+1)^2,
    chi+1=(X+1)f.

Since U has exact full f_3=X+1 multiplicity B, the polynomial

    gamma=U(chi)/f^B                         (NFJ8)

is a GENUINE binary polynomial quotient and is a unit at f.
It is formed from the entire U and its composition before any truncation.
Choose classes in the actual ring S satisfying

    a=P^(2u) A_0+2B_0,
    c=P^B C_0+2D_0.

They exist because of the displayed binary divisibilities and the kernel of reduction S -> S/2S.
Their reductions have the exact controlled precisions

    A_0bar=t^2 modulo f^(w-2u),
    C_0bar=gamma modulo f^(w-B).              (NFJ9)

This construction does NOT assume that any positive power of P divides the actual integer a or c.
The unconstrained half-class B_0 is deliberately retained.

All terms with two factors2B_0 vanish modulo4, so the true binomial expansion in S is

    a^5=P^(10u) A_0^5+10P^(8u)A_0^4 B_0
       =-2P^(2B)delta_w A_0^5
                      +10P^(8u)A_0^4 B_0,
    2c^2=2P^(2B)C_0^2.                       (NFJ10)

Here10u=w+2B is the actual necessary C763 tie, not a formal scaling assumption.
Global coefficientwise F=0 modulo4 implies that2c^2-3a^5 is zero in S, since the removed original quotient is a multiple of T and hence of V.
Using NFJ6 with j=2B<w, NFJ10 gives the actual binary consequence

    C_0bar^2+deltabar_w A_0bar^5
       +f^(w-2u) A_0bar^4 B_0bar=0
                              modulo f^(w-2B).  (NFJ11)

The last exponent is8u-2B=w-2u.
The sign and the odd multiplier15 from the integer expression disappear only after this legitimate annihilator step and reduction modulo2.
Thus every possible unknown integer half of every smaller oddpart15 factor is accounted for in the displayed last term.

### NFJ4. Pay the precision before taking any binary root

Because u_* is a positive even integer, u_*>=2.
The branch6u<w gives

    w-2B=2w-10u>2u>=4q,
    w-2u>4u>=8q,
    w-B=(3/2)w-5u>4u>=8q.                  (NFJ12)

Consequently NFJ11 may be projected to modulo f^(4q), its last term vanishes there, and both replacements in NFJ9 are valid there even before their powers are taken.
The result is the NECESSARY polynomial congruence

    gamma^2+deltabar_w t^10=0
                                  modulo f^(4q).  (NFJ13)

This is precisely where the lower-multiplicity branch pays the otherwise unconstrained B_0 term.
It is not discarded merely because its coefficient arose from an integer half.
The two controlled unit representatives are known to more than twice the precision required by NFJ13.

All subsequent roots are in F_2[X], with their divisibility precisions proved explicitly.
Write

    Hbar=H_*^q,
    U_* = f^(w_*+u_*) H_*,
    delta_* = X^(7w_*/2)+X^(3w_*/2),
    d_* = X^(7w_*/4)+X^(3w_*/4),
    delta_*=d_*^2,
    t_*=H_* delta_*,
    gamma_*=U_*(chi)/f^(B_*).                (NFJ14)

The first equality follows from the full binary exponents divisible by q, after removing the complete f exponent E.
The last expression is an actual polynomial quotient for the same chi+1 identity as NFJ8.
Every one of H_*,delta_*,d_*,gamma_* is a unit at f.
Linearity of the displayed exponents in w and the genuine full compositions give EXACT polynomial identities

    deltabar_w=delta_*^q,
    t=t_*^q, gamma=gamma_*^q.

Substitute them into NFJ13 to obtain

    (gamma_*+d_*t_*^5)^(2q)=0
                                  modulo f^(4q).

Since f is irreducible and squarefree, the ordinary polynomial f-order of a2q-th power is2q times its original order.
Thus this is equivalent to

    gamma_*=d_*t_*^5 modulo f^2.              (NFJ15)

The argument constructs no integer q-th root, uses no presumed canonical system for U_*, and transfers no coefficientwise F4 condition to a new integer polynomial.
It descends only the explicit binary consequence of the original modulo4 equation.

### NFJ5. The complete-factor character forces the new parity

For any root x of f, use C812's first-jet character

    ell_x(v)=Tr_(F16/F2)[xv'(x)/v(x)],
    Tr(z)=z+z^2+z^4+z^8.

It is well-defined for a unit modulo f^2, because a change by a multiple of f^2 changes neither its value nor its derivative at x.
Only evaluation of the derivative is used; no derivative endomorphism of an odd-power quotient is assumed.
The explicit d_* has even exponents since w_*>=8; hence d_*'=0, and delta_*'=0 as well.
Applying the multiplicative-to-additive character to NFJ15 therefore gives

    ell_x(gamma_*)=ell_x(H_*).                (NFJ16)

To compute the left side without composing a local class, factor the FULL binary polynomial

    U_*=(X+1)^(B_*) U_3,
    U_3(1)=1.

Then the ACTUAL quotient in NFJ14 is

    gamma_*=(X+1)^(B_*) U_3(chi).

The first factor has zero logarithmic derivative because B_* is even.
Also chi(x)=1 and x chi'(x)=x(X^2+X+1)^2 at x equals1.
It follows that x gamma_*'(x)/gamma_*(x)=U_3'(1)/U_3(1) is an F_2 scalar, whose four-term trace is0.
Thus

    ell_x(gamma_*)=0.                         (NFJ17)

The polynomial H_* is the COMPLETE binary product

    H_*=X^(A/q) product_(r>1 odd,r!=15)
                                  f_r^(E_r/q),

with an absent X factor understood when A=0.
Its exponents are integers, but no claim is made that the actual integer H has a q-th root or is the corresponding chosen lift.
C812's formula for every complete f_r, including all r>15 divisible by15, and the zero endpoint character give

    ell_x(H_*)=E_3/q+E_5/q
              =B_*+D_*=D_* modulo2.          (NFJ18)

All remaining complete odd-order factors, arbitrary dyadic conductors, repeated factors and endpoints are covered in this sum.
In particular selected irreducible components are never substituted for their complete f_r.
Combining NFJ16--NFJ18 proves D_* even.

Finally D_*=3B_*/2 in the present branch, with B_* even, so D_* even is equivalent to B_* divisible by4.
The equality B_*=5u_*-w_*/2 and dyadic w_*>=8 then make it equivalent to u_* divisible by4.
This proves NFJ2 while preserving the original canonical divisor, all smaller oddpart15 factors and every original multiplicity.

### NFJ6. Remaining scope

The new information is a necessary normalized first-jet parity, not a source construction or a full unit-image characterization.
It rules out the displayed normalized profiles even with arbitrarily large complete extra cofactors and arbitrary actual smaller oddpart15 factors.
Profiles with u_* divisible by4 remain subject to all C763 valuation ties, C809 derivative and radical-degree costs, and their still-unsolved full original unit conditions.
Neither a passing original cyclotomic example nor exclusion of every such example is asserted.
The original reciprocal degree2d and its zero Mahler measure under the complete cyclotomic hypothesis are unchanged; no statement transfers to a chosen factor or a nontorsion input.
The complete-character input is adopted; the initial open decision and subsequent assessment of this changed-profile theorem are retained below.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision normalized-fifteenth-parity-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T19:36 |
| status | open |
| reason | Fix the complete original-domain h15 lower-multiplicity-branch parity theorem after root read all NFJ1--NFJ6 and the author checked the saved argument. The actual V-only modulo4 quotient retains every smaller oddpart15 factor and the unconstrained integer half B0; exact annihilator and representative bounds pay the descent to the genuine binary first jet. Maximal global q, complete-factor character, excluded normalized profiles and the raw-doubling distinction are retained. Root and earlier_bit_obstruction are substantive contributors; fresh independent whole review and separate adoption remain required. No native evidence, integer Frobenius-root inheritance, arbitrary-profile exclusion or unrestricted Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full normalized h15 parity statement](#statement) | Original complete cyclotomic T with own F4/X2 and nonzero h15 G component, maximal global binary q, branch B<2u, D_* even and equivalent B_*,u_* multiples of4, all actual factors, normalized exclusions and raw-doubling/remaining-scope limits. |
| argument | [Complete NFJ2--NFJ6 argument](#complete-argument) | Actual V-only free modulo4 ring, explicit dyadic delta identities, unknown integer half and exact annihilator, full unit-representative precisions, genuine binary q and square roots, full composition quotient and complete-factor character; NFJ1 supplies the exact original hypotheses and normalized definitions. |
| dependency | [Adopted necessary multiplicity ties](Yin_C_G0763_v1.md#decision-whole-reviewed-2026-10-25) | Own original canonical definitions and F4/X2 domain, h15 multiplicities E,B,D, unique actual V=F_(30w), w=10u-2B, E>3B and lower branch D=3B/2. No realization or unit cancellation is supplied by that input. |
| dependency | [Adopted maximal Frobenius normalization](Yin_C_G0809_v1.md#decision-whole-reviewed-2026-10-26) | The SAME global maximal q divides w,u,E,B,D and all binary exponents, with w_*>=8 and u_*,B_* even. No integer T_* or inherited canonical congruence is imported. Its derivative/radical cost remains a separate necessary condition. |
| dependency | [Adopted complete cyclotomic factor interface](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) | Full integral trace/endpoint factorization, complete squarefree odd-order reductions and dyadic weights, including all smaller oddpart15 factors, odd-order root separation and original canonical binary identities; exact accepted source-inspection limits remain unchanged. |
| dependency | [Adopted actual canonical product identities](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Integral scalar divisions and monic remainders at the original T, a=rem_T Delta(T), binary Delta product and legitimate restriction through the actual divisor V. No own-canonical factor inheritance is asserted. |
| dependency | [Adopted complete first-jet character](Yin_C_G0812_v1.md#decision-whole-reviewed-2026-10-26) | Definition #first-jet-trace-character and TJ2 only: well-defined root-evaluated logarithmic character on units modulo f squared, complete odd-factor values including higher orders divisible by15, endpoint character zero and multiplicative-to-additive sum. Its fixed-base exclusion and native corroborations are not premises here. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T19:46 |
| status | proved |
| reason | Adopt the complete unchanged original-domain normalized parity theorem after the responsible main agent read the entire fixed C813 and the entire fresh isolated R1033 finding. The actual V-only quotient, all smaller oddpart15 factors, unconstrained integer half, strict representative precisions, genuine binary roots and complete-factor character are covered without an integer normalized lift. The conclusion is exactly D_* even and equivalent B_*,u_* multiples of4 in the stated h15 lower branch. Its nonblocking reverse-definition-navigation omission is repaired by adding C813's actual NFJ5 consumer; two administrative status sentences now point to the retained decisions without changing any mathematics. No native evidence, arbitrary-profile realization or unrestricted Task conclusion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full normalized h15 parity statement](#statement) | Original complete cyclotomic T with own F4/X2 and nonzero h15 G component, maximal global binary q, branch B<2u, D_* even and equivalent B_*,u_* multiples of4, all actual factors, normalized exclusions and raw-doubling/remaining-scope limits. |
| argument | [Complete NFJ2--NFJ6 argument](#complete-argument) | Actual V-only free modulo4 ring, explicit dyadic delta identities, unknown integer half and exact annihilator, full unit-representative precisions, genuine binary q and square roots, full composition quotient and complete-factor character; NFJ1 supplies the exact original hypotheses and normalized definitions. |
| dependency | [Adopted necessary multiplicity ties](Yin_C_G0763_v1.md#decision-whole-reviewed-2026-10-25) | Own original canonical definitions and F4/X2 domain, h15 multiplicities E,B,D, unique actual V=F_(30w), w=10u-2B, E>3B and lower branch D=3B/2. No realization or unit cancellation is supplied by that input. |
| dependency | [Adopted maximal Frobenius normalization](Yin_C_G0809_v1.md#decision-whole-reviewed-2026-10-26) | The SAME global maximal q divides w,u,E,B,D and all binary exponents, with w_*>=8 and u_*,B_* even. No integer T_* or inherited canonical congruence is imported. Its derivative/radical cost remains a separate necessary condition. |
| dependency | [Adopted complete cyclotomic factor interface](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) | Full integral trace/endpoint factorization, complete squarefree odd-order reductions and dyadic weights, including all smaller oddpart15 factors, odd-order root separation and original canonical binary identities; exact accepted source-inspection limits remain unchanged. |
| dependency | [Adopted actual canonical product identities](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Integral scalar divisions and monic remainders at the original T, a=rem_T Delta(T), binary Delta product and legitimate restriction through the actual divisor V. No own-canonical factor inheritance is asserted. |
| dependency | [Adopted complete first-jet character](Yin_C_G0812_v1.md#decision-whole-reviewed-2026-10-26) | Definition #first-jet-trace-character and TJ2 only: well-defined root-evaluated logarithmic character on units modulo f squared, complete odd-factor values including higher orders divisible by15, endpoint character zero and multiplicative-to-additive sum. Its fixed-base exclusion and native corroborations are not premises here. |
| review | [Whole independent normalized first-jet finding](../audits/reviews/Yin_R_G1033_v1.md#whole-finding) | Entire exact statement and NFJ1--NFJ6 proof, all normalized and original integer interfaces, every complete factor and precision/carry step, exact adopted sources and excluded-profile/raw-doubling limits; symbolic whole review without finite computation. The reverse-definition consumer is repaired without mathematical change. |


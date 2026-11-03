---
author: Yin
---

# Endpoint480 shifts preserve the first residual modulo eight and swap the second signs modulo four

Human author Yin.
Root proposed the actual endpoint multiplier and checked the preliminary first-residual binomial invariance and the formed exact sign-swap proof as a substantive contributor.
Primitive_second_eight derived and checked the complete original weighted defects, binomial bounds, shared-divisor carries, genuine half/quarter transport and every iteration, and assembled this fixed argument.
Characteristic_zero_bridge developed the endpoint-family multiplicity context used during author work; all required factor coverage and the modulo8 global equivalence are explicitly proved here.
These are substantive author/contributor roles; no independent review of this new theorem is claimed.
This candidate was initially fixed OPEN for cold whole review and separate adoption; its current assessment is selected below.
No mutable Draft, selected-word/native result or other new unadopted Claim is a mathematical premise.
The theorem is conditional on the stated lower gates and does not assert the existence of an input satisfying them.

## Statement

### A. Exact actual family and original canonical definitions

Use C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), so C_j(z+z^(-1))=z^j+z^(-j).
For n>2 let F_n be the complete monic integer primitive trace factor defined by z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z).
Put

    P=F_15=X^4-X^3-4X^2+4X+1,
    f=Pbar=X^4+X^3+1,
    V=F_960, J=P^4 V, deg J=144,
    H_0=(X-2)^2 F_3^2 F_5^3 F_9^4 B_187,
    B_n=1+sum_(j=1..(n-1)/2)C_j for odd n>1.

Let Z be ANY finite actual rectangle product

    Z=product_(n,u,v) B_n(C_(3^u5^v))^(e_(n,u,v)),
    n>1 odd, gcd(n,15)=1, u,v>=0,
    e_(n,u,v)>=0 with finite support.

Allow the empty product, all repetitions and overlapping full divisor orders.
For k>=0 define

    H=H_0^2(X-2)^k Z, T=JH,
    U=(X-2)^480,
    T^(m)=T U^m for every m>=0,
    deg T=374+k+sum e_(n,u,v)3^u5^v(n-1)/2.          (ST1)

The single actual F_960 is retained and is not replaced by F_480^2.
All complete cyclotomic factors and endpoint multiplicities count.
The original reciprocal polynomial has degree2deg T and total logarithmic Mahler measure0.
The endpoint X-2 has multiplicity4+k in H; it is not replaced by X in any integer calculation.

For EVERY original polynomial W=T or T^(m), define its OWN integer canonical polynomials

    a_W=rem_W(W(C_2))/2,
    b_W=rem_W(W(C_3))/3,
    c_W=rem_W(W(C_5))/5,
    F_W=rem_W(2c_W^2-3a_W^5),
    G_W=rem_W(c_W^3-2b_W^5),
    X_(epsilon,W)=rem_W(b_W^2-a_W^3+epsilon G_W),
    epsilon in{1,-1}.

All prime divisions are genuine integer coefficient divisions before reduction, and all remainders use that SAME original W.
The residual F_W is distinct from the indexed primitive factor F_n and from P=F_15.

Assume ONLY the original lower gates

    F_T=0 modulo4,
    X_(epsilon,T)=0 modulo2 for one sign epsilon.   (ST2)

The other second sign is then even because their difference is2G_T.
No first-eighth or second-quarter gate is assumed.

### B. Exact higher-gate transformation, all iterations and complete costs

For either original sign and EVERY m>=0, the actual fixed-factor restrictions satisfy

    [F_(T^(m))]_J=[F_T]_J modulo8,
    [X_(epsilon,T^(m))]_J
       =[X_(((-1)^m epsilon),T)]_J modulo4.         (ST3)

These are equalities in the monic quotient by the ACTUAL J, not equality of different-degree global canonical polynomials.
All original residuals are divisible over Z by their full outside-J factor, which is a unit modulo(J,8).
Consequently ST3 gives the GLOBAL equivalences

    F_(T^(m))=0 modulo8 iff F_T=0 modulo8,
    X_(epsilon,T^(m))=0 modulo4
        iff X_(((-1)^m epsilon),T)=0 modulo4.       (ST4)

The lower gates ST2 remain valid at every step.
For one step T'=TU, the genuine integral normalized classes obey

    [(F_(T')/4)]bar_J=[(F_T/4)]bar_J,
    [(X_(epsilon,T')/2)]bar_J
       =[(X_(epsilon,T)/2)]bar_J+G_Tbar_J
                                      in F_2[X]/f^36. (ST5)

The increment G_Tbar_J has exact f-order12 and is nonzero.
These statements concern actual global integer halves and quarters, not division in a ring with2-torsion.

Thus a480 shift only exchanges the two second-quarter signs; two shifts are invisible at both displayed higher gates.
No number of such shifts can repair a failed first-eighth gate or change whether either second sign passes modulo4.
If one second sign passes, that sign alternates with m; both signs cannot pass simultaneously because G_Tbar_J is nonzero.
The actual cost is

    deg T^(m)=deg T+480m,
    full reciprocal degree increases by960m.        (ST6)

Every endpoint factor remains present, with multiplicity4+k+480m in the full outside-J factor.
The conclusion is restricted to the actual family ST1 under ST2 and to F modulo8 and X_plus/X_minus modulo4.
No higher-precision period, arbitrary cofactor invariance, selected-word success/failure, characteristic-zero residual equality or unrestricted Task conclusion is asserted.

## Complete argument

### ES1. Actual input, same fixed factor and global precision equivalence

Use P=F_15=X^4-X^3-4X^2+4X+1, f=Pbar=X^4+X^3+1, V=F_960 and J=P^4V.
Retain H_0=(X-2)^2F_3^2F_5^3F_9^4B_187 and any actual finite rectangle product Z from the statement.
For k>=0 set

    H=H_0^2(X-2)^k Z, T=JH,
    U=(X-2)^480, T'=TU=JH', H'=HU.               (ES1)

All original scalar prime divisions and monic remainders are taken at their OWN full T or T', respectively, before reducing to J.
Assume the actual original lower gates

    F_T in4Z[X], X_(epsilon,T) in2Z[X]

for one sign epsilon; the other second sign is then even as well because their difference is2G_T.
No higher gate is assumed.

Here is the complete integer coverage for this actual family, including the added endpoint.
C815's adopted full factorization gives

    B_n(C_(3^u5^v))
       =product_(r|n,r>1)product_(i=0..u,j=0..v)F_(3^i5^j r).

Every r is greater than1 and prime to15, so none of these factors coincides with the endpoint, the base orders3,5,9 or the fifteenth-order primary.
The merged multiplicities at3^i5^j r do not increase when i or j increases, including the two B_187 copies at i=j=0.
Cubing and fifth powering therefore encounter a predecessor of at least the required multiplicity; when the relevant exponent is0, they permute the same complete order set.
These trace maps have no critical source in these nonsmooth odd-order sets, so the full local multiplicities are retained.
Doubling permutes every complete odd-order set.

The remaining base multiplicities in H are endpoint4+k and exact odd orders3,5,9 with exponents4,6,8.
For p=2,3,5, C_p(2)=2 and C_p'(2)=p^2 is nonzero over characteristic zero, so T(C_p) retains endpoint multiplicity4+k.
At order3, C_3-2=(X-2)F_3^2 supplies multiplicity2(4+k)>=4.
At order9, cubing encounters the order3 exponent4; hence b_T has at least multiplicity4 and b_T^2 covers the required8.
Cubing permutes order5 and preserves exponent6.
For fifth powering, orders3 and9 are permuted, while C_5-2=(X-2)F_5^2 supplies multiplicity2(4+k)>=6 at order5.
All these same counts apply with k replaced by k+480 or k+480m.

Subtracting the actual quotient times T preserves the displayed monic factor powers.
Each scalar p is canceled only in the free integer quotient by that monic factor power.
Combining the complete monic factors gives

    H|a_T,c_T,b_T^2,b_T^5,F_T,G_T,X_(+,T),X_(-,T)
                                                   over Z. (ES1a)

The b^5 divisibility follows from the already sufficient b^2 multiplicities.
The residual divisibilities hold before and after their ORIGINAL T-remainders because H|T.
The same proof gives the full H' coverage at T'.
All endpoint and rectangle multiplicities remain present.
Both Hbar and H'bar are prime to Jbar=f^36.

The binary inverse of H or H' modulo J lifts also modulo8, as follows explicitly.
If H A=1+2B modulo J for integer lifts A,B, then A(1-2B+4B^2) is an inverse modulo8, since(1+2B)(1-2B+4B^2)=1+8B^3.
The same calculation applies to H' and to the lower moduli.
For either original residual R, write R=H L or H'L' with quotient degree below144=deg J.
Multiplication by that unit and monic degree-bounded reduction prove that coefficientwise vanishing modulo8 or4 is equivalent to vanishing of its ACTUAL J restriction.
This is the full global equivalence used below; no own unweighted residual of J replaces the original one.

In the ordinary torsion-free integer quotient A=Z[X]/J, write a,b,c,F,G,X_epsilon for the restrictions of the old original variables and residuals.
They satisfy

    a=P^4 A_0, b=P^4 B_0, c=P^4 C_0 in A.          (ES2)

For a, P(C_2)^4 contains P^4 because doubling permutes the full primitive15 traces.
For b, the actual F_5^6 source composed with C_3 contains P^6, using the complete integral identity F_5(C_3)=F_5 P.
For c, the actual F_3^4 source supplies P^4 through C_5+1=P*(X+1).
Subtracting the full T quotient preserves P^4, and cancellation of each scalar2,3,5 occurs in the free integer quotient by P^4.
Restriction by J preserves it because P^4|J.
C814 proves the actual base binary orders(a,b,c,G)=(8,6,4,12) at f.
For the full cofactor(X-2)^k Z, its values at C_2,C_3,C_5 are binary units at f: the residue arguments have exact trace orders15,5,3 and are nonzero, while no complete rectangle factor has any of those exact orders.
C736's actual weighted identity consequently preserves the first three orders, and Gbar=cbar^3 gives the fourth.
In particular C_0bar is a unit at f and Gbar=f^12 C_0bar^3 modulo f^36 is nonzero.

### ES2. Exact shared carry and all required binomial bounds

Put L=X+1 and define the genuine integer polynomial

    delta=(V-P^32)/2.

In A, and hence in S_4=(Z/4)[X]/J and S_8=(Z/8)[X]/J, the EXACT relation is

    P^36=-2P^4 delta.                              (ES3)

The adopted actual single-factor calculation gives

    deltabar=delta_32bar
             =delta_16bar^2=X^48(X+1)^64.           (ES4)

It is a unit at f.
This is a genuine half of the integer difference V-P^32, not a division by2 in a modular ring.
The monic quotient S_4 is free over Z/4, so its annihilator of2 is exactly2S_4.
In S_4 the carry gives

    2P^36=0, P^64=-2P^32 delta, P^96=0.

For r=5 or6 and any integer polynomials E,D, direct binomial arithmetic gives

    (1+PE+2D)^(2^r)
       =1+2P^(2^(r-1))E^(2^(r-1))
                              +P^(2^r)E^(2^r) modulo4. (ES5)

To justify every omitted coefficient, for0<j<2^r the identity j*binom(2^r,j)=2^r*binom(2^r-1,j-1) gives valuation r-v_2(j), since the latter binomial coefficient is odd.
Its oddness follows from(1+t)^(2^r-1)=1+t+...+t^(2^r-1) over F_2.
Only j=2^(r-1) survives modulo4, with coefficient2.
The even perturbation2D disappears upon an even power modulo4 by the same binomial expansion.
Thus ES5 is valid in the integer polynomial ring before restriction and its carry reduction.

If v=P^32 E+2P^16 D in S_4, then

    v^2=P^64 E^2 in2P^32 S_4,
    v^3=P^96 E^3+2P^80 E^2D=0.                    (ES6)

Consequently(1+v)^m=1+v for m=5 or45: m=1 modulo4, binom(m,2) is even, and all later powers vanish.
Odd powers of an element1+2P^32 W remain in1+2P^32 S_4.

### ES3. The actual endpoint weights, including the nontrivial fifth weight

The exact new cofactor weights are

    u_p=U(C_p)=(C_p-2)^480, p=2,3,5.

For any integer polynomial A, (A-2)^480=A^480 modulo8: the first correction has coefficient960, the second4*binom(480,2) is divisible by8, and all subsequent terms contain8.
Also

    u_2=(X^2-4)^480=X^960 modulo8,                (ES7)

because the first correction has coefficient4*480 divisible by8 and every later one contains16.
These integer congruences do not assert that the resulting weights equal1 in the larger modular quotient.

Since X^15=1 modulo f, write X^15=1+PE_2+2D_2 with actual integer polynomials E_2,D_2.
Applying ES5 with r=6 to X^960=(X^15)^64 and then ES3 gives

    u_2-1 in2P^32 S_4.                            (ES8)

For p=3, lambda=C_3bar=X^3+X satisfies

    lambda^3+1=(lambda+1)(X^2+X+1)f.

Thus A_3=(C_3-2)^3 has a representation1+PE_3+2D_3.
Now u_3=A_3^160=(A_3^32)^5, so ES5--ES6 imply

    u_3-1 in P^32 S_4+2P^16 S_4,
    u_3^2-1 in2P^32 S_4.                          (ES9)

Reduction modulo2 also gives u_3bar^2=1 and u_3bar^5-1 in(f^32), whence

    2(u_3^2-u_3^5) in2P^32 S_4.                   (ES10)

The necessary lift of this binary statement is valid because S_4 is free over Z/4; multiplying a coefficient-even error by2 kills it modulo4.

For p=5, direct integer multiplication gives

    P*(X+1)=X^5-5X^3+5X+1=C_5+1.

Thus C_5-2=1+PL-4, with L=X+1, is1+PL modulo4.
Write u_5^2=[(C_5-2)^64]^15; ES5 with r=6 and the subsequent odd fifteenth power give

    u_5^2-1 in2P^32 S_4.                          (ES11)

For the unsquared fifth weight needed in the second residual, u_5^3=(C_5-2)^1440 has1440=32*45.
ES5 with r=5 followed by ES6 with m=45 therefore gives the precise formula

    u_5^3=1+P^32 L^32+2P^16 L^16 in S_4.          (ES12)

The P^32 term is retained; discarding it because its binary order is high would lose the sign-changing integer carry below.

### ES4. The first residual is unchanged modulo8

C736's integer identity, first restricted from T' to T and then to J, gives

    F'=u_2^5 F+2(u_5^2-u_2^5)c^2.                 (ES13)

No quotient or scalar division is changed in obtaining this formula.
By ES8 and ES11, u_5^2-u_2^5 belongs to2P^32 S_4.
When lifted to S_8 it therefore has the form2P^32 W+4Z, because the monic coefficient reduction S_8 -> S_4 has kernel4S_8.
Using c=P^4 C_0 and the EXACT ES3 carry, its defect is

    2(u_5^2-u_2^5)c^2
        =4P^40 W C_0^2
        =-8P^8 delta W C_0^2=0 in S_8.

Also u_2^5-1 is even, and the assumed F in4Z[X] makes(u_2^5-1)F vanish modulo8.
Consequently the actual original restrictions satisfy

    [F_(T')]_J=[F_T]_J modulo8.                   (ES14)

By ES1 this proves that T' passes the GLOBAL first-eighth gate if and only if T does.
Their genuine integer quarter classes(F_(T')/4)|J and(F_T/4)|J have the same binary reduction; no modular division by4 is performed.
In particular the lower first-four gate is preserved.

### ES5. The second residual swaps its two signs modulo4

C736's full weighted identity for either sign gives in S_4

    X'_epsilon=u_3^2 X_epsilon
       +(u_3^2-u_2^3)a^3
       +epsilon(u_5^3-u_3^2)c^3
       +2epsilon(u_3^2-u_3^5)b^5.                  (ES15)

The first term equals X_epsilon modulo4 because X_epsilon is even and u_3^2-1 lies in2P^32 S_4.
The second term vanishes: its weight lies in2P^32 S_4 and a^3 is divisible by P^12, so it contains2P^44=0 by ES3.
The last term likewise vanishes by ES10 and b^5 divisible by P^20, which gives2P^52=0.
The u_3^2-1 part multiplying c^3 also vanishes by the same P^12 argument.
ES12 therefore leaves precisely

    X'_epsilon-X_epsilon
       =epsilon(P^32 L^32+2P^16 L^16)P^12 C_0^3
       =2epsilon P^12
                   [P^16 L^16-delta L^32]C_0^3 in S_4. (ES16)

Here the first term P^44 was reduced by the actual shared-divisor carry, not discarded as if the divisor were P^36.
The binary bracket has the EXACT polynomial identity

    f^16 Lbar^16+deltabar Lbar^32
       =[(f Lbar)+X^3 Lbar^6]^16
       =(1+Xf^2)^16
       =1+X^16 f^32.                              (ES17)

The first equality uses ES4, and the middle identity follows by expanding f=X^4+X^3+1 and Lbar=X+1.
Multiplication by f^12 annihilates the extra term modulo f^36.
Equivalently in S_4, replace the integer bracket in ES16 by1+P^32 X^16 plus a coefficient-even class; its remaining contribution is2P^44 X^16=0.
Thus ES16 is EXACTLY

    X'_epsilon-X_epsilon=2c^3=2G in S_4,
    [X_(epsilon,T')]_J=[X_(-epsilon,T)]_J modulo4. (ES18)

The sign on2epsilon c^3 is immaterial modulo4, and2G=2c^3 there because G=c^3-2b^5.
The lower second-bit gates are preserved, but a selected second-quarter sign is exchanged with the other one.
For the genuine integer halves this is

    [(X_(epsilon,T')/2)]bar_J
       =[(X_(epsilon,T)/2)]bar_J+Gbar
                                          in F_2[X]/f^36. (ES19)

It uses the actual global even polynomials and the free-module annihilator of2, not cancellation of2 in a ring with2-torsion.
The increment Gbar has exact f-order12 and is nonzero.

### ES6. Every successive shift and its complete cost

For m>=0 set T^(m)=T(X-2)^(480m).
It remains in the stated family with endpoint multiplicity4+k+480m, and ES14/ES18 preserve the hypotheses needed for each next step.
Induction gives

    [F_(T^(m))]_J=[F_T]_J modulo8,
    [X_(epsilon,T^(m))]_J
           =[X_(((-1)^m epsilon),T)]_J modulo4.    (ES20)

Thus two480 shifts are invisible at both displayed higher gates, while one shift only swaps the second signs.
The full GLOBAL statement follows each time from the integer H coverage and unit inverse at J proved in ES1.
In particular endpoint480 shifts cannot repair a failed first-eighth gate.
They also cannot change whether either second sign passes modulo4: if neither passed originally, neither ever passes; if one passed, the passing sign simply alternates.
Since X_plus-X_minus=2G and Gbar is nonzero, both signs cannot pass modulo4 simultaneously in this family.
No additional first-eighth/either-second-quarter feasibility is created by these shifts.

The actual trace degree increases by480m and the reciprocal degree by960m.
Every endpoint factor and multiplicity is retained; there is no cost-free kernel move or replacement of the actual single F_960.
The result concerns exactly F modulo8 and X_plus/X_minus modulo4 under the stated lower gates, and asserts no higher precision or unrelated cofactor invariance.
No selected-word existence, diagnostic or native residue array is a premise.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision endpoint480-higher-gates-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T21:55 |
| status | open |
| reason | Fix the universal endpoint480 transformation under the exact original F4/X2 hypothesis: unchanged first residual modulo8, swapped second signs modulo4, genuine half/quarter classes, every iteration and every actual degree cost. The whole argument includes complete endpoint/rectangle multiplicity coverage, scalar cancellation in integer monic quotients, the modulo8 unit inverse, full P4 divisibility of a/b/c, the genuine single-F960 carry and all binomial terms needed for the sign change. Root and primitive_second_eight are substantive contributors; characteristic_zero_bridge supplied the earlier endpoint-family context, with the full necessary proof now explicit here. No mutable Draft, selected native word or other new unadopted Claim is a premise. Fresh cold whole review and separate adoption remain outstanding; no existence or higher-precision claim is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact endpoint family and universal higher-gate transformation](#statement) | ST1--ST6: every actual rectangle product and k,m>=0, full original canonical definitions, conditional F4/X2 hypothesis, restriction equalities and global vanishing equivalences, genuine half/quarter classes, nonzero G increment, all signs/iterations/degrees and limits. |
| argument | [Complete ES1--ES6 proof](#complete-argument) | Full integer H coverage including every endpoint/3/5/9/rectangle multiplicity, original prime cancellation and P4 factors, modulo8 unit equivalence, true delta32 carry, exact binomial weight bounds, first-eighth invariance, second-sign swap and all iterations. |
| dependency | [Adopted original integer canonical product and unit interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Actual monic and prime divisions, full weighted residual/defect identities for both signs, and binary gcd/unit lifting; no own unweighted factor residual or arbitrary precision inheritance. |
| dependency | [Adopted actual doubled base and single-F960 carry](Yin_C_G0814_v1.md#decision-whole-reviewed-2026-10-26) | DP3--DP4 true delta32 and exact shared relation, actual base binary orders8/6/4/12 and normalized coefficients. Its B/Gamma-only exclusion, native image and selected-word data are not premises. |
| dependency | [Adopted explicit first-profile integer half](Yin_C_G0812_v1.md#decision-whole-reviewed-2026-10-26) | TJ13 actual delta16bar=X56+X24=X24(X+1)^32, used through the adopted single-F960 squaring identity; no higher-precision extrapolation or first-profile exclusion is invoked. |
| dependency | [Adopted complete actual rectangle factorization and multiplicity interface](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | Full B_n(C_(3^u5^v)) primitive factorization, complete degrees and nonincreasing predecessor multiplicities. The additional endpoint coverage and modulo8 global equivalence are proved explicitly here. No64-target enumeration or native classification is used. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T22:05 |
| status | proved |
| reason | Adopt the entire unchanged conditional endpoint480 transformation after the responsible main agent read the complete fixed C817 statement and ES1--ES6 proof and the whole isolated R1037 finding. The review covers every actual factor/multiplicity and original scalar division, P4 factors, modulo8 global equivalence, true single-F960 carry, all binomial terms, both residual defects, genuine half/quarter transport, all iterations and exact costs. No mathematical repair, selected-word existence premise or native-array input is used; initial-status prose is historical. Under the original F4/X2 hypotheses, every480 endpoint shift preserves the first-eighth condition and only exchanges the two second-quarter signs. No higher precision or unrestricted Task conclusion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact endpoint family and universal higher-gate transformation](#statement) | ST1--ST6: every actual rectangle product and k,m>=0, full original canonical definitions, conditional F4/X2 hypothesis, restriction equalities and global vanishing equivalences, genuine half/quarter classes, nonzero G increment, all signs/iterations/degrees and limits. |
| argument | [Complete ES1--ES6 proof](#complete-argument) | Full integer H coverage including every endpoint/3/5/9/rectangle multiplicity, original prime cancellation and P4 factors, modulo8 unit equivalence, true delta32 carry, exact binomial weight bounds, first-eighth invariance, second-sign swap and all iterations. |
| dependency | [Adopted original integer canonical product and unit interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Actual monic and prime divisions, full weighted residual/defect identities for both signs, and binary gcd/unit lifting; no own unweighted factor residual or arbitrary precision inheritance. |
| dependency | [Adopted actual doubled base and single-F960 carry](Yin_C_G0814_v1.md#decision-whole-reviewed-2026-10-26) | DP3--DP4 true delta32 and exact shared relation, actual base binary orders8/6/4/12 and normalized coefficients. Its B/Gamma-only exclusion, native image and selected-word data are not premises. |
| dependency | [Adopted explicit first-profile integer half](Yin_C_G0812_v1.md#decision-whole-reviewed-2026-10-26) | TJ13 actual delta16bar=X56+X24=X24(X+1)^32, used through the adopted single-F960 squaring identity; no higher-precision extrapolation or first-profile exclusion is invoked. |
| dependency | [Adopted complete actual rectangle factorization and multiplicity interface](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | Full B_n(C_(3^u5^v)) primitive factorization, complete degrees and nonincreasing predecessor multiplicities. The additional endpoint coverage and modulo8 global equivalence are proved explicitly here. No64-target enumeration or native classification is used. |
| review | [Whole independent endpoint-transformation finding](../audits/reviews/Yin_R_G1037_v1.md#whole-finding) | Entire ST1--ST6 and complete ES1--ES6 argument, all selected dependency applicability, exact original integer/quotient/global interfaces, both signs and all m>=0 with full source and calculation limits. No selected-word or Task completion inference. |


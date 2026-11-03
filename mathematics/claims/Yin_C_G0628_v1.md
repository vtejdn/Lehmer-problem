---
author: Yin
---
# Complete multiplicity-six complement obstruction and original branch exclusion

Human author Yin.
Root proposed the exact A_0=6 original-layer projection and local square-root reduction as a question, without assuming a complement classification.
The same_trace contributor checked those interfaces, derived the complete twelve-representative list, and proved the parity-survivor logarithmic-derivative obstruction below.
Both are mathematical contributors, and the new argument requires a fresh isolated whole review.
The work continues under the [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
Focused reuse inspected C197v3's normalized odd-part derivative, C199v4/v5's full original gate and complete complement, C609v2's actual endpoint parity, and C626's adopted multiplicity-four classification.
Those inputs supply the exact applicable conditions and a workable cube-representative method, but do not supply the new multiplicity-six contradiction.
This is a new statement at A_0=6, not a revision of C626's fixed A_0=4 theorem or an extrapolation from its finite support certificate.
All arithmetic below is explicit polynomial algebra; no new J, numerical scan, native program or external source theorem is used.
The initial status is open pending review.

## Statement

### Formal impossibility with the complete degree bound

Put phi=X^2+X+1, chi=Xphi^2 and Psi=phi(chi)=1+chi+chi^2 in F_2[X].
Let Y be any monic polynomial prime to Xphi with X^12 dividing Y'.
Let B be any monic polynomial prime to phi such that

    deg B<12,
    ord_X B is even.

The possible constant polynomial B=1 is included.
Define the units of F_2[X]_(phi)

    H=X^6Y,
    C=X^6Y(chi)Psi^42.

There is no such pair B,Y satisfying both

    HB=C^3 modulo phi^12,
    H^6=C^21 modulo phi^24.                    (SC1)

No degree bound on Y, complete-group factorization of Y or B, global square condition, endpoint-order equality, original field realization or integer-layer hypothesis is imposed in this formal assertion.
In particular the even ord_XB condition does not assume that B is a square.

### Entire normalized multiplicity-six branch

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient1 and degree d=2r.
For an original root alpha set K=Q(alpha), delta=alpha+alpha^(-1), and suppose F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r minimal polynomial of delta, so P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta).

Assume a,b,c are nonzero and, for one s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G=rem_T(theta_5^3-2theta_3^5), w=deg G<r, U=T mod2 and R_G=G mod2.
Assume the normalized circle Haar integral of log(G(z+z^(-1))^2), using the integrable logarithm at circle zeros, is0.
Assume also

    ord_phi R_G<ord_phi U,
    ord_psi R_G>=ord_psi U for every irreducible psi dividing U,
                                             psi!=phi.

Let q=2^k be the actual maximal power of2 for which U is a q-th power in F_2[X], and retain the actual canonical roots U=U_0^q and R_G=R_0^q supplied by C199.
Set A_0=ord_XU/q and add ONLY A_0=6.
There is no such original P,T and residual data.
This excludes the ENTIRE normalized multiplicity-six branch on this zero-Haar and unique-unsaturated domain, with arbitrary complete complements, every original q, every permitted integer layer and all complete higher5 support retained.

Combined with [C609v2's adopted A_0=2 exclusion](Yin_C_G0609_v2.md#decision-whole-reviewed-2026-10-23), [C626's adopted entire A_0=4 exclusion](Yin_C_G0626_v1.md#decision-whole-reviewed-2026-10-23), and C199's inherited evenness, the remaining normalized multiplicities on this exact original domain are even A_0>=8.
This last range statement uses the two prior exclusions; the present A_0=6 proof does not depend on their proofs or native support certificates.
No restriction to powers of2 is imposed.
Multiple unsaturated factors, positive Haar, other original domains and the unrestricted G0001 objective remain outside this exclusion.

## Argument

### The low-X derivative supplies the exact local square

Under the formal hypotheses, write uniquely

    Y=1+u_1X^2+u_2X^4+u_3X^6+u_4X^8+u_5X^10
                                                  modulo X^12,
    u_i in F_2,
    L=1+u_1chi+u_2chi^2+u_3chi^3+u_4chi^4+u_5chi^5,
    Q=X^3Psi^21 L.                              (SC2)

The constant is1 because Y is prime to X.
Every odd coefficient below degree12 vanishes because its derivative would have degree below12.
Since ord_phi chi=2, substitution and characteristic-two squaring give

    C=Q^2 modulo phi^24.                        (SC3)

The omitted Y terms have X-degree at least12 and hence substituted phi-order at least24.
This is a local identity and does not assert a global square root of Y.

Raise the first congruence in (SC1) to the sixth power.
Its error is squared before being cubed, so the resulting error is divisible by phi^24.
Combining with the second congruence and dividing by the unit C^18 gives

    B^6 C^3=1 modulo phi^24.

Substitute (SC3), and use ord_phi(f^2)=2ord_phi f for a polynomial or rational local-ring element.
The result is

    (BQ)^3=1 modulo phi^12.                     (SC4)

All divisions here are by units at phi.
No stronger square-root precision is inferred from a truncated jet.

### Cube roots and the degree-determined representatives

Put p=phi and work first in S_12=F_2[X]/(p^12).
The polynomial

    beta=X+p+p^2+p^4+p^8=X^16

satisfies beta^2+beta+1=p^16=0 in S_12, and beta'=0.
Thus {0,1,beta,beta^2} is a coefficient copy of F_4 in S_12.
Each unit has a unique residue gamma in {1,beta,beta^2} and can be written gamma(1+h), with h in pS_12.
If h!=0 has least p-order j, then h+h^2+h^3 has the same least order j, since 1+h+h^2 is a unit.
Consequently (1+h)^3=1 forces h=0, and (SC4) is exactly

    BQ=gamma modulo p^12,
    gamma in{1,beta,beta^2}.                    (SC5)

Reduce (SC5) modulo p^6, whose degree is12.
Because Psi^21=Psi modulo p^6, while chi has order2, (SC2) gives

    Q=X^3[1+(1+u_1)chi+(1+u_1+u_2)chi^2]
                                                  modulo p^6.

Write a=1+u_1 and b=u_2.
Inverting this unit gives

    B=gamma X^(-3)(1+a chi+b chi^2) modulo p^6.
                                                           (SC6)

The strict actual bound deg B<12 makes this residue the entire polynomial B, not merely a necessary low jet of an unrestricted complement.
There are exactly twelve candidate representatives, one for each gamma and a,b in F_2.
For transparency, set f_0=X^(-3), f_1=X^(-2)p^2 and f_2=X^(-1)p^4 in S_6=F_2[X]/(p^6).
Then B is the degree-below12 representative of gamma(f_0+a f_1+b f_2).
All three coefficient polynomials for each gamma are displayed here:

| gamma | gamma f_0 | gamma f_1 | gamma f_2 |
| --- | --- | --- | --- |
| 1 | X^11+X^7+X^5+X^3+X | X^10+X^8+X^4+X^2 | X^11+X^9+X^7+X^5+X^3+X |
| beta | X^11+X^7+X^3+X | X^6+X^4+X^2 | X^11+X^7+X^3 |
| beta^2 | X^5 | X^10+X^8+X^6 | X^9+X^5+X |

This table is verified directly by

    p^6=X^12+X^10+X^6+X^2+1,
    beta=X^8+1 and beta^2=X^8 in S_6,
    X^3 f_0=1, X^2 f_1=p^2, X f_2=p^4.

For the first row, multiplication by the indicated power of X leaves exactly the displayed numerator plus a multiple of p^6.
For the third row, X^8 f_0=X^5, X^8 f_1=X^6p^2, and X^8 f_2=X^7p^4=Xp^4 in S_6, the last equality following from p^2 dividing X^6+1.
The second row is the sum of the first and third, since beta=1+beta^2.
This supplies an exact symbolic certificate for all twelve representatives, without an enumerating program.
The twelve are distinct because their residues first distinguish gamma, and then their chi and chi^2 coefficients distinguish a,b.

### Endpoint parity leaves exactly one polynomial

For gamma=1 and b=0, the coefficient of X is1 and no lower term occurs, for either a.
For gamma=1 and b=1, f_0+f_2=X^9; a=0 gives odd X-order9, whereas a=1 gives even X-order2.
For gamma=beta, the coefficient of X is always1, because only the first table entry contains X.
For gamma=beta^2 and b=0, the order is5 for either a; for b=1 it is1 for either a.
Therefore the sole candidate with even ord_XB is

    gamma=1, a=b=1, u_1=0, u_2=1,
    B_*=X^10+X^9+X^8+X^4+X^2.                 (SC7)

It is monic, prime to phi and of degree10.
Indeed B_*=X^9+E^2 with

    E=Xphi(X^2+1)=X^5+X^4+X^2+X,

so B_* has residue1 modulo phi.
The parity filter has not asserted that B_* is a square; its X^9 term makes that assertion false.
The initially possible B=1 has also been covered and eliminated by (SC6) and the table.

### The surviving logarithmic derivative has exact order six

For (SC7), retain the three still arbitrary bits u_3,u_4,u_5 and put

    L=1+chi^2+u_3chi^3+u_4chi^4+u_5chi^5,
    Q=X^3Psi^21L,
    tau=X^3+X.

Both L and Psi have residue1 modulo phi.
The exact derivative identities B_*'=X^8, chi'=phi^2 and Psi'=phi^2 give

    (B_*Q)'/(B_*Q)
       =X^8/B_* + 1/X + phi^2/Psi
                      +phi^2(u_3chi^2+u_5chi^4)/L.

Since 1/X+phi^2/Psi=(1+chi^2)/(XPsi), a common unit denominator is X B_* Psi L.
The exact numerator is

    N=[X^9Psi+B_*(1+chi^2)]L
                         +B_*Psi(u_3chi^3+u_5chi^5).        (SC8)

Its bracket has the polynomial identity

    X^9Psi+B_*(1+chi^2)
       =X^9chi+E^2(1+chi^2)
       =[X^5phi+E(1+chi)]^2
       =phi^2chi^2(1+tau)^2.                    (SC9)

For the last equality, factor out phi and use

    X^5+X(X^2+1)=chi,
    X(X^2+1)=tau.

Let bar_beta be the image of X in F_2[X]/(phi)=F_4, so bar_beta^2+bar_beta+1=0.
The first term in (SC8), after (SC9), has phi-order6; the u_3 term has order6 if u_3=1, and the u_5 term has order10 if u_5=1.
After division by phi^6 and reduction modulo phi, use

    B_*=Psi=L=1,
    X^3=1,
    tau=1+bar_beta=bar_beta^2

to obtain

    N/phi^6 =bar_beta+u_3 modulo phi.            (SC10)

Indeed the first term contributes bar_beta^2(1+bar_beta^2)^2=bar_beta, and the second contributes u_3.
Since u_3 lies in F_2 while bar_beta does not, (SC10) is nonzero for both choices.
The denominator in (SC8) is a phi-unit, and therefore

    ord_phi((B_*Q)'/(B_*Q))=6.                 (SC11)

But (SC5) and (SC7) require B_*Q=1 modulo phi^12.
The derivative of phi^12 is zero in characteristic two, so differentiating that congruence and dividing by the unit B_*Q requires the left side of (SC11) to have order at least12.
This contradiction proves the entire formal assertion (SC1), including every possible u_3,u_4,u_5 and every initial B,Y.

### Exact original layers before projecting the full gate

Return to the original domain with A_0=6 and q=2^k.
Use the [complete normalized C199v4 gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) and the [C199v5 original-layer statement](Yin_C_G0199_v5.md#statement).
Its integer factorization retains the original nonnegative a_b, with

    lambda_0=lambda_1=1,
    lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=36q.

The normalized correction window is exactly12q<lambda_b<36q, so the only possible powers in that window are16q and32q, at the ORIGINAL indices k+5 and k+6.
Set epsilon_16=a_(k+5) mod2 and epsilon_32=a_(k+6) mod2.
The exact formula UR17 is

    S_star=epsilon_16 X^8(X+1)^16phi^20
                  +epsilon_32 X^16(X+1)^32phi^4.            (SC12)

The two displayed coefficients are units at phi.
UR20 requires phi^6 to divide S_star, and the possible leading orders20 and4 are distinct, so epsilon_32=0.
Moreover the actual nonnegative weight sum36q gives a_(k+6)<=1, hence

    a_(k+6)=0,
    S_star=epsilon X^8(X+1)^16phi^20,
    epsilon=a_(k+5) mod2.

Every other original layer and its full integer multiplicity remains present; no a_b is divided by q, and no free normalized parity list is substituted.
The factors (X+1)^16 and phi^20 are retained exactly.

Write the same actual local units as

    H_0=X^6Y, C_00=X^6Y(chi)Psi^42,
    V_0=R_0/phi^36=H_0B,
    D_0=V_0+C_00^3.

The root Z_0 is specified modulo phi^18 by Z_0^11=H_0C_00^2 and is a unit.
The complete gate is

    Z_0D_0+H_0V_0S_star=0 modulo phi^24.

It first has the inherited D_0 in phi^6, so changing the root representative by phi^18 changes this equation only by phi^24, as in UR18--UR19.
With (SC12) and epsilon_32=0, the complete equation then forces D_0 in phi^20.
In particular it implies H_0B=C_00^3 modulo phi^12.
The unchanged old support identity is H_0^6=C_00^21 modulo phi^24.
These are exactly the two congruences (SC1); the projection uses the paid full error modulus, not an assumed improvement of root precision.

### The same canonical input supplies every remaining formal hypothesis

The [C199v4 complete complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) supplies the actual unique monic B prime to phi with deg B<12.
It contains every surplus multiplicity at saturated factors and every extra factor of the canonical R_0; there is no uncounted factor or chosen smaller representative.
The same normalized factorization has Y monic prime to Xphi.
The [C197v3 odd-part derivative theorem](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) gives X^12 dividing W_U', where Y=J^2W_U and J(0)=1.
Thus X^12 divides Y', with no identification of W_U and the distinct G-unit odd part.
The [C609v2 actual complete-factor parity theorem](Yin_C_G0609_v2.md#statement) gives ord_XB even at these original hypotheses.
That use depends on the complete actual V_0 factorization and its phi-derivative order; it does not assume that Y alone is a product of complete order groups.

All formal hypotheses have now been verified for the SAME actual B,Y,H_0,C_00.
The formal contradiction excludes the entire original A_0=6 branch.
The maximal q is the actual global Frobenius power of U and R_G from C199, whose R_0 is nonsquare; neither maximality nor nonsquareness is inferred from a finite jet.
All canonical C3/C5 and characteristic-zero residual conditions remain hypotheses of the original result, even though the contradiction uses their necessary interfaces rather than constructing a lift satisfying them.

For degree accounting before the contradiction, the exact canonical polynomial identities give

    deg U_0=90+deg Y,
    deg R_0=78+deg Y+deg B,
    r=q(90+deg Y).

At the sole formal parity survivor deg B_*=10, these become deg R_0=88+deg Y and r-deg R_G=2q.
The inherited zero-Haar integer cyclotomic factorization has leading coefficient1 or-1, so reduction does not lower deg G here, giving the conditional costs

    w=q(88+deg Y), r-w=2q, 2w=d-4q.

These are costs of the ruled-out candidate, not an original construction or a smaller trace-field theorem.

### Scope of the new exclusion

The new formal obstruction is independent of complete-group image computation and does not expand J125, J126 or their fixed questions.
The special projection used the precise A_0=6 integer window and the absence of the32q layer.
It is not a general formula for every even A_0: an allowed normalized layer lambda_b/q between4A_0 and5A_0 can give a correction order below2A_0, so that projection requires its own proof at other multiplicities.
No automatic next-multiplicity search or arbitrary degree/support scan is part of this result.
The two adopted earlier exclusions and the present one leave even A_0>=8 on the exact stated original domain; that remaining range and the unrestricted Task are unresolved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:15 |
| status | open |
| reason | Register the complete analytic multiplicity-six formal impossibility and its full original zero-Haar/unique-unsaturated application. The exact twelve degree-determined representatives, parity survivor, order-six derivative contradiction, original q and integer layers, canonical complement and degree costs are retained. This new proof awaits fresh isolated whole review; no Task completion or extrapolation to other multiplicities is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Formal and original theorem](#statement) | Every monic B of degree below12 and arbitrary Y under the explicit derivative/parity/two-congruence hypotheses; entire actual A_0=6 exclusion for every original q, plus the stated remaining-range consequence. |
| argument | [Complete SC1--SC12 argument](#argument) | Exact local square precision, coefficient-field cube roots, all twelve representatives, exhaustive parity filter, exact logarithmic-derivative obstruction and same-original-input application with full integer layers and canonical degrees. |
| dependency | [Original domain and normalized interfaces](Yin_C_G0199_v5.md#statement) | Exact P/T/field/residual/Haar/unique-unsaturated hypotheses, maximal global q and nonsquare canonical root, normalized gate and old relation, integer cyclotomic layers and inherited even A_0. |
| dependency | [Complete normalized gate proof](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | UR13--UR20 original normalization, exact S_star window, root precision, full error modulus and required phi^(A_0) divisibility; applied at A_0=6 with the original a_b retained. |
| dependency | [Complete canonical complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) | UR22 complete B, all surplus/extra factor costs, phi-unit property and strict bound deg B<2A_0. |
| dependency | [Original T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | QX17--QX20 normalized odd part gives X^12 dividing W_U' and hence Y'; no equality with the G-unit odd part. |
| dependency | [Complete actual parity and prior A_0=2 exclusion](Yin_C_G0609_v2.md#statement) | Actual ord_XB even through complete V_0 and derivative gate; its prior A_0=2 exclusion is used only for the final remaining-range consequence. |
| dependency | [Prior complete A_0=4 exclusion](Yin_C_G0626_v1.md#statement) | Used only with C609v2 and inherited evenness to state the remaining even A_0>=8 range; not an input to the new A_0=6 formal contradiction. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:25 |
| status | proved |
| reason | Adopt the complete multiplicity-six formal impossibility and entire original A_0=6 exclusion after main reading of the whole fixed C and isolated R831. The twelve complete representatives, unique even-order survivor, exact derivative obstruction, original integer window and every canonical/source hypothesis are checked. All q and complete complements are covered on the stated zero-Haar and unique-unsaturated domain; with the adopted A_0=2,4 results, remaining multiplicities are even A_0>=8. Other domains and the unrestricted Task remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Formal and original theorem](#statement) | Every monic B of degree below12 and arbitrary Y under the explicit derivative/parity/two-congruence hypotheses; entire actual A_0=6 exclusion for every original q, plus the stated remaining-range consequence. |
| argument | [Complete SC1--SC12 argument](#argument) | Exact local square precision, coefficient-field cube roots, all twelve representatives, exhaustive parity filter, exact logarithmic-derivative obstruction and same-original-input application with full integer layers and canonical degrees. |
| dependency | [Original domain and normalized interfaces](Yin_C_G0199_v5.md#statement) | Exact P/T/field/residual/Haar/unique-unsaturated hypotheses, maximal global q and nonsquare canonical root, normalized gate and old relation, integer cyclotomic layers and inherited even A_0. |
| dependency | [Complete normalized gate proof](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | UR13--UR20 original normalization, exact S_star window, root precision, full error modulus and required phi^(A_0) divisibility; applied at A_0=6 with the original a_b retained. |
| dependency | [Complete canonical complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) | UR22 complete B, all surplus/extra factor costs, phi-unit property and strict bound deg B<2A_0. |
| dependency | [Original T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | QX17--QX20 normalized odd part gives X^12 dividing W_U' and hence Y'; no equality with the G-unit odd part. |
| dependency | [Complete actual parity and prior A_0=2 exclusion](Yin_C_G0609_v2.md#statement) | Actual ord_XB even through complete V_0 and derivative gate; its prior A_0=2 exclusion is used only for the final remaining-range consequence. |
| dependency | [Prior complete A_0=4 exclusion](Yin_C_G0626_v1.md#statement) | Used only with C609v2 and inherited evenness to state the remaining even A_0>=8 range; not an input to the new A_0=6 formal contradiction. |
| review | [Independent whole multiplicity-six finding](../audits/reviews/Yin_R_G0831_v1.md#whole-a6-complement-obstruction-finding) | Entire formal and original statement, complete SC1--SC12 proof, exhaustive representatives and parity, exact derivative order, UR20 layer exclusion, full root/error precision, all actual input and conditional degree interfaces; historical source and SELF/UNKNOWN limits unchanged. |


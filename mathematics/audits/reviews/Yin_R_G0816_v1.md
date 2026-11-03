---
author: Yin
---
# Whole independent review of the unbounded canonical-control family

Date: 2026-10-23T16:51.
Human record author Yin.
This is a separately organized isolated whole review of [C613v1](../../claims/Yin_C_G0613_v1.md#statement), whose initial decision is dated 2026-10-23T16:42.
The reviewing agent was outside substantive proof development and received the fixed target, its exact input locators, review scope and operational conditions without inherited proof-generation discussion, mathematical summaries, author explanations or previous conclusions about this proof.
The target's complete statement, argument, input table and selected initial relations were read directly.
D35, development reports and other agents' development conversations were not consulted.
A second separately isolated reviewer checked only the integer lifts, UC5--UC7, zero Haar and the two vanishing divided quotients after the whole reviewer had independently reconstructed those steps.
Neither reviewer supplied a repair or edited the target.
The historical R477 and R489 relationship declarations were inspected after the initial mathematical findings to preserve their actual accepted-input limits.

This record makes no C/T adoption and does not change the research execution state.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole family finding](#whole-unbounded-family-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole family finding](#whole-unbounded-family-finding) | [Complete C613v1 statement](../../claims/Yin_C_G0613_v1.md#statement) | Every s>=2, deterministic least even k, all UC1--UC3 controls, complete groups, exact maximal q, every original q=2^t>=2, both signs and every monic integer lift of the specified full reduction. |
| [Whole family finding](#whole-unbounded-family-finding) | [Complete C613v1 argument](../../claims/Yin_C_G0613_v1.md#argument) | Entire UC1--UC7 proof: both recurrence moduli, root closure, all primary remainder components, global multiplicities, integer lifts and degrees, Haar value, exact full defects and C197 contradiction. |
| [Whole family finding](#whole-unbounded-family-finding) | [C608v1 argument](../../claims/Yin_C_G0608_v1.md#argument) | Selected dependency only: B_n root definition, squarefreeness, inverse-pair partition, Laurent recurrence and polynomial matrix identities; these were reconstructed directly, without using its finite character certificate. |
| [Whole family finding](#whole-unbounded-family-finding) | [C197v3 statement](../../claims/Yin_C_G0197_v3.md#statement) | Exact accepted arbitrary-monic QX1--QX2 domain, A=qA_0, N=7qA_0, all distinct irreducible factors of Y with B_i=q>=2, and both actual canonical residual congruences modulo4. |
| [Whole family finding](#whole-unbounded-family-finding) | [C197v3 local mod4 bridge](../../claims/Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | QX13--QX14 necessity at order4qA_0, with every extra numerator and composition factor retained in the exact rational unit mathcalF^q; accepted theorem reuse and checked full application, not a new whole C197 review. |
| [Whole family finding](#whole-unbounded-family-finding) | [C199v4 normalized gate](../../claims/Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Selected formal comparison: actual definitions H_0,C_00,V_0,D_0, original integer a_b and lambda_b, S_star, root precision3A_0 and full gate precision4A_0; G_star has only the low order5 layer, without asserting the original residual hypotheses. |
| [Whole family finding](#whole-unbounded-family-finding) | [C609v2 statement](../../claims/Yin_C_G0609_v2.md#statement) | Comparison only: complete-group endpoint and complement parity; the target's two exact orders are independently calculated and no sufficiency or global-square implication is imported. |
| [Whole family finding](#whole-unbounded-family-finding) | [C613v1 exact inputs](../../claims/Yin_C_G0613_v1.md#exact-inputs-and-review-boundary) | All five input rows, their logical versus comparison roles, complete degree costs, lack of original realization and unrestricted remaining-support boundary. |
| [Whole family finding](#whole-unbounded-family-finding) | [C613v1 initial selection](../../claims/Yin_C_G0613_v1.md#decision-initial) | Exact statement, argument, three dependency rows and two support rows inspected at the fixed initial version, without selecting a later assessment. |

<a id="whole-unbounded-family-finding"></a>
## Whole family finding

**The complete C613v1 statement and argument pass this independent whole review at their stated scope.**
No mathematical gap, missing used hypothesis, omitted support factor or required correction was found.
The parameter-uniform construction proves that the displayed canonical, complete-support, derivative and parity controls do not imply the full normalized unit condition.
The accepted arbitrary-monic C197 necessity also excludes every integer lift of each stated original reduction for both signs.
This does not classify all even A_0>=4 supports or settle G0001.

### Parameter choice, exact recurrence and complete roots

Write a=A_0 throughout this verification.
The least even k>=s+2 is either s+2 or s+3, so L is exactly 4a or 8a and is at least16.
Since 2^k=1 modulo3, n=1+10L is2 modulo3 and1 modulo5; n is odd and gcd(n,15)=1.
In particular the endpoint and order3/order5 groups are absent from Y.

For the matrix M=[[X,1],[1,0]] over F_2[X], multiplication gives M^2-I=XM and M^5-I=phi[phi M+(X+1)I].
The scalar identity matrix commutes with M, so Frobenius gives M^(5L)-I divisible by phi^L and M^L-I divisible by X^(L/2).
The second assertion also gives M^(5L)=I modulo X^(L/2).
Applying M^(5L) to (B_3,B_1) produces (B_(3+10L),B_(1+10L)); its second component therefore proves both asserted congruences for Y=B_n.
No interpolation in n or finite order test is used.

There are n-1 nonidentity n-th roots, and no such root is its own inverse because n is odd.
Two roots with trace x solve z^2+xz+1=0, so the inverse-pair traces are distinct.
Frobenius invariance places their monic product in F_2[X], with degree5L and all factors simple.
The nonconstant squarefree polynomial Y has nonzero derivative.
The disjoint exact-order partition includes every group of order d>1 dividing n, once each.
The maps z->z^3 and z->z^5 permute those complete sets and induce tau and chi on their traces; hence Y divides both Y(tau) and Y(chi).

Differentiating Y-1 in (phi^L) and in (X^(L/2)) preserves the respective ideals because both exponents are even.
All other factors multiplying Y in U_0,R_0,V_0 have even exponents and are disjoint from Y.
Their derivatives are the nonzero product of that multiplier and Y', proving every nonsquare assertion and the derivative controls.
Every Y factor has exact multiplicity1 in both U_0 and R_0.
After the q-th power its exact multiplicity is q, so neither polynomial is a 2q-th power, while both are q-th powers.
This proves the claimed global maximum without a local-jet inference.

### Every canonical component and complete degree cost

The identities tau=X(X+1)^2 and phi(tau)=phi(X)(X^4+X^3+1), together with Y dividing Y(tau), prove U_0 divides U_0(tau) with all displayed multiplicities.
Both maps fix0, tau permutes the order5 trace pair, and chi maps that pair to0.
Together with the complete Y groups, this verifies preservation of the entire geometric support.

The three coprime factors X^a, phi^(7a) and Y exhaust U_0.
At X, U_0(chi)^3 has exact order3a and R_0 has exact order a; both vanish modulo X^a.
At Y, the composition is divisible by Y^3 and R_0 is divisible by Y.
At phi, factoring X^a phi^(6a) leaves exactly

    X^(2a)Psi^(21a)Y(chi)^3-Y(X+1)^a.

From Y-1 divisible by X^(L/2) and ord_phi chi=2, one obtains Y(chi)=1 modulo phi^L.
Also Y=1 modulo phi^L, and Psi^(21a)=1 modulo phi^(2a).
The remaining expression is therefore X^(2a)+(X+1)^a=phi^a modulo phi^a, as required.
Thus the full difference is divisible by U_0.
Its candidate remainder has degree14a+5L, strictly less than15a+5L, so it is the actual monic Euclidean remainder.
The q-th power of this division identity preserves both divisibility and the strict degree inequality, giving the original R exactly.

Only phi loses multiplicity, from7a to6a.
X retains a and every Y factor retains1; the additional order3 factor has exponent a.
All order groups are complete with uniform multiplicity.
The complementary B=(X+1)^a has degree a<2a and no X factor, whereas V_0 has exact X order a.
These statements prove the saturation, complement and parity assertions directly.

### Integer lifts, original multiplicities and zero Haar

The Laurent identity for the integer recurrence is verified by its initial values n=1,3 and the odd-index recursion with the minus sign.
Its mod2 recursion is precisely that of B_n, so mathcalB_n reduces to Y.
The three exact pullback identities are

    z[(z+z^(-1))-2]=(z-1)^2,
    z[(z+z^(-1))+1]=Phi_3(z),
    z^2 F_5(z+z^(-1))=Phi_5(z).

Together with the integer mathcalB_n identity they prove UC5--UC6, including monicity, every scalar and every original exponent.
All zeros of the reciprocal pullback lie on the unit circle.
The normalized circle mean of log|z-zeta| is0 for each such zeta: rotation reduces it to log(2|sin(t/2)|), whose mean follows from the integrable log-sine identity by the double-angle formula.
Finite additivity therefore gives mean0 for the logarithm of the pullback's absolute value.
On the circle its absolute value equals |G_star(z+z^(-1))|, and the real square in the Haar definition doubles that logarithm.
Consequently the asserted Haar integral is exactly0, including its integrable zeros.

Since n is coprime to5, the displayed lift contains no other five-order layer.
Its original a_0=6qa and all higher a_b=0 therefore give S_star=0 under the exact C199 definition.
Neither q nor any layer index has been reassigned.
The polynomial degrees are q(15a+5L) and q(14a+5L), and their difference is qa.
The reciprocal degrees are twice the trace degrees, proving the complete totient-weighted account in UC7; the endpoint contributes its doubled exponent2qa.

For T_star, multiplication by2 and by3 permutes each nonendpoint root group, since its orders divide5n and are coprime to6.
Both C_2 and C_3 fix the endpoint2, and every root group carries its fixed uniform multiplicity.
Thus T_star divides T_star(C_2) and T_star(C_3) over the algebraic closure.
Monic division has integer quotient and remainder, so both integer remainders are identically0 and theta_2(T_star)=theta_3(T_star)=0.
This verifies the stated failure of the nonzero original-quotient domain; the zero-Haar lift is never identified with the actual canonical G of an original residual solution.

### Both exact defects and the arbitrary-lift contradiction

All Y, Y(chi), X and Psi denominators are units at phi.
The complete rational unit is

    mathcalF=X^(-15a)Psi^(-147a)Y^6/Y(chi)^21.

Both Y factors are1 modulo phi^L, including the composed factor by the X-adic congruence already established.
Since X^3=1+(X+1)phi and Psi=1 modulo phi^2, the unit X^(-15)Psi^(-147) has linear term (X+1)phi modulo phi^2.
Its a-th power has first nonzero term (X+1)^a phi^a modulo phi^(2a).
The error discarded at depth L>=4a cannot cancel that term, and X+1 is a phi-unit.
Hence ord_phi(mathcalF-1)=a exactly.

Likewise X^a(X+1)^a=(1+phi)^a=1+phi^a gives V_0=1+phi^a modulo phi^L.
The full C_00^3 is X^(3a) modulo phi^(2a), which equals1+(X+1)^a phi^a at that precision.
Their sum therefore has first term X^a phi^a, with unit coefficient, and exact order a.
The unit group modulo phi^(3a) has order3*4^(3a-1), coprime to11, so its eleventh-power map is an automorphism and the required root class Z_0 exists uniquely.
Every representative remains a unit and preserves that exact order upon multiplication.
Changing representatives at depth3a alters the product only at depth4a.
With S_star=0 the full gate necessarily fails at the required depth4a, for every allowed root lift.

Finally let T be any monic integer lift of U_0^q.
Its entire reduction has X exponent A=qa>=8, phi exponent N=7qa>6A, and precisely every distinct irreducible factor of Y with exponent B_i=q>=2.
There are no unlisted factors and none of the Q_i equals X or phi.
The two coefficientwise residual divisibilities are exactly C197v3's two congruences modulo(4,T), with the same fixed sign.
Its arbitrary-monic statement imposes no irreducibility, total reality, nonzero quotient or original G hypothesis.
The complete QX13 rational function is exactly mathcalF^q, since the product over all irreducible Y factors contributes Y^(6q) in the numerator and Y(chi)^(21q) in the denominator.
Frobenius gives exact defect order qa, whereas QX14 requires at least4qa.
This strict contradiction applies to every lift and both signs, without using T_star as a residual solution.

### Accepted-input and source boundaries

The C608 input was used only for its displayed root definition, recurrence and matrix identities, all directly checked above.
Its finite32-row character certificate and J119 are not premises of this family.
C197v3 remains the accepted necessary theorem at its exact selected arbitrary-monic scope; its QX1--QX14 statement and argument were read, and the complete new application was checked.
The [historical R477 finding](Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) currently declares relationship unknown, as do its inherited R620/R622 context declarations.
This review does not relabel that history or claim a new independent whole review of C197, its degree corollary or its upstream source chain.

C199v4 supplies exact gate/layer definitions and their required precision at the recorded original domain.
The new formal comparison is inspected independently, while the [historical R489 v4 finding](Yin_R_G0489_v1.md#normalized-unit-v4-whole-chain-finding) retains its declared unknown relationship.
No claim is made that G_star or T_star meets C199's actual original residual hypotheses.
C609v2 is comparison only, and its parity conclusion is checked directly for the explicit family rather than used to infer a full gate.
There is no dependency cycle through the new C613 result.

The elementary root partitions, polynomial identities, integer pullbacks and Haar calculation require no unverified external assertion for this new proof.
No new primary-source inspection or recursive audit of accepted source proofs is claimed.
No numerical experiment, finite parameter scan or program is used as evidence, and no formal verification is claimed.
The result excludes the specified unbounded power-of-two normalized family; all other permitted even normalized supports, the actual original-Haar comparison and the unrestricted Task remain open at their existing responsible scopes.

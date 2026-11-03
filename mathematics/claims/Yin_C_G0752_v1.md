---
author: Yin
---

# Complete cyclotomic precision examples and a binary-source noncyclotomic degree bound

Human author Yin.
Root proposed separating complete cyclotomic products from the nonzero canonical G condition and the actual C748 binary source, checked the explicit-family integer CRT interface, and proposed the source-profile, positive-measure and full noncyclotomic-degree consequences.
Earlier_bit_obstruction constructed the explicit cyclotomic family, derived its actual canonical remainders and precision bounds, and derived and checked the exact dyadic trace-factor order mechanism, arbitrary cyclotomic trace-divisor bound and full-part endpoint argument below.
Both are contributors, not independent reviewers.
Root read the entire stable CY1--CY7 statement and proof, including the full remaining-degree argument.
This complete author theorem is initially open for fresh independent whole review.
The conclusions deliberately distinguish nonzero INTEGER G from nonzero BINARY G and do not identify a separately chosen synthetic cyclotomic polynomial with the canonical remainder.

The [selected G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
Provenance: project deduction from actual integer canonical remainders and the accepted cyclotomic and Mahler interfaces identified below.
The [D5 development](../drafts/Yin_D_G0005.md#cyclotomic-finite-precision-and-binary-source-obstruction) is provenance only; this fixed material includes the complete necessary proof and has no mutable-D dependency.

## Statement

### CY1. Reused inputs and the two distinct statements

A bounded reuse search inspected the current G Claims and D records for complete cyclotomic trace products, torsion canonical remainders and finite precision.
[C200](Yin_C_G0200_v1.md#statement) has a prime-cyclotomic comparison with all actual canonical values zero, while [C729 LC16--LC17](Yin_C_G0729_v1.md#fixed-degree-two-adic-cyclotomic-limit) has a cyclotomic limit with all six canonical polynomials zero.
Neither supplies the nonzero-G cyclotomic family below.
[C199v2 KC6/JT5--JT7](Yin_C_G0199_v2.md#decision-whole-reviewed-2026-10-20) supplies the exact cyclotomic reductions, odd-order identification and full trace multiplicities; only those algebraic interfaces are used, not its original nontorsion residual or zero-Haar hypotheses.
[Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) supplies the accepted cyclotomic integrality, factorization and irreducibility statements at its recorded source-inspection scope.
[Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) supplies the accepted measure-one characterization including products and multiplicities, as read on printed p322; its original proof is not newly audited here.
These adequate recorded inputs stop the reuse search; the new canonical calculations and source obstruction are proved below.

For every monic integer T and epsilon in{1,-1}, use its OWN actual canonical remainders

    a=rem_T T(C_2)/2, b=rem_T T(C_3)/3,
    c=rem_T T(C_5)/5,
    F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5),
    X_epsilon=rem_T(b^2-a^3+epsilon(c^3-2b^5)),
    C_2=X^2-2, C_3=X^3-3X,
    C_5=X^5-5X^3+5X,
    P_T(z)=z^(degT)T(z+z^(-1)).

All three prime divisions are performed on the actual integer remainders before any reduction.
Their integrality follows from C_p=X^p modulo p and monic division, as in adopted C736.
For a nonzero integer polynomial, v_2 denotes the minimum2-adic coefficient valuation.
Set v_2(0)=+infinity when stating divisibility lower bounds.

The first statement is an explicit family showing that actual G!=0 and arbitrarily large finite joint precision do NOT by themselves force a noncyclotomic factor.
For each integer j>=1, set f=X^2+X-1 and

    T_j=X^j f,
    P_(T_j)=(z^2+1)^j Phi_5(z).

Then P_(T_j) is completely cyclotomic, while its own system has

    b=0, v_2(a)>=floor(j/2), v_2(c)=j,
    G=2^(2j)c!=0, v_2(G)=3j,
    v_2(F)>=min(2j+1,5floor(j/2)),
    v_2(X_epsilon)>=3floor(j/2), epsilon=1,-1. (CY1)

In particular j=2N, N>=1, gives BOTH signs on the SAME polynomial with

    F=0 modulo2^(4N+1), X_1=X_(-1)=0 modulo2^(3N),
    G!=0, Gbar=0, degT_j=2N+2,
    degP_(T_j)=4N+4, m(P_(T_j))=0.             (CY2)

This does not realize the nonzero binary G of C748.

The exact cyclotomic factor alternative used for the second statement is also part of the theorem.
For ANY monic integer T whose reciprocal P_T is completely cyclotomic, put phi=X^2+X+1, let E=ord_phi Tbar>=1 and let a_T be its OWN actual dyadic divided remainder.
Then in the full phi^E component either a_Tbar=0, or

    ord_phi a_Tbar=2(E-w)<E
       for a power of2 w with w<=E<2w.         (CY12 statement)

All integer factor multiplicities and endpoint factors are allowed; CY3--CY4 prove this precise alternative.

The second statement applies to a different domain and does exclude a completely cyclotomic reciprocal polynomial.
Let A>=1 be any integer and let T be any monic integer polynomial with

    U=Tbar=X^A Y phi^(7A), phi=X^2+X+1,
    Y monic in F_2[X], gcd(Y,Xphi)=1,
    Y divides Y(lambda), lambda=X^3+X.         (CY3)

If its OWN X_epsilon is coefficientwise even for either sign, then P_T is not a product of cyclotomic polynomials.
It has a noncyclotomic irreducible factor and strictly positive logarithmic Mahler measure.
Moreover every monic INTEGER trace factor J of T whose own reciprocal P_J is completely cyclotomic satisfies ord_phi Jbar<=A.
The FULL noncyclotomic part of P_T consequently has degree at least24A, counting every remaining factor with multiplicity.
This degree bound concerns the whole remaining part, not each of its individual irreducible factors.
No F congruence, normalized K, actual common factor or explicit numerical source relation A=aq is required for this second statement.
The complete actual C746/C748 source satisfies CY3 and has its selected second residual even, so its complete reciprocal polynomial is noncyclotomic with m(P_T)>0.
This is strict positivity for each constructed polynomial, not a quantitative lower bound or a small-positive-measure conclusion.

## Complete argument

### CY2. Complete integer computation for the cyclotomic family

Put g=X^2-X-1, so the exact integer identities are

    f(C_2)=fg,
    f(C_3)=f*(X^4-X^3-4X^2+4X+1),
    C_5-2=(X-2)f^2.                            (CY4)

Since C_3 has an X factor, CY4 gives T_j|T_j(C_3) in Z[X], so b=0 exactly.
For the dyadic remainder define the actual degree<j polynomial

    h_j=rem_(X^j)((X^2-2)^j g).

Division of T_j(C_2)=f g(X^2-2)^j by T_j=X^j f leaves exactly f h_j, of degree<j+2, and therefore a=f h_j/2.
In (X^2-2)^j modulo X^j, only binomial indices0<=i<=floor((j-1)/2) can survive.
Every such term has coefficient divisible by2^(j-i), hence by2^(floor(j/2)+1).
Multiplication by the integer g and further truncation modulo X^j preserve that divisor.
Consequently h_j/2 is integral and a is divisible by2^floor(j/2), with no division in a binary quotient.

The ideals(X^j) and(f) are comaximal over Z[X]: X(X+1)=1 modulo f, hence X^j(X+1)^j=1 modulo f.
For c, the actual T_j remainder of T_j(C_5) is divisible by X^j because both the dividend and T_j are divisible by X^j.
After its legitimate integer division by5, c is still divisible by X^j.
Modulo f, CY4 gives C_5=2 and f(C_5)=5, so the integer identity defining c gives5c=5*2^j in the free Z-module Z[X]/(f).
Cancel5 there to get c=2^j modulo f.
Let L_j=rem_f((X+1)^j), an actual integer polynomial of degree<2.
The two congruences and degree<j+2 identify the exact polynomial

    c=2^j X^j L_j.                             (CY5)

Indeed X^j L_j=1 modulo f and the displayed candidate vanishes modulo X^j; the integer CRT and degree bound give equality with the own canonical remainder.
The reduction of L_j is a unit in F_2[X]/phi because X+1 is a unit there, so its coefficients are not all even.
Thus v_2(c)=j exactly and c is nonzero.

Both c^2-2^j c and c^3-2^(2j)c vanish modulo X^j and modulo f.
Integer comaximality makes them divisible by T_j, giving

    rem_(T_j)c^2=2^j c,
    G=rem_(T_j)c^3=2^(2j)c.                    (CY6)

Monic reduction preserves every coefficientwise power-of-two divisor.
The formula for a, CY5--CY6 and b=0 therefore give every bound in CY1, with the exact G valuation3j and both residual signs retained.
At j=2N the first bound is min(4N+1,5N)=4N+1 for N>=1, proving CY2.
The reciprocal identity follows directly from z^2 f(z+z^(-1))=z^4+z^3+z^2+z+1=Phi_5(z) and zX=z^2+1 under the trace substitution.
All reciprocal roots are therefore roots of unity and the logarithmic Mahler measure is zero.

Complete torsion does not mean complete forward stability for every C_p.
Here C_3 preserves the full trace divisor, while C_5 takes the primitive-fifth traces to2, which is absent from T_j, and C_2 takes the zero trace to-2, also absent.
The nonzero a and c arise from these actual missing targets; no field-value calculation replaces a polynomial remainder with multiplicity.

### CY3. Full integer cyclotomic trace factorization

Suppose P_T is a product of cyclotomic polynomials, with every actual multiplicity retained.
For n>2, define the monic integer trace polynomial F_n by

    z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z).

To justify the integer trace form, z^(-varphi(n)/2)Phi_n(z) is a symmetric integer Laurent polynomial; its pairs z^k+z^(-k)=C_k(X) and its constant term express it as an integer polynomial in X.
Its largest Laurent exponent proves the asserted degree and monicity.
Its roots are the complete inverse pairs of primitive n-th roots.
For n=1,2 the trace factors are X-2 and X+2, whose reciprocal lifts are(z-1)^2 and(z+1)^2.
Every zero of P_T at z=1 or z=-1 has even multiplicity, because X-2=(z-1)^2/z and X+2=(z+1)^2/z.
Therefore the complete cyclotomic factorization of P_T gives an exact integer factorization

    T=(X-2)^(e_1/2)(X+2)^(e_2/2)
                         product_(n>2) F_n^(e_n), (CY7)

where all exponents are nonnegative integers and e_1,e_2 are even.
Equality follows from the reciprocal identities and injectivity of the Laurent trace substitution, so no factor or shared multiplicity is lost.
No irreducibility of T is assumed.

The accepted full cyclotomic reduction is, for n odd,

    Phi_(2^b n)bar=Phi_nbar^(lambda_b),
    lambda_0=1, lambda_b=2^(b-1) for b>=1.

The roots of Phi_nbar have exact odd order n because z^n-1 is squarefree in characteristic2 and its full divisor partition retains all orders.
At a primitive fifth root z in characteristic2, the trace x=z+z^(-1) is a root of phi, and conversely the two roots of z^2+xz+1 for such x are primitive fifth roots.
Thus precisely the trace factors F_(2^b*5) in CY7 can contain phi after reduction; every other trace factor, including X-2 and X+2, is a unit at phi.
This uses complete odd-order reduction, not characteristic-zero separability in bad characteristic.

Write f=F_5=X^2+X-1 and g=F_10=X^2-X-1.
For b>=1 put lambda_b=2^(b-1) and V_b=F_(2^b*5).
The full primitive-root identities give

    V_b=g(C_(lambda_b)), V_bbar=phi^(lambda_b). (CY8)

Indeed z^(lambda_b) has order10 precisely when z has order2^b*5; the degrees and full inverse pairs identify the monic trace polynomials.
Here C_0=2, C_1=X and C_(n+1)=X C_n-C_(n-1), so C_n(z+z^(-1))=z^n+z^(-n).
These identities imply the integer commutation C_n(C_2)=C_2(C_n) and, for dyadic lambda_b, C_(lambda_b)bar=X^(lambda_b).

### CY4. Exact possible dyadic orders at the fifth-order component

The necessary ACTUAL dyadic calculations for the factors in CY8 are

    Delta(f)=-Xf, theta_2(f)=0,
    g(C_2)=g*(X^2+X-3)+2(1-X),
    theta_2(g)=1-X,
    theta_2(V_b)=1-C_(lambda_b).               (CY9)

The last identity follows by substituting C_(lambda_b) into the complete preceding integer division, using the commutation identity, and observing that the resulting remainder degree lambda_b is less than degV_b=2lambda_b.
Thus it is the actual divided remainder at V_b, including b=1, not a formal substitution into a quotient class.
If V_b(C_2)=V_b Q_b+2theta_2(V_b), monic division modulo2 gives Q_b=V_b modulo2.
Hence

    Delta(V_b)=V_b(Q_b-V_b)/2+theta_2(V_b)

is an identity of integer polynomials.
Since 1+X^(lambda_b) is a unit at phi, Delta(V_b)bar is a phi-unit for EVERY b>=1.
Indeed a root of phi has order3, while lambda_b is a power of2.
In contrast Delta(f)bar has exact phi-order1.

Separate the actual factorization CY7 as T=J D, where

    J=f^(m_0) product_(b>=1) V_b^(m_b),
    E=m_0+sum_(b>=1)m_b lambda_b>0,
    Jbar=phi^E,
    Dbar is a unit at phi.                     (CY10)

Every m_b is its actual nonnegative integer multiplicity; only finitely many are nonzero.
The exact integer product identity for Delta and its binary reduction are

    Delta(JD)=D(C_2)Delta(J)+J^2Delta(D),
    Delta(JD)bar=Dbar^2 Delta(J)bar
                                      +phi^(2E)Delta(D)bar.

In the full phi^E quotient, the second term vanishes and Dbar^2 is a unit.
Since the actual canonical a_T is rem_T Delta(T), its phi-order below E is precisely that of Delta(J)bar modulo phi^E.
Common factors elsewhere cause no cancellation or coprimality requirement in this calculation.

Repeated application of the same product identity gives

    Delta(J)bar=(m_0 mod2)phi^(2(E-1))Delta(f)bar
       +sum_(b>=1,m_b odd)
                    phi^(2(E-lambda_b))Delta(V_b)bar. (CY11)

Terms with zero multiplicity are omitted; the f term is present only when m_0 is odd, so all written exponents are nonnegative.
The f term has order2E-1>=E and vanishes modulo phi^E.
If there is no odd m_b with b>=1, the canonical a_T vanishes on this full component.
Otherwise let w be the largest lambda_b with m_b odd, distinct from the map lambda=X^3+X.
These weights are distinct powers of2 for b>=1.
If E>=2w, every surviving summand has order at least E and again a_Tbar=0 modulo phi^E.
If E<2w, then m_b=1 at the largest weight, and all smaller weights are at most w/2.
Their summands have order at least2E-w>=E, since E>=w.
The unique largest-weight summand has exact order2(E-w)<E by the phi-unit conclusion of CY9, so no other term can cancel it.
We have proved the exact alternative

    a_Tbar=0 modulo phi^E, OR
    ord_phi a_Tbar=2(E-w)<E
             for a power of2 w with w<=E<2w.    (CY12)

Every division used to obtain CY12 was an actual integer division before binary reduction.
The statement is in the full repeated phi^E component, with no passage to the reduced root set.

### CY5. The actual binary profile excludes complete torsion

Assume CY3 and X_epsilon(T)=0 modulo2, and suppose for contradiction that P_T is completely cyclotomic.
Use alpha=a_Tbar, beta=b_Tbar and gamma=c_Tbar in F_2[X]/U.
Since the odd divisions are already integral and their divisors3,5 are units modulo2,

    beta=[U(lambda)]=0,
    gamma=[U(chi)]
         =[phi^(2A)X^A Y(chi)phi(chi)^(7A)],
    chi=Xphi^2.                                (CY13)

The first zero follows from X|lambda, phi|phi(lambda) and the full Y-forward divisibility in CY3, including every repeated multiplicity.
At phi, both X and the factors Y(chi), phi(chi) are units because chi=0 modulo phi, Y(0)=1 and phi(0)=1.
Thus gamma has exact order2A, and gamma^3 has exact order6A<7A in the full component.
Both residual signs reduce to the same binary equation

    alpha^3=gamma^3 modulo phi^(7A).            (CY14)

If a class has exact phi-order t and its cube is nonzero modulo phi^(7A), that cube has exact order3t; this follows by writing the class as phi^t times a unit.
CY14 therefore forces alpha to have exact order2A, without any normalized K assumption or F congruence.
Apply CY12 with E=7A.
Its zero alternative is impossible, and its other alternative would require

    2A=2(7A-w), hence w=6A.                    (CY15)

But A>=1 is an integer, so6A has a factor3 and cannot be a power of2.
This contradiction proves that P_T is not completely cyclotomic.
The same binary profile also gives Gbar=gamma^3!=0 at phi automatically; it is stronger than the mere integer condition G!=0 used in CY1.

### CY6. Exact application and the remaining analytic boundary

For the complete C746/C748 inputs, write Y=Y_b^q and A=aq.
Their binary divisor is exactly X^A Y phi^(7A), Y is prime to Xphi and its full lambda-forward divisibility follows by raising the original Y_b divisibility to q.
Their selected second residual is divisible by8 or by the prescribed2^N, with N>=1.
Thus CY5 applies to every actual constructed representative, even though the common factor in C749 makes the complete product reducible.
The source factors, originally chosen q, full degrees and every previous construction expense remain unchanged.
This deduction requires no further lifting, factor deletion, synthetic residual choice or new numerical estimate.

The reciprocal P_T is monic integral with constant coefficient1.
If its logarithmic Mahler measure were zero, the accepted Kronecker characterization would make it a product of cyclotomic polynomials and a monomial, with multiplicities retained.
The nonzero constant coefficient excludes a nonconstant monomial, contradicting CY5.
Because a monic polynomial has nonnegative logarithmic Mahler measure, it follows that m(P_T)>0 and at least one of its irreducible integer factors is noncyclotomic.
This invokes exactly the measure-one scope recorded in Smy08-U001, not an uninspected uniform lower bound.

No claim is made that an arbitrary nonzero binary G and finite residual precision outside CY3 force a noncyclotomic factor.
That broader implication remains unclassified here.
The explicit all-cyclotomic family CY1 has Gbar=0 and belongs to a different binary profile, so it does not conflict with the source obstruction.
Nor is any irreducible noncyclotomic factor asserted to inherit the original residual precision; adopted C749 retains the concrete failure for its specified core.
Strict positivity supplies neither a degree-independent gap nor a sequence whose positive measures tend to zero.
The unrestricted Lehmer objective, compatible characteristic-zero residual realization and quantitative measure control remain unresolved.

### CY7. Arbitrary cyclotomic trace divisors and the full remaining degree

Retain CY3 and the actual second-residual evenness, which already give ord_phi a_Tbar=2A by CY13--CY14.
Let J be ANY monic integer factor of T whose reciprocal P_J is completely cyclotomic, and write the actual monic integer quotient T=J D.
Define

    E_c=ord_phi Jbar, E_r=ord_phi Dbar,
    E_c+E_r=7A.                                (CY16)

No integer or binary coprimality of J and D is required.
The case E_c<=A is already the desired conclusion, so suppose E_c>A and in particular E_c>0.
Apply the complete cyclotomic trace classification in equations CY7--CY10 to J itself, and write J=J_5 Q with J_5bar=phi^(E_c) and Qbar a phi-unit.
The m_b and lambda_b below are the actual multiplicities and weights of J_5, not those of the full T.
The exact product identity and CY11 give the full binary polynomial identity

    Delta(J)bar=Qbar^2 [
          (m_0 mod2)phi^(2(E_c-1))Delta(f)bar
          +sum_(b>=1,m_b odd)
                phi^(2(E_c-lambda_b))Delta(V_b)bar]
                    +phi^(2E_c)Delta(Q)bar.    (CY17)

It is important here to keep the last term instead of only using CY12 modulo phi^(E_c).
Let Dbar=phi^(E_r)d_0 with d_0 a phi-unit.
In the actual product rule

    Delta(T)bar=Dbar^2 Delta(J)bar
                                      +Jbar^2 Delta(D)bar,

the f term from the first summand has order14A-1 when present, and its Delta(Q) term has order at least14A.
Each odd m_b with b>=1 contributes in that first summand an exact order

    14A-2lambda_b,                             (CY18)

because d_0, Qbar and Delta(V_b)bar are phi-units.
The second summand Jbar^2 Delta(D)bar has order at least2E_c>2A.
If no odd m_b with b>=1 occurs, both complete summands have order greater than2A, contradicting the known a_Tbar order.
Otherwise let w be the largest lambda_b with m_b odd.
The weights are distinct, so its term has the uniquely smallest order14A-2w among CY18, and that order is below14A-1.
Thus it cannot cancel with another contribution inside Dbar^2 Delta(J)bar.

If14A-2w>2A, both complete summands again have order greater than2A.
Equality would force w=6A, impossible for a power of2.
If14A-2w<2A, then w>6A, and E_c>=w because J contains that actual factor at least once.
The second summand then has order at least2E_c>=2w, which is greater than14A-2w since w>6A.
It therefore cannot cancel the first summand's uniquely lowest term, leaving an order strictly below2A, also impossible.
Subtraction of a multiple of Tbar cannot create a term at order2A from higher orders or cancel a unique lower term, because2A<7A.
This proves

    ord_phi Jbar=E_c<=A                        (CY19)

for every stated cyclotomic TRACE factor J.

To apply CY19 to the full cyclotomic part of P_T, take every cyclotomic irreducible factor with its full actual multiplicity and call their product P_cyc.
Every multiplicity at z=1 and z=-1 is even, as proved in CY3, because the full product comes from the trace T; the full cyclotomic part includes those entire multiplicities.
Consequently the factorization in equation CY7 constructs a monic integer J with P_J=P_cyc.
The quotient P_rem=P_T/P_cyc is monic integral, reciprocal, has constant coefficient1 and has even degree.
The symmetric integer Laurent argument of CY3 gives its monic integer trace polynomial D with P_D=P_rem.
Multiplicativity and injectivity of the trace substitution give T=J D over Z, so this J lies in the precise domain of CY19.
Every irreducible factor of P_rem is noncyclotomic, by the choice of the full P_cyc.
Since E_r=7A-E_c>=6A and phi has degree2,

    degD>=2E_r>=12A,
    degP_rem=2degD>=24A.                       (CY20)

This retains all noncyclotomic factors and their multiplicities.
An arbitrary naked cyclotomic divisor of P_T need not itself have even endpoint multiplicities and need not be a trace lift; CY19 is not stated for such a divisor without that hypothesis.
The FULL cyclotomic part does meet it, by the preceding endpoint argument.
Neither CY19 nor CY20 asserts a residual congruence for J, D or an individual irreducible factor, and neither supplies a quantitative Mahler bound.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision cyclotomic-precision-binary-degree-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:27 |
| status | open |
| reason | Register the complete CY1--CY7 theorem with its distinct domains. The exact all-cyclotomic family T_j=X^j(X^2+X-1) has both-sign arbitrarily large finite residual precision and nonzero actual G with Gbar=0. The exact CY12 alternative for every completely cyclotomic reciprocal input retains actual dyadic factor multiplicities and endpoints. For the separate binary source Tbar=X^A Y phi^(7A), A>=1, Y prime to Xphi and fully lambda-forward, own second-residual evenness forces a noncyclotomic reciprocal factor and strictly positive Mahler measure, without an F or normalized-K premise. Every monic integer cyclotomic TRACE factor has phi-multiplicity at most A, and the FULL noncyclotomic reciprocal part has degree at least24A. All actual integer CRT/prime divisions, other-order cofactor terms, no-cancellation cases, endpoint trace-lift restrictions and source-inspection limits are retained. The C746/C748 application keeps all originally paid source/q/degree costs. Root and Earlier_bit_obstruction are contributors; fresh independent whole review remains outstanding. No generic implication from arbitrary Gbar, per-factor degree or precision inheritance, quantitative Mahler estimate, small-positive-measure sequence, compatible infinite realization or unrestricted G0001 completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete distinct statements and exact order alternative](#statement) | CY1--CY3, the explicitly stated CY12 alternative and all included CY6--CY7 conclusions: complete cyclotomic actual-G counterexample for every j and N/both signs, exact fifth-order dyadic valuation alternative for arbitrary cyclotomic trace products, minimal same-binary source obstruction, m(P)>0, every cyclotomic trace-divisor phi bound and full noncyclotomic reciprocal degree>=24A, with all full-part/source/unknown-generic and analytic limits. |
| argument | [Complete actual remainder and cyclotomic-factor proof](#complete-argument) | Entire CY2--CY7 and CY4--CY20: integer f/g compositions and CRT, genuine canonical halves and odd divisions, exact c/G and residual bounds, full cyclotomic trace decomposition including endpoint multiplicities, exact dyadic divided remainders and Delta factors, unique largest-weight alternative, CY15 contradiction, complete CY17 cofactor terms and all no-cancel cases, full remaining-part trace lift, degree24A and source/measure application. |
| dependency | [Adopted exact canonical integer interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 actual monic prime divisions, integral Delta and exact product rule, including common/repeated factors. The current actual identities and their source domains are written and checked in CY2--CY4/CY7; no automatic factor precision or unit compatibility is imported. |
| dependency | [Adopted full cyclotomic reductions and trace multiplicities](Yin_C_G0199_v2.md#decision-whole-reviewed-2026-10-20) | KC6 and JT5--JT7 exact reductions Phi_(2^b n)bar=Phi_nbar^(lambda_b), full odd-order root partition and trace multiplicity/endpoint conventions. Only these algebraic identities are consumed in CY3; the original theorem's nontorsion residual/zero-Haar hypotheses and conclusions are not asserted for the new inputs. |
| dependency | [Accepted cyclotomic polynomial source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Exact monic integral cyclotomic polynomial, divisor-factorization and irreducibility interfaces read at the U's actual page3/pages6--7 scope. The recorded original-proof limits remain; no new whole-source audit is claimed. CY3 gives the required integer trace decomposition and endpoint handling. |
| dependency | [Accepted product-form Kronecker characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | The height-normalization section's printed p322 measure-one characterization for integer polynomials as a monomial times a product of cyclotomic polynomials with multiplicities. Applied only to monic P_T with constant1 after CY5, to deduce strict m(P_T)>0. The U's recorded source-proof inspection limits are retained; no quantitative lower bound is invoked. |
| dependency | [Adopted actual parameterized BOTH8 source](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25) | GS0 exact binary profile, full Y_b lambda-forward divisibility and actual second residual divisible by8, with unchanged original q/source/degree expenses. Used for the actual source application of the independently proved CY3 domain; no normalized K or common-factor condition is required by the new obstruction. |
| dependency | [Adopted every-finite-precision actual construction](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25) | GA1--GA4/GA18 preserve the same binary profile and own second-residual evenness on each separately constructed finite-precision polynomial. CY6 supplies positivity and CY7 the full noncyclotomic degree consequence while keeping every original source/q/degree/root cost. No fixed polynomial is extended, factor deleted or compatible infinite sequence assumed. |
| support | [Adopted forced-factor precision-loss comparison](Yin_C_G0749_v1.md#decision-whole-reviewed-2026-10-25) | CF1--CF7 supply only the explicitly cited comparison that the complete constructed product may be reducible and its specified smaller core loses canonical precision. None of its structural formulas is a premise of CY3/CY12/CY19; the new theorem does not grant residual inheritance to the noncyclotomic factors. |
| support | [Adopted prime-cyclotomic zero-canonical comparison](Yin_C_G0200_v1.md#statement) | Reuse comparison only: the displayed prime-cyclotomic family has all actual canonical values zero. Its energy/Haar theorem is not an input to the new family or obstruction. |
| support | [Adopted cyclotomic limit comparison](Yin_C_G0729_v1.md#fixed-degree-two-adic-cyclotomic-limit) | LC16--LC17 comparison only: the cyclotomic limit has all six canonical polynomials zero, while its finite nonzero-G family has zero binary G. No Salem, irreducibility, limit or height conclusion is consumed in the new theorem. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:35 |
| status | proved |
| reason | Register the complete CY1--CY7 theorem with its distinct domains. The exact all-cyclotomic family T_j=X^j(X^2+X-1) has both-sign arbitrarily large finite residual precision and nonzero actual G with Gbar=0. The exact CY12 alternative for every completely cyclotomic reciprocal input retains actual dyadic factor multiplicities and endpoints. For the separate binary source Tbar=X^A Y phi^(7A), A>=1, Y prime to Xphi and fully lambda-forward, own second-residual evenness forces a noncyclotomic reciprocal factor and strictly positive Mahler measure, without an F or normalized-K premise. Every monic integer cyclotomic TRACE factor has phi-multiplicity at most A, and the FULL noncyclotomic reciprocal part has degree at least24A. All actual integer CRT/prime divisions, other-order cofactor terms, no-cancellation cases, endpoint trace-lift restrictions and source-inspection limits are retained. The C746/C748 application keeps all originally paid source/q/degree costs. Adopt fresh isolated whole R972 after root read the entire CY1--CY7 argument, fixed statement and exact source scopes, then the complete independent finding. Root and Earlier_bit_obstruction remain contributors. The two explicit quotient-product multiplication signs are meaning-preserving notation clarifications, actually reread by the reviewer; no substantive repair was contributed. Every whole-proof domain and stated source limit passed. No generic implication from arbitrary Gbar, per-factor degree or precision inheritance, quantitative Mahler estimate, small-positive-measure sequence, compatible infinite realization or unrestricted G0001 completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete distinct statements and exact order alternative](#statement) | CY1--CY3, the explicitly stated CY12 alternative and all included CY6--CY7 conclusions: complete cyclotomic actual-G counterexample for every j and N/both signs, exact fifth-order dyadic valuation alternative for arbitrary cyclotomic trace products, minimal same-binary source obstruction, m(P)>0, every cyclotomic trace-divisor phi bound and full noncyclotomic reciprocal degree>=24A, with all full-part/source/unknown-generic and analytic limits. |
| argument | [Complete actual remainder and cyclotomic-factor proof](#complete-argument) | Entire CY2--CY7 and CY4--CY20: integer f/g compositions and CRT, genuine canonical halves and odd divisions, exact c/G and residual bounds, full cyclotomic trace decomposition including endpoint multiplicities, exact dyadic divided remainders and Delta factors, unique largest-weight alternative, CY15 contradiction, complete CY17 cofactor terms and all no-cancel cases, full remaining-part trace lift, degree24A and source/measure application. |
| dependency | [Adopted exact canonical integer interface](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 actual monic prime divisions, integral Delta and exact product rule, including common/repeated factors. The current actual identities and their source domains are written and checked in CY2--CY4/CY7; no automatic factor precision or unit compatibility is imported. |
| dependency | [Adopted full cyclotomic reductions and trace multiplicities](Yin_C_G0199_v2.md#decision-whole-reviewed-2026-10-20) | KC6 and JT5--JT7 exact reductions Phi_(2^b n)bar=Phi_nbar^(lambda_b), full odd-order root partition and trace multiplicity/endpoint conventions. Only these algebraic identities are consumed in CY3; the original theorem's nontorsion residual/zero-Haar hypotheses and conclusions are not asserted for the new inputs. |
| dependency | [Accepted cyclotomic polynomial source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Exact monic integral cyclotomic polynomial, divisor-factorization and irreducibility interfaces read at the U's actual page3/pages6--7 scope. The recorded original-proof limits remain; no new whole-source audit is claimed. CY3 gives the required integer trace decomposition and endpoint handling. |
| dependency | [Accepted product-form Kronecker characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | The height-normalization section's printed p322 measure-one characterization for integer polynomials as a monomial times a product of cyclotomic polynomials with multiplicities. Applied only to monic P_T with constant1 after CY5, to deduce strict m(P_T)>0. The U's recorded source-proof inspection limits are retained; no quantitative lower bound is invoked. |
| dependency | [Adopted actual parameterized BOTH8 source](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25) | GS0 exact binary profile, full Y_b lambda-forward divisibility and actual second residual divisible by8, with unchanged original q/source/degree expenses. Used for the actual source application of the independently proved CY3 domain; no normalized K or common-factor condition is required by the new obstruction. |
| dependency | [Adopted every-finite-precision actual construction](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25) | GA1--GA4/GA18 preserve the same binary profile and own second-residual evenness on each separately constructed finite-precision polynomial. CY6 supplies positivity and CY7 the full noncyclotomic degree consequence while keeping every original source/q/degree/root cost. No fixed polynomial is extended, factor deleted or compatible infinite sequence assumed. |
| support | [Adopted forced-factor precision-loss comparison](Yin_C_G0749_v1.md#decision-whole-reviewed-2026-10-25) | CF1--CF7 supply only the explicitly cited comparison that the complete constructed product may be reducible and its specified smaller core loses canonical precision. None of its structural formulas is a premise of CY3/CY12/CY19; the new theorem does not grant residual inheritance to the noncyclotomic factors. |
| support | [Adopted prime-cyclotomic zero-canonical comparison](Yin_C_G0200_v1.md#statement) | Reuse comparison only: the displayed prime-cyclotomic family has all actual canonical values zero. Its energy/Haar theorem is not an input to the new family or obstruction. |
| support | [Adopted cyclotomic limit comparison](Yin_C_G0729_v1.md#fixed-degree-two-adic-cyclotomic-limit) | LC16--LC17 comparison only: the cyclotomic limit has all six canonical polynomials zero, while its finite nonzero-G family has zero binary G. No Salem, irreducibility, limit or height conclusion is consumed in the new theorem. |
| review | [Fresh independent whole cyclotomic precision and remaining-degree review](../audits/reviews/Yin_R_G0972_v1.md#whole-cyclotomic-precision-degree-finding) | Entire fixed statement and CY2--CY7 proof, explicit CY12 alternative, CY4--CY20, actual all-cyclotomic family, exact source obstruction, accepted Kronecker use, all trace-divisor and full noncyclotomic degree conclusions, with exact bindings, independently reviewed relationship and preserved input/source limitations. |


---
author: Yin
---
# An unbounded normalized support family with exact canonical controls and a failed unit gate

Human author Yin.
The same_trace contributor derived the complete UC1--UC7 construction and all-lift exclusion under the [current all-strategy continuation](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
The [D1 author section](../drafts/Yin_D_G0001.md#remaining-normalized-uniform-control) is extraction provenance, not a logical input.
The question is whether the remaining normalized A_0>=4 range is controlled by derivative, endpoint parity, complete support and canonical C3/C5 identities alone.
The construction answers that proposed weakening negatively on an unbounded exact family, while the full C197 unit condition excludes every monic integer lift of each specified whole reduction.
This is not a next-multiplicity cutoff, an order scan, a numerical example or an inference of global Frobenius normalization from a local jet.
The reuse check inspected C197v3, C199v4/v5, C609v2 and C601's earlier finite controls and conditional multiplicity-two closure.
The earlier fixed scopes remain unchanged; this construction explicitly supplies its whole family, integer lift expense and unresolved actual-input boundary.
The material is open pending separate whole mathematical review.

## Statement


For every integer s>=2 set A_0=2^s, let k be the least even integer with k>=s+2, and set

    L=2^k in{4A_0,8A_0}, n=1+10L,
    phi=X^2+X+1, tau=X^3+X,
    chi=Xphi^2, Psi=phi(chi).

Let Y=B_n in F_2[X] be the squarefree monic polynomial of ALL nonidentity n-th-root traces, one trace per inverse pair, as in C608/C609.
Since k is even, gcd(n,15)=1.
The complete support factors of Y have exponents1, and none is X, phi or X+1.
Define

    H_0=X^(A_0)Y,
    U_0=X^(A_0)phi^(7A_0)Y,
    B=(X+1)^(A_0),
    R_0=X^(A_0)phi^(6A_0)Y B,
    V_0=H_0B,
    C_00=X^(A_0)Y(chi)Psi^(7A_0).              (UC1)

Then ALL of the following are exact assertions about these same polynomials:

    U_0 divides U_0(tau),
    R_0=rem_(U_0)(U_0(chi)^3),
    phi is the only unsaturated factor of U_0 in R_0,
    deg U_0=15A_0+5L, deg R_0=14A_0+5L,
    deg B=A_0<2A_0,
    ord_X V_0=A_0 even, ord_X B=0 even,
    phi^L divides V_0', X^(L/2) divides Y',
    U_0,R_0,V_0 are NOT squares.                (UC2)

Both tau and chi preserve the entire geometric U_0 support.
Every factor of R_0 occurs in a COMPLETE odd-order group with uniform multiplicity; in addition to Y's complete groups, its order-one, order-five and order-three exponents are respectively A_0,6A_0,A_0.
Thus this family has the actual canonical remainder, complete support, global nonsquareness and the stronger derivative order L>=4A_0 required by the old normalized necessary interface.
The conclusion is not that it satisfies that entire interface.
Indeed its same-polynomial rational unit and full zero-correction gate defects have the EXACT orders

    ord_phi(H_0^6/C_00^21-1)=A_0,
    ord_phi(V_0+C_00^3)=A_0.                    (UC3)

The full required precision is4A_0, so both conditions fail for every member of the unbounded family.
The derivative, parity, complete support and exact remainder controls in (UC2) therefore cannot replace the full normalized unit condition.

For every original q=2^t with t>=1, set U=U_0^q and R=R_0^q.
Their maximal common Frobenius power is EXACTLY q, their original X exponent is A=qA_0 and all extra support exponents are q>=2.
There is NO monic integer polynomial T with T mod2=U for which both canonical residuals

    rem_T(2theta_5(T)^2-3theta_2(T)^5),
    rem_T(theta_3(T)^2-theta_2(T)^3
                         +epsilon(theta_5(T)^3-2theta_3(T)^5))

have all coefficients divisible by4, for either epsilon in{1,-1}, where theta_p(T)=rem_T(T(C_p))/p uses the actual monic integer remainders and C_p(z+z^(-1))=z^p+z^(-p).
This is an all-lift exclusion of the specified whole reduction, not a finite search over its coefficient bits.
The full unrestricted set of even A_0>=4 supports remains outside this exclusion.

## Argument

### Exact recurrence depth, complete groups and global normalization

For the recurrence matrix M_0=[[X,1],[1,0]], the polynomial identities already used in C608 are

    M_0^5-I=phi[phi M_0+(X+1)I],
    M_0^2-I=XM_0.

Raising the first to L gives M_0^(5L)=I modulo phi^L.
Raising the second to L/2 gives M_0^L=I modulo X^(L/2), and hence M_0^(5L)=I modulo X^(L/2).
Since n=1+10L, the recurrence's initial vector (B_3,B_1) is shifted by5L steps.
It follows that

    Y=1 modulo phi^L,
    Y=1 modulo X^(L/2).                        (UC4)

This is an exact all-s identity, not an inference from sampled values of n.
The nonidentity n-th roots are distinct because n is odd, and their inverse-pair traces are distinct by the quadratic trace identity.
Thus Y is squarefree of degree(n-1)/2=5L and Y' is nonzero.
Its factors are precisely the complete primitive groups whose orders divide n and exceed1, each once.
As gcd(n,15)=1, none is of order1,3 or5.
The same coprimality implies Y divides Y(tau) and Y divides Y(chi), by the permutations z->z^3 and z->z^5 of these whole root sets.
Because L and L/2 are even, differentiating (UC4) preserves both displayed moduli.

The powers multiplying Y in U_0,R_0,V_0 all have even exponents.
Consequently each has nonzero derivative equal to that multiplier times Y', so each is globally nonsquare.
Equivalently every irreducible Y factor occurs with exponent exactly1, disjoint from X,phi,X+1.
After raising to q, those exact exponents are q and all remaining exponents are multiples of q.
This proves the maximal common Frobenius power is exactly q from the FULL factor multiplicities, with no reliance on a finite local jet.

### Actual whole canonical remainder and every component

The identities tau=X(X+1)^2 and phi(tau)=phi(X)(X^4+X^3+1), together with Y|Y(tau), show U_0|U_0(tau).
Both tau and chi also preserve the full U_0 root set: they permute Y's complete groups, tau permutes the order-five traces, chi sends them to the order-one trace0, and both fix0.

The candidate R_0 in (UC1) has degree14A_0+5L strictly below15A_0+5L=deg U_0.
It suffices to check U_0(chi)^3-R_0 modulo the pairwise coprime factors X^(A_0), phi^(7A_0) and Y.
At X, the first term has order3A_0 and R_0 has order A_0.
At every Y factor, Y|Y(chi) makes the first term divisible by Y^3 and the second is divisible by Y.
No factor or separate primary component is omitted.

At phi, use (UC4), ord_phi chi=2 and L>=4A_0 to obtain Y=Y(chi)=1 modulo phi^(A_0).
Since A_0 is a power of2 and Psi=1+Xphi^2+X^2phi^4, one has Psi^(21A_0)=1 modulo phi^(2A_0).
After factoring X^(A_0)phi^(6A_0), the remaining difference is

    X^(2A_0)Psi^(21A_0)Y(chi)^3-Y(X+1)^(A_0).

Modulo phi^(A_0), this is X^(2A_0)+(X+1)^(A_0)=phi^(A_0), hence zero.
The whole difference is therefore divisible by phi^(7A_0), establishing the exact canonical remainder in (UC2).
The same identity also proves R=rem_U(U(chi)^3) after raising to q: the remainder degree remains below deg U and Frobenius preserves the divisibility.
The asserted saturation, complete R groups and all degree identities now follow from the explicit disjoint factors in (UC1).

### Complete integer cyclotomic lifts and original degree expense

Let mathcalB_n in Z[X] be given by mathcalB_1=1, mathcalB_3=X+1 and mathcalB_(m+2)=X mathcalB_m-mathcalB_(m-2) for odd m>=3.
Its exact Laurent identity is

    z^((n-1)/2) mathcalB_n(z+z^(-1))=(z^n-1)/(z-1).

The recurrence verifies that identity directly, and reduction modulo2 gives mathcalB_n mod2=Y.
Let F_5=X^2+X-1, the integer order-five trace factor.
For the same original q define the two explicit monic integer polynomials

    T_star=[(X-2)^(A_0) F_5^(7A_0) mathcalB_n]^q,
    G_star=[(X-2)^(A_0)(X+1)^(A_0)
                                  F_5^(6A_0) mathcalB_n]^q. (UC5)

They reduce to U and R respectively.
All trace roots of G_star lie on the unit-circle trace interval and its pullback is the COMPLETE cyclotomic product

    z^(deg G_star)G_star(z+z^(-1))
      =(z-1)^(2qA_0) Phi_3(z)^(qA_0)
          Phi_5(z)^(6qA_0)[(z^n-1)/(z-1)]^q.  (UC6)

It is therefore a genuine integer zero-Haar lift of the reduction R, with every factor and integer exponent supplied.
It is NOT asserted to equal the actual canonical G(T_star), or the G of any original residual input.
Its only original five-order layer is a_0=6qA_0 at order5, with all higher a_b zero, so its normalized correction S_star is exactly0.
No layer is freely reassigned after the comparison.

The degree accounts are

    r_form=deg T_star=q(15A_0+5L),
    w_form=deg G_star=q(14A_0+5L),
    r_form-w_form=qA_0,
    sum_m a_m phi_Euler(m)=2w_form.             (UC7)

There is no missing scalar, omitted cyclotomic group or rescaled original degree.
The integral T_star itself has theta_2(T_star)=theta_3(T_star)=0: the maps C_2 and C_3 permute each nonendpoint whole root group with its fixed multiplicity and fix2, so T_star divides both compositions over Z[X].
It is a reducible cyclotomic support lift, not an original nonzero-quotient or nontorsion input.

### Exact full-gate failure and exclusion of every integer lift

Put mathcalF=H_0^6/C_00^21 in F_2(X) localized at phi.
All denominators below are units there.
The full definitions give

    mathcalF=X^(-15A_0)Psi^(-147A_0)
                                  Y^6/Y(chi)^21.

Equation (UC4) gives Y=Y(chi)=1 modulo phi^L, so mathcalF=(X^(-15)Psi^(-147))^(A_0) modulo phi^L.
The exact identity X^3=1+(X+1)phi and Psi=1 modulo phi^2 give

    X^(-15)Psi^(-147)=1+(X+1)phi modulo phi^2.

Frobenius at the power A_0 and L>A_0 prove ord_phi(mathcalF-1)=A_0, the first assertion of (UC3).
This is the actual full-support rational function from C197 QX13, not a function with the extra Y factors dropped.

For the second defect, (UC4) and the power-of-two identities give

    V_0=1+phi^(A_0) modulo phi^L,
    C_00^3=X^(3A_0) modulo phi^(2A_0)
           =1+(X+1)^(A_0)phi^(A_0) modulo phi^(2A_0).

Hence

    V_0+C_00^3=X^(A_0)phi^(A_0) modulo phi^(2A_0),

whose leading coefficient is a phi-unit.
Its exact order is A_0.
For the prescribed complete G_star layers S_star=0, every allowed unit root Z_0 leaves the full gate Z_0(V_0+C_00^3) with that same order A_0, below4A_0.
Thus no choice of a higher coefficient of a unit root can repair the failure.

Finally consider ANY monic integer T with reduction U=U_0^q and q>=2.
Its whole support matches C197v3 with original X exponent A=qA_0, original phi exponent7A and every extra factor exponent q>=2.
If both canonical residuals were zero modulo4, the [C197v3 QX13--QX14 necessity](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) would require its same full-support rational unit to be1 modulo phi^(4qA_0).
That rational unit is exactly mathcalF^q, and its defect has order qA_0 by (UC3) and Frobenius.
This contradiction proves the all-lift exclusion for both signs, without a coefficient scan, original-root realization or actual-G assumption.

The construction therefore supplies both an explicit countercontrol to replacing the full gate by its weaker canonical/derivative/parity screens and an actual parameter-uniform excluded class of all monic integer lifts in the remaining normalized range.
It does not show that every even A_0>=4 support has this defect, that another full-gate seed exists, or that the full original comparison is resolved.

## Exact inputs and review boundary

| Input | Actual use and limit |
| --- | --- |
| [C608 whole-trace recurrence and period proof](Yin_C_G0608_v1.md#argument) | Exact definition of B_n, complete root partition, recurrence and polynomial matrix identities. The new parameter-uniform depths and all canonical identities are proved here, with no finite certificate premise. |
| [C197v3 arbitrary-monic whole-support statement](Yin_C_G0197_v3.md#statement) | The all-lift exclusion matches its original A=qA_0, N=7qA_0 and every extra multiplicity q>=2, with both canonical residuals divisible by4 as the contradicted hypothesis. |
| [C197v3 exact rational-unit necessity](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | QX13--QX14 supplies the full rational function including every extra factor and its necessary order4qA_0 for either sign. No original irreducibility or characteristic-zero realization is added to that arbitrary-monic interface. |
| [C199v4 normalized gate and original layers](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Definition and required precision of the complete normalized gate and S_star. The explicit supplied integer G_star has only the actual low order5 layer, hence S_star=0; it is not assumed to be the original canonical G. |
| [C609v2 endpoint/complement parity](Yin_C_G0609_v2.md#statement) | Comparison only: the constructed even endpoint and complement orders are calculated directly, and do not imply the full gate or a global square. |

Every introduced polynomial is explicit in the parameters s and q, with the least admissible even k fixed rather than searched.
The proof retains all components of the canonical remainder, exact integer multiplicities, complete degree costs and the actual global maximum q.
The class exclusion is obtained from a checked fixed necessary theorem after computing its actual complete input, not by pretending the formal lift is an original residual solution.
The exact original-Haar comparison and arbitrary other even normalized multiplicities remain open.
No mathematical program or numerical computation was used, and no J allocation is needed for this analytic argument.
A separate reviewer must inspect the full family, both recurrence moduli, root closures, every primary remainder component, integer lifts, exact defect orders and the arbitrary-monic C197 application.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:42 |
| status | open |
| reason | Register the complete unbounded A_0=2^s>=4 support construction, exact canonical C3/C5 and complete cyclotomic controls, derivative/parity/global-Frobenius properties and integer degree expense. Its actual full unit defects have orderA_0, and C197 excludes every monic integer lift of each original whole reduction for every original power q=2^t>=2. The candidate awaits isolated whole review; it does not exclude all remaining supports or complete G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete family and all-lift assertion](#statement) | Every s>=2, deterministic minimal evenk, both normalized control identities and their full failure, arbitrary original q=2^t>=2, complete integer lifts and degrees, and no monic integer T of the specified reduction satisfying both residuals modulo4. |
| argument | [Complete analytic proof](#argument) | All recurrence, whole-root, primary-component, factor-multiplicity, actual normalization, integer lift and degree steps, exact normalized/original defect orders and the full C197 implication. |
| dependency | [Whole-trace polynomial interface](Yin_C_G0608_v1.md#argument) | B_n definition, root partition, recurrence and polynomial matrix identities used for the exact unbounded parameter construction. |
| dependency | [Arbitrary-monic full-support theorem](Yin_C_G0197_v3.md#statement) | Precisely matched original X/phi/extra multiplicities and the complete both-sign canonical mod4 hypothesis used in the final contradiction. |
| dependency | [Actual whole-unit lower order](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | QX13--QX14 on that entire support; all factors remain in mathcalF^q and its order is calculated exactly. |
| support | [Normalized gate and original layer definitions](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Exact formal comparison and S_star=0 from the supplied full low-layer integer lift, without asserting original residual realization. |
| support | [Earlier general parity boundary](Yin_C_G0609_v2.md#statement) | The precise weaker endpoint/complement parity condition satisfied by the construction, not a source of an inferred full gate. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:57 |
| status | proved |
| reason | Adopt the entire parameter-uniform complete-support construction and all-lift exclusion after reading its fixed proof and the independent whole R816 finding. Every original q, every canonical component, complete integer lift and exact unit-defect order is retained. The accepted C197 necessity is applied at its actual arbitrary-monic scope; historical unknown review relationships are preserved. This excludes the specified unbounded family, not all remaining A_0>=4 supports or the original G0001 contract. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete family and all-lift assertion](#statement) | Every s>=2, deterministic minimal evenk, both normalized control identities and their full failure, arbitrary original q=2^t>=2, complete integer lifts and degrees, and no monic integer T of the specified reduction satisfying both residuals modulo4. |
| argument | [Complete analytic proof](#argument) | All recurrence, whole-root, primary-component, factor-multiplicity, actual normalization, integer lift and degree steps, exact normalized/original defect orders and the full C197 implication. |
| dependency | [Whole-trace polynomial interface](Yin_C_G0608_v1.md#argument) | B_n definition, root partition, recurrence and polynomial matrix identities used for the exact unbounded parameter construction. |
| dependency | [Arbitrary-monic full-support theorem](Yin_C_G0197_v3.md#statement) | Precisely matched original X/phi/extra multiplicities and the complete both-sign canonical mod4 hypothesis used in the final contradiction. |
| dependency | [Actual whole-unit lower order](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | QX13--QX14 on that entire support; all factors remain in mathcalF^q and its order is calculated exactly. |
| support | [Normalized gate and original layer definitions](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Exact formal comparison and S_star=0 from the supplied full low-layer integer lift, without asserting original residual realization. |
| support | [Earlier general parity boundary](Yin_C_G0609_v2.md#statement) | The precise weaker endpoint/complement parity condition satisfied by the construction, not a source of an inferred full gate. |
| review | [Independent whole family finding](../audits/reviews/Yin_R_G0816_v1.md#whole-unbounded-family-finding) | Complete fixed statement, argument, selected dependencies and comparisons, exact whole original reduction, both signs and all-lift contradiction; prior unknown review relationships retained. |


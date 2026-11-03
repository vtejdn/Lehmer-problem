---
author: Yin
---
# Uniform elimination of upper original layers and the homogeneous normalized gate

Human author Yin.
Root proposed the general deformed-gate reduction, exact layer-composition identity and two-profile fifth-root argument.
The same_trace contributor checked and completed the full6m/8m root expansion, its linear cancellation, the two projection precisions and constant branches, the direct layer-order bootstrap and the actual integer multiplicity consequence.
Both are mathematical contributors; neither independently reviews this new proof.
The work continues under the [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
Focused reuse inspected C199's actual normalized gate/layers/complement, C197's T-support derivative, C634's exact fifth-root identities, C643v2's FORMAL homogeneous classification and C609v2's actual complete-factor endpoint parity.
The new elimination proof does not invoke C643's original intermediate-layer assertion or any special multiplicity calculation.
C649's adopted full CRT theorem is used only for the final full-jet consequence after the independent layer elimination; it is not an input to that elimination or its projection argument.
The [D1 uniform candidate](../drafts/Yin_D_G0001.md#uniform-full-gate-layer-projection-candidate) is development provenance, not a logical dependency.
No native mathematical computation, order scan or coefficient enumeration is used.
This new statement is initially open for fresh isolated whole mathematical review.

## Statement

### Full original hypotheses and the uniform conclusions

Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree d=2r.
For an original root alpha put K=Q(alpha), delta_original=alpha+alpha^(-1), and assume F=Q(delta_original) is totally real.
Let T in Z[X] be its actual monic degree-r minimal polynomial, so P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Define C_p by C_p(z+z^(-1))=z^p+z^(-p), and use the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta_original), b=theta_3(delta_original),
    c=theta_5(delta_original).

Assume a,b,c are nonzero and, for one s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G_can=rem_T(theta_5^3-2theta_3^5), w=deg G_can<r, U=T mod2 and R_can=G_can mod2.
Assume the normalized circle Haar integral of log(G_can(z+z^(-1))^2), using the integrable logarithm at circle zeros, is0.
Put phi=X^2+X+1 and assume

    ord_phi R_can<ord_phi U,
    ord_psi R_can>=ord_psi U for every irreducible psi dividing U,
                                               psi!=phi.

Let q=2^k be the actual maximal power of2 for which U is a q-th power.
Retain C199's canonical U=U_0^q and R_can=R_0^q.
Its normalized multiplicity A_0=ord_XU/q is even and at least2; write A_0=2m with m>=1.
With chi=Xphi^2 and Psi=phi(chi), retain the actual complete factors

    U_0=X^(2m)phi^(14m)Y,
    R_0=rem_(U_0)(U_0(chi)^3)=X^(2m)Yphi^(12m)B,
    H_0=X^(2m)Y, V_0=H_0B,
    C_00=X^(2m)Y(chi)Psi^(14m), D_0=V_0+C_00^3,

where Y is monic prime to Xphi and B is the unique COMPLETE monic phi-unit complement with deg B<4m.
All saturated surpluses and extra remainder factors stay in B.

For n>=3 let the integer trace polynomial F_n be defined by Phi_n(z)=z^(phi(n)/2)F_n(z+z^(-1)), with phi(n) Euler's totient.
Retain the SAME actual zero-Haar integer factorization

    G_can=V_int product_(b>=0) F_(2^b*5)^(a_b),
    a_b nonnegative integers of finite support,
    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=12mq.

The factor V_int includes the sign and all other factors.
Define the prescribed original layer sum

    S_star=sum_(a_b odd, 4mq<lambda_b<12mq)
       X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                          phi^(12m-lambda_b/q).

Every index and integer a_b is original; none is divided by q or freely reassigned.

Then ALL layers above8mq vanish as actual integers:

    a_b=0 whenever lambda_b>8mq.                          (UL1)

In particular S_star lies in phi^(4m), D_0 lies in phi^(4m), and the full original normalized gate always lies in the homogeneous branch.
There is no exception for an intermediate power in(8m,10m].

Moreover

    m is even, equivalently4 divides A_0.                  (UL2)

Thus every odd half-multiplicity is excluded, including m=7, A_0=14, on precisely these original hypotheses.
Combining with the already adopted prior remaining range A_0>=14, any remaining original input has

    A_0 in{16,20,24,28,...}.

This is a necessary remaining range, not an existence claim for any of its values.

Every original input in this domain also has the now-unconditional homogeneous description

    B=X^(Q-m)H(chi),
    Q a power of2, 2m<Q<5m,
    H in F_2[t], H(0)=1, 5deg H<5m-Q,
    nu_2(ord_XB)=nu_2(m).                                 (UL3)

Here Q is an endpoint exponent, distinct from the original Frobenius power q.
Writing Q=2^s, define

    h_Q(X)=1+sum_(i=0)^(s-1)X^(Q-2^i),

and let x(t) be the formal inverse of chi at0.
The SAME actual Y has its complete low-X jet

    Y=L(X^2) modulo X^(4m),
    L(t)=[(1+t+t^2)^(7m)H(t)h_Q(x(t))]^(-1)
                          modulo t^(2m), deg L<2m.

In fact the SAME actual Y also has the full phi-primary jet from the now-applicable adopted CRT theorem.
Choose N with2^N>=8m and2^N congruent to Q modulo3, and let beta=X^(2^N) as a local class.
Then

    Y=X^(-2m)B^(-7)+beta X^(-2m)B^(-13)S_star
                                        modulo phi^(8m),
    Z_0=beta^2B^(-1)(1+beta B^(-6)S_star)
                                        modulo phi^(6m), (UL4)

where Z_0 is the actual unique unit eleventh root of H_0C_00^2 at6m.
The root correction is retained and every denominator is a phi-unit.
Together with the low-X formula this is a necessary full two-primary target for the actual original input, not an all-primary or characteristic-zero existence statement.

The original q remains maximal, U_0 and R_0 retain their actual nonsquareness, and all degree costs are

    r=q(30m+deg Y),
    w=q(26m+deg Y+deg B),
    r-w=q(4m-deg B)=q(5m-Q-5deg H)>0.

No all-primary or characteristic-zero sufficiency, global square of Y/B, smaller original field or unrestricted Task completion is asserted.

### Standalone two-profile Laurent rigidity

Let m>=1, and let f in F_2[X] be nonzero with X^m dividing f and deg f<5m.
Let gamma be a cube-one unit class modulo phi^(4m).
Let h(t),kappa(t) be formal power series over F_2 such that h(0)=1 and ord_t kappa>=m.
The substitutions below depend only on their classes modulo t^(2m).
Suppose

    f=gamma h(chi)+gamma^2 kappa(chi)
                                         modulo phi^(4m). (TP1)

Then gamma!=1.
There is a sigma in{1,2} such that the Laurent polynomial f(z+z^(-1)) has exponents only in the pair plus-or-minus sigma modulo5.
Furthermore

    ord_Xf>=2m,
    ord_t kappa>=2m.                                      (TP2)

The latter assertion concerns the entire low class of kappa, not only its constant coefficient.
It removes the second local profile at precisely phi^(4m).

### Formal full-gate implication with a composition-compatible correction

The following purely characteristic-two implication is also proved, independently of an original realization.
Let m>=1, B be a monic phi-unit with deg B<4m, and Y prime to Xphi with X^(4m) dividing Y'.
Use the same definitions H_0,V_0,C_00,D_0 as above, and assume D_0 in phi^(2m).
Let S be a specified class in phi^(2m) modulo phi^(8m).
Let Z_0 be the unique unit eleventh root of H_0C_00^2 modulo phi^(6m), and assume

    H_0^6=C_00^21 modulo phi^(8m),
    Z_0D_0+H_0V_0S=0 modulo phi^(8m).                     (FB1)

Suppose, in addition, that for a series Sigma(t) in t^mF_2[[t]],

    X^(6m)S=Sigma(chi) modulo phi^(4m).                   (FB2)

Then ord_t Sigma>=2m and S lies in phi^(4m).
The two-profile hypothesis is a consequence of the FULL6m/8m gate and the stated composition relation, not an additional root truncation.
This implication does not claim the result for arbitrary corrections lacking (FB2).

## Argument

### Exact local constants and fifth-root coordinates

The elementary trace identities and finite fifth-root method are reused at the exact scope of [C634's proof](Yin_C_G0634_v1.md#argument); the full two-profile extension is proved here.
Work over an algebraic closure of F_2 and choose a primitive fifth root xi.
For j=1,2,3,4 put x_j=xi^j+xi^(-j), the two nonzero roots of phi in F_4.
The exact identities are

    X(z)=z+z^(-1)=(z+1)^2/z,
    phi(X(z))=z^(-2)(z^4+z^3+z^2+z+1),
    chi(X(z))=z^5+z^(-5)=(z^5+1)^2/z^5.                  (TP3)

Thus phi(X(z)) has simple zeros at the four nonidentity fifth roots.
The functions X(z) at1 and chi(X(z)) at each fifth root have exact order2.

Choose a power2^n>=4m.
The class beta=X^(2^n) satisfies beta^2+beta+1=phi^(2^n)=0 modulo phi^(4m).
The only cube-one classes are1,beta,beta^2: after fixing the residue constant, a principal unit1+u has

    (1+u)^3+1=u(1+u+u^2),

and its second factor is a unit.
Thus a cube-one principal unit must be1 at the full precision.

If gamma!=1, there is one sigma in{1,2} such that its constants at ALL four points are

    gamma_j=x_j^sigma=xi^(sigma j)+xi^(-sigma j).
    gamma_j^2=xi^(2sigma j)+xi^(-2sigma j).

This follows from the two Frobenius powers on F_4.
The chosen polynomial representatives differ from these local constants only at order at least4m, so the full precision is retained.
The pair plus-or-minus2sigma modulo5 is different from plus-or-minus sigma.

### Excluding the constant-one profile

Put F(z)=f(X(z)) and N=deg f.
If gamma=1, (TP1) gives at every nonidentity fifth root the SAME local function

    F(z)=(h+kappa)(chi(X(z))) modulo order4m.

The series h+kappa has constant1 because m>=1.
Let D(z)=F(xi z)+F(z).
The chi function is invariant under z going to xi z.
At z=xi,xi^2,xi^3 both arguments are nonidentity fifth roots, so D has a zero of order at least4m at each of these three distinct points.

Its Laurent exponents lie between-N and N.
Therefore z^N D is a polynomial of degree at most2N<10m, with nonzero-root multiplicity at least12m.
It must vanish identically.
Evaluating the resulting identity at z=1 gives F(xi)=F(1).
But F(1)=f(0)=0 because X^m divides f, whereas F(xi)=1 by the local profile.
This contradiction excludes gamma=1 using the full4m precision, without discarding kappa.

### Lower projection fixes the single Laurent residue pair

Now use the nontrivial gamma and the sigma above.
For a residue a modulo5 define

    F_a(z)=sum_(j=0)^4 xi^(-aj) F(xi^j z).

Since5=1 in characteristic2, direct finite geometric summation gives

    F_a(z)=sum_(n congruent a mod5) [z^n]F(z) z^n,
    F_a(xi z)=xi^a F_a(z).                                (TP4)

No analytic Fourier theorem is invoked.
At z=1, kappa(chi(X(z))) has order at least2m.
For j=1,...,4, (TP1) therefore implies

    F(xi^jz)=gamma_j h(chi(X(z))) modulo order2m.

For j=0, X^m divides f, so F(z) has order at least2m.
Set gamma_0=0, which equals xi^0+xi^0.
The same comparison then holds for every j=0,...,4.

If a is not sigma or-sigma modulo5, the weighted sum of these constants is0.
Thus F_a has a zero of order at least2m at1.
The eigenidentity in (TP4) propagates that order to ALL five distinct fifth roots.
But z^N F_a has degree at most2N<10m, while these five zeros have total multiplicity at least10m.
Hence F_a vanishes identically.
This proves that F has only the one pair sigma,-sigma, even though its local expansion initially had two profiles.

### Local inversion upgrades the endpoint to the full precision

The Laurent polynomial is symmetric: F(z)=F(z^(-1)).
For the two surviving components this gives

    F_(-sigma)(z)=F_sigma(z^(-1)).

The substitution z going to xi^2/z fixes z=xi and preserves chi(X(z)) exactly.
Both local functions h(chi) and kappa(chi), with the same constants gamma_1,gamma_1^2, are unchanged there.
Consequently F(z)+F(xi^2/z) has a zero of order at least4m at xi.
The substitution is locally invertible there, so this preserves the error order.

Writing A_sigma(t)=F_sigma(t), the exact residue classes give

    F(xi t)=xi^sigma A_sigma(t)+xi^(-sigma)A_sigma(t^(-1)),
    F(xi/t)=xi^sigma A_sigma(t^(-1))+xi^(-sigma)A_sigma(t).

Their sum is(xi^sigma+xi^(-sigma))F(t).
The scalar is nonzero.
Hence F(t) has order at least4m at t=1.
By X(t)=(t+1)^2/t, its exact order is2ord_Xf, proving ord_Xf>=2m.

### Full projection kills the second profile

The improved endpoint makes F(z) vanish to order4m at z=1.
Set gamma_0=gamma_0^2=0.
The full local comparison

    F(xi^jz)=gamma_j h(chi(X(z)))
                  +gamma_j^2 kappa(chi(X(z)))
                                         modulo order4m

now holds for EVERY j=0,...,4, including j=0.
Choose the residue a=2sigma modulo5.
It lies outside the surviving pair sigma,-sigma, so F_a is identically zero by the lower projection.
Finite orthogonality gives

    sum_(j=0)^4 xi^(-aj)gamma_j=0,
    sum_(j=0)^4 xi^(-aj)gamma_j^2=1.

The second equality selects exactly one of the two distinct residues2sigma,-2sigma.
Thus the full projection gives kappa(chi(X(z)))=0 modulo order4m at1.
By (TP3), this composition has exact order2ord_t kappa unless it vanishes identically.
Therefore ord_t kappa>=2m.
This proves (TP2), with no inference from a lower-order expansion to the full precision.

### The full6m/8m gate produces precisely the two profiles

We prove the formal implication (FB1)--(FB2).
The low-X derivative gives a unique polynomial L of degree below2m with

    Y=L(X^2) modulo X^(4m), L(0)=1.
    A(t)=(1+t+t^2)^(7m)L(t),
    u=X^mA(chi), f=X^mB, F=Bu=fA(chi).

Here u is a phi-unit and C_00=u^2 modulo phi^(8m).
Every low coefficient is retained; the error after substitution has order8m because ord_phi chi=2.

The old relation in (FB1) gives H_0^6=u^42 modulo phi^(8m).
Taking its exact square valuation gives

    (H_0/u^7)^3=1 modulo phi^(4m).

Choose the cube-one lift mu of its residue at precision8m.
Such a lift exists and is unique for the fixed residue by the same principal-unit argument used above, or by a sufficiently large Frobenius power.
Put

    Delta=H_0+mu u^7 in phi^(4m).

This Delta order follows from the OLD relation.
It does not assume the conclusion D_0 in phi^(4m), which has not yet been proved.
Since Delta^2 vanishes modulo phi^(8m), the representative

    Z_*=mu^2u(1+mu^2u^(-7)Delta)
       =mu^2u+mu u^(-6)Delta                              (FB3)

has eleventh power H_0u^4 modulo phi^(8m).
Indeed the base eleventh power is mu u^11, and its linear correction is u^4Delta.
It therefore represents Z_0 modulo phi^(6m).
Replacing the actual root by this representative in the gate is legitimate only because the INITIAL D_0 order2m pays the6m lift error at8m.

Using D_0=H_0B+u^6 modulo phi^(8m), expansion gives

    Z_*D_0=u^8B+mu^2u^7+mu Delta
                                         modulo phi^(8m).

The two linear terms mu^2uBDelta cancel exactly.
The remaining quadratic term mu u^(-6)BDelta^2 vanishes at8m.
Also

    H_0V_0S=H_0^2BS=mu^2u^14BS modulo phi^(8m).

Thus the full gate is equivalent, at the precision used here, to

    H_0=mu^2u^8B+mu u^14BS modulo phi^(8m).

Reduce this identity modulo phi^(4m), where H_0=mu u^7, and divide by the unit mu u^7.
It becomes

    F(mu+u^6S)=1 modulo phi^(4m).

Now S is in phi^(2m), so (u^6S)^2 vanishes at4m.
With gamma=mu^2, inversion of the unit gives

    F=gamma+gamma^2u^6S,
    F^2=gamma^2, F^6=1                      modulo phi^(4m).

Because F=Bu, the last equality gives u^6=B^(-6) at4m.
Consequently

    F=gamma+gamma^2B^(-6)S.                              (FB4)

All inverses are phi-local units.
These are necessary deductions from the whole gate; no unproved reverse deformed-cube equivalence is used.

The equality F^6=1 also gives

    B^(-6)=X^(6m)A(chi)^6 modulo phi^(4m).

Divide (FB4) by the unit A(chi) and use (FB2).
The result is

    f=gamma h(chi)+gamma^2 kappa(chi) modulo phi^(4m),
    h(t)=A(t)^(-1), kappa(t)=A(t)^5 Sigma(t).             (FB5)

The series h has constant1 and kappa has order at least m.
Only their classes modulo t^(2m) matter, but no auxiliary degree restriction was imposed.
The standalone two-profile theorem applies to the full polynomial f: it is nonzero, divisible by X^m and has degree below5m.
It yields ord_t kappa>=2m.
Since A(0)=1, multiplication by A^5 preserves order, so ord_t Sigma>=2m.
Then (FB2), with X a phi-unit, gives S in phi^(4m).
This proves the formal implication without prematurely strengthening D_0 or truncating the root.

### Exact layer algebra supplies the composition condition without circularity

Return to the original input and its actual S_star.
The [C199 normalized full gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) supplies D_0 in phi^(2m), S_star in phi^(2m), its square property, the old relation and the full6m/8m root/gate equations.
The [C197 derivative interface](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) supplies X^(4m)|Y' through the normalized T-support odd part.
The complete B and its degree below4m come from [C199's canonical complement](Yin_C_G0199_v4.md#normalized-low-degree-complement).
Thus every formal hypothesis except (FB2) has already been obtained from the SAME original input.

For each odd original layer in S_star put ell=lambda_b/q.
The high window ensures that ell is a positive integral power of2, with4m<ell<12m.
Write rho=6m-ell/2, a positive integer.
Its term S_ell satisfies the exact POLYNOMIAL identity

    X^(6m)S_ell
      =X^(6m+ell/2)(X+1)^ell phi^(12m-ell)
      =chi^rho [X(X+1)]^ell
      =chi^rho(1+phi^ell).                               (LI1)

The last step uses X(X+1)=1+phi and the fact that ell is a power of2.
Its extra term is exactly

    chi^rho phi^ell=X^rho phi^(12m).

Define the finite polynomial

    Sigma(t)=sum_(a_b odd, 4mq<lambda_b<12mq)
                    t^(6m-lambda_b/(2q)).

Summing (LI1) gives X^(6m)S_star=Sigma(chi) modulo phi^(12m), in particular modulo phi^(4m).
Since S_star is already in phi^(2m), this same identity gives Sigma(chi) in phi^(2m).
For any nonzero polynomial Sigma with lowest exponent e, the factorization chi=Xphi^2 gives exact order ord_phi Sigma(chi)=2e.
Thus ord_t Sigma>=m; if Sigma=0 this is automatic.
This obtains (FB2) DIRECTLY from C199 and the exact layer algebra.
It does not invoke C643's earlier intermediate-layer conclusion, so there is no circular dependence.

The formal implication now gives ord_t Sigma>=2m and S_star in phi^(4m).
Distinct high layer indices have distinct lambda_b: the only duplicated values lambda_0=lambda_1=1 are outside the high window.
Hence all exponents in Sigma are distinct.
A contributing exponent is below2m exactly when ell>8m.
No such term can remain after ord_t Sigma>=2m.
Therefore every original a_b with8mq<lambda_b<12mq is even.

The total ORIGINAL weight gives a_b lambda_b<=12mq.
When lambda_b>8mq this bounds a_b by1.
Its even parity therefore forces the integer a_b=0.
Every occurring lambda_b is already strictly below12mq by C199; larger layers are absent.
This proves (UL1) for ALL lambda_b>8mq, not merely their parity or a normalized choice.

### Homogeneous consequence, endpoint parity and remaining original scope

Since the actual S_star is now in phi^(4m), the full gate and unit Z_0 force D_0 in phi^(4m).
Alternatively (FB5) and the two-profile conclusion give fA(chi)=gamma modulo phi^(4m), hence the same homogeneous cube directly.
Either route uses the actual low polynomial L and the SAME complete B.

Apply only the FORMAL homogeneous statement of [adopted C643v2](Yin_C_G0643_v2.md#statement).
It gives the sharp power Q, unique H, complete B shape, all low Y coefficients and endpoint valuation in (UL3).
This use is independent of that source's original intermediate-layer assertion.
In particular ord_Xf=Q is even.
The [actual complete-factor parity theorem C609v2](Yin_C_G0609_v2.md#statement) gives even ord_XB for this original V_0.
Since ord_Xf=m+ord_XB, m must be even.
This proves (UL2), including the previously inhomogeneous m=7 branch, without using the earlier unverified special coefficient table.

The [adopted C640 remaining-range conclusion](Yin_C_G0640_v1.md#statement) already requires A_0>=14 on the identical original domain.
Combining it with4 dividing A_0 gives the necessary range{16,20,24,...}.
C640 is used ONLY for this final range statement, not for the uniform layer elimination or the parity argument.

The newly proved S_star order4m now meets the explicit hypothesis of [adopted C649's full CRT equivalence](Yin_C_G0649_v1.md#statement).
Applying that theorem to the SAME original Y,B and prescribed S_star gives (UL4), including its6m root correction and complete8m phi jet.
This use occurs strictly AFTER the independent layer/bootstrap proof and creates no circular input.
It neither replaces the actual Y by another formal CRT representative nor asserts the additional all-primary or characteristic-zero conditions from the jet alone.

The exact complete degree comparison remains

    deg U_0=30m+deg Y,
    deg R_0=26m+deg Y+deg B.

The zero-Haar integer cyclotomic factorization has leading coefficient1 or-1, so reduction preserves the degree of G_can.
Restoring the actual maximal q gives precisely the degree identities in the statement.
All remaining integer layers still sum to12mq; (UL1) does not divide, relabel or forget them.
The normalized nonsquare U_0,R_0 and original fields are retained from C199.
No polynomial-module extraction has altered q or produced a smaller original T.
The new theorem eliminates the intermediate-layer alternative; it does not construct or exclude every remaining multiple-of-four branch, prove all-primary sufficiency or complete the unrestricted Task.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:26 |
| status | open |
| reason | Register the standalone two-profile Laurent rigidity, complete6m/8m gate bootstrap and exact original layer-composition identity. They force every actual lambda_b>8mq coefficient to vanish, make the full original gate homogeneous and require4 to divide A_0, leaving the prior-range intersection{16,20,24,...}. The complete homogeneous B/low-Y shape and every original q/layer/degree are retained. No native calculation, original-input descent, remaining-branch realization or unrestricted completion is claimed. Fresh isolated whole mathematical review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original conclusions and standalone implications](#statement) | UL1--UL4, TP1--TP2 and FB1--FB2, including actual integer layer vanishing, all odd-m exclusion, complete homogeneous complement/full jets and exact remaining range on the explicit original domain. |
| argument | [Full two-profile and original layer proof](#argument) | Full and lower projection orders, constant-one contradiction, local inversion, second-pair orthogonality, root expansion/cancellation at6m/8m, LI1 and noncircular layer-order bootstrap, integer weight and actual costs. |
| dependency | [Exact original normalized domain](Yin_C_G0199_v5.md#statement) | Same original P/T/fields/divided remainders/residuals/Haar/unsaturation and actual maximal q/canonical roots. |
| dependency | [Actual full normalized gate and layers](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Initial D/S order2m, root6m/error8m, old relation, original a_b/lambda_b, total12mq weight and strict layer bound; no freely normalized integer data. |
| dependency | [Complete complement and degree budget](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual entire B, strict degree below4m and every saturated surplus/extra remainder factor. |
| dependency | [Actual normalized T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divisibility of Y' through the full normalized odd-support polynomial. |
| dependency | [Fifth-root trace identities](Yin_C_G0634_v1.md#argument) | Exact X,phi,chi Laurent identities, finite projection and inversion mechanism; the new two-profile conclusion is proved here. |
| dependency | [Formal homogeneous classification only](Yin_C_G0643_v2.md#statement) | SC3/SC5 and the explicit unique auxiliary jet once the NEW theorem has forced homogeneity; no reliance on its original intermediate-layer assertion. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB of the SAME original V_0, used after the homogeneous formal conclusion to force m even. |
| dependency | [Prior restricted remaining range](Yin_C_G0640_v1.md#statement) | A_0>=14 only for the final intersection with the new divisibility by4, not for the uniform core. |
| dependency | [Adopted complete homogeneous CRT](Yin_C_G0649_v1.md#statement) | Only the final full actual Y jet and corrected root after the new layer proof has supplied S_star in phi^(4m); no input to the uniform elimination. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:39 |
| status | proved |
| reason | Adopt the entire UL1--UL4, TP1--TP2 and FB1--FB2 theorem after main reading of complete C650 and isolated whole R858. The full two-profile projection/inversion proof, initial2m root-error payment and exact6m/8m cancellation, LI1 and noncircular layer bootstrap force every actual integer layer above8mq to vanish. The SAME original input is homogeneous and4 divides A0, giving the necessary remaining range{16,20,24,...}; complete classified B, both actual Y jets, corrected root, maximal q and all original costs remain. No native computation, original-input descent, remaining-branch existence, all-primary sufficiency or unrestricted Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original conclusions and standalone implications](#statement) | UL1--UL4, TP1--TP2 and FB1--FB2, including actual integer layer vanishing, all odd-m exclusion, complete homogeneous complement/full jets and exact remaining range on the explicit original domain. |
| argument | [Full two-profile and original layer proof](#argument) | Full and lower projection orders, constant-one contradiction, local inversion, second-pair orthogonality, root expansion/cancellation at6m/8m, LI1 and noncircular layer-order bootstrap, integer weight and actual costs. |
| dependency | [Exact original normalized domain](Yin_C_G0199_v5.md#statement) | Same original P/T/fields/divided remainders/residuals/Haar/unsaturation and actual maximal q/canonical roots. |
| dependency | [Actual full normalized gate and layers](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Initial D/S order2m, root6m/error8m, old relation, original a_b/lambda_b, total12mq weight and strict layer bound; no freely normalized integer data. |
| dependency | [Complete complement and degree budget](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual entire B, strict degree below4m and every saturated surplus/extra remainder factor. |
| dependency | [Actual normalized T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divisibility of Y' through the full normalized odd-support polynomial. |
| dependency | [Fifth-root trace identities](Yin_C_G0634_v1.md#argument) | Exact X,phi,chi Laurent identities, finite projection and inversion mechanism; the new two-profile conclusion is proved here. |
| dependency | [Formal homogeneous classification only](Yin_C_G0643_v2.md#statement) | SC3/SC5 and the explicit unique auxiliary jet once the NEW theorem has forced homogeneity; no reliance on its original intermediate-layer assertion. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB of the SAME original V_0, used after the homogeneous formal conclusion to force m even. |
| dependency | [Prior restricted remaining range](Yin_C_G0640_v1.md#statement) | A_0>=14 only for the final intersection with the new divisibility by4, not for the uniform core. |
| dependency | [Adopted complete homogeneous CRT](Yin_C_G0649_v1.md#statement) | Only the final full actual Y jet and corrected root after the new layer proof has supplied S_star in phi^(4m); no input to the uniform elimination. |
| review | [Independent entire layer-elimination finding](../audits/reviews/Yin_R_G0858_v1.md#whole-two-profile-layer-elimination-finding) | Entire UL1--UL4, TP and FB proof, both projection precisions and inversion, full initial2m/root6m/error8m expansion, exact LI1 and direct order bootstrap, integer layer vanishing, original parity/range/jets/costs and acyclic dependency scope. |


---
author: Yin
---
# Complete trace-group character, endpoint parity and the normalized multiplicity-two exclusion

Human author Yin.
This substantive v2 preserves the complete [physical v1 candidate](Yin_C_G0609_v1.md#statement), including its exact16-row proof, and supplies an analytic replacement for the all5-divisible-order step plus a general parity theorem.
Root supplied the character projection, general endpoint-parity proposal, exact B_(5m) composition identity and chain-rule argument.
The same_trace contributor checked and completed the Laurent exponents, every local precision, the coefficient functional, complete divisor induction and actual q/multiplicity bridge against C199v4/v5.
Both are mathematical contributors; no old review covers this new proof and neither contributor independently reviews it.
The result is developed under the [current all-strategy continuation](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
The [D1 analytic author account](../drafts/Yin_D_G0001.md#analytic-complete-group-parity) is extraction provenance, not a logical input.
The reuse check inspected the selected C608 character proof, the exact C199v4 normalized derivative/factor/complement proof and the retained C199v5 complete A_0=2 classification.
The new analytic all5-order step uses no16-row computational premise; J120 remains corroboration of the preserved first proof.
The new general parity result retains the full original zero-Haar and unique-unsaturated domain and gives no A_0>=4 classification or unrestricted Mahler estimate.

## Statement

### General formal parity and original complement consequence


Let phi=X^2+X+1 and let W_n be the complete primitive odd-order trace group polynomial for n>1, as defined in [C608](Yin_C_G0608_v1.md#statement).
For any integers e>=0 and b_n>=0 of finite support, with n odd and n!=5, put

    V=X^e product_n W_n^(b_n).

This is a monic polynomial prime to phi, including V=1 when all exponents are zero.
Then

    phi^8 divides V'  =>  e is even.             (AP1)

No low-X hypothesis, degree bound, actual trace-field realization or assumption about any separate integer cyclotomic multiplicity is imposed in this formal assertion.
On the complete original zero-Haar and unique-unsaturated domain of C199v4/v5, it implies

    ord_X V_0 even,
    ord_X B even.                               (AP2)

The second conclusion uses the actual identity V_0=H_0B and the inherited even A_0=ord_X H_0.
Thus the full A_0=2 branch, whose complete B is X^3, is impossible for every original q.
This is a shorter second proof of C609v1's original-input exclusion and does not classify the remaining even A_0>=4 cases.


### Exact original domain and preserved v1 conclusion

For the original-input application, let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree2r.
For an original root alpha set delta=alpha+alpha^(-1), assume F=Q(delta) is totally real, and let T in Z[X] be the actual monic degree-r minimal polynomial of delta.
Thus P(z)=z^r T(z+z^(-1)).
Define C_p by C_p(z+z^(-1))=z^p+z^(-p), and use the actual integer polynomials theta_p=rem_T(T(C_p))/p for p=2,3,5.
Assume a=theta_2(delta), b=theta_3(delta), c=theta_5(delta) are all nonzero and, for one sign s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G=rem_T(theta_5^3-2theta_3^5), U=T mod2, R=G mod2 and phi=X^2+X+1.
Assume the normalized circle Haar integral of log(G(z+z^(-1))^2) is0, with its integrable logarithm at circle zeros, and assume

    ord_phi R<ord_phi U,
    ord_psi R>=ord_psi U for every irreducible psi|U, psi!=phi.

These are exactly the relevant complete original hypotheses in [C199v5](Yin_C_G0199_v5.md#statement).
Let q be the maximal power of2 for which U is a q-th power in F_2[X], put A=ord_X U, and retain the normalized multiplicity A_0=A/q supplied by C199v5.
The new conclusion excludes A_0=2 for every original q; combined with C199's inherited evenness it leaves A_0>=4 on that full domain.
It does not exclude multiple unsaturated factors, another normalized multiplicity, a positive canonical Haar branch or the unrestricted Lehmer Task.


In that exact domain, use the actual canonical Frobenius roots U=U_0^q and R=R_0^q supplied by C199v4/v5.
Set H_0=U_0/phi^(7A_0) and V_0=R_0/phi^(6A_0), and use the unique complete monic complement B with V_0=H_0B and deg B<2A_0.
Then (AP2) holds for every allowed even A_0, not only2.
The complete formal nonexistence assertion of physical v1 is also retained: no finite product Y of complete W_n with n odd,n>1,n!=5 satisfies C608's low-X and full normalized A_0=2 gate for either parity.

## Argument

### Character projection and the endpoint factor


Put S=F_2[X]/(phi^8) and retain R=F_2[X]/(X^4phi^8).
For a canonical representative f of degree below16 in S define ell(f)=[X^13]f+[X^15]f.
If a polynomial of degree below20 is reduced from R to S, the discarded part is phi^8Q with deg Q<4.
Since phi^8=X^16+X^8+1, that discarded part has no X^13 or X^15 coefficient.
Therefore the old R functional is exactly ell after projection to S.
Differentiation descends to S because (phi^8)'=0, and the projection commutes with differentiation and unit inversion.
Consequently the character

    lambda_phi(u)=ell(u'/u), u in S^*,           (AP3)

agrees with C608's old character on every unit of R.
In particular C608's all-order coprime5 conclusion gives lambda_phi(W_n)=0 for every odd n>1 coprime to5.
The map (AP3) is a group homomorphism by the product rule.
It also applies to X, which is a unit in S even though it is not a unit in R.
The explicit identity

    X^(-1)=X^15+X^7 in S,
    lambda_phi(X)=1                            (AP4)

follows by multiplication, since X^16+X^8=1 modulo phi^8.

### Exact whole-root composition and the chain-rule certificate

For odd m>=1, let B_m=product_(d|m,d>1)W_d, with B_1=1, be the polynomial of all nonidentity m-th-root traces.
Use its whole-root Laurent identity from C608 and the identity B_5=phi.
With X=z+z^(-1) and chi=Xphi^2=z^5+z^(-5), multiply

    phi(X)=z^(-2)(z^5+1)/(z+1),
    B_m(chi)=z^(-5(m-1)/2)(z^(5m)+1)/(z^5+1).

The total exponent is -2-5(m-1)/2=-(5m-1)/2.
The product is exactly the Laurent expression for B_(5m), and injectivity of the trace substitution proves the polynomial identity

    B_(5m)(X)=phi(X) B_m(chi),
    D_(5m)=B_m(chi).                            (AP5)

This identity includes m divisible by5 and keeps the whole primitive-divisor content; it is not a statement only about order25.
Since B_m(0)=1, B_m(chi) is a unit at phi and the formal power series

    h_m(t)=B_m'(t)/B_m(t) in F_2[[t]]

exists with coefficients in F_2.
The exact chain rule and chi'=phi^2 give

    D_(5m)'/D_(5m)=phi^2 h_m(chi).

The substitution in S needs only the constant, linear and quadratic coefficients of h_m: every term of index j>=3 has phi-order at least2+2j>=8.
Hence the resulting logarithmic derivative in S belongs to the F_2-span

    span{phi^2, Xphi^4, X^2phi^6}.              (AP6)

The first two displayed polynomials have degrees4 and9.
The third has degree14 and only even powers of X, because phi^6 is a square.
Each has both its X^13 and X^15 coefficients zero.
Therefore

    lambda_phi(D_(5m))=0 for every odd m>=1.     (AP7)

This all-order step is analytic polynomial algebra and uses no16-row certificate as a premise.
J120 remains an exact independent-arithmetic corroboration of the earlier finite proof, without being promoted to independent agent review.

### Complete factor induction and application before degree normalization

For n>5 odd with5|n, the exact factor partition is D_n=product_(d|n,d>1,d!=5)W_d.
All its factors are units in S.
Use (AP7), the coprime5 input and induction over proper divisors to conclude lambda_phi(W_n)=0 for every remaining odd n>1,n!=5, exactly as in AG6--AG7.
This treats every power of5 and every additional odd prime factor.
By (AP3)--(AP4), any V in (AP1) has lambda_phi(V)=e modulo2.
If phi^8|V', its logarithmic derivative is zero in S, so e must be even, proving (AP1).

The formal complete-group nonexistence assertion retained from v1 also follows from this character proof.
For the Y of C608's full normalized A_0=2 gate, every factor W_n has character0, whereas C608 SG4/SG11 forces its class to one of two targets with character1.
Projection to S preserves that character value, giving the contradiction for both parity choices without an actual monic coefficient construction.

For the actual normalized gate, [C199v4's complete actual-unit argument](Yin_C_G0199_v4.md#normalized-actual-unit-odd-part) gives both ord_phi V_0'>=4A_0 and the exact factor multiplicities in V_0.
Write nu_n for the common ORIGINAL reduced multiplicity of the complete odd-order group n in V=V_int mod2, with the endpoint convention nu_1 for X.
The canonical equality V=V_0^q implies q divides every nu_n, including nu_1, by unique factorization in F_2[X].
Thus the actual polynomial has the complete factorization

    V_0=X^(nu_1/q) product_(n odd,n>1,n!=5)
                                      W_n^(nu_n/q). (AP8)

No individual characteristic-zero cyclotomic exponent a_m is assumed divisible by q.
The endpoint factor X and every other complete group retain their original multiplicities before this canonical Frobenius descent; the equality is not a separately realized normalized field input.
The inherited A_0 is even and at least2, so4A_0>=8 and (AP1) applies to (AP8).
This proves ord_X V_0=nu_1/q even.
The [exact complement identity](Yin_C_G0199_v4.md#normalized-low-degree-complement) is V_0=H_0B with ord_X H_0=A_0 even, whence ord_XB is even as well, proving (AP2).
Finally C199v5's complete A_0=2 classification gives B=X^3, whose X-order is3, a contradiction.
The full original domain, all original q and the complete cyclotomic layers remain those of C199; the conclusion does not remove any of those hypotheses.

## Exact inputs and review boundary

| Input | Exact use and limit |
| --- | --- |
| [C608 fixed character proof](Yin_C_G0608_v1.md#argument) | SG7--SG10 and its32 exact rows give the character0 result for all coprime5 complete groups. SG4/SG11 and both targets are used only to preserve the separate formal-Y nonexistence assertion, not for the new general parity theorem. |
| [C608 exact formal gate domain](Yin_C_G0608_v1.md#statement) | The exact full-group, low-X and both-parity conditions in the retained formal-Y assertion. |
| [C199v4 derivative and complete factor bridge](Yin_C_G0199_v4.md#normalized-actual-unit-odd-part) | UR20's ord_phi V_0 prime >=4A_0 and every actual normalized complete multiplicity nu_n/q, including X, derived from V=V_0^q; no individual characteristic-zero cyclotomic exponent is divided byq. |
| [C199v4 exact complete complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual V_0=H_0B, full monic B and its degree scope; every surplus and extra factor remains included. |
| [C199v5 exact original domain and classification](Yin_C_G0199_v5.md#statement) | Entire original residual/field/zero-Haar/unique-unsaturated domain, actual maximalq and even A_0>=2, inherited v4 conclusions, and B=X^3 only when A_0=2. |
| [J120 corroborating native evidence](../computations/programs/Yin_J_G0120/readme.md#results-and-limits) | The full16-row predivision certificate remains evidence for the first proof and corroborates AP5--AP7 on its exact finite classes. It is not a logical premise for this v2 analytic all-order argument. |

The exact Laurent identity and chain-rule truncation are proved completely in this version.
The accepted C608 coprime5 finite interface remains the only finite certificate used as a proof input.
The old C609v1 statement, proof and initial decision are preserved; the current selected assessment owns the separate whole-v2 review without fabricating a whole-v1 adoption.
A fresh isolated reviewer must cover the full current statement, all AP1--AP8 steps, character projection and endpoint, exact composition, nilpotent truncation, all-order divisor induction and every original q/factor/derivative/complement interface.
The full original Task remains unresolved beyond the exact excluded branch and new complement parity.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial-v2

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:04 |
| status | open |
| reason | Preserve v1's complete normalized A_0=2 exclusion, replace its all5-order finite premise by the exact B_(5m)=phi B_m(chi) chain-rule proof, and add the general phi^8 derivative endpoint-parity theorem and actual even X-order of V_0 and B for every allowed A_0. Root and same_trace are contributors; the complete revised chain awaits fresh isolated review. No unrestricted Task completion or A_0>=4 classification is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire revised theorem](#statement) | General formal derivative-parity theorem, full actual V_0/B parity on every allowed normalized multiplicity, preserved both-parity formal-Y exclusion and exact original A_0=2 exclusion for arbitraryq. |
| argument | [Complete analytic revised proof](#argument) | AP1--AP8, coefficient-functional projection, endpoint X, exact whole-root composition, chain-rule truncation, complete divisor induction, full Frobenius factor bridge and both original applications. |
| dependency | [Accepted coprime5 character and targets](Yin_C_G0608_v1.md#argument) | Coprime5 character proof and32-row input; the two target identities only for the separately retained formal-Y contradiction. |
| dependency | [Exact formal normalized gate](Yin_C_G0608_v1.md#statement) | Whole-group, low-X and full local-unit domain for the retained formal assertion. |
| dependency | [Actual normalized derivative and factors](Yin_C_G0199_v4.md#normalized-actual-unit-odd-part) | UR20 and exact nu_n/q factorization, including endpointnu_1, under the full actual original domain. |
| dependency | [Actual complete complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) | V_0=H_0B with every surplus/extra factor and full degree scope retained. |
| dependency | [Original domain, evenness and A_0=2 classification](Yin_C_G0199_v5.md#statement) | Full inherited original hypotheses and normalization, even A_0>=2, and exact B=X^3 only on A_0=2. |
| support | [Corroborating16-row native evidence](../computations/programs/Yin_J_G0120/readme.md#results-and-limits) | Finite evidence for preserved v1 and exact agreement with the analytic all5-order mechanism, without making a finite scan a premise of AP5--AP7. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T16:16 |
| status | proved |
| reason | Adopt the complete formal derivative-parity theorem, actual even X-orders of V_0 and B on every allowed normalized multiplicity, and full A_0=2 exclusion for every original q after the isolated whole R812 review. All original residual, field, zero-Haar and unique-unsaturated hypotheses remain. C608's finite premise was independently reconstructed; J120 remains corroboration of the analytic all-five-order argument. Older accepted C199 review relationships remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire revised theorem](#statement) | General formal derivative-parity theorem, full actual V_0/B parity on every allowed normalized multiplicity, preserved both-parity formal-Y exclusion and exact original A_0=2 exclusion for arbitraryq. |
| argument | [Complete analytic revised proof](#argument) | AP1--AP8, coefficient-functional projection, endpoint X, exact whole-root composition, chain-rule truncation, complete divisor induction, full Frobenius factor bridge and both original applications. |
| dependency | [Accepted coprime5 character and targets](Yin_C_G0608_v1.md#argument) | Coprime5 character proof and32-row input; the two target identities only for the separately retained formal-Y contradiction. |
| dependency | [Exact formal normalized gate](Yin_C_G0608_v1.md#statement) | Whole-group, low-X and full local-unit domain for the retained formal assertion. |
| dependency | [Actual normalized derivative and factors](Yin_C_G0199_v4.md#normalized-actual-unit-odd-part) | UR20 and exact nu_n/q factorization, including endpointnu_1, under the full actual original domain. |
| dependency | [Actual complete complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) | V_0=H_0B with every surplus/extra factor and full degree scope retained. |
| dependency | [Original domain, evenness and A_0=2 classification](Yin_C_G0199_v5.md#statement) | Full inherited original hypotheses and normalization, even A_0>=2, and exact B=X^3 only on A_0=2. |
| support | [Corroborating16-row native evidence](../computations/programs/Yin_J_G0120/readme.md#results-and-limits) | Finite evidence for preserved v1 and exact agreement with the analytic all5-order mechanism, without making a finite scan a premise of AP5--AP7. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0812_v1.md#whole-trace-parity-finding) | Entire revised statement and AP1--AP8 proof, every selected input, the actual original factor/derivative/complement applications and both native roles, with accepted predecessor and source-review boundaries explicitly preserved. |


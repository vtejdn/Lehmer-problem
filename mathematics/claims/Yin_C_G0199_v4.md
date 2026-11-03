---
author: Yin
---
# Frobenius-normalized actual cyclotomic unit gates

Date: 2026-10-20T16:31.
Human author Yin.
This substantive v4 continues the same actual canonical-residual and zero-Haar inquiry as [physical v3](Yin_C_G0199_v3.md#statement), preserving all its stated conclusions at their separate hypothesis domains.
The complete physical v1--v3 proofs, decisions, earlier independent reviews and author relationships remain at their exact original scopes.
This version supplies the complete new UR13--UR23 deduction; it does not duplicate the long v3 CC9, DL, UJ, UR1--UR12 or UP arguments.
Root proposed the normalization and low-degree complement; entropy_attainment_bridge checked and completed all algebra, precision, original integer-layer bookkeeping and consequences.
Both are mathematical contributors, and the original date and contribution details of the new argument are retained below.
Root/draft_inventory_later authored UP and the UJ mechanism; root/entropy_attainment_bridge authored the v3 UR relation and the overlapping C197 input.
At this revision v3 is still a proof draft without an independent whole finding.
The new version likewise awaits a whole-chain independent review, including its actual use of v3; the older R477/R483 scopes cannot discharge that obligation.
There is no new source, mathematical program, actual original-input construction or adoption.

<a id="statement"></a>
## Complete theorem statement and exact additional domains

### Common original residual domain

Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree d=2r.
For a root alpha set K=Q(alpha), delta=alpha+alpha^(-1), and assume its actual trace field F=Q(delta) is totally real.
Let T in Z[X] be its actual monic degree-r minimal polynomial, so P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    a,b,c nonzero,
    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0, s in{1,-1},
    g=c^3-2b^5!=0.

Set G=rem_T(theta_5^3-2theta_3^5), w=deg G<r, U=T mod2, R=G mod2, Phi=X^2+X+1 in Z[X] and phi=Phi mod2.
Let I_can be the normalized circle Haar integral of log(G(z+z^(-1))^2), using the integrable logarithm at circle zeros.
The common domain by itself assumes neither I_can=0 nor a unique unsaturated factor.
All [v3 statement Parts A--F](Yin_C_G0199_v3.md#statement) remain part of this version at their exact original domains: in particular UP needs unique unsaturation but no zero-Haar hypothesis, whereas the actual unit gate uses zero Haar and an unsaturated phi without requiring uniqueness.
The following new conclusions use BOTH additional hypotheses:

    I_can=0,
    ord_phi R<ord_phi U,
    ord_psi R>=ord_psi U
                    for every irreducible psi|U, psi!=phi.

The zero R, whose factor orders are infinite, cannot satisfy these conditions.
No bound on degree or Mahler measure is imposed.

### A. Maximal common Frobenius power and actual normalized units

The complete inherited factorization and exponent are

    U=X^A phi^(7A) product_i Q_i^(B_i),
    A>=2, B_i>=2, ord_phi R=6A,

where the Q_i are ALL distinct remaining monic irreducibles, different from X and phi.
Put

    k=min{v_2(A), v_2(B_i) for all i}, q=2^k,
    A_0=A/q, B_i0=B_i/q,
    H_0=X^(A_0) product_i Q_i^(B_i0),
    U_0=H_0 phi^(7A_0),
    R_0=rem_(U_0)(U_0(chi)^3), chi=X phi^2.

For an empty product take k=v_2(A); that case is excluded by the inherited odd-support theorem under the actual hypotheses.
Here q is an integer Frobenius power, not the value Phi(x) denoted q in the v3 selected-root proof.
Then A_0 is even and at least2, U=U_0^q, R=R_0^q!=0, and q is the maximal common Frobenius power of each polynomial.
In particular R_0 is not a square and deg R_0<deg U_0.

In O_loc=F_2[X]_(phi), define

    Psi=phi(chi), J_0=product_i Q_i(chi)^(B_i0),
    C_00=X^(A_0)J_0 Psi^(7A_0),
    V_0=R_0/phi^(6A_0), D_0=V_0+C_00^3.

Their original counterparts are H=H_0^q, C_0=C_00^q and V=V_0^q, with D=D_0^q and D_0 in phi^(A_0) O_loc.
All are reductions of the same original input; no normalized characteristic-zero realization is asserted.

### B. Exact original-layer gate after normalization

The zero-Haar factorization retains every original integer cyclotomic multiplicity.
For m>=3 write Phi_m(z)=z^(phi(m)/2)F_m(z+z^(-1)), where phi(m) is Euler's totient, and factor the SAME G as

    G=V_int product_(b>=0) F_(2^b*5)^(a_b),
    V=V_int mod2,
    lambda_0=lambda_1=1,
    lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=6qA_0.

The factor V_int includes the sign and all other odd-order factors, including the m=1,2 endpoint factors whose cyclotomic multiplicities are even.
Each occurring lambda_b is strictly below6qA_0.
With these original integers a_b and original indices, put

    S_star=sum_(a_b odd, lambda_b>2qA_0)
          X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                       phi^(6A_0-lambda_b/q),
    L_star=sum_(a_b odd, lambda_b>2qA_0)
          X^(lambda_b/(4q))(X+1)^(lambda_b/(2q))
                       phi^(3A_0-lambda_b/(2q)).

All displayed exponents are nonnegative integers, S_star=L_star^2, and empty sums are allowed.
These formulas do not require q to divide a_b and do not assign freely relabeled normalized cyclotomic multiplicities.
Let Z_0 be the unique unit class satisfying

    Z_0^11=H_0 C_00^2 modulo phi^(3A_0).

The original full UJ gate is EXACTLY equivalent to

    Z_0D_0+H_0V_0S_star=0 modulo phi^(4A_0).

This condition is necessary, not sufficient for the characteristic-zero original residual system.
Any lift of Z_0 gives the same condition.
The old support relation also descends exactly to

    H_0^6/C_00^21=1 modulo phi^(4A_0).

Under that old relation, the normalized gate is equivalent to the conjunction

    S_star in phi^(A_0) O_loc,
    V_0=[Z_0^3/(1+(Z_0^5/C_00)L_star)]^2
                                      modulo phi^(4A_0).

The denominator is a unit, and the3A_0 root precision is used at4A_0 only after the additional A_0 divisibility has been paid.

### C. Nontrivial actual odd part and complete low-degree complement

The normalized gate implies ord_phi V_0'>=4A_0.
Write uniquely V_0=J_G0^2 W_G0 with W_G0 monic and squarefree.
Then

    W_G0 is nonconstant,
    ord_phi W_G0'>=4A_0,
    deg W_G0>=8A_0+1.

For every odd order n!=5, each complete order group Omega_n occurs in W_G0 precisely when the common integer nu_n/q is odd; X occurs precisely when nu_1/q is odd.
The divisibility q|nu_n follows from R=R_0^q, not from divisibility of the individual original integers a_b.
The nonsquare conclusion concerns V_0; the original V may already be a square when q>1.

There is also a unique monic polynomial B such that

    R_0=H_0 phi^(6A_0)B,
    V_0=H_0B, phi not dividing B,
    0<=deg B<2A_0.

This B includes EVERY surplus multiplicity at saturated factors and every extra factor of R_0, with reduction degree drop allowed.
Consequently ord_phi(H_0B)'>=4A_0 and H_0B is not a square.
These assertions give no upper bound on deg H_0 and do not identify W_G0 with the T-support odd part W_U.
The large W_G0 degree is not a proved lower bound on deg B or an automatic payment of the unique phi deficit.
No overall exclusion, actual realization, smaller original field, new all-degree Haar transfer or stronger Mahler gap is asserted.

<a id="argument"></a>
## Complete new normalized proof and fixed predecessor reuse

The common domain, complete original factorization and prior conclusions use [physical v3](Yin_C_G0199_v3.md#argument) exactly, with the narrower interfaces listed under [exact inputs](#exact-inputs).
All UR1--UR12 references below mean their fixed v3 occurrences; all UP references mean the fixed v3 UP1--UP11 proof.
The earlier source and independent-review scopes are inherited only as declared there.
The following UR13--UR23 argument is retained completely from its author draft, with fixed-input links, current review-status wording and a unit-label clarification.
The latter distinguishes the units H_0,C_00,V_0 from D_0 in phi^(A_0); no formula, hypothesis or proof step changes.

<a id="normalized-common-frobenius-unit-gate"></a>
## Exact Frobenius descent when phi is the unique unsaturated factor

Date: 2026-10-20T16:26.
Human author Yin.
Root proposed extracting the entire UJ/UR gate by the maximal common Frobenius power, then combining it with the UP nonsquare conclusion.
The entropy_attainment_bridge agent checked and supplies the complete descent, original integer-multiplicity bookkeeping, truncation precision and conditional consequence below.
Root also supplied the final low-degree complement identity; the agent checked its exact divisibility and degree scope.
Both are contributors to this new author deduction, which is not an independent review of its inputs.
No new source, mathematical program or finite search is used.

Retain ALL the actual original-input and zero-Haar hypotheses of [physical v3 UR1--UR2](Yin_C_G0199_v3.md#cyclotomic-unit-gate-reuse-scope), and add its [precise unique-unsaturated hypothesis UP2](Yin_C_G0199_v3.md#unique-quadratic-unsaturated-frobenius-parity):

    ord_phi R<ord_phi U,
    ord_psi R>=ord_psi U
                  for every irreducible psi|U, psi!=phi.
                                                           (UR13)

The complete UP1--UP11 account is fixed in physical v3, which is still unreviewed at this revision; it is not treated as an independently reviewed theorem.
Its exact monic-remainder and degree arguments are used at their stated scope; the adopted C197 odd-support input retains its existing R477 evidence.
The UJ original-unit window remains the [fixed v3 author input](Yin_C_G0199_v3.md#quadratic-zero-haar-mod4-unit-jet); its new proof also awaits the whole-chain independent review.
Thus the deduction is also a conditional finite-ring theorem under these explicitly stated interfaces, without promoting their review status.

Write the complete original reduction and its maximal common Frobenius power as

    U=X^A phi^(7A) product_i Q_i^(B_i),
    k=min{v_2(A), v_2(B_i) for all i}, q=2^k,
    A_0=A/q, B_i0=B_i/q,
    H_0=X^(A_0) product_i Q_i^(B_i0),
    U_0=H_0 phi^(7A_0), U=U_0^q.               (UR14)

For an empty extra product the minimum is v_2(A).
The phi exponent adds no smaller power because7 is odd.
UP5, using the adopted C197 odd-support theorem, gives A_0 even and positive, hence A_0>=2, and excludes that empty product under the actual hypotheses.
At least one B_i0 is odd, and its full irreducible factor belongs to the distinct T-support polynomial W_U.
These valuations concern integer exponents, not primes of the original number field.

By actual monic Euclidean division, set

    R_0=rem_(U_0)(U_0(chi)^3).

Raising the division identity to the q-th power and using the strict remainder degree gives exactly

    R=R_0^q!=0, deg R_0<deg U_0,
    ord_phi R_0=6A_0,
    R_0 is not a square.                        (UR15)

The last assertion is the UP whole-degree conclusion: if R_0 were square, every odd B_i0 would require at least one additional copy of Q_i in its saturated remainder multiplicity, costing deg W_U>=2A_0+1 against the sole deficit2A_0.
Additional remainder factors only add nonnegative cost.
No particular distribution of the extra factors of R is assumed.
Consequently q is the maximal common Frobenius power of R as well as of U; if q>1, R itself is already a square, so the nonsquare assertion applies only to R_0.

Define the normalized quantities by

    J_0=product_i Q_i(chi)^(B_i0),
    C_00=X^(A_0) J_0 Psi^(7A_0),
    E_0=H_0 C_00^2,
    F_0=H_0^6/C_00^21,
    V_0=R_0/phi^(6A_0),
    D_0=V_0+C_00^3.                             (UR16)

Here F_0 denotes a normalized rational function in the local ring, not a number field or the earlier defect coordinate.
The exact order in(UR15) makes V_0 a polynomial unit at phi.
The definitions and(UR15) imply the actual equalities

    H=H_0^q, C_0=C_00^q, E=E_0^q,
    F_old=F_0^q, V=V_0^q, D=D_0^q.

For V, use R=phi^(6A)V and injectivity of Frobenius after dividing the exact common phi factor.
Since D lies in phi^A, D_0 lies in phi^(A_0).
These are identities of reductions of the SAME original data, not constructions of a smaller actual trace field or a new original polynomial input.

### The correction polynomial retains the original integer multiplicities

Keep the original nonnegative integers a_b and their original layer indices b from(UR2).
They satisfy sum_b a_b lambda_b=6qA_0.
There is no assertion that q divides any individual a_b.
In the sum for S, each occurring layer has a_b odd and lambda_b>2qA_0.
Since lambda_b is a power of2 and A_0>=2, q divides lambda_b and lambda_b/q is a power of2 at least8.
Moreover lambda_b<6qA_0, as in the original UJ budget.
Define, using EXACTLY those original indices and parity coefficients,

    S_star=sum_(a_b odd, lambda_b>2qA_0)
           X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                           phi^(6A_0-lambda_b/q).
    S=S_star^q.                                (UR17)

The equality follows term by term and from additivity of the q-th power in characteristic two.
All displayed exponents are nonnegative integers, with the phi exponent positive.
Every exponent in each term of S_star is even, so S_star is itself a square:

    S_star=L_star^2,
    L_star=sum_(a_b odd, lambda_b>2qA_0)
           X^(lambda_b/(4q))(X+1)^(lambda_b/(2q))
                           phi^(3A_0-lambda_b/(2q)).

The two coincident small layers b=0,1 remain outside this window.
No reindexing is needed; in particular(UR17) does not posit a new cyclotomic factorization with multiplicities a_b/q or freely chosen normalized odd layers.
The original integer factorization fixes the parity list in this formula, even though only its characteristic-two correction is being normalized.
An empty sum is allowed and gives S_star=L_star=0.

### Unique root lifts and the complete error modulus

Let Z_0 be the unique unit eleventh root

    Z_0^11=E_0 modulo phi^(3A_0).                (UR18)

Existence and uniqueness use exactly the finite local unit-group argument preceding(UR3), now at3A_0.
Choose any polynomial lift of this class.
Then

    (Z_0^q)^11-E=(Z_0^11-E_0)^q
                                      is divisible by phi^(3qA_0).

Uniqueness at3A implies that Z_0^q represents the original class Z modulo phi^(3A).
It is therefore a permitted lift in the original gate.
Changing Z by phi^(3A) changes ZD only by phi^(4A), because D has order at least A.
Similarly changing Z_0 by phi^(3A_0) changes the normalized product Z_0D_0 only by phi^(4A_0).
Thus neither passage introduces an unpriced lift choice.

Substitution of this lift and(UR16)--(UR17) gives the exact polynomial identity

    Z_0^q D+HVS
       =(Z_0 D_0+H_0 V_0 S_star)^q.

For any local-ring element K, ord_phi(K^q)=q ord_phi K, including the value infinity when K=0.
Consequently the ENTIRE original unit-window gate is equivalent to

    Z_0D_0+H_0V_0S_star=0 modulo phi^(4A_0).
                                                           (UR19)

This divides the full error modulus4A by q; it does not infer a stronger modulus from an approximation.
Likewise F_old-1=(F_0-1)^q, so the inherited support condition is equivalent to F_0=1 modulo phi^(4A_0).
There is no need to take a q-th root of an arbitrary residue-class error: all expressions being compared have already been proved to be actual q-th powers in the local ring.

<a id="normalized-actual-unit-odd-part"></a>
### The normalized square condition has no globally square alternative

Apply the [exact fixed v3 algebra of UR3--UR9](Yin_C_G0199_v3.md#old-support-sixth-power-equivalence) with A_0,H_0,C_00,Z_0,V_0,D_0,S_star.
All required hypotheses were checked above: A_0 is even, D_0 has order at least A_0, S_star=L_star^2, the eleventh-root precision is3A_0, and the old support condition holds at4A_0.
For clarity the resulting steps are

    Z_0^6=C_00^3 modulo phi^(4A_0),
    S_star in phi^(A_0),
    V_0=[Z_0^3/(1+(Z_0^5/C_00)L_star)]^2
                                      modulo phi^(4A_0),
    ord_phi V_0'>=4A_0.                         (UR20)

The second line follows first from(UR19), not from an assumed cancellation.
It makes the denominator in the third line a unit and pays the missing A_0 orders when the3A_0-precision identity H_0/Z_0=Z_0^10/C_00^2 is used.
The particular square displayed here is still determined by the full actual gate, and a derivative condition alone is not sufficient for that gate.

Write the unique complete odd-multiplicity decomposition

    V_0=J_G0^2 W_G0,
    W_G0 monic and squarefree, phi not dividing J_G0 W_G0.

Since R_0=phi^(6A_0)V_0 and6A_0 is even, (UR15) shows V_0 is NOT a square.
Hence W_G0 is nonconstant, and its derivative is nonzero.
As J_G0 is a unit at phi, differentiation and(UR20) give

    ord_phi W_G0'=ord_phi V_0'>=4A_0,
    deg W_G0'>=8A_0,
    deg W_G0>=8A_0+1.                           (UR21)

Unlike the unrestricted alternative(UR12), the branch W_G0=1 is now excluded, but only by the ADDITIONAL unique-unsaturated hypothesis and the UP proof.
If q>1, V=V_0^q can nevertheless be a square; the new conclusion concerns V_0 and does not contradict that original square branch.

The actual uniform order multiplicities remain complete after normalization.
For each odd order n other than5, the original equal multiplicity nu_n of all irreducible factors in Omega_n is divisible by q because V=V_0^q.
Their multiplicities in V_0 are the common integers nu_n/q.
The same assertion applies to X, the order-one trace factor.
Thus W_G0 contains an ENTIRE Omega_n exactly when nu_n/q is odd, and X exactly when nu_1/q is odd.
This divisibility follows from the exact canonical Frobenius identity, not from divisibility by q of the separate characteristic-zero a_b.
W_G0 is still distinct from the T-support polynomial W_U of UP5; no equality of the two polynomials has been assumed or proved.

<a id="normalized-low-degree-complement"></a>
## The exact low-degree complement and the remaining budget boundary

Saturation in(UR13), after division of every factor multiplicity by q, gives H_0|R_0 in F_2[X].
It is coprime to phi, while the exact phi order of R_0 is6A_0.
Therefore there is a unique monic polynomial B such that

    R_0=H_0 phi^(6A_0) B,
    phi not dividing B,
    V_0=H_0 B,
    0<=deg B<2A_0.                              (UR22)

The strict degree bound follows by subtracting the COMPLETE degrees:

    deg R_0=deg H_0+12A_0+deg B
       <deg U_0=deg H_0+14A_0.

The polynomial B may equal1.
It contains every extra factor of R_0 outside U_0 and every surplus multiplicity at the saturated factors; none is omitted from its degree.
This argument is valid with reduction degree drop and does not assume equality of the saturated multiplicities.
It uses only exact saturation and the canonical remainder degree, not an auxiliary choice of a representative.

Combining(UR20)--(UR22), this conditional original-input class must satisfy

    ord_phi(H_0 B)'>=4A_0,
    H_0 B is not a square,
    deg(odd_multiplicity_part(H_0 B))>=8A_0+1,
    deg B<2A_0.                                 (UR23)

The displayed degree comparison does not establish a contradiction: the hypotheses provide no upper bound on deg H_0.
In particular the large degree of the actual G-unit odd part is not a proved lower bound on the surplus degree deg B, and cannot be substituted for it.
The T-support polynomial W_U and the actual G-unit polynomial W_G0 may differ through the very surplus and extra factors collected in B.
No equality W_G0=W_U, no automatic payment of the unique phi deficit, and no global impossibility theorem is asserted.
The exact normalized gate(UR19), rather than its derivative consequence alone, remains required.

This section closes only the common-Frobenius normalization and its stated parity, derivative and low-degree-complement consequences.
It does not construct a smaller characteristic-zero input realizing U_0, R_0 or S_star, does not change the original fields or norm weights, and does not establish a stronger Mahler/Haar transfer.
Its necessary inputs are precisely the full UJ window and original multiplicities, the actual UR1--UR12 equivalences, the complete UP1--UP11 unique-unsaturated proof, and the fixed C197/C199 interfaces identified above.
The higher-adic original feasibility and any contradiction using the full normalized gate are separate unresolved obligations.

<a id="exact-inputs"></a>
## Exact inputs and pending whole-chain review

| Input | Exact scope |
| --- | --- |
| [Physical v3 complete statement and proof](Yin_C_G0199_v3.md#argument) | Retained Parts A--F at their separate original domains, exact original fields, nonzero divided trace quotients, complete cyclotomic product, and all original scalar/norm costs. Its new mathematical blocks are still unreviewed at this revision. |
| [v3 complete UJ window](Yin_C_G0199_v3.md#quadratic-zero-haar-mod4-unit-jet) | Actual original cyclotomic multiplicities a_b, lambda window, all higher-lift and local errors, D in phi^A, unique Z at3A, and full gate at4A. No arbitrary V or formal lift replaces the actual canonical data. |
| [v3 UR equivalences](Yin_C_G0199_v3.md#old-support-sixth-power-equivalence), [specified square](Yin_C_G0199_v3.md#actual-unit-gate-square-equivalence), [actual odd part](Yin_C_G0199_v3.md#actual-g-unit-odd-part-condition) | Exact eleventh-root and sixth-power precision, gate-to-specified-square equivalence, derivative and complete odd-multiplicity argument. These are contributor-overlapping inputs, not independently re-reviewed here. |
| [v3 UP1--UP11](Yin_C_G0199_v3.md#unique-quadratic-unsaturated-frobenius-parity) | Exact maximum q, canonical monic remainder identity, whole-support saturation and degree costs, R_0 nonsquare, empty-product and reduction-degree limits; no zero-Haar hypothesis is imported into the broader UP theorem. |
| [C197v3 odd-support theorem](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Adopted A_0 even, at least one odd B_i0 and full W_U degree after maximal common extraction; used through the v3 UP proof at its precise scope. |
| [Actual R477](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Independent coverage of C197v3 despite the present authors' upstream contributions; no coverage of new v3 UJ/UR/UP or present normalization. |
| [Actual R483](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding) | Independent coverage of physical v2 and its complete uniform order multiplicities only; not a review of v3 or v4. |

The original author location of UR13--UR23 was D40 at2026-10-20T16:26; that location is extraction provenance, not a logical premise.
All necessary new reasoning is present above, and the needed predecessor arguments are in the exact physical C199v3 anchors.
Root and entropy_attainment_bridge contribute to this version and to the earlier UR/C197 proof; root and draft_inventory_later contribute to UP and UJ.
The root's author readback and this agent's checks supply no independent finding.
A whole-chain independent review must cover v3's new arguments and this version's use of them, in addition to the new normalized deduction.
The previous R477/R483 and earlier adopted C199 decisions remain at their actual old scopes and do not adopt these two new physical versions.
No new source inspection is claimed; the original source definitions and audit limits stay with the v3/v2 dependencies.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-21)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T16:31 |
| status | open |
| reason | Complete substantive continuation of the same actual zero-Haar inquiry: preserve UR13--UR23 common-Frobenius descent of the full original unit gate, actual integer-layer parity, root/error precision, nonsquare normalized unit and complete low-degree complement. Physical v3 remains unreviewed and is an explicit exact prerequisite; whole-chain independent review is required before adoption. No global exclusion or original realization is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete normalized theorem](#statement) | Common actual residual domain; retain all v3 conclusions at their distinct scopes; new conclusions require BOTH zero Haar and unique unsaturated phi, including all original multiplicities, full normalized congruence, nontrivial W_G0 and complete B degree. |
| argument | [Complete UR13--UR23 proof](#argument) | Full new normalization and exact fixed predecessor reuse, all lift/error precision, original a_b parity, actual polynomial Frobenius, nonsquare argument, derivative degree and saturation complement. |
| dependency | [Physical v3 theorem chain](Yin_C_G0199_v3.md#argument) | Complete retained conclusions and all original definitions/costs, with new v3 blocks still unreviewed at this revision; no mutable selector or draft premise. |
| dependency | [Original UJ gate](Yin_C_G0199_v3.md#quadratic-zero-haar-mod4-unit-jet) | Exact actual unit-window gate, every original dyadic multiplicity and higher-adic error, D divisibility and unique-root precision; not an arbitrary characteristic-two unit condition. |
| dependency | [Exact old support equivalence](Yin_C_G0199_v3.md#old-support-sixth-power-equivalence) | UR3--UR4 root precision and old F equivalence, reused with A_0. |
| dependency | [Full specified-square conversion](Yin_C_G0199_v3.md#actual-unit-gate-square-equivalence) | UR5--UR9, including S divisibility before the3A-to4A substitution and the exact specified square rather than just a derivative test. |
| dependency | [Whole canonical parity](Yin_C_G0199_v3.md#unique-quadratic-unsaturated-frobenius-parity) | UP1--UP11 exact maximal common Frobenius, original remainder and nonsquare conclusion with every saturated and extra factor paid. |
| support | [Inherited actual odd part](Yin_C_G0199_v3.md#actual-g-unit-odd-part-condition) | UR10--UR12 factorization, full cyclotomic order groups and derivative degree mechanism; its formerly possible square branch is excluded only after adding the unique-unsaturated UP input. |
| support | [Adopted odd-support interface](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Exact A_0 parity and W_U degree used through UP, with present authors' upstream contributions disclosed. |
| support | [Actual independent C197 scope](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Upstream accepted proof only; not coverage of either new C199 version. |
| support | [Actual independent C199v2 scope](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding) | Old uniform whole-order and cancellation scope only, without retrospective v3/v4 review. |
| support | [Inputs and pending chain review](#exact-inputs) | Exact fixed dependencies, contributor identities, source/review limits and outstanding whole-chain independent review; no self-adoption. |

### Decision whole-reviewed-2026-10-21

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T16:38 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the complete v4 statement, including all physical v3 conclusions at their distinct domains, through the two actual whole R489 findings. The new normalized conclusions require both zero canonical Haar and unique quadratic unsaturation; retain original a_b parity, actual q-th powers, full root/error precision, nontrivial normalized odd part and every complement cost. The large odd-part degree is not a lower bound for the complement, and no global contradiction or uniform original/Haar transfer is asserted. Physical v3 and its initial historical assessment remain preserved; this current main-material decision adopts its complete proof through the exact reviewed chain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete normalized theorem](#statement) | Common actual residual domain; retain all v3 conclusions at their distinct scopes; new conclusions require BOTH zero Haar and unique unsaturated phi, including all original multiplicities, full normalized congruence, nontrivial W_G0 and complete B degree. |
| argument | [Complete UR13--UR23 proof](#argument) | Full new normalization and exact fixed predecessor reuse, all lift/error precision, original a_b parity, actual polynomial Frobenius, nonsquare argument, derivative degree and saturation complement. |
| dependency | [Physical v3 theorem chain](Yin_C_G0199_v3.md#argument) | Complete retained conclusions and all original definitions/costs, with all new v3 blocks independently covered by the separate whole-v3 R489 finding; no mutable selector or draft premise. |
| dependency | [Original UJ gate](Yin_C_G0199_v3.md#quadratic-zero-haar-mod4-unit-jet) | Exact actual unit-window gate, every original dyadic multiplicity and higher-adic error, D divisibility and unique-root precision; not an arbitrary characteristic-two unit condition. |
| dependency | [Exact old support equivalence](Yin_C_G0199_v3.md#old-support-sixth-power-equivalence) | UR3--UR4 root precision and old F equivalence, reused with A_0. |
| dependency | [Full specified-square conversion](Yin_C_G0199_v3.md#actual-unit-gate-square-equivalence) | UR5--UR9, including S divisibility before the3A-to4A substitution and the exact specified square rather than just a derivative test. |
| dependency | [Whole canonical parity](Yin_C_G0199_v3.md#unique-quadratic-unsaturated-frobenius-parity) | UP1--UP11 exact maximal common Frobenius, original remainder and nonsquare conclusion with every saturated and extra factor paid. |
| support | [Inherited actual odd part](Yin_C_G0199_v3.md#actual-g-unit-odd-part-condition) | UR10--UR12 factorization, full cyclotomic order groups and derivative degree mechanism; its formerly possible square branch is excluded only after adding the unique-unsaturated UP input. |
| support | [Adopted odd-support interface](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Exact A_0 parity and W_U degree used through UP, with present authors' upstream contributions disclosed. |
| support | [Actual independent C197 scope](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Upstream accepted proof only; not coverage of either new C199 version. |
| support | [Actual independent C199v2 scope](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding) | Old uniform whole-order and cancellation scope only, without retrospective v3/v4 review. |
| support | [Inputs and pending chain review](#exact-inputs) | Exact fixed dependencies, contributor identities and original source/review limits, with the initially pending whole-chain review now supplied by both actual R489 findings. |
| review | [Whole v3 independent finding](../audits/reviews/Yin_R_G0489_v1.md#cyclotomic-unit-v3-whole-chain-finding) | Complete inherited actual v3 Parts A--F, CC9/DL/UJ/UR1--UR12/UP and all twelve dependencies/nine supports, distinct domains, critical cancellation, original local and global weights, full coefficient errors, source/contributor evidence and noncoverage limits. |
| review | [Whole v4 independent chain finding](../audits/reviews/Yin_R_G0489_v1.md#normalized-unit-v4-whole-chain-finding) | Entire actual v4 statement and UR13--UR23, all five dependencies/five supports and complete use of physical v3, preserving every original multiplicity, lift, precision, parity and whole complement expense; no proof repair or reviewer contribution. |


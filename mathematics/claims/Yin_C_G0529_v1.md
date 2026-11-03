---
author: Yin
---

# Conditional sharp-profile transfer to complete actual finite-tail pressure

The unconditional hyperbolic full-tail exponent already has the sufficient stronger [C310 home](Yin_C_G0310_v1.md#statement), including sublinear prefixes; it is reused rather than registered again.
This C retains the distinct complete conditional theorem from [L286 Section3](../ledger/Yin_L_G0286_v1.md#conditional-sharp-profile-transfer), with its unproved premise explicit.
The original fixed proof, bounded C1 experiments, source search, author check and R185 input remain in L286/J71 and their responsible review homes.

## Statement and actual finite-prefix definitions

<a id="statement"></a>

Let alpha be any actual nonzero algebraic integer with monic minimal P of degree d>=1, m=log M(P), and full power basis1,alpha,...,alpha^(d-1).
Neutral conjugates, torsion and nonunits are allowed.
Let M be multiplication by alpha, v the coordinate vector of1, z_j=-M^(d+j)v, A_i=[z_0,...,z_(i-1)], W_i=(I+A_i A_i^T)^(-1), D_i=det(W_i)^(-1), D_0=1.
For integers i>=0,b>=d, let X=[z_i,...,z_(i+b-1)], Q=XX^T>0 and W_(i+b)=(W_i^(-1)+Q)^(-1).
Use independent original digits xi_j with probabilities1/4,1/2,1/4 on-1,0,1, mu(z)=Pr(Xxi=z), p_b=mu(0), a=log2 and

    G_(i,b)(u)=exp[a u^T W_(i+b)u]
                 E exp[-a(Xxi+u)^T W_i(Xxi+u)],
    K_d=2^(d/4)(2pi/log2)^(d/2).

If the sharp profile

    mu(z)<=p_b exp[-a z^T Q^(-1)z]                    (C1)

holds at every attained integer endpoint z of this specified X, then

    p_b<=G_(i,b)(0)<=sup_(u in R^d)G_(i,b)(u)
          <=K_d sqrt(D_i)p_b.

The upper bound pays the full positive completion factor and is uniform over the entire actual finite real-tail span; it does not identify the bounded-digit tail set with that span.
For any fixed P and integer prefix sequence i_b>=0 with i_b=o(b), if C1 holds for every required actual X_(i_b,b), then the complete supremum has limit exponent h2(P).
The same squeeze applies to a selected actual tail collection containing zero.
For i>=1 the complete logarithmic expense is at most

    log K_d+m i+(d/2)log(i+d)
                    -(1/2)log|disc P|+m(d-1),

while i=0 uses D_0=1 directly.
The sharp profile for unrestricted overlapping relations remains unproved by this argument; finite J71 passes and the proved half-profile with coefficient1/2 do not establish its premise.
No uniform-in-P bound, neutral unrestricted-tail theorem without C1, h2=m(P), efficient computation or positive Mahler gap is asserted.

## Complete retained conditional argument

<a id="argument"></a>

<a id="conditional-sharp-profile-transfer"></a>
### 3. Exact conditional transfer from the stronger profile

This is the precise conditional payoff of the unproved sharp profile C1; it does not use the separate hyperbolic proof.
Take the actual minimal polynomial P of any nonzero algebraic integer alpha (including neutral roots, torsion and nonunits), any i>=0 and b>=d.
Work now in the ORIGINAL INTEGER POWER BASIS, so X and every endpoint z=Xxi are integral.
Suppose(C1) holds for this particular X:
    mu(z)<=p_b exp[-a z^T Q^(-1)z],  Q=XX^T>0.          (10)
Then the following exact full-tail estimate follows:
    p_b<=sup_u G_(i,b)(u)<=K_d sqrt(D_i)p_b.             (11)
The upper bound is independent of u; no extra unknown root cost is concealed.

Put H0=W_i+Q^(-1) and c=-H0^(-1)W_i u.
Direct square completion gives
    (z+u)^T W_i(z+u)+z^T Q^(-1)z
       =(z-c)^T H0(z-c)+u^T W_(i+b)u.                 (12)
The constant identity is W_i-W_i H0^(-1)W_i=(W_i^(-1)+Q)^(-1).
Multiply the bound(10) by the actual Gaussian and the positive prefactor; (12) cancels that prefactor EXACTLY.
Enlarging the nonnegative sum from the actual integer support gives
    G_(i,b)(u)<=p_b sum_(z in Z^d) exp[-a(z-c)^T H0(z-c)]
               <=p_b sum_(z in Z^d) exp[-a(z-c)^T W_i(z-c)]
               <=K_d sqrt(D_i)p_b.                    (13)
For the last inequality the [complete current unit-cube proof](Yin_C_G0517_v1.md#finite-prefix-schur-remainder) applies to cubes centered at z-c: they still tile R^d, have volume1, and W_i<=I.
This proves the translated bound with the same K_d.
The lower bound uses the zero endpoint at u=0.

If C1 holds for all required actual X_(i_b,b), then [the complete current determinant cost](Yin_C_G0517_v1.md#finite-prefix-schur-remainder) implies the full-tail exponent h2 for every FIXED P and i_b=o(b), including all neutral-root cases.
The precise finite cost for i>=1 remains
    log K_d + m i +(d/2)log(i+d) -(1/2)log|disc P| +m(d-1).
The i=0 direct determinant1 case is included separately.
This is a conditional implication; neither the scalar nor the two-dimensional finite [J71 evidence](../computations/programs/Yin_J_G0071/readme.md) establishes its premise.
The weaker coefficient1/2 from L251/L255 does not give the exact cancellation(12) at a=log2.
There is no uniform near-one gap conclusion even if(C1) is eventually proved.


## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:04 |
| status | open |
| reason | Register the exact conditional theorem and its complete retained proof; the unrestricted sharp-profile premise stays unresolved, while whole internal checking of this implication and its interfaces follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conditional statement](#statement) | Every original digit, actual full-rank power-basis map, positive finite completion, integer endpoint, conditional domain and full fixed-input cost above. |
| argument | [Complete conditional proof](#argument) | Original whole square completion, exact positive-factor cancellation, translated integer-cube bound and fully paid sublinear-prefix implication, with C1 explicitly assumed. |
| dependency | [Complete actual finite geometry](Yin_C_G0517_v1.md#finite-prefix-schur-remainder) | Exact integer remainder columns, Schur formula, original zero atom, unit-cube constant, all-root determinant cost and original collision limit. |
| support | [Adequate unconditional hyperbolic theorem](Yin_C_G0310_v1.md#statement) | Separate already accepted stronger hyperbolic/all-prefix result; it is not a proof of C1 or an input needed by this conditional argument. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:09 |
| status | proved |
| reason | Adopt the complete exact statement and complete retained argument after actual whole current SELF. Original findings, dates, source/native boundaries and unresolved questions remain separate; no isolated review, original proof repair, native execution or research Task/E is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact current statement](#statement) | Exact sharp-profile conditional implication on all specified actual maps, full real-tail completion and fully paid sublinear prefixes; C1 itself stays unproved. |
| argument | [Complete retained proof](#argument) | Entire original conditional Section3: exact square completion/positive-factor cancellation, translated-cube constant and determinant/limit costs, under the explicit C1 premise. |
| dependency | [Complete actual finite geometry](Yin_C_G0517_v1.md#finite-prefix-schur-remainder) | Exact integer remainder columns, Schur formula, original zero atom, unit-cube constant, all-root determinant cost and original collision limit. |
| support | [Adequate unconditional hyperbolic theorem](Yin_C_G0310_v1.md#statement) | Separate already accepted stronger hyperbolic/all-prefix result; it is not a proof of C1 or an input needed by this conditional argument. |
| review | [Actual complete current whole SELF](../audits/reviews/Yin_R_G0734_v1.md#current-conditional-profile-whole-self-finding) | Exact sharp-profile conditional implication on all specified actual maps, full real-tail completion and fully paid sublinear prefixes; C1 itself stays unproved. Entire original conditional Section3: exact square completion/positive-factor cancellation, translated-cube constant and determinant/limit costs, under the explicit C1 premise. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:42 |
| status | proved |
| reason | Adopt the unchanged complete statement and written argument through the separately arranged isolated whole inspection completed at 2026-10-22T20:32; old findings keep their actual original inputs, relationships, dates and source/native limits. This decision performs no proof repair, native run or research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact current statement](#statement) | Exact sharp-profile conditional implication on all specified actual maps, full real-tail completion and fully paid sublinear prefixes; C1 itself stays unproved. |
| argument | [Complete retained proof](#argument) | Entire original conditional Section3: exact square completion/positive-factor cancellation, translated-cube constant and determinant/limit costs, under the explicit C1 premise. |
| dependency | [Complete actual finite geometry](Yin_C_G0517_v1.md#finite-prefix-schur-remainder) | Exact integer remainder columns, Schur formula, original zero atom, unit-cube constant, all-root determinant cost and original collision limit. |
| support | [Adequate unconditional hyperbolic theorem](Yin_C_G0310_v1.md#statement) | Separate already accepted stronger hyperbolic/all-prefix result; it is not a proof of C1 or an input needed by this conditional argument. |
| review | [Actual isolated whole written finding](../audits/reviews/Yin_R_G0769_v1.md#whole-current-independent-finding) | Entire exact current statement and complete argument, including every actual class, fixed-input interface, original-law/degree/cost control and stated negative or unresolved boundary; no new native execution or original source-proof audit. |


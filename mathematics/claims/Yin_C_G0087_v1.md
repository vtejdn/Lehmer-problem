---
author: Yin
---
# Full-order three-power saturation and legal small-block constant-delay rigidity

Date: 2026-10-12T17:27.
Human author Yin.
Fixed extraction under the continuing original G0001 instruction.
Root authored ALL new D41 mathematics and controls, including the later three-power automatic independence and resolved mixed-word theorem.
The g0001_matrix_recovery AI independently whole-reviewed the actual complete01:16 final D41 in R315 and NOW authors this statement, decision and extraction wrapper.
It is a contributor to this new artifact and cannot supply its independent extraction review.
A separate noncontributor must actually inspect this registered Claim.
The ENTIRE original candidate, conditional development, proof, controls, source/role boundaries and final freeze are retained below.

## Statement

Let alpha be an ACTUAL nontorsion algebraic integer unit of original degree d>=2, with monic irreducible minimal polynomial P, total logarithmic Mahler measure m=m(P)>0, K=Q(alpha) and nu=Norm_(K/Q)(alpha) in{+1,-1}.
Reciprocity is not assumed.
Let O be ANY specified full order in K containing alpha; it then contains alpha^-1.
All norms use ALL d original embeddings.
Write O0=Z[alpha].

Keep the adopted functions and exact numerical constant

    c0=log2/4, h0=c0 exp(-20),
    b0(u)=max{u,sqrt(u/c0)log(sqrt(c0/u))},
    epsilon(u)=min{1,15sqrt(b0(u))+4u}, 0<u<=h0,
    K0=c0/[2*36^8*5^64],
    K0<h0/2, K0<1/20,
    exp(2K0)[4/5+8epsilon(K0)+32K0]<1.

Every occurrence of epsilon has POSITIVE argument in its increasing domain.
Zero width is treated exactly.

**A. Full-order saturation of at most THREE powers, with automatic independence.**
For1<=r<=3 distinct integers a_1,...,a_r, put A=max a_i-min a_i.
If A*m/d<=K0, then these powers are Q-linearly independent and

    O intersect span_Q{alpha^(a_i):1<=i<=r}
        =sum_(i=1)^r Z*alpha^(a_i).

The one-power saturation is unconditional in the exponent and the two-power independence is automatic for every nontorsion unit.
The conclusion is uniform in rational coefficient denominators, the index of O over O0 and absolute exponent sizes apart from their spread.
Theorem1 in the retained development first proves the saturation with explicit independence; the later Section7 proves that independence automatically at the stated threshold.
That earlier condition is RESOLVED here, not an open premise of this final statement.

More precisely, a dependence among three DISTINCT powers normalizes to

    A0+B0*alpha^h+C0*alpha^k=0,
    A0,B0,C0 in Q minus{0}, 0<h<k,

where k is its actual span.
If P is NONRECIPROCAL, k>=d and the accepted Smy08 nonreciprocal statement gives k*m/d>=m>=log(theta0)>K0, where theta0>1 solves theta0^3-theta0-1=0.
This uses the TOTAL measure, not m/d.
If P is RECIPROCAL, u=alpha^h has

    u+u^-1=(C0^2-A0^2-B0^2)/(A0*B0)=n in Z,
    abs(n)>=3, [Q(u):Q]=2,
    M(u)=(abs(n)+sqrt(n^2-4))/2>2,
    h*m/d=(1/2)log M(u)>(1/2)log2>K0.

The d/2 repetitions of the two powered conjugates are retained.
For a GENUINE Salem input of degree>=4 the original circle conjugates exclude such a quadratic power altogether; hence three distinct powers are Q-independent at ANY span in that special domain.
This last independence observation does not remove the small-cost condition from the saturation theorem and is not asserted for all reciprocal units at arbitrary spans.

The analytic input to saturation is the accepted L229 estimate after clearing and canceling the SAME rational coefficient denominator: if a rational Laurent f has nonzero value, positive actual width t, squared coefficient norm S and effective support rho=(sum|coefficients|)^2/S, and0<t*m/d<=h0, then

    abs Norm_(K/Q)(f(alpha))^(2/d)
       <=S exp(2t*m/d)[1+(rho-1)epsilon(t*m/d)+4rho*t*m/d].

Rounding at most three rational coefficients to nearest integers leaves S<=3/4 and rho<=3.
Actual O membership and nonzero value give the integer-norm floor1, contradicting this upper bound at A*m/d<=K0.
This is a proof of actual order saturation, not a norm-only replacement for membership.
Four rounded coefficients need not give a strict margin, and no four-power theorem is asserted.

**B. Exact rational constant actions.**
Fix positive rational weights omega_i,omega_j and ANY rational constant2-by-2 matrix B with

    B^T diag(omega_i,omega_j) B=diag(omega_i,omega_j).

Apply it to TRUE signed monomials epsilon_i*t^a, epsilon_j*t^b, with signs in{+1,-1}.
Require both actual output values NONZERO in O and abs(a-b)*m/d<=K0.
Both TRUE output polynomials are signed monomials with exponents among{a,b}.

If a!=b, the matrix itself is an integer signed diagonal matrix, or an integer signed coordinate swap with omega_i=omega_j.
If a=b, only its actual action on the signed input column is forced to be a signed monomial column; the matrix need not be integral.
Signs may change.

More generally, a rational CONSTANT isometry of a positive diagonal metric acting on ANY finite selected set of signed monomial coordinates has only signed-monomial TRUE outputs whenever its current input uses at most THREE DISTINCT exponents of spread A with A*m/d<=K0 and every actual output is NONZERO in O.
Its output exponents already occur in that selected input support.
Repeated exponents do not force the entire matrix to be integral.
In particular EVERY at-most-three-coordinate constant block satisfies the exponent-count condition.
Saturation makes the collected coefficients integral, and the positive weighted coefficient-energy average1 forces each nonzero output to have exactly one coefficient+/-1.

**C. Arbitrary finite constant words and adopted binary-delay interleavings.**
Fix ANY finite N>=2 and fixed positive normalized rational weights omega_i, with ACTUAL least indexed denominator M and primitive positive copies m_i=M omega_i.
Start from TRUE signed Laurent monomials F_i^(0)=epsilon_i*t^(a_i) of common width A_init=max a_i-min a_i.

For CONSTANT-ONLY words, allow ANY finite number of the blocks in B, requiring at most three distinct current exponents in each selected block, and require EVERY intermediate actual coordinate NONZERO in the SAME full order O.
If A_init*m/d<=K0, every TRUE intermediate coordinate remains a signed monomial, its common width never increases, actual q_final=1, E=1 and

    Lambda=(1/d)sum_i omega_i log abs Norm_(K/Q)(F_i(alpha))=0,
    full surplus=Lambda-(1/2)log E=0.

For MIXED words, restrict explicitly to O0.
Allow ANY finite interleaving of those constant blocks and the actually adopted C84 primitive weighted binary delays, keeping the same labels and weights.
For the selected pair's reduced positive integer weight ratio r:s and any primitive integer direction(x,y) with BOTH entries nonzero, the permitted nonconstant factor is precisely

    S=r*x^2+s*y^2,
    Pi=(1/S)[[r*x^2,s*x*y],[r*x*y,s*y^2]],
    U_k=Id-Pi+t^k Pi, k in Z minus{0}.

These are the C84 factors, not arbitrary rational binary nonconstant matrices.
Its optional one-coordinate projection delay is also allowed.
Require EVERY actual intermediate coordinate, including unchanged ones, NONZERO in the SAME original O0.
Charge ALL delays, of either sign, by

    B_word=A_init+sum_(ALL delay steps)abs(k_j),
    U_word=B_word*m/d.

If U_word<=K0, every TRUE intermediate polynomial remains a signed monomial and actual q_final=1, E=1, Lambda=surplus=0.
The SAME K0 is uniform in N, both factor counts, all fixed positive rational weights/FINAL M, initial multiplicities and all primitive delay-direction heights.
A constant step introduces no exponent beyond its selected support; a delay increases common width by at most abs(k).
This induction uses the TRUE polynomial at each stage, not a value-equivalent replacement.

Constants may change individual signs.
The mixed theorem does not inherit original-sign invariance, copied-exponent conservation or coordinate-norm-product conservation from the delay-only theorem or a matrix determinant.
The full-order O statement applies to constant-only words; the mixed statement retains C84's O0 domain.
The earlier conditional Section5 is RESOLVED by the actual adopted C84 interface selected in Section8; no pending delay theorem is a premise of this final result.

For every fixed B_star>0, a positive-income word in this specified mixed class satisfies

    B_word<=B_star*d and Lambda>0 imply m>K0/B_star.

No input with small m or positive-income word is asserted to exist.
Small FINAL width obtained by large cumulative delay cancellation is not a substitute for the stated budget.

**D. Complete original arithmetic and physical widths.**
Before imposing small-cost rigidity, let q_B be each ACTUAL constant-matrix coefficient denominator and L_j each ACTUAL delay-matrix coefficient denominator.
Then

    q_final divides (product_constants q_B)*(product_delays L_j),
    T_final<=B_word,
    FINAL M and every positive copy m_i remain unchanged.

Divisibility is not equality.
After ONE common monomial t^b makes the true final coordinates ordinary, let D_i=Norm_(K/Q)(alpha^b F_i(alpha)) and H_i=q_final*t^b F_i in Z[t].
Then

    Res(P,H_i)=q_final^d D_i,
    product_i Res(P,H_i)^(m_i)
       =q_final^(dM)*product_i D_i^(m_i),
    sum_i omega_i ||H_i||_2^2=q_final^2,
    I_int=log q_final+Lambda,
    I_int-(1/2)log(q_final^2)=Lambda.

Every original root, content, label and full norm sign remains.
Under rigidity the RAW final norms are(epsilon_i')^d nu^(a_i') at the ACTUAL final signs/exponents; common normalization contributes nu^(bM) to the copied norm product.
The independently accepted finite covariance calculation additionally gives only Lambda<=T_final*m/d for the supplied actual packet.
It is not needed for the zero-income induction and supplies no construction.

**E. Exact controls with every cost.**
For P=t^2-t-1, alpha=(1+sqrt5)/2, d2 and nu=-1, take weights1/2,1/2, seed(1,t^5) and

    B=(1/5)[[3,4],[-4,3]],
    (g1,g2)=((3+4t^5)/5,(-4+3t^5)/5).

The actual values are3+4alpha and1+3alpha, with full signed norms5,-5.
Actual q_final5, FINAL M2, E1, T_final=A_init5, numerator resultants125,-125 and copied resultant-15625 give Lambda=surplus=(1/2)log5>0.
The scalar factor5^(dM)=5^4 and original value-norm product-25 are both retained.
Its fixed U=(5/2)log alpha>K0 is outside the exclusion; it is not a near-one family.

For ANY integer L>=2, weights1/L,(L-1)/L and input(1,1), the constant reflection

    B_L=(1/L)[[2-L,2(L-1)],[2,L-2]]

preserves the weighted metric and fixes that input.
Its ACTUAL matrix denominator is L/gcd(L,2), unbounded for odd L, while the ACTUAL output has q1, FINAL M=L, E1, width0 and zero income.
Thus a bound on the constant-matrix denominator cannot be inferred from coincident-input rigidity.

**F. Exact frontier and source scope.**
A first departure from signed monomials within a small-cost legal construction must leave the specified hypotheses: for example a constant factor may involve at least FOUR DISTINCT powers, a nonconstant factor may fall outside the adopted binary-delay class, or another fixed legality/weight/seed/budget condition may fail.
This is a necessary boundary, not a proof that any escape succeeds.
Genuinely multicoordinate nonconstant factors, changing weights/metrics, nonmonomial seeds, zero intermediate values and final-only order membership remain outside.
No general rational paraunitary matrix is asserted to have a legal factorization of the permitted kind.

The accepted Smy08 input is ONLY its retained2008 survey Section5.1 equation15, as recorded in Smy08-U002 Section1, at statement/convention/applicability scope.
There is no new1971 proof audit, equality/isolation classification or source-version substitution.
L229's Pri11/Dim19 limits are unchanged; C74 supplies the fixed numerical margin, C14 only the elementary integer coefficient-energy fact, and C84 only its actual accepted delay interface.
This proves no four-power saturation, uniform positive same-exponent income, unrestricted complementary surplus or Mahler gap.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:27 |
| status | open |
| reason | Register the final resolved three-power saturation, actual constant actions and specified legal mixed-word obstruction while retaining the ENTIRE actual01:16 D41. R315 whole-reviewed that original only; its reviewer now authors this extraction wrapper. Another noncontributor must inspect this actual statement, preserved proof and interfaces before adoption. The early explicit-independence and pending-delay conditions are resolved by the retained Sections7--8, without a four-power or unrestricted-gap extension. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F: original all-unit/full-norm domain, automatic at-most-three-power independence and saturation, full-O constant action/words, O0 mixed words, exact constants/controls/costs and limits. |
| argument | [Entire final author body](#argument) | COMPLETE actual01:16 D41, initial candidate and conditional history, Sections1--9/Theorems1--3/equations1--15, all nine anchors, later automatic-independence and adopted-input resolution, both controls, source/role accounts and freeze. |
| dependency | [L229 full coefficient-energy estimate](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Actual nonvanishing integer auxiliary and all original roots; retained proof clears/cancels the SAME rational denominator, uses positive actual width and rho<=3 within the accepted increasing domain. |
| dependency | [C74 numerical margin](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY R1 K0, h0 and1/20 bounds and strict exp(2K0)[4/5+8epsilon(K0)+32K0]<1; no older multiplicity word theorem supplies the new result. |
| dependency | [C14 coefficient spacing](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | ONLY nonzero integer-polynomial coefficient energy>=1, with equality iff signed monomial; not its short-width O0 representation theorem at enlarged order/span. |
| dependency | [Accepted nonreciprocal statement](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | STRICTLY Section1, retained2008 survey Section5.1 equation15 and reciprocal/total-measure conventions; nonzero nonreciprocal algebraic integer M>=theta0 at statement-level acceptance, not original1971 proof/equality/isolation/other unit results. |
| dependency | [Original powered-height normalization](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost) | Exact d/N repetition and h(alpha^n)=n*m/d; the new reciprocal proof also gives its actual N2 specialization locally. No upper cost is treated as arithmetic income. |
| dependency | [Adopted all-height binary delays](Yin_C_G0084_v1.md#statement) | Only actual primitive weighted binary signed delays and optional one-coordinate shifts, TRUE-polynomial classification at K0, fixed weights and all-stage nonzero O0 legality; the mixed consumer retains cumulative expense. |
| dependency | [Optional direct covariance expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Finite calculation for the supplied packet over all original roots and actual final width, giving only Lambda<=T_final*m/d, not a construction or a reciprocal-only hypothesis for this analytic use. |
| support | [Original entire whole finding](../audits/reviews/Yin_R_G0315_v1.md#three-power-whole-independent-finding) | ENTIRE actual D41 final01:16 freeze including new Sections7--9 and direct interfaces. That reviewer now authors this wrapper; R315 does not prospectively cover this extraction or adopt it. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:35 |
| status | proved |
| reason | Full-order automatic-three-power saturation, legal constant blocks and the explicitly O0 mixed-word rigidity are fixed with all original degree, norm, sign, denominator and cumulative-width conditions. Root authored this proof and relies on separate noncontributor original whole R315 and actual R424 findings. Entire original history remains. No unrestricted mathematical Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F: original all-unit/full-norm domain, automatic at-most-three-power independence and saturation, full-O constant action/words, O0 mixed words, exact constants/controls/costs and limits. |
| argument | [Entire final author body](#argument) | COMPLETE actual01:16 D41, initial candidate and conditional history, Sections1--9/Theorems1--3/equations1--15, all nine anchors, later automatic-independence and adopted-input resolution, both controls, source/role accounts and freeze. |
| dependency | [L229 full coefficient-energy estimate](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Actual nonvanishing integer auxiliary and all original roots; retained proof clears/cancels the SAME rational denominator, uses positive actual width and rho<=3 within the accepted increasing domain. |
| dependency | [C74 numerical margin](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY R1 K0, h0 and1/20 bounds and strict exp(2K0)[4/5+8epsilon(K0)+32K0]<1; no older multiplicity word theorem supplies the new result. |
| dependency | [C14 coefficient spacing](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | ONLY nonzero integer-polynomial coefficient energy>=1, with equality iff signed monomial; not its short-width O0 representation theorem at enlarged order/span. |
| dependency | [Accepted nonreciprocal statement](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | STRICTLY Section1, retained2008 survey Section5.1 equation15 and reciprocal/total-measure conventions; nonzero nonreciprocal algebraic integer M>=theta0 at statement-level acceptance, not original1971 proof/equality/isolation/other unit results. |
| dependency | [Original powered-height normalization](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost) | Exact d/N repetition and h(alpha^n)=n*m/d; the new reciprocal proof also gives its actual N2 specialization locally. No upper cost is treated as arithmetic income. |
| dependency | [Adopted all-height binary delays](Yin_C_G0084_v1.md#statement) | Only actual primitive weighted binary signed delays and optional one-coordinate shifts, TRUE-polynomial classification at K0, fixed weights and all-stage nonzero O0 legality; the mixed consumer retains cumulative expense. |
| dependency | [Optional direct covariance expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Finite calculation for the supplied packet over all original roots and actual final width, giving only Lambda<=T_final*m/d, not a construction or a reciprocal-only hypothesis for this analytic use. |
| support | [Original entire whole finding](../audits/reviews/Yin_R_G0315_v1.md#three-power-whole-independent-finding) | ENTIRE actual D41 final01:16 freeze including new Sections7--9 and direct interfaces. That reviewer now authors this wrapper; R315 does not prospectively cover this extraction or adopt it. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0794_v2.md#c87-three-power-actual-extraction-finding) | Entire actual statement, complete retained original and all direct/source/control/cost interfaces; separate actual noncontributor. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:31 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | ENTIRE A--F: original all-unit/full-norm domain, automatic at-most-three-power independence and saturation, full-O constant action/words, O0 mixed words, exact constants/controls/costs and limits. |
| argument | [Exact retained argument](#argument) | COMPLETE actual01:16 D41, initial candidate and conditional history, Sections1--9/Theorems1--3/equations1--15, all nine anchors, later automatic-independence and adopted-input resolution, both controls, source/role accounts and freeze. |
| dependency | [Exact retained dependency](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Actual nonvanishing integer auxiliary and all original roots; retained proof clears/cancels the SAME rational denominator, uses positive actual width and rho<=3 within the accepted increasing domain. |
| dependency | [Exact retained dependency](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY R1 K0, h0 and1/20 bounds and strict exp(2K0)[4/5+8epsilon(K0)+32K0]<1; no older multiplicity word theorem supplies the new result. |
| dependency | [Exact retained dependency](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | ONLY nonzero integer-polynomial coefficient energy>=1, with equality iff signed monomial; not its short-width O0 representation theorem at enlarged order/span. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | STRICTLY Section1, retained2008 survey Section5.1 equation15 and reciprocal/total-measure conventions; nonzero nonreciprocal algebraic integer M>=theta0 at statement-level acceptance, not original1971 proof/equality/isolation/other unit results. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-actual-product-cost) | Exact d/N repetition and h(alpha^n)=n*m/d; the new reciprocal proof also gives its actual N2 specialization locally. No upper cost is treated as arithmetic income. |
| dependency | [Exact retained dependency](Yin_C_G0084_v1.md#statement) | Only actual primitive weighted binary signed delays and optional one-coordinate shifts, TRUE-polynomial classification at K0, fixed weights and all-stage nonzero O0 legality; the mixed consumer retains cumulative expense. |
| dependency | [Exact retained dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Finite calculation for the supplied packet over all original roots and actual final width, giving only Lambda<=T_final*m/d, not a construction or a reciprocal-only hypothesis for this analytic use. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0315_v1.md#three-power-whole-independent-finding) | ENTIRE actual D41 final01:16 freeze including new Sections7--9 and direct interfaces. That reviewer now authors this wrapper; R315 does not prospectively cover this extraction or adopt it. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0794_v2.md#c87-three-power-actual-extraction-finding) | Entire actual statement, complete retained original and all direct/source/control/cost interfaces; separate actual noncontributor. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | The current finding is SELF because its initial complete argument input included author-validation conclusions beyond the necessary derivation. Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:49 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain earlier findings in their original homes at their actual recorded relationships and checking scopes. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | ENTIRE A--F: original all-unit/full-norm domain, automatic at-most-three-power independence and saturation, full-O constant action/words, O0 mixed words, exact constants/controls/costs and limits. |
| argument | [Argument: argument](#argument) | COMPLETE actual01:16 D41, initial candidate and conditional history, Sections1--9/Theorems1--3/equations1--15, all nine anchors, later automatic-independence and adopted-input resolution, both controls, source/role accounts and freeze. |
| dependency | [Dependency: actual-resultant-coefficient-energy-bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Actual nonvanishing integer auxiliary and all original roots; retained proof clears/cancels the SAME rational denominator, uses positive actual width and rho<=3 within the accepted increasing domain. |
| dependency | [Dependency: multiplicity-delay-explicit-threshold](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY R1 K0, h0 and1/20 bounds and strict exp(2K0)[4/5+8epsilon(K0)+32K0]<1; no older multiplicity word theorem supplies the new result. |
| dependency | [Dependency: short-width-power-order-obstruction](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | ONLY nonzero integer-polynomial coefficient energy>=1, with equality iff signed monomial; not its short-width O0 representation theorem at enlarged order/span. |
| dependency | [Dependency: smy08-u002](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | STRICTLY Section1, retained2008 survey Section5.1 equation15 and reciprocal/total-measure conventions; nonzero nonreciprocal algebraic integer M>=theta0 at statement-level acceptance, not original1971 proof/equality/isolation/other unit results. |
| dependency | [Dependency: general-unit-actual-product-cost](Yin_C_G0391_v1.md#general-unit-actual-product-cost) | Exact d/N repetition and h(alpha^n)=n*m/d; the new reciprocal proof also gives its actual N2 specialization locally. No upper cost is treated as arithmetic income. |
| dependency | [Dependency: statement](Yin_C_G0084_v1.md#statement) | Only actual primitive weighted binary signed delays and optional one-coordinate shifts, TRUE-polynomial classification at K0, fixed weights and all-stage nonzero O0 legality; the mixed consumer retains cumulative expense. |
| dependency | [Dependency: direct-exact-covariance-window-inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Finite calculation for the supplied packet over all original roots and actual final width, giving only Lambda<=T_final*m/d, not a construction or a reciprocal-only hypothesis for this analytic use. |
| support | [Recorded original finding](../audits/reviews/Yin_R_G0315_v1.md#three-power-whole-independent-finding) | ENTIRE actual D41 final01:16 freeze including new Sections7--9 and direct interfaces. That reviewer now authors this wrapper; R315 does not prospectively cover this extraction or adopt it. Finding relationship: self-reviewed. |
| review | [Current SELF finding](../audits/reviews/Yin_R_G0794_v2.md#g87-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:49 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The complete original final D41 follows.
Only its short author/framework front matter is omitted and its first title demoted by one heading level.
All original prose, equations, nine explicit anchors, initial candidate, early conditional and independence limits, later resolutions, both controls, source/role disclosures and final freeze remain verbatim.
All existing relative links remain valid from this Claim directory without rebasing.
Historical status wording is preserved at its original place and date; this initial decision owns the new Claim's current assessment.

The original full body was read during the independent whole review and reread for extraction.
Its actual length is31085 characters including36 characters of front matter; its31049-character body becomes31050 solely through title demotion.
Complete readback comparison, rather than a summary substitution, checks all235 body lines, nine anchors, equations1--15 and twelve links.
These operational counts do not replace mathematical review or impose a persistent digest/byte-retention requirement.

Root remains sole original proof/control author.
The matrix-recovery AI now owns only this new extraction wrapper in addition to its earlier original-review role, and cannot independently review its own wrapper.
Its older C84-wrapper and C74/C84-ancestor-review roles remain disclosed in R315 at their accepted-input scopes.
No mathematical native program, external acquisition, adoption or original-draft retirement accompanies this allocation.

## Argument

## Three-power order saturation and legal small-block constant rotations

Date: 2026-10-12T16:54.
Human author Yin.
Root AUTHOR continuation under the original G0001 weekly instruction, after developing the separate unequal-height delay proof D40.
This inquiry addresses the distinct still-excluded rational CONSTANT binary metric-preserving factors.
No native computation, source acquisition, new execution allowance or independent finding is asserted.
D40 is currently under independent whole review, not an adopted premise.

## Responsible question and candidate

At small actual exponent-spread times measure, does the rational span of TWO distinct monomial units intersect the original order only in their integer span?
If so, can an arbitrary rational two-coordinate constant matrix preserving the fixed positive diagonal weight metric create nonmonomial actual integral values from signed monomial inputs?
This is a saturation/integrality question, not a claim that every rational many-coordinate factor admits a legal binary factorization.

The current accepted inputs to read and apply precisely are L229's full-original-resultant coefficient-energy bound and C74's explicit numerical margins.
C71's all-weight E1 theorem, C82's now reviewed unit-direction words and the separate D40 all-height extension are nearby mechanisms; the new saturation proof should not be disguised as a denominator-only consequence of C71.
Every source/ancestor contribution role remains disclosed.
Root authored C74's fixed numerical derivation, which already has independent accepted reviews; a new reviewer must inspect this use rather than re-certify it by role.

## Proposed direct saturation proof to check

Fix a nontorsion algebraic integer unit alpha of original degree d and total measure m>0, and distinct exponents a,b.
If rational coefficients u,v satisfy u*alpha^a+v*alpha^b in O0, subtract nearest INTEGER multiples of the two original units.
The remaining two coefficients lie in[-1/2,1/2], and their value is still integral.
Unless both are zero, the resulting rational Laurent polynomial is nonzero at alpha: a rational relation between two distinct powers of an integer unit would force a rational unit power+/-1 and hence torsion.
If only one coefficient remains, its value is a nonzero rational coefficient of absolute value<=1/2 times a unit, contradicting its integer norm directly.

If both remain, the coefficient squared norm is<=1/2 and effective support<=2.
Clear its actual coefficient denominator, apply the full original L229 bound and CANCEL that same scalar in the original norm.
For U=abs(a-b)*m/d in(0,K0], the proposed contradiction is

    1<=abs Norm(value)^(2/d)
      <=(1/2)*exp(2U)*(1+epsilon(U)+8U)<1.

The last strict inequality follows from C74's accepted exp(2K0)*(4/5+8epsilon(K0)+32K0)<1.
Thus the proposed exact saturation is

    O0 intersect (Q*alpha^a+Q*alpha^b)
       =Z*alpha^a+Z*alpha^b.

This gives an integrality statement for rational two-term coefficients at SMALL exponent spread, independent of their denominator.
No actual finite arithmetic scan or rounded numerical embedding is intended; nearest integer coefficients are an exact proof operation.

## Proposed constant-matrix consequence

For a rational constant2-by-2 matrix B with B^T diag(r,s) B=diag(r,s), r,s>0, consider signed monomial inputs with different exponents.
If both outputs are integral, the saturation would force EVERY matrix entry to be an integer.
The determinant has absolute value1.
An integer isometry of a positive diagonal binary form is a signed diagonal identity or, when r=s, a signed coordinate swap: the first-column equation forces its top entry to be0 or+/-1, and the determinant handles the zero case.
This gives actual monomial outputs.

If the input exponents coincide, every output is a rational coefficient times one monomial.
Actual integrality and NONZERO outputs make those coefficients nonzero integers.
The positive weighted squared norm equals r+s, so both squared coefficients must equal1.
The matrix itself need not be integral in this coincident-input branch.
Signs may change or labels may swap; this is distinct from the sign-preserving delay conclusion.

Consequently a finite word of such constant binary factors would keep all true coordinates signed monomials at small initial common-width times measure, with fixed positive rational weights and EVERY intermediate value nonzero in O0.
If D40's separate all-height binary-delay theorem is accepted at its actual scope, the same induction should also allow arbitrary interleaving of those constant factors with its signed delays, charging only the latter in the cumulative width.
That combined conclusion is currently CONDITIONAL on the separately reviewed D40 input, not adopted by this allocation.
Complete q/M/copy/sign/common-normalization costs, the possible large constant-matrix denominator in a coincident branch, all exclusions and full author checking remain to be supplied before freeze.


<a id="power-saturation-exact-inputs"></a>
## 1. Actual integer-norm input and a three-dimensional margin

Date: 2026-10-12T17:00.
The two-power idea extends to AT MOST THREE rationally independent powers.
That independence is automatic for two distinct powers of a nontorsion integer unit, but is an EXPLICIT hypothesis for three.
Nothing below silently assumes independence of arbitrary three powers.

Let alpha be an actual nontorsion algebraic integer unit of original degree d>=2, total logarithmic Mahler measure m>0 and nu=Norm(alpha) in{+1,-1}.
Let O be ANY specified full order in K=Q(alpha) containing alpha, hence also alpha^-1 through the constant-unit minimal polynomial.
The main application is O0=Z[alpha].
Every nonzero element of O has a nonzero INTEGER original norm, and O intersect Q=Z.
No maximal-order equality is assumed.

Retain the precise accepted L229/C74 constants c0=log2/4, h0=c0 exp(-20), epsilon(u)=min(1,15sqrt(b0(u))+4u), b0(u)=max(u,sqrt(u/c0)log sqrt(c0/u)), and

    K0=c0/[2*36^8*5^64],
    K0<h0/2,
    exp(2K0)*(4/5+8epsilon(K0)+32K0)<1.               (1)

All functions are used only in their original increasing domain0<u<=h0.
For a rational Laurent polynomial f with nonzero value at alpha, actual width t>0, squared coefficient norm S and effective support rho, the accepted [L229 integer-auxiliary bound](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound), after clearing and CANCELING the same coefficient denominator q, gives

    abs Norm(f(alpha))^(2/d)
      <=S exp(2t*m/d)*[1+(rho-1)epsilon(t*m/d)+4rho*t*m/d]. (2)

To justify the rational passage, normalize its first exponent by a monomial unit and apply L229 to the integer polynomial q*f.
Its coefficient squared norm is q^2 S, effective support is unchanged and original norm is q^d times the signed original norm of f.
The same q^2 cancels after taking the2/d power.
Actual membership f(alpha) in O, rather than a norm-only surrogate, supplies the lower bound1 when needed.
A width-zero polynomial is treated exactly, not by evaluating epsilon at0.
Existing Pri11/Dim19 source-proof limits are not expanded.

At0<U<=K0 the exact elementary comparison

    (3/4)*[1+2epsilon(U)+12U]
       <4/5+8epsilon(U)+32U                          (3)

holds coefficient by coefficient.
With(1) and monotonicity, its product with exp(2U) is strictly below1.
This will handle every remaining rounded coefficient vector with at most three entries.

<a id="three-power-order-saturation"></a>
## 2. Exact saturation of at most three independent monomial powers

**Theorem 1.**
Let1<=r<=3 and let a_1,...,a_r be distinct integers such that alpha^(a_1),...,alpha^(a_r) are Q-linearly independent.
Put A=max a_i-min a_i.
If A*m/d<=K0, then

    O intersect span_Q{alpha^(a_i):1<=i<=r}
        =sum_(i=1)^r Z*alpha^(a_i).                  (4)

For r1 this holds without a width condition.
For r2, nontorsion makes the independence automatic.
The theorem is uniform in the coefficient denominators of a proposed rational combination, in the actual order index and in all exponent sizes apart from their common spread.

**Proof.**
The integer span is already in O.
Given u=sum q_i alpha^(a_i) in O with rational q_i, choose exact nearest integers n_i, either choice at a tie, and put e_i=q_i-n_i in[-1/2,1/2].
Then v=sum e_i alpha^(a_i) is in O.
If not every e_i is0, the Q-independence hypothesis makes v!=0.
If only one e_i is nonzero, abs Norm(v)=abs(e_i)^d<1, contradicting the nonzero integer norm.
Otherwise the rational Laurent polynomial f=sum e_i t^(a_i), after collecting the remaining nonzero terms, has actual positive width t<=A, S=sum e_i^2<=r/4<=3/4 and rho<=r<=3.
Equations(2)--(3) yield

    1<=abs Norm(v)^(2/d)
      <=(3/4) exp(2U)*[1+2epsilon(U)+12U]<1,
    U=A*m/d,                                       (5)

contradiction.
Thus all e_i0, proving(4).
No positive lower bound on the selected coefficient or denominator was assumed.

For r2, a rational dependence at distinct exponents would make a nonzero power of alpha rational.
Both that power and its inverse are algebraic integers, so this rational number is+/-1, contradicting nontorsion.
For r3 no such shortcut is asserted.
If a rational dependence is present, a nonzero rounded polynomial might evaluate to0, exactly where the integer-norm floor in(5) fails.
The three-power statement does not remove that explicit exception.

<a id="binary-constant-actual-monomial-rigidity"></a>
## 3. Arbitrary rational binary constant isometries

Fix positive rational weights omega_i,omega_j, write D=diag(omega_i,omega_j), and let B be ANY rational constant2-by-2 matrix with B^T D B=D.
Its determinant is+/-1.
On clean signed monomial inputs f_i=epsilon_i t^a,f_j=epsilon_j t^b require both output values at alpha to be NONZERO in O.
Suppose abs(a-b)*m/d<=K0.

**Theorem 2.**
Both TRUE output polynomials are signed monomials, with exponents among{a,b}.
If a!=b, the entire matrix B is an integer signed diagonal matrix, or an integer signed coordinate swap with omega_i=omega_j.
If a=b, B need not have integer entries; only its actual action on this signed input column is forced to be a signed monomial column.
Individual signs may change, unlike the sign-preserving binary delay result.

For a!=b apply Theorem1 to each output's unique rational two-power representation.
Its two coefficients are integers, hence every entry of B is an integer after restoring the input signs.
The pair alone, normalized by omega_i+omega_j, has exact circle covariance1 before and after B.
Each nonzero integer-polynomial output has squared coefficient norm at least1.
Their positive weighted average is1, so each squared coefficient norm is EXACTLY1; each row therefore has exactly one entry+/-1.
Invertibility puts those entries in different columns.
The metric identity permits the diagonal case for arbitrary weights, but the swapped case requires equal weights.
This proves the precise matrix classification, not only its value-level consequence.

For a=b each output is a rational coefficient times t^a.
Divide its actual value by the original monomial unit.
The resulting nonzero rational element of O is an ordinary nonzero integer.
The weighted squared coefficient average is again1, forcing both absolute coefficients1.
This proves the actual action, without incorrectly forcing matrix integrality from only one independent input power.
The old integer-energy-one argument is elementary and consistent with the adopted [C14 v2 coefficient-spacing argument](Yin_C_G0014_v2.md#short-width-power-order-obstruction); the new ingredient is the quantitative saturation that makes it applicable at larger actual spans.

A useful generalization is explicit: ANY rational constant isometry of a finite positive diagonal metric acting on a monomial vector with AT MOST THREE distinct Q-independent powers, at common A*m/d<=K0, has only signed-monomial outputs whenever all actual outputs are nonzero in O.
Collect each output in that independent power basis, use(4) to make all collected coefficients integers, then use the complete positive weighted coefficient-energy average1.
This does not assert that the matrix itself is integral when input powers are repeated.
In particular a constant factor on three coordinates cannot leave the monomial class unless its input has THREE DISTINCT Q-DEPENDENT powers, or one of the stated legality/width conditions fails.
No impossibility theorem for that dependence is supplied.

<a id="binary-constant-full-controls"></a>
## 4. Exact positive and nonintegral-matrix controls

The small-cost condition is essential.
The following hand-checked fixed-input control is a rational CONSTANT rotation, not a delayed reflection or a newly asserted near-one family.
Take

    P=t^2-t-1, alpha=(1+sqrt5)/2, d2, nu=-1,
    alpha^5=3+5alpha,
    B=(1/5)[[3,4],[-4,3]], weights(1/2,1/2),
    seed(1,t^5),
    g1=(3+4t^5)/5, g2=(-4+3t^5)/5.                  (6)

B^T B=Id and det B=1.
Both initial values are units.
The final actual values are3+4alpha and1+3alpha, respectively, both nonzero in O0.
The quadratic norm formula Norm(a+b alpha)=a^2+a b-b^2 gives

    D1=5, D2=-5,
    q_final=5, FINAL M=2, E1, T_final=A0=5,
    Res(P,5g1)=125, Res(P,5g2)=-125,
    full copied resultant product=-15625,
    Lambda=surplus=(1/2)log5>0.                      (7)

Actual q5 follows from the reduced coefficient3/5.
The original copied value-norm product is-25 and q^(dM)=5^4, so every scalar and negative norm sign is paid.
Direct circle expansion cancels the lag because3*4+(-4)*3=0, and each row has coefficient squared norm1.
The entire word has one constant step and nonzero integral endpoints.
Its U=A0*m/d=(5/2)log alpha>K0, where m=log alpha>0 is FIXED.
It violates none of the small-cost conclusions.
The recurrence alpha^2=alpha+1 proves the displayed fifth power directly; no native or floating computation was used.

A bounded local search for these exact polynomial/value strings found no identical retained control; the general rational orthogonal matrix mechanism is classical elementary algebra, and no novelty claim beyond this locally verified control is made.
C53/L380 remain credited for related rational weighted matrices, not used to assert this calculation without proof.

The coincident-input exception to matrix integrality is also real.
For ANY integer L>=2 put weights1/L,(L-1)/L, input(1,1), and

    B_L=(1/L)[[2-L,2(L-1)],[2,L-2]].                 (8)

This is the reflection Id-2Pi for the D-orthogonal direction(L-1,-1).
It satisfies B_L^T diag(1,L-1) B_L=diag(1,L-1), det=-1 and B_L*(1,1)^T=(1,1)^T.
Its actual coefficient denominator is L/gcd(L,2), unbounded for odd L.
The actual output has q1, FINAL M=L, E1, true width0 and zero norm income.
Thus the matrix denominator itself cannot be bounded in the coincident-power branch, even though the actual vector is rigid.
Every entry, denominator reduction and action in(8) follows by direct multiplication.

<a id="constant-delay-interleaving-and-costs"></a>
## 5. Binary constant words and the separate delay interface

Fix any finite N>=2 and fixed positive normalized rational weights, with actual indexed denominator M and positive primitive copies m_i.
Start from arbitrary signed monomials of common width A0.
A word of ANY finite number of rational B factors from Theorem2, on arbitrary pairs and with EVERY intermediate coordinate nonzero in O, stays in TRUE signed monomials whenever A0*m/d<=K0.
Induction applies because a constant step only uses exponents already present in its selected pair, so the common width never increases.
Signs and equal-weight labels may change; all absolute original norms remain1, actual final q1, E1 and full income0.

For an interleaving with the arbitrary-height primitive weighted binary DELAYS of [the complete D40 proof](Yin_C_G0084_v1.md#binary-height-entire-author-freeze), restrict now to O0, keep fixed weights and all-stage nonzero original-order legality, and put

    B_word=A0+sum_(DELAY steps)abs(k_j),
    U_word=B_word*m/d.                               (9)

Conditional on accepting that separately reviewed all-height delay input, U_word<=K0 makes every true intermediate polynomial a signed monomial.
At a delay, the current common width plus its abs(k) is at most B_word and D40 applies; at a constant factor Theorem2 applies with no additional width charge.
Constants may change signs and permute appropriate exponents, so the final sign is NOT claimed to equal the initial sign.
In every case actual q_final1, E1 and Lambda=surplus0.
Positive income with B_word<=B0*d then requires the strict m>K0/B0.
This conditional-input label records the current adoption boundary; the local saturation and constant theorems do not depend on D40.

Before small-cost rigidity is applied, let q_B be the ACTUAL coefficient denominator of each constant matrix, and L_j that of each delay matrix.
All labels and weights are fixed, hence

    q_final divides (product_constants q_B)*(product_delays L_j),
    T_final<=B_word, FINAL M unchanged.               (10)

A large matrix denominator is not assigned to the output when cancellation reduces it.
After one common monomial t^b, put D_i=Norm(alpha^b F_i(alpha)) and integer H_i=q_final*t^b F_i.
Full original signed arithmetic is

    Res(P,H_i)=q_final^d D_i,
    product_i Res(P,H_i)^(m_i)=q_final^(dM)*product_i D_i^(m_i),
    sum_i omega_i ||H_i||_2^2=q_final^2,
    I_int=log q_final+Lambda.                         (11)

Under the rigidity conclusions, raw final norms are(epsilon_i')^d nu^(a_i'), where both final signs and exponents are ACTUAL outputs.
Their copied product is the product of these factors to powers m_i.
The common shift contributes nu^(bM).
No conservation of the original sign vector, copied exponent sum or coordinate norm product is inferred from matrix determinants.
C10's accepted direct covariance expense additionally gives Lambda<=T_final*m/d; it constructs no packet and is not needed for the zero-income induction.

<a id="power-saturation-reuse-and-limits"></a>
## 6. Scope, actual reuse and remaining proof-review boundary

The new arithmetic statement is(4), proved using the already accepted L229 coefficient-energy estimate and exact nearest-integer coefficient subtraction.
The fixed K0 margin is adopted C74.
C14 already supplies the elementary integer coefficient-energy-one spacing principle; it does not provide the new order saturation at small common-width times measure, and no exact-dimension power-basis window is assumed here.
C53/L380 credit rational weighted matrix mechanisms.
The existing independent source/proof scopes of these inputs remain.
No new external theorem or source acquisition is required.

The three-power extension explicitly requires Q-independence.
With four rounded coefficients the universal squared-norm bound becomes1, losing the present strict margin; no four-power saturation theorem is claimed.
For three dependent powers a nonzero rounded polynomial can vanish at alpha; deleting this possibility would misuse the integer-norm floor.
Constants supported on more coordinates with more than three distinct powers, genuinely multicoordinate nonconstant delays, changing weights/metrics, nonmonomial seeds, final-only integrality, zero intermediate atoms and cancellations with large cumulative delay remain outside the mixed binary statement.
A rational paraunitary factorization need not consist of these factors or preserve actual-order membership at intermediate stages.

The two explicit controls retain fixed positive measure or zero income and do not supply the requested uniform near-one arithmetic lower income.
In particular this record does not prove A(n)>=eta*d at n<=C*d, a positive uniform complementary surplus or an unrestricted Mahler gap.
The entire initial candidate and its conditional D40 dependency are retained as research history.
No mathematical native program was executed.
Root is the sole new proof/control author and cannot provide its independent whole finding.
The actual adopted C14 v2 short-width/energy section has now been read: only its elementary integer-polynomial spacing argument is credited, with its short-width/order theorem kept separate.
Complete final self-check and the actual D40 adoption interface remain before a final whole-author freeze.


<a id="three-power-automatic-independence"></a>
## 7. The three-power independence condition is automatic at the actual threshold

Date: 2026-10-12T17:13.
The earlier rounding argument correctly retained an explicit independence hypothesis.
A subsequent argument now proves it automatically for at most THREE distinct powers in the present small-cost domain, using the already accepted nonreciprocal reduction and elementary reciprocal algebra.
The earlier candidate/conditional limitations are retained as their development history; they are not assumed away by the integer-norm argument.

The actual [Smy08-U002 nonreciprocal interface](../audits/literature/Smy08/Yin_U002.md#smy08-u002), restricted to its Section1 and the survey's Section5.1 equation15, states that EVERY nonzero nonreciprocal algebraic integer has M(alpha)>=theta0, where theta0>1 solves theta0^3-theta0-1=0.
This is an EXISTING statement-level acceptance from the theorem author's retained2008 survey, not a new proof audit of the1971 theorem.
Root actually read the unit's source/assessment and exact convention/statement after a separate read-only locator lookup.
Its equality/isolation classifications and other source results are not invoked.

Suppose three DISTINCT powers are Q-dependent.
Two distinct powers are already independent by Section2, so after a monomial normalization there is a relation

    A+B*alpha^h+C*alpha^k=0,
    A,B,C in Q minus{0}, 0<h<k, k=the actual span.    (12)

If P is NONRECIPROCAL, the nonzero rational polynomial in(12) is divisible by the actual minimal polynomial P, so k>=d.
The accepted statement gives

    k*m/d>=m>=log(theta0)>K0.

For the final strict comparison, x^3-x-1 is strictly increasing for x>=1 and its value at5/4 is-19/64.
Thus theta0>5/4, log(theta0)>log(5/4)>1/5>K0, using the elementary integral estimate and the already accepted K0<1/20.
This verifies the original LOGARITHMIC measure convention, not a degree-normalized substitute.

If P is RECIPROCAL, nontorsion irreducibility excludes the degree-one plus/minus exceptions, and the actual field automorphism sends alpha to alpha^-1.
Set u=alpha^h,v=alpha^k.
Applying that automorphism to(12) and multiplying by v gives

    A+B*u+C*v=0,
    C+B*v/u+A*v=0.

Eliminating v yields

    A*B*(u^2+1)+(A^2+B^2-C^2)*u=0,
    u+u^-1=(C^2-A^2-B^2)/(A*B) in Q.               (13)

Both u and u^-1 are algebraic integers.
Their rational sum is therefore an INTEGER n.
Nontorsion excludes n in{-2,-1,0,1,2}, since the corresponding roots of t^2-n*t+1 are roots of unity.
Consequently abs n>=3, u has actual degree2 (a rational integer unit would be+/-1), and

    M(u)=(abs n+sqrt(n^2-4))/2 >=(3+sqrt5)/2>2.

The exact original powered-field height identity, equivalently repetition of the two u-conjugates d/2 times among the alpha_i^h, gives

    h*m/d=(1/2)log M(u)>(1/2)log2>K0.               (14)

All ORIGINAL conjugates and multiplicities are retained.
Since k>h, the same contradiction holds for k*m/d<=K0.
This direct reciprocal elimination does not import an unproved sparse-polynomial gap or a source theorem about trinomials.

Hence under actual common span times measure<=K0, ANY set of at most three DISTINCT powers is Q-linearly independent.
Combining with Theorem1 removes that hypothesis in the present domain:

    O intersect span_Q{alpha^(a_i): 1<=i<=r}
      =sum_i Z*alpha^(a_i),
    1<=r<=3, distinct a_i, (max a_i-min a_i)*m/d<=K0. (15)

This is valid for every specified full O containing alpha, regardless of its index over O0.
No existence of an input with tiny m is asserted.
For genuine Salem degree>=4, the reciprocal argument gives the stronger qualitative observation that NO three distinct powers can be Q-dependent at ANY span: a nontrivial power u would be quadratic with two real off-circle conjugates, while an original circle conjugate would map to a circle conjugate of u.
That is impossible.
This observation uses the genuine Salem circle pair and is not asserted for all reciprocal units at arbitrary spans.

<a id="small-block-constant-and-binary-delay-frontier"></a>
## 8. Resolved mixed-word theorem and precise new boundary

The all-height binary delay proof originally referenced in Section5 is 2026-10-12T17:13 the actually adopted [C84](Yin_C_G0084_v1.md#statement), selected organized-reviewed after original whole R311 and separate actual extraction [R794 v2 original C84 extraction](../audits/reviews/Yin_R_G0794_v2.md#c84-binary-height-actual-extraction-finding).
Root is its proof author, and the new consumer uses this already independently accepted interface.
This resolves the historical conditional label in Section5; no source or reviewer finding is backdated.

**Theorem 3.**
In the fixed positive rational-weight, monomial-seed, original O0 setting, allow ANY finite interleaving of:

1. Rational CONSTANT isometries of the selected diagonal weight form on at most THREE coordinates.
   More generally a constant isometry may act on any number of selected labels if their current monomials use at most three DISTINCT exponents.
2. The arbitrary primitive two-coordinate signed delays of C84, and its optional one-coordinate delays.

Require EVERY actual intermediate coordinate to be NONZERO in O0.
Charge B_word=A0+sum abs(k_j) over every delay and put U_word=B_word*m/d.
If U_word<=K0, every TRUE intermediate polynomial is a signed monomial, actual final q1, E1 and full Lambda=surplus0.
The SAME K0 works for all dimensions, all finite numbers of either factor type, all fixed rational weights/FINAL M and all delay direction heights.

At a constant step, the current at-most-three distinct powers automatically satisfy(15), so every output has collected INTEGER coefficients in its current monomial support.
The full positive weighted coefficient-energy average remains1, hence every actual nonzero output is a signed monomial.
Its exponent already occurred in that selected support, so the common width does not increase.
At a delay step apply the precise adopted C84 interface at the actual current monomial vector and its local spread-plus-delay, bounded by B_word.
This proves induction.
Constants may change individual signs; no original-sign invariance or copied-exponent conservation is claimed for the mixed word.
All actual q/M/signed norm/common-normalization costs in(10)--(11) apply unchanged, with the actual denominator of each now permitted constant block.
Positive income at B_word<=B0*d implies m>K0/B0.

Constant-only words have the stronger full-order O version, since their saturation/energy argument uses only(15) and algebraic integrality.
The mixed statement is explicitly O0 because that is C84's adopted domain.
The two-coordinate matrix classification in Theorem2 remains exact; no unproved full-matrix classification is needed for a larger constant block with repeated input exponents.

The remaining constant-factor boundary is now more precise than the initial binary question: a first departure in a small-cost legal mixed program must use a constant factor involving at least FOUR DISTINCT powers, a nonconstant factor with at least three active coordinates, or violate another explicitly fixed hypothesis.
This is a necessary construction boundary, not proof that those escapes succeed.
Large final cancellation, changing weights, nonmonomial seeds, final-only legality and zero intermediate values remain outside.
No unrestricted arithmetic-income construction or uniform Mahler gap follows.


<a id="three-power-entire-author-freeze"></a>
## 9. Actual complete author freeze and new-input disclosure

Date: 2026-10-12T17:16.
Freeze the ENTIRE original two-power question/candidate, the later at-most-three-independent-power argument and all Sections1--9/Theorems1--3/equations1--15, including both explicit controls, all conditional-development history, the subsequent automatic independence proof and the now-resolved adopted C84 interface.
The fixed source D40 has been wholly retained in C84 and retired only after exact original-body comparison; this draft's same-proof link now names that canonical home.
The earlier conditional statements are retained as history and are expressly resolved by Section8's current theorem.

The author hand-checked exact coefficient rounding, zero/one/three-term cases, rational-denominator cancellation in the ORIGINAL norm, arbitrary full O membership, integer energy spacing, actual binary matrix/action distinctions, both exact control matrices, full signed norm/resultant/copy calculations and actual versus cumulative width.
The later three-power relation elimination was checked from BOTH reciprocal equations, including every nonzero coefficient, integral trace, torsion exceptional integer and powered-degree multiplicity.
The nonreciprocal branch uses only the actually read existing Smy08 statement and its precise measure convention.
The genuine-Salem stronger observation explicitly uses its original circle conjugates.
These are new AUTHOR checks, not an independent finding.

Exact resolved inputs are [L229](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound), [C74's numerical margin](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold), [C14 v2's coefficient spacing](Yin_C_G0014_v2.md#short-width-power-order-obstruction), [the accepted Smy08-U002 statement](../audits/literature/Smy08/Yin_U002.md#smy08-u002) restricted to Section1/nonreciprocal theorem, and [adopted C84](Yin_C_G0084_v1.md#statement) at its exact all-height binary-delay O0 scope.
The original-field powered-height normalization agrees with [L168](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost), with its repetition step also given locally.
The optional final direct expense uses [C10](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality).
No actual-order hypothesis from C14 or C84 is silently enlarged; the full-order constant-only theorem and O0 mixed theorem remain separate.

Root is the SOLE new proof/control author.
The independent-review agent supplied only a read-only locator/acceptance-scope lookup for already accepted Smy08, no new reciprocal elimination, rounding, control or word proof.
The matrix reviewer previously performed a preliminary check of the earlier local body; that is not an independent finding for this later complete revision.
A fresh actual whole review must include the new Sections7--9, the adopted interface and every earlier section before acceptance.
Existing source statement-level and proof-inspection boundaries are unchanged; no new PDF acquisition, native mathematical program or numerical scan occurred.
Original weekly execution authority remains monitored; this freeze makes no Claim adoption or unrestricted completion.

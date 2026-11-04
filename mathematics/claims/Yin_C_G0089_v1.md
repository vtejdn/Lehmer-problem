---
author: Yin
---
# Automatic four-power order saturation and legal constant-block delay rigidity

Date: 2026-10-12T17:46.
Human author Yin.
Fixed extraction under the continuing original G0001 instruction.
Root is the SOLE original proof/control author of the entire extended D43, including its final automatic four-power independence and resolved word theorem.
The g0001_matrix_recovery AI independently WHOLE-reviewed the actual01:37:52 extended freeze in R318 and NOW authors this new statement, decision and extraction wrapper.
It is therefore a contributor to this artifact and cannot independently review its own extraction.
A different noncontributor must actually inspect this registered Claim.
The complete original candidate, earlier explicit-gate proof, controls, freezes, DS17 boundary, new extension and all role/source limits are retained below.

## Statement

Let alpha be an ACTUAL nontorsion algebraic integer unit with monic irreducible minimal polynomial P of ORIGINAL degree d>=2, K=Q(alpha), total logarithmic Mahler measure m=m(P)>0, O0=Z[alpha] and nu=Norm_(K/Q)(alpha) in{+1,-1}.
Reciprocity is not assumed.
All norms retain ALL d original embeddings; negative powers lie in O0.
Use the exact accepted functions and constant

    c0=log2/4, h0=c0 exp(-20),
    b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0,
    K0=c0/[2*36^8*5^64], K0<h0/2,
    exp(2K0)[4/5+8epsilon(K0)+32K0]<1,
    5^8[epsilon(2K0)+12K0]<1.

The functions are used only at positive arguments in their accepted increasing domain.
Zero width is handled exactly.

**A. Automatic independence and original-order saturation of at most FOUR powers.**
For EVERY1<=r<=4 and distinct integer exponents a_1,...,a_r, put A=max a_i-min a_i.
If A*m/d<=K0, then the corresponding powers are Q-linearly independent and

    O0 intersect span_Q{alpha^(a_i):1<=i<=r}
        =sum_(i=1)^r Z*alpha^(a_i).

There is NO additional current independence premise at this threshold.
The one-power saturation holds without a width condition.
The conclusion has no coefficient-denominator, degree or absolute-exponent bound beyond the displayed actual spread-times-measure constraint.
It is explicitly an O0 theorem; no four-power saturation in arbitrary overorders is asserted.

The retained Theorem1 first proves the saturation assuming independence.
Its final Theorem3 then proves that independence automatically by using the actually adopted C87 THREE-power saturation, so the early explicit gate is RESOLVED rather than silently omitted.
For a putative primitive integer four-term relation, every three powers are already independent.
Solving for each omitted power and applying C87 in O0 forces all coefficient ratios to be integers; mutual divisibility gives coefficients c_i in{+1,-1}.

For nonreciprocal P, the relation polynomial after normalization has degree A>=d, while the accepted total-measure statement m>=log(theta0)>K0, theta0^3-theta0-1=0, contradicts A*m/d<=K0.
For reciprocal P, set u_i=c_i alpha^(a_i).
Actual inversion gives both sum_i u_i=0 and sum_i u_i^-1=0.
Their split polynomial is X^4+e2 X^2+e4, with e4 nonzero, hence even.
It must contain an opposite pair, which gives a nonzero power of alpha equal to+/-1, contradicting nontorsion.
This uses neither circle conjugates nor a sparse-relation factor-gap theorem.

**B. Exact doubled-coset mechanism and fully paid dyadic contradiction.**
Under the original explicit independence hypothesis, a rational coefficient vector giving an O0 value may be reduced by nearest INTEGER coefficients to e_i in[-1/2,1/2].
If the remainder is nonzero, its actual value is nonzero.
The accepted full L229 norm estimate, after canceling the SAME coefficient denominator, and the displayed K0 margin force

    S=sum_i e_i^2>4/5.

For r<=3 this contradicts S<=r/4.
For r4, reduce2e_i modulo integers to nearest remainders e'_i.
Then

    dist(2e_i,Z)^2<=(1-2abs(e_i))^2<=1-4e_i^2,
    S'=sum_i(e'_i)^2<=4-4S<4/5.

Its value remains in O0.
Independence and the same norm margin force all e'_i=0.
Thus the only possible nonzero coefficient coset is the all-half coset: ALL FOUR e_i are+/-1/2.

For that hypothetical coset, retain ALL sixteen indexed sign polynomials

    f_epsilon(t)=(1/2)sum_(i=1)^4 epsilon_i t^(a_i),
    epsilon in{+1,-1}^4, omega_epsilon=1/16.

Every value differs from the original remainder by integer powers, is in O0, and is NONZERO by independence.
Exact sign averaging gives constant Laurent covariance1, with every polynomial nonmonomial, ACTUAL q2, ACTUAL common width A, FINAL M16 and every copy1.
The adopted C71 all-weight E1 theorem gives

    2^8[epsilon(2A*m/d)+12A*m/d]>=1,

contradicting the displayed C74 margin.
This excludes the half coset and proves saturation.
The old C71 selector/product theorem is credited reuse; the new step forces arbitrary rational coefficient denominators into this forbidden dyadic case.
No epsilon(0), norm-only substitute for membership, zero-valued sign label or arbitrary-overorder extension enters this argument.

**C. Rational constant blocks and ANY finite legal mixed word.**
Let a rational CONSTANT matrix B preserve a finite positive rational diagonal metric D: B^T D B=D.
Apply it to TRUE signed monomial inputs whose selected block uses at most FOUR DISTINCT exponents.
If their span A satisfies A*m/d<=K0 and every actual output is NONZERO in O0, then EVERY TRUE output polynomial is a signed monomial on one of those input exponents.
The statement includes every block on at most four coordinates, and more labels whenever they have at most four distinct input exponents.
Repeated input powers do not force the entire matrix to be integral.
Individual signs may change.

Indeed A makes the collected output coefficients integers, while positive weighted coefficient-energy average1 forces every nonzero output to have exactly one coefficient+/-1.
This acts on the TRUE polynomial vector; a value-equivalent different vector is not substituted into its covariance identity.

For ANY finite number of labels at fixed positive normalized rational weights, start from TRUE signed monomials of initial common union span A0.
Allow ANY finite interleaving of these constant blocks with the ACTUALLY ADOPTED C84 primitive weighted binary delays and optional one-coordinate monomial shifts.
Each binary delay acts at the selected reduced positive ratio r:s, primitive integer direction v=(x,y)^T with xy nonzero and nonzero signed integer k, through

    U_k(t)=Id+(t^k-1)v(v^T D)/(v^T D v).

Keep all labels and weights fixed and require EVERY intermediate actual coordinate NONZERO in the SAME original O0.
Charge

    B_word=A0+sum_(ALL delayed factors)abs(k),
    U_word=B_word*m/d,

including each optional one-coordinate shift's own absolute delay; constant blocks add no delay charge.
If U_word<=K0, EVERY TRUE intermediate polynomial remains a signed monomial, actual final q1, E1 and full norm income/surplus0.
The same K0 is independent of label count, word length, fixed weights/FINAL M, exponent multiplicities and all primitive direction heights.
Every constant block uses its CURRENT exponents; A makes its earlier independence gate automatic.
Constants create no new exponent, and C84 delays increase common span by at most their absolute delay.

The current conclusion thus includes ALL at-most-four-distinct-exponent constant blocks in this legal small-cumulative-cost class, without a pending independence condition.
Signs may change, and neither the original sign vector nor a copied exponent sum is claimed invariant.
No general two-coordinate nonconstant matrix is included merely by its support size; the specified nonconstant factors are the accepted C84 delays.
The mixed theorem remains O0-only.

**D. All original scalar, indexed, sign and window costs.**
For the hypothetical sign packet in B, let D_epsilon=Norm_(K/Q)(f_epsilon(alpha)), a nonzero signed integer.
After ONE common shift t^b to nonnegative exponents, the primitive numerators F_epsilon=2t^b f_epsilon satisfy

    Res(P,F_epsilon)=2^d nu^b D_epsilon,
    product_epsilon Res(P,F_epsilon)
       =2^(16d)nu^(16b)product_epsilon D_epsilon,
    E=1, q=2, FINAL M=16, copies all1, S_int=4,
    Lambda=(1/(16d))sum_epsilon log abs(D_epsilon)>=0,
    I_int=log2+Lambda, full surplus=Lambda.

These are CONDITIONAL arithmetic data of the sign family ultimately excluded at the small threshold.
No specific norm values are invented there.
The common shift preserves ACTUAL width A, and the selected C71 auxiliary can have width up to2A, explaining the doubled epsilon argument.

For an actual general mixed word, let M be the least indexed weight denominator and m_i=M omega_i its primitive positive copies.
Let q_j be each ACTUAL constant-matrix entry denominator.
For a binary delay put c=gcd(abs(rx),abs(sy)) and L=(rx^2+sy^2)/c, its ACTUAL matrix denominator.
Then the final coefficient denominator divides

    (product_constant_steps q_j)*(product_binary_delays L).

One-coordinate shifts have denominator1.
Divisibility is not equality.
The rigidity theorem proves ACTUAL final q1, while M and every original copy remain unchanged.
At actual final monomials epsilon'_i t^(a'_i), RAW signed norms are(epsilon'_i)^d nu^(a'_i), every absolute norm1, and one common shift contributes nu^(bM) to the copied product.
Hence E=S_int1 and Lambda=I_int=surplus0.
All contents, original degree, signs and indexed duplicates are retained; a matrix determinant is not substituted for coordinate norm products.
Small final width after a large cumulative cancellation does not satisfy the stated budget merely by being small.

**E. Exact positive four-independent-power control outside the threshold.**
Take

    P=t^4-t^3-2t^2-t+1=t^2 T(t+t^-1), T(X)=X^2-X-4,
    tau_+=(1+sqrt17)/2, tau_-=(1-sqrt17)/2.

This is an ACTUAL irreducible reciprocal unit of degree4, with real root beta>1 and its inverse, two circle conjugates, nu1 and fixed m=log beta.
The four powers at exponents0,1,3,4 are Q-independent.
The exact relation

    alpha^4=alpha^3+2alpha^2+alpha-1,
    (1-alpha-alpha^3+alpha^4)/2=alpha^2 in O0

makes the all-half coset integral on this input, and all sixteen signs are nonzero.
The resulting packet has actual q2, FINAL M16, copies1, E1 and common width4.
For epsilon4=+1 its eight values are

    u_(a,b,c)=alpha^2+b alpha+c alpha^3-a, (a,b,c) in{0,1}^3.

With tau=alpha+alpha^-1 and tau^2=tau+4, all relative products and FULL signed degree-four norms are

| a,b,c | Relative product | Full signed norm |
| --- | --- | ---: |
| 0,0,0 | 1 | 1 |
| 1,0,0 | -tau | -4 |
| 0,1,0 | 2+tau | 2 |
| 0,0,1 | 2+tau | 2 |
| 0,1,1 | (1+tau)^2 | 4 |
| 1,1,0 | 1-tau | -4 |
| 1,0,1 | -3-2tau | -1 |
| 1,1,1 | -tau | -4 |

The remaining eight values are their negatives, with the SAME signed norm because d4.
The eight norms multiply to2^10 and all sixteen to2^20.
The primitive sign numerators and all indexed copies give

    product_epsilon Res(P,2f_epsilon)=2^84,
    S_int=4, Lambda=full surplus=5log2/16>0.

Since tau_+>5/2, beta>2 and U=4m/4=m>log2>K0.
This is a fixed positive-measure control, not a near-one family.
The16-label sign packet is not asserted to arise from a four-by-four constant isometry with preserved labels, and no optimality or matrix-realization conclusion is inferred.

**F. Resolved history, sparse-source boundary and precise exclusions.**
The old Theorem1/Theorem2 independence condition was a valid original stage and is retained verbatim.
The subsequent adopted C87 application and new Theorem3 resolve it at the same small-cost threshold.
C87 itself never depended on this four-power argument; the direct graph is acyclic.
Its broader full-order three-power theorem is used only after restriction to O0 and does not enlarge the present four-power order domain.

The accepted DS17 fixed-term gap concerns TOTAL m(F) of a sparse integer polynomial F, with arbitrary coefficient heights.
A four-power relation only gives P dividing F.
The identity m(F)=m(P)+m(F/P) allows a cofactor cost, so a lower bound on m(F) alone cannot lower-bound m(P).
The retained dated DS17 boundary remains correct; automatic independence is obtained instead from C87 saturation and reciprocal inversion, with the separately accepted nonreciprocal bound.
No new sparse-factor theorem or source-proof audit is claimed.

No fifth-power saturation, arbitrary-overorder four-power extension, general rational paraunitary factorization, nonconstant multicoordinate classification, uniform positive same-exponent income or unrestricted Mahler gap follows.
Five or more distinct powers, factors outside the specified nonconstant class, changing weights/labels, nonmonomial seeds, zero/illegal intermediate values, final-only legality and large cumulative delay remain outside.
This is an obstruction for the stated construction class, not proof that an excluded route succeeds or that near-one inputs exist.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:46 |
| status | open |
| reason | Register the final automatic at-most-four-power O0 saturation, true constant actions and specified legal mixed-word obstruction, retaining the ENTIRE actual01:37:52 extended D43. Earlier explicit-gate statements are preserved as resolved development history. R318 whole-reviewed that extended original only; its reviewer now authors this new wrapper, which awaits another noncontributor's actual extraction review. No overorder/fifth-power/general-gap extension is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F: automatic four-power independence and O0 saturation, doubled-coset/sign completion, resolved constant/mixed theorem, all actual costs/control/source and excluded scopes. |
| argument | [Entire extended original body](#argument) | COMPLETE01:37:52 D43 candidate/history, Sections1--8/Theorems1--3/equations1--15, twelve anchors, original freeze, DS17 supplement, later automatic-independence/resolved-word extension, all controls/roles/limits. |
| dependency | [L229 actual coefficient-energy bound](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound) | Actual nonvanishing integer auxiliary and full original norm; rational denominator cancellation is local, with rho<=4 and positive-width accepted-domain use. |
| dependency | [C74 R1 margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY exact K0, K0<h0/2, strict energy margin and5^8 doubled-parameter inequality; no older multiplicity word theorem supplies the new result. |
| dependency | [C71 all-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Actual nontrivial finite positive rational-weight packet, nonzero O0 values, true q2/T=A/M16 and q^8 necessary bound; no arbitrary-overorder extension. |
| dependency | [Adopted C84 delay interface](Yin_C_G0084_v1.md#statement) | Exact primitive weighted binary signed delays and optional one-coordinate shifts, actual TRUE-polynomial classification at K0, all-stage O0 legality/fixed weights/cumulative expense and denominator scope. |
| dependency | [Adopted C87 three-power saturation](Yin_C_G0087_v1.md#statement) | ONLY PartA automatic three-power independence and saturation at same K0, restricted to O0 and applied to EACH omitted-index basis in the new four-term relation. |
| dependency | [Accepted nonreciprocal bound](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | STRICTLY Section1 and retained2008 survey Section5.1 equation15, total measure and reciprocal convention, M>=theta0 at statement/applicability scope; no1971 proof/equality/isolation audit. |
| support | [DS17 exact source boundary](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Comparison ONLY: fixed-support gap for TOTAL m(F), not its arbitrary factor P. The new theorem does not use the invalid transfer or expand foundational proof coverage. |
| support | [C27 prior source application](Yin_C_G0027_v1.md#statement) | Comparison ONLY: accepted sparse result applied directly to an original bounded-support polynomial; retained D22 source account supplies no factor transfer. |
| support | [Original extended whole finding](../audits/reviews/Yin_R_G0318_v1.md#four-power-extended-whole-independent-finding) | ENTIRE actual01:37:52 extended D43, original and later mathematics, all costs/controls/direct/source interfaces. Its reviewer now authors this wrapper, so this is not a review of the new extraction. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:58 |
| status | proved |
| reason | Adopt original extended whole R318 and separate actual extraction [R794 v2 original C89 extraction](../audits/reviews/Yin_R_G0794_v2.md#c89-four-power-actual-extraction-finding). Automatic at-most-four-power independence and O0 saturation at the exact K0, and the precise legal constant-block/binary-delay word rigidity, are fixed with every original signed norm, actual denominator, indexed weight and cumulative-width cost. Earlier explicit-gate and source-comparison history remain. Root authored the proof and relies on distinct noncontributor findings; no arbitrary overorder/five-power/general-factorization or unrestricted gap conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F: automatic four-power independence and O0 saturation, doubled-coset/sign completion, resolved constant/mixed theorem, all actual costs/control/source and excluded scopes. |
| argument | [Entire extended original body](#argument) | COMPLETE01:37:52 D43 candidate/history, Sections1--8/Theorems1--3/equations1--15, twelve anchors, original freeze, DS17 supplement, later automatic-independence/resolved-word extension, all controls/roles/limits. |
| dependency | [L229 actual coefficient-energy bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Actual nonvanishing integer auxiliary and full original norm; rational denominator cancellation is local, with rho<=4 and positive-width accepted-domain use. |
| dependency | [C74 R1 margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY exact K0, K0<h0/2, strict energy margin and5^8 doubled-parameter inequality; no older multiplicity word theorem supplies the new result. |
| dependency | [C71 all-weight E1 selector](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Actual nontrivial finite positive rational-weight packet, nonzero O0 values, true q2/T=A/M16 and q^8 necessary bound; no arbitrary-overorder extension. |
| dependency | [Adopted C84 delay interface](Yin_C_G0084_v1.md#statement) | Exact primitive weighted binary signed delays and optional one-coordinate shifts, actual TRUE-polynomial classification at K0, all-stage O0 legality/fixed weights/cumulative expense and denominator scope. |
| dependency | [Adopted C87 three-power saturation](Yin_C_G0087_v1.md#statement) | ONLY PartA automatic three-power independence and saturation at same K0, restricted to O0 and applied to EACH omitted-index basis in the new four-term relation. |
| dependency | [Accepted nonreciprocal bound](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | STRICTLY Section1 and retained2008 survey Section5.1 equation15, total measure and reciprocal convention, M>=theta0 at statement/applicability scope; no1971 proof/equality/isolation audit. |
| support | [DS17 exact source boundary](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Comparison ONLY: fixed-support gap for TOTAL m(F), not its arbitrary factor P. The new theorem does not use the invalid transfer or expand foundational proof coverage. |
| support | [C27 prior source application](Yin_C_G0027_v1.md#statement) | Comparison ONLY: accepted sparse result applied directly to an original bounded-support polynomial; retained D22 source account supplies no factor transfer. |
| support | [Original extended whole finding](../audits/reviews/Yin_R_G0318_v1.md#four-power-extended-whole-independent-finding) | ENTIRE actual01:37:52 extended D43, original and later mathematics, all costs/controls/direct/source interfaces. Its reviewer now authors this wrapper, so this is not a review of the new extraction. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0794_v2.md#c89-four-power-actual-extraction-finding) | ENTIRE actual C89 A--F, full extended original, exact automatic-independence/order/word/cost/control/source interfaces; distinct noncontributor. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | The current finding is SELF because its initial complete argument input included author-validation conclusions beyond the necessary derivation. Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:50 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain earlier findings in their original homes at their actual recorded relationships and checking scopes. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | ENTIRE A--F: automatic four-power independence and O0 saturation, doubled-coset/sign completion, resolved constant/mixed theorem, all actual costs/control/source and excluded scopes. |
| argument | [Argument: argument](#argument) | COMPLETE01:37:52 D43 candidate/history, Sections1--8/Theorems1--3/equations1--15, twelve anchors, original freeze, DS17 supplement, later automatic-independence/resolved-word extension, all controls/roles/limits. |
| dependency | [Dependency: actual-resultant-coefficient-energy-bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Actual nonvanishing integer auxiliary and full original norm; rational denominator cancellation is local, with rho<=4 and positive-width accepted-domain use. |
| dependency | [Dependency: multiplicity-delay-explicit-threshold](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold) | ONLY exact K0, K0<h0/2, strict energy margin and5^8 doubled-parameter inequality; no older multiplicity word theorem supplies the new result. |
| dependency | [Dependency: all-weight-unit-energy-product-theorem](Yin_C_G0071_v1.md#all-weight-unit-energy-product-theorem) | Actual nontrivial finite positive rational-weight packet, nonzero O0 values, true q2/T=A/M16 and q^8 necessary bound; no arbitrary-overorder extension. |
| dependency | [Dependency: statement](Yin_C_G0084_v1.md#statement) | Exact primitive weighted binary signed delays and optional one-coordinate shifts, actual TRUE-polynomial classification at K0, all-stage O0 legality/fixed weights/cumulative expense and denominator scope. |
| dependency | [Dependency: statement](Yin_C_G0087_v1.md#statement) | ONLY PartA automatic three-power independence and saturation at same K0, restricted to O0 and applied to EACH omitted-index basis in the new four-term relation. |
| dependency | [Dependency: smy08-u002](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | STRICTLY Section1 and retained2008 survey Section5.1 equation15, total measure and reciprocal convention, M>=theta0 at statement/applicability scope; no1971 proof/equality/isolation audit. |
| support | [Support: ds17-u001](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Comparison ONLY: fixed-support gap for TOTAL m(F), not its arbitrary factor P. The new theorem does not use the invalid transfer or expand foundational proof coverage. |
| support | [Support: statement](Yin_C_G0027_v1.md#statement) | Comparison ONLY: accepted sparse result applied directly to an original bounded-support polynomial; retained D22 source account supplies no factor transfer. |
| support | [Recorded original finding](../audits/reviews/Yin_R_G0318_v1.md#four-power-extended-whole-independent-finding) | ENTIRE actual01:37:52 extended D43, original and later mathematics, all costs/controls/direct/source interfaces. Its reviewer now authors this wrapper, so this is not a review of the new extraction. Finding relationship: self-reviewed. |
| review | [Current SELF finding](../audits/reviews/Yin_R_G0794_v2.md#g89-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:50 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The ENTIRE original final D43 follows.
Only its36-character author/framework front matter is removed and its first title demoted by one heading level.
All original candidate prose, explicit-gate development, equations, twelve anchors, original01:32:09 freeze,01:33:15 DS17 boundary, later Sections7--8 and01:37:52 extended freeze, control table, source and contribution limits remain verbatim.
Existing relative links remain valid from this Claim directory and require no rebasing.
Historical status and gate wording remains at its original location/date; the current final theorem and this initial decision make the resolved scope explicit.

Original size is25620 characters.
Its25584-character body becomes25585 solely from title demotion, with210 body lines, twelve anchors, all equations1--15 and eight links retained.
Full readback comparison checks the entire body, not just statement text or a proof summary.
These are operational preservation facts, not a mathematical digest or a requirement to retain a byte image.

Root remains sole original proof/control author.
The matrix-recovery AI is now the new wrapper contributor in addition to its original R318 review role, and must not independently review this wrapper.
Its older C87/C84 wrapper and ancestor-review roles remain disclosed at their inherited scopes; no role manufactures independent evidence.
A distinct reviewer must inspect this ACTUAL new artifact before coordinator adoption.
No native mathematical program, external acquisition, original retirement or adoption accompanies this extraction.

## Argument

## Four-power saturation by coset doubling and dyadic sign completion

Date: 2026-10-12T17:27.
Human author Yin.
Root AUTHOR continuation of G0001 at unchanged weekly allowance.
This new question follows the complete three-power saturation proof and distinguishes a four-dimensional obstruction not covered by its nearest-integer energy margin.
Root supplied the candidate and is a proof contributor; no independent finding, native execution or adoption is asserted.

<a id="four-power-saturation-candidate"></a>
## Responsible candidate and intended boundary

For FOUR Q-linearly independent distinct powers of an actual nontorsion algebraic integer unit, investigate whether the original-order intersection is still exactly their integer span at the SAME accepted small width-times-measure threshold.
Nearest-integer remainders have coefficient energy at most1, so the earlier three-power strict-below-one estimate does not itself prove this.
The candidate is to first double a hypothetical nonintegral coefficient coset.
The norm floor should force every nonzero remainder's energy above4/5; doubling then has energy below4/5 and must vanish in the coefficient quotient.
The only surviving coset would have four half-integer coefficients.
Completing ALL its sign choices would make an actual q2/E1 packet, forbidden by the accepted small-parameter denominator theorem.

This is a genuine change in the lattice argument, not a reapplication of the three-dimensional3/4 bound.
Four-power Q-independence remains an EXPLICIT hypothesis; no automatic four-term-relation exclusion or general constant-matrix theorem is asserted.
The original order is O0=Z[alpha].
A wider full-order extension would need a separate checked interface and is not part of this candidate.
All substantive proof, failures, exact controls and full indexed costs will be retained here.
No native mathematical computation is proposed.


<a id="four-power-exact-inputs"></a>
## 1. Exact accepted inputs and the new rounding margin

Let alpha be an ACTUAL nontorsion algebraic integer unit, P its monic irreducible minimal polynomial of ORIGINAL degree d>=2, m=m(P)>0 its TOTAL logarithmic Mahler measure, O0=Z[alpha], and nu=Norm(alpha) in{+1,-1}.
All d original embeddings remain in every norm.
Negative powers lie in O0.
The exact accepted [L229 coefficient-energy bound](../ledger/Yin_L_G0229_v1.md#actual-resultant-coefficient-energy-bound), after clearing and canceling the SAME coefficient denominator, says for a rational Laurent f with nonzero value, actual positive width t, coefficient squared norm S and rho=||f||_1^2/S that

    |Norm(f(alpha))|^(2/d)
       <=S exp(2u)[1+(rho-1)epsilon(u)+4rho*u], u=t*m/d<=h0.       (1)

Here c0=log2/4, h0=c0 exp(-20), b(u)=max{u,sqrt(u/c0)log sqrt(c0/u)}, epsilon(u)=min{1,15sqrt(b(u))+4u}, only at positive arguments in its original increasing domain.
Applying L229 to qf multiplies S by q^2 and the original norm by q^d; those scalars cancel exactly in(1).
A common monomial changes only the signed unit factor nu to its integer power.
Integer membership and NONZERO value separately supply the norm floor1.
Width0 is handled by the exact norm of a rational multiple of a unit, not by assigning epsilon(0).

Use the actual independently accepted [C74 numerical margins](Yin_C_G0074_v1.md#multiplicity-delay-explicit-threshold):

    K0=c0/[2*36^8*5^64], K0<h0/2,
    exp(2K0)[4/5+8epsilon(K0)+32K0]<1,
    5^8[epsilon(2K0)+12K0]<1.                                  (2)

Root authored that old numerical derivation and the earlier three-power argument; those accepted roles are not an independent review of this new proof.
All L229/Pri11/Dim19 source acceptance boundaries remain unchanged.
The previous three-power proof uses rounded energy<=3/4; this proof's first new step is its application to a DOUBLED coefficient coset.

For0<U<=K0 put D4(U)=exp(2U)[1+3epsilon(U)+16U].
The coefficientwise comparison with(2) gives

    (4/5)D4(U)<1.                                             (3)

Thus EVERY nonzero O0-valued rational polynomial supported on at most four of the specified powers, of actual width at most A with U=A*m/d, has coefficient energy STRICTLY greater than4/5.
Indeed if actual width is positive then rho<=4 and(1)--(3) give1<=S D4(U); for a single surviving coefficient, its unit-normalized rational integer has absolute value>=1 and S>=1.
This implication will be used only when Q-independence ensures the value is nonzero.

<a id="four-power-doubling-saturation"></a>
## 2. Four-power saturation by doubling the coefficient coset

**Theorem 1.**
Let1<=r<=4, let a_1,...,a_r be distinct integers, and assume alpha^(a_1),...,alpha^(a_r) are Q-linearly independent.
Put A=max a_i-min a_i.
If A*m/d<=K0, then

    O0 intersect span_Q{alpha^(a_i):1<=i<=r}
        =sum_i Z*alpha^(a_i).                                (4)

Independence is an EXPLICIT hypothesis, especially for r4.
This theorem has no coefficient-denominator or order-index estimate as an extra premise.
Only the stated original order is used.

For r1, a rational multiple of a unit is integral only if the rational coefficient is an integer.
For r>=2, A>0.
Given z=sum_i q_i alpha^(a_i) in O0, subtract nearest integer coefficients n_i, choosing either integer at an exact tie.
Write e_i=q_i-n_i in[-1/2,1/2] and v=sum_i e_i alpha^(a_i) in O0.
If some e_i is nonzero, independence makes v nonzero.
Let S=sum_i e_i^2.
The margin in Section1 gives

    S>4/5, while S<=r/4<=1.                                 (5)

This already excludes r<=3.
For r4, subtract nearest integers from each2e_i and let e'_i denote the resulting residues.
For x=|e_i| in[0,1/2], the distance of2e_i to Z satisfies

    dist(2e_i,Z)^2 <= (1-2x)^2 <= 1-4x^2.

The first inequality remains valid when x<=1/4, since the nearer integer can be0; the second is exactly4x(2x-1)<=0.
Consequently

    S'=sum_i (e'_i)^2 <=4-4S<4/5.                            (6)

The actual value sum_i e'_i alpha^(a_i) is in O0 because it is2v minus integer powers.
If some e'_i were nonzero, Q-independence and Section1 would instead force S'>4/5, a contradiction.
Therefore every2e_i is an integer.
Every nonzero e_i equals+/-1/2.
Inequality(5) forces ALL FOUR coefficients to be nonzero: this is the unique possible surviving half-integral coset, not a statement that its actual integrality is available.

Choose the complete sixteen indexed sign polynomials

    f_epsilon(t)=(1/2)sum_(i=1)^4 epsilon_i t^(a_i),
    epsilon in{+1,-1}^4, omega_epsilon=1/16.                 (7)

Each differs from v by integer combinations of the four powers, so each actual value is in O0.
Independence makes ALL sixteen values nonzero.
Exact independent sign averaging, including every repeated exponent difference, gives sum_epsilon omega_epsilon f_epsilon f_epsilon*=1.
Every polynomial is nonmonomial, actual q=2, actual union width A, FINAL M=16.
The already accepted [C71 all-weight E1 theorem](Yin_C_G0071_v1.md#statement) therefore gives

    2^8[epsilon(2U)+12U]>=1,                               (8)

contradicting(2) and monotonicity.
No whole-order extension of C71 is used: every value is in its ACTUAL O0 domain.
This contradiction eliminates the last coset and proves(4).
C71's selector/product argument is credited old mathematics; the new ingredient is forcing arbitrary coefficient denominators into this forbidden dyadic coset.
The nearest-integer operation and all16 sign choices are exact finite proof operations, not a proposed native numerical search.

<a id="four-power-constant-and-mixed-words"></a>
## 3. Constant isometries and legal mixed words at the explicit independence gate

**Theorem 2.**
Fix a finite positive rational diagonal metric D=diag(omega_i).
Let a rational CONSTANT invertible B satisfy B^T D B=D.
Apply it to TRUE signed monomial inputs F_i=epsilon_i t^(a_i), whose selected block contains at most four DISTINCT exponents, with their corresponding powers Q-linearly independent.
If their actual spread A satisfies A*m/d<=K0 and every actual output belongs to O0 minus{0}, then EVERY TRUE output polynomial is a signed monomial on one of those input exponents.

Collect each output by distinct exponent.
Theorem1 says all its collected rational coefficients are integers.
Exact metric preservation gives, after normalizing the selected weights by their positive sum, a complementary energy1 packet.
Its positive weighted average of coefficient squared norms is1; each nonzero integer polynomial has integer coefficient squared norm at least1.
Thus every output has exactly one coefficient+/-1.
This is a true-polynomial statement; equality of field values alone was not substituted into an old covariance identity.
With repeated input exponents the MATRIX itself need not be integral.
Signs may change; there is no coordinatewise sign-preservation claim.

For ANY finite number N of labels at fixed positive normalized rational weights, start from TRUE signed monomials of initial union span A0.
Allow any finite word consisting of the preceding constant blocks and the actually adopted [C84 weighted binary delays](Yin_C_G0084_v1.md#statement), with optional single-coordinate monomial shifts.
Each constant block must satisfy the preceding at-most-four-distinct-power independence test on its CURRENT input.
Each delay acts on two coordinates at reduced weight ratio r:s with any primitive integer direction(x,y), xy nonzero, and any nonzero signed integer k, through

    B_delay(t)=I+(t^k-1)v(v^T D)/(v^T D v), v=(x,y)^T.

Require EVERY intermediate actual coordinate to be nonzero in O0, keeping all labels and weights fixed.
If

    B_word=A0+sum_(all delayed factors)|k|,
    B_word*m/d<=K0,                                        (9)

then all TRUE intermediate polynomials are signed monomials and final norm income and surplus are0.
In this sum a single-coordinate shift has its own |k| charge; constant blocks have no delay charge.
The proof is induction: constants create no new exponents by Theorem2; each C84 step, with current span plus its |k| bounded by B_word, preserves true monomials and increases span by at most|k|.
C84 is already adopted with original and actual independent findings; no conditional use of an unreviewed draft is needed.
The earlier three-power work can separately discharge its own independence condition but is NOT used as an unadopted premise here.

The explicit independence gate is part of this mixed-word class.
A dependent four-power block, a constant block on five or more distinct powers, a nonconstant factor with three or more active coordinates, changing weights/labels, nonmonomial seeds, zero or illegal intermediate values and a large cumulative delay with only small final width remain outside it.
A formal rational paraunitary factorization need not meet the gate or preserve intermediate membership.
This theorem is not a uniform positive-income construction or an unrestricted Mahler gap.

<a id="four-power-full-indexed-costs"></a>
## 4. All original-degree signs, coefficient denominators and indexed costs

For the hypothetical sign family(7), retain ALL16 labels even though global sign reversal gives equal absolute norms.
Write D_epsilon=Norm_K(f_epsilon(alpha)), each a nonzero signed integer.
After a common shift by t^b making every exponent nonnegative, the full norm acquires nu^b.
Let F_epsilon=2t^b f_epsilon be the primitive integer numerators.
Then

    Res(P,F_epsilon)=2^d nu^b D_epsilon,
    product_epsilon Res(P,F_epsilon)
       =2^(16d) nu^(16b) product_epsilon D_epsilon,
    E=1, q=2, M=16, copies all1, S_int=4,
    Lambda=(1/(16d))sum_epsilon log|D_epsilon|>=0,
    I_int=log2+Lambda, surplus=Lambda.                     (10)

The family is ultimately impossible at(9); these are its fully charged conditional arithmetic data, not invented actual norm values.
Its absolute width is A after the ONE common shift.
C71's auxiliary may have width up to2A; that is why the final inequality uses epsilon(2U) and K0<h0/2.

For an actual general mixed word let M be the least indexed weight denominator, m_i=M omega_i positive integers with gcd1, and q_j the least entry denominator of each constant B_j.
For a binary delay with reduced positive ratio r:s set c=gcd(|rx|,|sy|), L=(rx^2+sy^2)/c, the exact matrix denominator in C84.
Before any cancellations the final coefficient denominator divides product_j q_j times product_delays L.
The theorem proves the ACTUAL final q=1.
M and every original indexed copy stay fixed.
If the final TRUE representatives are epsilon'_i t^(a'_i), their original signed norms are (epsilon'_i)^d nu^(a'_i); every absolute norm is1.
Their copied product and its common-normalization factor nu^(bM) are retained exactly.
Thus E=S_int=1, Lambda=I_int=surplus=0.
Neither the determinant of B nor a copied exponent sum was assumed to preserve the coordinate norm product.
Only actual monomial output proves zero income.

<a id="four-power-fixed-positive-control"></a>
## 5. An exact four-independent-power countercontrol outside the threshold

The small-measure-width assumption is necessary.
This control is new hand algebra within this draft; a bounded exact phrase search found no identical retained formula, but no general novelty claim follows.
Put

    P=t^4-t^3-2t^2-t+1=t^2 T(t+t^-1), T(X)=X^2-X-4,
    tau_+=(1+sqrt17)/2>2, tau_-=(1-sqrt17)/2 in(-2,2).

T is irreducible over Q because17 is not a rational square.
In its real quadratic field, the discriminant of t^2-tau*t+1 is tau^2-4=tau, whose conjugate tau_- is negative.
A square in this real field has nonnegative image under each real embedding, so tau is not a square.
Hence P is irreducible of degree4; its exterior real root beta>1, inverse beta^-1 and the two circle roots give a nontorsion reciprocal unit with nu1 and m=log beta.
The four powers at exponents0,1,3,4 are Q-independent: a dependence would be a degree<=4 rational multiple of P, but its coefficient of t^2 is0 while P's is-2.
Since

    alpha^4=alpha^3+2alpha^2+alpha-1,
    (1-alpha-alpha^3+alpha^4)/2=alpha^2 in O0,

the coefficient half-coset IS integral at this input.
All sixteen sign choices are nonzero O0 values by that independence.
They form a genuine q2/M16/E1/width4 sign packet.
Fix epsilon4=+1; the eight integer values are

    u_(a,b,c)=alpha^2+b alpha+c alpha^3-a, (a,b,c) in{0,1}^3.

The remaining eight are their negatives, with the same signed degree4 norms.
Direct relative products u sigma(u) in F=Q(tau), using tau^2=tau+4 and tau^3=5tau+4, are:

| a,b,c | Relative product | Full signed norm |
| --- | --- | ---: |
| 0,0,0 | 1 | 1 |
| 1,0,0 | -tau | -4 |
| 0,1,0 | 2+tau | 2 |
| 0,0,1 | 2+tau | 2 |
| 0,1,1 | (1+tau)^2 | 4 |
| 1,1,0 | 1-tau | -4 |
| 1,0,1 | -3-2tau | -1 |
| 1,1,1 | -tau | -4 |

For the second row, (alpha^2-1)(alpha^-2-1)=4-tau^2=-tau.
Every listed full norm is the two-embedding norm in F of the displayed relative product, so all four ORIGINAL embeddings are counted.
The eight signed norms multiply to2^10; all sixteen to2^20.
Consequently this packet has primitive sign numerators, actual q2, FINAL M16, all copies1, integer energy4 and

    product_epsilon Res(P,2f_epsilon)=2^84,
    Lambda=surplus=5log2/16>0.                             (11)

Here U=A*m/d=m.
Since tau_+>5/2, beta+beta^-1>5/2 implies beta>2, so U>log2>K0.
The positive control therefore lies outside the small-U theorem and does not exhibit a near-one family.
It is a four-power sign packet, not a claim that these sixteen outputs arise from a particular four-by-four constant isometry with preserved labels.
No matrix realization, smallest energy, optimal packet or unrestricted mechanism is inferred.

<a id="four-power-author-check-and-limits"></a>
## 6. Reuse, verification, and remaining boundary

The new steps are the coefficient-coset doubling argument and its exact reduction to the already forbidden four-term dyadic sign packet.
C71 supplies the OLD all-weight E1 consequence; C74 supplies the OLD numerical margins; C84 supplies ONLY its adopted all-height binary-delay interface.
L229 supplies the actual coefficient-energy estimate, not an integrality theorem.
C50's old weight-two/three dyadic classification and restricted capacity do not already settle arbitrary coefficient denominators in the independent four-power span.
The preceding three-power draft/Claim covers a different rounding margin and automatic three-term independence; it is contextual and not a proof premise here.

Author checking reconstructed each distance inequality, the width-zero norm case, every independence use, all16 nonzero guards, exact sign covariance, every scalar and original norm exponent in(10), the true-polynomial weighted-energy argument, the complete mixed induction, and all eight relative products/norms in the control.
The theorem does not assert automatic four-power independence, saturation in arbitrary overorders, a five-power extension, a favorable factorization or the unrestricted income gate.
No floating root evaluation, symbolic-algebra program or mathematical native execution was used.
No independent review or adoption is asserted by this author account.


<a id="four-power-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T17:32.
Freeze this ENTIRE draft, including its original candidate, Sections1--6, Theorems1--2, equations1--11, exact fixed control and all dependency/role/scope boundaries, for a separate whole review.
Root is the proof author and cannot supply its independent finding.


<a id="four-power-sparse-source-boundary"></a>
## Sparse-source comparison and final review freeze

2026-10-12T17:33.
A subsequent bounded lookup actually read [DS17-U001](../audits/literature/DS17/Yin_U001.md#ds17-u001), C27 and D22's retained source account.
The accepted fixed-term gap applies to the TOTAL measure of a sparse integer polynomial F, with arbitrary coefficient heights.
A four-power dependence would only say that P divides such an F; m(F)=m(P)+m(F/P) can have a large cofactor contribution.
A lower bound on m(F) therefore supplies no lower bound on m(P), so this source does NOT remove the explicit four-power independence hypothesis in Theorems1--2.
This is an applicability boundary and credited existing result, not a new sparse theorem or a new foundational source audit.
The original freeze above is retained; this dated source-comparison paragraph is included in the ENTIRE final review target.
No equation or mathematical conclusion above changes.


<a id="four-power-automatic-independence"></a>
## 7. New extension: the fourth-power independence gate is automatic

The preceding complete proof and its explicit independence restriction remain as their original frozen scope.
At the actual time recorded below, [C87](Yin_C_G0087_v1.md#statement) has been separately whole/actual reviewed and [adopted](Yin_C_G0087_v1.md#decision-organized-reviewed).
Its THREE-power saturation supplies an additional argument resolving this restriction.
This is a NEW substantive extension, not a silent reinterpretation of an earlier independent finding.
Root authors the extension and cannot independently certify it.

**Theorem 3.**
For ANY four distinct integers a_i at A*m/d<=K0, the four powers alpha^(a_i) are Q-linearly independent.
Thus Theorem1's original-order saturation holds for ALL at-most-four distinct powers at this same threshold, without an extra independence assumption.

Assume a dependence.
C87 already makes every three distinct powers independent at this threshold, so it must be a minimal four-term relation

    sum_(i=1)^4 c_i alpha^(a_i)=0, c_i in Z minus{0},
    gcd(c_1,c_2,c_3,c_4)=1.                                (12)

For EACH index j, solve for alpha^(a_j) in the other three powers.
Its actual value is in O0.
Those three powers have spread at most A, so the adopted C87 saturation, restricted to O0, makes EVERY coefficient -c_i/c_j an integer.
Therefore every c_j divides every c_i.
Taking both directions for each pair gives equal absolute values; the primitive gcd in(12) forces

    c_i in{+1,-1} for ALL four indices.                    (13)

This mutual-divisibility step is crucial: an arbitrary rational four-term dependence does not initially have equal coefficients.
It uses actual THREE-power saturation, not only their independence, a sparse relation's measure bound, or an unproved ordinary-to-full-order transfer.

If P is NONRECIPROCAL, normalize(12) by its least exponent.
The resulting NONZERO rational polynomial has degree A and is divisible by the actual P, hence A>=d.
The exact accepted [Smy08-U002](../audits/literature/Smy08/Yin_U002.md#smy08-u002) Section1 nonreciprocal statement, already checked in C87 at the retained survey Section5.1 equation15, gives total m>=log(theta0)>K0.
Consequently A*m/d>=m>K0, a contradiction.
Only that accepted statement/interface is reused; the original1971 proof, equality classification and unrelated survey assertions are not newly inspected or adopted.
The comparison theta0>5/4 and log(5/4)>1/5>K0 is already proved locally in C87.
This branch would exclude ANY polynomial dependence at this span; it does not require changing total m into height m/d.

If P is RECIPROCAL, inversion alpha->alpha^-1 is an actual K automorphism.
Set u_i=c_i alpha^(a_i), all nonzero units in K.
Equations(12)--(13) and inversion give BOTH

    sum_i u_i=0, sum_i u_i^-1=0.                           (14)

Let e_j be their elementary symmetric functions.
Then e1=0 and e3=e4*sum_i u_i^-1=0, with e4 nonzero.
Thus the monic polynomial having these FOUR specified roots is

    product_(i=1)^4 (X-u_i)=X^4+e2 X^2+e4,                (15)

an EVEN polynomial.
If u1 is a root, so is -u1.
The polynomial already splits as the displayed product in K; hence -u1=u_j for some j.
Since u1 is nonzero and characteristic is0, j is not1.
It follows that alpha^(a_1-a_j)=-c_j/c_1 in{+1,-1}.
The exponents are distinct, contradicting nontorsion.
This proves automatic four-power independence in the reciprocal branch.
No circle conjugate, positivity of an embedding, four-term source theorem or distinct-root assumption for(15) is needed; even if root multiplicity were allowed, the displayed factorization still yields such a j.

These two branches prove Theorem3.
Applying Theorem1 now gives exact saturation of ANY at-most-four distinct powers in O0 at A*m/d<=K0.
The result is uniform in denominators, degree, exponent sizes outside their actual span and all original coefficients.
This does not contradict the source-boundary paragraph: DS17 alone still cannot transfer a sparse relation's lower measure bound to its factor P.
Here the new argument instead uses the already proved THREE-power saturation and reciprocal inversion to eliminate the relation.

<a id="four-power-resolved-word-frontier"></a>
## 8. Resolved constant-block and mixed-word conclusion

In Theorem2 and its mixed-word corollary, the at-most-four-distinct-powers condition now AUTOMATICALLY satisfies the earlier explicit independence gate at the stated cumulative threshold.
Therefore ANY finite word of rational constant isometries on blocks with at most FOUR DISTINCT current exponents, interleaved with the accepted arbitrary-height weighted binary delays and single-coordinate shifts, remains in the TRUE signed-monomial class whenever all weights/labels stay fixed, EVERY intermediate coordinate is nonzero in O0 and B_word*m/d<=K0.
Every block on at most four coordinates is included; a block on more labels is also included if it has only at most four distinct current exponents.
All q/M/copy/sign/window costs in Section4 are unchanged and the final full income/surplus is0.
Constants may change signs.
This is an O0 statement; the present dyadic argument does not assert a full-overorder four-power extension.

No fifth-power saturation or classification of general nonconstant three-coordinate factors follows.
The original Section3 exclusion of a dependent four-power block is now resolved by Theorem3 ONLY within these same small-cumulative-cost/legal/fixed-weight assumptions; it is retained as historical development and not repeated as a current unresolved gate.
The positive quartic control remains strictly outside the threshold, with its exact nontrivial half-coset and all full costs unchanged.
The unrestricted uniform-income requirement remains open.

The direct dependency graph is acyclic: C87 used only earlier L229/C74/Smy08/C84/C14 inputs, never this draft; this new fourth-power extension now uses adopted C87 saturation of three powers.
Root authored both proofs; the accepted independent reviews of C87 establish its inherited input scope, not an independent finding on the new Theorem3 or updated word theorem.
A separate reviewer must inspect the ENTIRE extended original, including Sections1--8 and the earlier freeze/source comparison, before any extraction.


<a id="four-power-extended-entire-author-freeze"></a>
## Extended entire author freeze

2026-10-12T17:37.
Freeze ENTIRE actual D43, preserving every earlier candidate, explicit-gate proof, original freeze and DS17 boundary, plus new Sections7--8/Theorem3/equations12--15 and the resolved unconditional-at-threshold word scope.
Author rechecked mutual coefficient divisibility using all four omitted-index bases, exact inversion/even-polynomial pairing, nonreciprocal total measure and original span, acyclic adopted dependency and all unchanged costs/controls.
The prior original-scope independent review, if fixed, does not automatically cover this extension.

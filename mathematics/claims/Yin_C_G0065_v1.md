---
author: Yin
---
# Short-row rigidity for universally order-preserving rational paraunitary matrices

Date: 2026-10-12T12:00.
Human author Yin.
Root authored the entire original D19 mathematical proof.
g0001_review_recovery independently reviewed its complete actual19:52 scope in R283 and NOW authors this new fixed statement/wrapper.
That contribution prevents a self-supplied independent actual-extraction review.
The complete original proof, antecedent/source/contributor history, all actual costs and scope boundaries are retained below.
Initial status is proof draft / under review; root will arrange a different noncontributor's actual extraction review before adoption.

## Statement

Let P(t)=sum_(i=0)^d p_i t^i be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, p_d=1, p_0 in{+1,-1}, every p_i in{0,+1,-1}, and support count n=#{i:p_i!=0}>=5.
Use the ACTUAL monogenic order O0=Z[alpha] and original field Q(alpha).
Reciprocity is NOT assumed.
Both alpha and alpha^-1 belong to O0.

For ANY positive integer M, let U(t) be an M-by-M matrix over Q[t,t^-1] satisfying the ACTUAL rational Laurent identity

    U(t) U(t^-1)^T=I_M.

Star here uses transpose and t inversion, with ordinary Euclidean coordinate weights.
No factorization or particular packet is assumed.
Each row is nonzero.
Define its ACTUAL row-union width as the largest exponent minus the smallest exponent across ALL its nonzero entries, rather than the largest individual entry width.

Assume BOTH

    U(alpha) O0^M is contained in O0^M,
    every ACTUAL row-union width is at most d.

The first condition is equivalent to EVERY matrix entry U_ij(alpha) belonging to O0, including entries whose value is zero: standard basis columns give necessity and the ring property gives sufficiency.
It is universal FORWARD preservation of the entire original-order module, not integrality on one selected packet or residue set.
No inverse-integrality assumption is imposed.

**A. Exact matrix classification, including the scalar case.**
There exist a permutation pi of{1,...,M}, signs epsilon_i in{+1,-1} and integer exponents a_i such that

    U_(i,pi(i))(t)=epsilon_i t^(a_i),
    U_(i,j)(t)=0 for j!=pi(i).

This is equality of the ACTUAL rational Laurent matrix, not only of its evaluation at alpha.
Its own actual coefficient denominator is therefore1.
The theorem includes M1, arbitrary differences between row positions and rows whose widths are strictly smaller than d.
Conversely every displayed signed monomial permutation satisfies the two hypotheses, with row widths0 and universal original-order preservation.

Consequently any genuinely mixing rational paraunitary matrix universally preserving O0^M for this input must have at least one ACTUAL row-union width>=d+1.
No single global span bound on all matrix entries or determinant-degree classification is substituted for the row condition.

**B. Complete local shell and charged zero-value entries.**
For every f in Q[t] of degree<=d with nonzero ACTUAL f(alpha) in O0,

    ||f||_2^2>=1-1/n.

If its value is NOT one of+/-alpha^j,0<=j<=d, then

    ||f||_2^2>=2-4/n>1.

The complete retained proof derives these bounds locally from f=z+cP, integer signed support coordinates and the outside-support integer squares.
It checks constant support, integer range>=2 and range1 with every multiplicity, including the two monomial equality patterns.
It does not assume a finite coefficient search, a chosen unit inventory, a maximal order or the separate D17/C62 second-shell result as a premise.

Normalize EACH whole row by its own common integer monomial.
This preserves paraunitarity and original-order membership and places every row entry in degree<=d.
The diagonal constant coefficient gives sum_j||V_ij||^2=1, so exactly one entry has nonzero original-order value; the remaining entries may initially be nonzero scalar multiples of P and are ALL charged.
The second floor forces the one nonzero value to equal epsilon alpha^j, hence that entry is epsilon t^j+cP and the others are c_lP.

Writing P*=P(t^-1) and A=c^2+sum_l c_l^2, the COMPLETE row identity is

    epsilon c[t^jP*+t^-jP]+A P P*=0.

If c0 it forces every correction zero.
If c!=0, evaluation at the ACTUAL alpha forces reciprocity up to p0; p0=-1 would imply P(1)=0 and violate irreducibility at degree>=2.
Thus P*=t^-dP, and division gives

    epsilon c[t^j+t^(d-j)]+A P=0.

Since A>0 and the first bracket has at most two terms while P has n>=5, this is impossible.
Every zero-value polynomial correction therefore vanishes.
Row orthogonality forces distinct selected columns, proving A.
This accounts for the j0/d and2j=d endpoint cases and distinguishes exact matrix rigidity from field-value agreement.

**C. Final composites and exact excluded interpretations.**
ANY finite product of rational Laurent paraunitary factors satisfies the same Laurent identity.
If its FINAL matrix also universally preserves O0^M and has the stated row widths, A applies regardless of intermediate factor denominators, integrality or support.
No factorization theorem is needed.
Thus later restoration in a composite cannot produce genuine universally integral mixing within these final row spans.

This does NOT exclude a matrix whose nonintegral entries happen to cancel on one specially tailored actual packet, integrality on a finite chosen residue set, or a wider universally integral word.
It does not assert that all support shortening is impossible: signed monomial rows can reposition separate coordinates.
The flat-input and n>=5 hypotheses provide the strict second shell; no analogous classification is asserted for support<=4, nonflat input or an overorder.
C53's earlier universal SINGLE-factor theorem and quadratic control remain separate results.

**D. Actual copied-packet arithmetic.**
Suppose an ACTUAL finite rational complementary packet with positive normalized FINAL weights is expanded using their actual least denominator M into M separately indexed coordinates f_1,...,f_M, EACH at weight1/M, with every original value nonzero in O0.
Only this equal-copy convention puts the packet into the ordinary Euclidean matrix identity above.
Let q be its ACTUAL common coefficient denominator and E its weighted coefficient energy.
A classified U gives

    g_i(t)=epsilon_i t^(a_i) f_(pi(i))(t).

Every output remains nonzero and in O0.
Coefficient energy and complete circle covariance are unchanged.
The ACTUAL coefficient denominator q is unchanged exactly; the unmerged equal-weight indexed list still has ACTUAL weight denominator M.
Merging identical labels later is a different representation whose actual final weight denominator must be recomputed.

Put

    nu=Norm_(Q(alpha)/Q)(alpha)=(-1)^d p0 in{+1,-1},
    D_j=Norm_(Q(alpha)/Q)(f_j(alpha)),
    D'_i=Norm_(Q(alpha)/Q)(g_i(alpha)).

Every norm uses ALL original d conjugates and retains its sign.
Then

    D'_i=epsilon_i^d nu^(a_i) D_(pi(i)),
    product_i D'_i=[product_i epsilon_i^d]nu^(sum_i a_i)product_j D_j.

For the ACTUAL integer Laurent numerators F_j=q f_j and G_i=qg_i, contents are preserved, the full original-root product of each G_i is q^d D'_i, and the complete indexed copied product is q^(dM)product_i D'_i.
Negative exponents are evaluated only at nonzero original conjugates; no ordinary-polynomial resultant is assigned to a negative-exponent polynomial.
After an actual single common monomial normalization, its corresponding original unit-norm sign is additionally retained, and ordinary resultants may then be used.

With the SAME actual q and indexed weights,

    Lambda=(1/(dM))sum_j log|D_j|
           =(1/(dM))sum_i log|D'_i|>=0,
    S_int=q^2E,
    I_income=logq+Lambda,
    I_income-(1/2)logS_int=Lambda-(1/2)logE.

Thus the COMPLETE surplus is unchanged, not merely coefficient energy.
No sign, content, original root or final copy is deleted.

**E. Physical width and inference limits.**
Each individual coordinate width is preserved by its signed monomial and permutation, so max_i width(g_i)=max_j width(f_j).
The common UNION width of the packet can nevertheless change under the separate row monomials.
It must be measured anew, after any needed common polynomial normalization, before applying the C10 original-root window inequality.
Equality of the old and new union widths, a cheap shortening for a given packet, and an absolute degree-linear window bound are not asserted.

The theorem classifies only universal original-order preservation within short ROW-union spans at the stated flat inputs.
It supplies no all-width or tailored-vector impossibility, full-profile optimum, new positive uniform Mahler gap or unrestricted G0001 completion.
Every new algebraic step is proved locally; no mathematical native program, pending extraction, external factorization or source-original theorem is used as a premise.

## Current assessment
[Selected decision](#decision-review-literal-corrected)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:00 |
| status | open |
| reason | Register the complete short-row universal original-order rigidity theorem, local integer shell, exact removal of all P-multiple corrections, arbitrary final-composite boundary and actual copied-packet q/M/signed-norm/width accounting. R283 covers the original complete19:52 D19 only; its reviewer now authors this wrapper, so a separate noncontributor must inspect the actual extraction before adoption. No wider or tailored-packet impossibility, native computation or unrestricted Task conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual flat original-unit/order domain, universal forward preservation, actual row-width hypothesis, exact matrix/scalar classification and full final-composite/copy/width limits. |
| argument | [Complete retained proof](#argument) | ENTIRE actual19:52 D19 allocation/reuse/contribution history, Sections1--7/equations1--11, full local shell, zero-value charges, reciprocity/support contradiction, all costs and author freeze. |
| dependency | [C25 original-order first-window reduction](Yin_C_G0025_v1.md#first-window-denominator-monic-fraction-reduction) | Actual monic power-basis membership gives f=z+cP at degree<=d; no overorder or norm-only substitute. |
| support | [C25 old complete individual floor](Yin_C_G0025_v1.md#statement) | Existing1-1/n floor attribution; the complete local shell used in the present argument is re-proved. |
| support | [C29 complete projected integer minimum](Yin_C_G0029_v1.md#flat-covariance-complete-integer-minimum) | Earlier all-integer support/outside/equality mechanism as credited context; no full-packet diagonal conclusion is substituted here. |
| support | [C53 universal SINGLE-factor boundary](Yin_C_G0053_v1.md#universal-order-preserving-projection-boundary) | Existing exact single-factor and actual-order statement, expressly not a prior theorem about arbitrary composites. |
| support | [C53 original copied-packet accounting](Yin_C_G0053_v1.md#delay-reduction-validity-and-full-costs) | Actual equal-indexed copies, distinct q/M, nonzero/integer guards and full signed norm/content costs; no general mixing norm-product invariance imported. |
| dependency | [C10 actual common-window expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the physical-width accounting interface after actual common normalization and measurement of the new union width, with all original roots and FINAL weights. Not a premise of matrix rigidity. |
| support | [Original complete independent finding](../audits/reviews/Yin_R_G0283_v1.md#short-row-universal-rigidity-whole-finding) | ENTIRE actual19:52 original D19 proof/interfaces only, not the new fixed statement written by that reviewer. |


### Decision organized-reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:08 |
| status | proved |
| reason | Adopt separate original whole R283 and actual extraction R284 findings, preserving the complete original proof and all actual order/row-width/cost boundaries. The exact matrix rigidity applies only to universal integrality with each row span at most d; it does not exclude tailored packets or wider matrices. No unrestricted Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual flat original-unit/order domain, universal forward preservation, actual row-width hypothesis, exact matrix/scalar classification and full final-composite/copy/width limits. |
| argument | [Complete retained proof](#argument) | ENTIRE actual19:52 D19 allocation/reuse/contribution history, Sections1--7/equations1--11, full local shell, zero-value charges, reciprocity/support contradiction, all costs and author freeze. |
| dependency | [C25 original-order first-window reduction](Yin_C_G0025_v1.md#first-window-denominator-monic-fraction-reduction) | Actual monic power-basis membership gives f=z+cP at degree<=d; no overorder or norm-only substitute. |
| support | [C25 old complete individual floor](Yin_C_G0025_v1.md#statement) | Existing1-1/n floor attribution; the complete local shell used in the present argument is re-proved. |
| support | [C29 complete projected integer minimum](Yin_C_G0029_v1.md#flat-covariance-complete-integer-minimum) | Earlier all-integer support/outside/equality mechanism as credited context; no full-packet diagonal conclusion is substituted here. |
| support | [C53 universal SINGLE-factor boundary](Yin_C_G0053_v1.md#universal-order-preserving-projection-boundary) | Existing exact single-factor and actual-order statement, expressly not a prior theorem about arbitrary composites. |
| support | [C53 original copied-packet accounting](Yin_C_G0053_v1.md#delay-reduction-validity-and-full-costs) | Actual equal-indexed copies, distinct q/M, nonzero/integer guards and full signed norm/content costs; no general mixing norm-product invariance imported. |
| dependency | [C10 actual common-window expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the physical-width accounting interface after actual common normalization and measurement of the new union width, with all original roots and FINAL weights. Not a premise of matrix rigidity. |
| support | [Original complete independent finding](../audits/reviews/Yin_R_G0283_v1.md#short-row-universal-rigidity-whole-finding) | ENTIRE actual19:52 original D19 proof/interfaces only, not the new fixed statement written by that reviewer. |
| review | [Actual independent extraction](../audits/reviews/Yin_R_G0284_v1.md#c65-short-row-actual-extraction-finding) | Complete actual A--E, entire retained argument/preservation and all current direct interfaces, independently inspected after allocation by a noncontributor. |


### Decision review-literal-corrected

| Field | Value |
| --- | --- |
| date | 2026-10-12T12:43 |
| status | proved |
| reason | Select the actual reviewer-authored R284v2 at the SAME mathematical scope after its explicit repair of malformed square characters. Original v1 and earlier Claim decision remain historical; the reviewer re-read the actual affected formulas and preserved the complete finding and role/source limits. This changes the selected literal review evidence, not this Claim proof or scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual flat original-unit/order domain, universal forward preservation, actual row-width hypothesis, exact matrix/scalar classification and full final-composite/copy/width limits. |
| argument | [Complete retained proof](#argument) | ENTIRE actual19:52 D19 allocation/reuse/contribution history, Sections1--7/equations1--11, full local shell, zero-value charges, reciprocity/support contradiction, all costs and author freeze. |
| dependency | [C25 original-order first-window reduction](Yin_C_G0025_v1.md#first-window-denominator-monic-fraction-reduction) | Actual monic power-basis membership gives f=z+cP at degree<=d; no overorder or norm-only substitute. |
| support | [C25 old complete individual floor](Yin_C_G0025_v1.md#statement) | Existing1-1/n floor attribution; the complete local shell used in the present argument is re-proved. |
| support | [C29 complete projected integer minimum](Yin_C_G0029_v1.md#flat-covariance-complete-integer-minimum) | Earlier all-integer support/outside/equality mechanism as credited context; no full-packet diagonal conclusion is substituted here. |
| support | [C53 universal SINGLE-factor boundary](Yin_C_G0053_v1.md#universal-order-preserving-projection-boundary) | Existing exact single-factor and actual-order statement, expressly not a prior theorem about arbitrary composites. |
| support | [C53 original copied-packet accounting](Yin_C_G0053_v1.md#delay-reduction-validity-and-full-costs) | Actual equal-indexed copies, distinct q/M, nonzero/integer guards and full signed norm/content costs; no general mixing norm-product invariance imported. |
| dependency | [C10 actual common-window expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only the physical-width accounting interface after actual common normalization and measurement of the new union width, with all original roots and FINAL weights. Not a premise of matrix rigidity. |
| support | [Original complete independent finding](../audits/reviews/Yin_R_G0283_v1.md#short-row-universal-rigidity-whole-finding) | ENTIRE actual19:52 original D19 proof/interfaces only, not the new fixed statement written by that reviewer. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0284_v2.md#c65-short-row-actual-extraction-finding) | Complete actual A--E, entire retained argument/preservation and all current direct interfaces, independently inspected after allocation by a noncontributor. |

## Registration and complete preservation

Date: 2026-10-12T12:00.
The actual D19 author body below is retained in full, with only repeated author front matter removed, its first title demoted once and final whitespace normalized.
Valid original relative links are preserved.
No mathematical step, source/reuse/contributor paragraph, scalar/row/composite distinction, actual arithmetic cost, physical-width qualification or author-freeze scope is removed.

The original discussion of D17 as an author antecedent rather than a fixed premise remains at its historical scope.
The entire needed shell proof is locally present, so this extraction does not turn a later C62 status into a proof premise.
The old paraunitary/source vocabulary remains under C53's actual accepted attribution limits; no new source theorem, source acquisition or native run accompanies extraction.

The extractor's completed R283 review remains at its original whole scope.
This new wrapper is an author contribution and requires a different noncontributor's actual statement/body/interface review.
Initial status stays proof draft / under review.
No adoption, original draft/proof edit or retirement is made here.

## Argument

## Universal order-preserving paraunitary words cannot mix short rows at flat inputs

Date: 2026-10-12T11:44.
Human author Yin.
Root AUTHOR continuation; root supplies the short-row/full-matrix rigidity candidate and cannot independently review it.
No mathematical native program or new external theorem/source is planned.

## Bounded reuse and changed scope

Read the actual [C53](Yin_C_G0053_v1.md#statement) general-unit delay and universal SINGLE-factor result, its source/reuse boundary and explicit absence of a composite-word theorem.
[C25](Yin_C_G0025_v1.md#statement) and [C29](Yin_C_G0029_v1.md#statement) give the flat first-window integer floor and projected-lattice equality.
Root's separate D17 develops a full all-residue second-shell bound and is whole-reviewed but not yet adopted as a Claim; it is credited as the current author antecedent, not silently used as a fixed premise.
A bounded G-Claim search found no full arbitrary paraunitary-word rigidity under a short ROW-union support assumption.
This is not a novelty assertion.
The rational paraunitary identity itself is old vocabulary retained through C53/L380, not a new factorization theorem.

## Candidate theorem and exact distinction

For an ACTUAL flat monic irreducible nontorsion integer-unit P of degree d, support count n>=5, consider ANY rational Laurent square matrix U(t) with U(t)U(t^-1)^T=I and EVERY entry of U(alpha) in actual O0=Z[alpha].
The latter is precisely universal forward preservation of O0^M, by testing standard basis columns; it is not a condition on one specially tailored packet.
Allow arbitrary composite words/factor denominators, no factorization assumption.
If every ROW's actual union support width is at most d, the candidate conclusion is that U is EXACTLY a signed monomial permutation matrix.
Thus any universally integral genuine mixing word needs at least one row span>=d+1.
No all-width or tailored-packet impossibility is claimed.

## Proposed proof and retained obligations

Normalize EACH row by its own common integer monomial, which preserves paraunitarity and actual entry integrality because alpha is an O0 unit.
Each normalized row has sum of coefficient squared norms1 and every entry degree<=d.
The old individual floor a=1-1/n shows at most one entry can have a nonzero integral residue.
The row cannot have none, since otherwise every entry is a scalar multiple of P and its squared Laurent sum cannot equal1 at a root.
The new second-shell calculation b=2-4/n>1 for n>=5 would force that one nonzero residue to equal +/-alpha^j for j in[0,d].
Give the complete local integer-range proof again if the fixed antecedent is not yet adopted.

Write its polynomial f=epsilon t^j+cP and every other entry c_lP.
The row norm identity becomes epsilon c(t^jP*+t^-jP)+A P P*=0, A=c^2+sum c_l^2.
If c0, all coefficients vanish.
If c!=0, evaluation at alpha forces P*(alpha)=0, so actual irreducibility makes P reciprocal up to p0.
The p0=-1 antiself case would force P(1)=0 and is excluded by degree>=2 minimality.
Hence P*=t^-dP; division gives epsilon c(t^j+t^(d-j))+A P=0, impossible for support n>=5 since the first polynomial has at most two terms.
Therefore all P-multiple corrections vanish, every row has exactly one signed monomial polynomial, and row orthogonality forces distinct columns.

All zero-entry cases, field/order/original-degree signs, common versus independent ENTRY shifts, row normalization, polynomial irreducibility/divisibility, row-support endpoints and matrix-size cases need complete proof below.
Exact matrix coefficient denominator would be1 after rigidity; when acting on an actual copied packet it only permutes coordinates and applies unit monomials, preserving norm magnitudes and coefficient energy but possibly changing union width.
Do not infer preservation of zero output coordinates or a cheap width change for a particular vector from universal matrix preservation.
This is developing author work, unadopted, with substantive proof to continue here.


<a id="short-row-universal-paraunitary-domain"></a>
## 1. Exact universal matrix domain and theorem

Fix the ACTUAL monic irreducible minimal polynomial P(t)=sum_(i=0)^d p_i t^i of a nontorsion algebraic integer unit alpha, d>=2,p_0=+/-1,p_d=1, every p_i in{0,+/-1}, and support count n>=5.
Use the actual monogenic order O0=Z[alpha] and original degree d.
No reciprocity is assumed.
Since alpha is a unit and P is monic with constant+/-1, alpha and alpha^-1 belong to O0.

For an arbitrary positive integer M let U(t) be an M-by-M matrix with entries in Q[t,t^-1], satisfying the ACTUAL rational Laurent identity

    U(t) U(t^-1)^T=I_M.                             (1)

This is the ordinary Euclidean paraunitary condition.
No factorization, individual factor denominator, real/complex existence theorem, degree profile or particular input packet is assumed.
For every row, take the minimum and maximum exponent across ALL its nonzero entries and call their difference its actual ROW-union width.
A row is nonzero by(1), so these two finite extrema exist.

Assume

    U(alpha)O0^M is contained in O0^M,
    every row-union width is at most d.             (2)

The first condition is equivalent to EVERY entry U_ij(alpha) belonging to O0, since standard basis vectors test necessity and O0 is a ring for sufficiency.
It is universal FORWARD preservation of all original-order vectors.
It is not a statement about a selected packet, a finite residue subset, a maximal order, or individual factors of a composite word.
No independent assumption on the inverse's integrality is made.

**Theorem.**
Under(1)--(2) there are a permutation pi of{1,...,M}, signs epsilon_i in{+/-1} and integer exponents a_i such that

    U_(i,pi(i))(t)=epsilon_i t^(a_i),
    U_(i,j)(t)=0 when j!=pi(i).                     (3)

Thus the ACTUAL Laurent matrix, not just its value at alpha, is a signed monomial permutation.
Conversely every matrix(3) satisfies(1)--(2), with every row width0 and actual universal order preservation.
In particular any genuinely mixing rational paraunitary matrix that universally preserves O0^M for this input has at least one row-union width>=d+1.
This is not an all-width or tailored-vector impossibility theorem.

<a id="short-row-integer-shell-lemma"></a>
## 2. Complete local integer shell lemma, with old interfaces credited

We need the following actual first-window facts, with proofs given here so that no pending D17 result is a premise.
Let f in Q[t],deg f<=d, have nonzero f(alpha) in O0.
The accepted C25 monic-order argument gives f=z+cP for integer z and rational c.
Let S be the support of P, x_i=p_i z_i for i in S, mu their mean, and b=sum_(j notin S)z_j^2.
Euclidean projection perpendicular to P gives

    ||f||^2>=b+sum_(i in S)(x_i-mu)^2.              (4)

All x_i and outside z_j are integers.
The old complete floor is

    ||f||^2>=1-1/n.                                (5)

Moreover, if f(alpha) is NOT one of+/-alpha^j,0<=j<=d, then

    ||f||^2>=2-4/n>1.                              (6)

Here is the complete integer case check.
If all x_i equal an integer k, subtract kP; b0 would give zero residue and is forbidden, b1 gives exactly one signed outside coordinate and thus a monomial value, and otherwise b>=2.
If the integer range of x is at least2, the minimum and maximum terms alone have squared deviation sum at least half that range squared, hence at least2.
If the range is1, write x_i=k or k+1 with r high entries,1<=r<=n-1.
Their squared deviation sum is r(n-r)/n, at least1-1/n.
If b>=1, adding the outside integer square gives at least2-1/n.
If b0 and r1 or r=n-1, subtract kP or(k+1)P to get exactly one signed coordinate and a monomial value.
The remaining cases2<=r<=n-2 have variance at least2(n-2)/n=2-4/n.
This proves(5)--(6).
The final strictness in(6) is exactly where n>=5 is used.

C25 already owns(5), and C29 owns the associated all-integer projected-form minimum/equality boundary.
The second-shell calculation is also in root's earlier author D17; this local proof credits that antecedent without treating a not-yet-adopted extraction as evidence.
It needs no named lattice theorem, native search, unit classification beyond these finitely many monomials, or reciprocal assumption.
Values of other algebraic units are not excluded by definition; they simply obey the same nonmonomial energy floor when they are not among those listed powers.

<a id="short-row-normalization-and-values"></a>
## 3. Normalize whole rows, then count all nonzero integral entries

For row i let its least actual exponent be b_i.
Left multiply U by the diagonal Laurent matrix with i-th entry t^(-b_i); call the resulting matrix V.
Then

    V(t)V(t^-1)^T=I_M,
    V_ij in Q[t], deg V_ij<=d,
    V_ij(alpha) in O0.                             (7)

The first identity follows because each diagonal monomial and its star multiply to1.
Actual integrality follows from alpha^-b_i being an O0 unit.
This operation shifts each ENTIRE row together, not each matrix entry separately; it preserves every row width.
No single global support-span bound on all of U is needed.

The constant coefficient of the i-th diagonal identity in(7) gives

    sum_j ||V_ij||^2=1.                            (8)

Every nonzero actual residue among these entries contributes at least1-1/n by(5).
Since2(1-1/n)>1, a row has at most ONE such entry.
It cannot have none: if all its values vanish at alpha, minimality and degree<=d imply every entry is a rational scalar c_j P.
Its row identity would be A P(t)P(t^-1)=1 with A=sum c_j^2, which evaluated at alpha gives0=1.
Evaluation is legitimate because alpha is nonzero and every expression is a Laurent polynomial.
Thus each row has EXACTLY one nonzero integral residue.

That single entry has squared coefficient norm<=1 by(8), so(6) forces its actual value to be epsilon alpha^j for some epsilon=+/-1 and0<=j<=d.
Write it as

    f(t)=epsilon t^j+cP(t),

with c rational, by actual minimality and degree.
Every other row entry is c_lP with c_l rational.
No zero-valued matrix entry is silently dropped from (8) or the Laurent identity; their full squared norms are part of the next step.

<a id="short-row-zero-corrections-cannot-hide"></a>
## 4. The row identity forbids every nontrivial P-multiple correction

Write P*(t)=P(t^-1) and A=c^2+sum_l c_l^2>=0.
The FULL row identity, including all its zero-valued entries, is

    epsilon c[t^j P*(t)+t^-j P(t)]+A P(t)P*(t)=0.   (9)

If c0, the integral-domain property of Q[t,t^-1] and P nonzero give A0, hence every c_l0; the row already has only epsilon t^j.
Suppose instead c!=0.
Evaluating(9) at the actual alpha gives epsilon c alpha^j P*(alpha)=0, so P*(alpha)=0.
Therefore the reversed polynomial R(t)=t^dP(t^-1) has alpha as a root.
It has rational integer coefficients, degree d and leading coefficient p0.
Actual irreducibility and monicity imply

    R(t)=p0 P(t).

If p0=-1, evaluating this identity at1 gives P(1)=-P(1), hence P(1)=0, contradicting irreducibility at degree d>=2.
Thus p0=1 and P is reciprocal: P*(t)=t^-dP(t).
Substitute into(9) and divide the NONZERO Laurent factor t^-dP(t) to obtain

    epsilon c[t^j+t^(d-j)]+A P(t)=0.              (10)

Because c!=0, A>=c^2>0.
But t^j+t^(d-j) has at most two nonzero coefficient positions (one if2j=d), whereas P has n>=5.
They cannot be scalar multiples.
This contradicts(10), proving c0 and then A0 after all.
The argument keeps the general p0 sign until reciprocity is actually forced; it does not assume a reciprocal field involution on an arbitrary input.

Every normalized row therefore consists of exactly one signed monomial polynomial.
If two different rows chose the same column, their off-diagonal product in V(t)V(t^-1)^T would be a nonzero signed monomial, contradicting orthogonality.
Thus their columns are distinct.
A square M-by-M matrix with M such distinct choices uses every column exactly once.
Undoing each whole-row shift proves(3).
This includes M1, where the matrix is scalar, and rows whose original span is strictly smaller than d.
The proof uses neither a determinant-degree assertion nor integrality of an inverse.

<a id="short-row-universal-versus-particular"></a>
## 5. Full composite-word meaning and the particular-packet boundary

Any finite composite of rational Laurent paraunitary factors has property(1) by matrix multiplication.
If the FINAL matrix also obeys universal order preservation and the row-width bound(2), the theorem applies to that FINAL matrix, regardless of whether individual factors preserve O0 or have large intermediate denominators.
Hence composite restoration cannot produce a genuinely mixing universally integral matrix within these row spans.
This is a different conclusion from C53's universal SINGLE delay-factor criterion and does not claim all composite words fail at every width.

A matrix could send ONE specially chosen actual packet vector to integral nonzero entries even when some of its own entries U_ij(alpha) are nonintegral.
Standard basis testing is then unavailable and(2) fails.
The present theorem does not exclude such tailored vectors, cancellation among their values, a finite chosen residue set or wider universal words.
It also does not say all legitimate support shortening is impossible: signed monomial rows can independently reposition coordinate supports.

The n>=5 and flat-input hypotheses have specific roles.
They give the complete integer shell and its strict second floor>1.
No analogous rigidity is inferred for n4, trinomial/quadratic inputs, nonflat polynomials, or a changed overorder.
The old C53 quadratic loss-of-integrality example remains a separate control.
No new full-profile optimum or gap theorem is deduced from this matrix classification.

<a id="short-row-actual-packet-costs"></a>
## 6. Actual copied-packet costs under the remaining legal matrices

For clarity, suppose an ACTUAL finite complementary packet was expanded using its FINAL rational weights into M coordinates f_1,...,f_M with equal indexed weights1/M, every value nonzero in O0.
Only this equality-weight expansion places it in the ordinary Euclidean matrix convention(1); no weighted factorization is silently substituted.
A matrix(3) sends it to

    g_i(t)=epsilon_i t^(a_i) f_(pi(i))(t).

Every output value remains nonzero and integral because alpha is a unit.
Coefficient energy and complete circle covariance are unchanged.
The ACTUAL least common coefficient denominator q is unchanged: multiplication by signs/monomials and permutation preserves every coefficient denominator and their lcm.
The equal-weight INDEXED family still has least denominator M.
Merging identical labels afterwards creates a different representation whose actual weight denominator must be recomputed; no unmerged formula is assigned to that new one.

Write nu=Norm_(Q(alpha)/Q)(alpha)=(-1)^d p0 in{+/-1}, D_j=Norm_(Q(alpha)/Q)(f_j(alpha)).
Then

    Norm(g_i(alpha))=epsilon_i^d nu^(a_i)D_(pi(i)),
    product_i Norm(g_i(alpha))
       =[product_i epsilon_i^d]nu^(sum_i a_i)product_j D_j.
                                                            (11)

All absolute norm income is exactly preserved.
For actual numerators F_j=q f_j and G_i=qg_i, integer Laurent numerator contents are preserved and full original-root products are q^d times these signed norms.
Their complete indexed copied product is q^(dM) times the signed product in(11).
Negative exponents cause no ambiguity in evaluation because alpha is nonzero; after a single common polynomial normalization its original unit-norm sign is additionally retained.
No nonexistent ordinary-polynomial resultant with a negative exponent is asserted.

The coefficient charge is still q^2 E and I_income is still logq+Lambda, with SAME actual q and FINAL weights, so the full surplus Lambda-(1/2)logE is unchanged.
The ACTUAL common union width can change under the separate row monomials and must be measured anew before applying C10.
In particular max_i individual_width(g_i)=max_i individual_width(f_i) is unchanged, but equality of the two common union widths is not asserted.
The theorem forbids genuine universal mixing under(2); it does not forbid an already available scalar coordinate relocation or supply a degree-linear width bound for a given packet.

<a id="short-row-complete-author-freeze"></a>
## 7. Complete author self-check and frozen scope

Root checked the actual flat monic-unit and n>=5 domain, forward-universal versus particular-vector equivalence, matrix and row-span definitions and M1; whole-row normalization and unit integrality; every integer shell case including sparse outside coefficients and genuine value monomials; the count of nonzero residues with ALL zero-valued entries still charged; polynomial remainder scalar form and reciprocal/nonreciprocal evaluation; p0=-1 exclusion by P(1), the2j=d and j0/d endpoint monomials, positivity of A and support contradiction; distinct columns and exact matrix rather than field-value rigidity; composite-final versus individual factors, actual q/FINAL M/content/signed costs and changed union width.
The local proof is complete with no factorization, source-original theorem, native program, scan, formal assistant or unadopted antecedent as premise.
Author checking is not independent evidence.

Freeze the ENTIRE allocation/reuse/contribution account and Sections1--7/equations1--11 at 2026-10-12T11:52.
Root alone authored the candidate and proof and cannot independently review it.
Whole noncontributor review, any actual later Claim extraction review and adoption remain separate.
No new allowance or unrestricted G0001 conclusion is asserted.

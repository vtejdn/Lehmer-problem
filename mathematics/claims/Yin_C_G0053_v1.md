---
author: Yin
---
# Exact original-order gates for multicoordinate rational delay reduction

Date: 2026-10-12T09:54.
Human author Yin.
g0001_width authored the original complete D9 proof.
Root independently whole-reviewed that proof in R257 and NOW contributes this new fixed statement/wrapper, so root cannot independently review its own extraction.
The ENTIRE original author account is preserved below.
A distinct noncontributor actual extraction finding remains necessary before adoption.

## Statement

Let P(t)=t^d+a_(d-1)t^(d-1)+...+a_1t+a_0 be an ACTUAL monic irreducible nontorsion integer-unit minimal polynomial, d>=2,a_0 in{+1,-1}, alpha a root and O0=Z[alpha].
Reciprocity is NOT required.
Begin with a finite rational Laurent complementary packet, positive normalized rational FINAL weights, actual NONZERO O0 values, energy E>0 and ACTUAL least final-weight denominator M.
Replicate its actual positive integer multiplicities to an M-component vector F with indexed weights1/M; after ONE common monomial its actual support lies in[0,T] with endpoints attained and F*F=ME.
Here star is transpose and t->t^-1, and q is the actual coefficient denominator, distinct from M.
Original monomial norm signs are retained.

**A. Old analytic degree step with actual costs.**
For T>=1 write F=sum_(j=0)^T c_jt^j, c_T!=0, and let v in Z^M be primitive with c_T a nonzero rational multiple of v.
Put

    s=v^T v>=1, Pi=vv^T/s,
    U(t)=I-Pi+t^-1Pi, G=UF.

Then U*U=I, detU=t^-1, G is ordinary rational polynomial of degree<=T-1, G*G=ME, and its actual least coefficient denominator q' divides q s.
The extreme lag kills the negative endpoint and the projection kills the old top endpoint.
This is the old rational delay mechanism, locally written for the finite unweighted vector; covariance/rationality alone do not assert actual integral or nonzero output values.
No step is performed at T0.

**B. Exact particular-vector arithmetic gate and full finite count.**
Put u=F(alpha), z=v^Tu.
Then

    G(alpha)=u+(alpha^-1-1)v z/s.

ALL new coordinates belong to O0 if and only if

    (alpha^-1-1)z in sO0,
    equivalently (alpha-1)z in sO0.

Each new value being NONZERO is a separate necessary condition.
In the COMPLETE ring R_s=O0/sO0, cardinal s^d, the annihilator of alpha-1 has exact size gcd(s,|P(1)|).
Since primitive v gives a surjective dot-product map, the number and fraction of ALL residue vectors in R_s^M satisfying the gate are

    gcd(s,|P(1)|) s^(d(M-1)),
    gcd(s,|P(1)|)/s^d.

Every prime power and repeated factor is retained, including s1.
These are ALL-residue counts, not probabilities assigned to actual complementary packet data.
When gcd(s,P(1))=1 the gate is exactly z in sO0; P(1)=+/-1 implies this for every s.
No maximal-order or squarefree substitution is allowed.

**C. Universal SINGLE-factor boundary.**
For ANY rational symmetric idempotent Pi of any rank, U(alpha)O0^M is contained in O0^M if and only if Pi is an integer matrix, if and only if Pi is diagonal with entries0 or1.
In that case U(alpha) is an order-lattice automorphism.
For the primitive rank-one factor, this is equivalent to v being a signed coordinate vector, or s1.
The actual power-basis coefficient of alpha^(d-1) in alpha^-1-1 is+/-1 and is essential.
This does not classify a mixed factor on one specific vector or a finite product that restores integrality after illegal intermediate values.

**D. Admissibility and complete transformed arithmetic.**
Keeping all M labels at weight1/M requires BOTH the B gate and all outputs nonzero.
If0<E<1, the OLD C14 short-support floor means a sequence preserving these conditions cannot reach physical width<d; if attempted, a guard fails by step T-d+1 at latest.
This permits legal reductions above that floor and gives no uniform near-one restriction on every matrix mechanism.

At any LEGAL transformed packet, after any needed common monomial, retain its actual q', transformed full SIGNED original norms D'_i, each positive copy1 and integer numerators H_i=q'G_i.
Then

    Res(P,H_i)=(q')^d D'_i,
    product_i Res(P,H_i)=(q')^(dM) product_i D'_i,
    S_int=(1/M)sum_i ||H_i||_2^2=(q')^2E,
    I'=log q'+Lambda', Lambda'=(1/(dM))sum_i log|D'_i|>=0,
    I'-(1/2)log S_int=Lambda'-(1/2)log E.

All contents and monomial signs remain.
After loss of integrality the algebraic norm/resultant identities still hold but the nonnegative integer-norm floor is unavailable.
detU(alpha) being a field unit does NOT preserve the product of coordinate norms.
There is no free coefficient/weight denominator or deletion of zero outputs with unchanged energy.

**E. Complete actual q3 countercontrol.**
For the ACTUAL P=t^2-3t+1 and alpha^2=3alpha-1, take the old C20 optimal packet replicated into

    F=((1+t^2)/3,(1+t^2)/3,(2-t^2)/3)^T,
    E=1/3,M=3,q=3,T=2,
    u=(alpha,alpha,1-alpha), Norm(u_i)=(1,1,-1).

Its primitive leading direction is v=(1,1,-1),s3,z=alpha^2.
Analytic reduction gives G=((1+t)/3,(1+t)/3,(2-t)/3), actual T'=1,q'=3 and G*G=1.
The gate FAILS: (alpha^-1-1)z=1-2alpha notin3O0.
Every output is nonzero but nonintegral; its signed full norms are5/9,5/9,-1/9.
Original numerator resultants9,9,-9 have product-3^6; transformed5,5,-1 have product-25.
Both normalized integer energies are3, but the transformed Lambda'=(log5)/3-log3<0.
The same second analytic factor gives the constant vector(2,2,1)/3, still nonintegral, with numerator product16.
All expansions are exact hand algebra.
This is a FIXED positive-measure control, not a near-one family or an admissible width1 packet.

No theorem here supplies a successful uniformly bounded word, generic failure probability, preserved coordinate norm inventory, or impossibility for all coordinate-replacing constructions.
The exact modular/nonzero conditions are the remaining arithmetic work; unrestricted G0001 is unresolved.

## Current assessment
[Selected decision](#decision-sufficient-rational-delay-home)

## Historical assessments

These noncurrent original assessments retain their exact fields, selections and dates.
They are historical records and do not select a current assessment.

<a id="decision-initial"></a>
### Historical assessment initial

| Field | Value |
| --- | --- |
| date | 2026-10-12T09:54 |
| status | proof draft |
| review-status | under review |
| reason | Register exact original-order projection gates, full finite counts and the actual quadratic failure control with the entire original proof preserved. R257 covers the original whole author freeze only; root now contributes this wrapper and a separate noncontributor actual extraction finding is required. No uniform matrix realization or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, general actual unit scope, particular versus universal single-factor tests, finite count and full costs/limits. |
| argument | [Complete original proof](#argument) | Entire D9 Sections1--8/Theorems1--2/equations1--17 and17:33 freeze, starting source/reuse/roles and stream-recovery facts. |
| dependency | [Old rational factor mechanism](../ledger/Yin_L_G0380_v1.md#rational-weighted-delay-factorization) | Classical local delay mechanism, with its exact rational/source/quotient limits; unweighted finite-vector algebra supplied locally. |
| dependency | [Old actual short-width floor](Yin_C_G0014_v2.md#statement) | Original O0, all nonzero integral values and positive normalized rational weights; no reciprocity needed. |
| dependency | [Actual quadratic optimum](Yin_C_G0020_v1.md#statement) | Only actual a3 attainer and original costs; transformed gates and all new arithmetic computed locally. |
| support | [Accepted C20 noncontributor review](../audits/reviews/Yin_R_G0746_v1.md#c20-quadratic-parameter-extraction-finding) | Exact already adopted antecedent scope, preserving upstream root contribution and no new antecedent self-review. |
| support | [Entire original D9 review](../audits/reviews/Yin_R_G0257_v1.md#delay-gate-whole-independent-finding) | Original17:33 whole proof only; root's later wrapper contribution cannot supply actual extraction acceptance. |

## Assessment history

### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:06 |
| status | proved |
| reason | Adopt the actual noncontributor extraction/interface finding and the separately fixed whole-author finding at their exact scopes. Entire proofs, source/contribution/correction history and all finite costs remain. Conditional uniform selection, particular versus universal single-factor preservation and unrestricted Task completion are not inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, general actual unit scope, particular versus universal single-factor tests, finite count and full costs/limits. |
| argument | [Complete original proof](#argument) | Entire D9 Sections1--8/Theorems1--2/equations1--17 and17:33 freeze, starting source/reuse/roles and stream-recovery facts. |
| dependency | [Old rational factor mechanism](../ledger/Yin_L_G0380_v1.md#rational-weighted-delay-factorization) | Classical local delay mechanism, with its exact rational/source/quotient limits; unweighted finite-vector algebra supplied locally. |
| dependency | [Old actual short-width floor](Yin_C_G0014_v2.md#statement) | Original O0, all nonzero integral values and positive normalized rational weights; no reciprocity needed. |
| dependency | [Actual quadratic optimum](Yin_C_G0020_v1.md#statement) | Only actual a3 attainer and original costs; transformed gates and all new arithmetic computed locally. |
| support | [Accepted C20 noncontributor review](../audits/reviews/Yin_R_G0746_v1.md#c20-quadratic-parameter-extraction-finding) | Exact already adopted antecedent scope, preserving upstream root contribution and no new antecedent self-review. |
| support | [Entire original D9 review](../audits/reviews/Yin_R_G0257_v1.md#delay-gate-whole-independent-finding) | Original17:33 whole proof only; root's later wrapper contribution cannot supply actual extraction acceptance. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0260_v1.md#c53-delay-gate-extraction-finding) | Actual statement, complete retained proof, preservation and present direct interfaces, separate from original whole scope. |


### Decision sufficient-rational-delay-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:12 |
| status | proved |
| reason | Use the complete sufficient accepted home of the same exact prior rational factor/orbit/fixed-vector pole interface. Preserve the original domain and scope, all other tuples/fields, current review, old decisions and actual historical reading inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, general actual unit scope, particular versus universal single-factor tests, finite count and full costs/limits. |
| argument | [Exact argument](#argument) | Entire D9 Sections1--8/Theorems1--2/equations1--17 and17:33 freeze, starting source/reuse/roles and stream-recovery facts. |
| dependency | [Exact dependency](Yin_C_G0441_v1.md#rational-weighted-delay-factorization) | Classical local delay mechanism, with its exact rational/source/quotient limits; unweighted finite-vector algebra supplied locally. |
| dependency | [Exact dependency](Yin_C_G0014_v2.md#statement) | Original O0, all nonzero integral values and positive normalized rational weights; no reciprocity needed. |
| dependency | [Exact dependency](Yin_C_G0020_v1.md#statement) | Only actual a3 attainer and original costs; transformed gates and all new arithmetic computed locally. |
| support | [Exact support](../audits/reviews/Yin_R_G0746_v1.md#c20-quadratic-parameter-extraction-finding) | Exact already adopted antecedent scope, preserving upstream root contribution and no new antecedent self-review. |
| support | [Exact support](../audits/reviews/Yin_R_G0257_v1.md#delay-gate-whole-independent-finding) | Original17:33 whole proof only; root's later wrapper contribution cannot supply actual extraction acceptance. |
| review | [Exact review](../audits/reviews/Yin_R_G0260_v1.md#c53-delay-gate-extraction-finding) | Actual statement, complete retained proof, preservation and present direct interfaces, separate from original whole scope. |

## Registration and preservation

Date: 2026-10-12T09:54.
The complete original author body is preserved below with only author front matter removed, first title demoted, relative Claim links rebased and final whitespace normalized.
Every substantive statement, proof, exact example, cost/source/contribution boundary, original author-check and freeze remains.
Original pending language is historical.
Root's earlier noncontributor whole review remains independent at its original target; root's authorship of this new statement means a different noncontributor must review the actual fixed extraction.
No classical source scope is enlarged.

## Argument

## Arithmetic gates for multicoordinate rational delay reduction

Date: 2026-10-12T09:24.
Human author Yin.
New AUTHOR inquiry under the current root-coordinated G0001 continuation.
The root assigned the broad nonscalar quantitative question but supplied no projection/congruence/counting or control formula for this inquiry.
This author chooses the exact single-factor integrality gate.
This newly allocated rolling address has no inherited scope from prior use.

## Question and starting scope

Test an actual route around retained-coordinate scalar width floors: a rational paraunitary delay projection can lower the degree of a complete multicoordinate constant-covariance polynomial vector while replacing its original coordinates.
Determine EXACTLY when this operation preserves actual monogenic-order integer values, separately from mere circle covariance and coefficient rationality.
Seek an exact finite congruence/counting obstruction and a concrete actual packet control, not a new abstract factorization or a claimed uniform construction.

The bounded local search found [L380's rational delay factorization](../ledger/Yin_L_G0380_v1.md#rational-weighted-delay-factorization), [its actual factor denominators](../ledger/Yin_L_G0380_v1.md#factor-denominator-prime-preservation) and [its exact quotient interpolation distinction](../ledger/Yin_L_G0380_v1.md#finite-word-exact-interpolation-criterion).
That complete weighted two-coordinate mechanism is OLD and is not claimed as a new result here.
[C14v2](Yin_C_G0014_v2.md#statement) supplies the actual power-basis/short-width integrality boundary, and [C20](Yin_C_G0020_v1.md#statement) supplies a precise a3, q3 quadratic optimum suitable for a finite control.
A targeted congruence/projection screen did not locate the proposed universal-order-preservation or primitive-leading-vector gate at this scope.
This is a bounded reuse result, not an exhaustive novelty claim.

Candidate: clear only the FINAL rational weights by actual positive copies, so the vector has equal weight1/M.
For primitive integral leading direction v, put s=v^Tv and Pi=vv^T/s.
The old extreme-lag calculation suggests that U(t)=I-Pi+t^-1Pi lowers degree, but actual new values need a separate test involving(alpha^-1-1)(v^Tu) modulo sO0.
Investigate this exact original-order test, its finite residue-class size, possible universal preservation and all scalar/norm costs.
The actual C20 optimum may show degree reduction with immediate loss of admissibility.
No conclusion is adopted at creation.

Existing L380 includes checked AJL17/AJL16 attribution for elementary paraunitary factors and explicitly distinguishes rational interpolation from complex factorization.
The exact canonical source scope will be read before using that name; the arithmetic conclusions sought here will have local proofs.
No numerical program, solver, factorization scan, new J or source acquisition is planned.
Positive-margin existence is assigned separately to root and is outside this inquiry.
All actual orders, original roots, signed norms, q versus FINAL M, possible zero output coordinates and hypothetical near-one limitations must remain explicit.

<a id="delay-gate-reuse-and-source"></a>
## 1. Old factor mechanism and the new arithmetic question

The author read L380's complete rational weighted factorization, factor-denominator and exact quotient-interpolation sections.
Its actual two-channel H=diag(1,2) factorization and explicit quartic target are not generalized by citation alone.
The elementary rank-one calculation below is written out for an unweighted finite vector; it is the same established degree-reduction mechanism, not a new FIR factorization claim.
The new question is the exact original monogenic-order test on the resulting values, together with its complete finite residue count and universal-preservation boundary.

The existing [AJL17-U001](../audits/literature/AJL17/Yin_U001.md#ajl17-u001) and [AJL16-U001](../audits/literature/AJL16/Yin_U001.md#ajl16-u001) were read in full.
They preserve the selected complex FIR and rational-factor statements, inspected preprint versions, possible factor cancellation and the lack of a rational-field/descent/interpolation theorem.
They supply classical attribution for the elementary delay factors, not an unproved arithmetic premise here.
No original Potapov proof, full paper, later edition or source-wide status is newly audited.
Existing accepted scope suffices; no external source acquisition is needed.

C14's actual short-coordinate power-basis proof and C20's a=3 optimal packet/costs were read directly.
A further targeted local search for integral projections, leading-vector denominators and the P(1) congruence gate found related value/denominator results but not the exact single-factor residue criterion below.
The polynomial-division, finite additive-group count and primitive-vector arguments below are elementary local proofs.
There is no exhaustive novelty or literature-priority claim.
Root supplied only the broad search assignment, not these formulas; this author supplies the deductions and cannot independently review them.

<a id="delay-gate-actual-packet-domain"></a>
## 2. Actual equal-weight coordinates and analytic degree reduction

Let P(t)=t^d+a_(d-1)t^(d-1)+...+a_1t+a_0 be the ACTUAL monic irreducible nontorsion integer-unit minimal polynomial of alpha, d>=2 and a_0 in{+1,-1}.
Reciprocity is NOT needed for this arithmetic inquiry.
Put K=Q(alpha) and actual O0=Z[alpha]; alpha^(-1) belongs to O0.
All integrality below means membership in THIS monogenic order, not in a larger order or at a selected numerical embedding.

Start with a finite rational complementary packet f_b in Q[t,t^-1], nonzero actual values in O0, positive normalized rational weights omega_b and exact constant circle covariance E>0.
Let M be the ACTUAL least denominator of these FINAL weights and m_b=M omega_b positive integers.
Replicate f_b exactly m_b times and use weight1/M for each copy.
This produces a rational M-component vector F, with every indexed value nonzero integral, unchanged actual coefficient denominator q and

    F(t)^* F(t)=M E,                                    (1)

where matrix star means transpose and t->t^(-1).
The copies and M are real input costs, not a free bounded dimension.
Identical copies remain separately labeled; no merging or weight change is performed during the operation below.

Use ONE common monomial to normalize the actual union support to[0,T].
Actual value integrality and nonvanishing survive because alpha is an O0 unit; signed full norms change by the actual sign Norm(alpha)^ell if applicable.
Write

    F(t)=sum_(j=0)^T c_j t^j, c_j in Q^M, c_T!=0.

If T=0 no degree step is performed.
For T>=1 choose the primitive integer vector v in the rational direction of c_T, so c_T=l v for some nonzero rational l and gcd(v_1,...,v_M)=1.
Put

    s=v^T v>=1, Pi=vv^T/s,
    U(t)=I-Pi+t^(-1)Pi,
    G(t)=U(t)F(t).                                     (2)

This is exact rational algebra.
Pi is symmetric and idempotent, U(t)^*U(t)=I, U(t)^(-1)=I-Pi+tPi and det U(t)=t^(-1).
By(1), the extreme lag gives c_0^T c_T=0.
Thus Pi c_0=0 and(I-Pi)c_T=0.
The possible t^(-1) coefficient and degree-T coefficient of G vanish, so

    G in Q[t]^M, deg G<=T-1,
    G^*G=M E.                                         (3)

Equivalently its coefficient at j is(I-Pi)c_j+Pi c_(j+1).
The new ACTUAL least coefficient denominator q' therefore divides q s.
A later common monomial shift changes neither q' nor the union span.
This is an upper denominator divisor only; cancellation may make q' much smaller than q s.

All covariance lags remain zero, but(3) says NOTHING yet about actual values G_i(alpha) being integers or nonzero.
The factor has replaced coordinates, so C49's retained-coordinate scalar lower theorem is not the applicable obstruction.
L380 already separates rational factorization from actual quotient interpolation; the next sections make the arithmetic test explicit for THIS single step.

<a id="primitive-delay-single-vector-integrality"></a>
## 3. Exact single-vector integrality and complete finite residue count

Write u=F(alpha) in O0^M and z=v^T u in O0.
Evaluation gives

    u'=G(alpha)=u+(alpha^(-1)-1)v z/s.                  (4)

**Theorem 1 (exact gate).**
All coordinates of u' belong to O0 if and only if

    (alpha^(-1)-1)z in sO0,
    equivalently (alpha-1)z in sO0.                     (5)

This condition alone does not guarantee that every new coordinate is nonzero.

*Proof.*
Since the starting u_i are integral, membership of each u'_i is equivalent to v_i w in sO0 for all i, where w=(alpha^(-1)-1)z.
Sufficiency of w in sO0 is immediate.
Conversely, primitive v gives integers b_i with sum b_i v_i=1, hence w=sum b_i(v_i w) belongs to sO0.
Multiplication by the unit-alpha changes the first condition into the second.
This proves the exact equivalence for the actual values, without assuming the original coefficients were integers or the projector denominator was coprime to anything.

Put R_s=O0/sO0, a finite ring of cardinal s^d, and let

    A_s=ann_(R_s)(alpha-1).

The gate is precisely z mod s in A_s.
Its cardinal is EXACTLY

    |A_s|=gcd(s,|P(1)|).                               (6)

*Proof.*
Multiplication by alpha-1 is an endomorphism of the finite additive group R_s.
Kernel and cokernel have equal cardinality.
Its cokernel is

    O0/(s,alpha-1)
        =Z[t]/(P(t),s,t-1)
        =Z/(s,P(1)),

whose size is the displayed gcd.
The identification uses the actual monogenic presentation and includes every repeated factor and prime power in s and P modulo s.
No squarefree reduction, residue-field substitute or maximal-order assumption occurs.
P(1)!=0 because the original irreducible nontorsion input is not t-1.

Since v is primitive, the map R_s^M->R_s sending u to v^T u is onto.
Each fiber has size s^(d(M-1)).
Thus the EXACT number and fraction of all residue vectors passing the integrality test are

    gcd(s,|P(1)|) s^(d(M-1)),
    gcd(s,|P(1)|)/s^d, respectively.                    (7)

This is a count on ALL original-order residue vectors.
It is not a probability statement about actual complementary profiles, whose values and leading vectors may be highly correlated.
No random distribution, independence or scarcity of actual solutions is inferred.
The separate nonzero-output condition can remove additional vectors and is not included in this count.

In particular, if gcd(s,P(1))=1, the gate simplifies to

    v^T u in sO0.                                      (8)

For completeness, P(t)-P(1)=(t-1)Q(t) gives(alpha-1)Q(alpha)=-P(1).
A Bezout identity for s and P(1) therefore makes alpha-1 invertible modulo s.
This agrees with the cardinal-one annihilator in(6).
When P(1)=+/-1, the simplification holds for EVERY positive s.
For s=1 the quotient is the one-element ring and every integrality condition is automatic, as it should be.

<a id="universal-order-preserving-projection-boundary"></a>
## 4. Universal order-preserving orthogonal projections are coordinate projections

The single-vector test must not be confused with preservation of the ENTIRE order lattice.
Let Pi be ANY rational symmetric idempotent M-by-M matrix and define U as in(2), without assuming rank one.

**Theorem 2 (universal boundary).**
The following are equivalent:

    U(alpha) O0^M subset O0^M;
    Pi has integer entries;
    Pi is diagonal with every entry0 or1.              (9)

In that case U(alpha) is an automorphism of O0^M, with diagonal entries1 or alpha^(-1).
For the primitive rank-one Pi of Section2, universality occurs exactly when v is a signed coordinate vector, equivalently s=1.

*Proof.*
The first condition is equivalent to all matrix entries delta_(ij)+(alpha^(-1)-1)Pi_(ij) being in O0.
The ACTUAL unit relation gives

    alpha^(-1)=-a_0[alpha^(d-1)+a_(d-1)alpha^(d-2)
                            +...+a_1].                 (10)

Because d>=2, the highest power-basis coefficient of alpha^(-1)-1 is-a_0 in{+1,-1}.
Uniqueness of the ordinary degree<d representation therefore forces every rational Pi_(ij) to be an integer.
This uses O0 exactly and is not extended to an overorder.

For a rational orthogonal projection, 0<=Pi_(ii)<=1; moreover symmetry and idempotence give Pi_(ii)=sum_j Pi_(ij)^2.
If entries are integers, each diagonal is0 or1.
Diagonal0 makes its entire row zero; diagonal1 already contributes its full square1, so all other entries in that row vanish.
Thus the matrix is a coordinate projection.
Conversely a coordinate projection plainly has integer entries and makes U(alpha) a diagonal unit matrix whose inverse uses alpha.
For rank one there is one diagonal1, so its primitive direction is+/-e_i and s=1.
This proves every equivalence.

This theorem restricts a SINGLE factor that is required to preserve ALL original-order vectors.
It does not assert that a mixed factor fails on every particular admissible packet: Theorem1 supplies its exact conditional test.
It also does not classify finite PRODUCTS with intermediate nonintegral values; cancellations and later restoration are possible and must be checked at the actual final quotient.
L380's finite-word criterion and its later exact interpolants are not contradicted.

<a id="delay-reduction-validity-and-full-costs"></a>
## 5. Admissibility, old stopping floor and full transformed costs

For a particular degree step, passing(5) AND having every u'_i!=0 are both necessary to keep the M labeled coordinates as an admissible equal-weight packet.
The identities(1)--(3) keep the energy and all lags exactly, but cannot waive either arithmetic requirement.
A zero value with a nonzero polynomial cannot simply be discarded while claiming the same covariance.
Even deletion of an identically zero coordinate followed by renormalization changes the normalized energy, so it is not the same operation.

If0<E<1, C14's adopted short-coordinate theorem says that any actual admissible packet in O0 has union width at least d: individual width<d and actual order integrality force integer coefficients, each nonzero coordinate then has coefficient energy at least1, and the positive normalized average cannot be E<1.
Consequently a sequence of these analytic degree reductions that keeps EVERY indexed value nonzero integral and all weights fixed cannot reach degree<d.
Starting at T>=d, at least one integrality or nonzero condition must fail by the step numbered T-d+1 at latest, if reductions are attempted that long.
This is an application of the OLD short-width floor, not a new all-window or uniform near-one obstruction.
It permits useful legal degree reduction while the width remains at least d.

At any actually LEGAL transformed packet, keep the ACTUAL q', the unchanged indexed final weights1/M, each positive copy1, and every transformed signed full norm D'_i=Norm_K(u'_i).
After any one common monomial normalization incorporate its actual Norm(alpha)^ell sign into these D'_i.
For integer numerators H_i=q' G_i one has

    Res(P,H_i)=(q')^d D'_i,
    product_i Res(P,H_i)=(q')^(dM)product_i D'_i,
    S_int=(1/M)sum_i||H_i||_2^2=(q')^2 E,
    I'=log q'+Lambda',
    Lambda'=(1/(dM))sum_i log|D'_i|>=0.                 (11)

All contents remain.
The common scalar cancels only after both norm and energy have been charged:

    I'-(1/2)log S_int=Lambda'-(1/2)log E.                (12)

If the output is not integral, the algebraic equality of full norms and resultants still exists but the nonnegative integer-norm floor Lambda'>=0 is unavailable.
The determinant det U(alpha)=alpha^(-1) is a field unit; its norm DOES NOT preserve the PRODUCT of the coordinate norms or ensure coordinatewise integrality.
Individual coordinates are linear combinations, not factors of a multiplicative norm identity.
The explicit control below displays that failure exactly.

The actual q' may divide q s with cancellation, while FINAL M and all copied labels remain separate.
The bounds/counts in this draft supply no uniform successful choice of v, no denominator sufficiency, no controlled product norm and no route from a small modular fraction to a missing real solution.
They only identify arithmetic work that matrix replacement must actually perform.

<a id="actual-quadratic-projection-loss-control"></a>
## 6. An exact admissible q3 packet loses integrality on its first degree step

Use the ACTUAL P=t^2-3t+1, alpha^2=3alpha-1, d=2 and O0=Z[alpha].
C20's a3 minimum has energy1/3.
Choose its allowed two-label attainer and expand the final weights2/3,1/3 into THREE equal copies:

    F(t)=((1+t^2)/3,(1+t^2)/3,(2-t^2)/3)^T,
    u=(alpha,alpha,1-alpha)^T,
    M=3, q=3, T=2, F^*F=1.                             (13)

Each actual u_i is a nonzero integer unit.
The full SIGNED degree2 norms are1,1,-1.
Coefficients satisfy

    c_0=(1,1,2)^T/3, c_2=(1,1,-1)^T/3,
    c_0^T c_2=0, v=(1,1,-1)^T, s=3.

Thus the analytic reduction is exactly

    G(t)=c_0+t c_2
        =((1+t)/3,(1+t)/3,(2-t)/3)^T,
    G^*G=1, T'=1, q'=3.                               (14)

The physical support genuinely shrinks and every lag still cancels.
But z=v^T u=3alpha-1=alpha^2.
Since P(1)=-1, the exact gate is z in3O0, which FAILS: its power-basis constant coefficient is-1.
Directly,

    (alpha^(-1)-1)z=alpha-alpha^2=1-2alpha notin3O0.

All three output values are nonzero but nonintegral:

    u'=((1+alpha)/3,(1+alpha)/3,(2-alpha)/3)^T.

Using Norm(a+b alpha)=a^2+3ab+b^2 gives their full signed norms

    5/9,5/9,-1/9.                                     (15)

This exposes the precise failed hypothesis, not just an unspecified denominator concern.
In the finite residue count, gcd(3,|P(1)|)/3^2=1/9 is the fraction of ALL possible order-residue vectors satisfying this factor's integrality gate; it is not a statistical assertion about admissible C20 packets.

The complete original and transformed numerator arithmetic is

    original numerator resultants: 9,9,-9,
    original signed product: -3^6,
    transformed numerator resultants: 5,5,-1,
    transformed signed product: -25,
    both normalized integer energies S_int=3.          (16)

The actual coefficient denominator stays3 despite the safe cap q s=9.
For the original packet Lambda=0.
For the transformed NONINTEGRAL vector,

    I'=(1/3)log5,
    Lambda'=(1/3)log5-log3<0,
    I'-(1/2)log S_int=(1/3)log5-(1/2)log3.             (17)

Thus neither the full-coordinate norm product nor its nonnegative income survives, even though the field-matrix determinant alpha^(-1) has full norm1.
No transformed vector is presented as an admissible below-one packet of width1.

A second application of the same analytic factor sends G to the constant rational vector(2,2,1)^T/3, still with squared vector norm1 and normalized energy1/3.
These are nonintegral constants, with full coordinate norms4/9,4/9,1/9, numerator resultants4,4,1 and signed product16.
This finite algebra illustrates complete analytic descent without the arithmetic qualification; it provides no legal bypass of C14 or a new Mahler construction.
All computations here are exact hand expansions, with no native numerical program or solver.

<a id="delay-gate-outcome-and-open-interface"></a>
## 7. Outcome and remaining matrix-repair question

The proposed nonscalar mechanism CAN remove coefficient support and evade a retained-coordinate scalar premise at the level of rational circle identities.
That analytic fact is old.
The successful new deduction is the exact single-factor original-order gate(5), the full finite count(6)--(7), and the universal-preservation classification(9), together with a complete actual input where the gate fails immediately.
This locates the missing arithmetic step instead of treating rational paraunitarity or unit determinant as automatic integer realization.

For inputs with P(1)=+/-1, every mixed primitive leading projection with s>1 imposes the explicit condition v^T u=0 modulo sO0.
When primes divide P(1), the exact annihilator can be larger, but(6) retains all prime powers and cannot be replaced by a squarefree factor test.
A useful future multicoordinate construction must select a correlated actual packet/direction meeting the modular condition and all nonzero output guards, or justify a final composite word that restores them with controlled norm/width costs.
This draft proves neither availability nor impossibility of those choices.

No part of the finite residue count establishes generic failure among real complementary packets, and no single-factor universal result is extended to arbitrary products or arbitrary matrices.
The original order is essential; overorders are not covered.
No full-signature price is strengthened, no fixed polynomial is inflated into a near-one family, no new profile upper bound is proved, and unrestricted G0001 remains unresolved.
The author wrote only this responsible D and makes no Claim adoption, strategy update, source-state change or independent-review assertion.

<a id="delay-gate-author-check"></a>
## 8. Complete author check and review boundary

The entire saved Sections1--7 was checked after the communication interruption without reallocating the draft or repeating any mathematical computation.


Author checking covered actual monogenic order and general original unit polynomial, constant coefficient+/-1 and signed monomial norms; actual FINAL M versus coefficient q and positive indexed copies; extreme-lag orthogonality, rational primitive leading direction, both canceled endpoints, degree0 stopping and the q s denominator divisor; the exact Bezout equivalence in(5), separate output nonvanishing, all prime powers and nilpotents in the finite ring, kernel/cokernel count and s1 case; primitive-vector surjectivity and the limitation of the fraction to ALL residue vectors; the P(1) coprime simplification; the unique highest power-basis coefficient in(10), every rational orthogonal-projection implication and the distinction between single-vector, universal single-factor and composite-word preservation.

The old C14 short-width consequence was checked only for fixed positive normalized weights and actual nonzero values; it is not a new uniform width theorem.
Full transformed signed norms, actual q', contents, copied resultants, scalar-energy cancellation and the unavailability of the integer-norm floor after an illegal step were checked.
The quadratic control was verified by exact algebra: original and transformed full covariance, both power-basis value lists, the failed mod3 gate, all signed norms/resultants/products, the negative transformed norm income and the optional second analytic step.
No source theorem was enlarged beyond the existing AJL attribution and local L380/C14/C20 scope.

No unresolved step was found in this bounded author argument.
It supplies exact arithmetic criteria and a concrete failure control, not a successful input-uniform matrix construction or an impossibility theorem for all nonscalar methods.
This is author checking only; the author does not supply independent review or select a proved Claim assessment.
The ENTIRE artifact still requires a separately organized noncontributor review before fixed adoption.
No native mathematical program, numerical solver or new source acquisition was used.

<a id="delay-gate-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T09:33.
Freeze the complete starting question/reuse account and Sections1--8, Theorems1--2, equations(1)--(17), complete exact congruence/counting/universal-preservation proofs, finite analytic degree reduction, all actual costs, quadratic control, source/contribution and failure/noncompletion boundaries.
The saved Section7 was recovered in place; no second allocation or new exploration was started during closeout.
The scoped material check passed before this final author-check/freeze addition and is repeated for the final text.
Its result verifies structure only.
Current mathematical status: complete author candidate, independent whole review pending.
The assigned D8 review is not begun in this closeout turn, following root's latest instruction.

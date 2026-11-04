---
author: Yin
---
# Exact monomial block transitions and power-law legal-word length obstruction

Date: 2026-10-12T14:25.
Human author Yin.
Root authored the original D32 and this fixed extraction.
Separate whole R300 independently checked the COMPLETE22:16 original body; this new wrapper needs its own actual noncontributor review.
Every original argument, candidate, role, source scope and cost is retained below.
No adoption or retirement is performed at registration.

## Statement

**A. Exact algebraic transition classification.**
Let f_i=epsilon_i t^(a_i), epsilon_i in{+1,-1}, a_i arbitrary integers with repetitions; let v in Z^N be nonzero primitive, s=sum v_i^2, Pi=vv^T/s and k ANY NONZERO integer of either sign.
Set U=I-Pi+t^k Pi, V=sum_i v_i epsilon_i t^(a_i), H=(t^k-1)V and g_i=f_i+v_i H/s.
EVERY g_i is a signed monomial as a Laurent polynomial if and only if either V=0 and all g_i=f_i, or there are an exponent a and a common sign delta such that for I={i:v_i!=0}, all a_i=a and v_i=delta epsilon_i on I.
In the latter case s=|I| and exactly those labels shift to epsilon_i t^(a+k); all others stay unchanged.
Thus every changing clean transition moves a subset of ONE exponent class and preserves every sign.
This classification uses no algebraic input or integrality assumption.

**B. Local arithmetic dichotomy.**
Fix the ACTUAL monic irreducible nontorsion integer-unit polynomial P, original degree d>=2, root alpha, K=Q(alpha), O0=Z[alpha], nu=Norm(alpha) in{+1,-1}, and total m=m(P)>0.
All norms use the entire original degree, including circle roots.
For clean signed monomial values with exponent span A and multiplicity R, retain the adopted C74 constant

    K0=(log2/4)/[2*36^8*5^64], eta_R=K0 R^-64.

If every g_i(alpha) is nonzero in O0 and (A+abs(k))*m/d<=eta_R, either V(alpha)=0 and ALL values are unchanged, or A's changing block transition holds for the CLEAN polynomials.
In the latter case s=|I|<=R.
The actual-zero branch can have V nonzero as a polynomial and arbitrary direction height.
In particular s>R cannot change any actual value at this threshold.
The proof uses the EXACT existing C74 small-parameter local theorem and its accepted source limits, followed by A; no new angular theorem is supplied.

**C. Linear multiplicity growth and sharpness.**
In ANY finite sequence of block moves as in A, or invisible steps, start with maximum multiplicity R0.
If n_a^(j) counts labels at exponent a, put E_j=sum_a max(n_a^(j)-R0,0).
Then E_j<=jR0 and R_j=max_a n_a^(j)<=min{N,(j+1)R0}.
Arbitrary splits/merges and signed delays are covered.
A move of r labels increases target excess by at most r and decreases source excess by min(r,max(n_a-R0,0)), so its excess increment is at most R0.

The bound is attained: for any L,R0>=1 put R0 positive labels at each exponent0,...,L.
At step j shift ALL jR0 labels now at j-1 to j using delay1 and their primitive indicator vector.
Then R_j=(j+1)R0, E_j=jR0, N=R0(L+1), actual q1/E1/FINAL M=N and B_word=2L.
This construction is legal for every input in B, with zero income throughout; it is not a near-one or positive-income family.

**D. Sharper finite LEGAL-word theorem.**
Retain TRUE vectors F^(j)=U_j F^(j-1), j1,...,L, L>=1, fixed N, primitive directions, nonzero integer delays of either sign, and a clean signed-monomial seed of span A0 and multiplicity R0.
Assume EVERY coordinate at EVERY stage0,...,L is nonzero in the SAME O0.
All indexed weights stay1/N.
Put

    B_word=A0+sum_j abs(k_j), U_word=B_word*m/d.

If U_word<=eta_(min{N,L R0}), all intermediate ACTUAL values remain signed powers, keep their original coordinate signs, and every step is invisible or the exact block shift in B.
Final full norm income Lambda and E1 surplus are ZERO.
Induction uses the PRE-step bound R_(j-1)<=min{N,jR0}; clean representatives have identical actual evaluation and their own newly established E1 covariance.
True polynomial representatives are not silently substituted inside another covariance identity.

Therefore ANY legal word with positive final income satisfies BOTH

    U_word>K0 N^-64, U_word>K0(L R0)^-64,
    N>(K0/U_word)^(1/64),
    L>(K0/U_word)^(1/64)/R0.

The N price is credited C74 reuse; the POWER-LAW L price is new and needs no bound on delay magnitudes.
For hypothetical actual m_j->0 positive-income words with B_word,j<=C d_j and R0,j<=Rbar, fixed C,Rbar, necessarily L_j>(K0/(C m_j))^(1/64)/Rbar->infinity.
No existence or converse is claimed.
The weak further m>K0/[C^65 Rbar^64 d^64] consequence is degree-dependent and does not improve a general gap theorem.

**E. TRUE full costs and limits.**
After ONE common polynomial normalization, let q_L and T_final be the actual final coefficient denominator and common union width, B_i=q_L F_i^(L) in Z[t], and D_i the complete original signed value norms.
Then q_L divides product_j s_j, T_final<=B_word, FINAL M=N with one copy per label,

    Res(P,B_i)=q_L^d D_i,
    product_i Res(P,B_i)=q_L^(dN) product_i D_i,
    (1/N)sum_i||B_i||_2^2=q_L^2,
    Lambda=(1/(dN))sum_i log abs(D_i),
    I_int=log q_L+Lambda, surplus=Lambda<=T_final*m/d.

A common shift t^b adds nu^b per norm and nu^(bN) to the product.
Under D, BEFORE that shift the signed product is (product_i epsilon_i^d)nu^(sum_i a_i'), with ORIGINAL signs and sum_i a_i'=sum_i a_i^(0)+sum_(changing j)r_j k_j.
This is not the exponent sum_j k_j of the matrix determinant.
Every content, actual q, original norm and copied sign remains.

The theorem still requires cumulative absolute-delay expense and every intermediate nonzero O0 value, fixed dimension/equal weights, rank-one delay factors and a monomial seed.
Final-only integrality, illegal/zero intermediate states, constant rational orthogonal factors, higher-rank factors without a legal decomposition, changing dimension/metric, nonmonomial seeds and short final width with large cumulative expense remain outside.
The unrestricted G0001 gap is unresolved.

## Current assessment
[Selected decision](#decision-sufficient-rational-delay-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:25 |
| status | open |
| reason | Register exact clean block classification, actual local dichotomy, linear multiplicity excess, sharp zero-income control and power-law legal-word length obstruction with all true costs. Entire D32 preserved; independent R300 supports actual original only. Separate actual extraction review required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--E: algebraic/arithmetic domains, all quantifiers, sharpness, power-law prices and complete true costs/limits. |
| argument | [Entire original proof](#argument) | COMPLETE22:16 D32 candidate/reuse/history and Sections1--5/equations1--16, roles/source limits and freeze. |
| dependency | [Adopted C74 local theorem](Yin_C_G0074_v1.md#statement) | Exact original unit domain, eta_R, all-height small-parameter local theorem and true cost interfaces; no new source-proof acceptance. |
| dependency | [C74 local complete proof](Yin_C_G0074_v1.md#repeated-monomial-one-step-price) | Separate clean E1 construction, actual q<=s, integral nonzero residual versus actual kernel, and all original-root quantities. |
| dependency | [C74 true costs](Yin_C_G0074_v1.md#legal-word-complete-true-costs) | TRUE q/M/indexed norm products and common normalization; C10 generic actual final-width expense inherited exactly. |
| support | [Old rational projection](Yin_C_G0053_v1.md#statement) | Reuse attribution of rank-one algebra; new classification proved locally. |
| support | [Old rational word criterion](../ledger/Yin_L_G0380_v1.md#finite-word-exact-interpolation-criterion) | Comparison only: no intermediate-legality or short cumulative expense guarantee. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0300_v1.md#monomial-transition-power-law-whole-independent-finding) | ENTIRE actual22:16 D32 only, not prospective extraction coverage. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T14:31 |
| status | proved |
| reason | Adopt original whole R300 and separate actual extraction R301. Exact monomial block classification and linear excess give the power-law legal-word length obstruction, with full original true costs and the sharp zero-income control. Every intermediate nonzero original-order value and cumulative absolute-delay hypothesis remains essential. Root authored proof/wrapper and is not either independent reviewer. No unrestricted gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--E: algebraic/arithmetic domains, all quantifiers, sharpness, power-law prices and complete true costs/limits. |
| argument | [Entire original proof](#argument) | COMPLETE22:16 D32 candidate/reuse/history and Sections1--5/equations1--16, roles/source limits and freeze. |
| dependency | [Adopted C74 local theorem](Yin_C_G0074_v1.md#statement) | Exact original unit domain, eta_R, all-height small-parameter local theorem and true cost interfaces; no new source-proof acceptance. |
| dependency | [C74 local complete proof](Yin_C_G0074_v1.md#repeated-monomial-one-step-price) | Separate clean E1 construction, actual q<=s, integral nonzero residual versus actual kernel, and all original-root quantities. |
| dependency | [C74 true costs](Yin_C_G0074_v1.md#legal-word-complete-true-costs) | TRUE q/M/indexed norm products and common normalization; C10 generic actual final-width expense inherited exactly. |
| support | [Old rational projection](Yin_C_G0053_v1.md#statement) | Reuse attribution of rank-one algebra; new classification proved locally. |
| support | [Old rational word criterion](../ledger/Yin_L_G0380_v1.md#finite-word-exact-interpolation-criterion) | Comparison only: no intermediate-legality or short cumulative expense guarantee. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0300_v1.md#monomial-transition-power-law-whole-independent-finding) | ENTIRE actual22:16 D32 only, not prospective extraction coverage. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0301_v1.md#c77-monomial-block-actual-extraction-finding) | Complete ACTUAL registered statement, entire preserved original and all exact interfaces independently checked after allocation by a noncontributor; earlier whole review retains its original scope. |


### Decision sufficient-rational-delay-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:12 |
| status | proved |
| reason | Use the complete sufficient accepted home of the same exact prior rational factor/orbit/fixed-vector pole interface. Preserve the original domain and scope, all other tuples/fields, current review, old decisions and actual historical reading inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--E: algebraic/arithmetic domains, all quantifiers, sharpness, power-law prices and complete true costs/limits. |
| argument | [Exact argument](#argument) | COMPLETE22:16 D32 candidate/reuse/history and Sections1--5/equations1--16, roles/source limits and freeze. |
| dependency | [Exact dependency](Yin_C_G0074_v1.md#statement) | Exact original unit domain, eta_R, all-height small-parameter local theorem and true cost interfaces; no new source-proof acceptance. |
| dependency | [Exact dependency](Yin_C_G0074_v1.md#repeated-monomial-one-step-price) | Separate clean E1 construction, actual q<=s, integral nonzero residual versus actual kernel, and all original-root quantities. |
| dependency | [Exact dependency](Yin_C_G0074_v1.md#legal-word-complete-true-costs) | TRUE q/M/indexed norm products and common normalization; C10 generic actual final-width expense inherited exactly. |
| support | [Exact support](Yin_C_G0053_v1.md#statement) | Reuse attribution of rank-one algebra; new classification proved locally. |
| support | [Exact support](Yin_C_G0441_v1.md#finite-word-exact-interpolation-criterion) | Comparison only: no intermediate-legality or short cumulative expense guarantee. |
| support | [Exact support](../audits/reviews/Yin_R_G0300_v1.md#monomial-transition-power-law-whole-independent-finding) | ENTIRE actual22:16 D32 only, not prospective extraction coverage. |
| review | [Exact review](../audits/reviews/Yin_R_G0301_v1.md#c77-monomial-block-actual-extraction-finding) | Complete ACTUAL registered statement, entire preserved original and all exact interfaces separately checked after allocation by a noncontributor; earlier whole review retains its original scope. Finding relationship: self-reviewed. |

## Registration and complete preservation

The [original D32 freeze](#monomial-transition-power-law-author-freeze) is the complete preservation target.
Its ENTIRE body follows.
Duplicate front matter is represented once, first title demoted one level, and line endings/terminal separating whitespace normalized; no original mathematical or historical paragraph is omitted.
Existing relative claim/ledger links remain valid here.
Root authored original and wrapper and cannot independently review them.
R300's reviewer did not author this wrapper and may separately perform an actual extraction review, or another noncontributor may do so.
No draft is retired or Claim adopted by registration.

## Argument

## Exact monomial transitions and a power-law price for legal delay-word length

Date: 2026-10-12T14:16.
Human author Yin.
New root AUTHOR inquiry under the unchanged G0001 continuation.
Root selects and develops the new algebraic classification and multiplicity accounting.
Root authored the antecedent D29/C74; that contribution is disclosed and a noncontributor must independently whole-review any new result.
No native mathematical program or new external source is needed or authorized here.

## Responsible candidate and bounded reuse

The actual adopted [C74](Yin_C_G0074_v1.md#statement) gives a precise local legal transition at u<=eta_R=K0 R^-64.
Its original proof used the coarse multiplicity bound6R per step, hence a logarithmic necessary word-length price.
[C53](Yin_C_G0053_v1.md#statement) supplies the old rank-one projection algebra, while [L380](../ledger/Yin_L_G0380_v1.md#finite-word-exact-interpolation-criterion) concerns rational factorization without legality guarantees.
The new question is the EXACT algebraic structure of a single factor taking a clean signed-monomial vector to another such vector.
A bounded current G Claim/ledger/draft search for monomial-to-monomial, block shifts and rank-one monomial classification found the known C53/C72/C74 scopes but no matching structural theorem.
This is a bounded reuse screen, not a novelty claim or an exhaustive literature review.
No new named external theorem is invoked; the proof is direct coefficient algebra and a discrete excess count.

The proposed mechanism is stronger than replacing6 by2.
A nontrivial pure monomial transition should shift a subset of coordinates sharing ONE exponent, with primitive direction entries equal, up to a common sign, to their original signs.
Other legal small-parameter factors should have zero ACTUAL residual and leave every value unchanged.
Such a block move increases total multiplicity excess above the INITIAL maximum by at most that initial maximum.
This would bound the maximum exponent multiplicity after j steps by(j+1)R0, yielding a power-law, rather than logarithmic, necessary number of legal factors.
Every true/clean distinction, cumulative delay and intermediate-legality assumption from C74 must remain; no general final-integral or short-final-width theorem is proposed.

<a id="monomial-transition-exact-algebra"></a>
## 1. Exact algebraic classification without an arithmetic hypothesis

Let f_i=epsilon_i t^(a_i),1<=i<=N, where epsilon_i in{+1,-1} and a_i are arbitrary integers, repetitions allowed.
Let v in Z^N be nonzero primitive, s=sum v_i^2, Pi=vv^T/s and k a NONZERO integer.
Put

    U=I-Pi+t^k Pi, V=sum_i v_i epsilon_i t^(a_i),
    H=(t^k-1)V, g_i=f_i+v_i H/s.                         (1)

Suppose every g_i is a signed monomial AS A LAURENT POLYNOMIAL.
Then exactly one of the following holds:

    V=0 as a polynomial, and every g_i=f_i;               (2)

or, with I={i:v_i!=0}, there are an integer a and a common delta in{+1,-1} such that

    a_i=a and v_i=delta epsilon_i for every i in I,
    s=|I|, V=delta |I| t^a,
    g_i=epsilon_i t^(a+k) for i in I,
    g_i=f_i for i outside I.                             (3)

Both possibilities conversely give signed-monomial outputs.
In particular a changing transition preserves each coordinate's sign and moves a nonempty subset of ONE exponent class by exactly k.
There is no restriction on the other coordinates' exponents.
The conclusion concerns this one rank-one delay acting on this vector, not a classification of every matrix with monomial determinant.

**Proof.**
Formula(2) is immediate.
Suppose V!=0 and first k>0.
Let b be the largest occupied exponent of V, with coefficient C!=0.
Then H has top exponent b+k with coefficient C, and also at least one lower occupied exponent: its bottom exponent is the bottom exponent of V, with nonzero coefficient of opposite sign.
For any active i with a_i=b+k, g_i retains a nonzero lower H coefficient.
Since it is a single monomial, its coefficient at b+k must cancel, giving

    epsilon_i+v_i C/s=0.

If there were any such i, summing their contributions to V at exponent b+k would yield

    [t^(b+k)]V=sum_(i:a_i=b+k) v_i epsilon_i
               =-(C/s)sum_(i:a_i=b+k) v_i^2 !=0,         (4)

where inactive coordinates contribute zero.
This contradicts maximality of b.
Hence NO active i has a_i=b+k.

For every active i the coefficient v_i C/s at exponent b+k in g_i is now nonzero.
This is therefore g_i's unique exponent, and every other occupied coefficient of H must be canceled by f_i, which has only exponent a_i.
Because H has at least two occupied exponents, H has exactly two, and all active a_i equal its one lower exponent a.
Thus V=C0 t^a, C0=sum_i v_i epsilon_i!=0, and cancellation at a gives

    epsilon_i-v_i C0/s=0 for every active i.             (5)

Consequently all nonzero v_i equal a common scalar s/C0 times epsilon_i.
Their common absolute value is a positive integer; primitivity forces that value1.
Thus v_i=delta epsilon_i, C0=delta |I| and s=|I|.
Substitution proves(3), including the unchanged signs.
For k<0, apply the proved argument after replacing t by t^-1, which negates all exponents and k while preserving primitive v and every sign.
Transforming back gives exactly(3).
This proves the theorem.
No root, field, integrality or small-parameter assumption was used.

The zero-polynomial case(2) means all sums sum_(i:a_i=a) v_i epsilon_i vanish separately.
It can occur with repeated exponents and nontrivial v.
It is distinct from the arithmetic case V(alpha)=0 with V!=0, which is addressed below.
In particular polynomial identity and equality at one algebraic input have not been conflated.

<a id="small-parameter-local-block-dichotomy"></a>
## 2. Actual small-parameter transitions are block moves or invisible

Retain C74's ACTUAL monic irreducible nontorsion integer-unit P, original d>=2, K=Q(alpha), O0=Z[alpha], total m>0 and nu=Norm(alpha).
Every original conjugate, including circle roots, remains.
Use its exact accepted epsilon and numerical

    K0=(log2/4)/[2*36^8*5^64], eta_R=K0 R^-64.           (6)

For a signed-monomial value vector epsilon_i alpha^(a_i), the representation is unique by nontorsion.
Let R be the maximum exponent multiplicity and A the exponent span.
Apply(1), and assume every actual output is NONZERO in O0 and

    u=(A+abs(k))*m/d<=eta_R.                            (7)

Then exactly the following actual alternatives cover every step:

- V(alpha)=0, so ALL values are unchanged; the direction may have arbitrary height and V need not vanish as a polynomial.
- V(alpha)!=0, and(3) holds for the CLEAN polynomials.
  Thus a subset of ONE exponent class moves by k, every coordinate sign is preserved, and s=|I|<=R.

**Proof.**
C74's local theorem gives the claimed coordinate shift at s1.
If s>=5R, its original full-norm obstruction forces V(alpha)=0.
If2<=s<5R, C74 gives that every CLEAN output polynomial is a signed monomial, using the actual denominator q<=s and the separate clean E1 covariance.
Apply Section1.
The nonzero-polynomial transition(3) changes every active actual value because alpha^k!=1; hence it cannot have V(alpha)=0.
The zero-polynomial alternative is already invisible.
Conversely if V(alpha)!=0, only(3) remains.
No new analytic estimate or stronger source acceptance enters this classification.

In particular a primitive direction with s>R cannot change ANY value under(7).
This strengthens the description of the previous6R transition estimate but does not remove the small-parameter or legal-output hypotheses.
A general true polynomial input is handled only through equal-evaluation clean representatives, as in C74.

<a id="block-move-multiplicity-excess"></a>
## 3. Linear multiplicity growth under arbitrary block moves

Consider ANY finite sequence of operations on N labeled integer exponents that leaves all labels unchanged or moves a subset of one occupied exponent a to another exponent b=a+k, k!=0.
Start with maximum multiplicity R0>=1.
Let n_a^(j) be the multiplicity at a after j operations and define finite total excess

    E_j=sum_(a in Z) max(n_a^(j)-R0,0).                 (8)

Initially E_0=0.
An invisible step preserves E.
For a changing step moving r labels from source multiplicity n_a to target multiplicity n_b, 1<=r<=n_a, the target's excess increases by at most r.
The source's excess decreases by exactly min(r,max(n_a-R0,0)).
Therefore

    E_(j+1)-E_j
      <=r-min(r,max(n_a-R0,0))<=R0.                    (9)

For the last inequality, if r is no larger than the old source excess the difference is0; otherwise r-max(n_a-R0,0)<=n_a-max(n_a-R0,0)=min(n_a,R0)<=R0.
The source and target differ because k!=0.
Consequently

    E_j<=j R0,
    R_j=max_a n_a^(j)<=min{N,(j+1)R0}.                 (10)

This counts arbitrary splits, merges, signs and delays.
It needs no bound on the magnitudes or signs of the k's, and does not assume every step merges entire classes.
It is substantially stronger than multiplying a one-step R bound through the word.

The linear growth is sharp as a purely algebraic legal construction.
For any L>=1 and R0>=1, start with R0 labels at EACH exponent0,1,...,L, with all signs positive, N=R0(L+1).
At step j=1,...,L, all labels originally at0,...,j-1 already have exponent j-1.
Choose v to be their indicator vector, primitive with s=jR0, and use delay k_j=1.
Section1 shifts that entire group to exponent j, merging it with the R0 untouched labels there.
Thus R_j=(j+1)R0, attaining(10), and E_j=jR0.
All values are nonzero O0 units for EVERY actual alpha in the domain; every true polynomial is a monomial and q1/E1/MN hold.
The seed span L and cumulative delay L give B_word=2L.
This is a zero-income structural sharpness control, not a near-one input family or a positive construction.

<a id="linear-multiplicity-legal-word-theorem"></a>
## 4. Sharper entire-word theorem and power-law length price

Use the EXACT word domain of C74: fixed N, L>=1 nonzero integer delays k_j of either sign, nonzero primitive directions v^(j), TRUE vectors F^(j)=U_j F^(j-1), a clean signed-monomial seed with initial multiplicity R0/span A0, equal indexed weights1/N, and every coordinate at EVERY stage0,...,L nonzero in the SAME O0.
Put

    B_word=A0+sum_j abs(k_j), U_word=B_word*m/d.          (11)

**Theorem.**
If

    U_word<=eta_(min{N,L R0}),                          (12)

every intermediate actual value remains a signed monomial, each coordinate keeps its original sign, and each changing ACTUAL step is the block move of Section2.
Every other step has zero actual residual.
Final full norm income Lambda and surplus are0.

**Proof.**
Suppose inductively that j-1 preceding steps have this property.
Actual values have unique clean signed-monomial representatives C^(j-1) with the same evaluation as the true vector.
Applying U_j preserves equality of evaluation, so the clean output inherits actual nonzero O0 membership.
It separately has E1 covariance by paraunitarity of its clean input.
The clean span is at most A0+sum_(ell<j)abs(k_ell), because each preceding block step changes each affected exponent by k_ell and invisible steps change none.
Section3 gives its maximum multiplicity

    R_(j-1)<=min{N,j R0}<=min{N,L R0}.

Since eta decreases, its local paid parameter is at most U_word<=eta_(R_(j-1)).
Section2 applies: this step is invisible or an exact block shift and preserves signs.
Section3 then supplies the next multiplicity bound, closing the induction from j1 to L.
Final signed powers have absolute full norm1, so Lambda0.
This uses the separately established clean covariance and actual evaluation equality, not replacement inside an old polynomial identity.
The TRUE coefficient vectors and all their costs remain retained.

Equivalently, ANY such legal word with positive final income satisfies BOTH

    U_word>K0 N^-64, U_word>K0(L R0)^-64,
    N>(K0/U_word)^(1/64),
    L>(K0/U_word)^(1/64)/R0.                            (13)

The N bound is exactly the old C74 necessary coordinate price and is credited as reuse; the power-law L price is the new consequence.
Unlike the old logarithmic bound, it holds for arbitrary nonzero signed integer delays, with no imposed upper bound on their magnitude.
Both sufficient conditions eta_N and eta_(L R0) follow from(12), hence both strict contrapositives in(13) are valid.
No converse is claimed.

On ANY HYPOTHETICAL actual positive-measure sequence m_j->0 admitting such positive-income words with B_word,j<=C d_j and INITIAL R0,j<=Rbar for fixed C,Rbar,

    L_j>(K0/(C m_j))^(1/64)/Rbar ->infinity.             (14)

Thus bounded-multiplicity legal words need at least this explicit power-law number of factors, even with arbitrary coefficient denominators and direction heights.
It does not establish that unbounded words suffice or that an actual m_j->0 family exists.
Since every nonzero integer delay has abs(k_j)>=1, also L<=B_word; combining(13) gives only the weak degree-dependent consequence m>K0/[C^(65) Rbar^64 d^64] when B_word<=Cd.
That consequence is not a degree-uniform gap or a replacement for stronger existing general degree-dependent results.

<a id="block-word-true-arithmetic-and-limits"></a>
## 5. True coefficients, complete signed costs and precise outside scope

Every true stage still has exact sum_i F_i^(j) F_i^(j)*=N.
For the final TRUE common-shift-normalized vector, let q_L be its actual least coefficient denominator, T_final its actual common union width, D_i=Norm_K(F_i^(L)(alpha)) in Z minus{0}, and B_i=q_L F_i^(L) in Z[t].
Retain the existing exact costs

    q_L divides product_j s_j, T_final<=B_word,
    FINAL M=N, each label has ONE copy,
    Res(P,B_i)=q_L^d D_i,
    product_i Res(P,B_i)=q_L^(dN) product_i D_i,
    (1/N)sum_i||B_i||_2^2=q_L^2,
    Lambda=(1/(dN))sum_i log abs(D_i),
    I_int=log q_L+Lambda, surplus=Lambda.                (15)

Every numerator content and signed norm is included.
The accepted direct C10 bound is Lambda<=T_final*m/d, with actual final width, not an identification of that width with B_word.
A common shift t^b contributes nu^b per norm and nu^(bN) to the product.
Under(12), in the original unshifted coordinates each value has the form epsilon_i alpha^(a_i'), with epsilon_i its ORIGINAL sign, and

    product_i D_i=(product_i epsilon_i^d)nu^(sum_i a_i'),
    sum_i a_i'=sum_i a_i^(0)+sum_(changing j) r_j k_j,   (16)

before the separately retained common-shift factor.
Here r_j is the actual moved block size; invisible steps contribute nothing to actual exponents.
A true matrix determinant is t^(sum_j k_j), generally different from the coordinate exponent change sum r_j k_j.
Therefore(16) is not a determinant-based norm-product invariance assertion.
True polynomial representatives can carry P-multiple corrections and large q even while all their values are signed monomials.

The same outside classes as C74 remain: merely final-integral words with illegal or zero intermediate coordinates, constant rational orthogonal factors, higher-rank factors without a legal decomposition, variable dimension or weighted metric, a nonmonomial seed, and bounded final support with an unbounded cumulative absolute-delay budget.
This result strengthens ONLY the structure/counting inside the legal rank-one word class.
It neither excludes every rational paraunitary packet nor resolves the unrestricted Mahler gap.
The algebraic sharpness control demonstrates multiplicity growth, not positive arithmetic income.

<a id="monomial-transition-power-law-author-freeze"></a>
## Entire author freeze and review scope

Freeze the ENTIRE candidate/reuse/history and Sections1--5/equations1--16 at 2026-10-12T14:16.
Root is sole new proof and wrapper-candidate contributor and cannot independently review this material.
C74's local theorem and direct true-cost interfaces are reused at their adopted scope; Section1 and the total-excess argument are new locally proved algebra, with no new source theorem or native computation.
An independent reviewer should reconstruct in particular the top-coefficient contradiction with cancellations inside repeated-exponent groups, both signs of k, primitivity forcing unit direction entries, exact actual-versus-polynomial zero residual, every split/merge in(9), the PRE-step jR0 rather than POST-step(j+1)R0 threshold, both strict contrapositives, the sharp all-input zero-income construction, and every complete true normalization/sign.
No Claim adoption or unrestricted completion occurs here.

---
author: Yin
---
# Sixth-power Frobenius class escape from the complete cyclic modulus

Date: 2026-10-15T13:28.
Human author Yin.
New delegated author continuation by f_unitary_scope, targeting a substantive strengthening of the C146 family while preserving its earlier physical versions and reviews.
Root supplied the mathematical combination candidate: replace L209 in C146v2's own-ratio-field argument by adopted C147, retain the full height-domain alternative, and derive sixth-power class escape and explicit supplied-class gaps.
Root is a PROOF CONTRIBUTOR and cannot independently review this new account.
This author develops/checks the exact substitution, constants, cutoffs and inverse.

## Responsible question and exact reuse

Read the ACTUAL adopted [C146v2](Yin_C_G0146_v2.md#decision-whole-reviewed-2026-10-15), its entire1--19 argument, and especially [the own-ratio-field calculation](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) and [full signed-norm return](Yin_C_G0146_v2.md#ratio-original-signed-norm-return).
Read the complete adopted [C147](Yin_C_G0147_v1.md#decision-whole-reviewed-2026-10-15), including its exact h<=exp(-40) domain, constant B, monotonicity, every original conjugate/degree-drop cost and source limits.
Those inputs are established and will be invoked at their exact scopes rather than recopied as new proofs.
The previous C146v1/v2 and R357/R358 remain unchanged.

C146v2 already proves a thirteenth-power escape and an explicit elementary inverse using L209.
Its domain-splitting, exponential-cutoff and inverse strategy are credited, not newly discovered here.
The changed mathematical input is C147's fifth-power cyclic-norm modulus, which must be inserted in the OWN ratio field with all actual degrees and original norm fees kept.
A bounded exact local search for sixth-power class escape and C147/Frobenius combinations found the existing C146v2 and C147 interfaces but no already retained corresponding all-lifts sixth-power conclusion.
This is not a literature-wide novelty claim.
The responsible content is the new finite substitution and its explicit implications, so a new working D is appropriate before a later substantive C146 revision.

Candidate: write A_p=p(p+1), H=A_p*kappa*m and h_star=exp(-40).
If H<=h_star, the new inequality should be kappa*B*[H log^2(1/H)]^(1/5)>=log p; the separate H>h_star branch must not be discarded.
Seek the corresponding finite minimum bound, explicit cutoffs for EVERY theta<1/6, fixed-finite-prime/every-lift quantifiers, and a supplied kappa<=k gap with fixed-p large-k order k^(-6)(log k)^(-2).
Automatic bounded-class coverage remains OPEN.
No unrelated new theorem, new source premise, native program or J is part of this round.

<a id="statement"></a>
## Statement of the strengthened conditional criterion

Let alpha be a nontorsion algebraic integer unit, K=Q(alpha), P its monic irreducible polynomial, d=[K:Q] its ORIGINAL degree and m=log M(P)>0 its TOTAL logarithmic measure.
In the normal closure L of K, choose ANY rational prime p, ANY prime of O_L above p, and ANY residue-Frobenius lift sigma in its decomposition group.
Let kappa be the ACTUAL conjugacy-class size of sigma in Gal(L/Q).
No normality of K, reciprocity, unramified-prime or good-power-basis condition is added.
Put

    c=log2/4, B=75c^(-1/4)+9, h_star=exp(-40),
    A_p=p(p+1), Q_p=(log p)^5/(B^5 A_p)>0,
    Phi(h)=[h log^2(1/h)]^(1/5), 0<h<=h_star.
                                                               (1)

Then H=A_p kappa m satisfies the complete alternative

    H>h_star OR [0<H<=h_star and kappa B Phi(H)>=log p].
                                                               (2)

For EVERY0<m<1 this implies

    kappa>=min{h_star/(A_p m),
                      [Q_p/(m log^2(1/m))]^(1/6)}.  (3)

Define

    X_p=max{1, (1/5)log[Q_p(A_p/h_star)^6]}.
                                                               (4)

For0<m<=exp(-X_p), the second entry alone is a valid bound.
If0<=theta<1/6, put q=1-6theta>0 and

    X_(p,theta)=max{X_p,
                  (2/q)log[32/(exp(2)q^2 Q_p)]}.
                                                               (5)

Then the finite strict escape is

    kappa>=2^(1/6)m^(-theta)>m^(-theta)
                         if0<m<=exp(-X_(p,theta)).   (6)

For theta<0 the strict conclusion kappa>m^(-theta) already holds whenever0<m<1.
For a fixed finite nonempty prime set S, replace the cutoff in(5) by its maximum over p in S: (6) then holds for EVERY such p, EVERY prime of each actual normal closure above it and EVERY residue-Frobenius lift.
Empty S is vacuous.
None of these statements assumes that a near-one sequence exists.

For a supplied integer upper bound kappa<=k, k>=1, define the explicit constants

    y_(p,k)=min{exp(-40), (log p/(2Bk))^5},
    Z_(p,k)=log(1/y_(p,k))>=40,
    g_6(p,k)=y_(p,k)/[4 A_p k Z_(p,k)^2].            (7)

Every such input/lift satisfies m>g_6(p,k)>0.
At fixed p and large k this bound has order k^(-6)(log k)^(-2), with its exact formula and finite cap retained below.
The prime and class-size conditions are supplied hypotheses; no automatic bounded-class coverage or unrestricted Mahler gap follows.

The inherited auxiliary field, exponent, integral signed norm and relative-degree costs remain those of C146v2 and are explicitly recorded in Section1.
In particular a growing kappa does NOT give a uniform degree-linear original window or a bounded-support one-variable representative.

<a id="argument"></a>
<a id="inherited-own-ratio-field-costs"></a>
## 1. Exact inherited field, norm and exponent interface

Use [C146v2 equations(1)--(4)](Yin_C_G0146_v2.md#ratio-own-field-author-calculation), BEFORE its use of L209.
They give the actual nontorsion algebraic integer unit

    rho=alpha^p/sigma(alpha), E=Q(rho), D=[E:Q],
    2<=D<=d'<=kappa d, r=d'/d<=kappa,
    m_rho=log M(P_rho)<=kappa(p+1)m,
    n=p^ceil(log_p D)<pD,
    u=n m_rho/D <p m_rho<=H=A_p kappa m,
    log abs Norm_(E/Q)(rho^n-1)/D >=(log p)/kappa.
                                                               (8)

Here K' is the SAME intermediate field of degree d'=r d in C146v2, not a new field declared Galois.
The old proof pays colliding restrictions to E by their exact fiber d'/D, retains at least D/kappa distinct rho-conjugates, and uses their OWN degree D for the positive local valuation step.
The binomial power in(8) reaches depth1, including ramified p and p=2.
These are adopted inputs; this continuation neither repeats their full proof nor substitutes the degree of the normal closure.

The original signed-norm return is [C146v2 equations(7)--(8)](Yin_C_G0146_v2.md#ratio-original-signed-norm-return).
With beta=alpha^(pn)-sigma(alpha)^n and eta=Norm_(K'/K)(beta), it gives the EXACT nonzero identities and costs

    eta in O_K,
    Norm_(K/Q)(eta)=epsilon Norm_(E/Q)(rho^n-1)^(d'/D),
    epsilon in {1,-1},
    log abs Norm_(K/Q)(eta)/d'
                       =log abs Norm_(E/Q)(rho^n-1)/D,
    n<p kappa d, pn<p^2 kappa d,
    r pn<p^2 kappa^2 d.                              (9)

The relative product has r<=kappa factors and at most2^r signed conjugate monomials before collection.
Its total conjugate exponent is bounded by r pn.
The equality is normalized by d'=r d, with all repeated E-embeddings retained; it is NOT an assertion that the same expression divided by original d has lost the factor r.
A nonzero integer norm exists in the full ORIGINAL O_K.
Membership in Z[alpha] and a cheap single-variable coefficient representative remain unproved and are not needed for(8)--(9).

These unchanged fees explain the exact original-degree meaning of the new bound.
They are O_(p,kappa)(d) only with p,kappa fixed.
Different lifts can use different rho,E,D,n and eta; their incomes are never added and charged at a fictional common time.

<a id="new-cyclic-modulus-substitution"></a>
## 2. Complete finite substitution and the height-domain split

C147 applies to EVERY nontorsion algebraic integer unit in its ORIGINAL field, at every positive exponent, including powered-degree drops.
Apply it to rho in its OWN field E at the n in(8).
Its actual parameter is u=n m_rho/D>0.
If H<=h_star, then u<H<=h_star, and C147 plus its monotonicity gives

    (log p)/kappa
       <=log abs Norm_(E/Q)(rho^n-1)/D
       <=B Phi(u)<=B Phi(H).                         (10)

This proves the small-height branch of(2).
When H>h_star no C147 value at H is asserted; that separate branch is kept as stated.
The C147 theorem, rather than its asymptotic shorthand or the old L209 function, is the substituted input.
No Salem trace-factor theorem or missing infinite-frequency estimate enters this application.

In the small-H branch, take the fifth power of(10), use H=A_p kappa m, and divide by the positive constants.
The exact result is

    kappa^6 m [log(1/(A_p kappa m))]^2 >=Q_p.        (11)

This algebra is the new sixth-power gain.
For0<m<1, A_p kappa>=6 ensures, in this branch,

    0<log(1/(A_p kappa m))<log(1/m).

Replacing its square by the larger square therefore gives the second lower bound in(3).
In the other branch H>h_star gives kappa>h_star/(A_p m), which implies the first lower bound.
Taking the minimum is valid in either branch.
One cannot drop the first entry merely because m is described informally as small; the next section supplies the explicit comparison needed to do so.

<a id="sixth-power-finite-class-cutoffs"></a>
## 3. Explicit inverse class bounds and every theta below1/6

Let x=log(1/m)>0.
The second entry in(3) is no greater than the first exactly when

    x^2 exp(5x)>=Q_p(A_p/h_star)^6.                 (12)

Raising the comparison to the sixth power verifies this equivalence directly.
If x>=X_p from(4), then x>=1 and exp(5x)>=Q_p(A_p/h_star)^6.
Consequently(12) holds, even when the logarithm defining X_p is negative.
Thus

    kappa >= [Q_p/(m log^2(1/m))]^(1/6)
                                 for0<m<=exp(-X_p). (13)

The elementary cutoff technique is reused from C146v2, now with the CORRECT exponent5 and new h_star,Q_p; it is not a new inversion method.
For0<=theta<1/6 put q=1-6theta.
The positive function x^2 exp(-q x/2) has maximum16/[exp(2)q^2], attained at x=4/q.
Hence, for x>=0,

    x^2 exp(-q x)<=16/[exp(2)q^2] exp(-q x/2).       (14)

If x>=X_(p,theta) in(5), the right side is at most Q_p/2.
Inserting this into the sixth power of(13) gives

    kappa^6>=Q_p exp(x)/x^2>=2 exp(6theta x),

which is exactly(6), including its strict factor2^(1/6).
Negative logarithms in(5) cause no problem because X_p>=1.
Theta0 is included.
If theta<0, the separate elementary fact kappa>=1>m^(-theta) applies to0<m<1.
No conclusion at theta=1/6 is asserted; the logarithmic correction in(13) has not disappeared.

For a fixed FINITE nonempty S and a fixed theta in[0,1/6), set X_(S,theta)=max_(p in S)X_(p,theta).
For every input with0<m<=exp(-X_(S,theta)), (6) applies individually to every p in S and every supplied lift at every prime above p.
These cutoffs depend only on the fixed primes and theta, not the polynomial, original degree, chosen prime ideal or chosen lift.
A hypothetical m_j->0 sequence therefore obeys these inequalities eventually with the SAME cutoff.
This proves the claimed all-lifts quantifier without a prime distribution theorem or a common choice of n.
If S is empty the assertion is vacuous; if p or S varies without bound these fixed-set conclusions do not follow.

<a id="explicit-sixth-power-supplied-class-gap"></a>
## 4. An elementary explicit gap for kappa<=k

Fix p and an integer k>=1.
Set y=y_(p,k), Z=Z_(p,k) from(7), and define

    h_c=y/(4Z^2)<h_star.                             (15)

This cap is essential for all finite p,k.
Since y<=exp(-40), one has Z>=40.
Moreover

    log(1/h_c)=Z+log4+2log Z<2Z.

Here log Z<Z/4 for Z>=40: it holds at40 because exp(10)>2^10>40, and Z/4-log Z increases there.
Also log4<2<Z/2.
Thus the displayed strict inequality is valid on the entire stated range.
It follows that

    h_c log^2(1/h_c)<y,
    B k Phi(h_c)<B k y^(1/5)<=(log p)/2.             (16)

Now suppose an actual input/lift has kappa<=k and m<=g_6(p,k)=h_c/(A_p k).
Then H=A_p kappa m<=h_c<h_star.
The small-height branch(10) and monotonicity would give

    log p<=kappa B Phi(H)
              <=k B Phi(h_c)<(log p)/2,

a contradiction.
Therefore m>g_6(p,k)>0, as asserted.
No H>h_star branch was lost: the assumed small-m threshold forced H<h_star before the contradiction.
This proves the gap for every actual m>0; it does not impose m<1 as an extra hypothesis on this supplied-class conclusion.

For all k satisfying

    k>=exp(8) log p/(2B),

the second term defines y, including equality of the two terms.
Then the EXACT formula is

    g_6(p,k)=(log p/(2B))^5
           /{4 A_p k^6 [5log(2Bk/log p)]^2}.         (17)

Its fixed-p large-k order is k^(-6)(log k)^(-2).
For smaller k use(7), whose cap and positive logarithm remain valid.
The earlier C146v1/v2 lower bounds remain true and may be stronger numerically at finite parameters; their maximum with g_6 is an available lower bound.
The ratio of this new supplied-bound function to C146v2's fixed-p large-k function tends to infinity with order k^7, because both have squared logarithmic denominators with asymptotically constant ratio.
This is an asymptotic comparison of PROVED bounds, not an optimum claim or a proof that bounded classes occur automatically.

<a id="sixth-power-source-and-comparison-boundary"></a>
## 5. Earlier versions, exact sources and remaining coverage

The initial local search and subsequent derivation concern only the existing C146 conditional criterion.
C146v2 already owns the own-ratio-field construction, embedding-fiber payment, first-depth n<pD step, full original signed-norm return and thirteenth-power consequence.
C147 already owns the all-unit cyclic modulus B Phi, its finite real regularization and frequency-weighted proof.
The new result is the exact finite substitution(10)--(11) and its newly paid sixth-power constants, domain comparison, all-lifts cutoffs and explicit inverse.
Neither the old subgroup/ratio proof nor the numerical summation is asserted as a new contribution here.

The new explicit domain h_star=exp(-40) is SMALLER than L209's old h0=(log2/4)exp(-20).
Therefore this successor must keep its own H>h_star branch and cannot claim a pointwise improvement throughout the old interval.
C146v2 and its earlier bound remain valid on their original domain.
The common-domain comparison of C147 shows asymptotic improvement, and(17) supplies the separately checked fixed-p large-k improvement for the supplied-class criterion.
It does not assert the new constants dominate every old finite p,k case.

The direct dependencies are the adopted C146v2 interfaces(8)--(9) and the adopted C147 statement with its monotonicity and exact original-domain conditions.
C146v2 inherits the [The26b-U001 local algebra](../audits/literature/The26b/Yin_U001.md#the26b-u001): residue-Frobenius availability and the own-field ramification/value-group statement, with its original uninspected ancestor proofs.
C147 inherits the [L229 finite angular statement](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence), [C131 numerical weighting](Yin_C_G0131_v1.md#frequency-weighted-angular-bound) and [C137 radial local step](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument).
Their exact Pri11/Dim19 accepted statement/application limits are unchanged.
No new external result, source version, theorem-proof audit or literature-wide novelty assertion is introduced.

The arithmetic exponents in(9) are those of the actual norm expression.
C147's internal analytic Fourier cutoff is separately paid in its proof at the actual u, including J*u<=h0 and all powered-degree multiplicities.
Invoking the adopted theorem does not claim that its internal test frequencies, a matrix realization, or runtime have a uniform original-degree-linear bound.
No independent norm income is assigned to those analytic test frequencies.
All full norm and relative-degree identities remain the original ones in(8)--(9).

The prior C146v1 comparison with stronger classical original-Galois-generator theorems also remains in force.
This strengthening does not newly establish that already-covered Galois domain.
Original nonnormal fields are allowed here because the accepted ratio-field and full-norm arguments already handle them, not because an ambient Galois degree is replaced by d.
A small total-m hypothesis has still not been shown to provide any bounded prime and bounded conjugacy class.
Torsion inputs are outside the ratio's nontorsion domain, and no near-one nontorsion family is produced.
The positive supplied-class gap and necessary all-lifts escape remain conditional information for the unrestricted task.

## Contributions

Root proposed the new C147 substitution, its sixth-power candidate, required large-H alternative and expected explicit consequences, and is a new proof contributor.
This f_unitary_scope author checked the actual accepted interfaces and supplied the finite domain comparison, constants X_p and X_(p,theta), the capped elementary inverse g_6, its exact large-k formula and complete parameter/quantifier/source accounting.
The cutoff strategy itself is credited to C146v2.
Root's older ratio-field contribution, g_bridge_audit's accepted v2 inverse/norm-return contribution, and root/f contributions to adopted C147 remain distinct from this new combination.
Neither root nor this author can independently whole-review the new strengthened account.

Only this new responsible D was authored.
Its address is reused without any authority from an earlier D at the same number.
No existing C/R/L/U version was edited, and no mathematical program, J or new source acquisition was created.
The intended next retention is a substantive C146 family version with v1/v2 and their reviews preserved, followed by actual whole noncontributor review before adoption.
No next independent theorem is begun in this round.

<a id="sixth-power-entire-author-freeze"></a>
## 6. Entire author check and freeze

2026-10-15T13:36.
Freeze the ENTIRE present account: question, actual reuse and candidate history, full Statement, Sections1--5, all17 formulas, exact inherited norm/exponent costs, source/comparison limits and contribution history.
Root and this author are contributors; this is author checking, not an independent review or an adopting decision.

The author reread the actual complete saved body and rechecked C146v2's consumed own-field outputs BEFORE its old Omega step, the signed norm tower and the denominator d'=r d, all actual exponent/factor counts, and C147's precise original-unit, positive-height, powered-degree and monotonicity domain.
The new proof check reconstructed the strict u<H interface, small-H versus large-H alternatives, fifth-power rearrangement, logarithm direction, sixth-power minimum comparison, negative-log cases in X_p and X_(p,theta), the maximum at4/q, the factor2^(1/6), theta0 and negative theta, and every fixed-finite-prime/all-prime-ideal/all-lift quantifier.

The inverse check separately verified both y branches, Z>=40, log(4Z^2)<Z, h_c<h_star, the explicit forcing of the small-H branch under m<=g_6, the strict contradiction and large-k threshold/formula.
It also checked the k^7 asymptotic comparison with the older k^(-13) bound without claiming pointwise domination.
The theorem does not cover theta=1/6, varying unbounded prime sets, k=0, torsion, or a degree-one nontorsion integer unit; the last domain is empty.
Formula(3) is explicitly for0<m<1, whereas the supplied-class gap applies to all actual m>0.
No numerical program, new source-proof audit or further downstream theorem was used.

The one-file material check returned checked1 before this freeze and is rerun afterwards; it tests structure and links only.
This full original is ready for fixed family retention and actual separately organized whole review, with all prior versions and reviews preserved.
Automatic arithmetic coverage and G0001 remain unresolved.

## Fixed organization

Retain the complete frozen successor account and all seventeen formulas.
The earlier C146 physical v1/v2 and their actual R357/R358 findings remain fixed with their full arguments, source limits, unsuccessful methods and exact finite domains.
This version changes the quantitative cyclic-norm input to adopted C147 and proves every resulting finite substitution, branch, constant and inverse.
Root and f_unitary_scope are contributors to this successor; a separate whole noncontributor review is required.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-15)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:39 |
| status | open |
| reason | Retain the entire sixth-power strengthening of the supplied Frobenius-class criterion, with its own smaller height domain and all original norm costs. Independent whole review is pending; automatic small-class coverage and unrestricted G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire sixth-power criterion](#statement) | Complete alternative, minimum bound, explicit fixed-prime and fixed-finite-set all-lifts cutoffs, capped supplied-class gap and full original costs. |
| argument | [Entire successor proof](#argument) | All six sections and seventeen formulas, exact inherited interfaces, new domain split and fifth-power substitution, all finite constants and source/contribution limits. |
| dependency | [Adopted own-field norm construction](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Equations(1)--(4) before the old Omega use: actual nontorsion ratio, own degree, height, selected mass, local amplification and full norm income. |
| dependency | [Original signed norm return](Yin_C_G0146_v2.md#ratio-original-signed-norm-return) | Equations(7)--(8), exact signed norm, all degree repetitions and actual conjugate-factor/exponent fees; no cheap original polynomial representative. |
| dependency | [Adopted universal cyclic modulus](Yin_C_G0147_v1.md#statement) | Exact B Phi(h) for all original integer units and powered degrees on0<h<=exp(-40), with proved monotonicity and inherited finite/source costs. |
| support | [Earlier explicit inverse comparison](Yin_C_G0146_v2.md#ratio-explicit-bounded-class-gap) | Old capped supplied-class bound and its fixed-prime large-k order, preserved for exact finite and asymptotic comparison. |

### Decision whole-reviewed-2026-10-15

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:47 |
| status | proved |
| reason | Adopt the actual whole noncontributor finding for the sixth-power Frobenius criterion, including exact own-field substitution, both height branches, all explicit cutoffs and the capped supplied-class inverse. Automatic bounded-prime/class coverage and unrestricted G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire sixth-power criterion](#statement) | Complete alternative, minimum bound, explicit fixed-prime and fixed-finite-set all-lifts cutoffs, capped supplied-class gap and full original costs. |
| argument | [Entire successor proof](#argument) | All six sections and seventeen formulas, exact inherited interfaces, new domain split and fifth-power substitution, all finite constants and source/contribution limits. |
| dependency | [Adopted own-field norm construction](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Equations(1)--(4) before the old Omega use: actual nontorsion ratio, own degree, height, selected mass, local amplification and full norm income. |
| dependency | [Original signed norm return](Yin_C_G0146_v2.md#ratio-original-signed-norm-return) | Equations(7)--(8), exact signed norm, all degree repetitions and actual conjugate-factor/exponent fees; no cheap original polynomial representative. |
| dependency | [Adopted universal cyclic modulus](Yin_C_G0147_v1.md#statement) | Exact B Phi(h) for all original integer units and powered degrees on0<h<=exp(-40), with proved monotonicity and inherited finite/source costs. |
| support | [Earlier explicit inverse comparison](Yin_C_G0146_v2.md#ratio-explicit-bounded-class-gap) | Old capped supplied-class bound and its fixed-prime large-k order, preserved for exact finite and asymptotic comparison. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0360_v1.md#sixth-power-frobenius-whole-independent-finding) | Entire actual successor statement and six-section seventeen-formula proof, every selected input and support, exact original costs and antecedent/source/contribution limits. Finding relationship: self-reviewed. |


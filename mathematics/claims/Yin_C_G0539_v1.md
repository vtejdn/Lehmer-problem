---
author: Yin
---

# Actual sparse trace factors: total costs, factor degrees and both prime branches

The complete original mathematical argument is retained from [L416](../ledger/Yin_L_G0416_v1.md#sparse-trace-reuse).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The [original review](../audits/reviews/Yin_R_G0425_v1.md#sparse-trace-whole-independent-finding) keeps its actual original L/J/source bindings, date, relationship declaration and checked scope; it is not retrospectively bound to this C.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Fix integers a>=6,n>=2 and

    F_n(t)=t^(2n)-t^(n+1)-a t^n-t^(n-1)+1
          =t^n[C_n(t+t^-1)-(t+t^-1)-a],
    C_0=2,C_1=y,C_(j+1)=yC_j-C_(j-1).

Every actual monic irreducible integer factor P is a nontorsion integer-unit polynomial of original degree D>=2, with no circle root.
P need not be reciprocal and F_n need not be irreducible.
With c_a=log2/[4log(a+3)],

    1<M(P)<=a+4,
    abs(log abs(z))<=log(a+3)/(n-1) for every root z of F_n,
    c_a(n-1)<=D<=2n.

The number of factors with multiplicity is at most4/c_a.
If n-1>=log(a+3)/log2, every actual factor additionally satisfies

    m(P)>=D log2/(2n)>=(log2)^2/[16log(a+3)]>0.

These are total-measure statements with the accepted Dim19 house input at its exact recorded statement scope; they do not produce near-one inputs.

Let p be prime, r>=1,q=p^r,n=q, and put A_k(P)=abs Norm_(Q(alpha)/Q)(alpha^k-1) over all original D conjugates.
If p divides a, F_q mod p=(t^(q-1)-1)(t^(q+1)-1).
For h_-=deg gcd(Pbar,t^(q-1)-1) and h_+=deg gcd(Pbar,t^(q+1)-1), h_-+h_+>=D, including repeated common roots and p=2.
Consequently one of k=q-1,q+1 has

    v_p(A_k(P))>=D/2,
    k<=[12log(a+3)/log2]D.

If p does not divide a, the trace reduction is y^q-y-abar.
Each trace-root degree f satisfies f/gcd(f,r)=p.
Writing r=p^v s,p not dividing s, all possible f are p^(v+1)e with e|s.
On the explicit schedule r=p^v,v>=0, every trace root has degree pr, each reduced root of F_q has degree pr or2pr, and the entire reduction is squarefree.
Its reduced root orders are at least pr+1.
Every actual factor therefore has p not dividing A_k(P) for every1<=k<=pr, at every local depth.

For fixed a,p this is only a logarithmic zero-income prefix in D comparable to p^r.
No multiplicative return-count estimate at original-degree-linear time, simultaneous treatment of a finite prime set, selected-factor reciprocity, degree preservation under powers, all-prime norm bound or unrestricted gap is claimed.
C130's stronger prior specified-prime bounded-measure comparison is retained at its distinct nonreciprocal scope.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every a>=6,n>=2 and every actual irreducible factor, total measure versus house, original factor degree and lower-range floor, p divides a proportional income including repeated reduction, p not dividing a exact Frobenius schedule and logarithmic all-depth zero prefix; no near-one/reciprocal-factor or simultaneous-prime conclusion. |
| argument | [Entire complete argument](#argument) | Every a>=6,n>=2 and every actual irreducible factor, total measure versus house, original factor degree and lower-range floor, p divides a proportional income including repeated reduction, p not dividing a exact Frobenius schedule and logarithmic all-depth zero prefix; no near-one/reciprocal-factor or simultaneous-prime conclusion. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exactly #smy08-height-normalization: Complete Mahler multiplicativity, circle coefficient upper bound and original multiplicities. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exactly #smy08-house: Accepted Dim19 2019v1 noncyclotomic monic irreducible D>1 house statement only, applied to each actual factor. |
| dependency | [Exact fixed input](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted finite-field Frobenius and extension-degree statements; the new orbit calculation is local. |
| dependency | [Exact fixed input](Yin_C_G0513_v1.md#nonreduced-layer-capacity-proof) | Original companion nullity/deg-gcd floor for every prime, including repeated reduction and index primes; no maximal-order substitution. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:36 |
| status | proved |
| reason | Under the current human maintenance authorization, adopt the exact complete current statement and original fixed argument after the actually completed R737 constructor SELF whole inspection. Preserve original author/source/native evidence, old R bindings and relationships, and all initial open registrations or precision successors. No new research or producer is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every a>=6,n>=2 and every actual irreducible factor, total measure versus house, original factor degree and lower-range floor, p divides a proportional income including repeated reduction, p not dividing a exact Frobenius schedule and logarithmic all-depth zero prefix; no near-one/reciprocal-factor or simultaneous-prime conclusion. |
| argument | [Entire complete argument](#argument) | Every a>=6,n>=2 and every actual irreducible factor, total measure versus house, original factor degree and lower-range floor, p divides a proportional income including repeated reduction, p not dividing a exact Frobenius schedule and logarithmic all-depth zero prefix; no near-one/reciprocal-factor or simultaneous-prime conclusion. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exactly #smy08-height-normalization: Complete Mahler multiplicativity, circle coefficient upper bound and original multiplicities. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exactly #smy08-house: Accepted Dim19 2019v1 noncyclotomic monic irreducible D>1 house statement only, applied to each actual factor. |
| dependency | [Exact fixed input](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted finite-field Frobenius and extension-degree statements; the new orbit calculation is local. |
| dependency | [Exact fixed input](Yin_C_G0513_v1.md#nonreduced-layer-capacity-proof) | Original companion nullity/deg-gcd floor for every prime, including repeated reduction and index primes; no maximal-order substitution. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0737_v1.md#current-g417-complete-self-finding) | Entire exact current Statement and complete Argument with every listed actual input, original field/core/law/time/cost boundary and no new mathematical producer; constructor SELF, not independent. |

## Complete original argument

<a id="argument"></a>

### Original account: Sparse reciprocal trace families and the price of a missing-prime window

Date: 2026-10-18T16:41.
Human author Yin.
Contributing author agents are root and loglog_cyclic_review.
Root proposed the sparse reciprocal family and its Frobenius trace reduction; loglog_cyclic_review developed the actual-factor degree and norm boundaries below.
No numerical experiment, factorization scan or new source theorem is used.

<a id="sparse-trace-reuse"></a>
## 1. Responsible question and exact reuse boundary

Can L413's absence of income from prescribed finite primes be achieved on an actual bounded-TOTAL-Mahler family?
The comparison is [L413](Yin_C_G0536_v1.md#fixed-prime-invisibility-statement), whose simultaneous finite-prime construction has m(P)=log d+O(1).
The existing [C130v2](Yin_C_G0130_v2.md#statement), adopted at its [whole reviewed decision](Yin_C_G0130_v2.md#decision-whole-reviewed-2026-10-15), ALREADY gives a bounded-total-measure actual nonreciprocal minimal-factor family with poor short returns at one specified prime.
Its binary specialization bounds ALL local depths by O(sqrt n), and its first-layer bound holds at every fixed enlargement of the original linear time.
More precisely, C130 selects the actual minimal polynomial of the positive root of t^q-t-1, q=ell^r>=3, with theta0<=M<=sqrt3 and kappa(q-1)<d<=q.
Its chosen-good-prime first-layer peak is at most sqrt(ell X) through time X, and its complete-group triple mass at X<=C d is at most ell^(3/2) C^(5/2)d^(5/2).
For ell=2 and q>=4 its complete original local valuation is at most (3/2)sqrt(2k) at every time k.
These are specified-prime obstructions on a uniformly positive, nonreciprocal measure family; they do not control other primes, simultaneous finite-prime silence, near-one reciprocal inputs or the full integer norm.
Those conclusions must not be presented as new here.
C130's translation-Frobenius proof does not automatically transfer through the two-valued map t->t+t^(-1).

Sparse reciprocal pentanomials and their graph/shortness costs already appear in [L33](../ledger/Yin_L_G0033_v1.md#excess-two-equivalence) and [L45](../ledger/Yin_L_G0045_v1.md).
The present inquiry uses a fixed central coefficient a>=6, excludes circle roots, and keeps EVERY actual irreducible factor's original degree.
It does not claim a new sparse family, new irreducibility theorem or an extension of C130's return-count estimate.
The useful partial result is an exact distinction between p|a and p not dividing a, together with the cost of extracting actual factors.

<a id="sparse-trace-factor-profile"></a>
## 2. Every actual factor has bounded total measure and degree comparable to n

Fix an integer a>=6 and an integer n>=2, and set

    F_n(t)=t^(2n)-t^(n+1)-a t^n-t^(n-1)+1,
    y=t+t^(-1),
    F_n(t)=t^n[C_n(y)-y-a].                              (1)

Here C_0=2, C_1=y, C_(j+1)=y C_j-C_(j-1).
The identity C_n(t+t^(-1))=t^n+t^(-n) is the elementary trace identity retained in [L66](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain).
No field-degree assertion from L66 is imposed before selecting an irreducible reciprocal factor.

For |t|=1, y and C_n(y) are real in [-2,2], so

    C_n(y)-y-a<=4-a<0.                                  (2)

Thus F_n has no circle root and no cyclotomic factor.
It is monic integral, reciprocal, degree 2n and constant coefficient1.
Every actual monic irreducible integer factor P has constant coefficient +/-1 and is nontorsion, of original degree D>=2.
Such a factor need NOT itself be reciprocal; reciprocal factors may instead occur in distinct paired factors.
No claim that F_n is irreducible, or that D=2n, is made.

The coefficient l1 norm of F_n is a+4.
The [Smy08-U001 Mahler circle identity](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) and the pointwise coefficient bound give M(F_n)<=a+4.
Every monic integral factor has Mahler measure at least1, so multiplicativity gives

    1<M(P)<=a+4.                                        (3)

This is TOTAL multiplicative measure, not absolute height or house.
For a root z with R=|z|>=1, the exact root equation gives

    R^n<=R+R^(-1)+a+R^(-n)<=R+a+2,
    R^(n-1)<=1+(a+2)/R<=a+3.

Reciprocity of the whole F_n gives the same upper bound for the reciprocal of any inside root.
Consequently EVERY root of F_n satisfies

    |log|z||<=log(a+3)/(n-1).                            (4)

Use the already accepted Dim19 statement precisely as recorded in [L80](../ledger/Yin_L_G0080_v1.md#degree-only-primitive-escape) and [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-house): the house of a noncyclotomic monic irreducible polynomial of degree D>1 is at least 2^(1/(4D)).
Its original proof is not newly audited.
Apply this to EACH P and combine with (4), obtaining

    c_a(n-1)<=D<=2n,
    c_a=log2/[4 log(a+3)]>0.                             (5)

Thus arbitrary actual-factor selection preserves the original n scale up to constants depending only on a.
The number of irreducible factors, counted with multiplicity, is at most 2n/[c_a(n-1)] and hence at most 4/c_a.
This uses the house theorem for factor degrees, not as an upper bound for total measures.

There is an explicit positive total-measure floor in this restricted family.
Suppose

    n>=2 and n-1>=log(a+3)/log2.                         (6)

For a root replace it by its reciprocal if necessary and write R>=1.
Then (4) gives R<=2, and the root equation implies

    R^n+R^(-n)>=|z^n+z^(-n)|
                 =|a+z+z^(-1)|>=a-R-R^(-1)>=a-3>=3.

Since R^(-n)<=1, this yields R^n>=2.
Therefore EVERY root obeys |log|z||>=log2/n.
The roots of any unit factor P have sum of logarithmic moduli zero, whether or not P is reciprocal.
It follows that

    m(P)=log M(P)=one_half sum_(P(z)=0)|log|z||
         >=D log2/(2n)
         >=(log2)^2/[16 log(a+3)]>0.                    (7)

All roots are counted with their original multiplicities.
Thus these actual bounded-measure factors stay uniformly away from measure1 for large n.
They are controls for a proposed bounded-measure inference, not near-one inputs.

<a id="sparse-trace-dividing-prime"></a>
## 3. If p divides a, one original linear time has proportional income

Let p be prime, r>=1 and q=p^r, and put n=q.
When p|a, direct multiplication in F_p[t] gives

    F_q mod p=(t^(q-1)-1)(t^(q+1)-1).                  (8)

Both binomials are separable, since p divides neither q-1 nor q+1.
Their common roots are among +/-1, and at a common root the full product has multiplicity exactly2.
For any actual factor P of F_q, let Pbar be its monic reduction and put

    h_-=deg gcd(Pbar,t^(q-1)-1),
    h_+=deg gcd(Pbar,t^(q+1)-1).

At a root belonging to only one binomial the multiplicity in Pbar is at most1.
At a common root it is at most2, while positive multiplicity contributes1 to each of h_- and h_+.
Counting these possibly repeated reductions proves

    h_-+h_+>=D.                                        (9)

This includes p=2, when the common root is1.
For the complete original field norm

    N_k(P)=Norm_(Q(alpha)/Q)(alpha^k-1),
    A_k(P)=|N_k(P)|,

where alpha is any root of P, the [L408 original companion/Smith interface](Yin_C_G0513_v1.md#nonreduced-layer-capacity-proof) gives

    v_p(A_k(P))>=deg gcd(Pbar,t^k-1).                   (10)

The norm is nonzero because P is nontorsion.
This is the original companion lattice and original degree, without replacing it by a maximal order or trace-field subnorm.
By (9)--(10), one of k=q-1 and k=q+1 satisfies

    v_p(A_k(P))>=D/2,
    k<=q+1<=[12 log(a+3)/log2]D.                        (11)

The time bound uses (5) and (q+1)/(q-1)<=3.
EVERY actual factor therefore has proportional p-income at an original-degree-linear time whenever p|a.
Bad reduction and overlapping +/-1 roots do not evade this conclusion.
This branch fails as a missing-income control at that prime.

<a id="sparse-trace-artin-schreier"></a>
## 4. If p does not divide a, the proved zero window is logarithmic

Keep q=p^r and assume p does not divide a.
In F_p[t,t^(-1)], the Frobenius identity gives

    F_q(t)=t^q T(t+t^(-1)),
    T(y)=y^q-y-abar.                                   (12)

This is the trace version of the Artin--Schreier translation mechanism in C130; its multiplicative return estimate is not reused on t.
The polynomial T has derivative -1 and q distinct roots.
Every such y satisfies

    y^(q^j)=y+j abar,
    y^(q^p)=y,

and its orbit under the r-th power of the p-Frobenius has EXACT length p because abar is nonzero.
If f=[F_p(y):F_p], the p-Frobenius has a cycle of length f on y, so its r-th power has length f/gcd(f,r).
Therefore

    f/gcd(f,r)=p.                                      (13)

Writing r=p^v s with p not dividing s, the integer solutions of (13) are

    f=p^(v+1)e, e|s.                                   (14)

Indeed write f=p^w e with p not dividing e.
The quotient forces w-min(w,v)=1 and e/gcd(e,s)=1, hence w=v+1 and e|s; conversely these give (13).
Choose the explicit infinite schedule

    r=p^v, v>=0, q=p^(p^v).

Then EVERY trace root has exact degree

    f=pr=p^(v+1).                                      (15)

Each root lambda of the full F_q lies over y through lambda^2-y lambda+1=0.
Since y belongs to F_p(lambda), its residue degree is f or 2f.
No irreducibility of that reciprocal quadratic is assumed.
Thus all residue degrees are O_p(log q), although (5) makes each original characteristic-zero factor degree comparable to q.

The full polynomial F_q mod p is squarefree.
At a nonzero root its derivative, computed from (12), can vanish only if 1-lambda^(-2)=0, since T'=-1.
Such a lambda is +/-1, so y=lambda+lambda^(-1) belongs to F_p and T(y)=-abar is nonzero, a contradiction.
The constant term1 excludes lambda=0.
Every actual monic factor P therefore has squarefree reduction at p; this is good reduction for P itself.

Let o be the multiplicative order of a reduced root lambda.
It exceeds1 because lambda=1 is not a root.
Its minimal polynomial divides (t^o-1)/(t-1), so its residue degree is at most o-1.
Equation (15) gives o>=pr+1.
Consequently EVERY actual factor P satisfies

    p does not divide A_k(P), 1<=k<=pr.                 (16)

The resultant criterion proves (16) at ALL local depths: Pbar and t^k-1 have no common root, so their integer resultant is a p-adic unit.
No deeper Smith layer contributes to a unit determinant.

By (5), D is comparable to p^r, whereas pr is comparable to log D for fixed p.
Thus (16) is only a logarithmic zero-income prefix.
A large residue-field degree does not itself prove multiplicative order of size D.
All roots lie in F_(p^(2pr)), so their orders divide p^(2pr)-1; this upper bound supplies no required lower bound.
No return-count estimate, triple-density estimate, bound on exceptional depths after the first return, or other-prime control is proved here.

<a id="sparse-trace-conclusion"></a>
## 5. Feasibility finding and exact next missing input

This sparse family gives actual bounded-total-measure nontorsion integer-unit factors with growing original degree, and selecting factors costs only a fixed proportion of that degree.
The whole polynomial is reciprocal, but reciprocity of the selected irreducible factor remains unproved.
The factors are uniformly separated from measure1 by (7).
At p|a, (11) gives proportional local income at a linear original time, the opposite of the desired behavior.
At p not dividing a, (16) gives complete local silence on a logarithmic window along an explicit schedule, not L413's degree-linear or exponentially long silence.
C130 already provides a stronger specified-prime obstruction on another bounded-measure family, including all binary depths, so (16) alone adds no general-domain coverage obstruction.

The changed unresolved question specific to this reciprocal trace construction is a multiplicative return estimate for

    {lambda: lambda^q+lambda^(-q)
               =lambda+lambda^(-1)+abar}

at times k of order the ACTUAL factor degree D, together with a way to select an actual reciprocal factor if that hypothesis is required.
C130's elementary translation count on y cannot be transferred through the trace map without paying its multiplicative fibers and quadratic extension.
Choosing a different power q for each prime does not produce simultaneous treatment of a supplied finite prime set.

## Author-check and dependency scope

Sections2--4 contain the complete original author argument.
Standard finite-field Frobenius and degree facts use the accepted [Hun74-U006 interface](../audits/literature/Hun74/Yin_U006.md#hun74-u006); no original-source proof audit is newly claimed.
C130, L413, L33 and L45 are comparisons.
L66 supplies trace notation, Smy08-U001 supplies Mahler normalization and the retained Dim19 statement, and L408 supplies the original companion Smith floor.
No C147 bound, all-prime norm estimate, whole-polynomial irreducibility, primitive degree preservation, near-one existence or uniform original Mahler gap is inferred.

<a id="sparse-trace-fixed-inputs"></a>
## Complete fixed input scopes


| Input | Actual role and limit |
| --- | --- |
| [C130v2 statement](Yin_C_G0130_v2.md#statement) and [adopted decision](Yin_C_G0130_v2.md#decision-whole-reviewed-2026-10-15) | Prior stronger specified-prime comparison on an actual bounded-measure nonreciprocal family, including complete ordered triple mass; no transfer through the reciprocal trace map. |
| [C130v2 exact binary depths](Yin_C_G0130_v2.md#binary-translation-exact-depths) | Prior full original valuation bound at2 only; neither other primes nor the full integer norm is controlled. |
| [Smy08-U001 normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) | Mahler circle identity, multiplicativity and original-root conventions; total measure is distinct from height and house. |
| [Smy08-U001 house interface](../audits/literature/Smy08/Yin_U001.md#smy08-house) and [L80](../ledger/Yin_L_G0080_v1.md#degree-only-primitive-escape) | Accepted Dim19 2019v1 theorem statement, house at least2^(1/(4D)); applied only to each actual factor's degree, with no new original-proof audit or later-edition comparison. |
| [L66 trace identity](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | The elementary C_n recurrence and Laurent identity only; no quadratic field-degree assertion for a possibly nonreciprocal factor. |
| [L408 companion/Smith floor](Yin_C_G0513_v1.md#nonreduced-layer-capacity-proof), independently reviewed in [R413](../audits/reviews/Yin_R_G0413_v1.md#nonreduced-layer-whole-independent-finding) | Full original norm and deggcd lower bound at every prime, including repeated reduction and index primes; no maximal-order replacement. |
| [Hun74-U006](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Accepted finite-field existence, Frobenius and degree statements; the new orbit-length application is proved here, without a new source-proof audit. |
| [L413 finite-prime comparison](Yin_C_G0536_v1.md#fixed-prime-invisibility-statement) | Simultaneous prescribed-prime invisibility with total logarithmic measure log d+O_S(1); not a bounded-measure or near-one premise. |
| [L33 sparse/shortness antecedent](../ledger/Yin_L_G0033_v1.md#excess-two-equivalence) and [L45 pentanomial antecedent](../ledger/Yin_L_G0045_v1.md#complete-length-five-cyclotomic-table) | Comparison only; no graph, cyclotomic-factor classification or irreducibility conclusion is imported into this fixed-a family. |

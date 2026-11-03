---
author: Yin
---

# Complete arbitrary-support single-Salem companion equality and strictness

The complete original mathematical argument is retained from [L428](../ledger/Yin_L_G0428_v1.md#general-single-pair-equality-reuse).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The [original review](../audits/reviews/Yin_R_G0441_v1.md#general-companion-equality-whole-independent-finding) keeps its actual original L/J/source bindings, date, relationship declaration and checked scope; it is not retrospectively bound to this C.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Let V=I+N be an integral upper-unitriangular matrix of rank R, B=|N| entrywise, and V_abs=I-B.
Write

    p_V(t)=det(tV+V^T),
    p_abs(t)=det(tV_abs+V_abs^T),
    p_cover=p_V p_abs.

Assume the ENTIRE original polynomial is p_V=P Q, where P is the monic minimal polynomial of a genuine Salem number alpha>1 occurring ONCE, and Q is any monic integer polynomial with every root on the unit circle.
All multiplicities and every neutral factor of Q are retained, and R=deg P+deg Q is the actual matrix rank.
There is no bound on rank, entry height, neutral degree or support cycles.
In particular m(p_V)=log alpha=m(P).

Decompose the undirected support graph of B into connected components C_j, including isolated vertices.
For each component use its inherited index order and let V_j=I+N_j and V_abs,j=I-|N_j|.
The full pencil factors over these components.
Because alpha is a simple root of the full polynomial, exactly one component C_* contains that root.
Every other original component polynomial is neutral, and C_* contains the unique expanding/contracting pair.
The latter assertion also follows directly from reciprocity of each component pencil; it does not assign a different degree to P.

Call C_* switchable to the absolute sign pattern if there is a diagonal sign matrix D_* on that component such that

    D_* N_* D_*=-|N_*|,
    equivalently D_* V_* D_*=V_abs,*.                    (1)

Then

    m(p_abs)=m(P)

holds IF AND ONLY IF both conditions hold:

    (i) C_* is switchable in the precise sense of (1);
    (ii) m(p_abs,j)=0 for EVERY j different from *.       (2)

For (ii), an isolated vertex contributes t+1 and automatically satisfies the condition.
Since each complete p_abs,j is monic with constant one, zero Mahler measure is equivalent to all its roots lying on the unit circle.
The same criterion is equivalent to m(p_cover)=2m(P).
If either condition fails, both measure comparisons are strict:

    m(p_abs)>m(P), m(p_cover)>2m(P).                     (3)

This is conditional on the stated actual proper realization.
It constructs no realization or neutral multiplier and makes no claim about repeated positive factors, multiple expanding pairs, negative expanding roots or nonreal expanding roots.
For the expanding component, switching is equivalent to product_((i,j) on C)(-sign N_ij)=1 on EVERY support cycle C, or equivalently the product of original entry signs is(-1)^(cycle length).
With several support components, neutral absolute measure does not assert equality of all neutral polynomials or switching of every neutral block.
No quantitative strict margin, upper realization, nonpositive expanding-pair extension or unrestricted original gap is proved.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:24 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every actual integral realization of one simple genuine Salem factor times all neutral factors, arbitrary support/rank/height; exact expanding-block negative switching and all-neutral-absolute-block equivalence, full-cover strictness and cycle signs with no margin or existence assertion. |
| argument | [Entire complete argument](#argument) | Every actual integral realization of one simple genuine Salem factor times all neutral factors, arbitrary support/rank/height; exact expanding-block negative switching and all-neutral-absolute-block equivalence, full-cover strictness and cycle signs with no margin or existence assertion. |
| dependency | [Exact fixed input](Yin_C_G0566_v1.md#positive-root-companion-proof) | Complete signed kernel/absolute inequality, connected-block left Perron pairing, continuous crossing and inherited nilpotence. |
| dependency | [Exact fixed input](Yin_C_G0566_v1.md#salem-neutral-companion-consequence) | Single simple positive Salem factor and every neutral factor, full measure and actual realization premise. |
| dependency | [Exact fixed input](Yin_C_G0002_v1.md#signed-cover-identity) | Literal cover, sign congruence sufficiency and complete factor accounting. |
| support | [Exact fixed input](Yin_C_G0500_v1.md#single-expanding-complete-classification) | Prior bipartite equality/neutral classification for consistency only; new arbitrary-support necessity is proved locally, and no quantitative margin is imported. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:29 |
| status | proved |
| reason | Under the current human maintenance authorization, adopt this exact complete current Statement and original complete Argument after the actually completed R752 constructor SELF whole inspection. Retain every original source, author, native, historical-review and unresolved-domain boundary, and preserve open initial precision predecessors. No research or new mathematical producer is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every actual integral realization of one simple genuine Salem factor times all neutral factors, arbitrary support/rank/height; exact expanding-block negative switching and all-neutral-absolute-block equivalence, full-cover strictness and cycle signs with no margin or existence assertion. |
| argument | [Entire complete argument](#argument) | Every actual integral realization of one simple genuine Salem factor times all neutral factors, arbitrary support/rank/height; exact expanding-block negative switching and all-neutral-absolute-block equivalence, full-cover strictness and cycle signs with no margin or existence assertion. |
| dependency | [Exact fixed input](Yin_C_G0566_v1.md#positive-root-companion-proof) | Complete signed kernel/absolute inequality, connected-block left Perron pairing, continuous crossing and inherited nilpotence. |
| dependency | [Exact fixed input](Yin_C_G0566_v1.md#salem-neutral-companion-consequence) | Single simple positive Salem factor and every neutral factor, full measure and actual realization premise. |
| dependency | [Exact fixed input](Yin_C_G0002_v1.md#signed-cover-identity) | Literal cover, sign congruence sufficiency and complete factor accounting. |
| support | [Exact fixed input](Yin_C_G0500_v1.md#single-expanding-complete-classification) | Prior bipartite equality/neutral classification for consistency only; new arbitrary-support necessity is proved locally, and no quantitative margin is imported. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0752_v1.md#current-g429-complete-self-finding) | Entire current exact Statement and complete Argument with all listed fixed inputs, original degrees/factors/kernel/support/error costs and stated limitations; actual constructor SELF. |

## Complete original argument

<a id="argument"></a>

### Original account: Exact companion equality for an arbitrary single-Salem unitriangular realization

Date: 2026-10-18T17:58.
Human author Yin.
Root assigned the bounded equality question after the fixed positive-root theorem L428.
The loglog_cyclic_review agent supplies every new deduction below; root supplied the question, not a criterion or proof step.
No fixed L428 text is changed.
There is no numerical run, matrix enumeration, optimization, new source acquisition or quantitative-frustration investigation.

<a id="general-single-pair-equality-reuse"></a>
## Reuse and the exact extension

Read the actual [L428 positive-root proof](Yin_C_G0566_v1.md#positive-root-companion-proof), now covered by the separately assigned [R440](../audits/reviews/Yin_R_G0440_v1.md), and [L405's bipartite equality criterion](Yin_C_G0500_v1.md#single-expanding-complete-classification).
L405 already retains disconnected neutral components, the difference between equal measure and equal polynomials, and a separately paid finite frustration estimate.
Its singular-value argument concerns bipartite matrices; no such representation is assumed here.
[C2](Yin_C_G0002_v1.md#signed-cover-identity) already proves that diagonal sign switching to nonpositive strict-upper entries is sufficient for complete polynomial equality and gives the literal cover product.
A targeted search/read of the retained equality, switching and positive-root interfaces found no exact non-bipartite necessity statement below.
No historical novelty assertion follows from this bounded search.

The current proof follows the equality steps of the ACTUAL positive-root pencil, rather than inferring a general equality theorem from L405's singular values.
It stops at an exact qualitative criterion, with no uniform strict margin or cost minimization.

<a id="general-single-pair-equality-statement"></a>
## 1. Statement with every support component retained

Let V=I+N be an integral upper-unitriangular matrix of rank R, B=|N| entrywise, and V_abs=I-B.
Write

    p_V(t)=det(tV+V^T),
    p_abs(t)=det(tV_abs+V_abs^T),
    p_cover=p_V p_abs.

Assume the ENTIRE original polynomial is p_V=P Q, where P is the monic minimal polynomial of a genuine Salem number alpha>1 occurring ONCE, and Q is any monic integer polynomial with every root on the unit circle.
All multiplicities and every neutral factor of Q are retained, and R=deg P+deg Q is the actual matrix rank.
There is no bound on rank, entry height, neutral degree or support cycles.
In particular m(p_V)=log alpha=m(P).

Decompose the undirected support graph of B into connected components C_j, including isolated vertices.
For each component use its inherited index order and let V_j=I+N_j and V_abs,j=I-|N_j|.
The full pencil factors over these components.
Because alpha is a simple root of the full polynomial, exactly one component C_* contains that root.
Every other original component polynomial is neutral, and C_* contains the unique expanding/contracting pair.
The latter assertion also follows directly from reciprocity of each component pencil; it does not assign a different degree to P.

Call C_* switchable to the absolute sign pattern if there is a diagonal sign matrix D_* on that component such that

    D_* N_* D_*=-|N_*|,
    equivalently D_* V_* D_*=V_abs,*.                    (1)

Then

    m(p_abs)=m(P)

holds IF AND ONLY IF both conditions hold:

    (i) C_* is switchable in the precise sense of (1);
    (ii) m(p_abs,j)=0 for EVERY j different from *.       (2)

For (ii), an isolated vertex contributes t+1 and automatically satisfies the condition.
Since each complete p_abs,j is monic with constant one, zero Mahler measure is equivalent to all its roots lying on the unit circle.
The same criterion is equivalent to m(p_cover)=2m(P).
If either condition fails, both measure comparisons are strict:

    m(p_abs)>m(P), m(p_cover)>2m(P).                     (3)

This is conditional on the stated actual proper realization.
It constructs no realization or neutral multiplier and makes no claim about repeated positive factors, multiple expanding pairs, negative expanding roots or nonreal expanding roots.

<a id="general-single-pair-equality-proof"></a>
## 2. Equality at the positive-root pencil forces switching

Use a nonzero real vector x supported on C_* with

    (alpha V_*+V_*^T)x=0.

Such a real vector exists because the real component pencil is singular.
Put v=|x|, M(t)=t|N_*|+|N_*|^T and h(t)=t+1-rho(M(t)).
The component is not an isolated vertex, and M(t) is irreducible nonnegative for every t>0.
L428's actual argument gives

    M(alpha)v>=(alpha+1)v,
    rho(M(alpha))>=alpha+1,
    h(alpha)<=0,
    h(t)>0 for all sufficiently large t.                (4)

The last statement retains rho(M(t))/t->rho(|N_*|)=0, because the inherited principal matrix |N_*| is strictly upper triangular.
Continuity is sufficient; no monotonicity or unique outside root for the absolute polynomial is assumed.

Suppose first m(p_abs)=log alpha.
If h(alpha)<0, the same intermediate-value argument gives an actual positive root t0>alpha of p_abs,* and hence of the COMPLETE p_abs.
Its contribution would make m(p_abs)>=log t0>log alpha, a contradiction.
Therefore h(alpha)=0 and rho(M(alpha))=alpha+1.

Take a strictly positive left Perron vector u of M(alpha).
The vector M(alpha)v-(alpha+1)v is nonnegative, and its scalar product with u is zero.
Thus every coordinate of that difference is zero:

    M(alpha)v=(alpha+1)v.                               (5)

The vector v is in fact strictly positive.
If some v_i were zero, equation (5), with positive entries along every incident support edge, would force all neighboring coordinates to be zero; connectedness would then force v=0, contradicting x!=0.
Hence every x_i is nonzero, including coordinates not known to be nonzero at the start.

For each row the original signed equation is

    (alpha+1)x_i=-sum_j (alpha N_*+N_*^T)_ij x_j.

Equation (5) states equality in the corresponding absolute-value triangle inequality.
The nonzero summands on the right must all have the sign of x_i, because their sum is the nonzero number (alpha+1)x_i.
For every support edge i--j, the relevant coefficient has the sign of the single original upper entry N_ij (with indices interchanged when necessary); the multiplying factor is either alpha>0 or one.
Writing d_i=sign(x_i), this gives

    sign(N_ij)=-d_i d_j

for every nonzero strict-upper entry of this component.
Thus D_*=diag(d_i) satisfies (1).
This proves necessity of switching without assuming a positive signed eigenvector, a bipartite support graph or nonsingular symmetric Gram form.

Conversely, (1) gives an exact pencil congruence by D_* and therefore

    p_abs,*=p_V,*.

Every original root outside the unit circle belongs to this component, so m(p_abs,*)=log alpha.
This proves sufficiency on the expanding component.
It also proves strictness there when switching fails: since (4) holds and h(alpha)=0 would force switching by the preceding argument, failure of (1) forces h(alpha)<0 and an absolute root strictly greater than alpha.
No quantitative lower separation is extracted.

<a id="neutral-block-equality-accounting"></a>
## 3. Full neutral-block accounting and the exact graph test

Grouping support components is a simultaneous coordinate permutation; there are no matrix entries between distinct groups.
Each component is upper-unitriangular in inherited order, so its pencil is monic, has constant one and is reciprocal by transposition.
The complete factorization and measure additivity are

    p_V=product_j p_V,j,
    p_abs=product_j p_abs,j,
    m(p_abs)=sum_j m(p_abs,j).                           (6)

Every summand in the last line is nonnegative.
By L428 the expanding component alone contributes at least log alpha.
Consequently equality for the full measure implies zero contribution from every other absolute component and equality on C_*.
The previous section then proves (i), while those zero contributions give (ii).
Conversely (i) gives exactly log alpha on C_* and (ii) makes every other summand zero, proving the complete iff criterion.
If (i) fails the expanding component already contributes strictly more; if (ii) fails at least one additional summand is positive.
The literal cover identity adds m(P) to both alternatives, proving (3).
No absolute factor, disconnected neutral direction or multiplicity is deleted.

Condition (i) can also be checked on the original support edges without spectral computation.
Assign the edge label -sign(N_ij) to each undirected edge of C_*.
Then (1) is equivalent to the product of these labels being +1 around every support cycle.
Indeed vertex signs cancel twice on a cycle.
Conversely choose a spanning tree, fix one vertex sign and propagate it along the tree according to the labels; a chord agrees exactly when the label product around its tree cycle is +1.
Equivalently the original entry-sign product on a cycle of length l must equal (-1)^l.
Trees cause no exception.
This criterion uses the negative absolute convention V_abs=I-|N|; it is not the all-positive cycle test for the original signs on an arbitrary non-bipartite graph.

If the full nontrivial support is connected, there are no other nontrivial components to test in (ii); isolated vertices contribute t+1 on both sides.
Equality then holds precisely when the expanding support is switchable, and in this case the ENTIRE original and absolute polynomials agree.
For a disconnected support satisfying (2), original and absolute neutral component polynomials need not agree; equal complete measures alone do not assert polynomial equality there.
The criterion does not require every neutral component to be switchable, only that its complete absolute polynomial remain neutral.

<a id="general-equality-scope-boundary"></a>
## 4. Exact relation to the older bipartite result

For V=[[I,-H],[0,I]], the original strict-upper edge signs are -sign(H_ij).
Thus (1) reduces exactly to row/column sign switching of H to |H|, and (ii) reduces to neutrality of every other absolute singular-value block.
The present criterion agrees with L405 on that domain, including disconnected neutral components and isolated Phi2 factors.
Its new domain is arbitrary proper unitriangular support with the same complete single-Salem factor hypothesis.

The proof supplies only equality versus strictness, not a uniform positive additive margin.
L405 already retains L299's connected frustrated single-pair controls whose positive measures approach the same positive limit; that earlier counterboundary is unchanged.
No quantitative resistance, Perron-weight lower bound, entry optimization or neutral-factor search is undertaken here.
The L238 universal integral companion floor also remains a separate accepted lower bound.
Neither this equality classification nor that floor constructs a cheap realization or proves an original-input Mahler gap.

<a id="general-equality-fixed-inputs"></a>
## Inputs and author check

| Input | Exact role |
| --- | --- |
| [L428 positive-root argument](Yin_C_G0566_v1.md#positive-root-companion-proof), [R440](../audits/reviews/Yin_R_G0440_v1.md) | Connected-block nonnegative subeigenvector, left Perron bound, continuous crossing and nilpotent tail, with every original and absolute factor. This author contributed L428 and reuses root's separate whole review. |
| [L428 Salem-neutral consumer](Yin_C_G0566_v1.md#salem-neutral-companion-consequence) | Arbitrary actual proper realization of one Salem factor times any neutral factor and its full cover lower bound; no equality claim inherited. |
| [L405 equality mechanism](Yin_C_G0500_v1.md#connected-sign-equality), [full neutral classification](Yin_C_G0500_v1.md#single-expanding-complete-classification) | Earlier bipartite equality, sign propagation and full disconnected neutral costs; the non-bipartite necessity is proved here. |
| [C2 full cover](Yin_C_G0002_v1.md#signed-cover-identity) | Complete original-times-absolute factorization and switching sufficiency, without rank normalization. |
| [L238 integral floor](../ledger/Yin_L_G0238_v1.md#uniform-companion-gap-and-bounded-ratio) | Existing uniform extra-factor floor, comparison only; no new source proof or original-measure implication. |
| [L405 strict-margin boundary](Yin_C_G0500_v1.md#single-pair-next-boundary) | Existing nonuniform additive-margin comparison through L299, not a new quantitative result. |

All new deductions are by loglog_cyclic_review; root supplied the question only.

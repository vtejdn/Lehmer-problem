---
author: Yin
---

# Complete unit-cycle leaf integer realizations and full companion expenses

This retains the complete [L299](../ledger/Yin_L_G0299_v1.md) proof; the original [written](../audits/reviews/Yin_R_G0776_v1.md#unit-cycle-leaf-complete-written-review) and [computational](../audits/reviews/Yin_R_G0776_v1.md#unit-cycle-leaf-complete-computational-review) findings retain their original inputs and dates at their current home, with no new source/native run.

<a id="statement"></a>
## Complete statement

For EVERY integer a>=3, let B0_a have diagonal1, superdiagonal1, lower-left-1 and all other entries0.
Append the row e_1^T to obtain the (a+1)-by-a matrix B_a and put D_a=|B_a|.
Use the actual integral upper-unitriangular matrices V_a=[[I_(a+1),-B_a],[0,I_a]] and V_a^- with B_a replaced by D_a.
Their actual plus-sign determinants p_V=det(tV+V^T), with s=t+1 and C_j=1+t+...+t^j, are
    P_a=s(t^a+1)^2-t C_(2a-1),
    A_a=s(t^a-1)^2-t C_(2a-1),
    p_cover=P_a A_a.
Original/absolute rank,height,energy are(2a+1,1,2a+1); literal proper cover costs are(4a+2,1,4a+2).
All matrices are in the displayed standard integer basis and every full factor remains.
For H=t^2-t-1 and H*=1-t-t^2,
    (t-1)P_a=(t^a+1)(t^a H-H*),
    (t-1)A_a=(t^a-1)(t^a H+H*).
These polynomial identities delete no actual factor or degree.
Both B/D have full column rank, so each full determinant has EXACTLY one t+1 factor.

For a>=5, P_a and A_a each have exactly one simple positive expanding reciprocal pair beta_a and alpha_a.
With phi=(1+sqrt5)/2, one has1<beta_a<phi<alpha_a<2.
Every remaining root is on the unit circle.
The full measures are log beta_a, log alpha_a and their SUM for the cover.
beta_a increases strictly to phi and alpha_a decreases strictly to phi; complete companion/original and cover/original ratios tend to1 and2.
At a=3 and4 the FULL original has zero measure, with exact factors
    P_3=Phi2 Phi6 Phi12,
    P_4=Phi1^2 Phi2 Phi3 Phi8.
The absolute side has positive measure there; these cases are excluded from positive original ratio claims.

For a>=5, the unique positive irreducible factors F_a/G_a occur once and are reciprocal, with all other factors cyclotomic.
Every contracting/circle conjugate is charged in the nonzero INTEGER resultant against H.
They satisfy
    deg F_a>2+[a log(7/5)-log(20/3)]/log3,
    deg G_a>2+[a log(3/2)-log8]/log3,
    0<phi-beta_a<(5/3)(5/7)^a,
    0<alpha_a-phi<2(2/3)^a,
    0<m(A_a)/m(P_a)-1
       <[(5/3)(5/7)^a+2(2/3)^a]/[(7/5)log(7/5)].
These are actual growing positive degrees at fixed positive limiting TOTAL measure log phi.

At a=5, the FULL rank11 original is Phi2 Phi10 S6, S6=t^6-t^4-t^3-t^2+1, and the full companion is Phi2 Phi5 Phi6 P4, P4=t^4-t^3-t^2-t+1.
S6 is genuinely irreducible; all original/companion/cover neutral degrees5/7/12 and full rank/energy11/11/22 remain.
The actual roots satisfy7/5<beta_S6<3/2 and5/3<beta_P4<7/4.
This paid rank11 realization does not contradict the distinct proper-rank6 obstruction, and it proves no minimum rank or global optimum.

The scalar Salem-Boyd sequence form and classical root-convergence mechanism retain the accepted Hir06 attribution only.
All actual plus-sign matrix, full-root and expense assertions have the local complete proof; no topological sign convention or uninspected source theorem is imported.
The sole J75 author run is2026-10-10T06:18,0.36307430002489127seconds, on exactly a=3,...,8.
Every18 complete arrays,306 saved pencils,24 secondary minor/Gram checks and all original source/native/written/computation limits remain without rerun.
The old R198 written/computation findings have unestablished extra initial target-mathematical context/order and remain UNKNOWN.
No near-one family, arbitrary-target coverage, minimum-rank theorem, optimal full scalar expense or unrestricted gap is asserted.

## Complete argument

<a id="argument"></a>

<a id="unit-cycle-leaf-reuse"></a>
### 1. Reuse and the changed construction

The Task, knowledge-reuse rules and full [L295](Yin_C_G0564_v1.md#statement) were read.
L295 pays for one weight-two edge and its positive root limit4.
Here that edge is replaced by a UNIT signed cycle with ONE unit leaf.
Thus every entry has height one, the growing core and full original polynomial change, and no repeated neutral pair or fixed positive factor is inserted.
The [L184 cycle formula](Yin_C_G0437_v2.md#cycle-order-polynomial), [L203 leaf recurrence](Yin_C_G0488_v1.md#pendant-chain-full-determinant), [L191 Gram determinant](Yin_C_G0458_v2.md#higher-degree-phi2-realization), [L242 complete lower-measure comparison](../ledger/Yin_L_G0242_v1.md#neutral-background-growing-salem-factor), and [D9 literal cover](Yin_C_G0002_v1.md#signed-cover-identity) supply the needed fixed mechanisms.
Their exact conventions were checked before derivation.
A local ledger screen for signed cycle/pendant scalar costs found L184's different surgery/energy-barrier claims; no absence or historical novelty claim is inferred.

The factorization below is a classical Salem-Boyd sequence with seed H=t^2-t-1.
That sequence form and its general root-convergence mechanism are ALREADY attributed to the published [Hir06 scoped reading](../audits/literature/Hir06/readme.md), introduction/Theorems1,3 and Section3.1 at its retained inspection limits.
They are not newly claimed constructions of Salem numbers.
The actual plus-sign integer matrices, complete companion matching, explicit paid realization of S6 and all cost/degree statements are derived here.
The original/absolute root counts are proved directly by the Gram quadratic form, so neither a topological convention transfer nor an uninspected source classification is needed.
The earlier E8/T(2,3,n) references in L246 remain comparison leads only and are not a theorem used here.
No new external statement, acquisition or novelty claim is required.

All new deductions and any declared verifier are by orbit_research for Yin.
Root supplied only the broad question and operational coordination.
For a proper integral upper-unitriangular V use p_V=det(tV+V^T), with V^- having strict-upper entries -|V_ij| and diagonal one.
Its literal proper cover has full polynomial p_V p_(V^-); all neutral multipliers, ranks and energies remain paid.

<a id="unit-cycle-leaf-full-polynomials"></a>
### 2. Standard integral matrices and complete scalar factors

For a>=3 define the a-by-a matrix B0_a with diagonal1, superdiagonal1, lower-left -1 and every other entry zero.
Append the row e_1^T to obtain the (a+1)-by-a matrix B_a.
Let D_a=|B_a| and

    V_a=[[I_(a+1),-B_a],[0,I_a]],
    V_a^-=[[I_(a+1),-D_a],[0,I_a]].                   (1)

These are actual upper-unitriangular integer matrices in the displayed standard basis.
The support is a2a-cycle plus a single leaf.
The original cycle sign product is -1 and the absolute cycle has all upper signs negative.
Bipartition order has a ascents on the cycle.
The extra left vertex is the leaf attached to the first right vertex.
No change of lattice, basis, normalization or graph order is implicit.

Let C_j(t)=1+t+...+t^j and s=t+1.
Deleting the leaf gives the signed or absolute cycle, whose full polynomials are(t^a+1)^2 and(t^a-1)^2.
Deleting its neighbor as well leaves a path on2a-1 vertices, with full polynomial C_(2a-1).
The exact leaf determinant expansion therefore gives

    P_a=p_(V_a)=s(t^a+1)^2-t C_(2a-1),
    A_a=p_(V_a^-)=s(t^a-1)^2-t C_(2a-1),
    p_cover=P_a A_a.                                  (2)

The leaf need not be placed last for this expansion: its two opposite pencil entries have product t, and all remaining indices retain their given induced order.
The path has no cycle term, so its determinant is the usual full path matching polynomial independently of its edge signs or ordering.
These facts are the previously retained formulas applied to this actual support.

Put H(t)=t^2-t-1 and H^*(t)=1-t-t^2, with reversal at degree two.
Direct multiplication yields the COMPLETE identities

    (t-1)P_a=(t^a+1)[t^a H-H^*],
    (t-1)A_a=(t^a-1)[t^a H+H^*].                     (3)

For example both numerator expansions have leading term t^(2a)H and constant block -H^*, while their middle term is respectively +2(t^2-1)t^a or -2(t^2-1)t^a.
The division by t-1 is the displayed polynomial identity, not removal of a factor from the actual matrix.
Equivalently P_a=(t^a+1)Q_a^- with Q_a^-=(t^a H-H^*)/(t-1), while A_a=C_(a-1)Q_a^+ with Q_a^+=t^a H+H^*.
These retain every cyclotomic contribution.
Both determinants have degree2a+1, and the cover has degree4a+2.

Original and absolute matrices have rank2a+1, height1 and squared strict-upper energy2a+1.
The proper cover has rank4a+2, height1 and energy4a+2.
Every matrix is unimodular.
In particular the rank is not the degree of a selected Salem factor unless the full cofactor is separately accounted for.

Both B_a and D_a have full column rank.
The equations from their first a rows determine every coordinate of a possible kernel vector by successive alternating signs from its first coordinate; the appended row sets that first coordinate to zero, so the entire kernel is zero.
The Gram formula hence gives exactly one unavoidable factor s from the rectangular rank difference, with the remaining factors

    p_V=s product_(j=1)^a [t^2+(2-lambda_j)t+1],        (4)

where the lambda_j are the strictly positive eigenvalues of B_a^T B_a or D_a^T D_a.
Since a quadratic in(4) has value lambda_j at t=-1, s has exactly multiplicity one.
Other cyclotomic factors may remain, and are never called absent without a proof.

<a id="unit-cycle-leaf-root-count"></a>
### 3. All roots, exact positive threshold and lower total measure

There is at most one lambda_j>4, counted with multiplicity, for either sign.
Indeed for the unit signed cycle adjacency H0, the elementary inequality |x^T H0 x|<=2||x||^2 makes G0=2I-H0 positive semidefinite.
Adding the unit leaf gives the symmetric form

    G=[[G0,w],[w^T,2]], w=+/-e_v.

Completing the leaf square makes G congruent to diag(G0-(1/2)e_v e_v^T,2).
Its first block is nonnegative on the codimension-one subspace x_v=0, so it has at most one negative eigenvalue.
For the bipartite adjacency, each singular value of B_a or D_a gives the two eigenvalues plus/minus that singular value, with one extra zero eigenvalue.
Consequently negative eigenvalues of2I-H correspond exactly to Gram eigenvalues lambda>4.
This proves the claimed full root count without a canonical Coxeter or indefinite-isometry classification.

The exact values at one are

    P_a(1)=8-2a, A_a(1)=-2a.                         (5)

Let phi=(1+sqrt5)/2, the positive root of H.
Since H^*(phi)=-2phi, (3) shows P_a(phi)>0 and A_a(phi)<0.
Also Q_a^+(2)=2^a-5>0.
Thus for EVERY a>=5 there are unique simple positive expanding roots beta_a,alpha_a with

    1<beta_a<phi<alpha_a<2.                          (6)

Their reciprocal partners are the only strictly contracting roots, and every other root of the complete degree2a+1 determinants is on the unit circle.
Neither t=1 nor a second expanding pair is hidden: (5) is nonzero in this range and the negative-index argument counts multiplicity.
The full logarithmic measures are therefore

    m(P_a)=log beta_a,
    m(A_a)=log alpha_a,
    m(p_cover)=log beta_a+log alpha_a.                (7)

The original threshold a=5 is exact among a>=3.
For a=3,4 the frustrated cycle form G0 is actually positive definite: equality in its edge Cauchy bound at eigenvalue2 would require a consistent sign assignment around the cycle, contrary to its frustrated product.
A negative rank-one perturbation of this positive definite form has all but possibly its least eigenvalue positive.
Its full determinant has the sign of P_a(1).
At a=3 this determinant is positive, so the form remains positive definite; at a=4 it is zero, so it is positive semidefinite with precisely one zero eigenvalue.
Thus both complete original determinants have zero measure at a=3,4.
The absolute form, by(5), has exactly one negative direction and a positive-measure root for every a>=3.
These boundary controls are not nontorsion near-one inputs.
Their complete original factorizations are P_3=Phi2 Phi6 Phi12 and P_4=Phi1^2 Phi2 Phi3 Phi8, as follows by multiplying the polynomials in(3).
Here P_4 denotes the index-four determinant only in this sentence; the named quartic P4 below is a different fixed polynomial.

<a id="unit-cycle-leaf-root-motion"></a>
### 4. Exact limiting cost, genuine degree growth and quantitative bounds

For t>1, H^*(t)<0.
At an original root beta_a, t^a H=H^*.
Hence

    N_(a+1)^-(beta_a)=(beta_a-1)H^*(beta_a)<0,
    N_a^-(t)=t^a H(t)-H^*(t).

The numerator N_a^- differs from the quotient Q_a^- in Section2 by the positive factor t-1 for t>1.
Its next unique root above one therefore satisfies beta_(a+1)>beta_a.
For the absolute root, t^a H=-H^*, so

    [t^(a+1)H+H^*]_(t=alpha_a)
          =-(alpha_a-1)H^*(alpha_a)>0,

giving alpha_(a+1)<alpha_a.
The signs of the complete factors outside the numerators in(3) are positive at t>1; no root of them can change this conclusion.
After division of the root equations by t^a, boundedness away from one shows that both limits are phi.
An explicit such lower bound is supplied in Section5 and then applies to all larger indices.
Therefore

    beta_a increases to phi, alpha_a decreases to phi,
    m(A_a)/m(P_a)>1 and tends to1,
    m(p_cover)/m(P_a)>2 and tends to2.                (8)

These are whole-measure ratios.
They are not normalized by rank, an assertion that signed companion measures always dominate, or a claim that this family gives a global minimum.
The original total measure stays below log phi; it tends to that positive number rather than to zero.

As in L295, each complete determinant has exactly one positive-measure monic irreducible factor, F_a in P_a and G_a in A_a, each occurring once.
Their unit constant terms force a factor containing the expanding root to contain its contracting reciprocal; every remaining irreducible factor is cyclotomic.
The resulting exact description is

    P_a=C_a F_a, A_a=E_a G_a,
    deg C_a=2a+1-deg F_a, deg E_a=2a+1-deg G_a,        (9)

with the full cyclotomic multiplicities retained in C_a,E_a.
Strict root motion implies the positive factors are pairwise distinct in each family.
Their bounded root moduli imply finite coefficient sets at any fixed degree, so both irreducible degrees tend to infinity.
No fixed positive background is present.

There is a stronger paid linear bound.
Section5 proves for all a>=5

    7/5<beta_a<phi<alpha_a<=beta4<7/4,

where beta4 is the positive root of P4=t^4-t^3-t^2-t+1.
Since H^*(t)=1-t-t^2, the root equations give

    |H(beta_a)|< (10/3)(5/7)^a,
    |H(alpha_a)|<4(2/3)^a.                           (10)

We used phi<5/3 and phi>3/2.
For the contracting reciprocals, H(1/t)=t^(-2)H^*(t), so their absolute H-values are less than2 in both cases.
Every circle conjugate z has |H(z)|<=3.
The integer resultants Res(H,F_a), Res(H,G_a) are nonzero: neither positive root is phi, and the other root of H has modulus below one without being its positive reciprocal.
Thus, putting d_a=deg F_a and e_a=deg G_a,

    1<=|Res(H,F_a)|<(20/3)(5/7)^a 3^(d_a-2),
    1<=|Res(H,G_a)|<8(2/3)^a 3^(e_a-2),
    d_a>2+[a log(7/5)-log(20/3)]/log3,
    e_a>2+[a log(3/2)-log8]/log3.                     (11)

This is a direct integer norm argument adapting L295's evaluation at4 to the quadratic limit polynomial H.
It keeps every conjugate and is not an assertion that the full determinants are irreducible.
In particular the actual positive irreducible complexity grows at least linearly in a despite possible growing neutral degree.

Factoring H(t)=(t-phi)(t+1/phi), the denominator beta_a+1/phi exceeds2, as does alpha_a+1/phi.
Consequently

    0<phi-beta_a<(5/3)(5/7)^a,
    0<alpha_a-phi<2(2/3)^a,
    0<m(A_a)/m(P_a)-1
      <[(5/3)(5/7)^a+2(2/3)^a]/[(7/5)log(7/5)].      (12)

The excess cover ratio above two is the same.
This supplies explicit all-root expense and convergence, not a numerical fit.

<a id="paid-s6-cycle-leaf-realization"></a>
### 5. A paid realization of the previously excluded sextic target

At a=5 the full identities(2)--(3) factor EXACTLY as

    S6=t^6-t^4-t^3-t^2+1,
    P4=t^4-t^3-t^2-t+1,
    P_5=Phi2 Phi10 S6,
    A_5=Phi2 Phi5 Phi6 P4,
    p_cover=Phi2^2 Phi5 Phi6 Phi10 S6 P4.             (13)

These follow by dividing t^5 H-H^* by t-1 to obtain S6, by t^5+1=Phi2 Phi10, and by

    t^5 H+H^*=(t+1)(t^2-t+1)P4,
    (t^5-1)/(t-1)=Phi5.

Every equality concerns the full original and absolute matrices, not an abstract factor deletion.
Original rank11, height1 and energy11, and proper-cover rank22, height1 and energy22, are literal.
The original pays cyclotomic degree5, the companion pays degree7, and the cover pays degree12 in addition to the sextic and quartic.
In particular this is outside L279's universal PROPER RANK6 exclusion for S6 and is not claimed to attain its minimum possible stabilizing rank.

For precision S6 is irreducible and has one expanding pair.
Its trace polynomial is v^3-4v-1, whose only possible rational roots +/-1 have values -4 and2.
It has roots in(-2,-1),(-1,0),(2,3), from values -1,2,-1,-1,14 at -2,-1,0,2,3.
Thus the trace cubic is irreducible and totally real.
At an inner real conjugate v^2-4<0, so it is not a square in that field, and the reciprocal lift doubles its degree to6.
Its exact expanding root beta_S satisfies

    S6(7/5)=-251/15625<0,
    S6(3/2)=109/64>0,
    7/5<beta_S<3/2.

The retained P4 has its unique expanding root beta4, with

    P4(5/3)=-29/81<0, P4(7/4)=53/256>0,
    5/3<beta4<7/4.

The root counts above or the retained quartic proof make these sign brackets actual root brackets.
Hence beta_5=beta_S and alpha_5=beta4, justifying the constants used in Section4 for all a>=5 by monotonicity.
The use of Section5 there is a dependency forward reference, not a circular inference: all the present polynomial factorizations and root intervals are independent of the bounds(10)--(12).

At this input the complete original/absolute/cover measures are

    log beta_S, log beta4, log beta_S+log beta4.       (14)

More generally beta_a<phi<5/3<beta4 and alpha_a<=beta4 show

    m(P_a)<log phi<m(P4),
    m(p_cover)<2m(P4),       a>=5.                   (15)

Thus the full scalar cost is genuinely lower than the known L191 rank6 Phi2^2 P4 presentation and its doubled cover cost, while the actual rank is larger and the input polynomial differs.
The original measures are also below every positive member of L242's family, whose minimal positive root is beta4.
None of these comparisons is a claim of record-small Salem measure, global cover optimality or a classification of other graphs.
The limiting original measure log phi remains strictly positive; small individual conjugate distances cannot be used to change that total.

<a id="unit-cycle-leaf-verification-declaration"></a>
### 6. Exact finite verification declared before execution

A new responsible J is requested for exactly a=3,4,5,6,7,8: six matrices(1), including the two zero-measure original boundary cases and four positive controls.
Aggregate author runtime cap120seconds; no search, numerical root discovery or extension of the index range is included.
For each control retain B_a,D_a,V_a,V_a^- and the literal proper cover; every full original/absolute/cover polynomial, actual rank/height/energy, and n+1 integer pencil evaluations at a rank-n matrix.
Check the full formulas(2)--(3), exact endpoint(5), full column rank and the first-index boundary factors.
At a=5 check ALL named cyclotomic factors and S6/P4, their four rational endpoints, both trace identities and the sextic rational-root list.
The all-a quadratic-form, monotonicity, limit and integer-resultant degree proofs are written arguments, not extrapolations from the controls.
Actual runs, failures and the final code scope will be recorded only after execution.

<a id="unit-cycle-leaf-author-verification"></a>
### 7. Executed evidence, complete self-check and remaining boundary

The declared computation was allocated as [J75](../computations/programs/Yin_J_G0075/readme.md).
Its first and sole author run completed at2026-10-10T06:18 in0.36307430002489127seconds on Python3.12.14/SymPy1.14.0.
Exactly six controls,18 complete original/absolute/literal-cover coefficient arrays and306 exact integer pencil evaluations passed.
Every declared matrix, Gram determinant, full-rank minor, quotient trace, endpoint, first-index factorization and paid a5 target check is retained in `result.json`; the program is `verify.py`.
The numerator identities were additionally checked symbolically using an independent variable y in place of t^a.
There was no failed execution, hidden index, search, cap expansion or numerical root claim.
This is an author computation, with exact helper reuse from the author's J74 disclosed in the J; it is not an independent review.

The author reread the entire argument and checked the following complete chain.
The literal standard integer matrix has the stated sign and bipartition order; deleting the leaf and then its neighbor leaves exactly the full cycle/path factors, with no scalar normalization.
The rectangular Gram factor s has multiplicity exactly one because the displayed column-rank equations have no nonzero solution.
The leaf Schur complement changes the negative index by at most one, and all other eigenvalues relevant to the positive threshold are strictly positive for the frustrated cycle.
Thus the determinant signs at1 certify the a3/4 zero-measure boundary and the a>=5 unique simple expanding pair.
The sparse numerator factors have positive prefactors for t>1, so the two opposite monotonicities and their common limit are justified on the full determinants.
The a5 factorization and rational brackets are derived independently before they are used in the quantitative forward references.
The integer resultants count expanding, contracting and every circle conjugate and are nonzero, yielding the stated linear factor-degree bounds.
The cost comparison uses complete logarithmic measures; energy and rank are reported separately rather than substituted for them.

This provides a height-one family of complete original measure below log phi, tending to log phi, with linearly growing positive irreducible degrees and a whole companion tending to the same measure.
It also realizes S6 after the explicit degree-five neutral multiplier Phi2 Phi10, with the full absolute and cover factors in(13).
It does not realize S6 in its excluded rank six, claim the displayed rank eleven minimal, or remove any neutral factors from an actual matrix.
The positive total measure remains bounded away from zero.
The classical Salem-Boyd sequence form is reused at the stated Hir06 inspection scope; no claim of novelty in the scalar number sequence, a universal signed-companion comparison, global minimum or unrestricted Lehmer gap is made.
All new proof and author computation are by orbit_research for Yin; root contributed only the question, allocation and coordination.
Complete noncontributor review and fixed adoption remain separate next operations.



## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:25 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Whole plus-sign determinant product with doubled actual rank and energy. |
| dependency | [Ordered cycle matching](Yin_C_G0437_v2.md#cycle-order-polynomial) | Exact induced edge/order convention for the unit signed cycle, not unrelated coverage claims. |
| dependency | [Complete leaf recurrence](Yin_C_G0488_v1.md#pendant-chain-full-determinant) | Actual full leaf/path determinant and reciprocal circle-factor mechanisms. |
| dependency | [Full Gram block](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Rectangular bipartition/positive Gram interface with all quadratic roots retained. |
| support | [Earlier weighted construction](Yin_C_G0564_v1.md#statement) | Actual weight-two architecture is a comparison/starting point, not a stronger family premise or a source of the new threshold. |
| support | [Full original J75 evidence](../computations/programs/Yin_J_G0075/readme.md) | All six finite exact domains, original complete programs/payloads/timings and separate computation scope, without replay. |
| support | [Original full proof/input](../ledger/Yin_L_G0299_v1.md#complete-retained-proof-and-review) | Entire original Sections1--7/equations1--15, complete source/author/native/boundary/cost limits; original formal findings together in R198. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:27 |
| status | proved |
| reason | Adopt the complete retained theorem after actual whole current SELF of the published Statement and entire Argument, preserving every actual matrix, full factor/root/cost and original source/native/negative limit; no isolated review or research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Whole plus-sign determinant product with doubled actual rank and energy. |
| dependency | [Ordered cycle matching](Yin_C_G0437_v2.md#cycle-order-polynomial) | Exact induced edge/order convention for the unit signed cycle, not unrelated coverage claims. |
| dependency | [Complete leaf recurrence](Yin_C_G0488_v1.md#pendant-chain-full-determinant) | Actual full leaf/path determinant and reciprocal circle-factor mechanisms. |
| dependency | [Full Gram block](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Rectangular bipartition/positive Gram interface with all quadratic roots retained. |
| support | [Earlier weighted construction](Yin_C_G0564_v1.md#statement) | Actual weight-two architecture is a comparison/starting point, not a stronger family premise or a source of the new threshold. |
| support | [Full original J75 evidence](../computations/programs/Yin_J_G0075/readme.md) | All six finite exact domains, original complete programs/payloads/timings and separate computation scope, without replay. |
| support | [Original full proof/input](../ledger/Yin_L_G0299_v1.md#complete-retained-proof-and-review) | Entire original Sections1--7/equations1--15, complete source/author/native/boundary/cost limits; original formal findings together in R198. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0750_v1.md#unit-cycle-leaf-whole-self) | Entire Statement and complete Argument, actual accepted dependency interfaces and all original source/native/negative limits. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:00 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire Argument after the actual isolated whole review completed2026-10-22T20:49 UTC, with all original domains, costs, failed/negative scopes, source depth and finite-evidence limits retained. The dated original reviews and current SELF findings keep their actual inputs and relationships; this decision neither backfills old review acts nor resumes research. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Whole plus-sign determinant product with doubled actual rank and energy. |
| dependency | [Ordered cycle matching](Yin_C_G0437_v2.md#cycle-order-polynomial) | Exact induced edge/order convention for the unit signed cycle, not unrelated coverage claims. |
| dependency | [Complete leaf recurrence](Yin_C_G0488_v1.md#pendant-chain-full-determinant) | Actual full leaf/path determinant and reciprocal circle-factor mechanisms. |
| dependency | [Full Gram block](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Rectangular bipartition/positive Gram interface with all quadratic roots retained. |
| support | [Earlier weighted construction](Yin_C_G0564_v1.md#statement) | Actual weight-two architecture is a comparison/starting point, not a stronger family premise or a source of the new threshold. |
| support | [Full original J75 evidence](../computations/programs/Yin_J_G0075/readme.md) | All six finite exact domains, original complete programs/payloads/timings and separate computation scope, without replay. |
| support | [Original full proof/input](../ledger/Yin_L_G0299_v1.md#complete-retained-proof-and-review) | Entire original Sections1--7/equations1--15, complete source/author/native/boundary/cost limits; original formal findings together in R198. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0776_v1.md#current-unit-cycle-leaf) | The complete current fixed Statement and entire Argument, all necessary mathematical interfaces and actual finite-evidence checks at2026-10-22T20:49 UTC; independently reviewed in the disclosed isolated arrangement, without native discovery/reviewer reruns. |


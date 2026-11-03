---
author: Yin
---

# Complete weighted-cycle integer matrices, all roots and full companion costs

This retains the entire [L295](../ledger/Yin_L_G0295_v1.md) proof and all original costs; its complete original formal written/computational findings are together in [R138](../audits/reviews/Yin_R_G0138_v1.md).

<a id="statement"></a>
## Complete statement

For EVERY integer a>=3, let B_a be the a-by-a integer matrix with diagonal1, superdiagonal1, lower-left-2 and all other entries0.
Put D_a=|B_a|, V_a=[[I_a,-B_a],[0,I_a]], and V_a^-=[[I_a,-D_a],[0,I_a]].
Use the actual plus-sign determinant p_V(t)=det(tV+V^T), and the literal integral proper cover of C2.
With C_j(t)=1+t+...+t^j, the COMPLETE determinants and cover are
    P_a=t^(2a)+1-3t C_(2a-2)+4t^a,
    A_a=t^(2a)+1-3t C_(2a-2)-4t^a,
    p_cover=P_a A_a.
Original/absolute rank,height,energy are(2a,2,2a+3); cover costs are(4a,2,4a+6).
Every neutral/cyclotomic factor remains and there is no lattice extension.
The sparse identities
    (t-1)P_a=t^(2a)(t-4)+4(t-1)t^a+4t-1,
    (t-1)A_a=t^(2a)(t-4)-4(t-1)t^a+4t-1
introduce no actual factor at1: P_a(1)=9-6a, A_a(1)=1-6a.
The actual B/D determinants are1+2(-1)^a and1-2(-1)^a.

Each FULL polynomial has exactly one simple positive expanding reciprocal pair, beta_a in(3,4) and alpha_a in(4,5), with every other root on the unit circle.
Thus m(P_a)=log beta_a, m(A_a)=log alpha_a and m(cover)=log beta_a+log alpha_a, with no rank/cover normalization.
The original beta_a increases strictly to4 and the absolute alpha_a decreases strictly to4.
The complete companion/original and cover/original logarithmic-measure ratios tend to1 and2, respectively.
Quantitatively,
    0<4-beta_a<13*3^(-a), 0<alpha_a-4<16*4^(-a),
    0<m(A_a)/m(P_a)-1
       <[13*3^(-a)+16*4^(-a)]/(3log3).
There is a unique monic positive irreducible factor F_a of P_a and G_a of A_a, each occurring once and reciprocal, with all remaining factors cyclotomic.
Their degrees satisfy
    deg F_a>2+(a log3-log52)/log5,
    deg G_a>2+(a log4-log64)/log5.
The bounds charge every contracting and circle conjugate through a nonzero INTEGER evaluation at4.
No complete irreducibility is claimed for arbitrary a.
At a=3 BOTH full sextics are irreducible, with their actual trace/rational-root/real-field arguments retained.

The sole original J74 author run is2026-10-10T05:49,0.2467733seconds; full author freeze2026-10-10T05:50.
All six indices a=3,...,8,18 complete polynomials,282 pencils, full matrices/energies/endpoints/trace/formal checks and the distinct original whole computational finding are retained without rerun.
The original R138 written and computational findings are both known SELF because actual candidate formulas and, separately, the preceding whole verdict were supplied before their checks.
The classical matching, literal cover and circle-factor mechanisms are reused at their accepted scopes.
No new external theorem/source acquisition, near-zero family, arbitrary-target realization, universal cost optimum or uniform Mahler gap is asserted.
Total original measure tends to the positive log4.

## Complete argument

<a id="argument"></a>

<a id="weighted-cycle-reuse-and-conventions"></a>
### 1. Reuse, changed architecture and conventions

The actual Task, knowledge-reuse and writing rules, current matrix-route handoff and full [L291](Yin_C_G0544_v1.md#statement) were read.
L291's universal paired block changes neither the original noncyclotomic factors nor the bounded residual degree at a fixed core.
Repeating that operation cannot answer this question.
A local screen read [L184's ordered-cycle determinant](Yin_C_G0437_v2.md#cycle-order-polynomial), [L196's weighted four-cycle calculation](../ledger/Yin_L_G0196_v1.md#interlaced-realization-fixed-scope), [L191's exact Gram block](Yin_C_G0458_v2.md#higher-degree-phi2-realization), [L203's full-factor/root argument](Yin_C_G0488_v1.md#bounded-measure-interlaced-fixed-scope), [L238's bounded-measure companion scope](../ledger/Yin_L_G0238_v1.md#bounded-companion-factor-fixed-scope), and [L242's neutral-core family](../ledger/Yin_L_G0242_v1.md#neutral-core-coupling-fixed-scope).
The general cycle matching formula, block determinant and monic integral circle-factor criterion are reused.
No cycle formula, finiteness theorem, Coxeter classification or source novelty is claimed as new.

The changed construction is a GROWING weighted cycle with one edge of magnitude two, arranged in bipartition order.
Its signed and absolute cycles differ in the sign of that edge.
The original positive factors change with the cycle length; no fixed positive core factor is repeated or deleted.
The complete original and companion measures both converge to log4, and their ratio tends to one from above.
This is a controlled-cost varying-complexity family, not a smaller total-measure seed than L242, a near-one family or an arbitrary-input realization theorem.

All deductions below are by orbit_research for Yin.
Root supplied the broad question and operational allocation only.
The local retained determinant mechanisms suffice for this direct modification; no new external theorem or source intake is used.
The elementary root-count argument below uses a displayed quadratic-form bound, not an imported classification of Lorentz or Coxeter isometries.

For a proper integral upper-unitriangular V set p_V(t)=det(tV+V^T), and V^- has strict-upper entries -|V_ij| and diagonal one.
[D9's literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) has full polynomial p_V p_(V^-), rank twice that of V, and twice its squared strict-upper energy.
This convention is unchanged throughout.
Full determinants, not selected factors, own all measures.

<a id="one-heavy-edge-complete-polynomial"></a>
### 2. Actual integer matrices and their whole polynomials

For every integer a>=3, let B_a be the a-by-a integer matrix with diagonal one, superdiagonal one, lower-left corner -2, and every other entry zero.
Put D_a=|B_a| and

    V_a=[[I_a,-B_a],[0,I_a]],
    V_a^-=[[I_a,-D_a],[0,I_a]].                       (1)

Every matrix is in the standard integer basis, upper triangular with diagonal one.
Its support is a simple2a-cycle, with2a-1 edges of magnitude one and one of magnitude two.
The signed edge product is -2, and the absolute all-negative cycle product is +2.
Bipartition order has exactly a ascents around the cycle.
There is no hidden basis change or normalization of the edge-two entry.

Write C_j(t)=1+t+...+t^j.
The full determinant formulas are

    P_a=p_(V_a)=t^(2a)+1-3t C_(2a-2)(t)+4t^a,
    A_a=p_(V_a^-)=t^(2a)+1-3t C_(2a-2)(t)-4t^a,
    p_cover=P_a A_a.                                 (2)

Indeed L184's identity/edge-transposition matching sum for a unit cycle is t^(2a)+1.
Changing one edge square from1 to4 changes exactly the matchings containing that edge: their extra contribution is -3t times the path matching polynomial C_(2a-2) on the remaining vertices.
The two full-cycle permutations each have negative sign; their products are -2 for the original and +2 for the absolute matrix, and each has t-exponent a.
These give respectively +4t^a and -4t^a.
All nonzero determinant permutations have been included.
This is also a direct specialization of the Gram determinant t^a det((t+t^(-1)+2)I-B_a^T B_a), and similarly for D_a.
Formula(2) retains every coefficient and every possible neutral factor.

Original and absolute ranks are2a, height2, and energy

    E(V_a)=E(V_a^-)=2a+3.

The proper cover has rank4a, height2 and energy4a+6.
Its complete polynomial has degree4a and is exactly the product in(2).
The matrices are integral unimodular; their construction entails no finite-index lattice extension.

Multiplying(2) by t-1 gives a useful sparse identity:

    (t-1)P_a=t^(2a)(t-4)+4(t-1)t^a+4t-1,
    (t-1)A_a=t^(2a)(t-4)-4(t-1)t^a+4t-1.             (3)

The t-1 factors here belong to these numerator identities, not to the determinants: P_a(1)=9-6a and A_a(1)=1-6a are nonzero.
They must not be added as padding or canceled from the actual cover.

<a id="weighted-cycle-all-root-control"></a>
### 3. Exactly one expanding pair in each complete determinant

Both Gram matrices B_a^T B_a and D_a^T D_a are positive definite.
In fact

    det B_a=1+2(-1)^a, det D_a=1-2(-1)^a,             (4)

because the only determinant permutations of I plus this weighted cyclic shift are the identity and the full a-cycle.
Neither determinant is zero.

There is at most one Gram eigenvalue strictly larger than4, counted with multiplicity.
To see this for either sign, let W denote B_a or D_a and let H=[[0,W],[W^T,0]] be its symmetric weighted-cycle adjacency.
Replace its heavy edge by an edge of the SAME sign and magnitude one, obtaining H_0.
For every real vector x,

    |x^T H_0 x|<=sum_edges 2|x_i x_j|<=2||x||^2,

since every cycle vertex has degree two.
Thus2I-H_0 is positive semidefinite.
The change H-H_0 is supported on the single heavy edge, and its quadratic form vanishes on the codimension-one subspace x_u=0, where u is either endpoint of that edge.
Hence2I-H is nonnegative on that subspace.
If H had two eigenvalues greater than2, their two-dimensional spectral subspace would meet x_u=0 nontrivially and would have strictly negative2I-H quadratic form there, a contradiction.
The positive eigenvalues of H are exactly the singular values of W, so at most one eigenvalue of W^T W exceeds4.
This proof covers either heavy-edge sign and arbitrary a in the stated range.

The Gram determinant expression after(2) maps an eigenvalue lambda to the full quadratic t^2+(2-lambda)t+1.
Strictly positive lambda<=4 gives a unit-circle pair (including the possible endpoint t=1).
A lambda>4 gives one positive expanding root and its reciprocal.
Direct signs now identify the sole exceptional eigenvalue and exclude the endpoint:

    (3-1)P_a(3)=-3^(2a)+8*3^a+11<0,
    (4-1)P_a(4)=12*4^a+15>0,
    (4-1)A_a(4)=-12*4^a+15<0,
    (5-1)A_a(5)=5^(2a)-16*5^a+19>0.                 (5)

For a>=3, the first and last inequalities follow by setting y=3^a>=27 or y=5^a>=125, respectively.
There is therefore exactly one expanding root beta_a of P_a and exactly one expanding root alpha_a of A_a, both simple, with

    3<beta_a<4<alpha_a<5.                            (6)

There are exactly their contracting reciprocals and2a-2 other roots, all on the unit circle, counted with multiplicity.
No Gram eigenvalue is zero by(4), and no eigenvalue is4 because neither polynomial vanishes at1.
Thus none of the remaining roots is +1 or -1.
The possible repeated unit-circle roots do not affect this full measure statement.
In particular the COMPLETE costs, with every root accounted for, are

    m(P_a)=log beta_a, m(A_a)=log alpha_a,
    m(p_cover)=log beta_a+log alpha_a.                (7)

This is not a Perron-only lower bound or a discarded-factor convention.

<a id="weighted-cycle-cost-limit-and-degree"></a>
### 4. Strict root movement, limiting costs and growing irreducible factors

The original roots increase strictly with a.
Put N_a^+(t)=(t-1)P_a(t).
Subtracting t^2 times the previous numerator gives

    N_(a+1)^+(t)-t^2 N_a^+(t)
      =-4t(t-1)^2 t^a-(4t-1)(t^2-1)<0, t>1.         (8)

At t=beta_a the new polynomial is negative.
Its only positive root above one is beta_(a+1), and it is positive above that root, so beta_(a+1)>beta_a.

For N_a^-(t)=(t-1)A_a(t) the same subtraction is

    N_(a+1)^-(t)-t^2 N_a^-(t)
      =4t(t-1)^2 t^a-(4t-1)(t^2-1)>0, t>4.          (9)

For the inequality it suffices to divide by t-1 and use a>=3:4t^(a+1)(t-1)>(4t-1)(t+1), which follows already from t^a>=t>4 and t(t-1)>t+1.
At t=alpha_a the new polynomial is positive.
Since the new polynomial is negative immediately above one and has exactly one root above one, alpha_(a+1)<alpha_a.
These sign conclusions also follow from the positive leading coefficient and the full root classification; no numerical ordering is used.

At either root, divide(3) by t^(2a).
The two lower terms tend to zero uniformly for t in[3,5].
Thus

    beta_a increases to4, alpha_a decreases to4,
    m(A_a)/m(P_a)>1 and tends to1,
    m(p_cover)/m(P_a)>2 and tends to2.                (10)

All total measures are uniformly bounded and positive: log3<m(P_a)<log4 and log4<m(A_a)<log5.
The cover measure lies strictly between log12 and log20 and tends to log16.
Bounds are on the full scalar determinants, without degree normalization.
The signed family does not attain companion ratio one at any finite a, and these limits are not a claim of optimality across other constructions.
The absolute all-negative presentations themselves trivially have equal original/companion costs; the content here is the actual changing signed family with its complete irreducible-factor complexity and no fixed positive background.

Each P_a has exactly one monic irreducible positive-measure factor F_a, of multiplicity one.
A factor containing beta_a must also contain beta_a^(-1): its integer constant term is plus or minus one, whereas all its other possible roots have modulus one; omission of the reciprocal would contradict the product of root moduli.
That factor therefore contains the entire off-circle pair.
Its reciprocal shares a root with it, so it is reciprocal, and all remaining factors are cyclotomic by the retained monic integral all-roots-on-the-circle criterion.
Write the COMPLETE factorization, without deleting it from(1), as

    P_a=C_a F_a, C_a cyclotomic (possibly1),
    A_a=Dtilde_a G_a, Dtilde_a cyclotomic (possibly1). (11)

The same argument applies to the absolute factor G_a.
No assertion that C_a or Dtilde_a always equals1 is made.

The F_a are pairwise distinct by strict increase of their sole expanding root, and the G_a are pairwise distinct by strict decrease.
Their degrees tend to infinity.
Indeed for any fixed degree bound d, all conjugates of these factors have modulus at most5, so their integer coefficients lie in the finite bounds |c_j|<=binom(d,j)5^j (with the actual factor degree used in each bound).
There are only finitely many such monic integer polynomials of bounded degree.
Pairwise distinctness then proves that only finitely many indices have bounded factor degree.
This is true growth of original and companion irreducible complexity with bounded total measure; it is not growth of neutral padding alone or a repeated fixed quadratic.
The full neutral degrees remain2a-deg F_a and2a-deg G_a in the respective rank2a determinants, and all of them remain in the rank4a cover.

The factor-degree growth can in fact be paid quantitatively.
Evaluating(3) at the actual roots and using(6) gives

    0<4-beta_a
      =4(beta_a-1)beta_a^(-a)+(4beta_a-1)beta_a^(-2a)
      <13*3^(-a),
    0<alpha_a-4
      =4(alpha_a-1)alpha_a^(-a)-(4alpha_a-1)alpha_a^(-2a)
      <16*4^(-a).                                    (11a)

For the first upper bound use12*3^(-a)+15*3^(-2a)<13*3^(-a), valid for a>=3.
The second follows by discarding its negative term and using alpha_a<5 and alpha_a>4.
Let d_a=deg F_a and e_a=deg G_a.
Since F_a(4) and G_a(4) are nonzero integers, their absolute values are at least one.
Their unique contracting roots are positive, their other d_a-2 or e_a-2 conjugates have modulus one, and each such conjugate has distance at most5 from4.
Therefore

    1<=|F_a(4)|<52*3^(-a)*5^(d_a-2),
    1<=|G_a(4)|<64*4^(-a)*5^(e_a-2),
    d_a>2+(a log3-log52)/log5,
    e_a>2+(a log4-log64)/log5.                        (11b)

The full determinant rank2a has thus at least the displayed LINEAR positive irreducible degree, with no assumption that its remaining factors are absent.
The same estimates give a fully explicit convergence expense for the entire companion ratio:

    0<m(A_a)/m(P_a)-1
      <[13*3^(-a)+16*4^(-a)]/(3 log3).                (11c)

Indeed log alpha_a-log beta_a< (alpha_a-beta_a)/beta_a and beta_a>3, log beta_a>log3.
The cover ratio exceeds two by exactly the same amount.
These bounds do not make the positive total original measure approach zero: it approaches log4 while the positive irreducible degree grows linearly.


<a id="weighted-cycle-irreducible-sextic-control"></a>
### 5. A complete irreducible sextic at the first index

At a=3 the actual full determinants are

    P_3=t^6-3t^5-3t^4+t^3-3t^2-3t+1,
    A_3=t^6-3t^5-3t^4-7t^3-3t^2-3t+1.              (12)

Their trace polynomials are respectively

    f(v)=v^3-3v^2-6v+7,
    g(v)=v^3-3v^2-6v-1,                              (13)

with P_3=t^3 f(t+t^(-1)) and similarly for A_3.
The possible rational roots of f are +/-1,+/-7; direct values are -1,9,161,-441 respectively.
The possible rational roots of g are +/-1, with values -9,1.
Thus both trace cubics are irreducible.
The root classification in Section3 shows they are totally real, with two conjugates in(-2,2) and the third above2.
At such an inner real conjugate v^2-4 is negative, so it cannot be a square in the totally real trace field.
Adjoining a root of t^2-vt+1 therefore doubles the degree.
Both COMPLETE determinants in(12) are irreducible sextics, with no neutral multiplier at this index.
Their literal proper cover is the full degree12 product P_3 A_3.
Rank6/6/12, height2 and energy9/9/18 are actual matrix costs.
This realizes different complete sextics; it does not contradict the earlier exclusions of the specifically prescribed Phi6 P4 or S6 targets.

<a id="weighted-cycle-finite-verification-declaration"></a>
### 6. Declared finite verification, before execution

A responsible J is requested for exactly six controls a=3,4,5,6,7,8, with the matrices(1) fixed before execution.
The declared aggregate author runtime cap is120 seconds, with no search, parameter optimization or expansion of the domain.
Each control must retain B_a,D_a,V_a,V_a^-, the literal proper cover, every full determinant coefficient, rank/height/energy and exact n+1 integer-pencil checks for each rank-n matrix.
Also check the all-a formal numerator identities(3),(8),(9), all endpoint signs in(5), the actual determinants(4), and the two cubic rational-root/trace identities(12)--(13).
Any failed assertion or cap will be retained.
Finite controls support the displayed all-a proofs and cannot establish them by extrapolation.
No run or independent review has yet occurred at the time this declaration is written.


<a id="weighted-cycle-execution-and-self-check"></a>
### 7. Actual verification, scope, self-check and author freeze

The responsible [J74](../computations/programs/Yin_J_G0074/readme.md) was normally allocated by root, and its exact six matrices, sign conventions, proper-cover rule, full polynomial/pencil domain and120-second aggregate cap were recorded before execution.
The sole author run completed at2026-10-10T05:49 in0.2467733seconds, using Python3.12.14 and SymPy1.14.0.
It passed all18 complete original, absolute and literal-cover polynomial arrays and282 integer-pencil values at the requisite degree-plus-one points.
All saved Gram determinants, trace conversions, rank/height/energy fields, endpoint values, formal numerator/difference identities and first-index rational-root tests passed.
No failed assertion, cap, numerical root approximation, search or extension of the six-control domain occurred.
The only native author files are J74/readme.md, verify.py and result.json.

The author's characteristic-polynomial and literal-cover patterns reuse its J72 code; this is disclosed code reuse, not an independent implementation.
Integer pencils are checked by a direct exact Bareiss routine in the new program.
No previous JSON is an input.
The finite checks do not establish the all-a root count, monotonicity, degree bounds or uniform limits by extrapolation; those are the written arguments above.
No source-classification or external theorem review is claimed by execution.

The author self-checked the complete matching/full-cycle permutation sum with the heavy-edge square and bipartition ascent count; exact B/D determinants and actual unit diagonal; the quadratic-form codimension-one bound and its count WITH multiplicity; all root-sign inequalities, positive/contracting pairs and every remaining circle root; monotonicity signs and limit without a logarithmic-integral interchange; the irreducible unit-factor and reciprocal argument; coefficient finiteness and the stronger nonzero integer evaluation at4, including constants13,16,52,64 and the denominator3 log3; and the two actual irreducible sextics' rational candidates, trace-field embeddings and quadratic lifts.
It separately rechecked complete rank, height, energy, polynomial and Mahler costs of the literal cover.
No endpoint t=1 or t=-1 is silently removed, and t-1 in(3) is not a matrix multiplier.

The result provides bounded COMPLETE positive measure with linearly growing original positive irreducible degree and an explicitly asymptotic doubled cover cost, using a changed actual matrix at every index.
It is complementary to L291's fixed-core degree boundary and L242's lower-measure but more expensive-companion family.
It does not improve the known rank6 quartic presentation's original measure or its exact doubled cover cost.
It does not determine the cyclotomic multipliers at every index, give complete irreducibility for all a, realize arbitrary targets, prove optimal companion costs, or reach near-zero total measure.
The log4 limit remains a substantial positive input cost.
The G0001 contract remains active and unresolved, and none of the parallel routes is paused.

All new derivations and author code are by orbit_research for Yin.
Root supplied the broad question and normal J allocation, not any formula or proof step.
Final whole author freeze:2026-10-10T05:50.
Complete Sections1--7/(1)--(13), including(11a)--(11c), and the three J74 native files are held for separately organized complete noncontributor review.
The scoped material check is a separate structural validation, not that mathematical review.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0138_v1.md#weighted-cycle-complete-written-review), with its original inspected scope and relationship.





## Current assessment
[Selected decision](#decision-complete-current-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:24 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Actual plus-sign full determinant product, doubled rank/energy, no division of total cost. |
| dependency | [Ordered-cycle matching mechanism](Yin_C_G0437_v2.md#cycle-order-polynomial) | All matching/whole-cycle permutation terms and actual bipartition order; no unrelated energy-barrier scope imported. |
| dependency | [Full Gram interface](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Actual integer block determinant and all positive Gram roots. |
| dependency | [Complete monic-factor/root mechanism](Yin_C_G0488_v1.md#bounded-measure-interlaced-fixed-scope) | Full irreducible reciprocal/circle-factor reasoning at its actual unit scope; all new root/degree estimates proved locally. |
| support | [Full original J74 evidence](../computations/programs/Yin_J_G0074/readme.md) | Six finite exact full domains, actual declarations/runtime/native payloads and different-method review; no new execution. |
| support | [Original full proof/input](../ledger/Yin_L_G0295_v1.md#complete-retained-proof-and-review) | All Sections1--7/equations1--13 including11a--c, source/author/native/negative limits; old R138 inputs remain original L/J. |

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
| dependency | [Complete literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Actual plus-sign full determinant product, doubled rank/energy, no division of total cost. |
| dependency | [Ordered-cycle matching mechanism](Yin_C_G0437_v2.md#cycle-order-polynomial) | All matching/whole-cycle permutation terms and actual bipartition order; no unrelated energy-barrier scope imported. |
| dependency | [Full Gram interface](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Actual integer block determinant and all positive Gram roots. |
| dependency | [Complete monic-factor/root mechanism](Yin_C_G0488_v1.md#bounded-measure-interlaced-fixed-scope) | Full irreducible reciprocal/circle-factor reasoning at its actual unit scope; all new root/degree estimates proved locally. |
| support | [Full original J74 evidence](../computations/programs/Yin_J_G0074/readme.md) | Six finite exact full domains, actual declarations/runtime/native payloads and different-method review; no new execution. |
| support | [Original full proof/input](../ledger/Yin_L_G0295_v1.md#complete-retained-proof-and-review) | All Sections1--7/equations1--13 including11a--c, source/author/native/negative limits; old R138 inputs remain original L/J. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0750_v1.md#weighted-cycle-whole-self) | Entire Statement and complete Argument, actual accepted dependency interfaces and all original source/native/negative limits. |


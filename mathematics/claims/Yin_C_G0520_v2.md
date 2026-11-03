---
author: Yin
---

# Complete charged bipartite sextic stabilization and full parameter costs

This organizes the complete original2026-10-10 result from [L283](../ledger/Yin_L_G0283_v1.md#complete-retained-proof-and-review).
The original rank9 untested statement and later J104 result retain their distinct scopes and dates; the entire original argument/input/source/review history remains below, without present Task/E authority.
The [v1 summary](Yin_C_G0520_v1.md#statement) left the normalization's residual-vector referent implicit in one sentence.
This version states the original y=(0,u), z=(1,v) decomposition and squared norms explicitly; the original proof, theorem and finite evidence are unchanged.

## Statement

For every integral rectangular matrix B, transpose the bipartition when needed to write B in Z^(r by g), r>=g, and use the actual proper matrix V_B=[[I_r,-B],[0,I_g]].
Its complete original polynomial and absolute companion are

    p_B(t)=(t+1)^(r-g)det((t+1)^2 I_g-t B^T B),
    p_abs(t)=(t+1)^(r-g)det((t+1)^2 I_g-t |B|^T |B|).

The literal signed cover has proper size2(r+g) and FULL polynomial p_B p_abs.
Row/column signs and permutations preserve the required original and absolute characteristic data; arbitrary integral congruence is not such an invariance.
Every neutral factor, zero Gram eigenvalue and complete unnormalized logarithmic measure is retained.

Fix

    P4=t^4-t^3-t^2-t+1, beta4>1 its expanding Salem root,
    F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1,
    chi(s)=(s-3)(s^2-5s+3)=s^3-8s^2+18s-9.

For EVERY integer r-by3 B with char(B^T B)=chi, the Gram is, up to signed column permutation,

    A=[[1,0,1],[0,3,0],[1,0,4]].

This is an all-row-count analytic classification, without an entry or height bound.
After normalizing the norm-one column to e_1, write the other columns as y=(0,u), z=(1,v).
Their residual vectors satisfy ||u||^2=||v||^2=3 and u dot v=0, so each has three unit coordinates and their support intersection is0 or2.
Thus r>=5; at r=5 or6 the intersection is2, whereas intersection0 requires r>=7.
For intersection epsilon in{0,2}, the absolute Gram is

    A_epsilon=[[1,0,1],[0,3,epsilon],[1,epsilon,4]].

Its full reciprocal factor is F at epsilon=0 and

    H=t^6-2t^5-3t^4-5t^3-3t^2-2t+1
      =t^3[(t+t^-1)^3-2(t+t^-1)^2-6(t+t^-1)-1]

at epsilon=2.
The trace cubic has exactly one root in each of(-2,-1),(-1,0),(3,4).
Hence H has whole logarithmic measure log alpha, where alpha>(3+sqrt5)/2>2>beta4.
All three-column original/absolute/cover polynomials are Phi2^(r-3)F, Phi2^(r-3)F or Phi2^(r-3)H, and their COMPLETE product.
Original and companion sizes are r+3, cover size2r+6, heights1, energies8/8/16.
Zero rows and their padding remain charged.

The actual5-by3 B5 has rows

    (1,0,1),(0,1,1),(0,-1,1),(0,0,1),(0,1,0).

It realizes Phi2^2 F in proper size8 with absolute Phi2^2 H, and cover Phi2^4 FH in size16.
The actual7-by3 B7 has one row(1,0,1), three rows(0,1,0) and three rows(0,0,1).
It realizes original=absolute=Phi2^4 F in size10 and the full Phi2^8 F^2 cover in size20, of measure2log beta4.
This is the first doubled-cost control within the classified three-column class, not a minimum proof across every bipartition for that cost objective.

The complementary4-by4 target has FULL Gram characteristic array[0,-9,18,-8,1] in ascending order.
Trace8 forces EXACTLY eight units, one double and four units, or two doubles in the16 positions.
The complete J67 finite certificate covers all12870 eight-unit supports/35256 forest-sign representatives and all21840 one-double supports/24000 representatives; all120 two-double supports are excluded by rank.
The e2=18 counts are4752 and576, with no full target.
All cycle-sign histogram entries and empty-target fields remain in the native record.
Every support, including disconnected ones, admits the proved spanning-forest sign normalization; no permutation quotient is assumed.
The original separate checker uses the larger row-first domains237216 and60480, with its full intermediate counts, squared-minor coefficients and complete Newton reconstruction retained.
All actual B5/B7 Grams, proper/absolute/cover matrices and full coefficient arrays are retained, including all78 author Bareiss evaluation nodes.
These are original executed finite facts at their recorded caps and times, not new runs.

For ANY integral rectangular bipartite realization of Phi2^k F, integer k>=0, necessarily

    rank B=3, r+g=6+k, r>=g>=3,
    char(B^T B)=s^(g-3)chi(s).

Combining the all-row analytic classification with the complete4-by4 certificate proves that the LEAST proper size in this ENTIRE bipartite class is8, k=2.
Every size8 realization has full absolute factor Phi2^2 H and cover Phi2^4 FH, of measure log beta4+log alpha>2log beta4.
This result excludes neither arbitrary non-bipartite size7 nor the untested(5,4) size9 partition.
The smaller target Phi2^2 P4 has its separate existing size6/energy5/height1 comparison and is not the complete sextic target F.

For EVERY ODD INTEGER h>=3 and EVEN INTEGER c with0<=c<=h-1, the explicit height-one B_(h,c) has one row(1,0,1), c/2 rows of each(0,1,1),(0,-1,1), and h-c rows of each(0,1,0),(0,0,1).
Put r=2h-c+1 and y=t+t^-1.
Its exact Grams and polynomials are

    A_(h,0)=[[1,0,1],[0,h,0],[1,0,h+1]],
    A_(h,c)=[[1,0,1],[0,h,c],[1,c,h+1]],
    Q_h=t^2+(2-h)t+1,
    P_(h+1)=t^4+(2-h)(t^3+t^2+t)+1,
    F_h=Q_h P_(h+1),
    chi_(h,c)(s)=(s-h)[(s-1)(s-h-1)-1]-c^2(s-1),
    H_(h,c)=t^3 chi_(h,c)(y+2),
    p_original=Phi2^(r-3) F_h,
    p_absolute=Phi2^(r-3) H_(h,c),
    p_cover=Phi2^(2r-6) F_h H_(h,c).

The two Grams are positive definite, of determinants h^2 and h^2-c^2.
Proper/absolute size is r+3=2h-c+4, cover size2r+6; all heights1, original/absolute energies2h+2 and cover energy4h+4.
With f(lambda)=0 on[0,4] and f(lambda)=arcosh((lambda-2)/2) for lambda>4, each FULL measure is the sum of f over ALL eigenvalues of its Gram, counted with multiplicity, and cover measure is their sum.
No Perron-only replacement or general measure monotonicity is asserted.
At c=0 the full factors coincide; h=3,c=2 or0 recovers B5/B7 up to row permutation.
The minimal row count is only for this normalized HEIGHT-ONE constructor at its specified support intersection, not all integer Gram factorizations when h>=5.
For h>=5 the positive factors retain degrees2 and4 and growing measure.
There is no bounded-measure/increasing-positive-irreducible-degree family, near-one coverage, arbitrary-form exclusion, unrestricted gap or Task completion.
Every original source/reuse, contribution, operational-error, finite execution and negative boundary is part of the complete fixed scope.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:50 |
| status | open |
| reason | Register the exact complete restricted theorem with the original residual coordinates/squared norms explicit in the summary; preserve the v1 precision preimage and entire unchanged original argument, with actual whole inspection/adoption still separate and no later rank9 result imported. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire integral rectangular bipartite class/full sextic and paid Phi2 targets; all-row three-column classification, full4-by4 certificate, least proper size8/compulsory full cost, precise size10 three-column control, every integer h/c parameter, full factors/ranks/energies/measures and all exclusions. |
| argument | [Exact argument](#argument) | Entire original Sections1--6/equations1--14 and assigned question, all analytic cases and determinant values, exact finite-domain coverage, complete native interfaces/run facts, variable support construction, full source/reuse/contribution/author check and negative limits. |
| dependency | [Exact dependency](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Full rectangular integral block determinant, zero Gram eigenvalues, every neutral factor, original/absolute eigenvalue measures and full literal-cover sum. |
| dependency | [Exact dependency](Yin_C_G0458_v2.md#irreducible-quartic-gram-family) | Exact P4/beta4 trace domain and irreducible quartic family; the size6 Phi2^2 P4 control has a different scalar target. |
| dependency | [Exact dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Literal vertex-then-sheet integral cover, both full factors, doubled proper size and full unnormalized Mahler cost. |
| support | [Exact support](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-construction) | Only the existing actual signed Gram/block conventions and sign-invariance reuse; no Walsh-family lower or ordering theorem is imported. |
| support | [Exact support](../ledger/Yin_L_G0246_v1.md#quartic-bipartite-neutral-padding-boundary) | Prior exact rank6 bipartite exclusion and separate smaller-target quartic neutral-padding comparison. |
| support | [Exact support](Yin_C_G0510_v1.md#universal-rank-six-coefficient-congruence) | Prior universal proper size6 coefficient obstruction at the exact full sextic; it does not exclude larger paid targets. |
| support | [Exact support](../computations/programs/Yin_J_G0067/readme.md) | Entire predeclared4-by4 energy-eight certificate, all-row analytic interface and complete B5/B7 controls, caps/methods/original execution facts. |
| support | [Exact support](../computations/programs/Yin_J_G0067/main.py) | Entire original author finite-domain/forest-sign/principal-minor/Bareiss implementation; static inspection only in this construction. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0067/readme.md#recorded-runs) | Complete original stages/histograms/zero targets/all B5/B7 matrices, Grams and full original/absolute/cover coefficient arrays. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0067/result.json`; this target locates its run account. |
| support | [Exact support](../computations/programs/Yin_J_G0067/review_independent.py) | Original distinct row-first sign/squared-minor/triangular-inverse-Newton checker; static inspection, with no new execution. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0067/readme.md#recorded-runs) | Complete saved independent finite-domain/control verification, larger-domain counts, cap, original timing and no-failure limits. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0067/review_result.json`; this target locates its run account. |


### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:53 |
| status | proved |
| reason | Adopt the entire exact charged bipartite theorem and unchanged14-equation proof after actual whole-v2 inspection and its explicit current SELF finding; preserve the v1 summary preimage, original author SELF, R136 known independent target scope and every original finite/native/source limit without importing later J104 rank9 results. No research Task/E, source acquisition or mathematical program is executed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire integral rectangular bipartite class/full sextic and paid Phi2 targets; all-row three-column classification, full4-by4 certificate, least proper size8/compulsory full cost, precise size10 three-column control, every integer h/c parameter, full factors/ranks/energies/measures and all exclusions. |
| argument | [Exact argument](#argument) | Entire original Sections1--6/equations1--14 and assigned question, all analytic cases and determinant values, exact finite-domain coverage, complete native interfaces/run facts, variable support construction, full source/reuse/contribution/author check and negative limits. |
| dependency | [Exact dependency](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Full rectangular integral block determinant, zero Gram eigenvalues, every neutral factor, original/absolute eigenvalue measures and full literal-cover sum. |
| dependency | [Exact dependency](Yin_C_G0458_v2.md#irreducible-quartic-gram-family) | Exact P4/beta4 trace domain and irreducible quartic family; the size6 Phi2^2 P4 control has a different scalar target. |
| dependency | [Exact dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Literal vertex-then-sheet integral cover, both full factors, doubled proper size and full unnormalized Mahler cost. |
| support | [Exact support](Yin_C_G0573_v1.md#walsh-companion-ratio-construction) | Only the existing actual signed Gram/block conventions and sign-invariance reuse; no Walsh-family lower or ordering theorem is imported. |
| support | [Exact support](Yin_C_G0573_v1.md#quartic-bipartite-neutral-padding-boundary) | Prior exact rank6 bipartite exclusion and separate smaller-target quartic neutral-padding comparison. |
| support | [Exact support](Yin_C_G0510_v1.md#universal-rank-six-coefficient-congruence) | Prior universal proper size6 coefficient obstruction at the exact full sextic; it does not exclude larger paid targets. |
| support | [Exact support](../computations/programs/Yin_J_G0067/readme.md) | Entire predeclared4-by4 energy-eight certificate, all-row analytic interface and complete B5/B7 controls, caps/methods/original execution facts. |
| support | [Exact support](../computations/programs/Yin_J_G0067/main.py) | Entire original author finite-domain/forest-sign/principal-minor/Bareiss implementation; static inspection only in this construction. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0067/readme.md#recorded-runs) | Complete original stages/histograms/zero targets/all B5/B7 matrices, Grams and full original/absolute/cover coefficient arrays. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0067/result.json`; this target locates its run account. |
| support | [Exact support](../computations/programs/Yin_J_G0067/review_independent.py) | Original distinct row-first sign/squared-minor/triangular-inverse-Newton checker; static inspection, with no new execution. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0067/readme.md#recorded-runs) | Complete saved independent finite-domain/control verification, larger-domain counts, cap, original timing and no-failure limits. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0067/review_result.json`; this target locates its run account. |
| review | [Exact review](../audits/reviews/Yin_R_G0728_v1.md#current-paid-stabilization-whole-self-finding) | ENTIRE actual current Statement and complete unchanged original Argument, every input/interface/source/native/cost/negative boundary; this actual maintaining whole finding is SELF, not isolated independent replacement. |

## Complete original argument

<a id="argument"></a>

## Changed full scalar targets beyond the universal sextic congruence obstruction

Date:2026-10-10.
G0001 and all eight mathematical strategies remain active and unresolved.

Current status: complete author proof and executed finite certificate, pending separately assigned full noncontributor review.
The adopted target is genuinely changed by paid Phi2 padding.
The resulting minimum-rank/cost conclusion is restricted to the entire rectangular bipartite class; no all-proper rank7 exclusion is asserted.

### Assigned question and scope

Go beyond L279 by changing the complete paid target or rank.
Seek a structural congruence criterion in arbitrary even rank, a justified cyclotomic stabilization or a genuinely changed integral realization.
Preserve actual characteristic polynomial, complete absolute companion, literal cover and every leading/neutral factor cost.
Do not repeat basis searches for either excluded rank-six target.

Develop substantive mathematics directly in this responsible draft.
Read exact local premises and perform the knowledge-reuse/source check before sustained proof investment.
Programs belong in a responsible J with a declared domain, cost cap and complete outputs before execution; preserve actual failures and costs.
A conjecture or finite diagnostic is not an unrestricted theorem.
No result, independent review or adoption is asserted at creation.
The root coordinator supplied this broad question, not a derivation.

<a id="paid-stabilization-reuse"></a>
### 1. Reuse and the changed complete target

The [L279 coefficient theorem](../ledger/Yin_L_G0279_v1.md#universal-sextic-congruence-fixed-scope) excludes the exact full sextic F=Phi6 P4 in proper rank6, across all integral forms.
The [L246 rectangular calculation](../ledger/Yin_L_G0246_v1.md#quartic-bipartite-neutral-padding-boundary) has the narrower rank6 Gram obstruction; the [L191 block identity and construction](../ledger/Yin_L_G0191_v1.md#higher-degree-phi2-realization) provide proper realizations and exact absolute costs after actual Phi2 padding.
The full signed-cover identity is reused from [D9](Yin_C_G0002_v1.md#signed-cover-identity).
The elementary row/column sign invariance also specializes the previously reviewed sign condition in [L234](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope).
These inputs already cover the matrix determinant, sign normalization and cover mechanisms needed here.
This round changes the COMPLETE target to Phi2^k F and classifies a concrete integral factorization cost; it does not search another forbidden rank6 basis or remove Phi6 from the polynomial.

For an integral r-by-g matrix B, r>=g, put V_B=[[I_r,-B],[0,I_g]].
The retained exact identity gives

    p_B(t)=(t+1)^(r-g) det((t+1)^2 I_g-t B^T B).       (1)

Its absolute companion uses |B| in the same formula, and its proper rank2(r+g) signed cover has their FULL product.
Every original and companion matrix is integral with diagonal1.
Independent sign changes of rows or columns conjugate the Gram by diagonal signs and leave its characteristic polynomial unchanged; they do not change |B|.
Row/column permutations have the same two invariances.
These are direct substitutions in(1), not a claim about arbitrary integral congruences preserving absolute costs.

The earlier fixed degree-six target is

    F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1,
    P4=t^4-t^3-t^2-t+1,
    chi(s)=(s-3)(s^2-5s+3)=s^3-8s^2+18s-9.          (2)

Thus for g=3 the entire target Phi2^(r-3) F is equivalent to chi_(B^T B)=chi.
The squared-entry sum of B is exactly8.
This finite energy follows from the full coefficient identity and is not a heuristic coefficient box or a proxy for Mahler measure.
No new external theorem is used for the elementary factor and support arguments below.

<a id="three-column-complete-gram-classification"></a>
### 2. All integer three-column factors and their complete expenses

For ANY integer B with three columns and chi_(B^T B)=chi, all three column squared norms are positive.
Sort them x<=y<=z.
Their sum is8, their pairwise-product sum minus the three squared inner products is18, and the Gram determinant is9.
The complete positive partitions are(1,1,6),(1,2,5),(1,3,4),(2,2,4),(2,3,3).

The first two have pairwise sum below18.
For(1,3,4), the squared-inner-product sum is1, so exactly one pair has inner product+/-1.
Coupling the pairs of norms(1,3),(1,4),(3,4) gives Gram determinants8,9,11 respectively.
Only the middle choice is possible.
For(2,2,4), the square sum is2, so exactly two pairs have inner products+/-1 and the third is0; the determinants are10 or12.
For(2,3,3), all three inner products have magnitude1, giving determinant8 or12.
Consequently, up to signed column permutation, the UNIQUE Gram matrix is

    A=[[1,0,1],[0,3,0],[1,0,4]].                    (3)

This is an all-row-count classification, with no coordinate bound.
An integral column of norm1 is a signed coordinate vector.
Normalize it to e_1 by row signs/permutation.
The other columns then have the form y=(0,u), z=(1,v), where

    ||u||^2=||v||^2=3, u.v=0.                     (4)

Every integral norm3 vector has exactly three nonzero coordinates, each+/-1.
Their support intersection has even size because its signed unit sum is0.
Hence it is either0 or2; if2, one common product is+1 and the other-1.
This proves r>=5.
Conversely r=5 is achieved by

    B_5=[[1,0,1],[0,1,1],[0,-1,1],[0,0,1],[0,1,0]]. (5)

It has Gram(3), rank3, height1 and squared-entry sum8.
V_(B5) is an actual rank8 positive upper-unitriangular realization of the complete Phi2^2 Phi6 P4.
This is a paid stabilization of F; it does not improve the already achieved rank6 Phi2^2 P4 construction for the smaller full polynomial.

For every B in this classified three-column family the absolute Gram is exactly

    A_h=[[1,0,1],[0,3,h],[1,h,4]], h in{0,2}.       (6)

There is no other absolute polynomial in this family.
Indeed h=|u|.|v| is precisely the intersection size.
The case h=0 needs six remaining row coordinates and therefore r>=7; it is achieved by taking u and v on disjoint supports of size3.
If r=5 or6 then necessarily h=2.
Extra zero rows can be added at either type without changing the Gram.

At h=0 the original and absolute full polynomials coincide.
At h=2 the complete absolute factor is

    H(t)=t^6-2t^5-3t^4-5t^3-3t^2-2t+1
        =t^3[(t+t^-1)^3-2(t+t^-1)^2-6(t+t^-1)-1]. (7)

To verify this, chi_(A_h)=s^3-8s^2+(18-h^2)s-(9-h^2); substitute s=t+t^-1+2 and multiply by t^3.
Thus every original, absolute and cover polynomial is respectively

    Phi2^(r-3) F,
    Phi2^(r-3) F or Phi2^(r-3) H,
    Phi2^(2r-6) F^2 or Phi2^(2r-6) F H.           (8)

The proper matrix rank is r+3, the cover rank2r+6, height1, original and absolute strict-upper energy8, cover strict-upper energy16.
The original logarithmic measure is log beta4.
The cubic in(7) has roots in(-2,-1),(-1,0),(3,4), since its values at-2,-1,0,3,4 are-5,2,-1,-10,7.
Therefore H has exactly one expanding reciprocal pair, with expanding root alpha>(3+sqrt5)/2>2>beta4.
Its entire measure is log alpha.
Every r=5 or6 factor has full cover measure log beta4+log alpha>2log beta4; h=0 at r>=7 gives exactly2log beta4.
No scalar or neutral factor is removed.
This is a complete dimension/cost tradeoff WITHIN the three-column factor class, not a general optimality theorem.

<a id="four-by-four-paid-test-declaration"></a>
### 3. Declared complementary rank-eight test

The other bipartite partition at total rank8 is r=g=4.
The complete target Phi2^2 F requires a rank3 Gram with characteristic polynomial s chi(s), hence again squared-entry sum8.
This singular four-column architecture is outside Section2 and can in principle change its cost conclusion.
Testing it has a coefficient-forced finite domain: all integral4-by4 B with sum B_ij^2=8, modulo independent row/column sign changes ONLY.
No row/column permutation quotient is required for completeness.

The complete squared-entry partitions are eight entries of magnitude1; one entry of magnitude2 and four of magnitude1; or two entries of magnitude2.
There are no larger magnitudes.
The last type has rank at most2 and cannot satisfy the target, but will be explicitly counted as a rejected type.
For each of the first two support/weight patterns form its bipartite graph on four row and four column vertices.
A deterministic spanning forest permits independent vertex signs to make every forest-edge sign positive: choose one root sign per component and propagate along the forest.
This normalization preserves both characteristic polynomials as stated after(1).
The remaining edge signs range independently over all possibilities.
Every full sign assignment is represented, including disconnected supports and isolated vertices.
The reduction is justified by elementary tree propagation, not an unproved sign-classification assertion.

Before any program execution, [J67](../computations/programs/Yin_J_G0067/readme.md) is assigned the ENTIRE support/weight domain just stated, all normalized cycle-edge signs, exact Gram coefficients, all successful candidates and the distribution of their complete absolute factors.
The aggregate runtime cap for the author discovery and exact control calculations is120 seconds.
A cap exit is incomplete and cannot prove absence or exhaust a cost class.
The program will also verify the explicit B5, its disjoint-support B7 control, all original/absolute/proper-cover polynomials and costs; any target or scope failure is retained.
There is no larger entry bound, higher rank enumeration, pivot search or follow-on scan in this declaration.
The deterministic sign quotient must be supported by the written argument rather than treated as all-bases exhaustion.
Results and the final theorem boundary will be added only after actual execution.

<a id="minimum-bipartite-padding-cost"></a>
### 4. Complete finite certificate and the precise minimum-rank theorem

The native J67 run (`mathematics/computations/outputs/Yin_J_G0067/result.json`) completed in0.735 seconds, below the declared aggregate120-second cap, with no failed assertion, repair, partial publication or cap exit.
It enumerated all12870 eight-unit supports with35256 forest-normalized sign representatives and all21840 one-double/four-unit supports with24000 sign representatives.
Their second Gram coefficient e2 equals18 in4752 and576 cases respectively.
None has the complete Gram characteristic polynomial s chi(s).
The120 two-double supports are separately counted and impossible by rank at most2.
The complete cycle-sign histogram, every stage count and empty successful-matrix list are retained, rather than a count asserted from a sample.

Here is why the finite certificate settles the ENTIRE stated integer class.
Trace8 bounds every magnitude by2 and permits exactly the three square partitions already listed.
The combinations loops visit each weighted support once, distinguishing the location of a double.
For every support, the union-find construction takes an edge into its forest exactly when it joins distinct components; all remaining edges are precisely its free sign coordinates.
Root-sign propagation normalizes any original sign assignment on that forest, so enumerating every chord sign covers all original signed matrices, including disconnected and degenerate cases.
The invariance after(1) means no lost sign assignment could have a different original or absolute polynomial.
There are no necessary-only cycle or eigenvalue prefilters.
The principal-minor identity gives each complete Gram characteristic coefficient over Z.
The e2 filter discards only a coefficient mismatch; every remaining candidate is compared with the entire array(0,-9,18,-8,1), in ascending order.
Thus zero targets is a complete exact certificate for all4-by4 integer B of the required full polynomial.
It is not a statement about all integer bases or all non-bipartite matrices.

**Theorem.**
Within the entire rectangular bipartite class V_B in(1), the least rank realizing Phi2^k F for some k>=0 is8, with k=2.
EVERY such rank8 presentation has original and absolute full polynomials Phi2^2 F and Phi2^2 H, respectively.
Its complete proper rank16 cover is Phi2^4 F H and has measure log beta4+log alpha>2log beta4.
These conclusions allow arbitrary integer B entries and either bipartition size; they do not claim a minimum among non-bipartite presentations.

To prove the dimension assertion, the equality of the FULL determinant in(1) with Phi2^k F requires rank B=3 and

    chi_(B^T B)(s)=s^(g-3) chi(s),
    r+g=6+k, r>=g>=3.                           (9)

Indeed the three nonzero eigenvalues are exactly3,(5+sqrt13)/2,(5-sqrt13)/2; every zero Gram eigenvalue contributes two additional Phi2 factors, and F(-1)=9 is nonzero.
The block sizes may be interchanged by transposing B without changing either full polynomial, so taking r>=g loses no case.
Rank at most7 forces g=3 and r<=4, excluded analytically by Section2.
At rank8 the choices are(5,3) or(4,4); Section2 gives the actual former construction and its UNIQUE full companion, while the complete finite certificate excludes the latter.
This proves the theorem, including the precise full factors and the absence of an untested fourth-column exception at that rank.

The explicit disjoint-support control is

    B7=[[1,0,1],[0,1,0],[0,1,0],[0,1,0],
        [0,0,1],[0,0,1],[0,0,1]].                 (10)

It gives proper rank10, full Phi2^4 F, identical absolute polynomial, and proper rank20 cover Phi2^8 F^2.
Its complete logarithmic cover measure is2log beta4.
Both B5 and B7 have height1 and strict-upper energy8; their covers have height1 and energy16.
Thus energy alone does not distinguish the two actual full Mahler costs.
Every actual integer matrix, complete original/absolute/cover coefficient array and rank/height/energy is retained in J67.
The program also checks each full pencil at degree-plus-one distinct integer points by exact Bareiss elimination: the rank8 original, rank8 companion and rank16 cover use9,9,17 points respectively; the rank10 original, rank10 companion and rank20 cover use11,11,21.
In total these are78 exact pencil evaluations.
The sheet decomposition proves the full factor identity separately; the point counts are ordinary polynomial verification, not a numerical root test.

The rank10 control is the FIRST doubled-measure construction in the three-column class, because h=0 forces r>=7.
It is not established minimal among all bipartite partitions: rank9 permits(5,4), not inspected by this finite test.
Likewise the theorem does not decide a non-bipartite rank7 realization of Phi2 F.
The existing L191 rank6 Phi2^2 P4 still attains2log beta4 for a different, smaller COMPLETE target.
This round is an exact dimension/cost result for the retained Phi6 factor, not a claim to improve that benchmark or solve unrestricted neutral completion.

<a id="support-overlap-stabilization-family"></a>
### 5. Extracting an explicit variable-parameter mechanism

The support argument gives an actual family beyond one finite matrix.
Let h>=3 be odd, and let c be even with0<=c<=h-1.
Construct B_(h,c) from one row(1,0,1), c/2 rows(0,1,1), c/2 rows(0,-1,1), h-c rows(0,1,0), and h-c rows(0,0,1).
It has

    r=2h-c+1, rank V=r+3=2h-c+4,
    B^T B=[[1,0,1],[0,h,0],[1,0,h+1]],
    |B|^T |B|=[[1,0,1],[0,h,c],[1,c,h+1]].        (11)

Every entry and every diagonal of V is explicit on the standard integer lattice.
Put y=t+t^-1 and define

    Q_h=t^2+(2-h)t+1,
    P_(h+1)=t^4+(2-h)(t^3+t^2+t)+1,
    F_h=Q_h P_(h+1),
    chi_(h,c)(s)=(s-h)[(s-1)(s-h-1)-1]-c^2(s-1),
    H_(h,c)(t)=t^3 chi_(h,c)(y+2).              (12)

The full original, companion and proper cover polynomials are exactly

    Phi2^(r-3) F_h,
    Phi2^(r-3) H_(h,c),
    Phi2^(2r-6) F_h H_(h,c).                    (13)

These follow by the explicit row products and(1).
No factor is inferred from a desired spectrum without an integer matrix.
Original and companion ranks are r+3, cover rank2r+6, all heights1, original/companion strict-upper energy2h+2, and cover energy4h+4.
Both Gram matrices are positive definite: the original determinant is h^2, and the absolute determinant h^2-c^2 is positive; they are also displayed Gram products.
The entire measure can therefore be read using the accepted exact L191 function f(lambda)=0 for0<=lambda<=4 and arcosh((lambda-2)/2) for lambda>4:

    m_original=sum_(lambda in spec A_(h,0)) f(lambda),
    m_absolute=sum_(lambda in spec A_(h,c)) f(lambda),
    m_cover=m_original+m_absolute.               (14)

Eigenvalues here are counted with full multiplicity.
This is an exact spectral cost formula for a completely specified cubic, not just its Perron root or a rank-normalized measure.
For c=0 both full factors coincide, giving2m_original.
For h=3,c=2 and0 the construction recovers B5/B7 (up to row permutation), H and F.
As c grows in steps of2 the required row count falls, and sign cancellation changes the absolute cubic by the explicit term-c^2(s-1).
No monotonicity of full measure for arbitrary h,c is asserted from this identity.

Within the normalized HEIGHT-ONE support constructor, the row count2h-c+1 is minimal for that specified intersection c: two supports of size h and intersection c have union2h-c, plus the norm-one coordinate.
This is not an all-integer Gram-factor theorem for h>=5, where norm-h vectors may contain entries of magnitude2.
Nor is it a bounded-original-measure or increasing-positive-irreducible-degree family.
At h=3 Q_h=Phi6; for h>=5 Q_h has an expanding reciprocal pair and the fixed L191 irreducible quartic P_(h+1) has growing measure.
Their degrees remain2 and4 while the total neutral padding grows.
The support mechanism is reusable, but those limitations prevent a near-one or unrestricted coverage inference.

<a id="paid-stabilization-author-check"></a>
### 6. Complete self-check, contribution and handoff scope

The author checked the full reciprocal-to-Gram conversion, including zero Gram eigenvalues, the complete positive partitions of8 and every possible determinant in Section2, sign normalization and support-overlap parity, all actual B5/B7 entries and costs, every finite support/sign orbit and rejection condition, the all-partition minimum-rank proof, and the variable-parameter construction with every neutral and absolute factor.
J67 uses Python3.12.14 standard-library integer arithmetic only; timings are operational floats, no mathematical comparison is floating point.
The complete principal-minor coefficients and degree-plus-one full-pencil checks are exact.
The program and declared finite domain are author evidence, not independent verification; separate noncontributor review with its own checking method remains required.

The coordinator supplied the broad changed-target question, J allocation and common allowance, not these arguments.
Orbit_research AI for Yin derived the complete three-column Gram classification, its absolute-factor/dimension consequence, the changed4-by4 finite certificate and its completeness proof, the minimum bipartite-rank theorem, and the support-overlap family.
Fixed block/cover identities, the quartic family, spectral measure formula and sign invariance are reused at the precise L191/D9/L234 scopes; no external theorem, new source intake or novelty claim is added.
No author mathematical failure or cap occurred.
A local operational rg invocation initially used a PowerShell option in the wrong command position and was immediately corrected; that search error had no mathematical output or effect on the declared computation.

This bounded round stops at the displayed classification and constructive controls.
It does not run a larger rank or another basis search.
The genuine remaining discriminators include non-bipartite Phi2 F at rank7, a changed partition at rank9, other charged neutral targets, and varying-input constructions with bounded positive full measure and growing irreducible complexity.
None is a prerequisite for keeping the route active, and no untested one is asserted successful.
All strategies and G0001 remain active and unresolved.
Full author freeze and separate review will be recorded after the final scope check.

Final author freeze:2026-10-10T04:16.
All Sections1--6, equations(1)--(14), the exact finite reduction and complete parameter/cost boundaries are held for review.
Native J67 author scope is readme.md, main.py and result.json.
The coordinator's reviewer-only names review_independent.py and review_result.json remain reserved.
No further discovery follows this freeze.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0136_v1.md#minimum-rank-and-the-full-parameter-family), with its original inspected scope and relationship.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0067](../computations/programs/Yin_J_G0067/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.

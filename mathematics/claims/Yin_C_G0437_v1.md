---
author: Yin
---

# Complete ordered signed-cycle surgery, integral obstruction and attachment barriers

The entire necessary original D21 proof is retained from [L184](../ledger/Yin_L_G0184_v1.md#retained-cycle-proof).
The structural author supplied the cycle determinant, lattice, sweep and barrier derivations.
Its briefly delegated same-candidate discovery and the coordinator's parallel absolute-cycle calculation remain exact contribution facts, not independent reviews.
The author had already written and checked that absolute-cycle lemma before the parallel calculation was communicated.
The two actual original [whole findings and listed author checks](../audits/reviews/Yin_R_G0083_v1.md#review-relationships) are self-reviewed at their precise arrangements.
The separate reviewer received the earlier written whole review and target cycle calculation before checking; its separately authored arithmetic implementation remains a separate fact.
Adequate J25/J31 homes retain the code, all executed finite domains, full outputs and original operational/reviewer-code failures.
No native rerun, source/PDF reading, new J, external classification or research Task/E execution is added.

## Statement

For an integral upper-unitriangular V define

    E(V)=sum_(i<j)V_ij^2,
    p_V(t)=det(tV+V^T),
    V^-=I-|V-I|.

The raw proper absolute-cover factor is p_(V^-), and its extra logarithmic Mahler cost is m(p_(V^-)).
The accepted original Stokes action consists of the adjacent integral congruences and diagonal sign gauges.
Switchable means a diagonal sign gauge makes every nonzero strict upper entry negative.

Suppose the strict upper support of V is exactly a simple n-cycle, n>=3, all supported entries are+/-1, and its edge-sign product is the frustrated value(-1)^(n-1).
Along either oriented cyclic traversal let k count increasing vertex-label edges,1<=k<=n-1.
Then

    p_V(t)=(t^k+1)(t^(n-k)+1),
    p_(V^-)(t)=(t^k-1)(t^(n-k)-1).

Reversing orientation replaces k by n-k.
Both full polynomials are cyclotomic products and have logarithmic measure zero.
The isolated cycle's raw absolute-cover extra cost is therefore zero even when an ordered-presentation obstruction holds.
No corresponding zero-cost assertion is made for attached cycles.

For every n>=4 and2<=k<=n-2, every integral upper-unitriangular W integrally congruent to this V has E(W)>=n and is not switchable.
This allows every integral unimodular congruence with such an endpoint and keeps its rank and integral form fixed.
The complete elementary proof identifies the even-coordinate-sum lattice, proves its orthogonal indecomposability by connected norm-two roots, and then uses positive principal minors, connected support and the tree polynomial's t^(n-1) coefficient.
For the explicit rank-four cycle order(0,2,1,3), p=(t^2+1)^2, no integral upper-unitriangular matrix of energy at most3 has that full polynomial, even without congruence.
All233 such inputs are covered, and a second elementary determinant-at+/-1 graph argument proves the same exclusion.
Neither result excludes stabilization, cyclotomic-factor removal or a different integral form.

For every integer m>=3, let A_m be upper unitriangular with successive path entries-1 except its last path entry+1 and no other strict entries.
Put it as a consecutive middle block of

    V=[[B_L,C,D],[0,A_m,R],[0,0,B_R]],

with arbitrary integral upper-unitriangular outside blocks and arbitrary integral coupling blocks; either outside dimension may be zero.
Let u_i concatenate column i of C and row i of R.
Apply forward adjacent moves(1,2),...,(m-2,m-1), then the inverse at(m-1,m), relative to the middle block.
For1<=j<=m-2 set s_j=sum_(i=1)^(j+1)u_i and s=sum_(i=1)^(m-1)u_i.
The exact basis, full polynomial and outside-block preservation are proved below, and

    Delta E_j=1+||s_j||^2-||u_1||^2,
    Delta E_final=2||s||^2-2<u_m,s>-||u_1||^2.

These include both earlier and later couplings.
For u_1=-e,u_2=...=u_(m-1)=0,u_m=-e+b with e a standard outside coordinate and<e,b>=0, every forward excess is1 and the final excess is-1.
This is an exact one-unit-barrier strict reduction for this stated ordered two-boundary attachment family in every length n=m+1.
The barrier is necessary and hence sharp when the whole input is a simple triangle-free signed graph, using its nonswitchability and the exact local rigidity theorem.
It is not asserted for every ordering or every attachment pattern.

With disjoint simple pendant attachments of cardinalities d_i at all swept vertices, in addition to the common closing coordinate, the same sweep instead gives

    Delta E_j=1+sum_(i=2)^(j+1)d_i,
    Delta E_final=-1+d_1+2sum_(i=2)^(m-1)d_i.

This can increase final energy and is a cost formula for this sweep, not an impossibility result for all other operations.

For every simple triangle-free signed graph whose every nonleaf vertex has degree at least r+2, any adjacent-mutation/sign path leaving its signed-graph class reaches energy at least E(V)+r+1.
Earlier zero-change steps preserve that symmetric signed-graph class, simplicity, triangle-freeness and degrees.
The first departing edge move costs degree(reflected endpoint)-1.
In particular, for every integer r>=0 and n>=4, attach r pendant leaves to each vertex of a frustrated simple n-cycle.
Every such path to a switchable presentation, if it exists, has necessary temporary excess at least r+1, in any vertex ordering.
This lower bound is unbounded with r.
It claims neither successful paths nor sharpness for r>0, and is restricted to adjacent/sign operations.
No arbitrary-congruence barrier, stabilization obstruction, near-one coverage, general representation theorem, optimized extra-cover cost or unrestricted gap follows.

## Current assessment

[Selected decision](#decision-retained-registration)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:56 |
| status | open |
| reason | Retain the complete ordered-cycle determinant, fixed-rank lattice obstruction, arbitrary-coupling all-length sweep and exact whole-input pendant first-escape barrier, separating isolated zero scalar cost from presentation/energy rigidity. Actual complete current self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire cycle and attachment theorem](#statement) | Entire original D21 mathematical Sections1--3: all n>=3/frustrated ascent1<=k<n/both ordered-cycle polynomials and zero isolated-cover cost, complete rank4/full-polynomial/E<=3 exclusion, all n>=4/2<=k<=n-2 fixed-rank arbitrary integral congruence/even-sum lattice/positive-definite support/tree-coefficient/no-switchable proofs, every m>=3 consecutive path block with arbitrary integral earlier/later blocks and couplings/full prefix-final basis and exact energies, exact two-boundary orthogonal-coupling one-unit upper bound with whole simple-triangle-free sharpness only, all disjoint-pendant sweep costs, whole simple-triangle-free signed-graph nonleaf-degree and every integer r>=0/n>=4 pendant-family first-escape lower bound for adjacent/sign paths, with every fixed-rank/no-stabilization/no-success/no-attached-zero-cost/no-small-measure limit and actual retained native/contribution boundaries. |
| argument | [All complete determinant/lattice/basis/barrier proofs](#argument) | Entire original D21 mathematical Sections1--3: all n>=3/frustrated ascent1<=k<n/both ordered-cycle polynomials and zero isolated-cover cost, complete rank4/full-polynomial/E<=3 exclusion, all n>=4/2<=k<=n-2 fixed-rank arbitrary integral congruence/even-sum lattice/positive-definite support/tree-coefficient/no-switchable proofs, every m>=3 consecutive path block with arbitrary integral earlier/later blocks and couplings/full prefix-final basis and exact energies, exact two-boundary orthogonal-coupling one-unit upper bound with whole simple-triangle-free sharpness only, all disjoint-pendant sweep costs, whole simple-triangle-free signed-graph nonleaf-degree and every integer r>=0/n>=4 pendant-family first-escape lower bound for adjacent/sign paths, with every fixed-rank/no-stabilization/no-success/no-attached-zero-cost/no-small-measure limit and actual retained native/contribution boundaries. |
| dependency | [Exact original integral Stokes action and proper cover](Yin_C_G0002_v1.md#mutation-and-energy) | Only original adjacent congruences, sign convention, full determinant preservation and proper absolute-cover factorization, at the retained FW24 direct-formula attribution depth. No orbit classification or general scalar realization is imported. |
| dependency | [Exact triangle-free local rigidity](Yin_C_G0003_v1.md#triangle-free-rigidity) | Exact degree(reflected endpoint)-1 energy change for nonzero adjacent edges in a simple triangle-free signed graph, zero-edge swaps and leaf-zero-change signed-graph permutation/gauge identification. Only the whole-input hypotheses give sharp one-unit/first-escape lower bounds; no capped search or arbitrary-congruence inference is used. |
| support | [Original exact author cycle and coupling controls](../computations/programs/Yin_J_G0025/readme.md#results) | Original consecutive n3--12/full233 rank4 matrices, five fully symbolic m3--7 with15--35 earlier/later couplings,76both-sign ordered cycles n3--6,233/32/0 direct+/-1 exclusion,9n4--12Gram/index and12n4--6/r0--3degree controls. Exact all-size proofs are local; the original SymPy-to-JSON serialization failure is not hidden or used as mathematics. |
| support | [Separately authored exact finite checker and author reruns](../computations/programs/Yin_J_G0031/readme.md#actual-results) | Original436orderings n3--7/both signs,233rank4 direct permutation determinant checks,119m3--16prefix-final/coupling matrices,249signed triangle-free rank4graphs/1494directed steps/1014zero permutation-gauge checks and two author reruns with all JSON mathematical fields equal. Initial ordered-bilinear comparison was a reviewer-code error corrected to the theorem's symmetric graph before the complete successful run. Separate code is not an isolated agent review and no current rerun occurs. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-cycle-proof"></a>
<a id="cycle-surgery-fixed-scope"></a>

<a id="cycle-order-polynomial"></a>
### 1. The polynomial remembers the cyclic ordering

Let V be upper unitriangular, with strict upper support exactly one simple n-cycle, n>=3, and all its nonzero entries equal to plus or minus one.
Traverse the cycle in either direction, and let k count the edges on which the vertex labels increase.
Thus 1<=k<=n-1; reversing direction replaces k by n-k.
Suppose the cycle is frustrated: its edge-sign product is (-1)^(n-1), opposite to the switchable product (-1)^n.
Then

    p_V(t)=det(tV+V^T)=(t^k+1)(t^(n-k)+1).

Here is a direct determinant proof.
The nonzero permutation terms, other than the two full cyclic permutations, consist of disjoint edge transpositions and fixed vertices.
Every transposition has weight -t, and every fixed vertex weight 1+t.
The corresponding sum for a path on r vertices satisfies F_r=(1+t)F_(r-1)-t F_(r-2), F_0=1,F_1=1+t, hence F_r=1+t+...+t^r.
Splitting the cycle matchings according to whether the closing edge occurs gives F_n-t F_(n-2)=1+t^n.
The two full-cycle terms have powers t^k and t^(n-k).
Their permutation sign (-1)^(n-1) cancels the frustrated edge-sign product, so both occur with positive sign.
Adding gives the stated factorization.
The n=3 terms obey the same matching/full-cycle separation.

Consequently cycle length alone does not determine p_V.
A vertex permutation that changes the induced ordering need not be an allowed upper-unitriangular congruence preserving p_V.
Conversely, all these isolated-cycle polynomials are cyclotomic products and have Mahler measure one.
Their ordering obstruction by itself says nothing about positive extra Mahler cost or an obstruction after factoring neutral factors or stabilizing the representation.

For a decisive small control, take the cycle order (0,2,1,3) with

    V=[[1,0,-1,-1],
       [0,1,-1,1],
       [0,0,1,0],
       [0,0,0,1]].

Here k=2 and p_V=(t^2+1)^2.
The exact program exhausts all 233 rank-four integral upper-unitriangular matrices with E<=3 and finds none with this polynomial.
Completeness is elementary: E<=3 forces every strict upper entry into {-1,0,1} and at most three of the six positions nonzero, giving sum_(j=0)^3 binomial(6,j)2^j=233.
Thus this specific V is a global minimum of E at fixed rank and complete polynomial, independently of how high an intermediate energy is permitted.
This is stronger than failure of a bounded mutation search, but remains exactly a rank-four/full-polynomial obstruction.

There is also a short check without enumeration.
At E<=3 the support is a graph with at most three edges on four vertices.
The possible determinants of V+V^T are16,12 for zero/one edge;9 or8 for two edges; and5 for a four-vertex path,4 for a three-edge star, or0/8 for a triangle and isolated vertex.
Signs do not affect a forest determinant.
The target has p_V(1)=4, forcing the star.
But its polynomial is (t+1)^4-3t(t+1)^2=(t+1)^2(t^2-t+1), whose value at -1 is zero rather than the target's four.
Thus no candidate can have the full target polynomial.

<a id="cycle-congruence-obstruction"></a>
#### General obstruction within the integral congruence class

For n>=4 and 2<=k<=n-2, no integral upper-unitriangular W integrally congruent to V can have E(W)<n, or be switchable.
This statement permits arbitrary integral unimodular congruences whose endpoint is upper unitriangular; it is stronger than a restriction to adjacent mutation paths, but keeps the rank and congruence class fixed.
The following elementary lattice argument proves it without a classification theorem.

After changing vertex signs and following the cyclic order, the symmetric form V+V^T is the Gram matrix of

    r_i=f_i-f_(i+1), i=1,...,n-1,
    r_n=f_n+f_1

in the ordinary Euclidean integer lattice.
The r_i generate exactly

    Lambda={a in Z^n: sum_i a_i is even}:

their sums are even; conversely subtracting (sum_i a_i)/2 times r_n leaves a zero-sum integer vector, which is a combination of the consecutive differences.
Thus the form is positive definite.
Every nonzero vector of Lambda has positive even squared norm, at least two.
Its squared-norm-two vectors are precisely plus or minus f_i plus or minus f_j, i!=j.
The graph on these vectors joining nonorthogonal pairs is connected for n>=3: a third coordinate connects orthogonal roots with the same support, and a root using one coordinate from each pair connects disjoint supports.
These roots span Lambda.

This lattice cannot split into two nonzero orthogonal integral summands.
Indeed a norm-two vector in such a decomposition belongs wholly to one summand, since two nonzero components would have squared norm at least four.
Connectivity under nonorthogonality puts all norm-two vectors in one summand; their spanning property leaves no other summand.

Now suppose W is an integral congruent upper-unitriangular presentation.
Positive definiteness of W+W^T forces every off-diagonal entry of W into {-1,0,1}, by its two-dimensional principal minors.
A disconnected support would split Lambda orthogonally in the W basis, which was just excluded.
Thus if E(W)<n, its connected support has exactly n-1 edges and is a tree.
For any signed tree the determinant expansion uses only fixed points and edge transpositions, so the coefficient of t^(n-1) in p_W is n-(n-1)=1.
But (t^k+1)(t^(n-k)+1) has that coefficient zero when both k and n-k exceed one.
Congruence preserves p, a contradiction.

Finally, if W were switchable, change signs to make every nonzero off-diagonal entry negative.
A cycle in its support contradicts positive definiteness: the vector equal to one on that cycle and zero elsewhere has squared form value at most2l-2l=0, where l is the cycle length and any chords only decrease the value.
Its connected support must therefore be a tree, giving the same contradiction.
This proves the stronger non-switchability conclusion throughout the integral congruence class.

No passage to a larger rank, removal of cyclotomic factors or change of the integral form is excluded by this argument.
In fact the all-negative absolute cycle has polynomial (t^k-1)(t^(n-k)-1), by the same determinant calculation with opposite full-cycle signs.
It too has Mahler measure one.
Thus this permanent obstruction to a switchable presentation has zero extra Mahler cost for the raw absolute cover in this isolated-cycle control; it is not a negative conclusion about the desired scalar gap transfer.

The coordinating AI independently communicated this same absolute-cycle calculation after it had already been written and checked here.
That parallel derivation did not author or alter the retained lemma; its timing is disclosed rather than presented as a premise supplied to the author.
Agreement alone is not an independent-review finding.

<a id="long-cycle-sweep"></a>
### 2. A sweep identity in every length and its attachment cost

Let m>=3 and let A_m be upper unitriangular with successive path entries -1 except for its last path entry (m-1,m), which is +1.
Its other strict upper entries are zero.
Place it as a consecutive principal block in

    V = [[B_L, C, D],
         [0,   A_m, R],
         [0,   0, B_R]],

where both outside diagonal blocks are arbitrary integral upper unitriangular, and all other displayed blocks are arbitrary integral matrices.
Empty outside blocks are permitted.
Package all outside couplings of vertex i in one integer vector u_i: concatenate column i of C and row i of R.
The Euclidean inner product on this direct sum exactly measures their combined contribution to E.

Apply forward adjacent mutations at (1,2),(2,3)...,(m-2,m-1), then the inverse mutation at (m-1,m), using indices relative to this block.
After the first j forward moves, 1<=j<=m-2, the basis is

    e_2,...,e_(j+1), h_j, e_(j+2)...,e_m,
    h_j=e_1+...+e_(j+1).

The last pair before the inverse move is h=e_1+...+e_(m-1),e_m and has entry +1.
The final basis is

    e_2,...,e_(m-1), e_m-h, h.

This explicitly describes a unimodular matrix P_m and proves that every step is one of the permitted adjacent congruences, hence the whole p_V is preserved.
The leading/trailing outside blocks and D are unchanged.

The internal energy is m-1 initially and finally, and m after each forward step.
This can be read directly from the basis above: the intermediate path has one additional triangle, and the inverse final step replaces that triangle by a two-edge fork.
Define s_j=u_1+...+u_(j+1) and s=u_1+...+u_(m-1).
The outside couplings undergo the same linear basis transformation, on C by right multiplication and on R by left-transpose multiplication.
Therefore the exact total energy changes from the initial matrix are

    after j forward moves:
        Delta E_j = 1+||s_j||^2-||u_1||^2,

    after the final inverse:
        Delta E_final = 2||s||^2-2<u_m,s>-||u_1||^2.

These formulas account for earlier-vertex couplings as well as later attachments; there is no tacit assumption that the path block starts at the first vertex.

In particular suppose u_1=-e, u_2=...=u_(m-1)=0 and u_m=-e+b, where e is a standard coordinate of the combined outside space and <e,b>=0.
Then the m block vertices and the distinguished outside vertex form a frustrated cycle of length n=m+1.
Every forward step has excess +1; the final excess is -1.
Thus every such cycle of arbitrary length admits an exact one-unit-barrier reduction preserving the full polynomial, with arbitrary outside matrices and arbitrary b subject only to the displayed orthogonality.
In the unicyclic simple-graph specialization this allows arbitrary attached trees at the two adjacent boundary cycle vertices, with the specified ordering and no attachments at the swept interior vertices.
When the whole input is a simple triangle-free signed graph, nonswitchability and C3's complete rigidity prove that the necessary barrier for strict energy reduction is exactly one.

Arbitrary attachments at all swept vertices cannot silently be included.
If each has disjoint simple pendant attachments of cardinalities d_i, in addition to the common closing coordinate, then the displayed formulas become

    Delta E_j = 1+sum_(i=2)^(j+1) d_i,
    Delta E_final = -1+d_1+2 sum_(i=2)^(m-1) d_i.

Thus the very same sweep can increase the final energy.
This is an exact coupling cost, not evidence that every different possible reduction must fail.

<a id="degree-barrier"></a>
### 3. Arbitrarily large necessary escape barriers from attachments

There is nevertheless an operation-invariant barrier before any new graph shape can be reached.
For a simple triangle-free signed graph, the first nonzero-energy adjacent mutation at an edge raises energy by the degree of its reflected endpoint minus one; a zero-change move preserves the signed graph up to vertex permutation and signs, as proved in C3.
Suppose every nonleaf vertex has degree at least r+2.
Along any path which has not yet changed that signed-graph class, a nonzero energy increase is therefore at least r+1.
Since all earlier nonincreasing steps have energy exactly E(V), every path that ever leaves the original signed-graph class must reach energy at least E(V)+r+1.

For an explicit family, attach exactly r>=0 pendant leaves to every vertex of a frustrated simple n-cycle, n>=4.
The cycle vertices have degree r+2 and the other vertices are leaves; the graph remains triangle-free and nonswitchable.
Any adjacent-mutation/sign path to a switchable presentation, if one exists, must have temporary energy excess at least r+1.
The lower bound is unbounded with r.
It applies to any ordering of the vertices and does not depend on a node cap, determinant approximation or external classification.

This does not assert the existence of a successful path, identify the sharp barrier for r>0, or give a lower bound under arbitrary integral congruences or stabilization.
In particular it does not contradict the one-unit theorem, whose internal vertices have no such pendant attachments.
It separates a genuine attachment obstruction from the finite-search outcomes of the previous round.

No small-positive-Mahler-measure bound or coverage theorem is proved for this pendant family.
Growing degree barriers in these controls cannot be transferred to the unresolved near-one class without additional arithmetic information.

## Exact retained native and contribution boundaries

All-size proofs above use the explicit determinant expansion, lattice basis, arbitrary-coupling basis calculation and degree argument.
Finite programs support their exact invoked domains and do not justify arbitrary size by extrapolation.
J25 owns both original exact author programs and every saved output field.
Its controls.py initial assertions passed before JSON serialization failed on a SymPy integer matrix; conversion to ordinary integers allowed the canonical successful rerun.
J31 owns its separately authored permutation determinant/basis/graph checker and the separate executions of both author programs with only output destinations redirected.
Every saved mathematical JSON field matches the corresponding J25 output.
Its initial zero-step comparison wrongly required ordered bilinear equality after graph permutation; the corrected comparison is the actual symmetric signed graph.
The complete checker then passed, with no author theorem or data altered to accommodate that reviewer-code error.
The original whole coordinator verifier rerun, later reviewer's own code and author reruns, and author executions are distinct events at their retained2026-10-10precision.
The current maintenance statically read all three entire programs and every saved mathematical field, without executing them.
All original prospective next tests and incomplete small-measure/optimized-cost directions remain fixed in L184, without selecting or resuming them here.
No source theorem beyond the accepted original action/rigidity interfaces, classification, new arithmetic family coverage or unrestricted gap is supplied.

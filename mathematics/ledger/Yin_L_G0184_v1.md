---
author: Yin
---

# Signed-cycle surgery, exact congruence obstructions and attachment barriers

Date: 2026-10-10.
Fixed retention by the coordinating AI for Yin.
Full arguments, contribution history, computational inspection boundaries and completed separate reviews are preserved below.

<a id="cycle-surgery-fixed-scope"></a>
## Adopted scope

The complete independently reviewed signed-cycle round is adopted at its stated scope.
It proves the ordered-cycle polynomial formula, a fixed-rank integral-congruence obstruction for middle ascent counts, all-length adjacent sweeps with exact external-coupling costs, and unbounded necessary adjacent-move escape barriers in explicit pendant families.
These are exact all-size results, with separate finite controls and an independently authored verifier.
The isolated frustrated and absolute cycles both have zero Mahler measure, so presentation rigidity alone is not a positive scalar-cost obstruction.
No stabilization, universal representation or near-one coverage conclusion is adopted.

Historical pending-review wording in the retained arguments records their status when written.
This adoption and the completed findings determine current status.
Only heading depth and relative navigation are relocated.
Necessary author/reviewer programs and mathematical results remain at J25 and J31; no fresh computation or source-proof inspection is claimed by this retention.
Unrestricted G0001 remains active and unresolved.

<a id="retained-cycle-proof"></a>
## Longer signed-cycle surgeries and the cost of attachments

Date: started 2026-10-09 and completed 2026-10-10, Asia/Hong_Kong.
New bounded structural exploration for G0001 under the coordinating execution gate.
The question is whether the exact five-cycle operation in [D G0012](../claims/Yin_C_G0003_v1.md#five-cycle-surgery) extends to longer frustrated cycles with controlled temporary energy, and which order or attachment hypotheses matter.

### Starting contract and reuse

Reuse the adjacent integral Stokes congruences, their full determinant preservation, the sign gauge and the triangle-free monotone-rigidity proof from D G0009 and D G0012.
The earlier source attribution to FW24 remains at its direct-formula scope; no orbit classification or realization theorem is imported.
This round must change the structural move or invariant, not re-enumerate the earlier 66 terminals.
Any bounded search failure is inconclusive unless full closure or an independent invariant is proved.
General representation of arbitrary reciprocal polynomials and the unrestricted Lehmer gap remain open.

The completed derivations and exact experiment scope are retained below.
No fixed adoption is asserted; the whole-round local review is pending.

The new continuing program is [J G0025](../computations/programs/Yin_J_G0025/readme.md).
A briefly delegated cycle_invariant agent independently flagged the ascent-count polynomial obstruction described below before the coordinator needed its concurrency slot for a different proof review.
The structural author independently identified the same candidate and supplies the full derivation and executed checks retained here.
That shared discovery is not an independent review.

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
When the whole input is a simple triangle-free signed graph, nonswitchability and D G0012's rigidity prove that the necessary barrier for strict energy reduction is exactly one.

Arbitrary attachments at all swept vertices cannot silently be included.
If each has disjoint simple pendant attachments of cardinalities d_i, in addition to the common closing coordinate, then the displayed formulas become

    Delta E_j = 1+sum_(i=2)^(j+1) d_i,
    Delta E_final = -1+d_1+2 sum_(i=2)^(m-1) d_i.

Thus the very same sweep can increase the final energy.
This is an exact coupling cost, not evidence that every different possible reduction must fail.

<a id="degree-barrier"></a>
### 3. Arbitrarily large necessary escape barriers from attachments

There is nevertheless an operation-invariant barrier before any new graph shape can be reached.
For a simple triangle-free signed graph, the first nonzero-energy adjacent mutation at an edge raises energy by the degree of its reflected endpoint minus one; a zero-change move preserves the signed graph up to vertex permutation and signs, as proved in D G0012.
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

<a id="cycle-round-verification"></a>
### 4. Executed checks, scope and next discriminator

The final retained J G0025 runs completed on 2026-10-10 using Python and SymPy.
The two programs import no previous search implementation and use exact integers/symbolic expressions; no floating-point root estimate or optimization output enters any result.

- `controls.py` checks consecutive cycles of lengths3 through12, with all intermediate energies and full characteristic polynomials.
  The length-three control decreases directly, while every length at least four follows n,n+1,...,n+1,n-1.
  It also exhausts all233 low-energy rank-four matrices for the displayed obstruction.
- `verify_family.py` checks the fully variable before-and-after coupling formulas for path-block sizes3 through7, with two earlier vertices, three later vertices and all15 through35 path/outside couplings symbolic.
  Arbitrary outside blocks and earlier-to-later couplings are also retained.
  These are finite symbolic controls for the arbitrary-size proof, not its justification by extrapolation.
- The latter program checks both the frustrated and absolute-cycle polynomials for all76 cycle orderings of sizes3 through6 modulo rotation and reversal.
  Direct determinants at n+1 integer values certify each polynomial identity independently of the first program's inverse/characteristic-polynomial calculation.
- A second rank-four exclusion calculation examines the same233 complete inputs via direct determinants at t=1 and t=-1:32 signed stars survive the first test and none survives the second.
  This matches the elementary graph argument above.
- Nine explicit lattice Gram/index controls in dimensions4 through12 and twelve pendant-degree controls (cycle lengths4 through6, zero through three leaves per vertex) also pass.
  Their observed first-step energy changes are precisely the permitted zero changes and positive changes r+1.

The first program's initial run reached its mathematical assertions but failed while serializing a SymPy integer matrix into JSON.
Converting that output matrix to ordinary integers fixed the operational error; canonical outputs were written only after the successful rerun.
No failed search is hidden or used as mathematical evidence.

The author self-checked the matching argument including n=3, every displayed basis vector, arbitrary earlier/later coupling sums, the even-sum lattice and its elementary indecomposability argument, and the first graph-change lower bound.
The brief subagent contribution and the coordinator's parallel absolute-cycle deduction were disclosed above.
Separately organized whole-round review is not supplied by these author-written programs.

The question now has three precise answers: long cycles in the stated two-boundary attachment family have a sharp one-unit reduction; internal attachments can impose unbounded necessary adjacent-move barriers; and middle ascent counts can prohibit switchable representatives in the entire fixed-rank integral congruence class even though the absolute cover adds zero Mahler measure.
Thus energy reduction or conversion to a tree is stronger than the scalar cost objective actually needs.

The next useful test should track the extra absolute-cover Mahler cost on controlled attached-cycle families, together with the exact coupling vectors, rather than treating every nonswitchable or high-energy presentation as costly.
One should first discriminate which attachments introduce noncyclotomic extra factors and whether the coupling identities move that cost without demanding a tree.
A separate needed arithmetic hypothesis would have to connect these attachment patterns to small-measure inputs.
No such hypothesis, general realization theorem, or gap conclusion is asserted in this round; no further enumeration is needed for the findings above.

<a id="cycle-round-local-review"></a>
### 5. Separately organized local review

On 2026-10-10, after the final Section 4 was retained, the coordinating AI for Yin read this entire argument and the complete J G0025 `verify_family.py`, then reran that verifier successfully with Python and SymPy.
The reviewer had assigned the general cycle/attachment question, received progress explanations and requested explicit scalar and small-measure boundaries.
The author had already written the absolute-cycle polynomial when the coordinator separately supplied the same calculation; this was a parallel matching derivation, not an input to that written proof.
The root did not contribute the sweep, lattice obstruction or degree-barrier proofs.
The review is nonblind local mathematical checking, not fixed adoption, personal human inspection or formal verification.

The review checked the matching recurrence and both full-cycle permutation signs, including n=3; the dependence on ascent count; all possible low-energy rank-four graph types and their t=1,-1 exclusions; the explicit even-sum lattice basis, norm-two spanning and nonorthogonality connectivity; the resulting orthogonal indecomposability; and the principal-minor, tree-coefficient and switchable-cycle contradictions.
It checked every intermediate sweep basis, the orientation of earlier and later coupling transformations, both exact energy formulas and their pendant specializations.
The first nonzero-energy move argument applies because all earlier zero-change moves preserve the same simple triangle-free signed graph and its degrees.
The strict-reduction barrier needs that whole-input hypothesis, present in the final statement.
The isolated-cycle zero-cost observation does not extend automatically to attached graphs or near-one inputs.

The rerun passed all five symbolic arbitrary-coupling cases, all 76 ordered-cycle identities for both signs, the complete 233-input rank-four determinant exclusion, nine lattice Gram/index controls and twelve pendant-degree controls.
This is a separate execution and inspection of the author's checking program, not a third implementation; the original `controls.py` discovery/control run was not repeated.
The all-size conclusions rely on the displayed proofs, not extrapolation of finite tests.
No defect was found in the final stated scope.
The unrestricted representation, extra-Mahler-cost and small-measure coverage questions remain open.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0083_v1.md#integral-congruence-obstruction), with its original inspected scope and relationship.




<a id="cycle-surgery-retention-bindings"></a>
## Retention and review bindings

The structural author developed the complete cycle, lattice, sweep and barrier proof.
The coordinator's parallel absolute-cycle observation and the temporary delegated discovery remain disclosed in that proof.
The [complete separate noncontributor review](../audits/reviews/Yin_R_G0083_v1.md#independent-cycle-surgery-review) checks all four mathematical sections, including their reused mutation/rigidity interfaces; [J31](../computations/programs/Yin_J_G0031/readme.md) retains its independently authored checker and separate reruns of J25.
The earlier [coordinator review](#cycle-round-local-review) has its exact local scope preserved.
These findings jointly support the adopted results at the stated fixed-rank, attachment and adjacent-move boundaries.

Only completed D21 and its D31 review are retired after consumer repair; earlier exploratory D9/D12 remain in their responsible homes.
No extra execution is claimed by retention.

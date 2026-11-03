---
author: Yin
---

# Sparse connected neutral presentations with linear absolute-companion cost

The complete current mathematical statement and necessary proofs are adopted in [Yin_C_G0595_v1](../claims/Yin_C_G0595_v1.md#decision-complete-current-self-adoption), with [actual whole constructor SELF](../audits/reviews/Yin_R_G0765_v1.md#current-g325-complete-self-finding).
The original mathematical dates, authors, complete arguments, native/source evidence, useful failures, actual freezes and old review/adoption scopes remain below.
Original2026-10-10 pending/active labels describe their historical stage; the current G0001 execution remains paused and unresolved.


Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="sparse-diamond-cost-fixed-scope"></a>
## Current adopted scope

For every k>=2 an explicit connected signed-diamond integer upper-unitriangular presentation has rank3k+1, height1, maximum support degree4, strict energy4k+1 and full original polynomial Phi2^(k-1) Phi1^(2k) Phi3.
Its complete absolute companion restores exponential path multiplicity and has total logarithmic Mahler cost of order k, with all continuants and proper-cover factors retained.
An explicit height2 disconnected presentation has exactly the same original scalar polynomial, rank and energy, but zero original/absolute/cover cost.
No congruence of the two forms, positive irreducible seed, optimized-basis obstruction or near-one construction is asserted.
The complete all-k proof and whole noncontributor review follow, together with the independently verified five paired J81 controls.

The complete D191 author proof and review follow without abridgment.
Historical pending-review, pending-adoption and stopped-execution handoff sentences are superseded only by this current adoption paragraph.
Heading depths and relative navigation are relocated; all statements, proofs, source boundaries, unsuccessful-test scope and review history are preserved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## Changed higher-rank structural constructions with full scalar costs

Date: 2026-10-10.

<a id="sparse-diamond-reuse-and-scope"></a>
### 1. Reuse, conventions and the changed discriminator

The current S3/S6 entrances, [L317's complete binary criterion](Yin_L_G0317_v1.md#even-binary-realization-fixed-scope), [L303's attained tree benchmark](Yin_L_G0303_v1.md#plastic-tree-fixed-scope), [L234's Walsh family](Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope), and the [charged bipartite construction in L283](Yin_L_G0283_v1.md#charged-bipartite-stabilization-fixed-scope) were inspected at their relevant construction and cost interfaces.
They do not assert a general neutral-completion operation.
In particular the binary criterion is a statement about actual integral congruence classes, the Walsh example has growing total original measure, and the classical tree benchmark cannot be promoted to arbitrary signed matrices.

There is a particularly important direct reuse.
[D9's dense neutral control](../claims/Yin_C_G0002_v1.md#dense-neutral-control) already gives an unbounded-rank neutral polynomial with an exponentially expensive absolute presentation, together with an explicit integral congruence to a zero-cost chain.
Thus the broad phenomenon that a neutral scalar can have an expensive presentation is already known here.
The new discriminator below is a connected, bounded-degree, height-one architecture with only linearly many edges, an exact all-rank continuant, and a second presentation having the SAME entire scalar polynomial, rank and squared-entry energy but zero companion cost.
No new general trace inequality is claimed: the exact path expansion and full reciprocal Mahler estimate are reused from [L230](Yin_L_G0230_v1.md#trace-energy-companion-cost-bound).

For a proper integral matrix V (upper triangular with every diagonal entry1), write

    p_V(t)=det(tV+V^T),  V^-_ij=-|V_ij| for i<j,
    V^-_ii=1,  E(V)=sum_(i<j) V_ij^2,
    H(V)=max_(i,j)|V_ij|.                                      (1)

All logarithmic Mahler measures include the complete monic polynomial with multiplicities.
The [literal two-sheet rule from D9](../claims/Yin_C_G0002_v1.md#signed-cover-identity) replaces an upper entry a<=0 by a I_2 and a>0 by -a[[0,1],[1,0]], with diagonal blocks I_2.
Denote the actual resulting proper matrix by W(V).
Its equal/opposite sheet subspaces give p_W=p_V p_(V^-).
We retain both factors and do not divide the scalar measure by2.

The matrix and determinant arguments below are elementary finite algebra, including Schur elimination over Q(t), path counting and the already retained trace estimate.
No new external theorem, classification of neutral forms, source-proof audit or external novelty claim is needed.
No congruence between the two new presentations is asserted.
This distinction is essential: equal scalar polynomials, equal rank and equal energy do not by themselves supply an integral change of basis.

<a id="signed-diamond-necklace-construction"></a>
### 2. A connected height-one family with an entirely neutral scalar

Fix an integer k>=2.
Order the n=3k+1 standard basis vertices as

    a_0,b_0,c_0,a_1,b_1,c_1,...,a_(k-1),b_(k-1),c_(k-1),a_k.

Let V_k have diagonal1 and exactly the following nonzero upper entries:

    V(a_i,b_i)=V(a_i,c_i)=V(b_i,a_(i+1))=-1,
    V(c_i,a_(i+1))=+1                    (0<=i<k),
    V(a_0,a_k)=-1.                                          (2)

All displayed positions are distinct for k>=2.
These are literal matrices in the standard integer basis; no rational or half-integral lattice is used.
Their undirected support is connected, has maximum degree4, and consists of k consecutive diamonds plus the closing edge.
The rank, height and energy are

    rank V_k=3k+1,  H(V_k)=1,  E(V_k)=4k+1,
    sum_(i,j)V_k(i,j)^2=7k+2.                               (3)

The rank here is the matrix dimension, and also its actual rank because det V_k=1.
The term "closing" describes the support graph; the matrix remains upper triangular in the prescribed order.

**Theorem 1.** For every k>=2 the complete scalar polynomial is

    p_(V_k)(t)=(t+1)^(k-1)(t-1)^(2k)(t^2+t+1)
              =Phi_2^(k-1) Phi_1^(2k) Phi_3.                 (4)

In particular m(p_(V_k))=0, and every one of its 3k+1 roots is retained in(4).

*Proof.* Put q=t+1, d=t^2+1 and e=(t-1)^2.
In the pencil tV_k+V_k^T, simultaneously eliminate the 2k vertices b_i,c_i.
Their principal block is q I_(2k), so this is legitimate over Q(t).
The two forward path terms between a_i and a_(i+1) are +t^2 and -t^2 before their common division by q; the two reverse terms are +1 and -1.
They cancel exactly.
Each of the two eliminated vertices subtracts t/q from each of its incident a-diagonal entries.
Consequently the reduced matrix on a_0,...,a_k has endpoint diagonals d/q, interior diagonals e/q, and only the corner entries -t and -1 remaining off diagonal.

Multiplying this reduced matrix by q and restoring the eliminated determinant gives

    p_(V_k)=q^(k-1) e^(k-1)(d^2-t q^2).

The last factor is

    (t^2+1)^2-t(t+1)^2
       =t^4-t^3-t+1=(t-1)^2(t^2+t+1).

This proves(4) over Q(t), hence as an identity of entire integer polynomials.
No evaluation at t=-1 is used in the elimination, and the polynomial identity retains its full multiplicity there.
The degrees sum to k-1+2k+2=3k+1.
All three displayed factors are cyclotomic, which proves the measure assertion.
This is a connected construction, but its growing degree is entirely neutral and is not growing positive irreducible complexity.

<a id="absolute-diamond-continuant"></a>
### 3. The full absolute companion and the exponential path charge

Let U_k=V_k^-.
All four edges of every diamond and the closing edge now have entry -1.
Define polynomials F_j by

    F_(-1)=0,  F_0=1,  F_1=e,
    F_j=e F_(j-1)-4t^2 F_(j-2)             (j>=2),             (5)

where d,e,q are as above.
For k>=2 put

    D_k=(d^2-t q^2)F_(k-1)-8d t^2 F_(k-2)
          +16t^4 F_(k-3)-2^k q(t^(2k)+t).                   (6)

The F_(-1)=0 convention handles k=2 exactly; there is no use of a negative-index recurrence beyond it.

**Theorem 2.** The complete companion and literal-cover polynomials are

    p_(U_k)=q^(k-1)D_k,
    p_(W(V_k))=q^(2k-2)(t-1)^(2k)(t^2+t+1)D_k.             (7)

Here D_k is monic, reciprocal, of degree2k+2 and constant1.
It is retained in full, including any further cyclotomic factors it may have; the power q^(k-1) in(7) is not asserted to be the exact total multiplicity of q in p_(U_k).

*Proof.* The same elimination has the same diagonal entries as in Theorem1.
Its adjacent a-entries are now -2t^2/q above and -2/q below, and its long corner entries are -t,-1.
Thus p_(U_k)=q^(k-1)det A_k, where A_k is the (k+1)-dimensional cyclic tridiagonal matrix with endpoint diagonals d, interior diagonals e, adjacent entries -2t^2,-2 and corner entries -tq,-q.

For the open path obtained by deleting the corner entries, the usual determinant expansion at an endpoint gives

    det(path)=d^2 F_(k-1)-2d(4t^2)F_(k-2)
                  +(4t^2)^2 F_(k-3).

This identity can alternatively be proved by multilinearity in the two endpoint diagonals followed by the recurrence(5).
A permutation using both corner entries as a transposition contributes -tq^2 F_(k-1).
Any permutation using a corner entry without that transposition must traverse the entire remaining path: the only simple cycle in this support besides edge transpositions is the full cycle.
The two orientations contribute -2^k t^(2k)q and -2^k t q.
Their signs are negative because a length-(k+1) permutation cycle has sign(-1)^k, and its k+1 negative matrix entries contribute(-1)^(k+1).
This also covers k=2, where the reduced support is a triangle.
These mutually exclusive cases give det A_k=(6).

The full determinant of a proper matrix is monic reciprocal of its dimension and has constant1.
Division by the explicitly symmetric monic factor q^(k-1) proves the stated degree, reciprocity and constant term of D_k, without any root classification or cancelled determinant.
The literal-cover factorization from(1) now gives the second equation in(7).

To charge the companion, write U_k=I-N_k with N_k the strictly upper, entrywise nonnegative adjacency matrix.
The exact retained L230 identity is

    tr(-U_k^-1 U_k^T)
       =-n+sum_(j=1)^(n-1) tr(N_k^j N_k^T).                 (8)

The j=1 term equals the energy4k+1.
For j>=2 a mixed trace counts a strictly increasing path from u to v, closed by an actual edge u->v.
None of the four edges inside a diamond has an alternative increasing path between its endpoints.
The only remaining possibility is the edge a_0->a_k, whose increasing alternative paths choose b_i or c_i at every diamond.
There are exactly2^k such paths, all of length2k; the direct edge itself has already been counted in the energy.
It follows that

    tr(-U_k^-1 U_k^T)=k+2^k.                                (9)

This counts the complete nilpotent expansion, not only a selected subset of cycles.
In particular the coefficient of t^(3k) in p_(U_k) is exactly -(k+2^k).

Put epsilon_k=1 when 3k+1 is odd and0 otherwise.
The full reciprocal trace estimate in L230, applicable also to nonreal roots and multiple expanding pairs, yields

    2 cosh m(p_(U_k)) >= 2^k-2k+1+2epsilon_k.

Since m>=0 and exp(-m)<=1, for every k>=3 this implies

    m(p_(U_k)) >= log(2^k-2k),
    m(p_(U_k)) >= (k-1)log2                  (k>=4).         (10)

For the second inequality, 2k<=2^(k-1) at k=4, and the inequality persists by induction.
At k=2 the sharper parity expression gives 2cosh m>=3, so the companion already has positive measure there.
At k=3 it also gives 2cosh m>=3.
No claim that D_k has only one expanding pair is involved.

There is an elementary upper bound of the same linear order.
On the unit circle a row of tU_k+U_k^T has squared Euclidean norm at most4 plus its support degree.
The two endpoint a-vertices have degree3, the k-1 interior a-vertices degree4, and the2k middle vertices degree2.
Hadamard's determinant inequality, followed by the logarithmic Mahler integral, gives

    m(p_(U_k)) <= log7 + ((k-1)/2)log8 + k log6.             (11)

Zeros on the circle cause no problem: the pointwise upper bound holds everywhere and the logarithm of a nonzero polynomial has an integrable circle singularity.
Equations(10)--(11) establish linear growth of the COMPLETE companion measure in k, although the original polynomial has measure zero and the original matrix is sparse, height one and of bounded support degree.
Since m(p_(V_k))=0, this is also precisely the full literal-cover measure.

<a id="same-scalar-rank-energy-neutral-control"></a>
### 4. A zero-cost presentation with exactly the same scalar, rank and energy

Let

    K=[[1,-2],[0,1]],    A=[[1,-1],[0,1]],
    Z_k=K^(direct-sum k) direct-sum A
                       direct-sum I_(k-1).                 (12)

This is another literal proper integral matrix, with no quotient or dropped factor.
The two complete binary determinants are p_K=(t-1)^2 and p_A=t^2+t+1.
Therefore

    p_(Z_k)=p_(V_k),  Z_k^-=Z_k,
    rank Z_k=3k+1,  H(Z_k)=2,  E(Z_k)=4k+1,
    p_(W(Z_k))=p_(V_k)^2,  m(p_(W(Z_k)))=0.                (13)

The identity matrix contributes exactly k-1 factors t+1.
Every rank, energy and neutral multiplicity in(13) agrees with the stated full polynomial; the larger height is paid explicitly.
Thus no function of just this complete scalar polynomial, matrix rank and squared-entry energy can recover the actual absolute-companion measure of an arbitrary presentation.
It takes the value zero on Z_k and at least(k-1)log2 on V_k for k>=4, with all three proposed scalar diagnostics identical.

This is not a new instance of the general presentation-dependence phenomenon from D9.
Its changed content is that the expensive presentation can have height1, maximum support degree4 and energy4k+1, and that the inexpensive presentation has the same rank AND energy.
D9's dense family has quadratic edge energy and provides an actual integral congruence; no such congruence is supplied here.
We neither infer congruence from equal scalar data nor claim inequivalence.
If a useful congruence exists, its basis height and all intermediate costs must still be established separately.

For clarity the full cost table is

| Actual matrix | Dimension | Entry height | Strict-upper squared energy | Entire logarithmic measure |
| --- | --- | --- | --- | --- |
| V_k | 3k+1 | 1 | 4k+1 | 0 |
| U_k=V_k^- | 3k+1 | 1 | 4k+1 | m(D_k), satisfying(10)--(11) |
| W(V_k) | 6k+2 | 1 | 8k+2 | m(D_k) |
| Z_k=Z_k^- | 3k+1 | 2 | 4k+1 | 0 |
| W(Z_k) | 6k+2 | 2 | 8k+2 | 0 |

The doubled energies follow because each nonzero original upper entry produces exactly two entries of the same magnitude in its literal two-sheet block.
The sums of squared entries including diagonals are7k+2 in each rank-(3k+1) matrix and14k+4 in each cover.
The proper-cover theorem is applied to actual upper-unitriangular matrices, so no relaxed full-entry lift, diagonal sign correction or determinant normalization is being substituted.

### 5. What this discriminates, and what remains open

This family is a negative test for an otherwise plausible neutral-completion design: composing local exact signed path cancellations in a connected sparse architecture does not make the resulting absolute completion cheap.
The absolute paths multiply across cells, and one retained closing edge charges their full product in a scalar coefficient.
The path count is a global interaction, despite the local bounded degree and small entries.
L230 then converts that interaction into a full Mahler cost rather than using energy as a surrogate objective.

At the same time the explicit Z_k family shows that the charge is avoidable by changing the actual form while preserving the complete scalar target.
This round supplies no canonical neutral-removal map between the two forms.
A discriminating next construction would keep a genuinely varying positive irreducible factor while replacing the multiple-path return by a controlled effective connection, and would estimate its whole companion before deleting or compressing any neutral factors.
Alternatively, an actual integral congruence or a precise invariant separating V_k from Z_k would clarify whether this scalar-level cost repair can also be realized as a basis operation.
These are questions, not asserted constructions.

In particular (4) is entirely cyclotomic: it is not a positive-measure seed, a near-one family, an irreducible-degree growth result, or an improvement on L303's attained positive benchmark.
The argument does not exclude all height-one completions, all sparse graphs, all congruence classes at the displayed scalar, or any of the active S3/S6 directions.
It supplies a reusable architecture-specific cost diagnostic at unbounded rank with all factors retained.

<a id="sparse-diamond-execution-and-self-check"></a>
### 6. Complete finite controls, contributions and author self-check

The responsible [J81](../computations/programs/Yin_J_G0081/readme.md) was allocated before execution for exactly k=2,3,4,5,6, each with both explicit architectures and their literal absolute companions and proper covers.
The aggregate author runtime cap was120seconds, without search, random choices, adaptive extension or a root approximation.
Exact matrices, signs, ordering, coefficient convention and every check were saved before the first run.
The sole author execution completed at2026-10-10T11:09 in0.2611711999925319 seconds, using Python3.12.14 and SymPy1.14.0.
No mathematical run failed or was repeated.

The program builds all30 literal matrices, inverts each unitriangular matrix by integer substitution and computes the complete characteristic polynomial of -X^-1 X^T.
This is compared against the original formula(4), the separately constructed continuant(5)--(6), and both complete cover products.
It checks every dimension, height, energy and total squared-entry sum in Section4, every reciprocal coefficient, and all n-1 mixed traces in(8) for each connected absolute matrix.
The traces6,11,20,37,70 agree with(9).
Full integer factor arrays are retained and their products checked; no irreducibility claim for their residual factors is inferred.
These finite controls corroborate the symbolic argument but do not substitute for its all-k proof.

For example k=2 gives

    D_2=(t+1)^2(t^4-9t^3+8t^2-9t+1).

Thus even here the displayed q^(k-1) in(7) is only an explicitly extracted factor, not the entire neutral multiplicity.
The saved k=4 polynomial additionally contains(t-1)^2.
Every such factor remains present in the full D_k and cover identity; no scalar cost is silently discarded.
These examples are consistency controls, not a proposed all-k factor classification.

The complete original whole author checklist and its actual date precision are retained at [the responsible original SELF finding](../audits/reviews/Yin_R_G0765_v1.md#original-g325-author-self-finding).

Root supplied only the broad changed higher-rank question, allocation and shared execution gate.
The authoring orbit_research agent derived the signed-diamond family, continuant, all-k path count and same-scalar/rank/energy control, implemented the exact finite checks and wrote this proof.
The reviewer structural_research was assigned only the final complete review and supplied none of these derivations.
Shared progress reports make the forthcoming review nonblind; no independent review has occurred at this author stage.
Author proof and native J81 files are to be held after the explicit freeze message for whole noncontributor review and a differently implemented complete finite verification.
No fixed adoption or G0001 completion is asserted by this draft.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0150_v1.md#genuinely-different-complete-j81-verification), with its original inspected scope and relationship.

---
author: Yin
---

# Complete necessary positive absolute-cover cost and exact interacting-triangle reductions

The entire necessary original D33 proof is retained from [L185](../ledger/Yin_L_G0185_v1.md#retained-positive-cover-proof).
The coordinator originated the general Gram-instability/Perron candidate; the structural author supplied its complete positive-vector details and the interacting-triangle family.
The exact original [whole collaborator check](../audits/reviews/Yin_R_G0084_v1.md#positive-cover-collaborator-review) is SELF.
The original whole finding's initial arrangement remains unknown: its known reading of the collaborator finding before final findings does not establish when its first autonomous complete reconstruction occurred.
Its exact whole scope is retained in [R653's later comparison for C440v2](../audits/reviews/Yin_R_G0653_v1.md#positive-cover-isolated-whole), without changing that historical relationship.
The original unsupported ordering-sensitive interpretation, exact requested correction and subsequent single-sentence reread remain precise in that same historical comparison.
That narrow closure is not a complete corrected-chain independent review, and R643's authored whole check supplies none.
[McM02-U001](../audits/literature/McM02/Yin_U001.md#mcm02-u001) owns the distinct actual author/reviewer source-comparison records; the complete proof below is local.
J32 owns every original program/result and finite execution domain.
No source/PDF reading, source-proof audit, native rerun/J, research Task/E or new ordering-variation result is added.

## Statement

For every integral upper-unitriangular real matrix V of finite rank n>=1, put

    p_V(t)=det(tV+V^T),
    E(V)=sum_(i<j)V_ij^2,
    G=V+V^T,
    A_ii=0, A_ij=A_ji=|V_ij| for i<j,
    a=rho(A),
    V^-=I-|V-I|.

Every measure below is the ordinary logarithmic Mahler measure of the entire polynomial, without division by rank.
The complete proper signed-cover factorization gives p_W=p_V p_(V^-), hence extra cost exactly m(p_(V^-)).
Arbitrary integral entry magnitudes and reducible support are allowed.

If m(p_V)>0, then G is not positive semidefinite, a>2, and p_(V^-) has an actual positive real root at least

    T(a)=((a+sqrt(a^2-4))/2)^2>1.

Consequently

    m(p_(V^-))>=log T(a)=2 arcosh(a/2)>0.

The singular semidefinite case is included: for C=-V^(-1)V^T, C fixes ker G pointwise, its quotient isometry has unit-circle spectrum and the full characteristic polynomial includes every kernel multiplicity, even with Jordan coupling.
If delta=-lambda_min(G)>0, then a>=2+delta and the same proof gives the lower cost2 arcosh(1+delta/2).
This delta depends on the chosen presentation.
The positive-root argument uses positive left/right Perron vectors on a component attaining a and a continuity/intermediate-value argument.
It assumes no global irreducibility, monotonicity or uniqueness of an exterior root.
This is a necessary lower cost, with no optimized upper cost relative to the original measure or degree-uniform consequence.

For every integer r>=1, let V_r have ordered vertices0,a_1,b_1,...,a_r,b_r and exactly the positive unit entries V_(0,a_j)=V_(0,b_j)=V_(a_j,b_j)=1.
Its r triangles share only the central vertex and E(V_r)=3r.
Put F=t^2+t+1 and s=t+1.
For any subset of k distinct branch forward adjacent mutations,0<=k<=r, let V_(r,k) be the result.
Every branch move changes its internal pair to-1, central coupling(1,1) to(1,0), lowers energy by one and introduces no cross-branch edge.
The disjoint branch operations commute.
For every such r and subset,

    E(V_(r,k))=3r-k,
    p_(V_(r,k))=s F^(r-1)[t^2+(1-r)t+1],
    p_(V_(r,k)^-)=s F^(r-1)[t^2+(1-3r+2k)t+1].

All polynomial factors and all roots at cleared Schur denominators remain included.
The signed Gram form is positive definite for r<3, positive semidefinite with a one-dimensional kernel for r=3 and has exactly one negative direction for r>3.
The whole original measure is zero for r=1,2,3.
For every r>=4,

    m(p_(V_r))=arcosh((r-1)/2)>0,
    m(p_(V_(r,k)^-))=arcosh((3r-2k-1)/2).

The full extra cost strictly decreases at every branch cancellation and at k=r equals the original measure.
The final r-arm tree is switchable; its proper doubled cover has total measure exactly2m(p_(V_r)).
This is an achieved endpoint, without global minimality over congruent or stabilized presentations.

For every r>=1 and0<=k<=r the full symmetric absolute adjacency polynomial is

    det(xI-A_(r,k))
      =(x^2-1)^(r-1)[x^3-(1+2r-k)x-2(r-k)].

For r>=4 the final tree's Perron radius is sqrt(r+1), and

    2 arcosh(sqrt(r+1)/2)=arcosh((r-1)/2).

Thus the general adjacency-dependent lower bound is sharp on these positive-measure integral examples.
For every r>=4 and k<r, its Perron radius is strictly below sqrt(3r-2k+1); the general lower bound is strictly smaller than the exact added cost.
This proves a strict excess above that bound, with no vertex-ordering variation claim.
The smallest positive original measure in the family is arcosh(3/2), bounded away from zero.
No near-one family, arbitrary reciprocal-polynomial realization, neutral-completion coverage, optimized upper cost or unrestricted gap is supplied.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-r800-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:07 |
| status | open |
| reason | Retain the complete singular-PSD/Perron/IVT positive-cost proof and all-parameter interacting-triangle signed/absolute/Gram/energy/adjacency/cost identities, with the corrected strict-excess interpretation, original contributor/source/native boundaries and unresolved optimized upper-cost/coverage gate. Actual whole current self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire positive-cost and exact triangle theorem](#statement) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. |
| argument | [Complete general and all-parameter family proofs](#argument) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. |
| dependency | [Exact original signed cover and mutations](Yin_C_G0002_v1.md#signed-cover-identity) | Only actual unnormalized proper p_W=p_V p_(V^-) identity and allowed adjacent integral unimodular changes, preserving the entire scalar polynomial at the existing FW24 direct-formula attribution scope; no orbit/classification/representation premise. |
| support | [Complete isolated-cycle zero-cost distinction](Yin_C_G0437_v2.md#cycle-order-polynomial) | Only the exact isolated frustrated/absolute cyclotomic cycle control explaining the original zero-cost question. Its fixed-rank presentation rigidity is not used to infer positive scalar cost or attached-family coverage. |
| support | [Original exact author finite controls](../computations/programs/Yin_J_G0032/readme.md#executed-scope-and-findings) | All60 actual r1--8 inputs/every subset r<=4 and prefix subsets beyond4,2148integer Bareiss determinant values for three full degree2r+1 polynomials,38reverse-order controls/every executed unit-energy-drop/sign gauge,8exact Gram/kernel/inertia checks and arbitrary weighted rank3 C/G identities. Original author execution and contributor rerun are retained; no new run, independent implementation or extrapolation to untested r is asserted. |
| support | [Exact earlier spectral source comparison](../audits/literature/McM02/Yin_U001.md#mcm02-u001) | Only the original2026-10-10 distinct author/reviewer reading of Theorems1.3/5.1, bicolored spectral relation and p171 symmetric-nonnegative adjacency extension at statement/formula/attribution depth. It supplies established context without a novelty claim; the complete proof here is direct and no full gap/classification theorem or underlying proof audit is imported. |

### Decision explicit-energy-and-inverse-conventions

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:08 |
| status | open |
| reason | Make the already used original squared strict-upper energy definition and inverse-matrix notation explicit in the Statement, and select the exact original mutation input separately from its cover-factorization input. Every complete mathematical proof, formula, parameter, source/native contribution and original interpretation-correction boundary remains unchanged. This open physical convention clarification precedes whole current self-check. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. Original energy is explicitly sum of strict-upper entry squares and C uses the inverse of V; no formula or proof changes. |
| argument | [Exact retained argument](#argument) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. Original energy is explicitly sum of strict-upper entry squares and C uses the inverse of V; no formula or proof changes. |
| dependency | [Exact retained dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Only the actual unnormalized proper p_W=p_V p_(V^-) identity at the existing FW24 direct-formula attribution scope; no orbit/classification/representation premise. |
| support | [Exact retained support](Yin_C_G0437_v2.md#cycle-order-polynomial) | Only the exact isolated frustrated/absolute cyclotomic cycle control explaining the original zero-cost question. Its fixed-rank presentation rigidity is not used to infer positive scalar cost or attached-family coverage. |
| support | [Exact retained support](../computations/programs/Yin_J_G0032/readme.md#executed-scope-and-findings) | All60 actual r1--8 inputs/every subset r<=4 and prefix subsets beyond4,2148integer Bareiss determinant values for three full degree2r+1 polynomials,38reverse-order controls/every executed unit-energy-drop/sign gauge,8exact Gram/kernel/inertia checks and arbitrary weighted rank3 C/G identities. Original author execution and contributor rerun are retained; no new run, independent implementation or extrapolation to untested r is asserted. |
| support | [Exact retained support](../audits/literature/McM02/Yin_U001.md#mcm02-u001) | Only the original2026-10-10 distinct author/reviewer reading of Theorems1.3/5.1, bicolored spectral relation and p171 symmetric-nonnegative adjacency extension at statement/formula/attribution depth. It supplies established context without a novelty claim; the complete proof here is direct and no full gap/classification theorem or underlying proof audit is imported. |
| dependency | [Exact original adjacent integer mutations](Yin_C_G0002_v1.md#mutation-and-energy) | Only original forward/inverse adjacent unimodular congruences, exact unitriangular endpoint, full scalar determinant preservation and original energy convention; no orbit classification or cost optimality is imported. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:09 |
| status | proved |
| reason | Adopt after actual complete current self-check of the general singular-PSD/kernel quotient and full characteristic multiplicities, signed-to-absolute Rayleigh/Perron/IVT positive-root bound and every all-r/all-subset triangle Schur, full signed/absolute/Gram/adjacency polynomial, exact energy, cost and sharp/strict comparison. Full native code/data were statically read at the original exact domain without a run; source reading remains comparison-only. No substantive mathematical defect or missing hypothesis was found. The unsupported old ordering interpretation and paragraph-only correction closure remain precise; current authored SELF does not close original whole UNKNOWN or any full corrected-proof independent-review obligation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. Original energy is explicitly sum of strict-upper entry squares and C uses the inverse of V; no formula or proof changes. |
| argument | [Exact retained argument](#argument) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. Original energy is explicitly sum of strict-upper entry squares and C uses the inverse of V; no formula or proof changes. |
| dependency | [Exact retained dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Only the actual unnormalized proper p_W=p_V p_(V^-) identity at the existing FW24 direct-formula attribution scope; no orbit/classification/representation premise. |
| support | [Exact retained support](Yin_C_G0437_v2.md#cycle-order-polynomial) | Only the exact isolated frustrated/absolute cyclotomic cycle control explaining the original zero-cost question. Its fixed-rank presentation rigidity is not used to infer positive scalar cost or attached-family coverage. |
| support | [Exact retained support](../computations/programs/Yin_J_G0032/readme.md#executed-scope-and-findings) | All60 actual r1--8 inputs/every subset r<=4 and prefix subsets beyond4,2148integer Bareiss determinant values for three full degree2r+1 polynomials,38reverse-order controls/every executed unit-energy-drop/sign gauge,8exact Gram/kernel/inertia checks and arbitrary weighted rank3 C/G identities. Original author execution and contributor rerun are retained; no new run, independent implementation or extrapolation to untested r is asserted. |
| support | [Exact retained support](../audits/literature/McM02/Yin_U001.md#mcm02-u001) | Only the original2026-10-10 distinct author/reviewer reading of Theorems1.3/5.1, bicolored spectral relation and p171 symmetric-nonnegative adjacency extension at statement/formula/attribution depth. It supplies established context without a novelty claim; the complete proof here is direct and no full gap/classification theorem or underlying proof audit is imported. |
| dependency | [Exact retained dependency](Yin_C_G0002_v1.md#mutation-and-energy) | Only original forward/inverse adjacent unimodular congruences, exact unitriangular endpoint, full scalar determinant preservation and original energy convention; no orbit classification or cost optimality is imported. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0643_v1.md#current-positive-cover-whole-finding) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. Original energy is explicitly sum of strict-upper entry squares and C uses the inverse of V; no formula or proof changes. Actual current whole relationship is self-reviewed; the original whole/interpretation/paragraph-closure UNKNOWN, complete collaborator SELF and precise listed author SELF remain separate; no full corrected-chain isolated review is supplied. |


### Decision complete-isolated-whole-r800-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:59 |
| status | proved |
| reason | Adopt the new complete isolated whole finding after full coordinator reading of its exact mathematics, old whole/negative/source/native comparisons and truthful date/context limits; no target proof repair and no retrospective change to original UNKNOWN or SELF relationships. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. Original energy is explicitly sum of strict-upper entry squares and C uses the inverse of V; no formula or proof changes. |
| argument | [Complete selected argument](#argument) | Entire original D33 mathematical Sections1--2/equations(1)--(5): every integral upper-unitriangular rank/reducible weighted support/full ordinary Mahler measure, singular PSD kernel and quotient isometry/characteristic multiplicities, signed-to-absolute Rayleigh/delta and positive left-right Perron geometric-mean bound, spectral continuity/strict-triangular large-t/IVT actual positive root T and lower cost, every r>=1/any subset0<=k<=r exact signed/absolute/Gram/energy/adjacency identity with all factors and denominator-root guards, r<=3 neutral/r>=4 positive/full cost per step/tree Perron equality and k<r strict comparison, corrected strict-excess-only interpretation and no ordering-variation/global optimality/optimized upper cost/near-one coverage/unrestricted gap. Existing J32 finite domains and McM02 comparison-only reading remain at their actual scope. Original energy is explicitly sum of strict-upper entry squares and C uses the inverse of V; no formula or proof changes. |
| dependency | [Exact accepted input](Yin_C_G0002_v1.md#signed-cover-identity) | Only the actual unnormalized proper p_W=p_V p_(V^-) identity at the existing FW24 direct-formula attribution scope; no orbit/classification/representation premise. |
| support | [Exact support](Yin_C_G0437_v2.md#cycle-order-polynomial) | Only the exact isolated frustrated/absolute cyclotomic cycle control explaining the original zero-cost question. Its fixed-rank presentation rigidity is not used to infer positive scalar cost or attached-family coverage. |
| support | [Exact support](../computations/programs/Yin_J_G0032/readme.md#executed-scope-and-findings) | All60 actual r1--8 inputs/every subset r<=4 and prefix subsets beyond4,2148integer Bareiss determinant values for three full degree2r+1 polynomials,38reverse-order controls/every executed unit-energy-drop/sign gauge,8exact Gram/kernel/inertia checks and arbitrary weighted rank3 C/G identities. Original author execution and contributor rerun are retained; no new run, independent implementation or extrapolation to untested r is asserted. |
| support | [Exact support](../audits/literature/McM02/Yin_U001.md#mcm02-u001) | Only the original2026-10-10 distinct author/reviewer reading of Theorems1.3/5.1, bicolored spectral relation and p171 symmetric-nonnegative adjacency extension at statement/formula/attribution depth. It supplies established context without a novelty claim; the complete proof here is direct and no full gap/classification theorem or underlying proof audit is imported. |
| dependency | [Exact accepted input](Yin_C_G0002_v1.md#mutation-and-energy) | Only original forward/inverse adjacent unimodular congruences, exact unitriangular endpoint, full scalar determinant preservation and original energy convention; no orbit classification or cost optimality is imported. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0653_v1.md#positive-cover-isolated-whole) | Whole corrected proper-cover/singular/Perron/positive-root chain and every r/subset/family cost, including actual old unsupported-ordering negative finding and narrow closure scope. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-positive-cover-proof"></a>
<a id="positive-cover-cost-fixed-scope"></a>

<a id="positive-absolute-cover-cost"></a>
### 1. Positive measure forces strictly positive extra cover cost

Let G=V+V^T and let A be the symmetric nonnegative matrix with A_ii=0 and A_ij=|V_ij| for i<j.
Set a=rho(A).
If m(p_V)>0, then G is not positive semidefinite, a>2, and p_(V^-) has a positive real root at least

    T(a)=((a+sqrt(a^2-4))/2)^2.

Consequently

    m(p_(V^-)) >= log T(a) = 2 arcosh(a/2) > 0.

All measures are ordinary logarithmic Mahler measures without division by the matrix rank.
Reducible support and arbitrary integral entry magnitudes are allowed.
This gives a necessary positive cost, not a degree-uniform lower bound or a cost upper bound relative to m(p_V).

#### The semidefinite kernel cannot hide off-circle eigenvalues

Put C=-V^(-1)V^T.
Direct multiplication gives

    C^T G C=G,       C-I=-V^(-1)G.

If G is positive semidefinite, C fixes ker G pointwise.
On the quotient by that kernel, G induces a positive definite inner product and the induced C is an isometry.
Its complex eigenvalues have modulus one.
The characteristic polynomial of C is the product of the quotient characteristic polynomial and (t-1)^(dim ker G), even if the full transformation has nontrivial Jordan blocks.
Since p_V=det(tI-C), all its roots have modulus one.
Its leading coefficient is one, so its logarithmic Mahler measure is zero.
This proves the contrapositive without assuming G is nonsingular.

When G is not positive semidefinite, some real v has v^T Gv<0.
Since G has diagonal2 and absolute off-diagonal matrix A,

    2||v||^2 < -sum_(i!=j) G_ij v_i v_j
               <= |v|^T A |v| <= a||v||^2.

Thus a>2.
More quantitatively, if delta=-lambda_min(G)>0, the same Rayleigh comparison gives a>=2+delta and hence the extra-cost lower bound 2 arcosh(1+delta/2).
Delta depends on the presentation; its size is not an invariant of integral congruence.

#### A positive real root from the absolute adjacency

Let B be the strictly upper triangular part of A and M(t)=tB+B^T for t>0.
Then

    p_(V^-)(t)=det((t+1)I-M(t)).

We claim rho(M(t))>=sqrt(t)*a.
Choose a connected support component attaining a; on it M(t) is irreducible unless it is an isolated vertex, which cannot attain a>2.
Let u,v be strictly positive right eigenvectors of M(t),M(t)^T with the same Perron eigenvalue r_t.
Put w_i=sqrt(u_i v_i).
For every i, Cauchy--Schwarz gives

    sum_j sqrt(M_ij M_ji) w_j
       <= sqrt((sum_j M_ij u_j)(sum_j M_ji v_j))
       = r_t w_i.

The matrix on the left is sqrt(t) times the same A component.
A positive subeigenvector bounds its spectral radius above by r_t: after diagonal scaling by w, every row sum is at most r_t.
Hence r_t>=sqrt(t)*a, and the full M(t) has at least that spectral radius.
This proves the needed geometric-mean inequality directly; no equality case or irreducibility of the full support is assumed.

Define h(t)=t+1-rho(M(t)).
It is continuous.
The equation T+1=a sqrt(T) gives h(T)<=0 for T=T(a)>1.
On the other hand,

    rho(M(t))/t = rho(B+B^T/t) -> rho(B)=0

as t tends to infinity, since B is strictly upper triangular.
Thus h(t)>0 eventually.
The intermediate value theorem supplies t_0>=T with rho(M(t_0))=t_0+1, which makes the displayed determinant zero.
This is an actual positive real root of p_(V^-), whose contribution to logarithmic Mahler measure is at least log T.
The argument does not require h to be monotone or assert t_0 is the only root outside the unit circle.

In particular every positive-measure signed presentation has positive extra cover cost.
This resolves the specific zero-cost question left by the isolated neutral cycles.
It does not compare that cost with the original measure strongly enough to transfer a uniform gap, and reducing a chosen energy does not by itself control either quantity.

<a id="interacting-triangle-cost-family"></a>
### 2. An exact positive-measure family with independently removable frustrations

For every integer r>=1, use vertices 0,a_1,b_1,...,a_r,b_r in this order.
Let V_r be upper unitriangular with exactly the three entries

    V_(0,a_j)=V_(0,b_j)=V_(a_j,b_j)=1

for each j.
Its support consists of r triangles sharing the central vertex0, and each triangle is frustrated.
Its energy is E=3r.
Put F(t)=t^2+t+1 and s=t+1.

The full polynomial is

    p_(V_r)(t)=s F(t)^(r-1) [t^2+(1-r)t+1].                 (1)

To prove it, each leaf pair has block D=[[s,t],[1,s]] in tV+V^T, with determinant F.
Its coupling row from the central vertex is (t,t), and the reverse column is (1,1)^T.
The corresponding scalar Schur-complement contribution is t*s/F.
Summing the r disjoint branches gives

    F^r [s-r*t*s/F] = s F^(r-1)(F-r*t).

This rational-function computation proves a polynomial identity, including at the zeros of F, by multiplication of denominators.
It requires no approximate root computation.

For r=1,2,3 the final quadratic in (1) is cyclotomic (with a repeated root at r=3).
For r>=4 it has one root greater than one, its reciprocal, and no further roots.
Therefore

    m(p_(V_r))=arcosh((r-1)/2)>0  for r>=4.                (2)

The signed Gram threshold agrees exactly here.
Each leaf block [[2,1],[1,2]] is positive definite and its central Schur contribution is2/3.
The remaining scalar is2-2r/3.
Thus G is positive definite for r<3, positive semidefinite with one-dimensional kernel for r=3, and has exactly one negative direction for r>3.
This agreement is specific to this family; the general result above proves only the implication from positive measure to indefiniteness.

#### Partial exact mutations and the full cost at every step

Apply the forward adjacent mutation at the consecutive pair (a_j,b_j).
Its two by two basis block is [[0,1],[1,-1]].
The pair entry becomes -1, while the central coupling row (1,1) becomes (1,0).
All other branches are unchanged.
Hence each move replaces one triangle by a two-edge arm, lowers energy by exactly one, and preserves the complete signed polynomial by integral unimodular congruence.
Distinct branch moves commute because their basis blocks are disjoint and their external couplings do not introduce cross-branch edges.

Let V_(r,k) denote the matrix after any k distinct branch moves, 0<=k<=r.
It has energy3r-k and still has polynomial (1).
Its absolute negative presentation satisfies

    p_(V_(r,k)^-)(t)
      =s F(t)^(r-1) [t^2+(1-3r+2k)t+1].                 (3)

Indeed the leaf-pair absolute block is [[s,-t],[-1,s]], still of determinant F.
An unprocessed triangle has central coupling row(-t,-t), column(-1,-1)^T and Schur contribution3*t*s/F.
A processed arm has row(-t,0), column(-1,0)^T and contribution t*s/F.
Thus the total contribution is (3r-2k)*t*s/F, proving (3) for every subset of k branches and every r.

For r>=4 all these quadratics have a unique positive root greater than one.
The exact extra logarithmic cover cost at the k-th stage is

    m(p_(V_(r,k)^-))=arcosh((3r-2k-1)/2).                (4)

It strictly decreases at each step and at k=r equals the original measure in (2).
The final graph is the tree of r two-edge arms, so it is switchable; its signed and absolute polynomials coincide.
The doubled cover at that explicit endpoint has total logarithmic measure2*m(p_(V_r)).
This is an achieved cost ratio, not a proof of minimality among all congruent or stabilized representations.

This family shows a concrete interaction threshold: up to three individually neutral frustrated triangles together remain neutral, while four or more produce positive Mahler measure.
The independent local cancellations then remove every frustration without a temporary energy increase and track the complete extra cost, not merely a dominant eigenvalue or determinant value at one.
Its smallest positive measure is arcosh(3/2), so it is bounded away from zero and supplies no near-one family.

#### Sharpness of the spectral lower bound at the final tree

The adjacency spectral radius of the final r-arm tree is sqrt(r+1).
One positive Perron vector is obtained by assigning central value r, each middle vertex sqrt(r+1), and each outer vertex1: the adjacency equations all have eigenvalue sqrt(r+1).
Connectivity makes it the Perron value.
Therefore

    2 arcosh(sqrt(r+1)/2)=arcosh((r-1)/2),   r>=4.

The general lower bound from Section1 is attained at this endpoint.
The identity follows by cosh(2u)=2cosh(u)^2-1.
It establishes sharpness of that adjacency-dependent bound within positive-measure integral examples; it does not make energy a general measure-cost potential or prove a global optimized bound.

The comparison is strict before all triangles have been removed.
More explicitly, the adjacency characteristic polynomial after k moves is

    det(xI-A_(r,k))
      =(x^2-1)^(r-1) [x^3-(1+2r-k)x-2(r-k)].            (5)

The same leaf-pair Schur complement proves this: an unprocessed triangle contributes2/(x-1) to the central equation and a processed arm contributes x/(x^2-1).
For r>=4 the Perron value is the largest positive root of the cubic.
Put D=3r-2k+1, the number whose square root would make the Section1 lower bound equal the actual cost in (4).
The cubic evaluated at sqrt(D) is

    (r-k)(sqrt(D)-2).

For k<r this is positive since D>=r+1>=5, and the cubic has exactly one positive root by its signs.
Hence rho(A_(r,k))<sqrt(D), so the spectral lower bound is strictly smaller than the actual added measure at every such stage.
For k=r equality holds.
This supplies an explicit strict excess above the symmetric-adjacency bound; it is still an exact family calculation, not an inequality for every presentation.

## Exact original interpretation, review and native boundaries

The original negative interpretation finding retains the unsupported words ordering-sensitive excess and the reviewer's exact reason that this shared-triangle family's complete polynomials are order-independent.
The retained corrected mathematical sentence above states only the proved strict comparison with the symmetric-adjacency bound.
All formulas(1)--(5) and their proofs were found correct in the original review.
Its subsequent same-reviewer closure directly reread only that sentence, with the rest left at the earlier checked scope.
It is not a complete corrected-chain independent review.
The current whole authored check cannot close that separate original whole/after-correction independent-review obligation.

J32's complete author code uses a separately coded integer Bareiss determinant with row-pivot/sign and exact-division checks.
At n+1 distinct integer values it checks each degree-n signed/absolute/adjacency polynomial, with n=2r+1.
Its output retains all60input rows, the aggregate counts2148determinant checks and38reverse-order controls, and all8Gram-control records at the exact original finite domain.
The individual2148determinant values are checked by the retained code but are not separate saved output fields.
The coordinator separately reran that same author implementation into a disposable destination and matched every retained mathematical field.
It did not produce an independently written verifier.
No initial author run failed.
Current maintenance reads the entire code and every saved field without executing it or generating new outputs.
Original source comparison, prospective structural tests, exact contributions, original correction/closure, day precision and pending/adoption history remain in L185/R84/U001/J32.
No new source theorem, original-law probability result, optimized-cost proof, global minimality or research resumption occurs.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0032](../computations/programs/Yin_J_G0032/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.

---
author: Yin
---

# Complete matrix, length and support compression equivalences with exact neutral-padding bounds

This owns the complete original L27–L29 mathematical conversions, without turning a structural reformulation into a solution of the unrestricted gap.

## Statement

For each monic irreducible p in Z[t] with p(0)=+1 or−1 and M(p)>1, let c range over monic cyclotomic products, with repetitions and c=1 allowed.
Let S(p)=min_c support(pc), L(p)=min_c ||pc||_1, and E(p)=min_{A,c:chi_A=pc}(||A||_F^2−dim A) over integral unimodular A of arbitrary positive size.
All minima exist, S>=3, E>=1, and every admissible presentation has full entropy m(p).
For integer k>=1 put H(k)=k![(k+2)2^{2k−1}]^k.
Then E(p)<=L(p)^2−1, L(p)<=H(E(p)), L(p)<=4^{E(p)}, and S(p)<=L(p)<=S(p)2^{S(p)−2}M(p).
Thus on every family with M(p)<=B<infinity, bounded S, bounded L and bounded E are equivalent.
The 4^k bound arises from the actual characteristic polynomial of a single strongly connected block containing p, not from adding a determinant power.

The assertion that there exist B>1 and an integer K>=3 with L(p)<=K for every such p satisfying M(p)<B is equivalent to a positive unit-core Mahler gap.
The reverse direction is vacuous by choosing a window strictly below a given positive gap; it supplies no construction on a prescribed window.
For c with maximum root multiplicity r, extend L to pc by the same definition; then L(p)<=L(pc)<=2^r L(p), including r=0 for c=1.
Every nonzero multiple of p(t)(t−1)^n has at least n+1 terms, so appending factors to arbitrary neutral padding cannot guarantee a universal final coefficient-length bound at fixed positive measure.
A search that deletes padding or chooses a fresh completion is not excluded.
No uniform complexity bound, prescribed-window theorem or gap is proved.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:07 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible integral unit polynomial of positive Mahler measure, every cyclotomic product with repetitions, arbitrary-size integral presentations, bounded-measure families and exact existential near-one quantifiers; all minima and neutral-padding distinctions. |
| argument | [Argument](#argument) | Complete companion and active-cycle determinant conversions, exact H(E) coefficient norm, finite-support height estimate, both directions and vacuity of the existential gap equivalence, repeated/squarefree padding bounds, and the full strongly connected cofactor 4^E argument. |
| dependency | [Sparse matrix construction](Yin_C_G0229_v1.md#bounded-excess-gap) | Exact matching, active signed cycles and determinant polynomial, with integer excess and neutral factors. |
| dependency | [DS17 fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) | A positive total-log-Mahler gap for each fixed support bound, with no explicit numerical eta. |
| dependency | [DS17 sparse height](../audits/literature/DS17/Yin_U002.md#ds17-u002) | Original Theorem1 coefficient-height bound for actual support s>=2, monomial guard and uninspected original derivative-theorem limit. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:16 |
| status | proved |
| reason | The registered exact statement, every complete retained proof and necessary accepted interface have actual current whole self-review; all finite-parameter, conditional, exceptional and no-uniform-conclusion boundaries are preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible integral unit polynomial of positive Mahler measure, every cyclotomic product with repetitions, arbitrary-size integral presentations, bounded-measure families and exact existential near-one quantifiers; all minima and neutral-padding distinctions. |
| argument | [Argument](#argument) | Complete companion and active-cycle determinant conversions, exact H(E) coefficient norm, finite-support height estimate, both directions and vacuity of the existential gap equivalence, repeated/squarefree padding bounds, and the full strongly connected cofactor 4^E argument. |
| dependency | [Sparse matrix construction](Yin_C_G0229_v1.md#bounded-excess-gap) | Exact matching, active signed cycles and determinant polynomial, with integer excess and neutral factors. |
| dependency | [DS17 fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) | A positive total-log-Mahler gap for each fixed support bound, with no explicit numerical eta. |
| dependency | [DS17 sparse height](../audits/literature/DS17/Yin_U002.md#ds17-u002) | Original Theorem1 coefficient-height bound for actual support s>=2, monomial guard and uninspected original derivative-theorem limit. |
| review | [Actual whole self-review](../audits/reviews/Yin_R_G0516_v1.md#current-compression-finding) | Entire exact registered statement and full proof, all necessary dependencies and stated boundary cases; no isolated independent or research completion claim. |

## Argument

<a id="completion-invariants"></a>
### Two presentation invariants

Let p be monic irreducible in Z[t], p(0)=+1 or -1, and m(p)>0.
Products of cyclotomic polynomials below are monic, may have repetitions, and include 1.
Define

    L(p)=min_c ||p c||_1,
    E(p)=min_{A,c: det(tI-A)=p c} (||A||_F^2-dim A),

where A is any integral unimodular matrix of any size.
These minima exist in nonnegative integers: c=1 and the companion matrix of p give admissible examples.
E(p)>=1, since zero excess would force a signed permutation matrix by L G0025.
Every admissible matrix has entropy exactly m(p).

E permits replacement of the entire integral presentation and arbitrary cyclotomic characteristic factors.
It is not the conjugacy-and-stabilization invariant of a given flow in L G0026.
In particular it retains no prescribed neutral Jordan structure or prescribed integral lattice class.

<a id="boundedness-equivalence"></a>
### Quantitative equivalence

For k>=1 put

    H(k)=k! [(k+2) 2^{2k-1}]^k.

Then

    E(p) <= L(p)^2-1,       L(p) <= H(E(p)).

For the first inequality, choose q=p c attaining L(p) and take its standard companion matrix.
If q=t^d+sum_{i<d} a_i t^i, the excess is sum_{i<d} a_i^2-1, which is at most ||q||_1^2-1.
Its determinant is a unit since q(0)=+1 or -1.

For the second, take A attaining E(p)=k, and use the full construction of [L G0025](Yin_C_G0229_v1.md#bounded-excess-gap).
It writes A=P+E with s<=k nonzero perturbation entries whose absolute values sum to at most k.
There are r<=2s active signed cycles.
Let A_0 be the active block, D its signed-permutation characteristic polynomial, and

    B=D I_s-D V^T(tI-P_0)^{-1}U,
    F=det B=D^{s-1}det(tI-A_0).

The inactive cycles remove only cyclotomic factors from det(tI-A).
Thus p divides det(tI-A_0), and F=p c' with c' again a monic cyclotomic product.
This uses the fact that p is irreducible and noncyclotomic; inactive cycles cannot contain it.

Each entry of D V^T(tI-P_0)^{-1}U is one perturbation coefficient times a signed monomial and r-1 binomials.
Its coefficient l1 norm is at most k 2^{r-1}.
Also ||D||_1<=2^r.
Therefore each entry of B has coefficient l1 norm at most (k+2)2^{r-1}.
The coefficient norm is submultiplicative and satisfies the triangle inequality, so the determinant expansion gives

    ||F||_1 <= s! [(k+2)2^{r-1}]^s
             <= k! [(k+2)2^{2k-1}]^k = H(k).

The construction remains valid with coincident cycle lengths or cancellation; these can only improve the norm bounds.
Since F is an admissible cyclotomic completion, the second inequality follows.

Consequently, on any family of positive irreducible unit polynomials, uniform boundedness of E is equivalent to uniform boundedness of L.
This concerns boundedness across a family, not equality of the minima or preservation of an original flow under conjugacy.

<a id="three-complexities"></a>
### The coefficient estimate closes the third equivalence

Let p be a monic irreducible integral unit polynomial with M(p)>1.
Write S(p) for the least number of nonzero terms of p c over monic cyclotomic products c (repetitions and c=1 allowed).
Write L(p) for the least coefficient l1 norm of such a multiple, and E(p) for the minimum integral matrix excess over characteristic polynomials p c, as in [L G0027](#completion-invariants).

All minima exist.
S(p)>=3: a monic polynomial with unit constant term and at most two nonzero terms must be t^d+1 or t^d-1, or a constant unit, so it has zero Mahler measure.
A completion attaining S has M(pc)=M(p).
The [DS17 coefficient-height bound](../audits/literature/DS17/Yin_U002.md#ds17-u002) therefore gives

    S(p) <= L(p) <= S(p) 2^{S(p)-2} M(p).

The first inequality follows from integral nonzero coefficients having absolute value at least one; the second bounds the length of a support-minimizing completion by its support times its height.
Its completion need not minimize length.

Consequently, for any family with M(p)<=B<infinity, bounded S, bounded L and bounded E are equivalent, using the two bounds in L G0027.
In particular

    S(p)<=K  =>  L(p)<=K 2^{K-2} B.

This supplies the additional coefficient estimate deliberately left open in L G0027's final comparison.
It means that bounded support is not a separate weaker structural route on the bounded-measure core.
No uniform bound for any of these quantities is established.

<a id="near-one-quantifiers"></a>
### An existential near-one formulation is already equivalent to the gap

Consider the assertion that there exist B>1 and K<infinity such that L(p)<=K for every positive irreducible unit p with M(p)<B.
It implies a positive gap: each such p has a cyclotomic completion with at most K terms, so the accepted DS17 gap gives log M(p)>=eta_K; the remaining p have log M(p)>=log B.

Conversely, if the unit-core Lehmer gap holds with M(p)>=gamma>1, choose 1<B<gamma.
The asserted boundedness then holds vacuously, for example with K=3.
Thus the existential choice of the window does not constitute an easier intermediate problem.
The standard reduction to the unit core is the one already fixed in the Task; nonmonic or nonunit irreducible factors have measure at least 2.

A preassigned window, such as 1<M(p)<1.3, together with an actual construction on its inputs, is a more concrete structural target.
Neither implication above asserts that Lehmer alone proves a bound on this fixed window, nor that the bound is false.
The bounded source assessment found no proof or counterfamily for it.
Do not present the existential formulation as additional evidence for Lehmer.

<a id="neutral-multiplicity-screen"></a>
### Why monotonically appending neutral factors is not a uniform algorithm

Fix any positive irreducible unit p and put q_n=p(t)(t-1)^n.
Every nonzero polynomial multiple of q_n retains a root of multiplicity at least n at 1.
The Euler-derivative Vandermonde argument in [L G0026](Yin_C_G0229_v1.md#jordan-complexity-obstruction) forces at least n+1 nonzero terms, hence coefficient length at least n+1 for an integral multiple.
Therefore a procedure that starts from arbitrary neutral padding and only appends factors cannot guarantee a universal final length bound, even at fixed positive Mahler measure.
This obstruction does not apply to a search that discards padding or chooses a new completion of the original p.

For comparison, prescribed neutral padding with bounded multiplicity is controlled.
Extend L to monic unit polynomials by the same cyclotomic-multiple definition.
If c is a cyclotomic product whose maximum root multiplicity is r, then

    L(p) <= L(p c) <= 2^r L(p).

Indeed, choose q_0=p c_0 attaining L(p), and take N divisible by all root orders of c.
Then c divides (t^N-1)^r and the quotient is cyclotomic.
Multiplying p c by c_0(t^N-1)^r/c yields q_0(t^N-1)^r, of length at most 2^r L(p).
For c=1 take r=0.
In particular squarefree neutral padding costs at most a factor 2, regardless of its degree.
Neither this upper bound nor the multiplicity obstruction controls the positive irreducible core.

<a id="scc-length-bound"></a>
### Strongly connected block statement

Let A in GL_N(Z) have characteristic polynomial p c, where p is monic irreducible, M(p)>1, and c is a monic cyclotomic product.
Put k=||A||_F^2-N.
There is a diagonal block A_* after a simultaneous permutation making A block triangular such that

    det(tI-A_*)=p c_*,       ||det(tI-A_*)||_1 <= 4^k,

where c_* is cyclotomic.
In particular the invariants of L G0027 satisfy

    L(p) <= 4^{E(p)}.

Unlike its earlier determinant construction, this bound uses the block's actual characteristic polynomial without adding a power of the signed-cycle determinant.
Both polynomial degree and matrix dimension are unrestricted.

### Selecting one component

Choose the signed permutation P and integer perturbation E=A-P using a nonzero determinant matching as in [L G0025](Yin_C_G0229_v1.md#bounded-excess-gap).
Contract every signed cycle of P to a vertex; each nonzero E_ij supplies a directed edge from the column's cycle to the row's cycle.
Strongly connected components can be topologically ordered, giving the asserted block triangular form.
Each P cycle lies wholly in one diagonal block.
The chosen matching entries cannot be canceled in A: P used their signs and E has the remaining magnitude there.

Every diagonal block is integral unimodular, since their integer determinants multiply to det A=+1 or -1.
Their monic characteristic polynomials multiply to p c.
Unique factorization and multiplicity one of p imply that exactly one block contains p, with all its remaining factors cyclotomic.
Select it as A_*=P_*+E_*.

Let r be its number of signed cycles, s the number of nonzero E_* entries, and q=sum|E_* entries|.
If r>1, strong connectivity requires at least one outgoing perturbation edge from each cycle, so r<=s.
If r=1, the presence of p forces s>=1.
The matching inequality and the nonnegative excess of all diagonal blocks give

    r <= s <= q <= k_* := ||A_*||_F^2-dim(A_*) <= k.

Off-diagonal blocks contribute additional nonnegative squares to k, so they cannot invalidate the last inequality.

### Minors of signed cycles

Set C=tI-P_*.
Expand det(C-E_*) by subsets T of perturbation entries.
Only subsets occupying distinct rows and columns contribute; their terms are

    +/- (product_{e in T} c_e) det C[I_T^c,J_T^c].

There is no factorial factor: a chosen set of entries fixes the matching on its rows and columns; the remaining sum is exactly the indicated cofactor.

The cofactor vanishes unless remaining row and column counts agree separately in each P cycle.
On a full signed cycle of length l and sign product sigma, the full minor is t^l-sigma, with coefficient norm 2.
Every proper square minor is zero or a signed monomial.
For l>=2, the bipartite graph of tI-P_cycle is one alternating cycle.
Deleting a row and a column breaks it into paths and isolated vertices.
A forest has at most one perfect matching, since two distinct perfect matchings would have a cycle as their symmetric difference.
Thus its determinant is zero or one signed monomial.
When l=1 the only proper square minor is the empty minor, equal to 1.

It follows that every cofactor has coefficient norm at most 2^r.
Submultiplicativity and the triangle inequality imply

    ||det(tI-A_*)||_1
      <= 2^r sum_{T partial matching} product_{e in T}|c_e|
      <= 2^r product_e(1+|c_e|)
      <= 2^{r+q} <= 4^k,

using 1+a<=2^a for positive integers a.
Cancellation only improves the bound.
Since det(tI-A_*)=p c_*, it is an admissible completion, proving the claim.

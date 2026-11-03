---
author: Yin
---

# Cycle-counted presentation bounds and the complete reciprocal excess-two class

This owns the complete original L33 proof, including the exact exceptional boundary and all edge-index controls.

## Statement

For each monic irreducible integral unit p with M(p)>1, use the minima L(p),E(p) defined below over arbitrary cyclotomic completions and integral unimodular presentations.
Without reciprocity, L(p)<=2^{E(p)+1}, hence E(p)>=ceil(log_2 L(p))−1.
For every integral unimodular A with excess k, there is a monic integral q of exactly the same Mahler measure and coefficient length at most4^k; q=1 is allowed at zero entropy.

If p is additionally reciprocal, then E(p)>=2 and L(p)>=5; E(p)=2 implies L(p)=5.
Conversely any length-five completion other than t^{2n}+3t^n+1 or t^{2n}−3t^n+1 gives E(p)=2 by the explicit two-cycle construction.
Those exceptional polynomials have measure(3+sqrt5)/2, so throughout1<M(p)<(3+sqrt5)/2 one has E(p)=2 if and only if L(p)=5.
This includes the smaller accepted least-Pisot threshold class but asserts no exhaustive small-measure coverage or value at the exceptional boundary.
For the named standard irreducible Task control p_L=t^10+t^9−t^7−t^6−t^5−t^4−t^3+t+1, one has (t^2−t+1)p_L=t^12−t^7−t^6−t^5+1, and the explicit positive5/7 cycles give E(p_L)=2,L(p_L)=5.
The named control's established irreducibility scope is retained, rather than newly audited.
No uniform upper bound on E or L follows from small measure.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:09 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All positive-measure monic irreducible integral units without reciprocity for the cycle bound and all unimodular flows for its same-measure corollary; additionally reciprocal p for the exact E=2/L=5 class, with its strict exceptional Mahler threshold and stated Lehmer control. |
| argument | [Argument](#argument) | Complete labelled directed-cycle expansion, injective even-subset count and F2 incidence rank including N=1/loops/parallel/opposite edges; full reciprocal length<=4 classification, one/two-cycle rank-two formulas, length-five parity and explicit cross-arrow realization, exceptional boundary and exact control. |
| dependency | [Presentation definitions](Yin_C_G0233_v1.md#completion-invariants) | Exact L/E minima and admissible monic cyclotomic completions; no assumed uniform bound. |
| dependency | [Signed matching construction](Yin_C_G0229_v1.md#bounded-excess-gap) | Integer entry matching/excess and diagonal component determinant facts, without normality. |
| dependency | [Kronecker and named control](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Existing measure-one cyclotomic-product characterization and standard Lehmer control at recorded source statement scope; no fresh irreducibility or source-proof audit. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:16 |
| status | proved |
| reason | The registered exact statement, every complete retained proof and necessary accepted interface have actual current whole self-review; all finite-parameter, conditional, exceptional and no-uniform-conclusion boundaries are preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All positive-measure monic irreducible integral units without reciprocity for the cycle bound and all unimodular flows for its same-measure corollary; additionally reciprocal p for the exact E=2/L=5 class, with its strict exceptional Mahler threshold and stated Lehmer control. |
| argument | [Argument](#argument) | Complete labelled directed-cycle expansion, injective even-subset count and F2 incidence rank including N=1/loops/parallel/opposite edges; full reciprocal length<=4 classification, one/two-cycle rank-two formulas, length-five parity and explicit cross-arrow realization, exceptional boundary and exact control. |
| dependency | [Presentation definitions](Yin_C_G0233_v1.md#completion-invariants) | Exact L/E minima and admissible monic cyclotomic completions; no assumed uniform bound. |
| dependency | [Signed matching construction](Yin_C_G0229_v1.md#bounded-excess-gap) | Integer entry matching/excess and diagonal component determinant facts, without normality. |
| dependency | [Kronecker and named control](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Existing measure-one cyclotomic-product characterization and standard Lehmer control at recorded source statement scope; no fresh irreducibility or source-proof audit. |
| review | [Actual whole self-review](../audits/reviews/Yin_R_G0516_v1.md#current-cycle-excess-two-finding) | Entire exact registered statement and full proof, all necessary dependencies and stated boundary cases; no isolated independent or research completion claim. |

## Argument

### Definitions and statement

For a monic irreducible noncyclotomic unit polynomial p in Z[t], with p(0)=+1 or -1, retain [L G0027](Yin_C_G0233_v1.md#completion-invariants)'s definitions

    L(p)=min_c ||p c||_1,
    E(p)=min_{A,c: det(tI-A)=p c} (||A||_F^2-dim A),

where c ranges over monic cyclotomic products, allowing repetitions and c=1, and A ranges over integral unimodular matrices of arbitrary dimension.
These minima exist.
M denotes multiplicative Mahler measure and m=log M, without a dimension normalization.

Without a reciprocity assumption, the general bound is

    L(p)<=2^(E(p)+1).

For the remaining exact statements, assume additionally that p is reciprocal; then p(0)=1.
The following statements hold.

1. Always E(p)>=2 and L(p)>=5.
2. If E(p)=2, then L(p)=5.
3. If p has a cyclotomic completion of length 5 other than t^(2n)+3t^n+1 or t^(2n)-3t^n+1, then E(p)=2.

Consequently, on the class

    1<M(p)<(3+sqrt(5))/2,

one has the exact equivalence E(p)=2 if and only if L(p)=5.
In particular this holds throughout the smaller M<theta_0 core, where theta_0 is the least Pisot number.
The theorem does not assert that all small-measure p belong to this class of presentations.

The exact excess-two proof uses the signed-permutation matching construction of [L G0025](Yin_C_G0229_v1.md#bounded-excess-gap).
Neither proof uses DS17's positive gap or any theorem asserting bounded shortness.
The short reciprocal classification below is also the elementary assertion recorded as ESM25 Remark 2.1; its proof is included here, so no new source dependency is needed.

<a id="cycle-counting-bound"></a>
### General bound by counting cycle collections

Choose A attaining E(p)=k.
Decompose its directed graph into strongly connected components, orienting each nonzero matrix entry from its column to its row.
In component order A is block triangular.
Each diagonal block B_i is an integral unimodular matrix, because its determinant is an integer and the product of the block determinants is det A=+1 or -1.
Consequently

    k_i=||B_i||_F^2-dim B_i >=0.

The inequality follows directly from a nonzero determinant matching: each of its dim B_i selected entries has squared magnitude at least one.
Moreover

    k=sum_i k_i + sum of squares of the off-block entries.

The irreducible factor p occurs in exactly one block characteristic polynomial.
Select that block B, of dimension N, and put k_*=||B||_F^2-N.
Then k_*<=k and det(tI-B)=p c_* for a monic cyclotomic product c_*.
Its underlying undirected graph is connected.

Replace each entry B_ij by |B_ij| distinctly labelled directed edges from j to i, all with sign sign(B_ij).
A diagonal entry produces labelled loops.
The total number of edges is

    m_edges=sum_(i,j)|B_ij| <=sum_(i,j)B_ij^2=N+k_*.

The determinant expansion for det(tI-B) is a sum over collections of vertex-disjoint directed cycles, allowing loops and the empty collection.
Expanding every integer entry into its labelled signed edges makes each collection contribute a signed monomial with coefficient magnitude one.
This can be seen by first expanding over the principal submatrices of B, and then over the permutations on their selected vertices.
Parallel-edge choices account exactly for the magnitudes of the entries.
Hence

    ||det(tI-B)||_1 <= number of these labelled cycle collections.

Forget the orientation, but retain each edge's identity: opposite directed arrows remain two distinct undirected edges, and loops remain loops.
Every directed cycle collection gives an even-degree edge subset of this connected undirected multigraph; a loop contributes twice to the undirected degree.
This map is injective.
The edge labels retain their original directed orientations, so the chosen subset determines the directed collection uniquely whenever it is such a collection.
No claim that every even-degree subset is a directed cycle collection is needed.

Over F_2 the vertex-edge incidence matrix of this multigraph has rank N-1.
The entries of each column sum to zero, giving the upper bound N-1.
A spanning tree, ignoring loops, supplies N-1 independent columns, as follows by successively removing leaves.
For N=1 the incidence matrix has rank zero, which is the same formula.
The number of even-degree subsets, including the empty one, is consequently

    2^(m_edges-N+1).

Combining these estimates gives

    L(p)<=||det(tI-B)||_1
         <=2^(m_edges-N+1)<=2^(k_*+1)<=2^(E(p)+1).

Negative signs, parallel edges, antiparallel edges, diagonal loops, repeated powers of t, and cancellation of coefficients are all covered: signs and cancellation can only decrease the coefficient norm.
Selecting the single p-containing component is essential; counting cycles in all disconnected neutral blocks would introduce their number into the estimate.

This replaces L G0027's factorial-exponential upper conversion by a singly exponential bound.
In the reverse direction it gives the necessary integer lower bound

    E(p)>=ceil(log_2 L(p))-1.

It does not give an upper bound on E(p) from small Mahler measure and therefore does not close the Task.
The coordinator's bounded source search for strongly connected directed cycle collections, edges-minus-vertices bounds, and Mahler/Frobenius-excess connections found no exact theorem used here; no inference of novelty is made.
The incidence-rank and determinant arguments are proved above without a new external input.

<a id="whole-flow-cycle-corollary"></a>
### A direct consequence for a whole integral flow

For any A in GL_N(Z) of excess k, select all strongly connected diagonal blocks B_i whose characteristic polynomials have Mahler measure greater than one.
Their product q has M(q)=M(det(tI-A)), because the omitted monic integer unit polynomials have measure one and are cyclotomic.
If there are r selected blocks, each has k_i>=1: a zero-excess integral unimodular matrix is a signed permutation, whose characteristic polynomial is cyclotomic.
Thus r<=sum k_i<=k.
Applying the cycle count to each block, which did not require irreducibility of its characteristic polynomial, gives

    ||q||_1 <= 2^(sum k_i+r) <= 4^k.

When r=0 use q=1.
This is an elementary same-measure short polynomial for an arbitrary integral automorphism, sharpening the quantitative certificate of L G0025.
The assigned agent supplied the corollary and the coordinator checked its block selection, zero-excess case and product bound.
It does not reverse the entropy-to-complexity implication or remove the neutral Jordan obstruction of L G0026.

<a id="excess-two-equivalence"></a>
### Reciprocal length at most four

A monic integral polynomial q with constant coefficient e in {1,-1} is called reciprocal up to sign here when q*=e q.
Every cyclotomic completion of p has this property.
If q has length at most four, then q is cyclotomic.

To check this completely, its leading and constant coefficients already contribute two to the length.
When there is just one additional central term, the possibilities are

    t^(2a)+b t^a+1,  b in {-2,-1,0,1,2},

all cyclotomic, by the quadratic factorizations or the polynomials x^2+x+1 and x^2-x+1 evaluated at x=t^a.
An anti-reciprocal polynomial has zero central coefficient.
When there is an additional pair, reciprocity forces the polynomial to be one of

    t^d+u(t^a+t^(d-a))+1=(t^a+u)(t^(d-a)+u),
    t^d+u(t^a-t^(d-a))-1=(t^a-u)(t^(d-a)+u),

with u in {1,-1}; the overlapping central case was already covered.
With no additional terms the polynomial is t^d+e.
These exhaust the possibilities, and every displayed factor has roots of unity.
Hence a cyclotomic completion of noncyclotomic p has length at least five.

### What excess at most two permits

Let A have characteristic polynomial p c and excess k<=2.
Choose a nonzero matching in its determinant and the associated signed permutation P, as in L G0025.
On a matched entry, a magnitude at least 2 would contribute at least 2^2-1=3 to the excess.
Off the matching, a magnitude at least 2 would contribute at least 4.
Consequently every matched entry has magnitude one and there are exactly k off-matching entries, each equal to +1 or -1.
Thus A=P plus at most two signed matrix units in positions where P is zero.

Orient matrix entries as arrows from column to row.
Every signed permutation cycle lies entirely in one strongly connected component of this graph.
A component containing r>1 permutation cycles requires at least r intercycle arrows, so with at most two additional arrows it can contain only two cycles, and then the arrows go in opposite directions between them.
In component order A is block triangular.
Its component characteristic polynomials are monic integral and multiply to p c.
Exactly one component polynomial q_0 contains p; all its other irreducible factors are cyclotomic.
In particular q_0 is an admissible completion of p.
Its constant coefficient is a unit: the product of the integer block determinants is det A=+1 or -1.

There are two cases for this component.

### One permutation cycle

Write D=t^N-sigma, where sigma is the cycle sign product, and R=(tI-P)^{-1} on this cycle.
Each entry of D R is a signed monomial of degree between 0 and N-1.
With no perturbation, the component polynomial is D.
With one perturbation c_1 e_i e_j^T it is

    D-c_1 D R_(j,i),

and therefore has length at most three.

For two perturbations c_h e_(i_h)e_(j_h)^T, where c_h=+1 or -1, the rank-two determinant formula gives

    q_0=D-c_1 D R_(j_1,i_1)-c_2 D R_(j_2,i_2)
          +c_1 c_2 D [R_(j_1,i_1)R_(j_2,i_2)
                      -R_(j_1,i_2)R_(j_2,i_1)].

The bracketed contribution after multiplication by D is zero or a signed monomial.
Here is a justification that also covers shared row/column indices and coincident exponents.
It is W/D, where W is a difference of two signed monomials of degrees at most 2N-2.
The entire determinant and its first three displayed summands are polynomials, so D divides W.
If the monomials cancel, the contribution is zero.
Otherwise a nonzero binomial divisible by t^N-sigma must have exponent difference a positive multiple of N and matching signs after reduction modulo D.
The degree range permits only difference N, making W/D a signed monomial.
A single nonzero monomial, including a coefficient of magnitude 2 after merging exponents, cannot be divisible by D.
It follows that ||q_0||_1<=2+1+1+1=5.

### Two permutation cycles

Both perturbations are intercycle arrows in opposite directions.
Put D_1=t^l-sigma_1 and D_2=t^m-sigma_2.
In the rank-two determinant formula the two linear perturbation terms vanish, because the unperturbed resolvent is block diagonal.
The mixed term is a signed monomial: its two resolvent denominators D_1 and D_2 cancel against det(tI-P)=D_1 D_2.
Thus

    q_0=(t^l-sigma_1)(t^m-sigma_2) +/- t^b

for some nonnegative integer b, and again ||q_0||_1<=5.
Exponent coincidences or cancellation can only decrease this bound.
The determinant-unit condition is inherited from A; it need not be inferred from an arbitrary choice of b and signs.

This proves L(p)<=5 when k<=2.
For k=0 all components are cyclotomic.
For k=1 the component containing p, if it existed, would have length at most three and be reciprocal up to sign, contradicting the preceding classification.
Hence E(p)>=2.
If E(p)=2, the bounds L(p)>=5 and L(p)<=5 give equality.

### Explicit realization of a length-five completion

Let q=p c have length five.
Its constant coefficient cannot be -1: anti-reciprocal coefficients occur in opposite pairs, giving even length.
A reciprocal polynomial of odd degree also has even length.
Thus q has even degree 2n and constant coefficient 1.
Its leading and constant terms account for two units of length, leaving either one central coefficient of magnitude three, or a symmetric pair of unit coefficients and one central unit coefficient.
Apart from the former exceptional shape, q therefore has the form

    q=t^(2n)+epsilon(t^(n+a)+t^(n-a))+delta t^n+1,
    1<=a<n,  epsilon,delta in {1,-1}.

In particular n>=2.
Set l=n-a, m=n+a, and sigma=-epsilon.
Take two disjoint signed cycles, on vertices u_0,...,u_(l-1) and v_0,...,v_(m-1).
Their forward arrows have weight +1, except that the last arrow returning to vertex 0 in each cycle has weight sigma.
Their characteristic polynomial is

    (t^l-sigma)(t^m-sigma)
       =t^(2n)+epsilon(t^l+t^m)+1.

Add the two cross arrows

    u_(l-1) -> v_0       with weight +1,
    v_(a-1) -> u_0       with weight -delta.

These are distinct off-matching positions, including when l=1 or a=1.
The new directed cycle uses all l vertices of the first cycle and the first a vertices of the second.
Its length is l+a=n, and its weight is -delta.
A directed cycle containing only one of the cross arrows cannot close; the cycle using both is unique.
In the determinant expansion its contribution is therefore delta t^(2n-n)=delta t^n, so the resulting matrix has characteristic polynomial exactly q.
Equivalently the same expression follows from the two-cycle rank-two determinant formula above.

This matrix is integral and has exactly 2n+2 entries of magnitude one, hence excess two.
Its determinant is 1 because q has even degree and constant coefficient 1.
It is therefore admissible for E(p), proving E(p)<=2 and hence E(p)=2.

For the exceptional shape q=t^(2n)+/-3t^n+1, substitution x=t^n preserves multiplicative Mahler measure, and direct solution of x^2+/-3x+1 gives

    M(q)=(3+sqrt(5))/2.

Since q/p is cyclotomic, this equals M(p).
Thus the exceptional case is excluded under the theorem's strict upper bound.
No assertion about E(p) at that boundary is needed.

<a id="lehmer-two-cycle-realization"></a>
### Lehmer control and strategic consequence

For the Task's standard irreducible Lehmer polynomial

    p_L=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,

direct multiplication gives

    (t^2-t+1)p_L=t^12-t^7-t^6-t^5+1.

The completion has n=6, a=1, epsilon=delta=-1.
The construction uses ordinary positive cycles of lengths 5 and 7, and positive cross arrows u_4 -> v_0 and v_0 -> u_0.
Thus E(p_L)=2 and L(p_L)=5.
The multiplication and matrix construction are exact symbolic checks; no numerical experiment was performed.
Irreducibility of the named Task control is retained at its existing scope, rather than newly audited here.

The general cycle count improves the conversion for all positive irreducible units, and the exact theorem identifies the first possible complexity level on the reciprocal positive core with an established shortness class.
It also gives an explicit two-cycle realization.
Neither conclusion shows that every sufficiently small positive measure has E=2 or L=5.
Polynomials with higher cyclotomic shortness remain outside that realization, and no uniform bound over all levels follows.
Existing length-five source enumeration or fixed-support gap results retain their own separate hypotheses and audit scope.

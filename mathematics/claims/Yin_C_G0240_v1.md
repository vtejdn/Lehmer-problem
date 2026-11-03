---
author: Yin
---

# Finite neutral net-trace repair and singular-safe primitive graph complexity

This retains the full original2026-10-07 existence and graph proofs without promoting the source realization theorem to a uniform complexity estimate.

## Statement

Let p be monic irreducible in Z[t], p(0)=±1 and M(p)>1; a monic cyclotomic product may have repetitions and includes1.
The roots of p have a unique positive strictly dominant lambda>1 if and only if a primitive nonnegative integer matrix A, z>=0 and cyclotomic c satisfy det(tI−A)=t^z p c.
Every such realization has full algebraic entropy m(p), with no prescribed dimension, Jordan structure, integral conjugacy, lattice or graph complexity.
Writing s_n=sum alpha_i^n, T_n=sum_(j divides n)mu(n/j)s_j and b_n=T_n/n, the b_n are integers, eventually positive, and finitely many cycle factors c=product(t^n−1)^max(0,−b_n) make all b_n(p c)>=0 without creating new negative indices.
The positive cutoff and total repair cost depend on p; zero padding is permitted by the accepted integer-spectrum theorem.
For any nonnegative integer N-by-N matrix whose underlying undirected graph is connected, M=sum A_ij, e=M−N, one has norm_1(det(tI−A))<=2^(e+1), including singular matrices.
A primitive realization thus gives L(p)<=2^(e+1); bounded e is a sufficient restricted-gap condition but is not supplied by this construction.
The explicit two/three-cycle control is primitive and singular, with characteristic polynomial t(t^3−t−1), and shows why a nonzero determinant matching or deletion of zero primary parts cannot be assumed.
No uniform repair support, zero multiplicity, dimension/edge-excess bound, general-unit realization, or Lehmer gap is proved.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:40 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible integral unit p with M(p)>1, exact Perron-versus-primitive equivalence with cyclotomic and zero padding, all finite net traces, arbitrary connected nonnegative integer matrices including singular controls, and the full missing-uniform-complexity boundary. |
| argument | [Argument](#argument) | Complete integral formal Euler-product and Mobius inversion, parameter-dependent eventual positivity, exact uncascaded cycle repair, accepted-source hypothesis check, parallel-edge bipartite matching injection, singular six-step primitive control and coefficient-length consequence. |
| dependency | [Primitive integer spectrum source](../audits/literature/KOR00/Yin_U001.md#kor00-u001) | MainTheorem2.2 at its original published-text statement/applicability depth, with nonnegative net traces and permitted additional zero eigenvalues; original sufficiency proof remains external. |
| dependency | [Integral entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Accepted formula including singular endomorphisms; added zero and cyclotomic roots have zero logarithmic Mahler measure. |
| dependency | [Rational hull scope](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Existing rational-hull convention and singular endomorphism boundary only. |
| dependency | [Completion length](Yin_C_G0233_v1.md#completion-invariants) | Minimum over monic cyclotomic products, with repetitions; no zero-free realization or conjugacy claim. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:44 |
| status | proved |
| reason | The complete exact current statement and retained argument were actually checked in the selected whole self finding; source depths, counterexamples and nonclaims remain explicit. This adoption does not complete any Task or certify an independent relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible integral unit p with M(p)>1, exact Perron-versus-primitive equivalence with cyclotomic and zero padding, all finite net traces, arbitrary connected nonnegative integer matrices including singular controls, and the full missing-uniform-complexity boundary. |
| argument | [Argument](#argument) | Complete integral formal Euler-product and Mobius inversion, parameter-dependent eventual positivity, exact uncascaded cycle repair, accepted-source hypothesis check, parallel-edge bipartite matching injection, singular six-step primitive control and coefficient-length consequence. |
| review | [Actual complete current finding](../audits/reviews/Yin_R_G0518_v1.md#current-primitive-graph-finding) | Complete current statement and argument at the exact selected scopes; actual self-review. |
| dependency | [Primitive integer spectrum source](../audits/literature/KOR00/Yin_U001.md#kor00-u001) | MainTheorem2.2 at its original published-text statement/applicability depth, with nonnegative net traces and permitted additional zero eigenvalues; original sufficiency proof remains external. |
| dependency | [Integral entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Accepted formula including singular endomorphisms; added zero and cyclotomic roots have zero logarithmic Mahler measure. |
| dependency | [Rational hull scope](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Existing rational-hull convention and singular endomorphism boundary only. |
| dependency | [Completion length](Yin_C_G0233_v1.md#completion-invariants) | Minimum over monic cyclotomic products, with repetitions; no zero-free realization or conjugacy claim. |

## Argument

<a id="perron-neutral-realization"></a>
### Exact existence statement

The following are equivalent:

1. The roots of p have a positive root lambda>1 whose modulus strictly exceeds that of every other root.
2. There are a primitive nonnegative integer matrix A, an integer z>=0, and a cyclotomic product c such that

       det(tI-A)=t^z p(t)c(t).

Every such realization has algebraic entropy m(p), since both the added zero roots and cyclotomic roots have zero logarithmic Mahler measure.
No prescribed dimension, integral conjugacy, lattice class, Jordan structure, or graph complexity is retained.

Necessity follows from the Perron-Frobenius property of a primitive matrix.
Since M(p)>1, the full spectrum has radius greater than one; the added roots have modulus at most one, so the positive simple dominant root must belong to p.
The proof of sufficiency follows.
This restricts the construction to the Perron unit class, which includes positive Salem polynomials.
A general positive-Mahler unit need not have this spectral property.

<a id="finite-nettrace-repair"></a>
### Finite repair of all negative primitive-orbit counts

Let alpha_1=lambda,alpha_2,...,alpha_d be the roots of p.
For n>=1 define

    s_n=sum_i alpha_i^n,
    T_n=sum_(j|n) mu(n/j)s_j,
    b_n=T_n/n.

Here T_n is the net trace; b_n is the normalized count that would enumerate primitive length-n orbits in a nonnegative graph realization.
They are distinct quantities, and before realization b_n can be negative.

The numbers b_n are integers.
To see this directly, put

    F(u)=u^d p(1/u)=product_i(1-alpha_i u) in 1+u Z[u].

There is a unique formal factorization

    F(u)=product_(n>=1)(1-u^n)^(b_n)

with integer exponents.
Recursively, if the quotient after removing factors of degrees less than n is 1+a u^n+O(u^(n+1)), choose the next exponent to be -a.
Integer powers, including negative powers, have integral formal coefficients.
Every coefficient of the infinite product depends on finitely many factors.
Taking formal logarithmic derivatives yields

    s_m=sum_(n|m)n b_n,

and Mobius inversion identifies these exponents with the displayed T_n/n.
Thus no divisibility assumption was silently added.

Put rho=max_(i>=2)|alpha_i|<lambda.
For n>=2 the dominant root and the proper-divisor estimates give

    T_n >= lambda^n-(d-1)rho^n-n d lambda^(n/2).

Indeed s_n differs from lambda^n by at most (d-1)rho^n; each proper divisor j of n is at most n/2 and |s_j|<=d lambda^j, and there are at most n such divisors.
Both error terms are o(lambda^n), so b_n>0 for every sufficiently large n.
The cutoff is allowed to depend on the entire polynomial; no parameter-uniform cutoff is proved.

Choose the finitely supported nonnegative integer sequence

    a_n=max(0,-b_n),       c(t)=product_n(t^n-1)^(a_n).

The roots of t^n-1 contribute n to s_m when n divides m and zero otherwise.
Mobius inversion therefore gives a contribution of exactly one to b_n, and zero to every b_m with m!=n.
Equivalently, its reciprocal polynomial is 1-u^n, one factor in the formal product.
Consequently

    b_m(p c)=b_m(p)+a_m>=0 for every m>=1.

There is no cascade of new negative net traces at multiples of a repaired index.
Ordinary traces do change at those multiples, which is why fixing ordinary traces and fixing primitive-orbit counts must not be confused.

The roots of p c are nonzero; their characteristic polynomial is monic integral; lambda>1 remains the unique positive strictly dominant root; and their net traces m b_m(p c) are nonnegative for every m.
The accepted realization theorem now supplies A and z, proving sufficiency.

This gives existence for each Perron unit polynomial.
It supplies no bound on the support of the repair sequence, on sum n a_n, on the zero multiplicity z, or on the size or edge count of A.
The Perron logarithm log(lambda) equals m(p) in the one-expanding-conjugate case; with further expanding conjugates it is smaller than the total algebraic entropy.
These quantities must not be interchanged in a graph-growth argument.

<a id="graph-excess-length-bound"></a>
### A coefficient bound that tolerates singular matrices

Let A be a nonnegative integer N by N matrix whose underlying undirected graph is connected.
Count its parallel directed edges with multiplicity:

    M=sum_(i,j) A_ij,       e=M-N.

Then

    ||det(tI-A)||_1 <= 2^(e+1).                         (1)

For a primitive matrix every row has positive integer sum, so e>=0.
The argument itself does not require A to be nonsingular or to possess a nonzero permutation term in det A.

Construct a bipartite multigraph with N row vertices and N column vertices.
At each diagonal position put one distinguished edge of weight t.
At position (i,j) also put A_ij separately labelled edges of weight -1.
Thus a diagonal entry with loops is represented by its distinguished t-edge and the additional negative edges, not by a single combined weight.

Perfect matchings index the expanded determinant terms: each matching contributes a signed monomial in t.
The graph has N+M edges and 2N vertices.
It is connected because contracting all distinguished diagonal edges yields the connected underlying graph of A.
Its cycle space over F_2 therefore has dimension

    (N+M)-2N+1=e+1.

This elementary dimension formula follows by choosing a spanning tree: each non-tree edge supplies one independent fundamental cycle, and they generate every even-degree edge set.

The distinguished t-edges form a perfect matching M_0.
For any perfect matching M_1, its symmetric difference M_1 triangle M_0 is an even-degree edge set, hence an element of that cycle space.
The map is injective because M_0 is fixed.
There are at most 2^(e+1) perfect matchings.
Summing the absolute values of their monomial contributions proves (1); cancellations only improve the bound.
Parallel edges, including the two-edge cycles they can create, are retained throughout this argument.

Apply (1) to any realization in the existence statement.
Removing the monomial factor t^z leaves the coefficient norm unchanged, so the invariant of [L G0027](Yin_C_G0233_v1.md#completion-invariants) satisfies

    L(p) <= ||p c||_1=||det(tI-A)||_1 <= 2^(e+1).       (2)

Thus uniformly bounded edge excess in this class of primitive realizations would imply the existing bounded-length Mahler gap.
Equivalently every such realization must have e>=log_2 L(p)-1.
This is a necessary complexity lower bound and a sufficient restricted-gap criterion; it is not a converse construction with bounded e.
The realization theorem does not supply that missing estimate.

<a id="singular-matching-control"></a>
### Exact control for the zero-padding boundary

Consider the directed graph formed by a length-two cycle and a length-three cycle sharing exactly one vertex.
With the shared vertex first, its adjacency matrix is

    A=[[0,1,1,0],
       [1,0,0,0],
       [0,0,0,1],
       [1,0,0,0]].

It has N=4, M=5, and e=1.
Its only simple directed cycles are the two stated cycles, which cannot occur together in a disjoint cycle cover.
The determinant expansion therefore gives

    det(tI-A)=t^4-t^2-t=t(t^3-t-1).

The matrix is primitive: each vertex reaches the shared vertex in at most two steps and is reached from it in at most two steps.
For any ordered pair, choose those two paths; the remaining length needed to make a walk of length six is at least two, and every integer at least two is a nonnegative combination of two and three.
Insert the corresponding cycles at the shared vertex.
Thus A^6 is strictly positive.

Nevertheless its second and fourth rows have their only nonzero entry in the same first column.
There is no nonzero permutation term in det A.
This explicitly prevents importing the determinant-matching step of [L G0025](Yin_C_G0229_v1.md#bounded-excess-gap) just from primitivity or from nonnegative edge excess.
Bound (1) applies without that step and gives the valid estimate 3<=4.

This example does not show that a zero-free realization of the same nonzero spectrum is impossible: t^3-t-1 also has a nonnegative companion matrix.
The general point is that neither the accepted existence theorem nor an arbitrary realizing graph authorizes deleting the zero primary component while preserving entrywise nonnegativity.
No such deletion theorem is assumed.

---
author: Yin
---

# Uniform cyclotomic and repair bounds for the primitive scaled-plastic family

This retains the complete2026-10-07 fixed-support argument; graph size and zero padding do not replace the actual whole-spectrum repair calculation.

## Statement

For every integerN>=2,g>=1,gcd(N,g)=1, q=t^N((t^g)^3−t^g−1)+(1−(t^g)^2−(t^g)^3) has the full stated primitive positive graphs with edge excess3; every cyclotomic order lies in O={1,2,3,4,5,6,8,9,10,12,15,18,24,30,36}, each multiplicity<=5. For the whole noncyclotomic quotient F, degree(c)<=360, R*(F)<=360, D(F)<=1055 and all negative original Euler indices<=36. The sole noncyclotomic irreducible-core consequences include strict Perron/all-power degree preservation but no unconditional small Mahler bound or factorwise repair claim.

## Current assessment
[Selected decision](#decision-complete-retained-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:26 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | For every integerN>=2,g>=1,gcd(N,g)=1, q=t^N((t^g)^3−t^g−1)+(1−(t^g)^2−(t^g)^3) has the full stated primitive positive graphs with edge excess3; every cyclotomic order lies in O={1,2,3,4,5,6,8,9,10,12,15,18,24,30,36}, each multiplicity<=5. For the whole noncyclotomic quotient F, degree(c)<=360, R*(F)<=360, D(F)<=1055 and all negative original Euler indices<=36. The sole noncyclotomic irreducible-core consequences include strict Perron/all-power degree preservation but no unconditional small Mahler bound or factorwise repair claim. |
| argument | [Argument](#argument) | Complete three-vertex delayed return graph and no-zero length-six graph, primitive return-length gcd includingN2/g1, exhaustive rank-one/rank-two minimal-relation lattice proof for the fixed six-point support, bounded index<=6 and orders, all multiplicities via sparse Euler/Vandermonde, exact totient/positive-Mobius sums72/211 and whole-polynomial cost bounds; no empirical parameter scan or new external theorem is used. |
| dependency | [Minimal unit relations](Yin_C_G0262_v2.md#argument) | Relative-order bounds for each actual rational minimal component. |
| dependency | [Positive length-six realization](Yin_C_G0269_v1.md#positive-length-six-graph) | Exact no-zero primitive reciprocal graph and actual edge-excess count. |
| dependency | [Repair budget](Yin_C_G0249_v1.md#argument) | Full-polynomial Euler coordinates, canonical D and unrestricted all-order R*. |

### Decision complete-retained-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:39 |
| status | proved |
| reason | Actual complete statement-and-argument self-check recorded at its real current date; historical findings remain at their actual scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | For every integerN>=2,g>=1,gcd(N,g)=1, q=t^N((t^g)^3−t^g−1)+(1−(t^g)^2−(t^g)^3) has the full stated primitive positive graphs with edge excess3; every cyclotomic order lies in O={1,2,3,4,5,6,8,9,10,12,15,18,24,30,36}, each multiplicity<=5. For the whole noncyclotomic quotient F, degree(c)<=360, R*(F)<=360, D(F)<=1055 and all negative original Euler indices<=36. The sole noncyclotomic irreducible-core consequences include strict Perron/all-power degree preservation but no unconditional small Mahler bound or factorwise repair claim. |
| argument | [Complete argument](#argument) | Complete three-vertex delayed return graph and no-zero length-six graph, primitive return-length gcd includingN2/g1, exhaustive rank-one/rank-two minimal-relation lattice proof for the fixed six-point support, bounded index<=6 and orders, all multiplicities via sparse Euler/Vandermonde, exact totient/positive-Mobius sums72/211 and whole-polynomial cost bounds; no empirical parameter scan or new external theorem is used. |
| dependency | [Minimal unit relations](Yin_C_G0262_v2.md#argument) | Relative-order bounds for each actual rational minimal component. |
| dependency | [Positive length-six realization](Yin_C_G0269_v1.md#positive-length-six-graph) | Exact no-zero primitive reciprocal graph and actual edge-excess count. |
| dependency | [Repair budget](Yin_C_G0249_v1.md#argument) | Full-polynomial Euler coordinates, canonical D and unrestricted all-order R*. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0532_v1.md#current-complete-scaled-plastic-finding) | Complete exact current statement and proof, with every quantifier, boundary and external/native limit specified in this finding; constructor self-review, with no retrospective isolation or Task advancement. |

## Argument

<a id="scaled-plastic-repair-bound"></a>
### Question and result

The attempted family replaces the plastic core in [L G0038](Yin_C_G0248_v1.md) by long subdivided paths, while a coprime additional delay makes the entire positive graph primitive.
This is a possible way to avoid the failure of plain substitution to preserve the degree of every power.
The question is whether this construction can force unbounded canonical or optimized cyclotomic repair for an irreducible reciprocal Perron core of small Mahler measure.

Put

    f(X)=X^3-X-1,           h(X)=1-X^2-X^3,
    q_(N,g)(t)=t^N f(t^g)+h(t^g)
             =t^(N+3g)-t^(N+g)-t^N+1-t^(2g)-t^(3g),            (1)

where N>=2, g>=1, and gcd(N,g)=1.
Let c be the entire monic cyclotomic part of q, including multiplicities, and put F=q/c.
The small-Mahler threshold theta_0 denotes the unique positive root of X^3-X-1, the plastic number.
The following conclusions hold for every such pair (N,g):

1. There is an explicit primitive nonnegative integer matrix A with N+4g-1 vertices, N+4g+2 edges, and chi_A(t)=t^(g-1)q(t).
   Its actual edge excess is three.
   The general reciprocal length-six graph lemma cited below also supplies a primitive unimodular matrix with characteristic polynomial exactly q, dimension N+3g, and edge excess three.
2. Every cyclotomic order of q belongs to the candidate set

       O={1,2,3,4,5,6,8,9,10,12,15,18,24,30,36}.             (2)

   Each cyclotomic factor has multiplicity at most five.
   Consequently deg c<=360.
   The set O is an upper bound, not an exact classification of the factors occurring for each parameter pair.
3. For the whole noncyclotomic quotient F, the canonical repair degree D(F) and least cyclotomic repair degree R_*(F) satisfy

       D(F)<=1055,                 R_*(F)<=360.                (3)

   Every negative normalized net trace of F has index at most 36.
4. If F is irreducible, it is a reciprocal Perron unit polynomial p, and its positive Perron root lambda satisfies Q(lambda^r)=Q(lambda) for every integer r>=1.
   The bounds (3) therefore apply to every eligible small-Mahler core in this family, without needing to assume a bound on its Mahler measure in the proof.

No assertion is made that F is irreducible for every pair, or that all these polynomials have Mahler measure below theta_0.
If F has several noncyclotomic irreducible factors, (3) concerns their whole product: discarding all but one of them does not give a cyclotomic completion of that selected factor.
In particular this theorem cannot turn such a factor selection into a counterexample in the prescribed irreducible core scope.

<a id="scaled-plastic-graph"></a>
### The explicit primitive graph, including zero padding

Begin with three vertices a_0,a_1,a_2 and the four arrows

    a_0 -> a_1,    a_1 -> a_2,    a_2 -> a_0,    a_2 -> a_1.

Replace each arrow by a separate directed path of length g, giving all four paths fresh, mutually disjoint internal vertices.
This core has 4g-1 vertices and 4g edges.
Its two simple directed cycles have lengths 2g and 3g; they intersect, so they cannot occur together in a disjoint cycle collection.

Add a disjoint directed N-cycle b_0,...,b_(N-1), with indices read modulo N, and add exactly the two cross arrows

    b_(N-2) -> a_2,                 a_1 -> b_0.                (4)

The choice N-2 in (4) is part of the construction.
The path from b_0 to b_(N-2) along the N-cycle has N-2 edges, including zero edges when N=2.
A mixed simple cycle uses both cross arrows and one of the two simple core paths from a_2 to a_1, whose lengths are g and 2g.
Thus the mixed cycles have lengths N+g and N+2g.
These are the only mixed simple cycles: continuing once around either the core or the N-cycle before leaving repeats a vertex.
Each mixed cycle intersects both core cycles and the N-cycle.
The only pairs of disjoint simple cycles are consequently the N-cycle with either one of the core cycles.

The directed cycle expansion of the determinant gives

    det(I-uA)
      =(1-u^(2g)-u^(3g))(1-u^N)-u^(N+g)-u^(N+2g)
      =1-u^(2g)-u^(3g)-u^N-u^(N+g)+u^(N+3g).                 (5)

This expansion remains valid when distinct cycles have the same length; their contributions simply add.
Counting the vertices and edges gives

    v=N+4g-1,             e_edges=N+4g+2,
    e_edges-v=3,          chi_A(t)=t^(g-1)q_(N,g)(t).         (6)

The graph is strongly connected.
Its core cycles and its N-cycle show that the greatest common divisor of all cycle lengths divides gcd(2g,3g,N)=1.
Hence A is primitive.
Its Perron root is strictly larger in modulus than every other eigenvalue and occurs simply.
Since q(1)=-2 and q is monic, q has a positive real root greater than one; the Perron root is therefore greater than one.

The polynomial q is monic reciprocal with constant coefficient one.
Every negative term in (1) has exponent strictly between zero and N+3g, so coincidences among these exponents only add negative coefficients.
Its coefficient length is exactly six and it has at most six distinct monomials.
For g>1 the matrix in (6) is singular: the g-1 zero roots are explicit.
They change neither Mahler measure nor any positive power trace.
This is an actual edge-excess-three presentation; no equality for minimum Frobenius excess, no unimodularity of A, and no minimality of the displayed edge excess is asserted.

There is also a realization without zero padding.
The complete retained general graph lemma in [L G0048](Yin_C_G0269_v1.md#positive-length-six-graph) applies with

    D=N+3g,    u=min(N,3g),    v=min(2g,N+g),
    a=min(u,v),                b=max(u,v).

Then q=t^D+1-t^a-t^(D-a)-t^b-t^(D-b), with 1<=a<=b<=D/2 and b>=2.
Also gcd(D,a,b)=gcd(N,g)=1: taking reciprocal complements preserves the exponent gcd, and the original support generates the same subgroup of Z as N,2g,3g.
That lemma constructs a primitive nonnegative integral unimodular matrix U of dimension D and edge excess three with chi_U=q.
Its graph uses two disjoint cycles of lengths a and D-a, one cross arrow and two return arrows; coincident returns are counted with multiplicity.
Thus in the sole-core case the bound deg c<=360 below supplies an actual edge-excess-three realization of dimension at most deg p+360, with no zeros.
This application uses the exact proved graph interface and does not identify its Frobenius excess with its edge excess in the parallel-arrow case.

<a id="rank-two-cyclotomic-bound"></a>
### A rank-two bound on all cyclotomic orders

The sole relative-order input is the complete rational-coefficient minimal-relation proof in [L G0044](Yin_C_G0262_v2.md#minimal-vanishing-order): in a minimal relation of k nonzero rational multiples of roots of unity, the order of every ratio of the roots divides P_k, the product of the primes at most k.
Repeated roots are permitted.
We apply that proved local lemma, not an uninspected original-source proof.

Suppose zeta has exact order m and q(zeta)=0.
Use the six displayed terms in (1), with their signs as rational coefficients.
Their formal support vectors, in coordinates multiplying (N,g), are

    (1,3), (1,1), (1,0), (0,0), (0,2), (0,3),               (7)

with respective coefficients +1,-1,-1,+1,-1,-1.
These six formal vectors are distinct even when some actual powers of zeta coincide.
Partition the six terms into minimal nonempty vanishing blocks.
Every block has at least two terms.
Let ell be the largest block size, and let Lambda be the subgroup of Z^2 generated by all differences of support vectors within individual blocks.
The relative-order lemma implies, for every v in Lambda,

    m divides P_ell (v_1 N+v_2 g).                           (8)

Indeed this first holds for each generator, using the lemma for its block and P_(block size) dividing P_ell; it then holds for every integer linear combination.

We show that Lambda has rank two.
It has positive rank because a block contains at least two distinct formal support vectors.
If its rank were one with all first-coordinate differences zero, every block would lie in one of the two columns of (7).
Each column has exactly three points.
Because no singleton can vanish, each column would have to be one complete block.
On putting X=zeta^g, their two vanishing sums would give

    f(X)=0,                    h(X)=0.

But f(X)+h(X)=-X(X+1); X is nonzero, so X=-1, whereas f(-1)=-1.
This is impossible.

If rank one has nonzero first-coordinate direction, a line parallel to that direction meets either column in at most one point.
Each block must therefore be a pair joining the two columns.
Orient each pair from first coordinate zero to first coordinate one.
All three pair differences have first coordinate one and lie on the same line, so they have the same integer second coordinate delta.
This would give a translate equality

    {0,1,3}={0,2,3}+delta.

Taking sums gives 4=5+3 delta, impossible for integer delta.
This excludes rank one in every direction.

Let d=[Z^2:Lambda].
Choose two independent generating differences.
Each has first coordinate in {-1,0,1} and second coordinate in [-3,3], so their determinant has absolute value at most six.
Their generated sublattice is contained in Lambda; hence d divides this nonzero determinant and

    1<=d<=6.                                                 (9)

The finite group Z^2/Lambda has order d, so d Z^2 is contained in Lambda.
Formula (8), applied to (d,0) and (0,d), gives divisibility of both P_ell dN and P_ell dg by m.
Bezout's identity and gcd(N,g)=1 therefore imply

    m divides P_ell d.                                     (10)

There is a useful improvement over applying P_6 uniformly.
If the entire six-term relation is minimal, the differences of (7) include (1,0) and (0,1), so Lambda=Z^2.
Thus in this case m divides P_6=30.
If the relation has more than one minimal block, each block has at least two terms, so ell<=4.
Then P_ell divides 6 and (10) gives m dividing 6d for some d in {1,2,3,4,5,6}.
Therefore

    m | 30, or m | 6,12,18,24,30,36.

The union of these divisor sets is precisely O in (2).
This proves the candidate order bound without an exhaustive torsion scan, an irreducibility assumption, or a Salem hypothesis.
The order one is in the overestimate O even though q(1)=-2 excludes it in this family.

<a id="uniform-scaled-plastic-repair"></a>
### Multiplicity, all-index repair and explicit bounds

For completeness, the sparse multiplicity argument from [L G0040](Yin_C_G0250_v1.md#bounded-order-followup) applies directly.
If P(t)=sum_(i=1)^s a_i t^(n_i) has distinct exponents and nonzero coefficients and rho is a nonzero root of multiplicity at least s, then the operators (t d/dt)^j for j=0,...,s-1 give

    sum_i n_i^j a_i rho^(n_i)=0.

The Vandermonde matrix in the distinct n_i is invertible.
This would force every a_i rho^(n_i) to vanish, a contradiction.
A nonzero root has multiplicity at most s-1.
Applied to q, this proves

    c=product_(m in O) Phi_m^(e_m),          0<=e_m<=5.        (11)

We use normalized net traces, with all roots counted with multiplicity,

    b_j(P)=(1/j) sum_(a|j) mu(j/a) sum_(alpha root of P) alpha^a,
    D(P)=sum_(j>=1) j max(0,-b_j(P)).                         (12)

For the polynomials at issue these are integer Euler exponents.
For q this follows directly from the graph: trace A^a counts based closed walks, and the usual decomposition into repetitions of a primitive cyclic orbit gives b_j(q)>=0 for every j.
Zero eigenvalues contribute nothing.
For c the cyclotomic formula is

    b_j(Phi_m)=mu(m/j) if j|m, and zero otherwise.            (13)

Additivity of traces under products then gives integer b_j(F) and b_j(F)=b_j(q)-b_j(c).

By definition R_*(F) is the least degree of a monic cyclotomic product c' for which every b_j(Fc') is nonnegative.
The original c in (11) is feasible because Fc=q.
Thus

    R_*(F)<=deg c<=5 sum_(m in O) phi(m)=360.                 (14)

If b_j(F)<0, (13) shows that j divides some m in O and hence j<=36.
Moreover b_j(q)>=0 implies

    max(0,-b_j(F))<=max(0,b_j(c))
                     <=sum_(m in O, j|m, mu(m/j)=1) e_m.

Multiplying by j and summing, with only finite nonzero terms, gives

    D(F)<=sum_(m in O) e_m S_+(m)<=5 sum_(m in O) S_+(m),
    S_+(m)=sum_(j|m, mu(m/j)=1) j
          =[m product_(p|m)(1+1/p)+phi(m)]/2.                (15)

The last identity is the positive correction budget already proved in [L G0040](Yin_C_G0250_v1.md#prime-support-repair-budget).
The finite divisor arithmetic is displayed here for direct checking:

| m | phi(m) | S_+(m) |
| --- | ---: | ---: |
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 2 | 4 |
| 5 | 4 | 5 |
| 6 | 2 | 7 |
| 8 | 4 | 8 |
| 9 | 6 | 9 |
| 10 | 4 | 11 |
| 12 | 4 | 14 |
| 15 | 8 | 16 |
| 18 | 6 | 21 |
| 24 | 8 | 28 |
| 30 | 8 | 40 |
| 36 | 12 | 42 |
| Total | 72 | 211 |

Equation (15) is therefore D(F)<=1055.
These are intentionally coarse universal bounds; no claim of optimal constants or simultaneous occurrence of the candidate cyclotomic factors is made.
The canonical product

    product_(j>=1) (t^j-1)^(max(0,-b_j(F)))

has degree D(F) and is feasible, since b_i(t^j-1) is one for i=j and zero otherwise.
Thus (12) is also the actual canonical repair degree, rather than merely a finite negative-trace statistic.
If there are no negative traces, both D(F) and R_*(F) are zero.

### The irreducible small-Mahler boundary

If F is irreducible, write F=p and let lambda be the positive Perron root of A.
It is not cyclotomic, so it is a root of p.
The reciprocity of q and of all its cyclotomic factors other than Phi_1, which does not divide q, gives reciprocity of p.
It is monic integral with constant coefficient one and has lambda>1 as its unique root of maximal modulus, by the primitivity of A.

For every r>=1 let K=Q(lambda^r) and L=Q(lambda).
In characteristic zero the identity embedding of K has [L:K] distinct extensions to embeddings of L into C.
Their values on lambda are roots z of p with z^r=lambda^r, hence |z|=lambda.
Unique maximal modulus forces each value to be lambda; there can be only one extension.
Thus [L:K]=1.
This supplies the required all-power degree preservation.

The proof of (2)--(3) used no Mahler-measure estimate.
Consequently, if an instance also satisfies 1<M(p)<theta_0, it still has uniformly bounded canonical and optimized repair.
What has not been proved is that all parameters, or any specified infinite sequence, satisfy both the sole-core and small-Mahler hypotheses.
In a reducible instance the positive graph supplies a completion of F, not a neutral completion of an arbitrarily selected irreducible factor of F.

### Consequence and remaining route

This closes a specific candidate mechanism for unbounded repair: uniformly scaling the plastic core and restoring primitivity with a coprime outer cycle does not escape a bounded list of cyclotomic orders.
The increasing matrix dimension and the explicit g-1 zero padding do not force the negative net-trace budget to increase.
Within the sole-core scope the candidate cannot produce an unbounded-repair family, even if small Mahler measure can separately be established for infinitely many parameters.

The next useful search must change this exponent-support geometry or its coefficient structure.
In this two-parameter method, an unbounded order would need the within-block difference lattice to lose rank or acquire unbounded index.
The present fixed six-point support admits neither event.
Such a different construction would still need a positive primitive realization, a sole noncyclotomic irreducible factor, and the required Mahler bound.
A redundant high-order cyclotomic factor or a plain common substitution does not supply those missing conditions.
No further candidate is explored in this record, and no lower bound on algebraic entropy, Shannon entropy, or maximum-atom entropy follows from (3).

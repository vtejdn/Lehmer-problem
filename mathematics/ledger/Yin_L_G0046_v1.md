---
author: Yin
---

# G0001: equitable neutral deletion and unbounded redundant cyclotomic orders

The complete current mathematical home is [Yin_C_G0264_v1](../claims/Yin_C_G0264_v1.md#argument), adopted at 2026-10-21T06:39 after the [actual complete current self-check](../audits/reviews/Yin_R_G0532_v1.md#current-complete-equitable-neutral-finding).
The original2026-10-07 mathematics and still-needed fixed review input below retain their original scope and date; this is no new research run.


Date: 2026-10-07.
Working argument by assigned AI review_matrix_completion for Yin.
The coordinator and assigned agent independently considered twin cyclic modules; the coordinator requested the general equitable-partition mechanism.
This gives an exact entropy-preserving reduction beyond duplicate-row amalgamation and a fixed-excess counterexample to a bound on the cyclotomic orders of every primitive presentation.
It does not refute the existential bounded-order question in [L G0040](Yin_L_G0040_v1.md).

No new source or numerical search is used.
The proofs below are direct.
The branch-return conventions are those of [L G0041](Yin_L_G0041_v1.md): row adjacency, multiplicities counted as edges, and nonnegative edge excess e(A)=sum A_ij-dim A.
This is different from Frobenius excess for entries greater than one.

<a id="equitable-neutral-deletion"></a>
## A verifiable entropy-preserving quotient

Let A be a primitive nonnegative integer adjacency matrix, and partition its vertices into nonempty cells C_1,...,C_b, of sizes r_1,...,r_b.
Suppose the partition is equitable in the outgoing convention: for each g,h the number of outgoing edges from a vertex i in C_g into C_h is independent of i.
Let B_gh be this common number.
The matrix B is nonnegative integral.
With the N by b cell-indicator matrix R,

    A R=R B.                                         (1)

The columns of R are independent, so im R is an A-invariant rational subspace on which A is represented by B.
Let T denote the induced linear map on Q^N/im R.
Block triangularization gives

    chi_A(t)=chi_B(t) chi_T(t).                      (2)

Here chi_T is monic integral: the other two characteristic polynomials are monic integral, and monic polynomial division in Z[t] identifies their exact quotient.
One can also choose an integral basis by keeping one cell-indicator column and all but one coordinate column in each cell.

The quotient B remains primitive.
Choose k with A^k strictly positive.
Every entry of A^k R is positive because each cell is nonempty.
From A^k R=R B^k, each row of B^k is repeated in the corresponding nonempty cell, hence B^k is strictly positive.
It has the same Perron root as A: a positive Perron eigenvector x of B lifts to the strictly positive eigenvector R x of A with the same eigenvalue.

Let d_g=sum_h B_gh, the common outgoing degree of vertices in C_g.
Then

    e(A)-e(B)=sum_g (r_g-1)(d_g-1).                 (3)

Indeed the edge sums are respectively sum_g r_g d_g and sum_g d_g, and the dimensions are sum_g r_g and b.
All d_g>=1, so this cannot increase edge excess; it decreases excess whenever a nontrivial cell has outgoing degree at least two.

The exact additional hypothesis for preservation of full algebraic entropy is that T has only zero and root-of-unity eigenvalues.
Under this verifiable hypothesis, chi_T=t^z c for a cyclotomic product c, and

    m(A)=m(B).                                       (4)

Equations (1)--(3) alone do not imply this neutral-spectrum hypothesis.
An arbitrary equitable quotient preserves the positive Perron root but may discard other expanding eigenvalues.
Nor does the presence of root-of-unity eigenvalues by itself provide an equitable partition.
These are separate conditions to check on a proposed reduction.

Unlike duplicate-row amalgamation, this move can delete nonzero neutral eigenvalues from a nonsingular matrix.
It is not asserted to preserve the entire nonzero spectrum or strong shift equivalence.
It preserves exactly the entropy required here when the induced quotient is neutral.

<a id="twin-cycle-unbounded-orders"></a>
## A primitive unimodular family of edge excess four

For each n>=2, take three disjoint positive directed cycles:

    a_0,...,a_(n+1)     of length n+2,
    b_0,...,b_(n-1)     of length n,
    c_0,...,c_(n-1)     of length n.

Add the four unit-weight arrows

    a_0 -> b_0,          b_(n-1) -> a_0,
    a_0 -> c_0,          c_(n-1) -> a_0.

All these positions are distinct and absent from the three base cycles.
Let A_n be the adjacency matrix.
It has

    N=3n+2 vertices,       M=3n+6 arrows,       e(A_n)=4.

It is strongly connected.
At a_0 there are return cycles of consecutive lengths n+1 and n+2, so all sufficiently large lengths are return lengths.
Adding fixed entrance and exit paths gives a common walk length for every ordered pair of vertices, proving primitivity.
In particular this example does not obtain large orders by sacrificing primitivity.

Partition each a vertex into its own cell and put b_j,c_j in one cell for each j.
This partition is equitable.
Its quotient B_n consists of an (n+2)-cycle and an n-cycle, with cross arrows

    a_0 -> b_0       of weight 2,
    b_(n-1) -> a_0   of weight 1.

Thus

    dim B_n=2n+2,       sum B_n=2n+5,       e(B_n)=3.

All paired cells have outgoing degree one except the final cell, which has degree two.
Formula (3) therefore gives the exact decrease e(A_n)-e(B_n)=1.
The Frobenius excess of B_n is five because of its entry 2; only the nonnegative edge-excess claim is being made.

The symmetric subspace im R consists of vectors with equal b_j and c_j coordinates.
The complementary antisymmetric subspace consists of vectors with all a coordinates zero and b_j=-c_j.
It is A_n-invariant: the two outgoing module contributions cancel in the a_0 coordinate, and the modules act there as one directed n-cycle.
Consequently the induced quotient T has characteristic polynomial t^n-1, with no nilpotent part.

The simple cycles of B_n are its two base cycles and the mixed cycle of length n+1 and weight 2.
Only the two base cycles are disjoint.
The cycle expansion gives

    P_n(t)=chi_(B_n)(t)
          =(t^(n+2)-1)(t^n-1)-2t^(n+1)
          =t^(2n+2)-t^(n+2)-2t^(n+1)-t^n+1,

    chi_(A_n)(t)=(t^n-1) P_n(t).                    (5)

P_n is a monic reciprocal integral unit polynomial of coefficient length six.
The polynomial chi_(A_n) has constant coefficient -1, so A_n is unimodular; B_n is also unimodular.
Moreover

    P_n(t) = -2t  modulo t^n-1,

so gcd(P_n,t^n-1)=1.
Thus A_n has every n-th root of unity as an eigenvalue of multiplicity exactly one, including primitive roots of exact order n.
The orders are unbounded while edge excess remains four.
Equations (2)--(4) apply with the explicitly identified neutral quotient and yield

    m(A_n)=m(B_n),

with the entire t^n-1 factor deleted by a primitive nonnegative integral quotient of smaller edge excess.
This is a genuine neutral deletion for nonsingular presentations, where duplicate-row compression cannot apply.

## The same obstruction inside a fixed-mass return matrix

The only branching vertices of A_n are a_0,b_(n-1),c_(n-1).
Their first-return matrix in this order is

    H_n(u)=[[u^(n+2), u^n, u^n],
            [u,       u^n, 0  ],
            [u,       0,   u^n]].                   (6)

Its total coefficient mass is seven, exactly three branch states plus edge excess four.
Direct elimination gives

    det(I-H_n(u))
      =(1-u^n)[(1-u^(n+2))(1-u^n)-2u^(n+1)]
      =(1-u^n)P_n(u).                               (7)

The last equality uses reciprocity of P_n.
The quotient has the two-state return matrix

    K_n(u)=[[u^(n+2), 2u^n],
            [u,       u^n]],

with coefficient mass five and determinant P_n(u).
Thus even positive polynomial return matrices of fixed size and fixed coefficient mass, arising from primitive unimodular graphs, may have cyclotomic factors of unbounded order.
The unbounded exponents remain meaningful; evaluating the matrices at u=1 would discard the information being tested.

## Exact boundary for the repair-budget question

This family disproves a universal order bound on every primitive graph of bounded nonnegative edge excess.
It also disproves such a bound with unimodularity and a reciprocal unit quotient added.
It does not settle the narrower question in L G0040: for an irreducible reciprocal all-power-preserving p with 1<M(p)<theta_0, does some admissible realization of the same bounded excess have bounded cyclotomic orders?

Several differences are explicit.
We have not proved that P_n is irreducible, or that M(P_n)<theta_0.
Additional factors of P_n have not been classified.
More decisively, the exhibited high-order factor is deleted by B_n with smaller edge excess, so it cannot obstruct an existential choice of a better presentation.
The quotient's normalized net traces are all nonnegative because B_n is a nonnegative integer graph.
Thus its full spectrum needs no canonical repair at all.
This does not assert that every irreducible factor of P_n separately has nonnegative net traces.

Any positive Perron minimal factor of P_n does have all-power degree preservation by the already established unique-dominant-conjugate argument, but this does not say that the remaining factors are cyclotomic.
It therefore does not put the entire family into the narrower L G0040 scope.
No unbounded actual negative budget D(p) is obtained here.

The useful next structural target is consequently an entropy-preserving neutral quotient or surgery with verifiable positive realizations, not an order bound on a chosen redundant representation.
Equitable partitioning is one actual mechanism, and (2) specifies exactly the spectral test it must pass.
There is no claim that every neutral factor is accessible to this mechanism, or that such reductions always terminate with uniformly bounded cyclotomic orders.

The complete original review account is retained in [the formal R home](../audits/reviews/Yin_R_G0532_v1.md#complete-original-g46-review-account), with original dates, contributions and unknown context scopes preserved.

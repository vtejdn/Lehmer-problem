---
author: Yin
---

# G0001: graph compression with full-spectrum accounting

Date: 2026-10-06T17:58.
Direct argument by assigned AI review_matrix_completion for Yin.
The primary target remains the full algebraic entropy of the integral flow.
The results below separate three operations: exact spectral state amalgamation, exact polynomial return presentations, and time-changing graph subdivision.
Only the first supplies an actual decrease of edge excess, under a concrete redundancy hypothesis.
No general small-entropy simplification theorem is obtained.

## Local and source boundaries

The local starting points are [L G0034](Yin_L_G0034_v1.md#graph-excess-length-bound), which permits zero padding and bounds coefficient length from nonnegative graph excess, [L G0038](Yin_L_G0038_v1.md), which has large-degree unimodular positive graph presentations, and [L G0039](Yin_L_G0039_v1.md#degree22-small-core-counterexample), whose small reciprocal example has three expanding conjugates.
The latter explicitly distinguishes log spectral radius from full algebraic entropy.

The original2026-10-07 [BL02 comparison](../audits/literature/BL02/Yin_U001.md#bl02-u001) owns the actual inspected return convention and spectral-containment limits.
The separately inspected [BS20 definitions](../audits/literature/BS20/Yin_U001.md#bs20-u001) retain their definitions-only scope.
Their original source dates, passage depths, artifact identities and unadopted realization/classification boundaries are preserved at those units and the registry.
Neither supplies an entropy-preserving two-state construction or a uniformly bounded coefficient mass.

Throughout this argument use the row convention A_ij = number of arrows i->j.
Transposition changes none of the spectral or complexity quantities.
Write

    Q_A(u)=det(I-uA),
    m(A)=log M(det(tI-A)),
    e(A)=sum_(i,j) A_ij - dim A

for a nonnegative integer adjacency matrix.
The edge sum counts multiplicities.
This e is the nonnegative edge excess, not the Frobenius excess when entries exceed one.
Existing algebraic-entropy inputs identify m(A) with the full entropy, including for singular A.
Equality of Q_A preserves every nonzero eigenvalue with multiplicity, hence m(A), all traces and all normalized net traces.
It is substantially stronger than equality of the positive Perron root.

<a id="spectrum-preserving-amalgamation"></a>
## Exact state amalgamation can reduce excess

Assume every row of A is nonzero, and partition the rows into groups of identical rows.
Let R be the zero-one matrix assigning each state to its row group, so every row of R has exactly one entry 1 and every column is nonempty.
Let S have one copy of each row prototype.
Then

    A=R S,                  B=S R.

B is again nonnegative integral.
The block determinant identity, obtained by eliminating either diagonal identity block in

    [[I, u R], [S, I]],

gives

    det(I-uA)=det(I-uB).                              (1)

Thus amalgamation removes only zero eigenvalues and preserves the full algebraic entropy.
If A is primitive, B is primitive as well: B^k=S A^(k-1) R is strictly positive for all sufficiently large k, since each row of S and each column of R is nonzero.

For group g, let r_g be its size and d_g the sum of its prototype row.
Direct counting yields

    e(A)-e(B)=sum_g (r_g-1)(d_g-1).                  (2)

Hence amalgamation cannot increase edge excess when all row sums are positive, and strictly decreases it whenever a repeated row has row sum at least two.
An analogous statement follows by transposing.
This is an actual spectrum-preserving reduction, not a Perron-only replacement.
It need not decrease Frobenius excess: merging columns can create entries greater than one, so that different quantity requires its own accounting.

More generally an elementary strong shift equivalence A=R S, B=S R satisfies (1), and a finite chain preserves Q_A.
The determinant identity requires no positivity; retaining nonnegative integer matrices is an additional requirement on the chosen factors.
It supplies no automatic decreasing complexity function for arbitrary factorizations.

Ordinary shift equivalence also preserves the full nonzero spectrum.
In its defining equations

    A R=R B,       S A=B S,       A^l=R S,       B^l=S R,

for some l>=1, restrict over C to the eventual images on which A and B are invertible.
The intertwining maps preserve these images; R is injective there because S R=B^l is invertible, and surjective because R S=A^l is invertible.
Hence the nonnilpotent restrictions are similar.
This proves equality of Q_A without asserting that an arbitrary shift equivalence is a chain of positive elementary amalgamations.

The redundancy hypothesis is substantial.
A nonsingular A has linearly independent rows, so no two rows can coincide.
More generally it cannot have a factorization A=R S through a smaller vector space.
Thus a direct elementary step cannot reduce the dimension of a nonsingular presentation.
This does not rule out chains that first enlarge the presentation, nor does it rule out changes that reduce excess at unchanged dimension.
The unimodular small-core matrix in L G0039 already shows that small Mahler measure does not force duplicate rows.

For an explicit control on presentation dependence, start with

    A=[[1,1],[1,0]],       det(tI-A)=t^2-t-1.

For k>=1 take as states the admissible binary words of length k with no consecutive 1s, with the usual overlapping-word transitions.
There are F_(k+2) states and F_(k+3) arrows, with F_1=F_2=1, so their excess is F_(k+1), unbounded.
Periodic paths correspond bijectively, with marked starting point, to periodic paths of the original graph.
All traces and Q_A are therefore unchanged; the characteristic polynomial is

    t^(F_(k+2)-2)(t^2-t-1).

The graphs are primitive and have only zero padding beyond the same unit polynomial.
For k>=2, merging words with identical suffix of length k-1 is exactly the row amalgamation above, and recovers the preceding presentation.
This demonstrates both a successful reduction on genuinely redundant graphs and why an arbitrary realization's excess is not itself a spectral invariant.
It says nothing adverse about the minimum excess.

<a id="branch-return-budget"></a>
## An exact return presentation with at most e branch states

Let A be strongly connected, with every vertex of positive outgoing degree, and not a single directed cycle, counting parallel edges separately.
The outgoing-degree condition explicitly excludes the one-vertex zero graph if strong connectivity permits length-zero paths.
Then e=e(A)>=1.
Let B be the set of vertices of outgoing degree at least two, and C its complement.
Put b=|B|.
Since every vertex has positive outgoing degree,

    e=sum_i(outdeg(i)-1),       1<=b<=e.

Every vertex of C has exactly one outgoing edge, of weight one.
The subgraph induced by C has no directed cycle: such a cycle could never leave C, contradicting strong connectivity and B nonempty.
Hence A_CC is nilpotent.
Define the b by b polynomial matrix

    H(u)=u A_BB+u^2 A_BC (I-u A_CC)^(-1) A_CB.        (3)

The inverse is a finite geometric sum.
Every entry of H is a polynomial with nonnegative integer coefficients and zero constant term.
Its coefficient of u^l counts first-return paths of length l between branch states, with no intermediate branch state.

Each outgoing edge from B has exactly one continuation until the first return to B.
No infinite continuation inside C is possible.
Consequently, counting all coefficients with multiplicity,

    ||H||_coeff = sum_(i,j) H_ij(1)
                =sum_(i in B) outdeg(i)=b+e<=2e.     (4)

Eliminating the C block in I-uA gives the exact identity

    det(I-uA)=det(I-u A_CC) det(I-H(u))
             =det(I-H(u)).                          (5)

Thus a graph of edge excess e has a full-spectrum positive polynomial return presentation with at most e states and at most 2e coefficient units.
The lengths in its monomials may be arbitrarily large.
The source's convention writes H=uP; retaining this factor of u is essential.

Conversely, let H have nonnegative integer coefficients, zero constant term, and a strongly connected underlying graph H(1) with positive outgoing degrees.
Replace each coefficient unit in a degree-l monomial of H_ij by a separate directed path of length l from i to j, using fresh internal vertices.
The adjacency matrix A_H satisfies (5), by the same nilpotent-block elimination.
If w=||H||_coeff and its base has b vertices, then

    edges(A_H)=sum_(labelled paths) l,
    vertices(A_H)=b+sum_(labelled paths)(l-1),
    e(A_H)=w-b.                                     (6)

The expanded graph is strongly connected.
Its period is the greatest common divisor of the total lengths of closed walks in the polynomial presentation; primitivity therefore requires this gcd to be one.
In the return presentation of a primitive A this is automatically the original gcd, so re-expansion remains primitive.

Equations (3)--(6) compress the number of displayed states while preserving every delay and the entire nonzero spectrum.
They do not lower excess: re-expanding the canonical presentation gives e again, even if shared deterministic tails have been duplicated.
A small displayed matrix by itself is insufficient; its coefficient mass is the missing complexity quantity.
Establishing a uniformly bounded such mass for the low-entropy class would be useful, but no such inference is proved here.

<a id="subdivision-entropy-obstruction"></a>
## Time-changing subdivision can move full entropy in the wrong direction

Consider the positive bouquet graph with a length-two cycle and a length-three cycle sharing exactly one vertex.
This is L G0034's primitive singular control: it has four vertices, five arrows, excess one, and

    chi_A(t)=t(t^3-t-1),       Q_A(u)=1-u^2-u^3.

Subdivide one edge of the length-two cycle twice.
The new cycles have lengths four and three; the new graph has six vertices, seven arrows, excess one, and

    chi_B(t)=t^2(t^4-t-1),     Q_B(u)=1-u^3-u^4.       (7)

Both graphs are strongly connected and primitive, as their cycle lengths are coprime.
Each edge subdivision is a symbolic expansion: in the suspension flow it replaces traversal of that edge by a longer subdivided traversal, with an orientation-preserving time change.
The inverse simply concatenates the forced consecutive new edges.
Thus these graphs are flow equivalent in precisely this time-changing sense.
Moreover det(I-A)=det(I-B)=-1, so both integer cokernels coker(I-A), coker(I-B) are trivial.
These weaker invariants agree although Q_A and Q_B do not.

The nonzero polynomial of A is the irreducible unit f_3=t^3-t-1; let theta be its positive root.
Its other two roots have modulus theta^(-1/2), so M(f_3)=theta.
The nonzero polynomial f_4=t^4-t-1 of B is also an irreducible unit.
Indeed its reduction t^4+t+1 over F_2 has no linear factor and is not divisible by the only irreducible quadratic t^2+t+1.

Write r for the positive root of f_4 and -a for its negative real root.
There is exactly one of each: Descartes' rule gives the positive one, while a solves the strictly increasing equation a^4+a-1=0 on (0,infinity).
The other two roots are a nonreal conjugate pair.
One has

    1<r<theta,

because f_4(theta)=theta^2-1>0.
Nevertheless M(f_4)>M(f_3).
To verify the stronger direction exactly, put g(x)=x^4+x-1.
Since r^4=r+1,

    g(1/r)=(r^2-1)/r^3>0,

so a<1/r.
The nonreal pair therefore has squared modulus 1/(ra)>1, and

    M(f_4)=r/(ra)=1/a.

Also theta<sqrt(2), by the cubic's monotonicity on [1,infinity), and

    g(1/theta)=(2-theta^2)/theta^4>0.

Hence a<1/theta and

    log rho(B)<log rho(A),       m(B)>m(A).            (8)

This is an actual primitive graph and algebraic-unit control, permitting only zero padding.
It lies outside the remaining small reciprocal core and is not offered as a Lehmer counterexample.
Its role is to show that time-changing simplification, even with fixed excess and trivial Bowen--Franks cokernel, does not preserve the full algebraic entropy.
It can even move Perron entropy and full entropy in opposite directions.

## Consequence for the route

Exact zeta/determinant surgery must retain Q_A(u), or change it only by explicitly permitted cyclotomic factors.
Elementary strong shift equivalence and the return identities above meet the stricter equality condition.
A flow equivalence or a spectral-containment theorem with unchanged Perron root does not.
In particular Boyle--Lind's two-state presentation theorem cannot be used to assert neutral completion or bounded edge excess: it does not control the extra spectrum, and its two-state coefficient mass is not uniformly bounded by its statement.

There is a concrete reduction algorithm when repeated rows or columns exist, with the precise excess decrease (2).
There is also a canonical full-spectrum compression into delay-labelled branch states, with the exact mass budget (4).
What remains unproved is that small m(p), or bounded scalar cyclotomic shortness, forces a positive presentation admitting these reductions to a uniformly bounded coefficient mass.
The existing inverse bound from edge excess to shortness does not give that missing direction.
None of these observations changes the original objective to Perron entropy or to a flow-equivalence classification.

## Review and current proof home

The complete original graph author, separate and coordinating findings are retained under their actual scopes at [R528](../audits/reviews/Yin_R_G0528_v1.md#original-graph-author-finding).
The complete current statement and proof are [C253](../claims/Yin_C_G0253_v1.md#argument), adopted after the actual [whole current self-check](../audits/reviews/Yin_R_G0528_v1.md#current-complete-graph-compression-finding).
The redundancy, coefficient-mass and full-entropy limitations above remain unresolved at exactly their stated boundaries.

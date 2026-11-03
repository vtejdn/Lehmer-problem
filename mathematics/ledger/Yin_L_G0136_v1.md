---
author: Yin
---

# Sparse integer defects give exact finite-energy threshold certificates

Date: 2026-10-08.
Direct bounded G0001 derivation by the assigned execution_and_deliverables AI for Yin.
The coordinator requested an exact lower-certificate method for the finite problem of L G0130 and its actual-product application in L G0132.
The coordinator contributed the cube-free Gram obstruction in the last section.
Completed independent review is recorded below.
No optimization, coefficient search or numerical mathematical computation has been executed.

## The same finite problem, with its recurrence dimension retained

Use the monic irreducible unit polynomial P of [L G0130](Yin_L_G0130_v1.md#finite-rational-energy-coercivity): its degree is d, its logarithmic Mahler measure is positive, and it has at least one unit-circle root.
Write P(t)=sum_(i=0)^d p_i t^i.
In particular p_0 is 1 or -1.
The algorithm below only needs that P is a fixed nonzero integral polynomial of degree d; the stated unit/central domain is retained for its application and the final control.

For an integer R>=0 put

    I_R={-R,...,R+d},  n=2R+d+1,
    J_R={-R,...,R},    s=2R+1.

Let A be the s by n integer matrix of P(S) on these intervals:

    (Ax)_j=sum_(i=0)^d p_i x_(j+i),  j in J_R.

The columns indexed by -R+d,...,R+d form a triangular s by s submatrix with nonzero diagonal p_d.
Consequently

    rank A=s,  dim ker A=d.                              (1)

The exact old quantity is

    E_R=min { ||x||_2^2 : x in [-1/2,1/2]^n,
                          Ax in Z^s, (Ax)_0!=0 },        (2)

with value infinity if the feasible set is empty.
L G0130 proves that its finite minima are rational and E_R tends to infinity in the stated unit/central domain.
L G0132 further proves that every E_R is finite there and [E_R<=a_P log n+b_P](Yin_L_G0132_v1.md#logarithmic-finite-energy-witnesses).
Neither of these growth claims is a premise of the finite algorithm below.

Fix a rational threshold B>=0.
The output will decide the strict statement E_R>B exactly, including the equality case E_R=B.
Define the fixed coefficient and integer budgets

    L=sum_i |p_i|,   Z=floor(L/2),
    K=floor(L^2 B),  a=min(Z,floor(sqrt K)).                (3)

All these integers are computable by rational/integer arithmetic; the square root floor means the largest integer whose square is at most K.

## Energy bounds the number of nonzero integer defects

Extend x by zero outside I_R.
Every restricted shift has norm at most ||x||_2, so the triangle inequality gives

    ||Ax||_2 <= L ||x||_2.                                (4)

If x is feasible in (2) and ||x||_2^2<=B, then z=Ax satisfies

    z in Z^s, z_0!=0, |z_j|<=Z,
    sum_j z_j^2 <= K.                                    (5)

The coordinate bound follows from |x_i|<=1/2.
The squared norm on the left is an integer, which justifies the floor in K.
Thus at most K defect coordinates are nonzero, including the origin, and every coordinate has modulus at most a.

Let D_(R,B) be the finite integer set specified by (5).
If K=0 or a=0, it is empty and E_R>B follows immediately.
Otherwise it can be enumerated by choosing its support, which must contain 0, assigning nonzero integers of modulus at most a, and retaining only assignments whose sum of squares is at most K.
In particular

    |D_(R,B)| <= sum_(h=1)^min(s,K)
                     binom(s-1,h-1) (2a)^h.              (6)

For fixed P and B this is O_(P,B)((R+1)^(K-1)).
This is an upper bound, not a claim that every listed vector has a feasible fiber.
Opposite signs may be paired if desired, since x and -x have the same energy, but that optional saving is not needed in (6).

The origin condition is important to the exponent K-1: it forces one of the at most K support locations.
The algorithm remains finite without exploiting that saving.

## Exact Gram exclusion before imposing the box

The rational matrix G=A A^T is positive definite by (1).
For a fixed integer z the unconstrained affine minimum is

    x^0(z)=A^T G^(-1)z,
    Q_R(z)=min_(Ax=z) ||x||_2^2=z^T G^(-1)z.              (7)

This follows by orthogonally decomposing any solution into x^0 and ker A.
All entries and the minimum are exact rational numbers.
If Q_R(z)>B, no point of that fiber can witness E_R<=B.
If Q_R(z)=B, a witness exists in the fiber exactly when x^0 lies in the box; otherwise the strict convexity and compactness of the box fiber imply its minimum is strictly greater than B or the fiber is empty.
Thus equality does not require a numerical tolerance or a limiting test.

One may evaluate (7) on the finite list (5), or enumerate only the intersection of that list with the ellipsoid Q_R(z)<=B.
For an exact branch implementation write

    G^(-1)=U D U^T,
    Q_R(z)=sum_(i=1)^s D_i
                 (z_i+sum_(j>i) U_(j,i) z_j)^2,          (8)

where U is unit lower triangular and each D_i is positive rational.
Such an LDL factorization uses rational arithmetic without square roots.
Having fixed z_s,...,z_(i+1), subtract their terms from B.
A negative remainder excludes the branch; otherwise enumerate the integers z_i in [-a,a] whose displayed squared term does not exceed that remainder.
Also keep the remaining integer square budget in (5), reserve a nonzero origin if it is not yet assigned, and enforce its nonzero value when it is assigned.
These are all rational inequalities.

Every vector in (5) with Q_R(z)<=B survives every prefix test, since the omitted terms in (8) are nonnegative.
Conversely every completed retained branch satisfies those conditions.
Thus the pruning is complete.
It does not assert that the ellipsoid alone can provide arbitrarily large lower bounds; the box is essential.

## At most d active coordinates suffice for each box fiber

Fix z and consider

    F_z={x in [-1/2,1/2]^n : Ax=z}.

If nonempty it is compact and has a unique minimum-norm point x*.
List all coordinates at which x*_i is 1/2 or -1/2.
Restrict their coordinate functionals to ker A, a space of dimension d.
Choose a basis among those restricted functionals, indexed by a subset T with |T|<=d.
Zero or dependent restrictions need not be selected.
The rows of A together with the selected coordinate rows are independent.

On the affine fiber Ax=z, imposing the selected active equations

    x_i=x*_i in {1/2,-1/2},  i in T                     (9)

imposes every other active coordinate equation as well: their restrictions to ker A are linear combinations of the selected ones, and all constants agree at x*.
The affine space defined by Ax=z and (9) is therefore the affine hull obtained by imposing all active coordinates at x*.

All other box inequalities are strict at x*.
A sufficiently small motion in either direction of any vector in that affine space's direction space remains feasible.
The first derivative of the squared norm in each such direction is zero.
Hence x* is precisely the orthogonal projection of zero onto that affine space.

It follows that the following finite enumeration finds every nonempty fiber minimum.
For each subset T of at most d coordinates, and each assignment of signs at those coordinates, form

    C=[A; (coordinate rows indexed by T)],
    b=[z; assigned signs divided by 2].

Skip a case unless C has full row rank s+|T|.
In a remaining case compute the exact rational projection

    x=C^T(CC^T)^(-1)b.                                  (10)

Retain it if every coordinate lies in [-1/2,1/2].
Its equality constraints already hold by construction.
Minimize ||x||_2^2 over retained points.
A nonempty F_z supplies x* as just proved; conversely every retained point is in F_z.
No retained point means the box fiber is empty.
Dependent active equations are not lost because their independent basis was among the enumerated cases.

The number of projections tried per z is at most

    H_(n,d)=sum_(h=0)^d 2^h binom(n,h),                   (11)

with binom(n,h)=0 when h>n.
For fixed P this is O_P(n^d), in place of enumerating all 3^n coordinate faces.
It is not a claim that d or this exponent is small in a varying-degree input.

<a id="sparse-energy-threshold-decision"></a>
## Exact decision, equality boundary and search cost

Enumerate (5), prune by (7), and perform (9)--(10) on each retained defect.
If any retained point has squared norm <=B, output that rational point as a witness for E_R<=B.
If no such point occurs, output E_R>B.
The proof of correctness is complete in both directions: every true witness has a defect in (5), survives (7), and belongs to a fiber whose exact minimum is enumerated; every returned point satisfies all the original conditions (2).

In particular E_R=B returns the non-strict outcome E_R<=B, with a rational equality witness.
An empty original feasible set returns E_R>B.
No transcendental comparisons occur.

A direct implementation using the full sparse list, Gram filtering and all projections in (11) uses at most

    |D_(R,B)| H_(n,d)                                   (12)

projection attempts.
Rank tests and projections have matrices of size at most n and can use cubic-many rational arithmetic steps.
For K>=1 this gives the conservative arithmetic-operation bound

    O_(P,B)((R+1)^(K+d+2)).                              (13)

Constructing the sparse list and the Gram filter fits within this bound.
The optional branching implementation (8) may save work; no extra saving from it is assumed in (13).

This is also a polynomial bit-complexity bound in R for fixed P,B, with an additional polynomial factor if the rational operations are expanded into bit operations.
Indeed all entries of C are bounded integers from P or coordinate rows, and the right side b has denominator at most two and bounded numerator for fixed P,B.
Gram entries are bounded by a polynomial in n.
Hadamard's bound gives O_(P,B)(n log(n+1)) bits for their minors.
Fraction-free elimination and determinant ratios therefore keep all intermediate integers and final rational projections at polynomial bit length.
Comparisons with the fixed rational B are exact.
Rank-deficient cases can be detected by the same exact elimination.

The dependence on the parameters must remain visible.
The exponent K=floor(L^2 B) can be enormous; d also appears in the exponent.
There is no uniform polynomial bound in degree or in the binary encoding length of B.
Polynomial in R means polynomial in the explicit window length, not polynomial in the binary length of R.
This result supplies no bound on how large R must be before a threshold succeeds, and no practical-runtime claim.

<a id="rational-energy-dual-certificates"></a>
## Compact rational certificates for the strict lower outcome

The enumeration already gives a verifiable exact decision.
There is also a dual format that need not list every active face.
For a rational vector y in Q^s define

    psi(t)=t^2                  if |t|<=1/2,
           |t|-1/4             if |t|>=1/2,
    D_z(y)=2 y^T z-sum_i psi((A^T y)_i).                  (14)

The formulas agree at |t|=1/2, so D_z(y) is rational and directly checkable.
For any x in the box with Ax=z, completing the square and minimizing each coordinate in the box give

    ||x||_2^2 >= D_z(y).                                 (15)

Equivalently psi(t)=max_(|u|<=1/2)(2tu-u^2); its maximizer is the clipped value min(1/2,max(-1/2,t)).
This proves (15) without assuming an optimization algorithm or strong duality.

A strict lower certificate E_R>B consists of the fixed P,R,B, the exhaustive integer list (5) or its stated enumeration rule, and, for each z in that list with Q_R(z)<=B, a rational y_z with

    D_z(y_z)>B.                                         (16)

A verifier enumerates (5), verifies the exact Gram exclusions, and checks (16) on every remaining defect.
Equations (4)--(7) and (15) prove that passing all checks certifies E_R>B.
It is not enough to check a selected subset of integer defects.

For completeness such a finite dual certificate always exists when E_R>B.
If F_z is nonempty, its rational minimizer x* was constructed in (10).
The elementary normal-cone condition for minimizing a differentiable convex function over a polyhedron gives an equality multiplier y satisfying

    (A^T y)_i=x*_i          when |x*_i|<1/2,
    (A^T y)_i>=1/2          when x*_i=1/2,
    (A^T y)_i<=-1/2         when x*_i=-1/2.                (17)

Here is the applicable condition explicitly: the feasible tangent directions satisfy Av=0, v_i<=0 at upper active coordinates and v_i>=0 at lower active coordinates; optimality says x*^T v>=0 on this polyhedral cone.
The finite-dimensional Farkas alternative expresses this polar-cone membership by the equality multiplier and nonnegative active-coordinate multipliers, which is exactly (17).
All its coefficients and x* are rational.
A nonempty rational system of linear equalities and weak inequalities has a rational point, obtainable for example by exact elimination.
Thus y can be chosen rational.
Since x* clips A^T y, equality holds in every coordinate of (15), so D_z(y)=||x*||_2^2>B.

If F_z is empty, z is outside the compact rational polytope A[-1/2,1/2]^n.
Strict separation supplies y with

    y^T z > (1/2)||A^T y||_1.                            (18)

It may be chosen rational: the image polytope has finitely many rational vertices and the finitely many strict separating inequalities persist under a sufficiently small rational change of y.
For a positive rational t tending to infinity,

    D_z(t y)=t(2y^T z-||A^T y||_1)+O(1) -> infinity.

Thus a rational multiple supplies (16) in the empty-fiber case as well.
This proves completeness of the rational dual format.
It does not claim that exhaustive enumeration of rational dual vectors is an efficient method for constructing those certificates.
The direct finite algorithm (9)--(13) already proves the stated polynomial-in-R decision bound independently of dual extraction.

A non-strict outcome has the simpler certificate consisting of one rational x: check its box constraints, integer Ax, nonzero origin defect, and squared norm <=B.
Equality is fully checkable.

<a id="cube-free-gram-boundary"></a>
## Why the cube must remain, and what is new for L G0132

The following diagnostic was proposed by the coordinator.
Drop the box in (2), retaining integer defects and a nonzero defect at the origin.
The coordinate vector x=delta_0 on I_R has

    ||x||_2^2=1,  Ax in Z^s,  (Ax)_0=p_0 in {1,-1}.

Consequently for every R,

    min_(z in Z^s, z_0!=0) z^T(AA^T)^(-1)z <=1.          (19)

The bound is witnessed after minimizing the affine fiber of that integer z, even though delta_0 itself is outside the box.
In the present unit-circle domain it survives even the inherited coordinate defect bound |z_j|<=Z: if beta is any unit-circle root, P(beta)=0 implies |p_i|<=sum_(h!=i)|p_h|, hence |p_i|<=L/2 for every i.
The integer entries of A delta_0 are therefore at most floor(L/2).
For B>=1 this witness also obeys the sparse budget (5).

Thus exact integer-ellipsoid optimization alone cannot certify a strict lower bound above one in this domain, whereas the box-constrained E_R tends to infinity.
The active-coordinate or dual box test is essential, not an optional numerical repair.

Compared with L G0130, the mathematical quantity E_R and its threshold meaning have not changed.
The new facts are the threshold-dependent sparse defect bound (5)--(6), the at-most-d active-coordinate reduction (9)--(11), the resulting exact fixed-P,B polynomial-in-window decision bound, and the complete rational lower-certificate format.
In particular [L G0132's fully rational test](Yin_L_G0132_v1.md#tunable-salem-finite-energy-envelope) E_R>4 B_bar can use B=4 B_bar here; more generally any rational L_R can be certified by proving E_R>L_R.

This gives no actual optimized E_R value, no product lower bound, no degree-uniform threshold or search complexity, and no Mahler gap.
It does not reproduce or assume the separately investigated quantitative coercivity estimate for the first successful R.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0042_v1.md#contributions-and-review), with its original inspected scope and relationship.

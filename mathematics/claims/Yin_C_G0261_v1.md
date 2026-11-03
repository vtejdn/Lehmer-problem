---
author: Yin
---

# Cyclic-norm groups, exact local generator constraints and all-time rounding surjections

This retains every original 2026-10-07 L77 proof: integral semidirect and quotient identities, good-prime local bases, full generator/rank and depth controls, the explicit all-time rounding map and exact entropy scope.
The retained fixed interfaces are credited at their original domains; no native execution, new source or uniform binary alphabet claim is made.
The fixed original input remains [L77](../ledger/Yin_L_G0077_v1.md).

## Statement

Let alpha be a nontorsion algebraic unit with monic irreducible P of degree d, K=Q(alpha), m=log M(P)>0, and L any alpha-invariant full integer lattice.
Multiplication A is an integral automorphism and for every n>=1,

    H_n(L)=L/(A^n-I)L,
    |H_n(L)|=|det(A^n-I)|=C_n=|Norm(alpha^n-1)|.

For Gamma=L semidirect_A Z, its index-n cyclic subgroup has abelianization Z direct_sum H_n(L).
The index C_n is lattice invariant; its group type can differ, as the full explicit norm45 example has Z/45Z versus Z/3Z direct_sum Z/15Z.
At a good squarefree prime, a lifted cyclic vector makes every invariant lattice locally companion, so its entire p-primary quotient is lattice invariant.

For O=Z[alpha], Gamma has two generators and the index-n subgroup has the displayed n+1 Schreier generators.
The exact coinvariant presentation is

    H_n(O)=Z[t]/(P,t^n-1)=coker P(S_n),
    min_generators(H_n(O))=max_p deg gcd(P modp,t^n-1)<=min(d,n).

For a lattice needing mu Laurent-module generators the bounds are mu n+1 and mu n; arbitrary lattices are not declared cyclic.
At a good prime write n=p^v n_0 with p not dividing n_0.
Then k_p(n)<=min(d,n_0) and k_p(n)(1+v)<=n, so the same-time floor obeys A_S(n)<=n sum_(p in S)logp.
For reciprocal even-degree constant-one P,

    k_p(n) is even,
    k_p(n)<=min(d,n_0-gcd(n_0,2)),

including characteristic two; no good prime contributes at n1 or2.
These are upper caps and a maximum over primes, without a summed generator-rank obstruction or positive local coverage.

For every integer R>=4 coprime to3, the actual irreducible reciprocal all-power-stable unit P_R=t^2-(R-1)t+1 has

    C_3=(R-3)R^2,
    H_3(O)(p)=(Z/p^(v_p R)Z)^2 for every p dividing R.

Those primes are good, and arbitrarily many chosen primes/depths coexist at the same exponent with two generators.
Its measure grows without bound; it is no near-one counterfamily.

In a chosen basis L=Z^d, let Q=[0,1)^d and F={floor(Ax):x in Q}.
This finite parameter-dependent alphabet contains0 and for every n,

    T_n(A,F) -> H_n(L) surjectively,
    C_n<=|T_n(A,F)|.

The full representative/sign argument includes unit-circle conjugates.
The complete elementary limsup of log C_n/n is m, and the finite-set entropy has the exact attainment

    H(A,F)=h(A|L)=h(A|Q^d)=m.

No uniform alphabet size, binary capture or convergence time follows.
A finite-time trajectory slope is an upper bound on its limiting entropy; quotient blocks add and do not encode independent concatenations.
The archimedean d log2 norm cost remains.

The original rational flow has Q^d/(A^n-I)Q^d=0 and rational semidirect abelianizations Z; its whole group is not the finitely generated integral model.
The exact rational primary and multiplicity/capture boundaries remain necessary for arbitrary finite-entropy flows.
No new Mahler gap, all-prime scalar theorem or uniform arithmetic coverage is supplied.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:04 |
| status | open |
| reason | Register the complete original mathematical argument and exact retained input boundaries; actual current whole review and adoption follow separately. This registers no native execution, source acquisition, numerical certification, research resumption or independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | All integral lattice/group/Schreier/local-rank and depth claims, complete all-time rounding-surjection/entropy statements, exact examples and rational/finite-time scope. |
| argument | [Entire original proof](#argument) | Complete original determinant/abelianization/local-basis/presentation/generator proofs, reciprocal guards, exact quadratic modules, all-n rounding signs and representatives, limsup/finite-set entropy and rational-flow distinctions. |
| dependency | [Complete norm certificate](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original nonzero K/Q cyclic norm and archimedean d log2 bound, with all original roots and no powered-degree replacement. |
| dependency | [Rational entropy upper interface](Yin_C_G0205_v1.md#rational-primary-formula) | Only the accepted total characteristic-polynomial Mahler formula and monotonicity upper bound; the all-time lattice surjection and lower limsup are proved here. |
| support | [General flow boundary](Yin_C_G0205_v1.md#capture-equivalence) | Original rational primary and positive-constituent multiplicity/capture quantifiers, without identifying arbitrary extensions or neutral blocks with one cyclic lattice core. |
| support | [Prior rounding construction](Yin_C_G0239_v1.md#finite-alphabet-capture-and-the-remaining-arithmetic-question) | Existing parameter-dependent coordinate-floor alphabet only; the half-open representative all-n quotient surjection and its group constraints are proved here in full. |
| support | [Prior lattice effect control](Yin_C_G0251_v1.md#local-conductor-period-bound) | Only the retained alpha=2+3epsilon index-three example; both norm45 Smith calculations and the good-prime whole-group argument are proved here. |
| support | [Prior elementary periodic limsup](Yin_C_G0236_v1.md#adjoint-periodic-index-boundary) | The already retained compact-torus-return limsup at the original eigenvalues; no full Baker limit or new source audit is used. |
| support | [Toral/index attribution](../audits/literature/War05/Yin_U001.md#war05-u001) | Fixed integral toral determinant/periodic-index interface, with the retained source/Baker scope; its stronger full limit is not a premise of this elementary argument. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:07 |
| status | proved |
| reason | Adopt the complete original group/local-rank/depth and all-time rounding-surjection theorem after actual whole current self-review. Every lattice/rational distinction, nonzero norm, local good-prime guard, exact example, finite-time/subadditivity and fixed-alphabet scope is retained; no block concatenation, uniform alphabet, native execution or independent review is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All integral lattice/group/Schreier/local-rank and depth claims, complete all-time rounding-surjection/entropy statements, exact examples and rational/finite-time scope. |
| argument | [Argument](#argument) | Complete original determinant/abelianization/local-basis/presentation/generator proofs, reciprocal guards, exact quadratic modules, all-n rounding signs and representatives, limsup/finite-set entropy and rational-flow distinctions. |
| dependency | [Dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original nonzero K/Q cyclic norm and archimedean d log2 bound, with all original roots and no powered-degree replacement. |
| dependency | [Dependency](Yin_C_G0205_v1.md#rational-primary-formula) | Only the accepted total characteristic-polynomial Mahler formula and monotonicity upper bound; the all-time lattice surjection and lower limsup are proved here. |
| support | [Support](Yin_C_G0205_v1.md#capture-equivalence) | Original rational primary and positive-constituent multiplicity/capture quantifiers, without identifying arbitrary extensions or neutral blocks with one cyclic lattice core. |
| support | [Support](Yin_C_G0239_v1.md#finite-alphabet-capture-and-the-remaining-arithmetic-question) | Existing parameter-dependent coordinate-floor alphabet only; the half-open representative all-n quotient surjection and its group constraints are proved here in full. |
| support | [Support](Yin_C_G0251_v1.md#local-conductor-period-bound) | Only the retained alpha=2+3epsilon index-three example; both norm45 Smith calculations and the good-prime whole-group argument are proved here. |
| support | [Support](Yin_C_G0236_v1.md#adjoint-periodic-index-boundary) | The already retained compact-torus-return limsup at the original eigenvalues; no full Baker limit or new source audit is used. |
| support | [Support](../audits/literature/War05/Yin_U001.md#war05-u001) | Fixed integral toral determinant/periodic-index interface, with the retained source/Baker scope; its stronger full limit is not a premise of this elementary argument. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0530_v1.md#current-group-quotient-finding) | Entire exact current statement, complete original argument and every selected interface, self-reviewed; no retrospective replacement of original finding inputs or scope. |

## Complete retained argument

<a id="argument"></a>

<a id="cyclic-norm-group-interface"></a>
### Quotients and cyclic-index subgroups

Put

    H_n(L)=L/(A^n-I)L,    C_n=|Norm(alpha^n-1)|,    n>=1.

The map A^n-I is nonsingular, so H_n(L) is finite and

    |H_n(L)|=|det(A^n-I)|=C_n.                              (1)

The right side is independent of L; the finite group's isomorphism type need not be.
This is the integer index/toral periodic interface already retained in [War05-U001](../audits/literature/War05/Yin_U001.md#war05-u001), not a count of fixed elements of the discrete lattice.

Let Gamma=L semidirect_A Z, with stable letter t, and let Gamma_n be the kernel of Gamma -> Z/nZ.
It is L semidirect_(A^n) Z, with stable letter t^n.
Since L is abelian, its commutator subgroup is precisely (A^n-I)L.
The splitting by the stable letter gives

    Gamma_n^ab = Z direct-sum H_n(L).                       (2)

Thus C_n is the order of the torsion subgroup of this abelianization.
This interpretation changes neither the norm nor the arithmetic coverage question of L G0074.

For a concrete structure boundary, reuse alpha=2+3 epsilon, epsilon^2-epsilon-1=0, from [L G0070](Yin_C_G0251_v1.md#local-conductor-period-bound).
On Z[alpha] a companion matrix is [[0,-1],[1,7]]; on Z+Z epsilon the matrix is [[2,3],[3,5]].
At n=2 the respective matrices A^2-I are

    [[-2,-7],[7,47]],    [[12,21],[21,33]].

Their absolute determinants are both 45.
The gcds of their entries are 1 and 3, so their Smith forms give Z/45Z and Z/3Z direct-sum Z/15Z, respectively.
Equality of the index in (1) must not be strengthened to equality of the group at every prime.

At a good prime p, meaning that P modulo p is squarefree, there is a stronger lattice-independent statement: the entire p-primary group H_n(L) is the same for every invariant full L.
Indeed the reduction of A has characteristic polynomial P modulo p and is cyclic: the distinct irreducible summands each have multiplicity one, and a vector nonzero in every summand is cyclic.
Lifting that vector to L tensor Z_p makes its first d iterates a basis, since their determinant is nonzero modulo p.
In that basis A is the companion matrix of P over Z_p.
Therefore the cokernel over Z_p, and hence the finite p-primary group, is independent of L.
This argument also explains exactly why it does not cover the repeated reduction in the displayed example.

<a id="schreier-local-rank-constraint"></a>
### What cyclic generation actually bounds

For the companion lattice O=Z[alpha], Gamma is generated by t and the lattice element 1.
The subgroup Gamma_n is generated by

    t^n,    1, alpha, ..., alpha^(n-1),

where the displayed lattice elements are regarded as group elements.
To check this directly, write any integer exponent j=qn+r with 0<=r<n.
Conjugation by t^(qn) produces alpha^j from alpha^r.
These orbit elements span O over Z.
This is the explicit Schreier bound of n+1 generators, without requiring a presentation theorem.

The coinvariant group has the exact cyclic-module presentation

    H_n(O) = Z[t]/(P,t^n-1)
           = coker(P(S_n):Z^n -> Z^n),                     (3)

where S_n cyclically permutes the standard n basis vectors.
Both descriptions follow by imposing t^n=1 in the polynomial module; t is then automatically invertible.
Its minimal number of abelian generators is

    max_p dim_Fp(H_n(O)/p H_n(O))
      = max_p deg gcd(P mod p,t^n-1) <= min(d,n).           (4)

For the equality, finite abelian groups decompose into p-primary parts.
Each p-primary part requires its dimension modulo p many generators, and generators for different primes can be combined coordinatewise.
Thus the relevant maximum is over primes, not a sum of their ranks.
The gcd formula is the dimension of the quotient of the principal ideal domain F_p[t] by (P,t^n-1).
It applies also at repeated reductions.

For an arbitrary invariant lattice generated by mu elements as a Z[alpha,alpha^(-1)]-module, the same argument gives mu*n+1 group generators for Gamma_n and at most mu*n generators for H_n(L).
It does not make an arbitrary lattice cyclic.
At good primes the stronger companion formula follows from the preceding local-basis argument.

Now let p be good, write n=p^v n_0 with p not dividing n_0, and use k_p(n) from [L G0074](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail).
Squarefreeness gives

    k_p(n)=deg gcd(P mod p,t^(n_0)-1)
          <=min(d,n_0).                                    (5)

Consequently k_p(n)(1+v)<=n, since 1+v<=p^v.
For a finite good prime set S, the automatic floor therefore obeys the additional upper bound

    A_S(n)<=n sum_(p in S) log p.                           (6)

This is an upper cap, not a source of nonzero local contributions.
In particular (4) gives no sum-of-ranks restriction that prevents the multiple-prime aggregation used in J G0011.

If P is reciprocal of even degree with constant term 1, one can sharpen (5).
Write P=t^(d/2) T(t+t^(-1)) with T in Z[t].
A root t=+1 or -1 of P modulo p would also be a root of its derivative: at such a root the derivative of t+t^(-1) vanishes, and the other product-rule term contains T.
This remains valid at p=2, where the two points coincide.
A good reduction therefore has no such root.
All other roots pair under inversion.
The set of those whose order divides n is also inversion-invariant.
Thus

    k_p(n) is even,
    k_p(n)<=min(d,n_0-gcd(n_0,2)).                           (7)

There are gcd(n_0,2) distinct excluded self-inverse roots among the n_0-th roots of unity: when p=2, n_0 is odd, so that number is one.
In particular no good prime contributes at n=1 or n=2.
The bound in (7), multiplied by (1+v), can replace (5) in a first-floor upper estimate.
It still supplies no lower bound or uniform coverage theorem.

<a id="good-prime-generation-depth-boundary"></a>
### Fixed generator rank permits arbitrary good-prime depth

Let R>=4 be an integer with gcd(R,3)=1, and put

    P_R(t)=t^2-(R-1)t+1,    s=R-1.

This is irreducible over Q: for s>=3, the discriminant s^2-4 lies strictly between (s-1)^2 and s^2.
Its roots are alpha>1 and alpha^(-1), so it is a reciprocal unit polynomial.
Every positive power of alpha still has degree two, because a rational power would be a rational integral unit and hence +1 or -1.
Thus this boundary retains irreducibility, reciprocity, the unit condition, and all-positive-power degree preservation.

For the companion matrix A, the identity A^2=sA-I gives

    A^3-I=R((R-2)A-I),
    det((R-2)A-I)=3-R,
    C_3=(R-3)R^2.                                          (8)

For every p dividing R, the discriminant is -3 modulo p and is nonzero.
Such p is good.
The second matrix factor in (8) is invertible over Z_p, so

    H_3(O)(p) = (Z/p^(v_p R) Z)^2,
    k_p(3)=2,    v_p(C_3)=2v_p(R).                          (9)

Here H_3(O)(p) denotes the p-primary subgroup.
One may prescribe arbitrarily many prime factors of R, excluding 3, and arbitrary positive depths at all of them.
They coexist with the same two generators for Gamma and the same exponent n=3.
Thus neither group generator count nor the local rank bound controls the number of contributing primes or their initial valuation depths.

This is not a near-one counterfamily: alpha>R-2, so its Mahler measure tends to infinity.
Nor does it prove that every possible group-theoretic refinement fails.
It isolates the information absent from the particular generator/rank constraints (4)--(7).

<a id="periodic-quotient-trajectory-surjection"></a>
### A fixed finite alphabet realizes every periodic quotient

Choose any integer basis of L, identify it with Z^d, and set

    Q=[0,1)^d,    F={floor(Ax):x in Q} subset Z^d.

This is a finite, parameter-dependent alphabet containing zero.
It is the rounding alphabet already used for finite-alphabet capture in [L G0032](Yin_C_G0239_v1.md#finite-alphabet-capture-and-the-remaining-arithmetic-question); here it gives the additional all-n quotient comparison

    T_n(A,F)=F+AF+...+A^(n-1)F -> H_n(L) surjectively,
    C_n<=|T_n(A,F)| for every n>=1.                         (10)

Proof.
For a class represented by ell in L, first solve (A^n-I)y=ell in R^d, then replace y by its unique representative x_0 in Q modulo L.
The vector (A^n-I)x_0 represents the same class as ell.
Let x_j be the representative of A^j x_0 in Q.
Then x_n=x_0, and

    f_j=A x_j-x_(j+1)=floor(A x_j) belongs to F,
    sum_(j=0)^(n-1) A^(n-1-j) f_j=(A^n-I)x_0.

The sum belongs to T_n(A,F) and represents the prescribed class.
This proves (10).
No expansiveness or absence of unit-circle conjugates was used; nonsingularity of A^n-I was the needed guard.

For completeness, this also gives a direct finite-set entropy attainment statement without requiring a uniform periodic limit.
The elementary estimate C_n<=2^d exp(nm) bounds its logarithmic limsup by m.
For the reverse inequality, collect the finitely many unit-circle eigenvalues in a torus vector z.
None equals 1.
Compactness gives unbounded positive return exponents q_j with z^(q_j)->1; hence z^(q_j+1)->z, whose coordinates differ from 1.
Their logarithmic factors stay bounded along this subsequence.
Expanding eigenvalues contribute log|alpha_i| in the normalized limit and contracting eigenvalues contribute zero.
Thus

    limsup_n (log C_n)/n=m.                                 (11)

This is the same elementary limsup argument retained in [L G0062](Yin_C_G0236_v1.md#adjoint-periodic-index-boundary), applied to the original eigenvalues.
The stronger full limit at the retained War05/Baker scope is not needed here.

The numbers log|T_n(A,F)| are subadditive, so their normalized limit H(A,F) exists.
By (10)--(11), H(A,F)>=m.
Conversely, monotonicity into the rational flow and the accepted rational Yuzvinski formula give H(A,F)<=h(A|Q^d)=m; see [L G0002](Yin_C_G0205_v1.md#rational-primary-formula) for those source interfaces.
Consequently

    H(A,F)=h(A|L)=h(A|Q^d)=m.                               (12)

The size and shape of F depend on A and the chosen basis.
No uniform alphabet size, binary capture, or convergence time is asserted.

<a id="finite-periodic-data-do-not-concatenate"></a>
### Why this does not turn one finite quotient into an entropy gap

Equation (10) converts a local norm certificate into a genuine finite trajectory lower bound.
But a finite-time slope log|T_n(A,F)|/n is an upper bound for H(A,F), since the latter is the infimum of those slopes.
It cannot itself be used as an entropy lower bound.

There is also an exact obstruction to the simplest proposed concatenation.
On H_n(L), A^n acts as the identity.
In a trajectory made of q blocks of length n, the projected block contributions therefore add in H_n(L).
They do not yield an injective encoding of H_n(L)^q.
A proof of exponentially many distinct concatenations would need information about the successive kernel layers, which (1)--(4) do not supply.

The valid finite entropy estimate remains the archimedean norm
bound of L G0074,

    m >= [log C_n-d log 2]/n.

The group interpretation and (10) do not remove its cost d log 2.
Even zero-entropy integral maps can have nontrivial finite coinvariants: A=-I has H_n=(Z/2Z)^d for odd n.
This last example only warns against omitting the nontorsion/asymptotic guard; it does not belong to the positive irreducible target domain.

<a id="rational-versus-integral-group-boundary"></a>
### The original rational flow has different coinvariants

On Q^d, A^n-I is invertible for every n, so

    Q^d/(A^n-I)Q^d=0.

The corresponding rational semidirect product has abelianization Z, and its cyclic-index subgroups do as well.
It is not the finitely generated Gamma used above.
Indeed any finite list of rational vectors lies in (1/q)L for some integer q; this lattice is invariant under A and A^(-1).
The subgroup they generate together with the stable letter cannot contain all of Q^d.

Choosing an integral model for a unit irreducible core preserves its entropy value as in (12), and the existence reductions may use such models.
It does not identify the original rational flow's coinvariants or its semidirect product with those of L.
For an arbitrary rational finite-entropy flow, the separate primary decomposition and capture quantifiers of [L G0002](Yin_C_G0205_v1.md#capture-equivalence) remain necessary.
A two-generator assertion for one cyclic integral core cannot be imposed on the original whole flow.

### Original outcome and remaining scope

The useful positive interface is the explicit surjection (10) and its finite-set witness.
The route boundary is that generator ranks do not aggregate additively across primes and do not bound initial local depths; finite quotient counts also do not concatenate automatically.
The unresolved requirement remains uniform arithmetic coverage for the positive irreducible core, not a missing identification of its cyclic norms with group torsion or toral periodic counts.

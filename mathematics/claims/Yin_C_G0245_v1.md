---
author: Yin
---

# Complete cyclic-norm gaps from dense collisions and bounded residue degrees

This retains the complete original 2026-10-07 proof of [L68](../ledger/Yin_L_G0068_v1.md).
The explicit restricted-class gap and quantitative density equivalences remain separate from the unproved full small-Mahler coverage obligation.

## Statement

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P of degree d>=2, original roots alpha_i and m=log M(P).
Let p be a prime not dividing discP and u_i the d distinct nonzero reduced roots in an algebraic closure of F_p.
No positive power of alpha is required to preserve degree.
For positive integers a,N and 0<gamma<=1, if at least gamma d original indices satisfy u_i^(aN)=1, then every integer r>=0 gives

    m>=d[gamma(r+1)log p-log 2]/(aNp^r).

The full proof uses the nonzero cyclic norm over all original embeddings, including multiplicities when powered degrees drop, with no residue-degree divisor in its valuation.

For a>=1 put c_lambda=#{i:u_i^a=lambda} and nu_(a,p)=sum_lambda c_lambda^2.
If nu_(a,p)>=eta d^2 with 0<eta<=1, one maximum cluster has c_max>=eta d and its Frobenius degree f satisfies f c_max<=d and 1<=f<=floor(1/eta).
Its entire orbit supplies at least eta f d indices of order dividing p^f-1.
Fix an integer p_0>=2 and real constants C>0,0<eta<=1 across the class admitting some prime p<=p_0 not dividing discP and an integer a<=Cd with this collision density.
Then in every degree

    m(P)>=eta log 2/[C(p_0^floor(1/eta)-1)p_0^ceil(1/eta)]>0.

This is an explicit convenient bound, without an optimality claim or a separate bounded-degree completion.
The original large-degree two-level Vandermonde certificate remains valid at its own guarded scope; this proof uses a different integer and needs no such power-degree guard.

With the same p and linear exponent budgets, fixed positive collision density, a cluster containing a fixed positive fraction of all indices, a fixed positive fraction of bounded-Frobenius-degree powered values, and a fixed positive fraction lying in a uniformly bounded powered-value set imply each other up to changed fixed constants.
Precisely, if at least gamma d powered values have residue degree at most K_0, put B_0=sum_(f=1)^K_0(p_0^f-1); then nu>=gamma^2 d^2/B_0.
The same bound holds for gamma d indices in any set of at most B_0 values, whether that chosen set is Frobenius invariant or not.
There is also the direct low-degree bound

    m(P)>=gamma log 2/[C N_* p_0^ceil(1/gamma)],
    N_*=max_(prime p<=p_0) lcm_(1<=f<=K_0)(p^f-1).

Every finite-entropy rational flow whose positive irreducible factors all belong to one such fixed class has finitely many positive factors counted with multiplicity and captures its entropy in a finite-dimensional invariant subspace and a finite set.
No theorem giving these arithmetic budgets for all small-Mahler inputs, or unrestricted Lehmer/capture assertion, is supplied.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:01 |
| status | open |
| reason | Register the entire original proof with all exact domains, costs and source/evidence limits; actual current full review and adoption follow separately. No registration itself supplies independent review, new research, original-source proof audit or numerical certification. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact statement](#statement) | Cyclic-norm bound without powered-degree assumptions, full maximum-cluster argument, all-degree explicit dense/low-degree/finite-value constants and restricted rational capture. |
| argument | [Entire retained proof](#argument) | Every p2 valuation step, complete original-embedding cyclic norm, cluster/Frobenius multiplicities, exact constants and converse density implications, with all arithmetic-coverage limits. |
| dependency | [Unramified collision and local splitting proof](Yin_C_G0242_v1.md#collision-layers-and-frobenius-defect) | Actual simple-root unramified splitting and v(p)=1 normalization, not a new source theorem or degree-preservation assumption. |
| dependency | [Exact first-layer nullity](Yin_C_G0242_v1.md#unramified-powered-collision-nullity) | The semisimple nu=sum c_lambda^2 identity itself; degree guards used for separate order indices or Vandermonde certificates are not imported here. |
| dependency | [Complete rational capture criterion](Yin_C_G0205_v1.md#capture-equivalence) | Positive irreducible weights with multiplicity in arbitrary-dimensional finite-entropy rational flows, without an arbitrary-abelian decomposition or an unrestricted gap. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:05 |
| status | proved |
| reason | Adopt the complete cyclic-norm, maximum-cluster and quantitative density-equivalence theorem after actual whole current self-review of every valuation, original-root multiplicity, exact constant and rational-capture interface. The result has no power-degree assumption, while all fixed prime/exponent/density budgets remain substantive conditional hypotheses; no coverage theorem or independent review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cyclic-norm bound without powered-degree assumptions, full maximum-cluster argument, all-degree explicit dense/low-degree/finite-value constants and restricted rational capture. |
| argument | [Argument](#argument) | Every p2 valuation step, complete original-embedding cyclic norm, cluster/Frobenius multiplicities, exact constants and converse density implications, with all arithmetic-coverage limits. |
| dependency | [Dependency](Yin_C_G0242_v1.md#collision-layers-and-frobenius-defect) | Actual simple-root unramified splitting and v(p)=1 normalization, not a new source theorem or degree-preservation assumption. |
| dependency | [Dependency](Yin_C_G0242_v1.md#unramified-powered-collision-nullity) | The semisimple nu=sum c_lambda^2 identity itself; degree guards used for separate order indices or Vandermonde certificates are not imported here. |
| dependency | [Dependency](Yin_C_G0205_v1.md#capture-equivalence) | Positive irreducible weights with multiplicity in arbitrary-dimensional finite-entropy rational flows, without an arbitrary-abelian decomposition or an unrestricted gap. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0522_v1.md#current-dense-cyclic-finding) | Entire current statement, complete retained argument and every selected interface, self-reviewed; historical findings stay tied to the original inputs and exact stages. |

## Complete retained argument

<a id="argument"></a>

All original mathematical sections and local equation numbers are retained in full.
Only heading depth and established current responsible proof locators change.

<a id="cyclic-norm-residue-density"></a>
### A positive fraction of residues of bounded order suffices

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P of degree d>=2, roots alpha_1,...,alpha_d, and m=log M(P).
Fix a rational prime p not dividing disc P.
In a finite unramified splitting extension of Q_p, all roots are units and have distinct reductions u_i in the algebraic closure of F_p.
The simple-root lifting construction and valuation normalization v(p)=1 are the ones used in [L G0065](Yin_C_G0242_v1.md#collision-layers-and-frobenius-defect).

Suppose that for positive integers a,N and some 0<gamma<=1, at least gamma d of the original root indices satisfy

    u_i^(aN)=1.                                      (1)

For every integer r>=0, put L=aNp^r.
Then

    m >= d[gamma(r+1)log p-log2]/(aNp^r).             (2)

To prove this, first note that v(x-1)>=1 implies

    v(x^(p^r)-1)>=v(x-1)+r>=r+1.                    (3)

For one step, write x=1+y.
In the binomial expansion of (1+y)^p-1, the first term py has valuation v(y)+1, each middle term has at least that valuation, and the last term y^p has valuation p v(y)>=v(y)+1.
This includes p=2 and v(y)=1; possible cancellation only increases valuation.
Iterating proves (3).

Apply (3) to x=alpha_i^(aN) for the indices in (1).
The cyclic resultant

    C_L=Res(P,t^L-1)=product_i(alpha_i^L-1)

is a nonzero integer: none of the conjugates of a nontorsion irreducible input is a root of unity.
Its p-valuation is the sum over all d roots in the chosen splitting field, with no additional division by residue-field degree.
The selected indices give

    v_p(C_L)>=gamma d(r+1),
    |C_L|>=p^(gamma d(r+1)).                          (4)

The other root contributions have nonnegative valuation.
At the archimedean places the elementary bound gives

    |C_L|<=product_i 2 max(1,|alpha_i|)^L
          =2^d M(P)^L.                               (5)

Taking logarithms of (4)--(5) proves (2).
No squarefreeness of a powered polynomial, independence of its powered conjugates, or degree preservation at a, aN or L is needed.
Nonvanishing is the cyclic-root-of-unity test, not a distinct-node Vandermonde test.

<a id="dense-collision-maximum-cluster"></a>
### A maximum cluster has bounded Frobenius degree

For an integer a>=1 let c_lambda be the number of reduced roots whose a-th power equals lambda, and put

    nu_(a,p)=sum_lambda c_lambda^2.

The semisimple identity of L G0065 identifies this with the mod-p mixed-Sylvester nullity.
That modular identity itself does not need any power-degree guard.
Suppose

    nu_(a,p)>=eta d^2,       0<eta<=1.                (6)

Since sum c_lambda=d, one cluster has size

    c_max>=nu_(a,p)/d>=eta d.                         (7)

Let lambda be its value and f=[F_p(lambda):F_p].
Frobenius permutes the multiset of powered roots and preserves cluster sizes, so all f values in this orbit have the same multiplicity c_max.
Hence

    f c_max<=d,       1<=f<=floor(1/eta).             (8)

Every value in that orbit belongs to F_(p^f)^*, and its order divides N=p^f-1.
Thus at least f c_max>=eta f d of the original root indices satisfy (1), with this particular N.
Only this one finite field is needed; no least common multiple across all possible residue degrees enters the dense-collision argument.

<a id="dense-collision-explicit-all-degree-gap"></a>
### Explicit uniform constant at every degree

Fix an integer p_0>=2, a real C>0 and 0<eta<=1.
Consider the nontorsion unit inputs P for which some prime p<=p_0 not dividing disc P and some positive integer a<=Cd satisfy (6).
Set

    K=floor(1/eta),       R=ceil(1/eta).

Equations (7)--(8) and the cyclic-norm estimate imply

    m(P)>=eta log2
       /[C (p_0^K-1) p_0^R] >0.                     (9)

Indeed apply (2) with r=R and N=p^f-1.
The selected fraction gamma=f c_max/d is at least eta.
Since eta R>=1,

    gamma(R+1)log p-log2 >= eta log2.

Finally d/a>=1/C, N<=p_0^K-1 and p^R<=p_0^R.
This proves (9) for all d>=2, with no separate bounded-degree argument.
The constant is a convenient explicit one, not an optimized or claimed sharp value; the larger fraction eta f or a smaller actual order of lambda may improve a specified instance.

In particular the dense-collision class of L G0065 already has this stronger conclusion after dropping its power-degree guards.
The former two-level Vandermonde certificate remains correct at its stated scope; (9) uses a different integer, namely a cyclic norm.
No additional invariant has been counted twice.

<a id="collision-and-low-residue-degree-equivalence"></a>
### Relation to low residue degrees and finite residue-value sets

All following conditions refer to the powered reductions u_i^a, not necessarily to the original u_i.
The same bound p<=p_0 and the same linear exponent budget a<=Cd are retained.

Dense collision implies a positive fraction of low-degree values: by (7)--(8), at least eta d indices have values of residue degree at most floor(1/eta).
In fact the full orbit gives the stronger count eta f d at one degree f.
Equivalently, existence of a cluster of size at least delta d, with fixed delta>0, suffices: it implies nu>=delta^2 d^2 and itself has residue degree at most floor(1/delta).
Conversely nu>=eta d^2 gives such a cluster with delta=eta.
These are quantitative implications between density conditions, not pointwise equalities of their constants.

For the reverse low-degree implication, suppose a fixed constant 0<gamma<=1 and integer K_0>=1 satisfy

    #{i:[F_p(u_i^a):F_p]<=K_0}>=gamma d.              (10)

There are at most

    B_0=sum_(f=1)^(K_0) (p_0^f-1)

possible nonzero values of these degrees: each belongs to one of the fields F_(p^f), f<=K_0.
Overlaps only decrease this count.
Cauchy--Schwarz on their multiplicities therefore gives

    nu_(a,p)>=gamma^2 d^2/B_0.                       (11)

Thus (10) implies a dense-collision criterion with a positive constant independent of d, and (9) applies with eta=gamma^2/B_0.
The same calculation holds whenever gamma d indices take values in a set of at most B_0 elements.
A finite set need not itself be Frobenius invariant: the resulting large cluster and its full orbit restore the bounded-degree conclusion by (8).

One can also apply (2) directly to (10).
Put

    N(p,K_0)=lcm_(1<=f<=K_0)(p^f-1).

All indices in (10) then satisfy u_i^(a N(p,K_0))=1.
Put R_0=ceil(1/gamma) and let N_* be the maximum of N(p,K_0) over the primes p<=p_0.
Equation (2) gives the explicit bound

    m(P)>=gamma log2/[C N_* p_0^(R_0)].               (12)

This is a valid general low-degree route, although the single maximum cluster avoids this larger least common multiple when starting from (6).

Consequently the existence of fixed positive collision density, a fixed positive fraction of bounded-degree powered residues, or a fixed positive fraction in a uniformly bounded set of powered residue values are equivalent up to changing fixed constants.
None asserts that every remaining small-Mahler input admits such p and a within the stated budgets.

<a id="cyclic-norm-gap-scope"></a>
### Entropy implication and remaining arithmetic obligation

The quantity bounded in (2) and (9) is the original logarithmic Mahler measure m(P), hence the original companion-flow algebraic entropy at the already accepted normalization.
There is no new entropy of a d-squared-dimensional auxiliary flow.
For a finite-entropy rational flow whose positive irreducible factors all satisfy one fixed class above, the positive factor weights have the explicit common lower bound (9).
There are only finitely many such factors counted with multiplicity, and [L G0002](Yin_C_G0205_v1.md#capture-equivalence) gives finite-dimensional and finite-set entropy capture.

The coverage problem remains substantive.
Passing to the all-power endpoint is unnecessary for this conditional proof and does not establish modular collision density.
Nor does the mere existence of a finite field containing all reduced roots give the bounded-degree or linear-exponent budgets used above.
Any claim about the full Lehmer problem still needs a theorem providing those budgets or a different arithmetic input.

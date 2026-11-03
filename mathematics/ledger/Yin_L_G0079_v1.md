---
author: Yin
---

# G0001: cyclotomic norm modules and finite-quotient reconstruction

Date: 2026-10-07.
Current complete proof and exact statement: [responsible claim](../claims/Yin_C_G0266_v1.md#cyclotomic-successive-modules).
The original mathematical input below remains fixed; its complete historical review account remains separately located.
Direct argument by assigned AI review_matrix_completion for Yin.
The coordinator proposed examining the cyclotomic norm layers and possible CRT/concatenation improvements after [L G0077](Yin_L_G0077_v1.md).
This note proves exact module and extension formulas and distinguishes their entropy content from periodic-orbit counts.
No computation, new source or novelty claim is used.

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial, d=deg P, O=Z[alpha], and A multiplication by alpha.
Write Phi_n for the n-th cyclotomic polynomial and put

    C_n=|Norm(alpha^n-1)|,
    D_n=|Norm(Phi_n(alpha))|,
    H_n=O/(alpha^n-1)O,
    M_n=O/Phi_n(alpha)O.

All norms and modules here are finite and nonzero in the determinant sense: nontorsion means Phi_n(alpha) and alpha^n-1 are nonzero.
The zero module has cardinality one.
No preservation of degree by alpha^n is assumed.

<a id="cyclotomic-successive-modules"></a>
## Successive modules, not primitive periodic-point sets

For polynomials f,g in Z[t] whose values at alpha are nonzero, write M_f=O/f(alpha)O.
There is an exact sequence

    0 -> M_g --multiplication by f(alpha)--> M_(fg)
      -> M_f -> 0.                                         (1)

The last map is reduction modulo f(alpha).
Its kernel is the image of f(alpha)O, and injectivity of the first map follows by cancelling the nonzero element f(alpha) in the domain O.
It follows that

    C_n=product_(a|n) D_a,
    D_n=product_(a|n) C_a^(mu(n/a)).                         (2)

More strongly, choosing any order of the divisors of n gives a filtration of H_n whose successive quotients are their M_a.
In particular M_n embeds in H_n by multiplication by (alpha^n-1)/Phi_n(alpha), with quotient O/(((alpha^n-1)/Phi_n(alpha))O).
This is an integral module statement, not only a norm factorization.

The cardinalities in (2) use multiplicative Mobius inversion.
For the dual real torus, the number of points of exact period n is instead

    E_n=sum_(a|n) mu(n/a) C_a,

and the number of periodic orbits of length n is E_n/n.
These are additive Mobius inversion formulas.
The set of exact-period points need not be a subgroup, and E_n is not D_n.
The group M_n includes zero and can also contain nonzero points of a smaller A-period.

<a id="exact-cyclotomic-crt-defect"></a>
## Exact CRT defects between two cyclotomic layers

The natural CRT map fits into an exact sequence

    0 -> (fO intersect gO)/(fg)O -> M_(fg)
      -> M_f direct-sum M_g -> O/(fO+gO) -> 0.              (3)

Here fO denotes f(alpha)O.
The last map sends two residue classes to their difference.
If their difference is f(alpha)u+g(alpha)v, subtracting f(alpha)u from one representative supplies a common representative; this proves exactness.
By (1), the kernel and cokernel in (3) have equal order.
Any integer in the polynomial ideal (f,g) annihilates both: for the kernel, multiply an element of fO intersect gO by a Bezout combination of f and g.

For integers 1<=a<b there is the stronger exact polynomial-ideal description

    (Phi_a,Phi_b)=Z[t]                     if b/a is not a prime power,
    (Phi_a,Phi_b)=(p,Phi_a)                if b=a p^j, j>=1. (4)

A self-contained proof also gives the absolute resultant

    |Res(Phi_a,Phi_b)|=1 or p^(phi(a)), respectively.        (5)

First, write an index as p^e s with p not dividing s.
Root factorization gives, for e>=1,

    Phi_(p^e s)(t)=Phi_s(t^(p^e))/Phi_s(t^(p^(e-1))).

Reducing modulo p therefore gives Phi_s(t)^(phi(p^e)); for e=0 the reduction is Phi_s itself.
The roots of Phi_s modulo p are the distinct elements of exact order s.
Thus Phi_a and Phi_b have a common root modulo p precisely when their indices become equal after removing their p-parts.
Since a<b, this is equivalent to b/a being a positive power of p.
The resultant is nonzero over Q.
Consequently it is a unit integer unless that ratio is a prime power, proving the first cases of (4)--(5) by the integer resultant Bezout identity.

For the exceptional case, write a=p^e s and b=p^(e+j)s.
At a primitive a-th root zeta, take the ratio of the derivatives in the displayed polynomial quotient.
The zeros of numerator and denominator are simple there, giving

    Phi_b(zeta)=p zeta^(p^(e+j)-p^(e+j-1))
        *Phi_s'(zeta^(p^(e+j)))/Phi_s'(zeta^(p^(e+j-1))).   (6)

As zeta runs through the primitive a-th roots, both derivative arguments run through the primitive s-th roots with the same multiplicity phi(a)/phi(s).
The absolute norms of the derivative products therefore cancel, and the root-of-unity factor has absolute norm one.
This proves the second case of (5).

Modulo p, Phi_a divides Phi_b by the preceding reduction formula.
Thus u=Phi_b(zeta)/p belongs to Z[zeta].
Equation (5) gives |Norm(u)|=1.
The integer multiplication matrix for u is unimodular, so its inverse sends 1 to an element of Z[zeta]: u is a unit in this order.
Hence p belongs to (Phi_a,Phi_b), while Phi_b belongs to (p,Phi_a).
These two inclusions prove the exceptional ideal equality in (4).

Apply (3)--(4) to the companion order O.
If b/a is not a prime power, then

    O/(Phi_a(alpha)Phi_b(alpha))O = M_a direct-sum M_b.

If b=a p^j, the CRT cokernel is canonically

    F_p[t]/(P mod p,Phi_a mod p),

an elementary abelian p-group of rank

    r=deg gcd(P mod p,Phi_a mod p).                         (7)

The kernel in (3) is annihilated by p and has the same order, so it too is abstractly (Z/pZ)^r.
No canonical identification of kernel with cokernel is asserted.
This conclusion permits repeated reductions and a nonmaximal order O.
The extension M_(Phi_a Phi_b) itself need not split even though both defects are elementary groups.

For another invariant full lattice L, (1) and (3) remain valid with polynomial maps on L.
The exceptional rank becomes dim_Fp coker(Phi_a(A mod p)); it must not be replaced by the companion gcd formula unless cyclicity has been justified.

<a id="cyclotomic-exact-period-away-from-index"></a>
## What the layer's period means away from primes dividing n

Fix n and a rational prime p not dividing n.
Every pair of distinct divisors a,b of n has unit cyclotomic resultant over Z_p: the possible exceptional prime in (5) would divide n.
The Chinese remainder theorem therefore gives

    H_n(p) = direct-sum_(a|n) M_a(p),                       (8)

where (p) denotes the finite p-primary part.
Further, every nonzero element of M_n(p) has exact A-period n.
Its period divides n since Phi_n divides t^n-1.
If a proper divisor k of n fixed an element, the polynomials Phi_n and t^k-1 would both annihilate it.
Their resultant is a unit at p, by (5) applied to the divisors of k, so a Bezout identity forces that element to be zero.

Consequently

    |M_n(p)| = 1 modulo n;                                 (9)

a nontrivial such module has cardinality at least n+1.
The same conclusion holds for the direct sum of all p-primary parts with p not dividing n.
This is the module counterpart of the ideal-primitive part of D_n.
Its primes need not be new rational primes in the earlier norm sequence: different prime ideals above the same rational prime can have different residue orders.
No such rational-prime novelty is inferred.

At primes dividing n, the exact-period conclusion is false.
For the irreducible reciprocal unit P=t^2-3t+1, one has Phi_6(alpha)=2alpha.
Therefore M_6 is the additive group of F_4, because P modulo 2 is t^2+t+1.
Its three nonzero elements have A-period 3, not 6.
Here D_6=4 and the prime 2 already divides C_3=16.
The cyclotomic index labels an integral polynomial factor, not an unconditional primitive-orbit set.

There is also a direct control on the retained small Lehmer input from [J G0009](../computations/programs/Yin_J_G0009/readme.md):

    P=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1.

Direct remainders give

    P(1)=-1,    P(-1)=1,
    P=3t modulo Phi_4,
    P=t-1=t^2 modulo Phi_6.

Thus M_4=F_3[t]/(t^2+1)=F_9, while M_6=0.
The first two values give C_1=C_2=1, so C_4=D_4=9.
Its exact-period-4 point count is C_4-C_2=8, consisting of two periodic orbits, whereas the cyclotomic module has cardinality 9.
These identities are exact polynomial reductions, not root probes.
The irreducible-unit status of this named input is reused at the retained computation/source scope.

<a id="shared-layers-and-cost-accounting"></a>
## Shared layers and different exponent costs

For distinct prime indices p and q, their primitive modules M_p and M_q split exactly by (4).
However

    C_p=C_1 D_p,    C_q=C_1 D_q.

The C_1 layer is shared.
For a set S of distinct prime indices, the norm of the polynomial (t-1) product_(p in S) Phi_p(t) is

    C_1 product_(p in S) D_p
      = product_(p in S) C_p / C_1^(|S|-1).                 (10)

In general, multiplying several C_n counts the D_a layer with multiplicity equal to the number of selected n divisible by a.
This is a legitimate norm of a product polynomial, but it cannot be described as disjoint new primitive data.
The CRT defects in (7) also cannot be counted as additional norm factors: kernel and cokernel have equal order in (3).

Applying the generic cyclic bound separately at exponents n_1,...,n_s gives only

    m >= [sum_j log C_(n_j)-s d log 2]/sum_j n_j,

the n_j-weighted average of their individual certificates.
A better estimate for a product of cyclotomic factors needs an additional joint archimedean estimate; neither (1) nor CRT supplies it.
This note does not rule out such estimates.

<a id="periodic-quotient-profinite-boundary"></a>
## Even all compatible cyclic quotients give a different entropy flow

Let L be any invariant full lattice and retain the canonical maps H_m(L)->H_n(L) for n dividing m.
The entire inverse system has an exact description:

    inverse-limit_(n under divisibility) H_n(L)
      = profinite completion of L = product_p Z_p^d.        (11)

This follows from cofinality, not an approximation theorem.
Each subgroup (A^n-I)L has index C_n and therefore contains C_n L.
Conversely, for every integer q>=1, the matrix A has finite order modulo q, so some n satisfies (A^n-I)L subset qL.
The two families of subgroups are cofinal; the isomorphism of completions is canonical from their maps on L and commutes with A.

On this compact profinite completion A has topological entropy zero.
The partitions into cosets modulo qL are permuted by A, so joining their iterates creates no additional parts.
They refine every finite open cover, by compactness and the neighborhood basis of congruence subgroups.
Hence every open-cover entropy is zero.
Moreover A^n-I is injective on each Z_p^d, because its nonzero determinant makes it invertible over Q_p.
Thus this compact system has only the zero fixed point at every n, although its cokernel still has cardinality C_n by the integer Smith form.

The profinite completion in (11) is not the real torus dual to the discrete lattice L.
The latter has positive entropy m(P) and exactly C_n fixed points.
Consequently even keeping all the cyclic quotients and their transition maps does not justify assigning their inverse-limit flow that positive entropy.
The direction and underlying group of the bridge matter, as in [L G0077](Yin_L_G0077_v1.md#rational-versus-integral-group-boundary).
This does not say that the indexed integers C_n fail to determine m(P) externally: their logarithmic limsup already equals m(P), and the stronger limit is available at the retained War05 scope.
It says that the profinite inverse-limit dynamical construction does not preserve that entropy.

An even simpler boundary applies to separating the layers: the direct sum of the finite flows (M_n,A), over all n, has algebraic entropy zero.
Every finite subset is supported in a finite direct sum of finite invariant groups, so all of its trajectories remain in a finite group.
This construction can use the actual layers of any one positive-entropy unit; it does not reconstruct the original integral flow.

## Proof scope and current outcome

The complete original contribution, source/evidence limits and review account are retained in [R531](../audits/reviews/Yin_R_G0531_v1.md#historical-cyclotomic-author-finding).
Original dates and inspected scopes remain fixed; the current claim has its own actual complete self-review and adoption.

The concrete addition is the exact correction (7) and the flow distinction (11), with actual integral-unit controls.
No uniform lower estimate for enough D_n, no uniform bound on primitive-divisor time, and no new Mahler gap is proved.

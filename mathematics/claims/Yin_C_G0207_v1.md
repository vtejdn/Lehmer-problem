---
author: Yin
---

# Zero Mahler gap gives one rational direct-sum automorphism without finite capture

Provenance: project deduction using accepted rational entropy interfaces.
The original reverse argument is in [L G0001 Section1](../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment), dated 2026-10-06.
The explicit primitive-companion normalization and complete checks were retained by [R G0529](../audits/reviews/Yin_R_G0384_v1.md#zero-gap-direct-sum-independent-finding) on 2026-10-18T10:40.
This material owns the full reusable proof without backdating the present registration or changing the older finding's input.
[G0001 remains paused](../tasks/Yin_T_G0001_v1.md#decision-human-pause-after-closeout).

## Statement

For a nonzero primitive integer polynomial f with all roots counted with multiplicity, use the unnormalized logarithmic Mahler measure m(f)=log|a|+sum_i log max(1,|alpha_i|), where a is its leading coefficient.
Assume inf{m(f): f is a nonzero primitive integer polynomial and m(f)>0}=0.
Then there exist positive integers d_n, rational automorphisms A_n of Q^(d_n), and positive numbers e_n=h(A_n)=m(f_n)<2^(-n-1), for every integer n>=0, such that the single automorphism phi=direct-sum_(n>=0) A_n of the discrete additive group G=direct-sum_(n>=0) Q^(d_n) has total natural-log algebraic entropy

    0<h(phi)=sum_(n>=0)e_n<1.

For every nonempty finite subset F of this same G, H(phi,F)<h(phi), where H uses the positive finite-sum trajectory and its limiting logarithmic quotient.
Every finitely generated Z[t]-submodule for t acting by phi also has entropy strictly below h(phi).
No exact-spectrum theorem, prescribed numerical entropy, finite-set realization on individual blocks or irreducibility of the selected f_n is required.
The assertion is an implication from zero gap; it does not assert that zero gap, such a small-measure sequence or such a nonattaining flow exists unconditionally.

## Current assessment

[Selected decision](#decision-current)

## Assessment history

### Decision current

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:08 |
| status | proved |
| reason | The complete summable-polynomial, primitive-companion and direct-sum proof is retained in C and checked by the selected current agent self-review. The exact conclusion remains conditional on zero Mahler gap and does not resolve G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Zero gap implies one positive finite-entropy rational direct-sum automorphism with failure of finite-subset attainment and finite flow-module capture. |
| argument | [Argument](#argument) | Full primitive normalization, invertible companion realization, directed-union entropy sum and strict finite-support tail proofs below. |
| dependency | [GBV15 rational formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Rational Yuzvinski with actual primitive characteristic-polynomial normalization and full leading-coefficient term; not individual-block finite-set attainment. |
| dependency | [DGB16 basic interfaces](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Finite-subset trajectory convention, monotonicity, directed invariant unions and finite products at their recorded inspection scope. |
| review | [Current zero-gap finding](../audits/reviews/Yin_R_G0498_v1.md#zero-gap-current-finding) | Complete registered statement, retained proof and exact source interfaces; actual contributor self-review, without a new isolated independent claim. |

## Argument

The complete argument below retains L G0001's original mechanism with the explicit normalization and support checks written out in R G0529.
The extra detail is part of the selected proof here, rather than an empty C pointing to reasoning left in a review or ledger.
The original R finding remains at its original L1 input and date.

### Primitive polynomial selection and actual invertible rational blocks

Assume the infimum of positive logarithmic Mahler measures of nonzero primitive integer polynomials is zero.
For each integer n>=0, its defining property permits selection of a primitive polynomial f_n with

    0 < m(f_n) < 2^(-n-1).

Remove every factor t from f_n and change its overall sign if necessary.
The remaining polynomial is still primitive, its leading coefficient a_n is a positive integer, its constant coefficient is nonzero and its measure is unchanged.
Its degree d_n is at least one: a primitive constant is plus or minus one and has zero measure, contrary to the strict positivity.
Zero-root removal introduces neither a missing leading-coefficient term nor a discarded positive measure.
Reducibility and repeated nonzero roots do not obstruct this construction.

Let A_n be the rational companion matrix with monic characteristic polynomial f_n/a_n, acting additively on the discrete group Q^(d_n).
Its determinant is nonzero because f_n(0) is nonzero, so A_n is a rational automorphism.
The least positive integer clearing the coefficients of f_n/a_n is exactly a_n.
Indeed a_n is a clearing integer; conversely, if s clears them then a_n divides s times every coefficient of f_n.
Primitivity supplies an integer Bezout combination of those coefficients equal to one, so a_n divides s.
This verifies the required denominator normalization even for a nonmonic primitive polynomial.

The accepted GBV15-U001 formula therefore gives

    h_alg(A_n) = m(a_n(f_n/a_n)) = m(f_n) =: e_n.

All characteristic roots and their multiplicities, and the full term log a_n, are retained.
Entropy is total natural-log entropy, with no division by d_n.
The source theorem applies to arbitrary rational endomorphisms, so these particular invertible companion maps meet its hypotheses without any additional irreducibility or simplicity requirement.
Only this formula is needed; finite-set realization on each block is not required for the argument.

### One automorphism, a finite total and every finite subset

Take the external direct sum

    G = direct-sum_(n>=0) Q^(d_n),
    phi = direct-sum_(n>=0) A_n.

Both phi and the coordinatewise inverses preserve finite support, so phi is one automorphism of this discrete abelian group.
Let G_N be the sum of blocks indexed from zero through N.
The subgroups G_N form an increasing invariant union equal to G, and finite direct sums are finite direct products.
DGB16-U001 Proposition 2.8(d), iterated finitely, gives

    h_alg(phi restricted to G_N) = sum_(n=0)^N e_n.

Its Proposition 2.8(c), which applies to this actual directed union of invariant subgroups, then gives

    h_alg(phi) = sup_N sum_(n=0)^N e_n = S.

The bounds on e_n imply 0<S<1.
Positivity already follows from e_0>0.
For strictness of the upper bound, e_0<1/2 and sum_(n>=1)e_n<=sum_(n>=1)2^(-n-1)=1/2, so S<1.
No exact numerical value of S is required or asserted.
All sums are of nonnegative finite terms and the total is finite, so no subtraction of infinite entropies occurs.

Every nonempty finite subset F of G is contained in one G_N: each of its finitely many elements has finite coordinate support and the finite union of those supports is bounded in the index set.
Invariance makes every phi-trajectory of F remain in that same G_N, with identical cardinality when computed in G or in G_N.
Consequently

    H(phi,F) = H(phi restricted to G_N,F)
             <= sum_(n=0)^N e_n < S = h_alg(phi).

The last inequality is strict because the omitted tail contains the positive term e_(N+1).
This is nonattainment by every finite subset for the same automorphism phi.
It is stronger than merely producing different flows with the same entropy value and does not restrict finite subsets to subgroups or require that they contain zero.

Likewise, a finitely generated Z[t]-submodule for t acting by phi is generated by a finite set inside one G_N.
That invariant block contains the whole generated submodule, whose entropy is at most the block entropy by monotonicity and hence strictly below S.
This verifies the associated failure of finite flow-module capture in exactly the sense used in L1.

### Source and scope boundary

DGB16-U004 records that the printed reverse proof invokes its externally reported exact-spectrum Theorem7.4, whose original passage and proof were not inspected there.
The present proof uses arbitrary sufficiently small positive primitive-polynomial values, the accepted GBV15 formula and their convergent positive sum instead.
It neither checks nor adopts that exact-spectrum theorem.
The positive-gap direction and its separate Addition Theorem, stabilization and realization inputs remain outside this Claim's selected scope.
The original p-adic proof of GBV15 remains accepted at its recorded statement/applicability depth.

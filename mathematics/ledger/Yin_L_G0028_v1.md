---
author: Yin
---

# G0001: completion criteria coincide on bounded-measure families

Date: 2026-10-06.
The complete current mathematical home is [the responsible Claim](../claims/Yin_C_G0233_v1.md#argument), with [actual whole self-review](../audits/reviews/Yin_R_G0516_v1.md#current-compression-finding).
The original mathematical body remains its historical fixed input and substantive exploration.
Coordinating AI for Yin, with separate assigned AI review and strategy assessment.
This consolidates the matrix-completion route and screens its missing quantifier.
It does not prove a Lehmer gap, construct a counterexample, or claim novelty.

<a id="three-complexities"></a>
## The coefficient estimate closes the third equivalence

Let p be a monic irreducible integral unit polynomial with M(p)>1.
Write S(p) for the least number of nonzero terms of p c over monic cyclotomic products c (repetitions and c=1 allowed).
Write L(p) for the least coefficient l1 norm of such a multiple, and E(p) for the minimum integral matrix excess over characteristic polynomials p c, as in [L G0027](Yin_L_G0027_v1.md#completion-invariants).

All minima exist.
S(p)>=3: a monic polynomial with unit constant term and at most two nonzero terms must be t^d+1 or t^d-1, or a constant unit, so it has zero Mahler measure.
A completion attaining S has M(pc)=M(p).
The [DS17 coefficient-height bound](../audits/literature/DS17/readme.md#sparse-height-bound) therefore gives

    S(p) <= L(p) <= S(p) 2^{S(p)-2} M(p).

The first inequality follows from integral nonzero coefficients having absolute value at least one; the second bounds the length of a support-minimizing completion by its support times its height.
Its completion need not minimize length.

Consequently, for any family with M(p)<=B<infinity, bounded S, bounded L and bounded E are equivalent, using the two bounds in L G0027.
In particular

    S(p)<=K  =>  L(p)<=K 2^{K-2} B.

This supplies the additional coefficient estimate deliberately left open in L G0027's final comparison.
It means that bounded support is not a separate weaker structural route on the bounded-measure core.
No uniform bound for any of these quantities is established.

<a id="near-one-quantifiers"></a>
## An existential near-one formulation is already equivalent to the gap

Consider the assertion that there exist B>1 and K<infinity such that L(p)<=K for every positive irreducible unit p with M(p)<B.
It implies a positive gap: each such p has a cyclotomic completion with at most K terms, so the accepted DS17 gap gives log M(p)>=eta_K; the remaining p have log M(p)>=log B.

Conversely, if the unit-core Lehmer gap holds with M(p)>=gamma>1, choose 1<B<gamma.
The asserted boundedness then holds vacuously, for example with K=3.
Thus the existential choice of the window does not constitute an easier intermediate problem.
The standard reduction to the unit core is the one already fixed in the Task; nonmonic or nonunit irreducible factors have measure at least 2.

A preassigned window, such as 1<M(p)<1.3, together with an actual construction on its inputs, is a more concrete structural target.
Neither implication above asserts that Lehmer alone proves a bound on this fixed window, nor that the bound is false.
The bounded source assessment found no proof or counterfamily for it.
Do not present the existential formulation as additional evidence for Lehmer.

<a id="neutral-multiplicity-screen"></a>
## Why monotonically appending neutral factors is not a uniform algorithm

Fix any positive irreducible unit p and put q_n=p(t)(t-1)^n.
Every nonzero polynomial multiple of q_n retains a root of multiplicity at least n at 1.
The Euler-derivative Vandermonde argument in [L G0026](Yin_L_G0026_v1.md#jordan-complexity-obstruction) forces at least n+1 nonzero terms, hence coefficient length at least n+1 for an integral multiple.
Therefore a procedure that starts from arbitrary neutral padding and only appends factors cannot guarantee a universal final length bound, even at fixed positive Mahler measure.
This obstruction does not apply to a search that discards padding or chooses a new completion of the original p.

For comparison, prescribed neutral padding with bounded multiplicity is controlled.
Extend L to monic unit polynomials by the same cyclotomic-multiple definition.
If c is a cyclotomic product whose maximum root multiplicity is r, then

    L(p) <= L(p c) <= 2^r L(p).

Indeed, choose q_0=p c_0 attaining L(p), and take N divisible by all root orders of c.
Then c divides (t^N-1)^r and the quotient is cyclotomic.
Multiplying p c by c_0(t^N-1)^r/c yields q_0(t^N-1)^r, of length at most 2^r L(p).
For c=1 take r=0.
In particular squarefree neutral padding costs at most a factor 2, regardless of its degree.
Neither this upper bound nor the multiplicity obstruction controls the positive irreducible core.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0004_v1.md#independent-matrix-review), with its original inspected scope and relationship.

## Decision and next discriminating work

Keep algebraic entropy primary and linear growth secondary.
The present conversion chain should no longer generate new routes merely by renaming matrix, length or support complexity.
Continue only with an arithmetic restriction on the positive irreducible core, a concrete completion construction with stated input coverage, or a growth certificate carrying genuinely additional information.
MS25 remains optional until its method is inspected.
All-degree uniformity remains the unsolved requirement.

---
author: Yin
---
# QY26-U001: exact real-neighborhood integral-orbit criterion and its unresolved application

Date: 2026-10-20T11:00.
Human record author Yin.
Root read these selected primary-source passages for the general residual-singleton existence question.

<a id="qy26-u001"></a>
## Read; source statement checked, critical existence input not yet adopted

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Binggang Qu and Chengyuan Yang, Limit distribution of algebraic integral points on curves, arXiv:2609.39505v1,30 September2026,79-page author preprint. No journal or later-version equivalence is asserted.

Passages: Printed/PDF1 contents;2--6 introduction, orbit measures and Theorems A--C;12 Section1.7 conventions;68--69 complete Section7.2 and Theorem7.5 with its displayed proof.

Inspection: Directly text-read the full named statements, conventions and Section7.2 proof. The proof's regular-model reduction, Lemma2.9 capacity argument, Theorem7.1 and its underlying Sections3--6 construction were not independently audited. This is a checked statement/applicability screen, not whole-proof acceptance for a new project existence theorem.


The [actual retained preprint](../../../literature/pdf/QY26--arxiv-v1.pdf) and [complete supplied contents](../../../literature/contents/QY26--arxiv-v1.md) identify the edition.
The source's assertion remains conditional as a project input until the needed critical proof interfaces and actual application are resolved.
No existence or nonexistence of a project residual triple is inferred from this reading.

<a id="arithmetic-orbit-and-real-neighborhood"></a>
## Complete conventions needed here

A projective arithmetic surface is a projective integral flat scheme over Spec(Z) of absolute dimension2; a quasi-projective arithmetic surface is a nonempty open subscheme of one.
For an algebraic point alpha on its generic fiber, alpha' is its closed Q-point and delta_(alpha,C) is the probability measure assigning equal mass1/deg(alpha) to all complex points of that full Galois orbit.
An algebraic integral point is an extension to Spec(O_L) for some number field L; on an affine Z-model each regular coordinate is consequently integral.
The source denotes these points by U(overline Z), not by U(Q) or rational integral points alone.
Weak convergence of probability measures means convergence against every continuous bounded test on the common compact set.

For a compact F in U(C), an R-neighborhood consists of a neighborhood of the closure of F minus U(R) in U(C), together with a neighborhood of F intersect U(R) in the real locus.
It is strictly bigger if its difference from F has an interior point in the complex locus or an interior point relative to U(R).
A compact R-neighborhood in the theorem must also be stable under complex conjugation.
For support entirely in U(R), a finite union of compact real arcs can supply the required relative neighborhood; a mere complex neighborhood does not force all conjugates to be real.
The strict-bigger condition cannot be omitted when the support is a union of real connected components.
The source specifically distinguishes this from an unresolved capacity-one boundary case.

<a id="real-integral-orbit-criterion"></a>
## Exact reported Theorem7.5

Let U/Z be a normal quasi-projective arithmetic surface with nonprojective generic fiber.
Let mu be a compactly supported conjugation-invariant probability measure on U(C), and E a conjugation-stable strictly bigger compact R-neighborhood of its support.
The source asserts equivalence between the following two conditions.

1. There are distinct algebraic integral points alpha_n whose COMPLETE Galois orbits lie in E and whose orbit probability measures converge weakly to mu.
2. For EVERY nonzero global regular function Q in H^0(U,O_U), the integral of log(abs(Q)) against mu is nonnegative.

The second condition ranges over the arithmetic model's full regular-function ring.
It is not a finite list of tested coordinates, a condition on all rational functions, or local solvability at finitely many places.
Zeros may give the value minus infinity, which fails the inequality.
The full compact-orbit requirement keeps escaping conjugates from carrying unrecorded logarithmic mass.

The displayed proof reduces to a regular model, uses Dirichlet units to balance masses over the constant field, translates the regular-function tests to adelic tests and applies the earlier adelic theorem after establishing strict capacity via Lemma2.9.
Those are the actual relied-on interfaces; reading this final descent does not verify the earlier global patching and Eisenstein construction.
Theorem A on page4 uses a complex compact neighborhood, while Theorem7.5 supplies the stronger exact real-neighborhood formulation needed for totally real points.

## Application boundary for the residual singleton

A possible unit-g counterexample must be modeled with integral a,b,c and an integral inverse h of g=c^3-2b^5, together with the two original residual equations.
Its actual arithmetic component, normal model and map back to the original coordinates must first be established.
One must then supply a compact real-locus measure satisfying ALL regular-function tests and a strictly bigger real neighborhood on that model.
Because both g and h would be regular with gh=1, their two tests force the equality integral log(abs(g))=0; checking that equality alone does not check the remaining functions.
These requirements are not currently supplied by the local ramification compatibilities, the f-only control, or any previously read finite-place integral-point theorem.
No such measure, normal-model certificate or exact application has yet been constructed.

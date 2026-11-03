---
author: Yin
---
# QY26-U002: closed-point capacity and the arc-exhaustion portion of Lemma 7.7

Date: 2026-10-20T11:52.
Human record author Yin.
The delegated source reader checked these passages after root identified the possible real-branch application.
Root also independently read the named capacity passages during author discussion.
This is source inspection and separation of the proof's actual inputs, not an independent review or adoption of a project existence theorem.

<a id="qy26-u002"></a>
## Read; the selected capacity mechanism is checked, the full GVF lemma is not adopted without its hypotheses

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Binggang Qu and Chengyuan Yang, Limit distribution of algebraic integral points on curves, arXiv:2609.39505v1, 30 September 2026, 79-page author preprint.

Passages: Printed/PDF 4–5, Section 1.2 conventions and Theorem 1.2; 8–9, Section 1.3.1 loose admissible sets; 17–18, Section 2.2.2 closed-point Green matrix; 26–27, Lemma 3.1 with its complete displayed proof; 69–71, Lemma 7.7 statement and displayed proof through page 71, in particular the complete capacity argument on page 70.

Inspection: Direct reading of the named definitions, formulas, Lemma 3.1 proof and Lemma 7.7 capacity argument. The remainder of the GVF approximation proof, its measure-regularization dependencies and the earlier global construction are not accepted as whole-proof inspected here. The capacity argument's standard canonical-kernel and monotonicity inputs are identified in the separately checked primary Rumely manuscript.


The [actual preprint](../../../literature/pdf/QY26--arxiv-v1.pdf) and [complete supplied contents](../../../literature/contents/QY26--arxiv-v1.md) identify the edition.
The older [U001](Yin_U001.md#qy26-u001) retains its own exact Theorem 7.5 reading boundary.
This unit does not enlarge that earlier inspection retrospectively.

<a id="admissible-and-loose-adelic-sets"></a>
## Definition: admissible and loose admissible adelic sets

Let K be a number field, C/K a projective smooth geometrically integral curve, X a nonempty finite set of closed points, and U=C minus X.
Absolute values are normalized so that the sum over all places of log|a|_v is zero for a in K^times.
For nonarchimedean v the source works on the Berkovich curve over K_v; for real v it uses the complex curve modulo complex conjugation.
This differs from Rumely's geometric-point presentation over completed algebraic closures and requires the Galois averaging described below.

A compact F_v in U_v^an is locally admissible as follows.
At a nonarchimedean place it is the inverse image under a reduction map of an open subvariety of the special fiber of some projective model of C.
At a complex place it is a finite union of closures of connected open sets.
At a real place it is a finite union of such closures and closed intervals in C_v(R).
The same local definition is allowed with U=C.

An adelic set on U is a family of nonempty compact subsets E_v of U_v^an.
It is admissible when every E_v is locally admissible and a single quasi-projective model of U realizes every finite-place E_v as the inverse image of its special fiber under reduction.
A loose admissible adelic set tilde E is an adelic set on C such that every local set is locally admissible in C_v^an, it agrees outside finitely many places with an admissible adelic set on U, and

\[
 \text{for every closed point }x\in X,\quad
 \text{there is a place }v\text{ with }x_v\cap\widetilde E_v\ne\varnothing .
\]

The finite set S={v:X_v intersects tilde E_v} is the set of loose places.
The condition is one place and at least one local point for each closed x.
It does not require every geometric conjugate in that closed-point orbit to belong to a real locus.
For a real-arc application the chosen point must actually be approached by nondegenerate real arcs in the prescribed local sets; isolated-point membership is not a replacement for that part of the proof.

The source's Theorem 1.2 reports that admissible E with cap_X(E)>1 contains infinitely many full algebraic Galois orbits at all places.
That theorem is attributed there to Rum13, Theorem 1.6.
The [actual primary theorem](../Rum13/Yin_U001.md#compact-set-fekete-szego-lrc) is separately checked with its own compactness, nonpolarity, local-form and X-triviality hypotheses.
The QY26 restatement is not used as evidence that an arbitrary finite collection of local integral points already satisfies those hypotheses.

<a id="closed-point-cantor-capacity"></a>
## Definition and normalization: the closed-point Green matrix

For a closed point x of degree d_x and a place v, the source averages the single-local-point equilibrium measures and Green functions with weights deg(x')/d_x over x' in the base change x_v.
For distinct closed points x,y, the local entry c_(x,y,v) is the analogous weighted average over y_v of the Green function with pole averaged over x_v.
The diagonal entry is the regularized single-pole value of the same averaged Green function, with the corresponding weighted pole singularity subtracted.
The subtraction uses a rational function with a simple pole at the closed point, and the sum over all places removes that choice by the product formula.

Equivalently, after passing to a finite normal splitting extension and forming Rumely's normalized global geometric-point matrix Gamma^geom, write O_x for the geometric orbit of x.
The closed-point entry is its block average

\[
 c_{x,y}=\frac{1}{d_xd_y}
          \sum_{a\in O_x}\sum_{b\in O_y}\Gamma^{\rm geom}_{a,b}.
\]

This includes the diagonal block, with the ordinary Robin entries on its geometric diagonal and the Green cross-entries between distinct points of the same orbit.
The global matrix Gamma_X(E)=(c_(x,y)) is symmetric.
For q=|X| and probability vectors s,r in P^q the capacity is

\[
 \operatorname{cap}_X(E)
   =\exp\!\left(-\operatorname{val}(\Gamma_X(E))\right),
 \qquad
 \operatorname{val}(\Gamma)=\sup_{s\in P^q}\inf_{r\in P^q}s^T\Gamma r .
\]

Printed pages 17–18 explicitly identify this as the Galois block averaging of Rumely's geometric-point matrix and state that it gives the same capacity, because that global matrix is Galois-stable.
The splitting-extension and place weights are those in the [primary capacity normalization](../Rum13/Yin_U001.md#cantor-capacity-normalization).
Averaging over the geometric orbits is not removal of the original conjugate multiplicities.
In the application a real branch of a higher-degree closed point therefore contributes with a positive weight to its diagonal block even if the other geometric branches are nonreal.

<a id="arc-capacity-and-exhaustion"></a>
## Checked source mechanism: local arcs and the capacity portion of Lemma 7.7

Lemma 3.1 concerns a smooth projective geometrically connected complex curve, a pole a, and its canonical kernel d_a(y,z)=exp(G_a(y,z)).
The source writes d_a=rho_a exp(eta_a), where rho_a is a metric on the punctured curve and eta_a is continuous on the compact product of the complete curve with itself.
For a path-connected compact H disjoint from a and A=inf_(H times H) eta_a it proves

\[
 \operatorname{cap}_a(H)\ \ge\
       \frac{e^A}{4}\operatorname{diam}_{\rho_a}(H).
\]

The displayed proof takes an arc joining diameter endpoints, maps it continuously onto the interval of distances from one endpoint, uses the triangle inequality for rho_a and the interval capacity length/4, and compares the equilibrium energies.
The complete displayed proof was read.
The equilibrium-measure properties and interval capacity are retained standard potential-theoretic inputs; no independent audit of their earlier proofs is claimed.
For the intended smooth real arcs, the compact sets are nondegenerate continua.

The kernel normalization is supplied explicitly by [Rum13-U001](../Rum13/Yin_U001.md#small-local-disc-interface), printed pages 74–75 of that early manuscript.
There rho_a(b,z) is comparable to the inverted spherical metric, which tends to infinity when z approaches a and b remains fixed and distinct.
The comparison constants are independent of z.
A change of the fixed pole uniformizer changes the single-pole capacity by a fixed positive factor and does not affect divergence.

The FULL statement of Lemma 7.7 additionally assumes a normalized GVF functional ell on K(C) integral with respect to the loose admissible set.
It produces both admissible compact sets E_n of capacity tending to infinity and modified functionals ell_n satisfying additional zero-mass and convergence assertions.
This unit does not adopt that whole conclusion after removing the GVF assumption.

The capacity-only portion on printed page 70 precedes all use of ell.
Its directly read reasoning is as follows.
At each loose archimedean place choose nested admissible compact sets containing successively longer arcs from a fixed point b toward a selected pole a in the local portion of a closed point x.
Lemma 3.1 and the preceding metric comparison force cap_a to infinity, or equivalently the natural-log Robin constant V_a to minus infinity.
The nonarchimedean part of that page instead uses shrinking type-II test points; this alternative is not required for the proposed real-arc application.

The [single-pole energy and Green monotonicity interface](../Rum13/Yin_U001.md#single-pole-robin-and-green-monotonicity) was checked in the primary manuscript.
For nested compact sets, every other Robin term and every cross-Green term is bounded above by its value for the fixed initial nonpolar compact set.
Cross-Green terms are nonnegative.
After the positive Galois averaging, each selected closed-point diagonal tends to minus infinity, while off-diagonal entries satisfy

\[
 c_{x,x}^{(n)}\longrightarrow-\infty,\qquad
 0\le c_{x,y}^{(n)}\le c_{x,y}^{(1)}
 \quad(x\ne y).
\]

Using the uniform probability vector for r in the displayed minimax definition gives

\[
 \operatorname{val}(\Gamma_n)
 \le\frac1q\max_x\sum_y c_{x,y}^{(n)}
 \longrightarrow-\infty,
 \qquad
 \operatorname{cap}_X(E_n)\longrightarrow+\infty .
\]

Thus the page's capacity subargument is independent of the later GVF approximation steps.
This is a separated reading of the actual proof, not a source quotation of Lemma 7.7 with fewer hypotheses.
Using it for a different family of Rumely-compatible local sets still requires a consuming project argument to check all those sets, normalizations and the stated nested-arc and bounded-entry properties.

## Application and inspection limits

The [G0001 inquiry](../../../tasks/Yin_T_G0001_v1.md) may use the two explicitly supplied real branches, if established on the actual smooth projective curve, rather than asserting that every branch of its infinity divisor is real.
A separate proof must establish the precise infinity divisor, finite-place nonpolar invariant compact sets, good-prime X-triviality, regular integral coordinates on those sets, and a strict supercritical member of the constructed sequence.
The source mechanism supplies no missing local point and does not by itself prove these algebraic properties.
It also supplies no norm counterexample until the output point's full conjugate orbit and all integer/unit coordinates are checked.

The inspection was prompted by a critical secondary citation and an apparent ambiguity between closed points and geometric points.
The source follow-up used the retained QY26 preprint and the separately acquired actual Rumely early manuscript.
It resolves the one-local-branch quantifier and the selected kernel, energy and compact-set theorem interfaces.
It does not establish the full global GVF construction, any published-version equivalence, or a completed project existence theorem.
No new mathematical computation or parameter scan was performed.

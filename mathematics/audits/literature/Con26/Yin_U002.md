---
author: Yin
---

<a id="con26-u002"></a>
# Con26-U002: the weighted logarithmic unit lattice in every signature

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Con26](../../../literature/pdf/Con26.pdf), Keith Conrad, *Dirichlet's Unit Theorem*, retained undated 27-page author notes; artifact. The 2026 key is an inspection-year convention.

Passages: Theorem 1.1 p.1; Section 3 pp.3--7, especially the Euclidean embedding and norm p.4, Theorem 3.4 pp.5--6, the weighted logarithmic map p.6 and full-lattice conclusion p.7.

Inspection: 2026-10-12. Root AI for Yin directly read the selected Section 3 proof and inspected the rendered p.7; the D8 author separately read the complex-pair norm and logarithmic weights on pp.4,6--7. The current public author PDF was also opened. Minkowski's convex-body theorem and foundational lattice results remain accepted external inputs, without a new audit of their original proofs.


## Accepted statement and conventions

Let F have signature (r1,r2), where r1 counts real embeddings and r2 counts complex-conjugate pairs.
Let B be any full order in F, not necessarily maximal.
Choose one embedding rho_j from each complex pair.
The map

    L(u)=(log|rho_1(u)|,...,log|rho_r1(u)|,
          2log|rho_(r1+1)(u)|,...,2log|rho_(r1+r2)(u)|)

sends B^times to a discrete full cocompact lattice in

    H={x in R^(r1+r2): sum_i x_i=0}.

Its kernel on B^times is the finite root-of-unity group of that actual order.
This statement is accepted as an established external theorem with its displayed order-level hypotheses checked.
The norm on R^r1 times C^r2 is the product of real coordinates and squared complex absolute values.
Thus the factors 2 in L are necessary.
In signature (0,1) the hyperplane is zero dimensional and the unit group is finite; no nonzero logarithmic direction is available.

The first-page wording says 2r2 pairs.
This is a literal wording slip: the Section 3 construction consistently uses r2 complex pairs, 2r2 complex embeddings, dimension r1+2r2 and squared complex absolute values.
The accepted statement uses those explicit proof conventions.
This issue is checked at the present complex-place interface, rather than importing U001's totally real scope silently.

## Proof mechanism, reliance and limits

The displayed source proof embeds every order as a full Euclidean lattice, identifies its units inside the absolute-norm-one group, and proves compactness of the quotient using Minkowski and finiteness of principal ideals of each bounded integral norm.
Bounded logarithmic coordinates allow only finitely many conjugate polynomials with integer coefficients, giving discreteness.
The continuous surjection from the compact unit quotient to H/L(B^times) forces full rank and cocompactness.
These selected proof steps have been read; their classical foundational inputs have not been recursively re-audited.

The intended consumer is the nonreal reciprocal trace-field construction in [the retained nonreal profile argument](../../../claims/Yin_C_G0013_v2.md#nonreal-profile-working-geometry), which must separately prove that B is a full order, choose actual units from strict cones, control complex phases by one common return subsequence, solve its positive rational system, and pay seed norms, denominators and support costs.
None of those additional deductions is supplied by this source.
No effective unit heights, phase-return rates, rational coefficient bounds, constant Laurent covariance or uniform Mahler gap are asserted by this acceptance.

This new unit preserves the earlier [U001](Yin_U001.md#con26-u001) totally real interface and the old L265/R164 rank-one inspection at their actual historical scopes.
No new artifact acquisition, publication date, formal verification or whole-notes audit is inferred.

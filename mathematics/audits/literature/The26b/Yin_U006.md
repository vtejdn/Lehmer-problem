---
author: Yin
---
# Curves, Riemann--Roch and finite integral closure for the Hankel lattice argument

<a id="the26b-u006"></a>
## Exact source statements and inspection

Use the [curve and lattice source editions](readme.md#curves-and-finite-lattices).
Yin's proof-development agent directly read the following primary passages on 2026-11-05.
This is statement/applicability inspection with the selected displayed proofs identified below, not an independent source-proof review.

The official HTML Section 53.2, Tag 0BXX, Theorem 53.2.6 identifies one-variable function fields over k with their nonsingular projective curve models.
Lemma 53.2.8 says that the model is smooth when k is perfect.
The theorem, lemma and their displayed explanations were read; their cited normalization and compactification ancestors were not independently audited.

The official HTML Section 53.5, Tag 0B5B, equation (53.5.0.3) and Lemma 53.5.2 give Riemann--Roch and duality on a proper Gorenstein curve over a field.
Nonsingular curves are included, and the statement imposes no characteristic-zero restriction.
For a smooth projective curve C with full constant field k, a divisor D and canonical divisor K_C, its divisor form is

    l(D)-l(K_C-D)=deg D+1-g,
    l(D)>=deg D+1-g.

Here l(D) is the dimension over k of the rational sections of the line bundle O_C(D), and g=dim_k H^1(C,O_C).
The displayed statement and its short reduction to the earlier duality formulas were read.
The full duality proof and the cited general degree/intersection machinery were not independently audited.

The already retained Commutative Algebra chapter, revision ed88ff78 compiled 2026-07-14, printed/PDF p.442, Lemma 161.8/Tag 032L, says: for a Noetherian normal domain R with fraction field F and a finite separable extension L/F, the integral closure of R in L is a finite R-module.
Its displayed trace-pairing proof was read.
The proof bounds the integral closure inside the trace-dual of a finite integral basis lattice and uses Noetherianity to conclude finite generation.
The underlying trace-pairing and minimal-polynomial lemmas were not separately audited.

<a id="accepted-curve-lattice-inputs"></a>
## Accepted scope and exact application boundary

These established statements are accepted as inputs at the inspected scope for the finite-field quadratic Hankel argument.
The relevant field k is finite and hence perfect; the extension of k(X) has degree two and is separable.
Its actual rational infinity places give full constant field k, and its nonsingular projective model meets the stated Riemann--Roch hypotheses.
The ring k[X] is a Noetherian normal PID, so Tag 032L applies to its integral closure in that extension.
Finite generation and torsion freeness then give a free rank-two k[X]-module.
The source's theorem is used for this finite-module step; it is not being represented as a new project result.

The finite rational divisor class group, the explicit Hankel kernel/divisor maps, the zero-index calculation, the polynomial-lattice stabilization and the common nonzero progression are project deductions in [C858 v3](../../../claims/Yin_C_G0858_v3.md#general-quadratic-lattice).
Neither the source statements nor this source unit asserts those deductions without their proofs.
The new source scope does not enlarge earlier The26b units or their reviews, and supplies no uniform genus, divisor-order or period bound.

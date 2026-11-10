---
author: Yin
---

# EMRS17: genetic coefficient search and factor output

<a id="emrs17-u001"></a>
## Inspected scope

Use the [identified 2017 PDF body](readme.md#author-upload), whose hosting metadata names a different work.
The reading covers the algorithm in Section 2, printed pages 2621--2622, implementation and results in Section 3 on page 2623, and Sections 4--5 on pages 2623--2624.
The first-page identity and introductory conventions on pages 2619--2621 were also checked in the online PDF's extracted text.
Rendered pages, reported runs, numerical values, irreducibility and novelty comparisons were not independently checked.
Historical census assertions in the introduction are not adopted as current completeness facts.

<a id="genetic-mechanism"></a>
## Mechanism and coefficient domain

The genes are the free integer half-coefficients of a monic reciprocal polynomial, with total Mahler measure as fitness.
Section 2 starts with a random population, retains elites, favors low-measure parents, crosses parent coefficient arrays, and mutates a few genes.
It does not specify reference-list seeding, complete proposal distributions, population size, rates, crossover masks or a reproducible stopping budget.
Section 3 uses MATLAB integer optimization and restricts raw coefficient genes to \(\{-1,0,1\}\).
For whole outputs below 1.3, it tests irreducibility in PARI and also examines factors; those factors explain the listed larger coefficients.
The reported degree-46 and degree-56 factors have measures approximately 1.286061466752 and 1.2839804468828.
Their parent polynomials and parent degrees are not identified in the inspected text.

Section 4 compares the 51 listed examples with substitutions in 48 known bivariate limit-point polynomials.
It attributes 49 high-degree examples to that separate construction; the degree-46 and degree-56 examples survive the reported comparison.
This is a finite source-reported comparison, not exclusion of all possible structured constructions.
Section 5 identifies slowness as a practical limitation.

<a id="applicability-and-comparison"></a>
## Applicability and the first unsupported step

A raw reciprocal ternary population is an actual finite integer domain once its degree is fixed.
Its paired-coordinate convention can be written using the [reciprocal basis](../RS03/Yin_U001.md#reciprocal-neighborhood), now with every independent coefficient restricted to three values.
Crossover can inherit correlated coordinate blocks from two parents, while mutation can introduce coordinates absent from the current population.
These are identifiable proposal ingredients, but the source does not fix one probability law whose run can be reproduced from this paper alone.
Known-reference initialization, a specific mask, or a neutral-output penalty would therefore be local choices, not verified source settings.

Factor discovery legitimately supplies integer polynomials outside the raw ternary box.
It does not show that the complete raw polynomial equals that factor's measure or that the factor degree equals the population's degree.
Consequently, increasing degree because the paper found a degree-56 factor would silently leave the required parent-degree parameter unknown.
An evaluation should separately retain parent coefficients and degree, full measure, extracted factor identity and measure, and neutral factors.

The first unsupported step for a \(1<M<1.2\) search is a benefit in new nonneutral core discovery at equal evaluation cost beyond a fixed seed-and-mutation baseline.
A narrow discriminator is to hold the seed population and total evaluation budget fixed while comparing mutation alone with explicitly specified crossover plus mutation; count previously unseen core identities and whole-output-shell hits separately from known-core recovery and factor-only hits.
No population size, rate or degree is selected by this source inspection.
The reported examples are above 1.2 and supply no shrinking-shell guarantee.
The 2021 [nearest-reference restoration](../SEMR21/Yin_U001.md#restoration-map) is a different proposal mechanism and does not supply the missing genetic settings.

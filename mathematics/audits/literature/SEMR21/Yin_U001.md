---
author: Yin
---

# SEMR21: nearest-reference restoration of integer polynomial coefficients

<a id="semr21-u001"></a>
## Source and inspection scope

The [inspected author deposit](readme.md#arxiv-deposit) is arXiv:2609.20468v1 of the 2021 paper, not a new 2026 research result.
The source reading on 9 November 2026 covers Sections 2.1--2.2 on printed/PDF page 3, the implementation, examples, table and final remarks on page 4, and the introduction and cited-work identities on pages 2 and 4--5.
The algorithm and result-table formulas were checked against rendered pages.
The reported runs, numerical measures, irreducibility checks and novelty comparisons have not been independently reproduced.
The introductory theorems are not adopted as new proof inputs by this unit.
For multivariable normalization, reuse the [BM05 convention](../BM05/Yin_U001.md#bm05-u001): total logarithmic torus integral \(m(P)\), with \(M(P)=\exp(m(P))\).

<a id="restoration-map"></a>
## The actual coefficient restoration mechanism

The source uses the 36-coordinate ternary domain
\[
 P_a(x,y)=\sum_{i,j=0}^{5}a_{6i+j}x^iy^j,
 \qquad a\in\{-1,0,1\}^{36}.
\]
Its reference list \(\mathcal R\) starts from 11 previously reported six-term polynomials and adds eligible earlier examples after padding their coefficient arrays with zeros.
The exact initial array is not printed in this paper.

The following notation states the source's nearest-reference operation.
For selected coordinate positions \(S\subseteq\{0,\ldots,35\}\) and assigned values \(b\in\{-1,0,1\}^{S}\), choose
\[
 r_*\in\mathop{\rm argmin}_{r\in\mathcal R}
          \sum_{k\in S}(b_k-r_k)^2,
 \qquad
 a_k=\begin{cases}b_k,&k\in S,\\(r_*)_k,&k\notin S.\end{cases}
\]
This is the squared version of the source's Euclidean distance on assigned coordinates only; it selects the same nearest references.
The source's seven-step procedure draws a random integer \(N\) between 1 and 10, selects \(N\) coefficient positions, assigns random ternary values, performs this restoration, checks the resulting measure and irreducibility, compares a candidate or factor with the known list when its measure is below 1.37, and repeats.
The original assigned coordinates remain unchanged when the other coordinates are copied.
Section 3 says that recovered representations of previously known values were added to the reference list.

The text says that the draws are random; it does not explicitly specify uniform distributions, dependence conventions, a random seed, or a nearest-reference tie rule.
The paragraph before the procedure mentions fixing a leading coefficient to one, whereas the numbered sampling step selects among all 36 coefficients without spelling out that constraint's implementation.
Thus the paper identifies a concrete restoration mechanism, but does not specify every choice of one reproducible probability law.
Uniform draws and a fixed tie rule would be choices for a local implementation, not verified descriptions of the source run.

<a id="reported-results"></a>
## What the paper reports

Section 3 describes a two-week computation using MATLAB for restoration, Maxima for irreducibility and GNU Octave for numerical Mahler measures.
Its table reports the following two new limit points and representatives:

| Reported measure | Bivariate polynomial |
| --- | --- |
| 1.359375641 | \(1-y-x^2-x^3y^3-x^5y^2+x^5y^3\) |
| 1.368922213 | \(y-y^3-x^2-x^3y^4-x^5y+x^5y^3\) |

These are source-reported decimals, not locally certified intervals.
The paper also gives recovered values with alternative polynomial representatives that fit the selected coefficient domain.
The inspected text supplies no controlled uniform-sampling comparison, success probability, sample count, or shrinking-shell theorem.

The attribution of the initial 11 bivariate references needs care in any reproduction.
Section 2.1 cites El Otmani et al. (2017), while the bibliography separately lists the 2017 *Finding new small degree polynomials with small Mahler measure by genetic algorithms* and the 2019 *Finding New Limit Points of Mahler's Measure by Genetic Algorithms*.
These are distinct source identities, and this inspection does not reconstruct the seed array or silently identify those papers.
No reproduction requiring that reconstruction is selected here.

<a id="sampling-comparison"></a>
## Scope for a whole-polynomial sampling comparison

The restoration map supplies actual integer coefficients and preserves correlations from the reference array; it does not require rounding a continuous proposal.
Each raw completion differs from its selected reference in at most \(N\le10\) coordinates.
The source's candidate class is a finite bivariate coefficient box, even if the reference list changes during the run.
These immediate properties do not give arbitrarily small positive total measure.

The source permits retaining a factor when the full generated polynomial fails the measure threshold.
A whole-output comparison must therefore record and evaluate the raw completion separately from any extracted factor; a factor hit is not evidence that the sampled polynomial has the same measure.
Neither the fixed 1.37 cutoff nor the two reported values supplies a sequence approaching one.
The limit-point interpretation also requires its own specialization argument and does not become an unrestricted positive-shell result from the coefficient-restoration step alone.

For a prospective comparison with the current sampling work, the transferable ingredient is nearest-reference completion after a sparse random assignment.
Its empirical value would require a separately specified reference set, random law, tie rule and evaluation budget, with new whole-measure values distinguished from recovered representations.
This source inspection neither changes a current sampling law nor supplies a comparative-performance conclusion.

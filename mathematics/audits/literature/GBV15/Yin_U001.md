---
author: Yin
---

# GBV15: rational algebraic entropy and finite-set realization

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [GBV15](../../../literature/pdf/GBV15.pdf), arXiv:1111.1287v3, 19 February 2013; acquisition.

Passages: Introduction pp.2--4, finite grids Section 4.1 p.15, the cofinal denominator set pp.21--22, Theorem 4.17 pp.23--24, and Theorem 5.4 p.26; printed and PDF pages agree.

Inspection: Record consolidated 2026-10-06T06:02: coordinating agent for Yin directly checked the exact formula, normalization and realization interfaces against the retained PDF; assigned Section 5 and Section 7 agents also read their needed primary passages.
Statement/applicability check, with selected proof-interface reading, not a complete independent audit of the p-adic proof.


<a id="gbv15-u001"></a>
## GBV15-U001: the two accepted interfaces

State: **Read**; accepted established external inputs for the specified DGB16 source audit.
Acceptance does not upgrade the proof-inspection depth.

Let $N\geq1$ and let $\phi:\mathbb Q^N\to\mathbb Q^N$ be an arbitrary additive endomorphism, equivalently a rational linear map.
Give the group the discrete topology.
For a nonempty finite subset $F$, use the positive sum trajectory

$$
T_n(\phi,F)=F+\phi F+\cdots+\phi^{n-1}F,
\qquad H(\phi,F)=\lim_{n\to\infty}\frac{\log|T_n(\phi,F)|}{n},
\qquad h(\phi)=\sup_F H(\phi,F).
$$

The source's locally compact definition uses Haar measure and a limsup.
On a discrete group compact subsets are finite, counting measure is Haar measure, and the finite-set subadditivity argument gives a limit, so the convention agrees with DGB16.

Let $\chi_\phi(t)\in\mathbb Q[t]$ be the **monic rational** characteristic polynomial, and let $s$ be the least positive integer clearing all its denominators.
Then $p_\phi=s\chi_\phi$ is primitive integral.
The introductory Algebraic Yuzvinski Formula states

$$
h(\phi)=m(p_\phi)=\log s+\sum_{|\lambda_i|>1}\log|\lambda_i|,
$$

with eigenvalues counted with multiplicity and natural logarithms.
There is **no invertibility or nonzero-determinant assumption**.
Removing the $\log s$ term is incorrect for general rational endomorphisms.
For example the formula gives $h(x\mapsto x/2\text{ on }\mathbb Q)=\log2$, not zero.

The second accepted interface is **attainment by a finite set**: for every such $\phi$ there exists nonempty finite $F\subset\mathbb Q^N$ with $H(\phi,F)=h(\phi)$.
Theorem 4.17 directly states $h_A(\phi)=H_A(\phi,E_m)$ for every $m\in\mathcal N(\phi)$, where Section 4.1 defines

$$
E_m=\left\{\sum_{i=1}^N c_i e_i:
c_i\in\{0,\pm1/m,\ldots,\pm m/m\}\right\}.
$$

The denominator family $\mathcal N(\phi)$ is cofinal in the positive integers ordered by divisibility (p.22); hence it is nonempty.
This existence conclusion is all that DGB16 Proposition 7.10(b) requires.
Theorem 5.4 combines realization and Mahler measure on its stated denominator family.
We do not identify differently named denominator families merely by typography.

## Proof and application boundaries

Theorem 4.17 compares trajectory cardinalities with products of local Haar measures and sandwiches their normalized logarithmic growth; its final cofinality step gives the global supremum.
The Mahler-measure conversion uses the preceding local polynomial formula.
The Section 7 agent read the proof of Theorem 4.17, and the coordinator read its statement and terminal supremum step; the earlier approximation, local-volume and polynomial lemmas were not re-audited.
The exact established theorem is retained as an external input, with no concrete objection found at these two interfaces.

The [DGB16 addition audit](../DGB16/Yin_U002.md#dgb16-u002) needs the formula on finite-dimensional rational invariant subspaces and quotients.
The [DGB16 realization audit](../DGB16/Yin_U004.md#dgb16-u004) needs finite-set attainment on the rational divisible hull; its denominator-clearing step transports the attaining set back to the original finite-rank torsion-free group.
These are direct applications, not new project Claims.

The retained artifact is v3, not the journal version.
DGB16's reference to **published Theorem 4.18** is matched by mathematical content to **v3 Theorem 4.17**, not by a claimed full version comparison.
No Bridge Theorem, locally compact extension, formal verification or complete GBV15 proof audit is asserted.

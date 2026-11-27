---
author: Yin
---

# The regulator ratio and the normalized relative regulator

<a id="fs99-u001"></a>
## The bound and its normalization

Equation (0.2) of Friedman and Skoruppa gives absolute constants \(d_0>0\) and \(d_1>1\) such that every finite extension of number fields \(L/K\) satisfies
\[
  \frac{\operatorname{Reg}(L)}{\operatorname{Reg}(K)}
  \ge \bigl(d_0 d_1^{[L:K]}\bigr)^{[K:\mathbb Q]} .
\]
Here \(\operatorname{Reg}(L)\) and \(\operatorname{Reg}(K)\) are the ordinary field regulators. [Equation (0.2), printed page 115](../../../literature/pdf/FS99.pdf#page=1)

For the relative regulator \(\operatorname{Reg}(L/K)\), equation (1.2) uses the same relative-unit group and deleted-place determinant recorded in the [relative-unit convention](../Sun18/Yin_U001.md#relative-units-and-deleted-place-regulator).
Equation (1.3) expresses the relative regulator as the ordinary ratio divided by the index of the norm image modulo roots of unity.
\[
  \operatorname{Reg}(L/K)=
  \frac{\operatorname{Reg}(L)}{\operatorname{Reg}(K)}
  \frac{1}{[\mathcal O_K^\times:\mu_K N_{L/K}(\mathcal O_L^\times)]}.
\]
Thus converting a lower bound for the ordinary ratio into a lower bound for the relative regulator requires an upper bound for this index. [Equations (1.2)–(1.3), printed page 119](../../../literature/pdf/FS99.pdf#page=5)

On printed page 118 the authors propose in (0.5) a lower bound \(f_0 f_1^{r_{L/K}}\) for the relative regulator, with absolute \(f_0>0\) and \(f_1>1\) and with \(r_{L/K}\) the relative-unit rank.
They explain that this conjectural inequality would give a positive gap for Salem numbers, whose field over its trace field has relative-unit rank one. [Equation (0.5), printed page 118](../../../literature/pdf/FS99.pdf#page=4) · [Project calculation for the Salem relative regulator](../../../ledger/Yin_L_G0400_v1.md#salem-relative-regulator-identity)

## The later correction

Chinburg, Friedman and Sundstrom identify an omitted real part of the exponential error term in the estimate of \(J_1\) in the proof of Lemma 5.5.
They report that it affects the derivation of the numerical constants in Theorem 4.1 and its corollaries, that the qualitative Main Theorem survives, and that Sundstrom recovered the stated constants with improved estimates and computations. [NSF-hosted manuscript, page 4, continuation of footnote 2](../../../literature/pdf/CFS22--nsf.pdf#page=4) · [Public manuscript](https://par.nsf.gov/servlets/purl/10382893)

The inspection compared (0.2), (0.5), and (1.2)–(1.3) against the rendered pages of the journal PDF and read the correction report in the NSF-hosted manuscript.
The proof of the Main Theorem and the calculations recovering the numerical constants were outside this inspection. [Journal-edition notes](readme.md#yin-source-edition)

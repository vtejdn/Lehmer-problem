---
author: Yin
---

<a id="bv20-u002"></a>
# BV20-U002: Bernoulli dimension consequences and their boundaries

## Source and inspection

[Source and edition notes](readme.md).

Source edition: BV20, [retained PDF](../../../literature/pdf/BV20.pdf), arXiv:1510.04043v4, 23 April 2021. Bibliographic publication year 2020 does not identify the inspected 2021 revision.

Passages: Introduction pp.1--6, especially Theorems 1--2, (1.2), Remark 6 and Corollary 8; Section 3.4 and Theorem 19, p.22; Section 5, pp.30--31. Printed page numbers equal PDF page numbers.

Inspection: 2026-10-06, human author Yin; direct reading and self-check by the assigned AI source-review agent. The complete mathematical body was read; this unit checks the dimension deduction and source interfaces, not the original proofs of Hochman, Feng--Hu or the separate approximation paper. Rendered pp.3--5 and22 were inspected. Targeted primary-source statements in Hoc14 and BV19 were separately checked as recorded below. No independent human or formal review is asserted.


## Assessment

**Audited within scope** for the deduction of the qualitative Theorem 1, the entropy/dimension identity under the retained external inputs, and the use of Theorem 2 to remove algebraicity.
**Questioned at literal scope** for the endpoint and numerical certification in Corollary 8, and the finer-scale quantifier as transcribed in Theorem 19.
The source's open problems are recorded as source-dated questions, not asserted to remain open today.

<a id="bv20-bernoulli-convolution"></a>
## Bernoulli convolution and dimension

For **\(0<\lambda<1\)**, the Bernoulli convolution \(\mu_\lambda\) is the law on \(\mathbb R\) of the absolutely convergent random series
\[
\sum_{i=0}^{\infty}\xi_i\lambda^i,\qquad
\mathbb P(\xi_i=1)=\mathbb P(\xi_i=-1)=\tfrac12,
\]
with independent digits.
It obeys \(\mu_\lambda=\mu_\lambda^{(n)}*(\lambda^n\mu_\lambda)\).
For a finite real digit law \(\nu_0\), define \(\mu_{\lambda,\nu_0}\) similarly.
The finite walk and its entropy in [U001](Yin_U001.md#bv20-random-walk-entropy) have a larger parameter domain than this infinite measure.

The dimension used here is the almost-sure local dimension of this exact-dimensional self-similar measure, equivalently its Hausdorff and entropy dimensions in this setting.
Exact dimensionality is an established external input; it is not inferred merely from a numerical entropy estimate.
Full dimension **does not imply absolute continuity**.
No such strengthening of Theorems 1--2 or Remark 6 is licensed by this audit.

<a id="bv20-dyadic-entropy"></a>
## Dyadic partition entropy and the dimension identity

Let \(\mathcal D_k=\{[j2^{-k},(j+1)2^{-k}):j\in\mathbb Z\}\), using \(\mathcal D_t=\mathcal D_{\lfloor t\rfloor}\) for noninteger indices.
Define
\[
H(\nu,\mathcal D_k)=-\sum_{I\in\mathcal D_k}\nu(I)\log_2\nu(I),\qquad
H(\nu,\mathcal D_k\mid\mathcal D_l)
=H(\nu,\mathcal D_k)-H(\nu,\mathcal D_l),\quad k\ge l.
\]
This is genuine partition conditional entropy because the partitions are nested in the indicated direction.
It differs from the Gaussian difference notation in U001.

For algebraic \(\lambda\in(1/2,1)\), the source obtains
\[
\dim\mu_\lambda=\min\left\{\frac{h_\lambda}{\log_2(1/\lambda)},1\right\}.\tag{1.2}
\]

The checked deduction has two branches.
Put \(n'=\lfloor n\log_2(1/\lambda)\rfloor\).

- If \(\dim\mu_\lambda<1\), Hochman's finer-scale conclusion gives \(H(\mu_\lambda^{(n)},\mathcal D_{qn'}\mid\mathcal D_{n'})=o(n')\) for each fixed **\(q>1\)**.
  The algebraic separation estimate \(c_\lambda n^{-d_\lambda}M_\lambda^{-n}\) allows one to choose a fixed sufficiently large \(q\) for which the fine dyadic partition separates every distinct finite-walk atom.
  Thus its entropy equals the discrete walk entropy.
  The infinite tail has diameter \(O(\lambda^n)\), giving an \(O(1)\) coarse-partition entropy discrepancy between the finite and infinite laws.
  Dividing by \(n'\) yields (1.2).
- If the dimension is one, the same bounded-tail comparison and the fact that partition entropy does not exceed atom entropy imply \(1\le h_\lambda/\log_2(1/\lambda)\).
  This handles the saturated branch without assuming the strict-dimension hypothesis of Hochman's theorem.

The separation estimate is retained as Garsia [22, Lemma 1.52], with the precise interface quoted and applied on p.22.
Its original proof was not separately read.
For units, the product-formula separation mechanism was also checked in BV20 Lemma 16; the general algebraic interface is not relabeled an independently audited Garsia proof.

## Consequences that survive with a symbolic constant

With the rigorous \(c_0>0\) of [U001](Yin_U001.md#bv20-u001),
\[
\dim\mu_\lambda\ge
\min\left\{\frac{c_0\min(1,\log_2M_\lambda)}{\log_2(1/\lambda)},1\right\}
\quad(\lambda\in\overline{\mathbb Q}\cap(1/2,1)).
\]
In particular, full dimension follows whenever \(\log_2(1/\lambda)\le c_0\min(1,\log_2M_\lambda)\).

The classical Lehmer gap supplies \(\delta>0\) with \(\log_2M_\lambda\ge\delta\) for these real algebraic parameters.
Choose \(\delta\le1\).
Then every algebraic \(\lambda\) sufficiently close to one has \(\log_2(1/\lambda)<c_0\delta\), so (1.2) gives dimension one.
This is Theorem 1 with `0.44` replaced by the proved symbolic constant; no fixed numerical threshold is needed.

Theorem 2 says that the parameters in \((1/2,1)\) with dimension below one lie in the closure of the **algebraic** parameters with dimension below one.
A whole terminal interval without exceptional algebraic parameters therefore has no exceptional parameters at all.
This implication uses a closure statement on the exceptional set, not an unsupported assertion of continuity of dimension.

Remark 6 permits general rational digit laws for **algebraic units** and constants arbitrarily close to one.
When \(\log M_\lambda>\log(1/\lambda)\), a law with sufficiently large \(c(\nu_0)\) makes the corresponding dimension one by the weighted self-similar version of the same entropy argument.
A common denominator rescales the rational digits to integers, preserving dimension.
The source names units whose inverse is neither Pisot nor Salem as a sufficient algebraic class.
Here this last named-class identification is source-checked, while the explicit logarithmic inequality is the transparent reuse interface.
This does not claim a single digit law works for all such parameters or prove absolute continuity.

<a id="bv20-u002-findings"></a>
## Findings and source-version precautions

- **F1 -- medium reuse limitation, Corollary 8 p.5.**
  Its exponent `0.44` depends on explicitly non-rigorous integration on pp.16--17; see [U001 F3](Yin_U001.md#bv20-u001-findings).
  The symbolic sufficient condition above is audited.
  The source also includes \(\lambda\le1\).
  At \(\lambda=1\), its numerical hypothesis holds because \(M_1=1\), but the defining sign series does not converge (its terms do not tend to zero).
  Restrict to \(\lambda<1\), consistently with the measure's domain.
- **F2 -- low, Theorem 19 p.22: finer-scale quantifier/domain mismatch.**
  The printed theorem says `q>0` immediately after defining the entropy difference only with a finer first partition.
  Hochman's original Theorem 1.3 says **\(q>1\)**.
  The proof uses a large \(q\), so changing to that domain does not affect (1.2).
  For \(q<1\), ordinary conditional entropy would be trivially zero in the reversed nesting, but it is not the printed difference formula; do not extend that difference formula and claim its limit remains zero.
  \(q=1\) is harmless and trivial.
- **F3 -- version-sensitive hypothesis, Remark 6 p.4.**
  The [arXiv v4 record](https://arxiv.org/abs/1510.04043v4) explicitly identifies addition of the **unit** hypothesis to Remark 6 as the revision.
  Retain it whenever transferring the general-digit conclusion.
  Earlier copies or the 29-page author PDF do not define the selected audit's hypotheses.
  This is a resolved version boundary, not a new defect in v4.
- **F4 -- terminology, pp.5,31.**
  The source calls \(\lambda\in(1/2,1)\) a Salem number when discussing \(h_\lambda=\log(1/\lambda)\).
  In the usual convention a Salem number is greater than one: this passage concerns its **reciprocal**.
  Its unit-circle conjugates exclude application of Proposition 7.
  The same reciprocal convention must be checked when using nearby Pisot statements.

## Targeted external-source checks

The following checks were performed on 2026-10-06 to settle actual proof interfaces or source-version questions.
They are not full audits of the dependency papers.

| Input | Exact evidence and acceptance boundary |
| --- | --- |
| Hochman entropy concentration | Hoc14, [retained PDF](../../../literature/pdf/Hoc14.pdf), published Annals of Mathematics 180 (2014), pp.776--777, especially Theorem 1.3. The uniform-contraction IFS, arbitrary probability vector, normalized dyadic entropy and \(q>1\) statement were directly checked. They apply to the two maps \(x\mapsto\lambda x\pm1\). Accepted as an established theorem; original inverse-entropy proof unreviewed. The same surrounding text supplies the exact-dimensional/coarse-entropy interface used above. |
| BV20 Theorem 2's formerly forthcoming input | BV19, [retained PDF](../../../literature/pdf/BV19.pdf), *On the dimension of Bernoulli convolutions*, arXiv:1610.09154v3, 13 November 2018, Corollaries 3--4 in the introduction. The exceptional-set closure statement and its conditional terminal-interval consequence were directly checked. Publication metadata: Ann. Probab. 47(4) (2019), 2582--2617. Accepted at statement/application depth; no proof of its quantitative approximation theorem was audited. |
| Exact dimensionality | Feng--Hu, source reference [21], is the attribution given in BV20 p.22 for exact dimensionality of these self-similar measures. The precise coarse-partition entropy interface is also stated in the directly inspected Hoc14 p.776. This unit retains that interface through Hoc14; it does not claim inspection of the original Feng--Hu proof or independently verified earliest attribution. |

The consequential dependency search addressed the suspected \(q\)-quantifier, the concrete forthcoming-reference identification and the needed dimension interface.
Sufficient statements for these applications were found, so no recursive dependency audit followed.
Optional later developments were not adopted as premises or audited results in this record.

## Section 5 and limits

Problems 1--2 ask for growth gaps controlled by the derived length of a solvable group and for a Mahler-based form of such a bound; these are stronger uniformity questions than merely fixing the matrix dimension in U003.
Problem 3 asks for equality \(h_\lambda=\log(1/\lambda)\) at reciprocal Salem parameters, equivalently full dimension by (1.2).
This unit records what the selected source asks, without a present-day claim of unresolved status.

<a id="bv20-mercat-binary-example"></a>
### Mercat's reported binary support deficit

The final degree-six example \(x^6+x^5+x^4-x^3+x^2+x+1\) is attributed to Mercat's private communication and an eight-step count.
In the original 2026-10-06 inspection, the reported count was read but not independently recomputed, so it remained a source-reported finite computation at that inspection's scope.
The source's precise report is that this polynomial has \(M(P)<2\) and its eighth binary support has size strictly less than \(M(P)^8\), giving support growth strictly below \(\log_2 M(P)\).
The report is in the final paragraph before the references, printed/PDF p.31 of the same retained arXiv v4 artifact.
Its attribution is Paul Mercat, bibliography item [36], “Private communication”, on p.33.

The later 2026-10-07 record in [L_G82](../../../ledger/Yin_L_G0082_v1.md#binary-support-counterexample-source) states that the source-review agent and coordinator actually extracted and visually inspected retained p.31.
That bounded source reading established the displayed polynomial, the strict eight-step comparison and the private-communication attribution; it did not acquire or inspect a separate Mercat document, contact either author or audit a private proof.
The source uses base-2 logarithms, whereas the local complete reconstruction uses natural logarithms; dividing by the logarithm base changes both rates by the same factor.
The [complete current algebraic reconstruction](../../../claims/Yin_C_G0273_v1.md#binary-support-counterexample-algebra) and the separate retained [J_G12 diagnostic/verifier](../../../computations/programs/Yin_J_G0012/readme.md) have their own proof and exact finite checking scopes.
They do not turn the source paragraph into an independently inspected private communication or expand this source unit's original proof coverage.
Neither this example nor the cited historical generalizations are needed for Theorems 1,4,5.

No project Claim or Task is created.
Consumers must retain the unit/nonzero domains, base-2 normalization, strict \(\lambda<1\), source-dated problem status and numerical-certification boundary.

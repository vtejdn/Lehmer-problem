---
author: Yin
---

<a id="miy26-u008"></a>
# Miy26-U008: External Interfaces and Version Boundaries

- Source: [Miy26](../../../literature/pdf/Miy26.pdf), registered arXiv v2, especially pp. 2, 5-6, 10, 15, 17 and references pp. 22-23.
- Record: 2026-09-08, the spectral-interface reviewer, for [Miy26 spectral source audit](readme.md#miy26-spectral-source-audit).
- Kind: exact dependency interfaces, primary-source checks, and comparison with existing audits.
This is not a recursive audit of the cited literature.


## Existing audited inputs

Miy26 Theorem 2.1 accurately combines the bounded criterion in Miy22 Theorem 3.1 with its Theorem 4.5:

$$
a\in M:\quad a\in C_{\rm div}(s)\iff [r_i^*,a]\text{ is finite rank for all }i,
\qquad D(s)\cap M=C_{\rm div}(s).
$$

Use [Miy22-U003](../Miy22/Yin_U003.md#miy22-u003) and [Miy22-U007](../Miy22/Yin_U007.md#miy22-u007), retaining their local corrections and finite-tracial hypotheses.
The homogeneous word estimate is reconstructed in [Miy22-U004](../Miy22/Yin_U004.md#miy22-u004); a further Bozejko download is unnecessary for the q=0 inequality consumed here.
Miy26's new step is to prove boundedness from the $L^2$ condition before applying the bounded criterion.
It must not assume all $L^2$ coefficients already act boundedly.

The Haar proof uses [DR97-U002-U004](../DR97/readme.md) in the reduced group representation, together with Lin00's bounded affiliated intersection below.
DR97's Malcev-Neumann branch supplies no identification with $U(L(F_d))$.
The common finite-residual mechanism transfers only after changing the coefficient basis and operator domains.

## MSY23: the field property actually needed

Miy26 cites this work as **[MSY23]**.
Exact statements were read in [arXiv:1905.08187v2](https://arxiv.org/pdf/1905.08187v2), Theorems 1.1-1.2, pp. 3-5, and Definition 6.1, Proposition 6.2, pp. 34-35.
In a finite von Neumann algebra with faithful normal tracial state, the division closure of a bounded tuple $X$ in affiliated operators is the free skew field when $\Delta(X)=d$.
A bounded dual system satisfying $[X_i,D_j]=\delta_{ij}P_\Omega$ implies this condition.
Separately, Theorem 1.2 equates the division-ring property with the strong Atiyah property: every polynomial matrix has integral analytic rank, measured using **unnormalized** matrix trace $\operatorname{Tr}\otimes\tau$.
Integrality is not asserted for the normalized matrix trace.

For semicircles take $D_j=-r_j^*$: the Fock creation/deletion actions give $[s_i,-r_j^*]=\delta_{ij}P_\Omega$.
This checks applicability directly, without importing an entropy-dimension computation.
For Haar generators, let $V_j\delta_w$ delete a final positive $g_j$ and be zero otherwise.
Then $[u_i,V_j]=-\delta_{ij}P_e$, as is checked at the empty word and at each nonempty reduced word; hence $D_j=-V_j$ is a bounded dual system.
The sign is fixed by our convention $[A,B]=AB-BA$.
It also verifies the field assertion reported in preprint Corollary 6.4, p. 36.
Adjoining $u_j^{-1}$ does not enlarge the resulting division ring.

These primary theorems are accepted for the field property used by Corollary 1.2 and Theorem 3.5.
Proposition 6.2's finite-rank trace argument was inspected: multiplying a putative relation $\sum_i[T_i,X_i]=0$ by commutant operators and a dual operator makes every matrix coefficient of each $T_j$ vanish.
The main free-field equivalence proof and its algebraic infrastructure were not independently audited.
The [journal record](https://www.sciencedirect.com/science/article/abs/pii/S0022123623001738) verifies the 2023 bibliographic identity and displays matching principal interfaces; this is not a line-by-line preprint/journal comparison, and all detailed locators above refer to the identified 2020 preprint.

## AP18: canonical $L^2$ operators and affiliated algebra

Miy26's **[AP18]** is the Anantharaman-Popa draft.
The [author-hosted draft](https://www.math.ucla.edu/~popa/Books/IIun.pdf), Theorem 7.2.8, printed pp. 105-106, makes closed affiliated operators a $*$-algebra using closures of the densely defined sums and products.
Theorem 7.3.2, printed pp. 106-107, identifies $\xi\in L^2(M,\tau)$ with the closure of

$$
\widehat x\longmapsto R_x\xi,\qquad x\in M,
$$

as a bijection onto square-integrable affiliated operators.
These statements apply to **tracial von Neumann algebras**, not only factors.
Their precise statements, preceding definitions and applicability were checked; the full foundational proofs were not reviewed.
They are accepted interfaces for U001-U003.
The draft's inner product is antilinear in the first variable, whereas Miy26 uses the opposite convention; the multiplication map and norm identity do not change under this conversion.

The inspected artifact has 338 PDF pages; these locators are PDF pp. 111-113.
Its front matter says “Draft” and supplies no preparation date.
The citation key's year follows Miy26's bibliography; this audit does not assert that the current URL's bytes are the exact 2018 draft.
The directly checked statements, rather than a presumed unchanged book version, are the evidence consumed here.

## Lin00: the Haar bounded intersection

The [primary preprint](https://arxiv.org/pdf/math/9907075v1), Theorem 1.1, p. 3, gives

$$
D(G)\cap W(G)=S(G),
$$

where $G$ is free, $D(G)$ is the division closure of $\mathbb CG$ in affiliated operators and $S(G)$ is its scalar inverse closure in $C_r^*(G)$.
The definitions on pp. 2-3 specify these different ambient algebras.
This is the exact additional interface needed to use bounded rational regularizers in the Haar argument.
The theorem's full unbounded finite-rank characterization is not needed in U003.
The theorem and applicability are accepted, with the original proof unreviewed.
The published [journal record](https://www.sciencedirect.com/science/article/pii/S0022123699935267) identifies JFA 171 (2000), 115-123; the inspected preprint is arXiv:math/9907075v1, 1999-07-12, seven pages.
No equality of journal and preprint pagination is assumed.

## HL00: the R-diagonal Brown-support interface

Miy26 calls this **[HL00]**.
The original author preprint [MPS-RR 1999-27](https://www.maphysto.dk/publications/MPS-RR/1999/27.pdf), Theorem 4.4, printed p. 13 (PDF p. 14), and Proposition 4.6, printed pp. 19-21, were read.
For $a=uh$, where $u$ is Haar, $h\geq0$ is bounded, and $u,h$ are free in a finite faithful tracial setting,

$$
\operatorname{supp}\mu_a=\{z:r_-\leq |z|\leq r_+\},\quad
r_+=\|h\|_2,\quad
r_-=\left(\int t^{-2}\,d\mu_h(t)\right)^{-1/2}.
$$

The extended integral convention makes $r_-=0$ when there is no $L^2$ inverse.
Proposition 4.6 treats scalar $h$, including zero, and distinguishes spectrum from Brown support.
The statements and hypotheses are accepted; the Brown-measure calculation's original proof was not audited.

Miy26 Theorem 1.3, rendered p. 2, omits the modulus around the complex spectral parameter.
Its correct annulus statement uses $|\lambda|$, not an ordering of $\lambda\in\mathbb C$.
This is a local transcription repair, not a different theorem.
The support formula alone does not prove the disk assertion for an arbitrary R-diagonal rational function; its inner radius still requires checking.
The circular example unit performs that check.
The [MaPhySto record](https://www.maphysto.dk/oldpages/publications/publ-131.html) dates the preprint August 1999 and links it to the 2000 published work; no complete comparison with the journal version was performed.

## DHH+25: the free-walk Brown-support comparison

Miy26's **[DHH+25]** was checked in [arXiv:2510.10712v1](https://arxiv.org/html/2510.10712v1), Theorems 1.25 and 1.27-1.28, PDF pp. 13-15.
For normalized, identically distributed, freely independent R-diagonal steps and an independent unitary initial condition, Theorem 1.27 identifies the Brown support as a closed survival-time region minus an explicit disk.
For the circular specialization with $u_0=1$, the inverse $L^2$ norm is infinite, so that disk is empty.
With real nonzero step coefficient $t$ in Miy26, the other source's time is $k t^2$, giving

$$
\operatorname{supp}\mu_{\prod_{j=1}^k(1+t c_j)}
=\overline{\left\{z:
\frac{|z-1|^2(|z|^{2/k}-1)}{|z|^2-1}<t^2
\right\}}.
$$

The radial quotient $(|z|^{2/k}-1)/(|z|^2-1)$ has continuous value $1/k$ on $|z|=1$, so the complete threshold there is $|z-1|^2/k$, as also specified by Theorem 1.28.
At $t=0$, the product is the identity and its Brown support is $\{1\}$; the strict-sublevel formula above does not apply.
The sign invariance for negative $t$ and the separate zero case are justified in [U005](Yin_U005.md#miy26-u005).
This checks the parameter conversion and exact support interface accepted in the circular example unit; the original 109-page paper's proof and random-matrix convergence theorems were not audited.
The [version history](https://arxiv.org/abs/2510.10712v1) inspected on the audit date lists only v1, submitted 2025-10-12.
No later version or publication is asserted.

## Contextual citations and search limits

The homogeneous R-diagonal combinatorial interface from **NS06 [NS06]** is checked and reconstructed in the circular example unit, including its exact author-version and errata evidence; it is not duplicated here.
The remaining introductory references on general strong convergence, Brown-measure existence/support, and random-matrix convergence are contextual to Miy26's motivation and are not inputs to the local boundedness or spectral calculations.
Those general results were not independently audited, and this review makes no current-literature completeness or novelty claim.

On 2026-09-08, searches began with the exact MSY free-field statement, AP square-integrable-operator theorem, Linnell rationality criterion, Haagerup-Larsen support formula, and DHH free-walk theorem.
Primary arXiv, author and publisher sources above were inspected; PDF web screenshots for the initial external sources failed with cache misses, so those reads use extracted primary text and the DHH HTML, not a claimed visual inspection.
The supplied Miy26 formulas were checked in local renders.
No additional external PDF was retained or reclassified as fully audited.
Search stopped after the exact consumed interfaces, parameter conventions, and version limitations were available.
No author contact, unpublished-material transfer, exhaustive errata survey, formal verification, or external human review occurred.

These scoped checks strengthen the external interface evidence available to this audit.
They do not silently rewrite the historical verification statements of the completed Miy22 and DR97 audits, or establish all results from the newly consulted sources.

## Source and inspection

Source edition: Miy26, arXiv:2603.19528v2, dated 2026-04-21; the registered 23-page artifact. Printed page numbers equal PDF page numbers. Other works retain the separate versions and limitations stated in the body.

Passages: Miy26 consumed references on pp. 2, 5-6, 10, 15, 17 and 22-23. Exact external theorem, edition and printed/PDF locators are separately stated for MSY23, AP18, Lin00, HL00, DHH+25 and NS06 in the body.

Inspection: 2026-09-08: identified primary statements, hypotheses and applicability were checked at the explicit per-source scopes, with selected proof steps distinguished from accepted statements. External version uncertainty, extraction/visual-inspection limits and unreviewed original proofs are retained. No recursive whole-source audit, exhaustive errata survey, formal verification or external human review.

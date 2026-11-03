---
author: Yin
---

<a id="smy08-u004"></a>
# Smy08-U004: Dynamical heights, variants, and application interfaces

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Smy08, [retained PDF](../../../literature/pdf/Smy08.pdf): Chris Smyth, *The Mahler measure of algebraic numbers: a survey*, arXiv math/0701397v2, 28 January 2008, corresponding to the 2008 chapter, pp.322–349.

Passages: Complete Sections 12–15, printed pp.338–342 / PDF pp.17–21; equations (39)–(43), all six applications in Section 14, and the relevant bibliography entries. Printed page = PDF page +321.

Inspection: 2026-10-06, human record author Yin; assigned AI reviewer. The complete assigned prose and displayed mathematics were read, and PDF pp.17–21 were rendered and visually inspected. Elementary implications, normalization, missing hypotheses and counterexamples were checked as described below. This is a source-unit self-review; no independent human or formal proof review is claimed. Targeted primary checks and their exact depth are distinguished below.


## Assessment and section coverage

**Audited within the stated scope**, with **questioned assertions as printed**: the factor-count estimate in Section 14.1 lacks restrictions, and the degree-only statement of (42) is false.
Several other passages are useful interfaces once their domains and conventions are supplied.
This unit does not turn every theorem cited by the survey into an independently audited original proof.

| Passage | Coverage and disposition |
| --- | --- |
| Section 12, pp.338–339 | Entire canonical-height paragraph read. Definition and the finite-orbit criterion checked against their standard proof mechanism; the proposed lower bound needs the nonpreperiodic condition. The 2008 assessment of progress is historical. |
| Section 13, p.339 | Entire section read: elliptic, q, metric and areal variants. Integral and metric conventions checked. The word “often” in the elliptic-height comparison supplies no reusable theorem hypotheses. q and areal results remain pointers. |
| Section 14.1, pp.339–340 | Both factorization paragraphs read. Multiplicative argument checked; the trinomial argument needs the reciprocal-factor observation supplied below. Two exact counterexamples qualify the general factor-count sentence. |
| Section 14.2, p.340 | Entire toral-entropy statement read. Integral lattice, invertibility, logarithm and lack of a dimension divisor checked. Classical entropy formula retained as an external theorem. |
| Section 14.3, p.340 | Entire paragraph read. Resultant proof of the displayed Liouville estimate checked, including nonmonic minimal polynomials. Equation (40)'s singleton “max” is redundant. General logarithmic-dependence bounds remain an external pointer. |
| Section 14.4, pp.340–341 | Entire section read, including (41)–(43) and the final root-distance lemma. (41) and the lemma checked directly. (42) fails without a height restriction; (43) leaves its constant undefined. Targeted primary verification is recorded below. |
| Section 14.5, p.341 | Entire unit-lattice statement read. Positive rank, the logarithmic embedding, Euclidean metric and field-of-definition multiplicity are necessary interface data. |
| Section 14.6, p.341 | Entire knot paragraph read. Alexander-polynomial normalization, the restricted pretzel family and the fixed twisting construction are separated from a general Lehmer theorem. Targeted primary checks are recorded below. |
| Sections 15.1–15.3, pp.341–342 | Entire bibliography guide, memoir and acknowledgements read. These supply attribution and historical context, not new mathematical assertions requiring proofs. |

<a id="smy08-canonical-height"></a>
## Canonical height and the dynamical question

For a rational map $f\in K(z)$ of degree $D\ge2$ over a number field, use $P\in\mathbf P^1(\overline{\mathbf Q})$, with poles evaluated projectively.
The absolute logarithmic Weil height gives

$$
\widehat h_f(P)=\lim_{n\to\infty}D^{-n}h(f^n(P)).
$$

The standard height estimate $h(f(P))=D h(P)+O_f(1)$ makes consecutive normalized terms a summable Cauchy sequence; it also gives $\widehat h_f=h+O_f(1)$ and $\widehat h_f(f(P))=D\widehat h_f(P)$.
If the canonical height is zero, the orbit has bounded ordinary height and lies in the fixed number field $K(P)$; Northcott finiteness makes it finite.
Conversely, a finite orbit has bounded ordinary height and hence canonical height zero.
The height estimate and Northcott's theorem are retained standard inputs; their original proofs were not audited here.

The dynamical Lehmer question must be posed for **nonpreperiodic** $P$: $\widehat h_f(P)\ge C(f,K)/[\mathbf Q(P):\mathbf Q]>0$.
Using $[K(P):K]$ instead changes constants for fixed $K$ and must be stated explicitly.
As literally unqualified in the survey, the lower bound fails, for example, for $f(z)=z^2$ and $P=1$.
“Some extension field” must mean an algebraic extension for this absolute algebraic height.
For $f(z)=z^D$ the height is exactly $h(P)$; on nonzero affine points the exceptional points are roots of unity, with $0$ and $\infty$ also preperiodic.
The survey's statement about the absence of estimates is a 2008 report and is not adopted as the present state of arithmetic dynamics.

<a id="smy08-variant-measures"></a>
## Variants: accepted definitions and limited comparisons

Equation (39) uses normalized Haar measure on a complex elliptic curve $E=\mathbf C/L$, a chosen Weierstrass coordinate $x=\wp_L$, and

$$
m_E(F)=\int_0^1\!\!\int_0^1
 \log|F(\wp_L(t_1\omega_1+t_2\omega_2))|\,dt_1\,dt_2.
$$

For nonzero $F\in\mathbf C[z]$, zeros and poles produce locally integrable logarithmic singularities.
For $F=0$ the value is $-\infty$.
Changing a lattice basis preserves Haar measure; changing the curve's coordinate/model need not preserve this expression.
The survey says that $m_E(Nz-M)=2\widehat h(Q)$ “often” holds for $x(Q)=M/N$.
It does not state the model, normalization or local correction hypotheses.
**That identity is retained only as a motivation, not an unconditional arithmetic input.**
References [77]–[79] were not proof-audited; [78] expressly has a corrigendum (JLMS 62 (2000), p.640), which must be checked before using its results.

For nonzero algebraic $\alpha$, the metric variant is

$$
\mathcal M(\alpha)=
\inf_{\alpha=\beta_1\cdots\beta_n,\ n\ge1}
\prod_{i=1}^n M(\beta_i),
\qquad \beta_i\in\overline{\mathbf Q}^{\times}.
$$

The actual additive metric on $\overline{\mathbf Q}^{\times}/\mu_\infty$ is $d([\alpha],[\beta])=\log\mathcal M(\alpha/\beta)$.
Concatenating factorizations proves the triangle inequality; inversion preserves Mahler measure, and root-of-unity factors cost one.
The elementary bounds $\exp h(\gamma)\le\mathcal M(\gamma)\le M(\gamma)$ follow from $h(\prod\beta_i)\le\sum h(\beta_i)\le\sum\log M(\beta_i)$.
They prove positive definiteness modulo torsion.
If all nontorsion Mahler measures are at least $B>1$, every factorization of a nontorsion element has a nontorsion factor, giving $\mathcal M\ge B$.
Conversely $\mathcal M\le M$ transfers a discrete metric neighborhood to a Mahler gap.
This verifies the stated equivalence with Lehmer positivity without claiming the rest of [74] was audited.

The q-analogue has no formula or precise parameter domain in this survey; its $q\to1$ statement remains a pointer to [91,118].
The areal variant replaces circle probability measure by disk probability area measure.
No equality of the areal and circle measures, or transfer of their gap problems, is asserted.
The date phrases in this section are historical.

## Polynomial factorization: a valid mechanism and missing restrictions

Here factor counts concern nonconstant primitive irreducible polynomial factors, with multiplicity; integer content is separate.
For integer polynomials, multiplicativity and $M(P)\ge1$ show that $M(P)<B^2$ permits at most one irreducible factor of measure at least $B$, counting multiplicity.
For a genuine trinomial $P=z^d+\epsilon z^m+\eta$ with $0<m<d$ and $\epsilon,\eta\in\{\pm1\}$, the cited Vicente Gonçalves inequality gives $M(P)^2+M(P)^{-2}\le3$, hence $M(P)\le\varphi$.
The inequality itself remains a cited input [162,117,124].

To apply the nonreciprocal lower bound (15), one also needs to know that every reciprocal irreducible factor of this trinomial is cyclotomic.
Indeed, with $P^*(z)=z^dP(z^{-1})$,

$$
P(z)-\eta P^*(z)=\epsilon(z^m-\eta z^{d-m}).
$$

When $2m\ne d$, every nonzero common root is a root of unity.
When $2m=d$, either $\eta=-1$ and there is no common root, or $\eta=1$ and $z^{2m}+\epsilon z^m+1$ is itself a product of cyclotomic polynomials.
Thus two noncyclotomic factors would have product measure at least $\theta_0^2>\varphi$, a contradiction.
This supplies an omitted elementary implication, not a counterexample to the trinomial conclusion.

**Finding F1 — Section 14.1's uniform factor-count sentence needs two restrictions.**
It prints $O_\varepsilon(d^\varepsilon\|P\|_2^{1-\varepsilon})$ for every fixed $\varepsilon>0$ and all integer polynomials.
For $\varepsilon>1$, the primitive irreducible polynomial $P_N=Nz-(N+1)$ has one noncyclotomic factor while the proposed right side tends to zero as $N\to\infty$.
For $0<\varepsilon<1$, counting the noncyclotomic factor $z$ in $P=z^d$ gives $d$ factors and $\|P\|_2=1$, again a contradiction.
Use $0<\varepsilon<1$ and count factors with **measure greater than one**, or assume $P(0)\ne0$ when using “noncyclotomic.”

The repaired bound is consistent with the cited mechanism.
If $k$ factors have degrees $d_i$ and a retained Dobrowolski consequence gives $\log M(f_i)\ge c_\delta d_i^{-\delta}$, convexity yields $\log M(P)\ge c_\delta k^{1+\delta}/d^\delta$.
Set $\varepsilon=\delta/(1+\delta)$ and use $M(P)\le\|P\|_2$ to obtain the displayed, weaker norm bound.
This checks the deduction, conditional on the usual degree-dependent Mahler lower bound; [54]'s full original proof was not read.

<a id="smy08-toral-entropy"></a>
## Toral entropy normalization

The precise Section 14.2 input is: for $A\in\operatorname{GL}_d(\mathbf Z)$, the toral automorphism $T_A$ of $\mathbf R^d/\mathbf Z^d$ has

$$
h_{\rm top}(T_A)=\log M(\det(zI-A))
 =\sum_{j=1}^d\log\max(1,|\lambda_j|).
$$

Logarithms are natural, eigenvalues are counted with algebraic multiplicity, and this is total entropy, **without division by $d$**.
No hyperbolicity or ergodicity hypothesis is required; eigenvalues on the unit circle contribute zero.
Determinant $\pm1$ is exactly the integral invertibility assumption in the passage.
Its monic characteristic polynomial has unit constant coefficient.
The equality is retained as the classical toral-entropy theorem cited in [96,33,79, Theorem 2.6]; the survey supplies no proof and these original proofs were not inspected.
An algebraic-entropy formula alone would also require an explicit topological/algebraic bridge before replacing this input.

## Liouville bounds and distance from one

For an algebraic $\alpha$ of degree $d$, nonzero $f\in\mathbf Z[z]$ with $\deg f\le N$ and $f(\alpha)\ne0$, the Section 14.3 estimate is

$$
|f(\alpha)|\ge
\bigl(M(\alpha)^N\|f\|_1^{d-1}\bigr)^{-1}.
$$

Let $P=a\prod_{j=1}^d(z-\alpha_j)$ be the primitive integral minimal polynomial, with $a>0$ and $\alpha_1=\alpha$.
The nonzero integral resultant has absolute value $a^{\deg f}\prod_j|f(\alpha_j)|\ge1$.
For $j\ne1$, use $|f(\alpha_j)|\le\|f\|_1\max(1,|\alpha_j|)^N$ and $a^{\deg f}\le a^N$.
This proves the bound, including for nonintegral $\alpha$.
With $f(z)=qz-p$, $q>0$, $p/q\ne\alpha$, it gives

$$
|\alpha-p/q|\ge
\frac1{M(\alpha)\,q\,(|p|+q)^{d-1}}.
$$

The printed $\max(|p|+q)$ in (40) has a single argument: remove the redundant “max,” rather than silently changing the sum to $\max(|p|,q)$.
At $p=q=1$ one obtains (41), $|\alpha-1|\ge2^{1-d}/M(\alpha)$, valid whenever $\alpha\ne1$.
The earlier general statements about dependent logarithms are pointers to [169]; a reusable version would need nonzero algebraic inputs, selected logarithm branches, and its actual coefficient bound.

**Finding F2 — Equation (42) is false under its printed degree-only hypothesis.**
Its claimed right side is $\exp(-(1+\varepsilon)\sqrt{d\log d\log M(\alpha)})$.
Roots of unity already disprove it: $M(\zeta_n)=1$ makes that side $1$, while primitive $\zeta_n=e^{2\pi i/n}$ approach $1$ with unbounded degree.
Excluding them does not suffice.
Fix any $d\ge2$ and take $N\equiv3\pmod4$, $\alpha=(1-1/N)^{1/d}$, the real root in $(0,1)$.
The primitive polynomial $Nz^d-N+1$ is Eisenstein at $2$, so $\deg\alpha=d$, and all roots lie inside the unit circle, giving $M(\alpha)=N$.
But $0<1-\alpha\le1/N$.
For $\log N>(1+\varepsilon)^2d\log d$, this is strictly below (42)'s proposed lower bound.
The family works at any degree above the claimed $d(\varepsilon)$.

The constant improvement from $1$ to $\pi/4$ is also not a bound at unrestricted height.
The primary small-height hypothesis must accompany either attribution.
A 2008 summary must not be promoted to a present-day optimality claim.

The elementary lemma at the end of Section 14.4 is valid as stated: if $\deg F=t$ and $F'(1)\ne0$, some root $a$ satisfies $|a-1|\le t|F(1)/F'(1)|$.
If $F(1)=0$, this is immediate; otherwise $F'(1)/F(1)=\sum_{j=1}^t(1-a_j)^{-1}$ and the triangle inequality proves it, with multiplicities.
No integrality or reality assumption is needed.

## Targeted primary check of the distance estimates

[Dubickas 1998](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/60B9140FFA9F76643562A309A8750D4B/S0004972700032408a.pdf/div-class-title-on-algebraic-numbers-close-to-1-div.pdf), pp.423–425, was read; pp.424–425 were rendered and inspected.
Its introduction explicitly retains $0<h(\alpha)<\delta(\varepsilon)$.
Equation (3) restates the author's earlier bound as

$$
|\alpha-1|>
\exp\!\left[-(\pi/4+\varepsilon)d\sqrt{h(\alpha)\log(1/h(\alpha))}\right].
$$

The corresponding constant $1+\varepsilon$ is attributed there to Mignotte–Waldschmidt.
This verifies the missing small-height boundary; the original 1994/1995 proofs were not audited.
The 1994 journal volume is **47**, not Smy08 bibliography [113]'s printed **4**; the [publisher record](https://www.sciencedirect.com/science/article/pii/S0022314X84710250) confirms volume and pages.

**Finding F3 — Equation (43) does not define $c$.**
Dubickas's p.425 Corollary supplies $c=2\sqrt{2/7}\log7$ and, for every $\varepsilon>0$, an unbounded sequence of degrees with $0<\log M(\alpha)<C_\varepsilon\log d$ and

$$
|\alpha-1|<
\exp\!\left[-(c-\varepsilon)
\sqrt{\frac{d\log M(\alpha)}{\log d}}\right].
$$

Take $0<\varepsilon<c$ for a nonvacuous decay statement.
The primary proof uses a small-coefficient auxiliary polynomial with large vanishing order at $1$, then the logarithmic-derivative lemma.
The theorem statement and that elementary lemma were checked; the Bombieri–Vaaler input and complete construction were not proof-audited.

<a id="smy08-unit-lattice-convention"></a>
## Unit lattice: metric qualification

Assume positive unit rank $r=r_1+r_2-1\ge1$ and set $M_K=\min\{M(u):u\in\mathcal O_K^\times,\ u\notin\mu_\infty\}$.
Existence of this minimum follows from bounded-degree height finiteness.
At rank zero both the minimization set and the set of nonzero unit-lattice vectors are empty; the stated shortest-vector formulation does not apply.

[Kes91](../../../literature/pdf/Kes91.pdf), pp.377–379, was read with all displayed formulas visually checked.
Its actual Euclidean lattice uses $(c_i\log|\sigma_i(u)|)_{i=1}^{r}$, where $c_i=1$ at real places and $2$ at complex places, **omitting the last of the $r+1$ places**.
Its proof treats nonreciprocal and reciprocal units separately; the cardinality improvement to $\sqrt{2/(r+1)}$ appears in the reciprocal case.
The paper's final general theorem uses explicit degree-dependent constants, not the survey's single $M_K$ formulation.
The external Dobrowolski/Smyth proofs were not checked through Kessler.

**Finding F4 — Section 14.5 must specify the lattice metric before its constant is reused.**
Here is a sufficient, explicitly checked convention: take the full vector $\ell_K(u)=(\log|\sigma(u)|)_{\sigma:K\hookrightarrow\mathbf C}$ with conjugate complex embeddings both present, and its ordinary Euclidean norm.
If $n=[K:\mathbf Q]$ and $d_u=[\mathbf Q(u):\mathbf Q]$, the unit product formula gives

$$
\|\ell_K(u)\|_1=2(n/d_u)\log M(u).
$$

Consequently Cauchy–Schwarz and $n=r_1+2r_2\le2(r+1)$ yield

$$
\|\ell_K(u)\|_2
\ge\frac{2(n/d_u)}{\sqrt n}\log M(u)
\ge\sqrt{\frac2{r+1}}\log M_K.
$$

This proves the survey's stated numerical bound under that full-embedding metric.
It is **not** an identification of this norm with Kessler's projected norm.
For the latter, a direct general argument instead gives $\|\operatorname{Log}_{\rm proj}(u)\|_2\ge\log M(u)/\sqrt r$: replace $u$ by $u^{-1}$ if necessary so the omitted coordinate is nonpositive, then apply Cauchy–Schwarz to the remaining positive coordinates.
The uniform stronger $M_K$ assertion in that projected metric is not certified by the inspected passages.
An unweighted vector containing just one coordinate per complex pair is yet another norm and must not be substituted.

## Knot polynomials and twisting

Alexander polynomials are normally defined up to multiplication by $\pm t^j$, which does not change Mahler measure.
The substitution $t\mapsto-t$ also preserves Mahler measure, but is a separate change of variable, not generally multiplication by such a unit.
Thus the survey's $L(-t)$ identification is enough for its Mahler-measure claim while still requiring sign care for a polynomial identity.

[Hir01 author version](../../../literature/pdf/Hir01.pdf), dated 19 November 2001, is linked “with corrections” on the [author's publication list](https://www.math.fsu.edu/~hironaka/papers/).
Pages 2–3 were read and rendered.
The stated family has positive $p_1,\ldots,p_k$ twists and $k-2$ twists of order $-1$; for $k\ge3$, Theorem 1.2 identifies its Alexander polynomial with $Q_{p_1,\ldots,p_k}(-t)$.
Theorem 1.3 restricts the minimum to members **with a Salem factor**.
Cyclotomic members have measure one and cannot be included in a minimum equal to $M(L)>1$.
This restricted theorem is accepted as an external statement; its topology and minimality proof were not audited.

The displayed formula for $Q$ gives $Q_{2,3,7}(t)=L(t)$ by exact expansion.
The author PDF's Lemma 1.1 instead prints $L(t)=Q_{2,3,7}(-t)$, a sign inconsistency with its own formula.
Theorem 1.2 and the expansion yield $L(-t)$, agreeing with Smy08.
This is a defect of the inspected auxiliary artifact, not a newly established defect in Smy08.
The separately published [2002 erratum](https://doi.org/10.4153/CMB-2002-026-7) was located, but its complete text was not read; no claim is made that every correction was checked.

For [CK05](../../../literature/pdf/CK05.pdf), the primary text of Theorem 2.2 and its proof, pp.6–7, was read online.
Fix a link diagram and an encircling unknot $U$; $(-1/m)$ surgery on $U$ adds $m$ full twists at that fixed site.
Jones Mahler measures converge to a two-variable polynomial's measure.
The proof constructs $P(t,t^m)$, then uses Boyd–Lawton specialization; multiplying the rational expression by $1+t$ clears the relevant denominator without changing Mahler measure.
Representation-theoretic and specialization inputs remain external.
Hyperbolicity is unnecessary for this polynomial theorem.
It is not a claim about arbitrary changing surgery families, nor an identity with hyperbolic volume, nor a new positive Lehmer gap.

## Primary-access provenance

The selected Kes91, Dub98, Hir01 and CK05 PDFs were acquired and retained on 2026-10-06.
The coordinating agent checked absent destinations, retained each file exclusively and rehashed the bytes.
These are targeted supporting inspections, not additional full-paper audits.

## Dependencies and intended use

This unit accepts standard height inequalities, Northcott finiteness, integer resultant integrality, Mahler multiplicativity, the nonreciprocal lower bound (15), the cited Vicente Gonçalves inequality, and the classical toral-entropy theorem only at the inspection depths specified above.
It gives reusable conventions and checked elementary deductions.
It supplies neither a new Lehmer gap nor a general theorem turning elliptic, dynamical, lattice or knot expressions into such a gap.

All assertions about what was “known,” “recent,” or unavailable are dated to the selected 2008 source.
Sections 12–15 do not establish the current global status of the associated questions.
No research task or mathematical claim was allocated from this audit.

## Verification facts and revision status

- All assigned survey text was read, and all five containing PDF pages were rendered and inspected, rather than trusting extracted formulas.
- Counterexamples F1 and F2 are exact algebraic arguments, not numerical searches.
  The resultant and logarithmic-derivative deductions were independently reconstructed by this reviewer.
- Exact integer coefficient convolution verifies $Q_{2,3,7}=(1,1,0,-1,-1,-1,-1,-1,0,1,1)$ in ascending powers, agreeing with $L$ and detecting the auxiliary source's sign typo.
- Original proofs cited only through Smy08 remain external.
  Primary-page inspections above are not full-paper proof audits.
- The coordinating agent read and integrated this fixed source unit and checked its elementary counterexamples.
  No independent second whole-source review is asserted.

## Revisions and downstream effects

2026-10-06: first fixed source unit for Sections 12–15.
Consumers must carry the dynamical nonpreperiodic condition, the repaired factor-count domain, the small-height boundary for (42), and explicit lattice/knot conventions.
The selected source bytes are preserved; corrections are recorded here, not silently inserted into the source.

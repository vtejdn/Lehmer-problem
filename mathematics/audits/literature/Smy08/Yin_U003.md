---
author: Yin
---

<a id="smy08-u003"></a>
# Smy08-U003: Small measures, discriminants, algebraic values and counting

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Smy08, [retained PDF](../../../literature/pdf/Smy08.pdf), arXiv:math/0701397v2, 28 January 2008. The inspected object is the retained author preprint, not an independently compared copy of the published chapter.

Passages: Entire Sections 8--11, printed pp.335--338 / PDF pp.14--17, equations (33)--(38), and the bibliography entries cited below. Printed page = PDF page + 321.

Inspection: 2026-10-06, human author Yin; assigned AI source reviewer. All assigned text was read, and complete PDF pp.14--17 were rendered and visually inspected. Elementary implications and counterexamples below were checked directly. Selected original statements were traced online; their exact access and proof limits are recorded below. This is self-review of this unit, not independent human review or an audit of all the cited papers.


## Assessment and conventions

**Audited within scope** for the definitions, elementary discriminant/separation checks, the Perron implication for algebraic integers, the displayed local boundary checks, and the explicitly traced statement interfaces.
**Read** for the historical computations and the remaining secondary reports.
**Questioned** for the literal additive-group claim, the unrestricted distance estimate (37), and reuse of the unqualified counting statements.
These localized defects do not refute Lehmer's conjecture or the accurately qualified external results.

Throughout, $M$ is the multiplicative Mahler measure and $m=\log M$ uses the natural logarithm.
For an algebraic number its minimal polynomial is primitive in $\mathbb Z[z]$ and has positive leading coefficient.
Write $\operatorname{house}(\alpha)=\max_\sigma|\sigma(\alpha)|$.
The degree of $M(\alpha)$ need not be the degree of $\alpha$.
Discriminants below are polynomial discriminants; replacing one by a number-field discriminant requires a separate index/denominator check.

### Section 8: finite searches and their domain

The surveyed searches concern nontrivial small measures $M>1$ of algebraic integers, or houses of nonzero algebraic integers that are not roots of unity.
They are historical results as reported in the 2008 version, not claims about present records.
The survey's shorthand “algebraic numbers” in the minimum-house discussion cannot mean arbitrary nonintegral numbers: rational scaling makes the house arbitrarily small in every fixed degree.
The search domain must retain integrality and the trivial exceptions from the preceding house discussion.

The reported coverage is: Boyd's reciprocal measures $M\le1.3$ through degree 20 and coefficient height one through degree 32; Mossinghoff's extension to degree 24 and height-one degree 40; the 47 Salem numbers below 1.3 complete through degree 40; and the later Flammang--Rhin--Sac-Épée searches below $\theta_0$ through degree 36 and below 1.31 through degree 40.
For the house, Boyd's tables cover degrees at most 12, reciprocal degrees at most 16, and Rhin--Wu's later search reaches degree 28.
These enumeration/completeness claims were read in Smy08 but their programs, tables and original correctness proofs were not rerun or audited.
The at-most-four-monomials statement is a conjecture suggested by the data, not a theorem established here.

<a id="smy08-salem-number"></a>
A **Salem number** here is a real algebraic integer $\tau>1$ of degree at least four, with conjugates $\tau^{-1}$ and all remaining conjugates on the unit circle.
The source's reciprocal/unique-outside-circle description gives this characterization.
Consequently $M(\tau)=\tau$.
This definition does not identify every reciprocal algebraic unit with a Salem number; several reciprocal pairs may lie off the circle.

<a id="smy08-discriminant-separation"></a>
## Section 9: discriminant and separation interfaces

Let $P(z)=a_0\prod_{i=1}^d(z-\alpha_i)$ be a nonzero complex polynomial of degree $d\ge2$, and put
$$
\operatorname{disc}(P)=a_0^{2d-2}\prod_{i<j}(\alpha_i-\alpha_j)^2,
\qquad \operatorname{sep}(P)=\min_{i<j}|\alpha_i-\alpha_j|.
$$
Smy08 (33), attributed to Mahler [103], is
$$
|\operatorname{disc}(P)|\le d^dM(P)^{2d-2}.
$$
The elementary mechanism was checked: apply Hadamard's inequality to the Vandermonde matrix, whose $i$th row has norm at most $\sqrt d\max(1,|\alpha_i|)^{d-1}$, square, and include $|a_0|^{2d-2}$.
Repeated roots cause no problem for this non-strict upper bound.
For nonzero discriminant its exact logarithmic consequence is
$$
2(d-1)m(P)\ge\log|\operatorname{disc}(P)|-d\log d.
$$
Thus a discriminant argument must overcome the **$d\log d$ subtraction**.
A lower bound on root discriminant merely exceeding one does not supply a degree-independent Mahler gap.

The survey's conditional observation $|\operatorname{disc}(P)|\ge(cd)^d\Rightarrow M(P)\ge c^{d/(2d-2)}$ is algebraically correct for $c>1$ and $d\ge2$.
Its stated proposed premise “for all irreducible $P\in\mathbb Z[z]$” cannot hold: $\Phi_3=z^2+z+1$ has $|\operatorname{disc}|=3<4c^2$.
This is an impossible premise, not a false conditional implication.
Any usable strategy must specify a noncyclotomic class and actually establish the stronger discriminant estimate there; no such estimate is established by this paragraph.

**Matveev parameter, (34).** The original theorem is accepted here for a nonzero **algebraic integer** $\alpha$ of degree $d\ge2$ satisfying $[\mathbb Q(\alpha^p):\mathbb Q]=d$ for every prime $p$: for every $\varepsilon>0$ there is a threshold $\delta_0(\varepsilon)>0$ for which
$$
M(\alpha)\ge \exp\!\left((2-\varepsilon)
 \left(\frac{\log\log\delta}{\log\delta}\right)^3\right),
\qquad
\delta=\max\left\{\frac d{|\operatorname{disc}(\alpha)|^{1/d}},\delta_0(\varepsilon)\right\}.
$$
The retained Smy08 PDF omits the absolute-value bars in $\delta$.
They are necessary: negative discriminants occur.
The [Mat96](../../../literature/pdf/Mat96.pdf), definition of $\Delta$ on p.415 and Theorem 1 on p.416, was subsequently acquired and these pages visually inspected.
It confirms the constant, the existential threshold, integrality and the all-prime restriction.
This statement is accepted on the displayed degree-at-least-two domain; the original proof was not audited, and no explicit numerical threshold is supplied here.
The logarithms require $\delta>1$.
This is not an unconditional replacement of degree by a bounded parameter, and its degree-preservation hypothesis cannot be dropped.
Reuse outside algebraic integers needs an additional argument, rather than quoting the original theorem with integrality omitted.

**Root separation, (35).** The source prints $M(P)^{-(m-1)}$ with no degree parameter $m$ defined there.
Its consistent correction is
$$
\operatorname{sep}(P)>
\sqrt3\,|\operatorname{disc}(P)|^{1/2}d^{-(d+2)/2}M(P)^{-(d-1)},
\qquad \operatorname{disc}(P)\ne0.
$$
Both the variable repair and the distinct-root hypothesis matter.
With $P=(z-1)^2$, the source's unrestricted strict inequality would read $0>0$.
The corrected estimate was checked directly by choosing a closest pair with $|\alpha_1|\le|\alpha_2|$, replacing the second Vandermonde row by its difference from the first, and factoring out $\alpha_2-\alpha_1$.
Its $j$th remaining entry is bounded by $j\max(1,|\alpha_2|)^{d-2}$.
Hadamard and $\sum_{j=1}^{d-1}j^2<d^3/3$ give the displayed strict estimate.
This elementary source repair is not a claim to have re-audited Mahler's original paper.
An EMS reprint was located online, but its image-only pages were not successfully inspected as original proof evidence in this review.

**Totally positive case, (36).** For a totally positive algebraic integer $\alpha$ of degree $d\ge2$, with $\delta_1=|\operatorname{disc}(\alpha)|^{1/[d(d-1)]}$, the reported lower bound is
$$
M(\alpha)\ge\left(\frac{\delta_1+\sqrt{\delta_1^2+4}}2\right)^{d/2}.
$$
This exact statement was checked in [Rhi04](../../../literature/pdf/Rhi04.pdf), Theorem 1, printed p.156 / PDF p.2, including the subsequently acquired rendered page.
It is accepted at statement/hypothesis scope.
The original auxiliary-function proof and the claimed derivation from Zaïmi [172] were not audited.
Total positivity is essential to this input; it does not resolve the general reciprocal-unit family.

<a id="smy08-perron-mahler-value"></a>
## Section 10: algebraic properties of the value

Smy08 calls an algebraic integer a Perron number when it has exactly one conjugate of maximal modulus.
To avoid importing a convention silently, the usual stricter terminology here will mean a **real algebraic integer $\beta>1$ whose other conjugates have modulus strictly below $\beta$**.
The source's abbreviated definition permits boundary values such as 1.
Therefore its assertion about every algebraic integer $\alpha$ translates to: $M(\alpha)=1$, or $M(\alpha)$ is a Perron number in the stricter sense.
The case $M(\alpha)=1$ includes $\alpha=0$ as well as roots of unity.
This is a convention/exception clarification, not a counterexample to the source's own abbreviated definition.

For algebraic integral $\alpha$, the product formula proves this directly.
The product of precisely the conjugates outside the circle, with the appropriate sign, is the positive real algebraic integer $M(\alpha)$.
Every Galois image is a product of the same number of conjugates.
A different selected subset loses an outside-circle factor in favor of one of modulus at most one, so its modulus is smaller; an unchanged subset gives the same value.
No unit condition is needed for this implication.
If $\alpha\ne0$ and $M(\alpha)<2$, its primitive minimal polynomial has leading and constant coefficients of absolute value one, so $\alpha$ is a unit.
The nonzero hypothesis is indispensable for that latter reduction.

The other surveyed interfaces and their limits are:

| Passage | Exact usable content and actual review depth |
| --- | --- |
| Boyd [35], p.337 | If $\beta=M(\alpha)$, every other conjugate lies in $\beta^{-1}<\lvert z\rvert<\beta$, or equals $\pm\beta^{-1}$. Dubickas [67], Theorem A, pp.196--197, extends the original integral-$\alpha$ statement to arbitrary algebraic $\alpha$; $\alpha=0$ is separately vacuous. The short product/complement argument was read. Its p.197 printed $\lvert\beta'\rvert\ge\beta$ contradicts the immediately preceding strict upper bound and must read $<\beta$. This typographical repair leaves the theorem intact; Boyd's original proof was not audited. |
| Perron realization [70] | The statement that an integer multiple of a Perron number is a Mahler measure is secondary here, with the positive, $>1$ convention. The source's abbreviated definition must exclude $\beta=0$ for this reverse statement, since all integer multiples of zero are zero and no Mahler measure is zero. The theorem does not say every Perron number is a Mahler measure. The $1+\sqrt{17}$ question is historical, not verified current status. |
| Reciprocity examples [36] | The degree-four Pisot/degree-six reciprocal example and the family $z^4-qz^3+(q+1)z^2-2z+1$ with integer $q\ge3$ and measure $(q+\sqrt{q^2-4})/2$ were read, not independently checked for every parameter. They are reported counterexamples to preservation of reciprocity in either direction. |
| Multiplicative closure [52] | The survey reports that $(1+\sqrt2)(2+\sqrt3)$ is not itself $M(\alpha)$ although the factors are. The original nonrealization proof was not inspected. The distinction from arbitrary polynomial measures is sound: $M(PQ)=M(P)M(Q)$ makes the latter set multiplicatively closed. |
| Equal measures [32], p.338 | The displayed degree-six and degree-eight polynomials and their value $1.746793\ldots$, with the described pairwise-root-product explanation, were read as a secondary example; exact irreducibility, root labels and equality were not computationally or independently proved. The elementary substitution identity $M(P(\pm z^k))=M(P)$ is valid for integers $k\ge1$; $k=0$ is excluded. |

### F1: the additive group is stated incorrectly

The last paragraph of p.337 attributes to Dubickas [69] that the additive group generated by all Mahler measures equals all real algebraic numbers.
The correct target is **all real algebraic integers**.
The Dub04 indexed abstract and Theorem 3, p.281 explicitly retain integrality.
The primary PDF's browser opening failed; the exact abstract/theorem passage returned by primary-source search was read, not its complete proof.

The error is independently decisive: each Mahler measure of an algebraic number is a real algebraic integer, as also stated at the start of the original paper.
Integer linear combinations remain algebraic integers, so $1/2$ cannot belong to the generated additive group.
By contrast the multiplicative group may use inverses: the reported correct multiplicative target is all positive real algebraic numbers.
Neither group-generation statement says that every element of the target is itself one Mahler measure, nor that small differences/ratios yield small nontrivial Mahler measures.

### F2: distance estimate (37) omits $\gamma\in\mathbb R$ and $\gamma\ge1$

Let $\gamma$ be a **real algebraic number with $\gamma\ge1$**, of degree $n$ and positive primitive leading coefficient $c$.
Let $\beta=M(\alpha)$, of degree $D$, and suppose $\beta\ne\gamma$.
[Dub02, Theorem 1, p.197](../../../literature/pdf/Dub02.pdf) gives
$$
|\beta-\gamma|>c^{-D}\bigl(2\operatorname{house}(\gamma)\bigr)^{-nD}.
$$
The original statement and the proof on p.199 were read, with rendered pp.197 and 199 checked against the acquired PDF.
**When the two minimal polynomials differ**, their nonzero integer resultant gives $1\le|\beta-\gamma|c^D(\beta+\operatorname{house}(\gamma))^{nD-1}$; the final contradiction uses $\operatorname{house}(\gamma)\ge\gamma\ge1$.
This identifies the precise lost hypothesis.
Smy08 instead says an algebraic $\gamma$ not equal to any Mahler measure, without the real/$\ge1$ condition.
Its literal version fails for $\gamma=1/2$, $\alpha=1$: $n=D=1$, $c=2$, and both sides equal $1/2$, contradicting strict $>$.
The unrestricted formula is also undefined at $\gamma=0$.
These examples do not contradict the original theorem.
The degree $D$ is the degree of the **measure**, not automatically that of $\alpha$; the bound gives no uniform positive Lehmer gap as $D$ grows.

The selected original proof has a further repairable omission: it treats $\beta\ne\gamma$ as sufficient for a nonzero resultant, although distinct conjugates have the same minimal polynomial.
In that remaining case $n=D\ge2$, $c=1$ and $\operatorname{house}(\gamma)=\beta$.
The nonzero integer discriminant instead gives
$$
1\le |\operatorname{disc}(P_\beta)|
 \le |\beta-\gamma|^2(2\beta)^{D(D-1)-2},
$$
so $|\beta-\gamma|\ge(2\beta)^{1-D(D-1)/2}>(2\beta)^{-D^2}$, which is stronger than required.
This completes the inspected proof interface without declaring the original all-$\gamma\ge1$ theorem false.
It is an elementary repair of the cited argument, not an audit of the rest of Dubickas's paper.

<a id="smy08-bounded-measure-count"></a>
## Section 11: counting requires a fixed normalization

The survey literally defines $\#(d,T)$ as the number of all integer polynomials of exact degree $d$ and measure at most $T$.
Take $d\ge1$ and $T\ge1$; for $0<T<1$ this set is empty, so the positive lower bound below would fail.
The zero polynomial is never counted.

The survey reports the asymptotic (38)
$$
c(\log d)^{-1/2}d^{-1}
 \exp\!\left(\frac{\sqrt{105\zeta(3)d}}\pi\right)(1+o(1)),
\qquad
c=\frac{\sqrt{105\zeta(3)e^{-\gamma_E}}}{4\pi^2},
$$
for $\#(d,1)$, attributed to Boyd--Montgomery [41]; the bounds
$$
\tfrac12T^{d+1}(d+1)^{-(d+1)/2}<\#(d,T)
 <T^{d+1}e^{d^2/2},
$$
with sufficiently large degree for the stated upper bound; a further bound $T^{d(1+16\log\log d/\log d)}$ for $T\ge\theta_0$; and, for fixed $d$ as $T\to\infty$, Chern--Vaaler's $V_{d+1}T^{d+1}+O_d(T^d)$, with $V_{d+1}$ the relevant coefficient-space star-body volume.
Sinclair's reciprocal-polynomial results are mentioned without an explicit formula.
Their original proofs and constants were not audited.

**F3: the counting convention and the sharper upper bound are not safe for direct reuse.**
The original DK98, p.325, explicitly defines $N(d,T)$ with **positive leading coefficient and nonzero constant coefficient**.
This primary opening passage was available through indexed PDF text, while direct PDF access failed with HTTP 403.
The survey's definition omits both conditions.
If $C_d$ counts monic products of cyclotomic polynomials of degree $d$, with $C_0=1$, the literally defined all-polynomial count at $T=1$ is exactly
$$
\#(d,1)=2\sum_{j=0}^d C_j,
$$
because every such polynomial is uniquely $\pm z^{d-j}$ times one such product.
The [MPV98 statement immediately after (3.12)](../MPV98/Yin_U002.md#unrestricted-cyclotomic-products) reports the leading term in (38) for $C_d$, including the same factor $e^{-\gamma_E/2}$ outside the radical.
A visual check of the [Smy08 preprint](../../../literature/pdf/Smy08.pdf), printed p. 338, confirms that $e^{-\gamma_E}$ lies inside the radical.
Since $\#(d,1)\ge 2C_d$, the reported asymptotic for $C_d$ precludes (38) for the survey's literal all-polynomial count.
Direct inspection of the [Boyd–Montgomery chapter](https://doi.org/10.1515/9783110848632-004) remains outstanding.

Moreover the directly located primary passage [72], p.328, equation (5), has the general estimate
$$
|N(d,T)|<T^{d(1+16\log\log d/\log d)}e^{3.58\sqrt d},
$$
whereas Smy08 omits the last factor.
The full preceding theorem and its family/threshold qualifications were not accessible in this bounded check, so this records a **source-interface discrepancy requiring resolution**, not a proof that no stronger bound can hold.
In particular one may not drop that factor merely by quoting the located equation.
The exact relation between all-polynomial counts and the normalized counts is $\#(d,T)=2\sum_{j=0}^d|N(j,T)|$, extending $N(0,T)$ to positive integer constants at most $T$.
Any transfer must account for these terms and signs.
Fixed-degree finiteness or a fixed-degree large-$T$ asymptotic does not supply a gap uniform over unbounded degree.

## Dependencies, search limits and downstream effects

The primary checks were bounded responses to concrete mismatches: Matveev [106]'s definition and Theorem 1; Rhin [127] Theorem 1 for (36); Dubickas [67] Theorems A and 1 and the latter's proof with the repairs above; Dubickas [69]'s indexed publisher abstract/Theorem 3 for the additive target; and Dubickas--Konyagin [72]'s indexed definition and equation (5).
Searches used exact cited titles and implicated formulas.
The original Boyd--Montgomery asymptotic and the full counting theorem remain unverified at original-statement scope.
Failed opens and image-only extraction do not imply that no accessible source exists.
Following the parent's explicit retention instruction, this reviewer downloaded the selected Rhin and Matveev originals and recorded URL/time/bytes/hash metadata for parent registration; a single counting-PDF acquisition attempt returned HTTP 403.
No claim of an exhaustive errata search or nonexistence of a corrigendum is made.

Canonical keys for these selected dependencies are **Mat96**, **Rhi04**, **Dub02** (Smy08 [67], published 2002), **Dub04** ([69], no locally obtained PDF), and **DK98** (Dubickas--Konyagin [72], no locally obtained PDF).
The exact online locators above identify the inspected statements.

The full Sections 8--11 contain mainly theorem reports and examples, not proofs of all their cited results.
The checks above are deliberately not represented as a complete proof audit of that bibliography.
No enumeration programs, interval root certificates, symbolic factorization experiments or formal proof-assistant checks were run.
Exact hand checks cover the $\Phi_3$ discriminant obstruction, the repeated-root separation failure, the $\gamma=1/2$ equality, and the integral-closure obstruction to $1/2$ in the additive group.

On 2026-10-06 the actual consumers [S G0001](../../../strategies/Yin_S_G0001.md) and [S G0004](../../../strategies/Yin_S_G0004.md) were searched: they use other Smy08 passages for the nonreciprocal core, height/Dobrowolski normalization and toral entropy, and do not rely on the faulty statements (35), (37), the additive-group claim or these counting formulas.
Thus no existing strategy conclusion is invalidated by these findings.
For future arithmetic-route use, keep the $d\log d$ discriminant loss, integrality of the additive target, $\gamma\ge1$, the degree of the measure, and all counting conventions explicit.
Nothing here proves a new uniform gap or changes the Task's algebraic-entropy priority.

## Verification and revisions

- 2026-10-06: first fixed source unit; checked retained PDF hash, read all assigned passages, inspected complete rendered Smy08 PDF pp.14--17, Dub02 pp.197/199, Rhi04 p.156 and Mat96 pp.415--416, and checked the elementary proof repairs and counterexamples above.
  Mat96 text extraction was corrupt, so the original statement was read from rendered pages.
  External inspection depth is stated passage by passage.
  The coordinating agent read the integrated record and checked its elementary repairs; no independent second whole-source review is asserted.
- Definition anchors available for indexing: `smy08-salem-number`, `smy08-discriminant-separation`, `smy08-perron-mahler-value`, `smy08-bounded-measure-count`.
  Their scope is the definitions and conventions actually given here, not every externally reported theorem.

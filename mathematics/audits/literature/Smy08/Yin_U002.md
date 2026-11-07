---
author: Yin
---

<a id="smy08-u002"></a>
# Smy08-U002: Restricted Mahler gaps, auxiliary functions, and the house

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Smy08, [retained PDF](../../../literature/pdf/Smy08.pdf): Chris Smyth, *The Mahler measure of algebraic numbers: a survey*, arXiv:math/0701397v2, 28 January 2008. Chapter publication: *Number Theory and Polynomials* (2008), 322--349. This record concerns that preprint, not an independently compared publisher artifact.

Passages: Sections 5.1--5.4, 6.1--6.5, 7.1--7.4, printed pp.327--335 / PDF pp.6--14; equations (14)--(32), proof sketches, examples, and their reference locators.

Inspection: 2026-10-06; human author Yin, prepared by an assigned AI source-review agent. Every paragraph in Sections 5--7 was read; rendered PDF pp.6--14 were inspected. This record was self-checked. Selected elementary implications and counterexamples were checked as stated below. Most results are survey reports whose original proofs were not inspected.


Targeted primary checks: [Mig78](../../../literature/pdf/Mig78.pdf), Proposition 4 and Corollary 2, printed 39-03 / PDF p.4: assumptions and corollary read and visually checked.
[Zag93](../../../literature/pdf/Zag93.pdf), printed p.486 / PDF p.3: absolute-height definition and Theorem 1 read and visually checked; surrounding proof was read in extracted text, but not independently audited in full.

## Assessment and coverage

**Read** for the entire assigned survey passage.
**Audited within scope** for the elementary convention checks, repaired norm-averaging implication, resultant/nonreciprocity interface, house transfer identities, and explicit counterexamples below.
**Questioned at literal scope** for the Mignotte quotation, equation (23), the degree exponent in Section 6.5, and the definition in Section 7.4.
These are findings about the retained survey text, not refutations of the original theorems it cites.

| Passage | Actual inspection and retained boundary |
| --- | --- |
| 5.1, pp.327--329 | Reciprocal convention, Breusch/Smyth bounds and complete supplied proof sketches read. Integer-resultant and unit-normalization steps checked; Schur coefficient criteria, the sharp bound, equality classification and isolation proofs not reconstructed. |
| 5.2--5.3, p.329 | Kroneckerian-field extensions and Galois-field statement read. The external generalizations and Amoroso--David proof not audited. |
| 5.4, pp.329--330 | Mignotte, length/sparsity/parity, symmetric-matrix and graph statements read; Mignotte's primary hypotheses checked, with an exact counterexample to the survey's broader wording. Numerical searches and matrix/graph classification proofs not rerun. |
| 6.1, pp.330--331 | Schinzel's hypotheses, normalized spectrum and auxiliary-function sketch read; norm averaging checked and the printed sign disproved. Spectrum constants and fractal-measure assertions not independently computed. |
| 6.2--6.4, pp.331--332 | Restricted-conjugate, abelian and totally p-adic statements and supplied mechanism read. Exceptional-value and dependence-of-constant interfaces recorded; cited original capacity, sector, abelian-height and p-adic proofs not audited. |
| 6.5, pp.332--333 | All composition/height statements read. Zagier's primary height normalization and exact theorem checked; survey exponent tested by an irreducible quartic. General Zhang, Beukers--Zagier, Doche and Samuels proofs remain external. |
| 7.1--7.4, pp.333--335 | All bounds (25)--(32), power-sum sketch and field-constant discussion read. Basic Mahler-to-house transfer, real quadratic lift and Kroneckerian norm argument checked. Cited sharp constants, degree cutoffs and optimization proofs remain external; no assertion that the historical “strongest” bounds are current. |

No whole-original-paper proof audit, certified numerical optimization, search-table reproduction, or proof-assistant verification is asserted.
The review does not certify every historical attribution or decimal value.

<a id="smy08-reciprocal-number"></a>
## 1. Conventions and the nonreciprocal reduction

For a polynomial of degree \(d\), write \(P^*(t)=t^dP(t^{-1})\).
It is **reciprocal** in the survey's convention when \(P^*=\pm P\).
For a **nonzero** algebraic number \(\alpha\), reciprocity means that \(\alpha^{-1}\) is a conjugate of \(\alpha\).
For its primitive irreducible polynomial these conditions agree.
In the minus case \(P(1)=0\); a nonconstant irreducible polynomial then reduces to the corresponding linear exception.
Zero must be excluded whenever an inverse is used.

All logs here are natural.
For primitive irreducible \(P(t)=a_d\prod_{i=1}^d(t-\alpha_i)\),

\[
M(\alpha)=M(P)=|a_d|\prod_i\max(1,|\alpha_i|),\qquad
m(\alpha)=\log M(\alpha),\qquad
h(\alpha)=m(\alpha)/d.
\]

The *absolute multiplicative* quantity in Section 6 is \(M(\alpha)^{1/d}=e^{h(\alpha)}\).
It must not be identified with \(M(\alpha)\), or with algebraic entropy \(m(\alpha)\).

Section 5.1, equation (15), reports Smyth's theorem: every nonzero nonreciprocal algebraic integer satisfies

\[
M(\alpha)\ge\theta_0,
\qquad \theta_0>1,\quad \theta_0^3-\theta_0-1=0.
\]

This is a direct statement by the author of the cited theorem; it was already used as a statement-level input in the G0001 strategy.
This unit does not upgrade the 1971 proof to a complete independent proof audit.
The later [Smy71 primary-source inspection](../Smy71/Yin_U001.md#smy71-u001) checks the complete original proof and corollaries; this survey unit retains its original edition and inspection scope.
The equality classification by conjugates of \((\pm\theta_0)^{\pm1/k}\), the isolated gap, and the listed subsequent small values remain reported results with the source's stated references and scope.

Two elementary proof interfaces were checked:

1. If irreducible monic \(P\) is nonreciprocal and \(P(0)\ne0\), then \(P\) and \(P^*\) are relatively prime.
   Their resultant is a nonzero integer, hence has absolute value at least one.
   A common root would give an inverse-conjugate relation and force reciprocity.
   This validates the arithmetic starting point of the Breusch sketch; it does not supply the analytic estimates yielding (14) or (15).
2. The rational function \(F(z)=P(0)P(z)/P^*(z)\) has integer Taylor coefficients at zero for monic integral \(P\), since \(P^*(0)=1\).
   However \(F(0)=P(0)^2\).
   The next assertion \(F=f/g\) with \(f(0)=g(0)=M(P)^{-1}\) therefore requires \(P(0)=\pm1\).
   This is a recoverable missing reduction: nonunits have \(M(P)\ge |P(0)|\ge2>\theta_0\), so only units need that analytic argument.
   For example \(P=z-2\) has \(F(0)=4\), and cannot satisfy the displayed equal-at-zero factorization as written.
   No defect in the nonreciprocal theorem follows.
   The primary 1971 paper explicitly makes this unit reduction on printed p.171, as checked in [Smy71-U001](../Smy71/Yin_U001.md#smy71-inner-products); the omission discussed here concerns the later survey sketch.

<a id="smy08-kroneckerian-field"></a>
A **Kroneckerian number field** here means a totally real number field or a totally imaginary quadratic extension of a totally real field (a CM field).
Section 5.2's polynomial extensions over such fields need the original relative/field normalization before reuse; the survey's constants alone do not define a theorem for arbitrary coefficients in such a field.
Section 5.3 separately reports a universal \(c>1\) for nonzero non-torsion \(\alpha\) with \(\mathbb Q(\alpha)/\mathbb Q\) Galois.
This is a restricted family, not a reduction of every algebraic number to the Galois case at unchanged Mahler measure.

## 2. The Mignotte quotation and an exact counterexample

**F1 — Substantive missing hypothesis; Section 5.4, p.329 / PDF p.8.**
The survey attributes \(M(\alpha)\ge1.2\) to the existence of an unramified prime \(p<d\log d\).
Mig78, Corollary 2, actually requires an **odd**, **unramified**, **completely split** prime, and imports Proposition 4's assumption that \(\alpha\) is an algebraic unit which is not a root of unity.
Its sufficient numerical condition is \(p\le d\log d\).
The complete-splitting condition is substantive even after all usual nonzero/non-torsion restrictions are restored.

Here is a counterexample to the broader survey wording, with finite exact checks rather than a floating-point estimate.
Let

\[
L(t)=t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1
=t^5Q(t+t^{-1}),
\]
\[
Q(x)=x^5+x^4-5x^3-5x^2+4x+3.
\]

The values of \(Q\) at \(-2,-3/2,-1,0,1\) are, respectively, \(-1,3/32,-1,3,-1\).
Thus four distinct roots lie in the four corresponding disjoint intervals, all in \((-2,2)\).
Its fifth root lies in \((2,61/30)\), since \(Q(2)=-1\) and

\[
Q(61/30)=6762031/24300000>0.
\]

These five roots exhaust its degree.
Modulo 2, \(Q=x^5+x^4+x^3+x^2+1\); its remainders on division by \(x,x+1,x^2+x+1,x^3+x+1,x^3+x^2+1\) are \(1,1,x,x^2+x+1,x^2\).
In particular it has no degree-one or degree-two irreducible factor and is irreducible of degree five.
The field generated by a root \(u\) is totally real.
At some real embedding, \(u^2-4<0\), so \(u^2-4\) is not a square in that field.
Hence \(t^2-ut+1\) is irreducible over it and \(L\) is irreducible of degree ten.

Eight roots of \(L\) lie on the unit circle.
The remaining two are positive reciprocals \(\tau,\tau^{-1}\), where \(1<\tau<6/5\), because \((6/5)+(5/6)=61/30\) and \(t+t^{-1}\) increases for \(t>1\).
Consequently

\[
1<M(\tau)=M(L)=\tau<6/5.
\]

Modulo 3, the Euclidean algorithm for \(L,L'\) has successive nonzero remainders

\[
t^5+2t^4,\quad t^4+2t^3+1,\quad 2t,\quad1.
\]

Thus 3 does not divide the polynomial discriminant and is unramified in \(\mathbb Q(\tau)\).
Also \(3<10\log10\).
This is an algebraic unit of degree ten violating the survey's claimed \(1.2\) lower bound.
Complete splitting fails: a squarefree degree-ten polynomial over \(\mathbb F_3\) cannot have ten linear factors.
This check uses the usual field-discriminant/index identity and the factorization criterion at a prime not dividing the polynomial discriminant; those elementary algebraic-number-theory inputs were not re-proved here.

**Reuse:** adopt Mig78's checked hypotheses when invoking its Corollary 2.
Its original proof was not fully audited.
This finding does not challenge the more general nonreciprocal bound, or Lehmer's conjecture itself.

The remaining Section 5.4 results are *restricted-family* reports: bounded coefficient length, bounded number of nonzero terms, odd coefficients, and reciprocal polynomials obtained from integer symmetric matrices.
Their constants are not uniform after their controlling parameter is allowed to grow.
For sparsity statements, exclude zero/monomial and measure-one cases explicitly; “noncyclotomic” must not be read as merely “not equal to a single cyclotomic polynomial” while permitting products of cyclotomic factors.
None of the original sparse-polynomial, parity, or matrix/graph proofs was audited here.

<a id="smy08-restricted-height-gap"></a>
## 3. Strong restricted height gaps and the auxiliary-function mechanism

The main distinction in Section 6 is a lower bound \(M(\alpha)\ge C^d\), equivalently \(h(\alpha)\ge\log C>0\), on a specified family.
This is much stronger on that family than the classical Lehmer target \(m(\alpha)\ge c>0\), but it cannot be extended to all algebraic numbers: \(h(2^{1/n})=(\log2)/n\to0\).

Equation (22) reports \(M(\alpha)\ge\phi^{d/2}\) for a totally real algebraic integer \(\alpha\notin\{0,1,-1\}\), where \(\phi=(1+\sqrt5)/2\).
The stated Kroneckerian extension has the additional condition \(|\alpha|\ne1\).
Equation (24)'s positive-real-part family excludes the roots of \(z-1\) and \(z^2-z+1\).
Section 6.3 states \(M(\alpha)\ge5^{d/12}\) for a nonzero non-torsion number generating an abelian extension of \(\mathbb Q\).
Section 6.4's totally p-adic discussion must likewise be read on nonzero non-torsion numbers, with \(p\) fixed; its \(c_p>1\) is allowed to depend on \(p\).
These are source reports, not original-proof audits.

**F2 — Incorrect sign in a proof mechanism; equation (23), p.331 / PDF p.10.**
The printed inequality is

\[
\log^+|x|\ge c-\sum_i c_i\log|P_i(x)|,\qquad c_i\ge0.
\]

It does not imply the next claimed bound by averaging over conjugates.
Take \(P_1(x)=x^2+2\), \(c_1=1\), \(c=\log2\).
The printed inequality holds for every real \(x\), since its right side is \(\log(2/(x^2+2))\le0\).
Nevertheless the totally real algebraic integer \(\phi\), which is not a root of \(P_1\), has \(M(\phi)=\phi<2=e^c\).
This disproves the literal implication.

The valid reusable sufficient inequality has a **plus** sign on its right:

\[
\log^+|x|\ge c+\sum_i c_i\log|P_i(x)|
\quad(x\in\mathbb R),
\qquad P_i\in\mathbb Z[x],\ c_i\ge0.
\]

If \(\alpha\) is totally real and integral, and every \(P_i(\alpha)\ne0\), the sum over its \(d\) conjugates gives

\[
\log M(\alpha)\ge dc+
\sum_i c_i\log|N_{\mathbb Q(\alpha)/\mathbb Q}(P_i(\alpha))|
\ge dc.
\]

The last inequality uses a nonzero integer norm.
Hence the normalized conclusion is \(M(\alpha)^{1/d}\ge e^c\).
Exceptional roots of the auxiliary polynomials must be handled separately.
This elementary repaired implication was checked in full; the construction and optimization of useful \(P_i,c_i\) and the original spectrum proof were not audited.
When a \(P_i\) vanishes at a real point, its logarithm is interpreted with the limiting value \(-\infty\); this is compatible with the corrected sufficient inequality.

The same paragraph's finite spectrum limit uses an undefined \(\alpha_n\), while defining \(\beta_0=1\), \(\beta_n-\beta_n^{-1}=\beta_{n-1}\), of degree \(2^n\).
It must be normalized before reuse: unnormalized \(M(\beta_n)\) cannot converge to \(1.31427\ldots\), since (22) gives \(M(\beta_n)\ge\phi^{2^{n-1}}\).
The surrounding spectrum is that of \(M(\alpha)^{1/d}\).
This audit does not independently certify the reported limit or fractal dimension.

**Contextual scope completions in Section 6.2.**
The stated Langevin conclusion cannot literally include \(M(P)=1\): take \(V=\mathbb C\setminus\mathbb R\) and \(P=x-1\).
Its roots avoid \(V\), but \(M(P)=1\).
Likewise \(P=x\) must be excluded.
The intended reusable nontrivial scope is \(M(P)>1\), with exceptional measure-one polynomials removed.
At the optimal totally real constant \(C=\sqrt\phi\), use \(\ge\), since \(P=x^2-x-1\) attains equality; a strict inequality is available with a smaller constant.
These omissions are readily recoverable from the surrounding Lehmer discussion and do not refute the cited original theorem.
The original Langevin proof and its exact exception formulation were not inspected.
The reported capacity argument and annulus/sector refinements therefore remain external interfaces, not a complete proof supplied by this unit.

## 4. Zagier's height bound and the degree conversion

**F3 — Factor-of-two degree error under the survey's ordinary degree convention; Section 6.5, p.332 / PDF p.11.**
The survey says that irreducible nonconstant \(P\in\mathbb Z[x(x-1)]\), apart from \(\pm(x(x-1)+1)\), has \(M(P)\ge\phi^{d/2}\).
With \(d=\deg_xP\), this is false.

Take

\[
P(x)=(x^2-x)^2+1=x^4-2x^3+x^2+1.
\]

If \(P(\alpha)=0\), then \(\alpha^2-\alpha=\pm i\), so \(\mathbb Q(i)\subset\mathbb Q(\alpha)\).
The discriminant \(1+4i\) is not a square in \(\mathbb Q(i)\): if \((a+bi)^2=1+4i\) with \(a,b\in\mathbb Q\), then \((a^2+b^2)^2=17\), impossible.
The conjugate sign gives the same conclusion, so \(P\) is irreducible over \(\mathbb Q\) of degree four.
Solving its two quadratics gives

\[
M(P)=\frac{1+\sqrt{17}+\sqrt{2+2\sqrt{17}}}{4}
<\frac{17}{8}<\phi^2.
\]

For the first strict bound use \(\sqrt{17}<17/4\) and \(\sqrt{2+2\sqrt{17}}<13/4\).
Thus the test is exact, not a decimal comparison.

Zag93, Theorem 1, explicitly uses the absolute logarithmic height \(H(\alpha)=\log M(\alpha)/[\mathbb Q(\alpha):\mathbb Q]\), and states

\[
H(\alpha)+H(1-\alpha)\ge\tfrac12\log\phi
\]

outside \(0,1,(1\pm\sqrt{-3})/2\).
For an irreducible invariant \(P(x)=R(x(x-1))\), \(\alpha\) and \(1-\alpha\) are conjugate and have equal height.
The direct conclusion is therefore

\[
M(P)\ge\phi^{d/4},\qquad d=\deg_xP.
\]

If degree were instead defined as \(\deg R=d/2\), the exponent “degree/2” would have a different meaning; the survey does not introduce that changed convention.
Nor should its adjacent spectrum statement be copied without stating which normalized height or measure is being used.
The targeted primary statement is accepted for this normalization check; no full independent audit of Zagier's proof, its equality classification, or the general Zhang theorem is claimed.

<a id="smy08-house"></a>
## 5. The house and its limits as a Lehmer tool

For an algebraic number with conjugates \(\alpha_1,\ldots,\alpha_d\), its **house** is \(\operatorname{house}(\alpha)=\max_i|\alpha_i|\).
On nonzero algebraic integers which are not roots of unity, it exceeds one and

\[
M(\alpha)\le\operatorname{house}(\alpha)^d,
\qquad
\operatorname{house}(\alpha)\ge\exp(m(\alpha)/d)
\ge1+m(\alpha)/d.
\]

This checks the Mahler-to-house direction used in Section 7.2: the nonreciprocal bound implies \(\operatorname{house}(\alpha)\ge1+(\log\theta_0)/d\).
The reverse direction does not follow: one conjugate of size \(1+c/d\) alone yields only a degree-dependent lower bound for \(m\).
A Schinzel--Zassenhaus house theorem must not be substituted for a classical Lehmer gap.

Equations (25)--(28) are historical degree-dependent general lower bounds.
Read them in the Section 3/7 domain of **nonzero algebraic integers, not roots of unity**, with the printed degree thresholds.
In particular, the Cassels sentence on p.334 cannot be extended literally to arbitrary algebraic numbers: \(\alpha=1/2\) has house \(1/2\) and no unit-circle conjugate.
The omission is a contextual integrality restriction, not evidence against Cassels' theorem.
The same caution applies to inverse/log expressions at zero.

The power-sum mechanism in Section 7.1 requires integral conjugates: \(s_k=\sum_i\alpha_i^k\in\mathbb Z\), and the characteristic-\(p\) identity for symmetric polynomials gives \(s_{kp}\equiv s_k\pmod p\).
The subsequent quantitative argument is not included in this survey.
In (29), the second variable is complex-conjugated: its factors are \(|z_k\overline{z_j}-1|\).
The derived nonreciprocal estimate involving \(\prod_i\log|\alpha_i|\) is a cited external result, not proved here.
Nonzero nonreciprocal irreducible numbers have no unit-circle conjugate; such a conjugate would identify an inverse with a complex conjugate and force reciprocity.

For the totally real lift in Section 7.3, let \(\alpha\) be integral and totally real and solve \(\gamma+\gamma^{-1}=\alpha\).
Then \(\gamma\) is integral, \(\deg\gamma\le2d\), and its conjugates are real or on the unit circle.
For \(A=\operatorname{house}(\alpha)>2\),

\[
G=\max(\operatorname{house}(\gamma),\operatorname{house}(\gamma^{-1}))>1,\qquad
A=G+G^{-1}=2+\frac{(G-1)^2}{G}.
\]

The maximum includes both quadratic roots even if the quadratic splits over \(\mathbb Q(\alpha)\); one may choose the root of larger house without changing the degree bound.
This proves the threshold transfer \(A\le2+\delta^2/(1+\delta)\Rightarrow G\le1+\delta\).
If \(A\le2\), all conjugates of \(\gamma\) have modulus one, so the usual Kronecker theorem gives \(\alpha=\omega+\omega^{-1}\) for a root of unity \(\omega\).
The explicit constants in (30)--(32), including the sharper coefficient in (31), remain source-reported external estimates; the elementary lift alone, with degree bounded by \(2d\), is not recorded as a verification of every displayed sharp constant.

<a id="smy08-kronecker-constant"></a>
## 6. Correct domain and extremum for the Kronecker constant

**F4 — Invalid literal definition; Section 7.4, p.335 / PDF p.14.**
The source calls this the *least* \(\varepsilon>0\) for which every algebraic integer in \(K\) has house at least \(1+\varepsilon\).
Including \(0\) and roots of unity makes any such positive \(\varepsilon\) impossible.
Even after removing them, if one positive \(\varepsilon\) works then every smaller positive value works, so there is no least positive admissible value.

The reusable convention is the **largest uniform gap**, equivalently

\[
\kappa(K)=\inf_{\alpha\in\mathcal O_K\setminus(\{0\}\cup\mu(K))}
\bigl(\operatorname{house}(\alpha)-1\bigr).
\]

For fixed \(K\), this is positive and attained: bounded house and degree at most \([K:\mathbb Q]\) bound all coefficients of the integral minimal polynomial, leaving finitely many possibilities.
Kronecker excludes nonzero non-torsion elements of house at most one.
Integer 2 supplies a nonempty comparison set.
Thus the infimum can equally be called a minimum; it is the maximum of the admissible uniform constants, not their minimum.

The final Kroneckerian-field argument was checked.
Complex conjugation commutes with embeddings in this setting.
If a nonzero integral \(\alpha\) had every conjugate of modulus \(<\sqrt2\), then the algebraic integer \(\alpha\overline\alpha-1\) would have every conjugate strictly between \(-1\) and 1.
Its integer norm has modulus below one, so it vanishes.
Consequently every conjugate of \(\alpha\) has modulus one, and Kronecker makes \(\alpha\) a root of unity.
Therefore \(\kappa(K)\ge\sqrt2-1\) for a Kroneckerian number field.
This confirms that particular supplied argument, with the stated exclusions, without auditing the full Callahan--Newman--Sheingorn article.

## 7. Search boundary, verification facts, and downstream use

The consequential primary follow-ups on 2026-10-06 were bounded to two concrete discrepancies.
For Section 5.4, Smy08 reference [109] led to the Numdam Mig78 scan; the visually checked Corollary 2 resolves the missing splitting hypothesis.
For Section 6.5, the exact title/reference [171] led to Zagier's MPI-hosted journal scan; visually checking its definition and Theorem 1 resolves the height factor.
No conclusion about the absence of formal errata is drawn.
The remaining original works cited in Sections 5--7 were not recursively acquired or audited.
Discovery searches concerning Langevin's exceptions and the Kronecker-constant terminology did not become additional proof premises; the literal scope problems above already have elementary checks.

The retained exact polynomial arithmetic consists of the displayed rational signs, the modulo-2 remainder checks, and the modulo-3 Euclidean sequence.
These were recomputed with exact integer arithmetic in the tool runtime; the formulas are sufficient to reproduce them independently.
No numerical root finder or Sturm certificate is being presented as the basis of F1 or F3.
The quartic radical comparison and norm-averaging counterexample were checked symbolically.

For [S G0001](../../../strategies/Yin_S_G0001.md), the nonreciprocal theorem still supplies a legitimate restricted-family reduction; the outstanding reciprocal family is not thereby reduced to Salem numbers alone.
Under the rational algebraic Yuzvinski interface, \(\log M(P)\), rather than \(h(\alpha)\), is the corresponding entropy.
None of the restricted-field bounds or house results controls all degrees and all reciprocal algebraic units.

For [S G0004](../../../strategies/Yin_S_G0004.md), F2 is directly relevant: an auxiliary-polynomial certificate must have the correct sign, integer nonzero resultants/norms, a fixed normalization, and explicit exceptional factors.
F1 rules out using mere unramifiedness to obtain a universal \(1.2\) gap.
F3 rules out importing the larger exponent from the survey.
F4 changes only the local field-constant definition.
The present source corrections do not prove or refute the project's classical Lehmer target, and they add no new Task or project Claim.

Initial record: 2026-10-06, for the retained Smy08 v2.
Future source editions or adaptations require checking the affected statements before carrying these assessments forward.

---
author: Yin
---

<a id="dgb16-u003"></a>
# DGB16-U003: Uniqueness Axioms and the Length-Function Proof

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Dikran Dikranjan and Anna Giordano Bruno, *Entropy on abelian groups*, Advances in Mathematics 298 (2016), 612–653, DOI 10.1016/j.aim.2016.04.020; the 42-page published [local artifact](../../../literature/pdf/DGB16.pdf), formerly supplied as DB16.pdf.

Passages: Theorem 1.3 and normalization on printed pp. 615–616 (PDF pp. 4–5); complete Section 6, printed pp. 643–646 (PDF pp. 32–35).

Inspection: 2026-10-06, agent working for the bound author Yin; direct text reading and full inspection of both internal uniqueness arguments, with rendered PDF pp. 34–35 checked. The original proofs and exact primary interfaces of source references [16], [38], and [44] were not verified here. This record is self-reviewed; no independent-review or formal-verification claim is made.


Reading coverage: **Read, with complete internal proof inspection and retained external verification limits**.
The proof reductions have been checked, but the unverified primary interfaces listed below prevent treating this record as an independently established proof of every dependency.
The terminology and omitted justification identified below do not refute the uniqueness conclusion.

## Statement and conventions

All groups are discrete abelian groups, written additively; an endomorphism need not be injective or surjective.
For a nonempty finite subset $F\subseteq G$,

\[
T_n(\phi,F)=F+\phi(F)+\cdots+\phi^{n-1}(F),\qquad
H(\phi,F)=\lim_{n\to\infty}\frac{\log|T_n(\phi,F)|}{n},
\]

and $h(\phi)=\sup_F H(\phi,F)\in[0,\infty]$, with natural logarithms.
The [foundational unit](Yin_U001.md#dgb16-u001) owns the definitions and basic entropy properties.
The direct sum $K^{(\mathbb N)}$ consists of finite-support sequences, and $\beta_K(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots)$.

For an endomorphism $\phi$ of $\mathbb Q^n$, let $\chi_\phi\in\mathbb Q[t]$ be its monic characteristic polynomial and let $s$ be the least positive integer with $s\chi_\phi\in\mathbb Z[t]$.
The polynomial $s\chi_\phi$ is primitive.
The normalization is

\[
m(\phi)=m(s\chi_\phi)
=\log s+\sum_{|\alpha_i|>1}\log|\alpha_i|,
\]

where roots have their algebraic multiplicities.
It is not the Mahler measure of the unscaled rational characteristic polynomial under the usual polynomial convention.

**Theorem 1.3.**
The family $\{h_G:\operatorname{End}(G)\to[0,\infty]\}_G$ is the unique such family having all five properties:

1. Conjugation invariance under every group isomorphism intertwining the endomorphisms.
2. If $G$ is a directed union of $\phi$-invariant subgroups $G_i$, then $h_G(\phi)=\sup_i h_{G_i}(\phi|_{G_i})$.
   This is continuity for direct limits of invariant subgroups, not an unqualified assertion about arbitrary diagrams with noninjective transition maps.
3. For every invariant subgroup $H\leq G$, $h_G(\phi)=h_H(\phi|_H)+h_{G/H}(\bar\phi)$, in the extended nonnegative reals.
4. $h_{K^{(\mathbb N)}}(\beta_K)=\log|K|$ for every finite abelian group $K$, including the trivial group.
5. $h_{\mathbb Q^n}(\phi)=m(\phi)$ for every integer $n\geq1$ and every $\phi\in\operatorname{End}(\mathbb Q^n)$.

These are jointly sufficient axioms.
The theorem neither proves their logical independence nor permits omission of one of the two normalization families.
The logarithmic law is a consequence of uniqueness and the actual entropy's properties, rather than an additional stated axiom.

## Direct proof: checked reductions

Let $h^*$ satisfy the five axioms.
Addition and nonnegativity imply monotonicity on invariant subgroups and quotients.
To show $h^*(\beta_{\mathbb Z})=\infty$, reduce $\mathbb Z^{(\mathbb N)}$ modulo $p$ for each prime $p$.
The quotient flow is $\beta_{\mathbb Z/p\mathbb Z}$, so monotonicity gives $h^*(\beta_{\mathbb Z})\geq\log p$ for arbitrarily large primes.
This uses no subtraction of infinite values.

The source's five reductions were checked in order:

1. **Torsion groups.**
   The argument invokes the torsion uniqueness theorem [16, Theorem 6.1].
   The source expressly notes on p. 644 that this older theorem includes a logarithmic-law axiom and invokes [38] to obtain it from the current torsion axioms.
   Both interfaces must be retained; citing only [16] would leave an axiom mismatch.
2. **Removal of torsion.**
   Apply addition to $t(G)\leq G$ for both functions.
   Since $G/t(G)$ is torsion-free, equality on the torsion and torsion-free cases gives equality on $G$.
   Addition is used without cancellation, so infinite entropy causes no issue.
3. **Finite torsion-free rank.**
   Embed $G$ essentially in its divisible hull $D(G)\cong\mathbb Q^n$.
   The quotient $D(G)/G$ is torsion.
   The entropy on $D(G)$ is finite by the rational normalization and the Algebraic Yuzvinski Formula.
   Both addition identities can therefore be subtracted in the ordinary real numbers after torsion equality on the quotient; there is no $\infty-\infty$.
   Rank zero is the trivial group, already fixed by axiom 4.
4. **One generator under the flow and infinite rank.**
   If $G=V(\phi,g)$ is torsion-free of infinite rank, the orbit $g,\phi g,\phi^2g,\ldots$ is $\mathbb Z$-linearly independent.
   A nonzero polynomial relation would bound the rank after tensoring with $\mathbb Q$.
   These orbit elements generate $G$, so the flow is the right shift on $\mathbb Z^{(\mathbb N)}$, with entropy $\infty$ for both functions.
5. **Finitely many flow generators, then arbitrary $G$.**
   For $G=\sum_{i=1}^kV(\phi,f_i)$, either all cyclic orbit groups have finite rank, and their sum has finite rank, or one has infinite rank and monotonicity gives entropy $\infty$.
   Every $G$ is the directed union of these finitely generated $\mathbb Z[t]$-submodules.
   Axiom 2 and actual entropy continuity complete the proof.

The argument uses finite generation as a $\mathbb Z[t]$-module, not finite generation as an abelian group.
The finite entropy needed for cancellation occurs only in step 3, where it has been established before subtraction.

<a id="dgb16-length-function"></a>
## Length functions and the second proof

For a commutative unital ring $R$, a **length function** in Definition 6.1 is an isomorphism-invariant function $L:\operatorname{Mod}_R\to[0,\infty]$ with $L(0)=0$, additive on every short exact sequence and upper continuous:

\[
L(M)=\sup\{L(F):F\leq M\text{ is a finitely generated }R\text{-submodule}\}.
\]

The module corresponding to $(G,\phi)$ has $t\cdot g=\phi(g)$.
Proposition 6.2 translates conjugacy, directed continuity, and addition into this definition for $R=\mathbb Z[t]$.
The zero-object condition additionally follows from the normalization at the trivial Bernoulli shift; it must not be inferred from $L(0)=L(0)+L(0)$ alone because $\infty$ also satisfies that equality.

The second proof invokes [44, Corollary of Lemma 2]: for a commutative Noetherian ring, length functions are determined by their values on $R/\mathfrak p$ for prime ideals $\mathfrak p$.
Its mechanism is a finite prime filtration of every finitely generated module, followed by upper continuity.
The cited original theorem and original proof remain outside the present inspection.

The prime cases in the source were checked with the terminology correction below:

| Prime case in $\mathbb Z[t]$ | Flow and value | Check |
| --- | --- | --- |
| $(0)$ | Multiplication by $t$ on $\mathbb Z[t]$, conjugate to $\beta_{\mathbb Z}$; value $\infty$. | The monomial basis supplies the conjugacy. |
| Height-one $(p)$, $p$ an integer prime | Multiplication by $t$ on $\mathbb F_p[t]$, conjugate to $\beta_{\mathbb F_p}$; value $\log p$. | Axiom 4 applies exactly. |
| Maximal $(p,f)$, with $f\bmod p$ irreducible of positive degree | Finite field $\mathbb F_p[t]/(\bar f)$; entropy zero. | Finiteness is sufficient for actual entropy zero; equality for $h^*$ uses the retained torsion uniqueness input. |
| Height-one $(f)$, $f$ primitive irreducible of positive degree | $M=\mathbb Z[t]/(f)$ embeds in $D=\mathbb Q[t]/(f)\cong\mathbb Q^{\deg f}$. | Gauss's lemma gives $(f)\mathbb Q[t]\cap\mathbb Z[t]=(f)$; $1,t,\ldots,t^{n-1}$ show $M$ spans $D$ rationally, so $D/M$ is torsion. Equality on $D$ and on $D/M$, followed by finite cancellation, yields equality on $M$. |

The last case only needs $h^*(\bar\mu_t)=h(\bar\mu_t)$, not that their common value is zero.
Thus even if the source's extra zero assertion is omitted, its equality proof goes through, since the entropy on $D$ is finite.

## Located corrections and their impact

All findings in this section are newly recorded in this audit and pre-existing in the published source.

- **P3 — p. 645, second proof, prime classification:** “minimal prime” must mean “height-one prime” or “minimal nonzero prime.”
  The ring $\mathbb Z[t]$ is a domain, so its only minimal prime in the standard sense is $(0)$; e.g. $(2)$ contains the strictly smaller prime $(0)$.
  The intended split into $(0)$, height-one principal primes, and maximal ideals is correct.
  Correct the terminology when reusing the argument.
- **P3 — p. 646, last prime case:** the sentence assigning entropy zero to the torsion quotient is not a consequence of torsion uniqueness alone; torsion flows may have positive entropy.
  The equality needed by the proof does follow from that input, so remove the unnecessary zero claim from this step.
  The zero claim is also true for this particular quotient after a further argument: $(D/M)[m]\cong M/mM$ is finite for finite-rank torsion-free $M$; each finite subset of $D/M$ therefore lies in a finite invariant subgroup.
  This uses the finite-rank quotient fact also invoked by the source at p. 637, rather than torsionness alone.
  Its external original proof is not audited here.
- The second proof briefly writes the codomain as $\mathbb R_{\geq0}$ on p. 645.
  It must retain $\infty$, as both the theorem and the very next prime case require it.
  This is a notation lapse, not an alternative finite-valued theorem.

No counterexample to Theorem 1.3 was obtained.
These repairs do not remove the primary-source verification limits below.

## Dependencies and retained limits

| Input | Role and present verification boundary |
| --- | --- |
| [DGB16-U001](Yin_U001.md#dgb16-u001), Sections 2–4 | Basic entropy, Bernoulli shifts, orbit groups, divisible hulls, and directed unions; use its exact findings and corrections. |
| [DGB16-U002](Yin_U002.md#dgb16-u002), Theorem 1.1 | Addition for actual $h$; its own source-input boundaries remain in force. |
| [GBV15-U001](../GBV15/Yin_U001.md#gbv15-u001), arXiv:1111.1287v3 | Exact rational-endomorphism formula and primitive integer normalization checked in a primary artifact. The original p-adic proof is not re-audited here. |
| DGB16 reference [16], Theorem 6.1 | Torsion uniqueness as reported by DGB16; exact original statement/proof were not inspected in this unit. The source's additional logarithmic-law requirement must be supplied through [38]. No independent acceptance is inferred from the citation. |
| DGB16 reference [38] | Claimed derivation of the logarithmic law from the other torsion axioms. Primary statement and proof remain unchecked; this is a source-verification obligation, not a demonstrated mathematical error. |
| DGB16 reference [44], Corollary of Lemma 2 | Noetherian length-function determination by prime quotients. The source's stated interface and its applicability to $\mathbb Z[t]$ were read; exact original primary text and proof were not checked. |

Bounded searches on 2026-10-06 used the titles/authors of [16], [38], and [44], together with “Theorem 6.1,” “logarithmic law,” and “Corollary of Lemma 2.”
They located bibliographic or secondary summaries rather than the exact missing primary passages.
This unit does not treat search snippets as theorem verification.
The coordinating source record owns acquisition attempts and any failed-download exception.

## Intended use and downstream scope

This is a literature-audit record, not a new project Claim or Task selection.
The exact five axioms and finite-cancellation mechanism may be consulted with the dependency boundaries above.
Before adopting the full uniqueness theorem as newly reviewed support, close or explicitly accept through an adequately checked primary source the torsion uniqueness/logarithmic-law interface; the alternative length-function route has its separate cited-input boundary.

The companion [Lehmer/realization unit](Yin_U004.md#dgb16-u004) does not require the length-function proof.
No downstream project theorem is reclassified by this unit.

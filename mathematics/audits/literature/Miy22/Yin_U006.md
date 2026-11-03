---
author: Yin
---

# Miy22: Affiliated Operators and Domain-Sensitive Rationality

Source: [Miy22](../../../literature/pdf/Miy22.pdf), published journal version, Section 4, printed/PDF pp. 19-24.
The printed page sequence agrees with the PDF page sequence here.

Audit date: 2026-09-08.
Reviewer: the Section 4 audit agent.
This is a reading and reconstruction audit of the source, using the extracted text and visual inspection of all six corresponding page renders.
It is separate from the source author's proof and includes the reviewer's own rechecks of the formulas below.
It is not external human review, formal verification, or verification of the cited outside papers.
Theorem 3.1 is an input to this unit, not independently proved by this Section 4 review.

## Shared Setting and Trust Boundary

Write \(\mathcal H=\mathcal F(H)\), where \(H\) has finite dimension \(d\), and let \(M=L^\infty(s)\) act in the full Fock representation of the free semicircular family.
The source's vacuum trace is faithful and tracial.
The bounded right creation operators satisfy
\[
r_i^*r_j=\delta_{ij}I,\qquad
\sum_{i=1}^d r_i r_i^*=I-P_\Omega.
\]
The operator \(r_i+r_i^*\) commutes with \(M\), as used in Remark 3.10, p. 18.

Let \(U(M)=\widetilde L^\infty(s)\) be the algebra of closed densely defined operators affiliated with \(M\).
Its algebraic sums and products mean the appropriate closures of the initially defined operator operations.
An equality in \(U(M)\) does not by itself license an unbounded composition on every vector of \(\mathcal H\).

Let \(C_{\mathrm{div}}(s)\) be the division closure of the polynomials inside the bounded algebra \(M\), and let \(D(s)\) be their division closure inside \(U(M)\).
The ambient algebra matters: a denominator in \(C_{\mathrm{div}}(s)\) may have an unbounded affiliated inverse and need not be invertible in \(M\).

The standard finite von Neumann algebra facts used below are spectral/polar decomposition, the algebra structure of affiliated operators, and bounded fraction representations.
Their application and consequences are reconstructed here; foundational proofs were not independently audited.
The cited results of Linnell (2000), reference [12] in Miy22, and Mai-Speicher-Yin, reference [13] in Miy22, were accessed only through Miy22.
No new bibliographic keys are assigned to them here.


This source analysis comprises [U006](#miy22-u006), [U007](Yin_U007.md#miy22-u007), [U008](Yin_U008.md#miy22-u008).
Its [shared source, inspection and setting](#miy22-affiliated-operators-and-domain-sensitive-rationality) and [joint review dated 2026-09-08](Yin_U008.md#independent-cross-review-of-u006-u008) retain their original scopes.

<a id="miy22-u006"></a>
## Miy22-U006 - Regular Fractions and Denominator-Independent Defects

- Kind: representation machinery and a finite-rank criterion independent of the chosen fractions.
- Source locators: Section 4 opening and Lemmas 4.1-4.3, p. 19; definitions of \(R(s),R'(s)\), p. 19; Lemma 4.6, p. 20.
- Verification: statements and hypotheses read; fraction identities, finite-rank cancellation, and denominator regularity reconstructed.
  The affiliation infrastructure and external source attribution remain within the shared trust boundary.

### Statements, Assumptions, and Notation

A regular bounded element here means a nonzero divisor of \(M\), not merely an element different from zero.
The source specifies the condition \(\theta x\ne0\) for every nonzero \(x\in M\).
In this finite tracial setting it implies that \(\theta\) is injective on \(\mathcal H\), has dense range, and is invertible in \(U(M)\).

Every \(u\in U(M)\) admits bounded representatives
\[
u=f^{-1}a=bg^{-1},\qquad a,b,f,g\in M,
\]
with \(f,g\) regular.
For example,
\[
f=(1+uu^*)^{-1},\quad a=(1+uu^*)^{-1}u,\qquad
g=(1+u^*u)^{-1},\quad b=u(1+u^*u)^{-1}.
\]
Functional calculus and polar decomposition give bounded numerators: the relevant scalar function is \(t/(1+t^2)\), bounded by \(1/2\).
The denominators have trivial kernel and dense range.
These are identities in the affiliated algebra; the domain interpretation needed later is given in U008.

For any such pair of left/right representations define the bounded defect
\[
\Delta_i(f,a,b,g)=f r_i^* b-a r_i^* g.
\]
Define \(R(s)\) by finite rank of every \(\Delta_i\) for every valid representation, and \(R'(s)\) by existence of one valid representation with every \(\Delta_i\) finite rank.
Lemma 4.6 states \(R(s)=R'(s)\).

The phrase \(f[r_i^*,u]g\) is only a formal mnemonic until the compositions' domains have been justified.
The definition uses the everywhere-defined bounded defect \(\Delta_i\).

### Lemma-by-Lemma Reconstruction

**Lemma 4.1: common denominators.**
Start with bounded fractions \(u_k=f_k^{-1}a_k=b_k g_k^{-1}\), with regular \(f_k,g_k\).
Represent
\[
f_1f_2^{-1}=x^{-1}y,\qquad x,y\in M,\quad x\text{ regular}.
\]
The affiliated ratio on the left is invertible, so \(y\) is invertible in \(U(M)\) and consequently regular as a bounded element.
Thus
\[
f=xf_1=yf_2
\]
is regular, and \(u_1=f^{-1}xa_1,\ u_2=f^{-1}ya_2\).
For the right side choose
\[
g_1^{-1}g_2=pq^{-1},\qquad g=g_1p=g_2q.
\]
Both \(p,q\) are regular by the same argument, and
\[
u_1=b_1p g^{-1},\qquad u_2=b_2q g^{-1}.
\]
The common denominators therefore have the required invertibility; that property must not be omitted when reusing the lemma.

**Lemma 4.2: finite-rank cancellation.**
For bounded maps \(\theta:\mathcal H_1\to\mathcal H_2\) and \(\phi:\mathcal H_2\to\mathcal H_1\), injectivity of \(\phi\) and finite rank of \(\phi\theta\) imply finite rank of \(\theta\), by injectivity on its range.
If instead \(\theta\) has dense range, continuity of \(\phi\) puts \(\phi(\mathcal H_2)\) in the closure of \(\phi\theta(\mathcal H_1)\), which is already a closed finite-dimensional space.
No inverse of a bounded operator is asserted to be bounded.

**Lemma 4.3: operator meaning of regularity.**
The kernel projection of \(\theta\in M\) belongs to \(M\).
The nonzero-divisor condition forces this projection to vanish.
In the polar decomposition, the initial support is then \(I\); finiteness and the faithful trace force the final support also to be \(I\), giving dense range.
This reconstructs the adaptation invoked by the source.
Finiteness is essential: an injective unilateral shift in \(B(\ell^2)\) has a proper closed range.

**Lemma 4.6: independence of fractions.**
Compare a representation with finite-rank defects to another \(u=f_1^{-1}a_1=b_1g_1^{-1}\).
Choose
\[
ff_1^{-1}=x^{-1}y,\qquad g^{-1}g_1=x'(y')^{-1}.
\]
All denominators are regular by construction, and the invertibility of the ratios also makes the relevant numerators regular.
In particular, \(y\) is injective and \(y'\) has dense range.
The bounded identities
\[
yf_1=xf,\quad ya_1=xa,\quad
g_1y'=gx',\quad b_1y'=bx'
\]
give
\[
y\Delta_i(f_1,a_1,b_1,g_1)y'
=x\Delta_i(f,a,b,g)x'.
\]
The right side is finite rank.
First cancel the injective left factor using Lemma 4.2(1), then the dense-range right factor using Lemma 4.2(2).
This proves finite rank for every representation.

### Findings, Local Adaptation, and Limits

The first line of the proof of Lemma 4.1 prints \(a_k,b_k,f_k,g_k\in\widetilde L^\infty(s)\).
The argument requires their bounded choices in \(L^\infty(s)\), which the opening paragraph already supplies.
This is a type/notation correction, not a new existence assumption.
Also, the lemma statement leaves regularity implicit in the fraction notation; reuse it with regular \(f,g\) explicitly stated.

No unresolved defect was found in the common-denominator or cancellation argument after making these boundedness and regularity conditions explicit.
The conclusion concerns finite rank, not an invariant numerical rank or a fixed bound on the ranks.
This unit does not define or assert a globally bounded commutator with an arbitrary affiliated operator.

### Dependencies and Verification Facts

Depends on the shared finite tracial setting, affiliated fraction calculus, and the elementary Hilbert-space arguments just given.
It supplies denominator independence and common fractions to U007, and bounded defects to U008.
Text and rendered pp. 19-20 were checked on 2026-09-08; no outside version, erratum, source [12] proof, computation, or proof-assistant artifact was checked.
This is the initial unit audit.


## Source and inspection

[Source and edition notes](readme.md).

Source edition: Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here.

Passages: Section 4 opening, Lemmas 4.1-4.3 and definitions of R(s), R'(s), p. 19; Lemma 4.6, p. 20.

Inspection: 2026-09-08: regular-denominator identities, cancellation and denominator-independent defects reconstructed from text and rendered Section 4 pages. The shared U006-U008 independent review and common setting are linked. General affiliation foundations were not independently audited; Linnell and Mai-Speicher-Yin were accessed here only through Miy22. Later source records do not retrospectively change this inspection; no external human review or formal verification.

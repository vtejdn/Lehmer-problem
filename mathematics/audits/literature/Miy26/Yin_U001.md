---
author: Yin
---

<a id="miy26-u001"></a>
# Miy26-U001: Fock and Affiliated-Operator Interfaces

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

- Source: [Miy26](../../../literature/pdf/Miy26.pdf), the user-supplied arXiv:2603.19528v2 artifact dated 2026-04-21.
- Locator: Section 2, pp. 4-6, Theorem 2.1; Theorem 1.1, p. 1.
  Printed and PDF page numbers agree.
- Record: 2026-09-08, the coordinating agent, source reading and local interface reconstruction for [Miy26 spectral source audit](readme.md#miy26-spectral-source-audit).
- Kind and coverage: definitions and reused source interfaces, audited at the finite-system scope below.
  Imported general affiliated-operator theory and free-field results have their actual verification depth recorded in U008.

## Setting and hypotheses

Fix a finite integer $d\geq1$, $H=\mathbb C^d$, and full Fock space

$$
\mathcal F(H)=\bigoplus_{n\geq0}H^{\otimes n},\qquad H^{\otimes0}=\mathbb C\Omega.
$$

For the standard orthonormal basis, left creation $\ell_i$ prepends $e_i$ and right creation $r_i$ appends it.
Their adjoints remove a matching first or last letter and annihilate the vacuum.
Put $s_i=\ell_i+\ell_i^*$, and

$$
\mathcal P=\mathbb C\langle s_1,\ldots,s_d\rangle,
\quad A=C^*(s_1,\ldots,s_d),\quad M=W^*(s_1,\ldots,s_d).
$$

The faithful normal trace is $\tau(x)=\langle x\Omega,\Omega\rangle$; the $s_i$ are variance-one free semicircular operators.
We use $\|f\|_2^2=\tau(f^*f)$ and the unitary identification $L^2(M,\tau)\simeq\mathcal F(H)$.
The left/right multiplication conventions and the word basis are those already audited in [Miy22-U001](../Miy22/Yin_U001.md#miy22-u001).

For words $w=w_1\cdots w_n\in[d]^*$, $e_w=e_{w_1}\otimes\cdots\otimes e_{w_n}$ and $U_w\in\mathcal P$ is the Wick/Chebyshev polynomial satisfying $U_w\Omega=e_w$.
The empty word has $U_\varnothing=1$ and $e_\varnothing=\Omega$.
Reversal $w^{\rm rev}=w_n\cdots w_1$ satisfies $U_w^*=U_{w^{\rm rev}}$.
Word-polynomial substitution is linear, not multiplicative: $U_i^2=U_{ii}+1$.

**Source scope correction.**
The p. 5 assertion that $M$ is a $\mathrm{II}_1$ factor cannot hold for $d=1$, when $M=W^*(s_1)$ is abelian.
The proofs use a finite tracial von Neumann algebra with faithful trace, not factoriality; the main theorem includes the one-generator case unchanged.
For $d\geq2$ the familiar factor identification is a separate foundational fact, unnecessary here.

## Three ambient spaces and two closures

Let $L^0(M,\tau)$ denote the algebra of closed densely defined affiliated operators.
In a finite tracial algebra these are measurable operators; sums and products mean their closed affiliated-algebra realizations, not arbitrary compositions of everywhere-defined maps.

- $C_{\rm div}(s)$ is the scalar division closure of $\mathcal P$ in $M$: invert only elements whose inverses exist in $M$.
- $D(s)$ is the scalar division closure of $\mathcal P$ in $L^0(M,\tau)$: invert elements invertible in that larger algebra.

These are definitions of inverse closure; being a skew field is an additional theorem, not part of either definition.
$D(s)$ is star closed: the adjoint of a finite inverse expression is again an inverse expression, using $(x^{-1})^*=(x^*)^{-1}$.
The precise imported assertion that every nonzero element of $D(s)$ has an affiliated inverse is recorded in [Miy26-U008](Yin_U008.md#miy26-u008).
It is needed for the general resolvent statement in U003.
The local regularization step of U002 only uses inverses known to exist by positivity, so it does not independently need the full free-field theorem.

For $f\in L^2(M,\tau)$, its affiliated realization $L_f$ is the closure of left multiplication on the bounded-vector domain $M\subset L^2(M,\tau)$.
On that domain,

$$
L_f(\widehat b)=f b=R_b f,\qquad b\in M,
\qquad \|fb\|_2\leq\|b\|\,\|f\|_2.
$$

Here $\widehat b=b\Omega$ and $R_b$ is bounded right multiplication.
Thus $\mathcal F_{\rm alg}(H)=\mathcal P\Omega$ lies in the domain of every $L^2$ affiliated operator.
This does not make $L_f$ bounded on all of Fock space.
Miy26 cites its AP18, Theorem 7.3.2, for this canonical realization; U008 records the inspected external evidence.
The association from an $L^2$ affiliated operator to its vector $f\Omega$ is injective, since equality of vectors gives zero $L^2$ norm of their difference and the trace is faithful.

## Theorem 2.1 and actual reuse from Miy22

Miy26 states the following two interfaces:

$$
f\in M:\quad f\in C_{\rm div}(s)
\Longleftrightarrow [r_i^*,f]\text{ has finite rank for every }1\leq i\leq d,
$$

and

$$
D(s)\cap M=C_{\rm div}(s).
$$

These are quoted from [Miy22](../../../literature/pdf/Miy22.pdf), Theorems 3.1 and 4.5, with supporting Lemma 4.3.
Their bounded analytic and affiliated proof chains are already recorded in [Miy22-U005](../Miy22/Yin_U005.md#miy22-u005), [Miy22-U006](../Miy22/Yin_U006.md#miy22-u006), and [Miy22-U007](../Miy22/Yin_U007.md#miy22-u007), with the existing repairs and external-proof limits.
This audit checks the match of the finite variance-one system, trace, scalar closures, and bounded operators; it does not erase those earlier verification boundaries or restart a whole Miy22 audit.

The polynomial commutator formula is

$$
[r_i^*,U_w]e_v=
\begin{cases}
e_u,&w=uiv^{\rm rev},\\
0,&\text{otherwise}.
\end{cases}
$$

It follows from the cut formula in [Miy22-U003](../Miy22/Yin_U003.md#miy22-u003), with commutator convention $[T,f]=Tf-fT$.
U002 separately justifies its extension to $L^2$ coefficients; the bounded-only statement is not silently applied to an arbitrary unbounded operator.

The homogeneous semicircular Haagerup estimate used later is

$$
\left\|\sum_{|w|=n}\alpha_wU_w\right\|
\leq(n+1)\left(\sum_{|w|=n}|\alpha_w|^2\right)^{1/2}.
$$

It is the precise $q=0$ bound used in Miy26 p. 9 and Miy22 Lemma 3.5.
The corresponding word-operator decomposition and norm estimate were reconstructed in [Miy22-U004](../Miy22/Yin_U004.md#miy22-u004).
It concerns a fixed homogeneous degree and standard semicircular normalization; an estimate for an arbitrary polynomial follows by summing degrees, not by asserting a universal norm equality.

## Limits, verification, and revisions

The coordinating agent read Section 2 and the cited existing Miy22 units, and visually inspected the defining formulas and Theorem 2.1 on pp. 5-6 on 2026-09-08.
The finite-dimensional Fock actions, closure distinctions, and domain inequality above were checked locally.
General trace/affiliation infrastructure remains explicitly imported; any additional primary inspection is linked through U008.
No new project theorem, unrestricted operator-domain assertion, or formal verification is made.
On 2026-09-08, the separate spectral-interface reviewer checked the regularizer domains, canonical L2 model and reused interfaces; no unresolved local issue was found.
The integrated audit records the complete review scope.

## Additional retained definition source recheck

<a id="definition-recheck"></a>

Date: 2026-09-10.
Reviewer: the unbounded-operator agent, primary-source reading and self-review.
Scope: definition and notation reuse in the existing Miy26 units.

Source: [Miy26](../../../literature/pdf/Miy26.pdf), arXiv:2603.19528v2, 2026-04-21, 23 pages.
Printed and PDF page numbers agree.
Text on pp. 1–2, 4–6 and 10–12 was read; rendered pages 1–2, 5–6 and 10–12 were inspected.
No new whole-paper review or source-version comparison is claimed.

## Definitions retained in their existing homes

| Concept | Exact home | Rechecked source locator and use |
| --- | --- | --- |
| Algebraic/full Fock space and standard semicircular tuple | [U001, Setting and hypotheses](#setting-and-hypotheses) | Section 2, pp. 4–5. Algebraic finite sums precede Hilbert completion; \(s_i=\ell(e_i)+\ell(e_i)^*\). This is the same construction as Miy22-U001, with the same first-linear source inner product. |
| Semicircular word coefficients and reversal | [U001, Setting and hypotheses](#setting-and-hypotheses) | p. 6 defines \([d]^*\), the empty word, length, tensor basis and reversal \(w^*\). The starred symbol at this point only reverses letters. |
| Canonical closed left multiplication associated with an \(L^2\) vector | [U001, Three ambient spaces and two closures](#three-ambient-spaces-and-two-closures) | p. 5: start with \(\widehat b\mapsto R_b f=fb\) on bounded vectors \(b\in M\), then take its closure.
The source explicitly includes the algebraic Fock domain; it does not declare an everywhere-defined bounded operator. |
| Circular normalization, barred letters and mixed Wick basis | [U004, Statement and hypotheses](Yin_U004.md#statement-and-hypotheses) | Section 4 opening, pp. 11–12: \(c_i=(s_i+\mathrm i s_{d+i})/\sqrt2\). The Hilbert space for the full starred algebra has \(2d\) letters. |
| Holomorphic polynomial algebra and its \(L^2\) closure | [U004, Statement and hypotheses](Yin_U004.md#statement-and-hypotheses) | Bottom of p. 12: \(\mathbb C\langle c\rangle\) omits adjoints; \(L^2(c,\tau)\) is its \(L^2\) closure. It is distinct from \(L^2(c,c^*,\tau)\). |
| Free-Haar instance of the affiliated rational algebra | [U003, Theorem 3.5: completing the Haar argument](Yin_U003.md#theorem-35-completing-the-haar-argument) | Theorem 3.5 and preceding paragraph, p. 10. Miy26 names free Haar unitaries and refers to DR97/Lin00; the audited realization is \(u_i=\lambda(g_i)\) in \(L(F_d)\), with the regular trace. |

<a id="circular-word-conventions"></a>
## Circular word and space conventions

The complete adopted definitions already appear in [U004](Yin_U004.md#statement-and-hypotheses).
The rendered source confirms the conjugate label:

\[
u_i=(e_i+\mathrm i e_{d+i})/\sqrt2,\quad
u_{\bar i}=(e_i-\mathrm i e_{d+i})/\sqrt2,\qquad
c_i=\ell(u_i)+\ell(u_{\bar i})^*.
\]

Thus \(\tau(c_i^*c_j)=\delta_{ij}\).
For the mixed-word convention the involution reverses the word and bars every letter.
It is different from the plain reversal of the selfadjoint semicircular alphabet, though both implement the adjoint of the corresponding Wick polynomial.
Ordinary holomorphic words \(c_w\Omega=u_w\), \(w\in[d]^*\), form a basis of the holomorphic subspace only.
They are not a basis of the full \(2d\)-letter GNS space.
No normality of the circular variables is asserted.

These are source-formulation checks, not a new equivalence theorem.
The equality of the two starred polynomial algebras after the displayed linear change of variables is already the explicit source convention on p. 12.
Its division-closure instance does not create a new general closure definition.

## Ambient and domain conventions

Miy26 p. 5 and the first line of p. 6 use the general scalar division-closure definition, with two ambient choices, \(M\) and \(L^0(M,\tau)\).
The [existing U001 entry](#three-ambient-spaces-and-two-closures) is the exact instance record.
Use the common MSY23/Yin20 ring-definition entry for the general construction rather than registering either choice as another definition.
That \(D(s)\) is a skew field is a cited theorem, not a consequence of the word “closure.”

The source names the affiliated algebra but does not give the general affiliation definition there.
The canonical \(L^2\)-operator construction above has its retained external foundation in [U008](Yin_U008.md#miy26-u008).
Its bounded-vector domain must not be replaced by an arbitrary dense domain without proof.
The p. 5 factor assertion requires the existing \(d=1\) correction in [U001](#setting-and-hypotheses); that correction remains unchanged.

No rank metric is defined or used in the rechecked definition passages.
The finite rank in Lemma 3.1 is the ordinary dimension of the commutator image on the indicated algebraic core.
It is not tracial rank and is not a definition of a bounded extension.

## Spectral definition pointer

The existing [U003, Corollary 1.2 with unbounded-operator conventions](Yin_U003.md#corollary-12-with-unbounded-operator-conventions) is also an exact definition home.
The source opening on p. 1 defines the ordinary spectrum by failure of a bounded inverse; the continuation of Corollary 1.2 on p. 2 defines \(\operatorname{spec}_1^2(f)\) as the complement of the set of points having a neighborhood throughout which the affiliated inverse belongs to \(L^2\).
In the audit notation it is \(\mathbb C\setminus\operatorname{int}R_2(f)\).
The neighborhood requirement is part of this definition.
Equality with the pointwise inverse-failure set is the subsequent theorem in the rational semicircular setting, not its general definition.

Both pages were checked in text and images for this pointer.
The attribution to HK19 on source p. 2 was read through Miy26 only; no historical-priority claim or new primary audit of that reference is made.
This entry supports the existing source audit and provides a notation citation candidate; no new Claim-level proof dependency is asserted.

## Consumer navigation and inspection limits

The earlier consumer account distinguished its model-specific semicircular/circular/Haar interfaces from general finite-residual and R-diagonal holomorphic settings.
The former C_F0015/C_F0017 fixed proof consumers are not located in the current retained F-family collection; no current same-number theorem or additional proof dependency is inferred from those historical labels.

Citation purposes are current formulation and notation for the circular normalization and canonical \(L^2\) realization, and exposition for the semicircular/Haar applications.
No historical priority claim is supported by this check.
The earlier complete source audit retains its own proof and dependency assessments.
No old mathematical or source-audit file was modified.

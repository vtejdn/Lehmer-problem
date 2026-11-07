---
author: Yin
---

<a id="miy22-u001"></a>
# Miy22-U001: Fock Model, Word Basis, and Ambient Closures

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

- Source: [Miy22](../../../literature/pdf/Miy22.pdf), local published journal version, 24 pages.
- Locators: Section 2.1, pp. 3-6; Definitions 2.1-2.3; Section 3 opening, p. 8; Section 4 opening, p. 19.
- Record: 2026-09-08, primary audit by the coordinating agent; source text read and rendered formulas inspected.
  This is a source-input unit for [Miy22 source audit](readme.md#miy22-source-audit).
- Kind: definitions, notation normalization, and foundational source inputs.

## Mathematical Setting

Let $d\geq1$ be finite, $H=\mathbb C^d$ with orthonormal basis $e_1,\ldots,e_d$, and

\[
\mathcal F(H)=\bigoplus_{n\geq0}H^{\otimes n},\qquad H^{\otimes0}=\mathbb C\Omega.
\]

The source uses inner products linear in the first variable.
For a word $w=w_1\cdots w_n$, write $e_w=e_{w_1}\otimes\cdots\otimes e_{w_n}$.
The empty word is represented by $\Omega$.
The left and right creation operators prepend and append letters:

\[
\ell_i e_w=e_{iw},\qquad r_i e_w=e_{wi}.
\]

Their adjoints delete the first or last letter if it equals $i$, and otherwise return zero; both annihilate $\Omega$.
Set

\[
s_i=\ell_i+\ell_i^*,\qquad P=\mathbb C\langle s_1,\ldots,s_d\rangle,
\quad A=C^*(s_1,\ldots,s_d),\quad M=W^*(s_1,\ldots,s_d).
\]

The paper writes $M=L^\infty(s)$ and denotes $A$ by a norm-closure bar over $\mathbb C\langle s\rangle$.
That bar is easily lost in text extraction; this audit uses $P,A,M$ to keep the three algebras distinct.

The vacuum state $\tau(x)=\langle x\Omega,\Omega\rangle$ is a faithful trace on $M$, and the $s_i$ form a variance-one free semicircular family.
The vacuum is cyclic and separating.
The map $x\mapsto\widehat x=x\Omega$ extends to a unitary $L^2(M,\tau)\to\mathcal F(H)$.
These statements are stated on p. 5 and imported there from Miy22's references [15] and [18]; those textbooks were not independently inspected in this audit.
In particular, do not call $M$ a factor uniformly in $d$: $d=1$ is included.

## Word Polynomials and Reversal

The source's monic semicircular Chebyshev normalization is

\[
U_{-1}(x)=0,\quad U_0(x)=1,\quad U_{n+1}(x)=xU_n(x)-U_{n-1}(x).
\]

For the maximal-run decomposition $w=i_1^{k_1}\cdots i_m^{k_m}$, with adjacent run letters distinct, define

\[
U_w=U_{k_1}(s_{i_1})\cdots U_{k_m}(s_{i_m}),\qquad U_\Omega=1.
\]

Then $U_w\Omega=e_w$, so the $U_w$ form an orthonormal basis of $L^2(M,\tau)$.
The run letters need not be pairwise distinct: a word such as $121$ is allowed.
Let $w^{\mathrm{rev}}$ denote reversal; then $U_w^*=U_{w^{\mathrm{rev}}}$.
The source writes $w^*$ for this word reversal, which must not be confused with coefficient conjugation.

The map $X^w\mapsto U_w$ is linear, not multiplicative.
For example, $U_i^2=U_{ii}+1$.
Substituting $s_i$ directly into a formal series whose coefficients are the $U_w$-expansion therefore does not preserve its coefficient interpretation; [U004](Yin_U004.md#miy22-u004) supplies the necessary matrix realization.

For cancellation notation, $vw^{-1}$ removes a suffix $w$, while $w^{-1}v$ removes a prefix.
Failed removal is a zero symbol, not the empty word.
The paper denotes that symbol by $0$, sets $U_0=0$, and separately uses the polynomial $U_0(x)=1$.
In reusable formulas, distinguish the zero vector from $e_\Omega=\Omega$.

## Closure Interfaces

For unital $B\subseteq E$, the division closure is the smallest unital subalgebra containing $B$ and closed under inversion of its elements invertible in $E$.
Rational closure requires the analogous property for inverses of matrices of every finite size.

In this paper:

- $C_{\mathrm{div}}(s)$ and $C_{\mathrm{rat}}(s)$ are the two closures of $P$ inside the **bounded** algebra $M$.
- $\widetilde M=\widetilde L^\infty(s)$ is the algebra of closed densely defined operators affiliated with $M$, with the affiliated-algebra sum/product conventions.
- $D(s)$ is the division closure of $P$ inside $\widetilde M$.

Division closure is not by definition a skew field.
A bounded nonzero element need not be boundedly invertible; inverse closure in $M$ differs from inversion in $\widetilde M$.
The equality of division and rational closures in Theorem 3.1 is a theorem in this setting, not a general algebraic identity.
See [U007](Yin_U007.md#miy22-u007) for the external free-field identification quoted in Section 4 and its role outside the core proof.

## Checks, Dependencies, and Limits

The creation/deletion actions, the Chebyshev vacuum recurrence, and the reversal identity were reconstructed from the definitions.
For a single run, the recurrence cancels the backward-annihilation term; appending a different run leaves only the required creation term when acting on the vacuum.
The separating-vector property can also be checked using the right semicircular operators: they commute with the left algebra and generate a dense vacuum orbit.

The trace/free-semicircular identification and the general affiliated-algebra construction are retained as the foundational inputs quoted by Miy22, without a new proof of those external theories.
No claim is made for an arbitrary tuple of noncommuting operators, a nontracial state, an infinite number of generators, or a different covariance normalization without further adaptation.

This unit supplies the objects used by all other Miy22 units.
No new project theorem or formal verification is asserted.

## Additional retained definition source recheck

<a id="definition-recheck"></a>

Date: 2026-09-10.
Reviewer: the unbounded-operator agent, source reading and self-review.
This is a selected definition/convention reading, with no new whole-source proof review.

Source: [Miy22](../../../literature/pdf/Miy22.pdf), the 24-page published journal version.
This review retains its original input and inspection scope.
Printed and PDF pages agree.

## Inspection and exact definition homes

Extracted text was reread on pp. 3–8 and 19.
Complete rendered pages 4–8 and 19 were inspected, including closure bars, transpose, word cancellation and Laurent exponents.
The entries below retain the existing complete definitions in place; this section supplies the checked source locators.

| Concept | Exact existing home | Source locator and confirmed convention |
| --- | --- | --- |
| Full Fock space, word basis, creation and annihilation | [U001, Mathematical Setting](#mathematical-setting) | Section 2.1, pp. 3–5; Definition 2.1, p. 4. Hilbert direct sum including the vacuum sector; left creation prepends and right creation appends. Both annihilators kill the vacuum. |
| Standard semicircular Fock normalization and tracial GNS identification | [U001, Mathematical Setting](#mathematical-setting) | \(s_i=\ell_i+\ell_i^*\), p. 4; vacuum trace and \(L^2\) identification, p. 5.
The source inner product is linear in its first argument, \(\langle x,y\rangle=\tau(y^*x)\). |
| Wick/Chebyshev word polynomials and reversal | [U001, Word Polynomials and Reversal](#word-polynomials-and-reversal) | p. 5: \(U_{-1}=0,\ U_0=1,\ U_{n+1}(x)=xU_n(x)-U_{n-1}(x)\); maximal runs define \(U_w\), with \(U_w\Omega=e_w\). Only adjacent run labels must differ. |
| Prefix/suffix removal | [U001, Word Polynomials and Reversal](#word-polynomials-and-reversal) | Definition 2.2, pp. 5–6. \(vw^{-1}\) removes a suffix and \(w^{-1}v\) a prefix. Failed removal is the zero symbol, distinct from the empty word. |
| Formal series, recognizability and rational formal series | [U002, Formal Series and Exact Interfaces](Yin_U002.md#formal-series-and-exact-interfaces) | Section 2.2, Definition 2.4, p. 6, and opening p. 7. Coefficients satisfy \(\alpha_v=\lambda^{\mathsf T}\mu(v)\gamma\). The transpose is algebraic, not adjoint. Rationality is scalar inverse closure in the formal-series algebra. |
| Left/right residual spaces; minimal-dimensional representation | [U002, Formal Series and Exact Interfaces](Yin_U002.md#formal-series-and-exact-interfaces) | Theorem 2.5 and paragraph before Theorem 2.6, p. 7. Right residuals have coefficients \(\alpha_{uw}\), left residuals \(\alpha_{wu}\). Minimal means smallest representation dimension, not merely any finite realization. |
| Hadamard product | [U002, Formal Series and Exact Interfaces](Yin_U002.md#formal-series-and-exact-interfaces) | Definition immediately before Theorem 2.7, p. 7: coefficients are multiplied at the same word. No convolution or operator product is intended. |
| Bounded Hankel operator and Laurent convention | [U009, Exact Statement and Conventions](Yin_U009.md#exact-statement-and-conventions) | Section 2.3, pp. 7–8. \(H_{m,n}=\alpha_{m+n}\) on \(\ell^2(\mathbb N_0)\), with boundedness explicitly part of the source's operator convention; \(a(z)=\sum_{n\ge0}\alpha_n z^{-n-1}\). |
| Regular bounded denominators and bounded fractional defect | [U006, Statements, Assumptions, and Notation](Yin_U006.md#statements-assumptions-and-notation) | Section 4 opening, p. 19; definitions of \(R(s),R'(s)\) on the same page. Regular means nonzero divisor; \(u=f^{-1}a=bg^{-1}\) has bounded coefficients and regular \(f,g\). The defect is \(fr_i^*b-ar_i^*g\). |

The finite-residual/recognizable/rational equivalence and the minimal-realization consequences are existing source results, not new definitions or claims to be reproved by this indexing operation.
Their proof-inspection boundaries remain in U002; the selected BR10 primary-definition supplement is [recorded separately](../BR10/Yin_U002.md#definition-recheck).

## Closure and affiliation instances

Definition 2.3, p. 6, states the same general division and matrix rational closures indexed from the project's MSY23/Yin20 ring sources.
The exact Miy22 entry remains [U001, Closure Interfaces](#closure-interfaces).
This is an additional formulation/citation candidate for that same definition, not a new definition arising from its parameters.

The source instances are \(B=\mathbb C\langle s\rangle\) in the bounded ambient algebra \(M=L^\infty(s)\), p. 8, and in \(U(M)=\widetilde L^\infty(s)\), p. 19.
The equality between their resulting closures is a theorem at the audited semicircular scope.
It is not a definition and cannot be transferred to another tuple by notation alone.

The opening of Section 4 names closed densely defined affiliated operators and uses their algebra structure.
It does not restate the general commutant/domain definition of affiliation.
Therefore this page is an application and a fraction reference, not the authoritative general affiliation definition.
The standard-infrastructure boundary is explicit in [the existing shared conventions](Yin_U006.md).
No rank metric is introduced in these inspected passages.

<a id="usage-boundaries"></a>
## Usage boundaries and consumers

- Formal series here have finitely many formal variables and arbitrary complex coefficients.
  Neither recognizability nor formal invertibility includes an \(L^2\), norm-convergence or bounded-evaluation hypothesis.
- \(X^w\mapsto U_w\) is the linear word-basis correspondence.
  It is not algebra substitution: \(U_i^2=U_{ii}+1\).
  The existing [analytic-realization audit](Yin_U004.md#miy22-u004) owns the actual evaluation argument.
- The source's first-linear inner product must be converted when used with the project's second-linear convention.
  Stating the column action of a Hankel matrix avoids introducing an unintended conjugate.
- The Laurent convention is strictly proper at infinity.
  The existing rank statement counts reduced poles with multiplicity, including zero; [U009](Yin_U009.md#exact-statement-and-conventions) already records the zero-series convention and the distinction from the one-normal divided-difference kernel.
  The earlier repeated-pole estimate correction remains in [U002](Yin_U002.md#scalar-rational-decay-and-the-printed-error).

The earlier source account's actual Fock/residual/formal-elimination consumers are [original C_F0011](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/claims/Yin_C_F0011_v1.md#inputs-and-their-exact-roles), [original C_F0015](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/claims/Yin_C_F0015_v1.md#yin_c_f0015) and [original C_F0017](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/claims/Yin_C_F0017_v1.md#yin_c_f0017).
The [fixed original proof and comparison-review boundary](Yin_U009.md#historical-one-normal-generator-comparison-the-same-finite-dimensional-mechanism) applies to these source-only links.
Their old numbers identify original-source objects, not current same-number Claims; they create no new local dependencies.
The one-normal-generator comparison remains in U009, with the fixed original proof, source-only access and actual review boundary stated there.

Citation purposes: current formulation or notation for the Fock/residual/Hankel conventions, and exposition for their role in semicircular rationality.
No origin claim is made.
This sidecar does not change historical proof dependencies, conduct an independent audit of every imported theorem, or perform formal verification.
The existing source units and PDF were left unchanged.

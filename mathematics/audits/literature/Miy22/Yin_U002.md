---
author: Yin
---

<a id="miy22-u002"></a>
# Miy22-U002: Rational Series, Finite Residual Spaces, and Decay

- Source: [Miy22](../../../literature/pdf/Miy22.pdf), published version, pp. 6-8.
- Locators: Definition 2.4, Theorems 2.5-2.8, and Corollary 2.9.
- Record: 2026-09-08, source audit by the coordinating agent; repeated-pole issue independently noticed by both Section 3 reviewers.
  Source text and rendered pp. 6-8 inspected.
- Kind: imported algebraic interfaces and an analytic input with an explicit correction.
- Prerequisite: [U001](Yin_U001.md#miy22-u001).

## Formal Series and Exact Interfaces

Let $Z=\sum_{v\in[d]^*}\alpha_vX^v\in\mathbb C\langle\!\langle X_1,\ldots,X_d\rangle\!\rangle$.
Formal inversion requires a nonzero constant coefficient and is not an operator-convergence assertion.
A rational series is in the division closure of the noncommutative polynomials in this formal-series algebra.

For a word $w$, normalize the right and left residuals as

\[
Z\mathbin{\triangleleft}w=\sum_u\alpha_{uw}X^u,
\qquad w\mathbin{\triangleright}Z=\sum_u\alpha_{wu}X^u.
\]

These are the cancellation sums on p. 7, with terms from unsuccessful cancellations understood as zero.
Theorem 2.5 states the equivalence of:

1. finite-dimensional span of all right residuals;
2. finite-dimensional span of all left residuals;
3. a finite linear representation $\alpha_v=\lambda^{\mathsf T}\mu(v)\gamma$, where $\mu$ is a monoid representation by complex matrices;
4. rationality of $Z$.

The transpose in this representation is algebraic transpose, not conjugate transpose.
No summability assumption belongs to this algebraic equivalence.

For a **minimal-dimensional** representation, Theorem 2.6 states that there are finitely many words $u_k,w_l$ and constants $c_{ij}^{kl}$ such that, uniformly in $v$,

\[
\mu(v)_{ij}=\sum_{k,l}c_{ij}^{kl}\alpha_{u_kvw_l}.
\]

Minimality matters: unused states could contain matrix growth invisible in the coefficient sequence.
The audit checked the underlying finite-dimensional mechanism: minimality makes the reachable columns $\mu(w)\gamma$ and observable rows $\lambda^{\mathsf T}\mu(u)$ span the state space and its dual.
Choosing finite bases expresses each matrix entry by their pairings, producing the displayed formula.
Consequently, if $\sum_v|\alpha_v|^2<\infty$, every entry sequence $\{\mu(v)_{ij}\}_v$ is square summable, since $v\mapsto u_kvw_l$ is injective and the sum over $k,l$ is finite.

Theorem 2.7 states that rational series are closed under coefficientwise Hadamard multiplication.
A representation-level check is immediate: if coefficients are represented by $\mu,\nu$, their products are represented by $\mu\otimes\nu$.
Conjugating every coefficient similarly conjugates the finite matrices and preserves recognizability.
Summing coefficients of a fixed word length is encoded by the single matrix $\sum_i\mu(i)$; this makes the corresponding one-variable generating series rational.

Theorem 2.5 is attributed by Miy22 to its reference [2], Corollary 1.5.4 and Theorem 1.7.1; Theorems 2.6 and 2.7 to Corollary 2.2.3 and Theorem 1.5.5 of that reference.
The book itself was not read in this audit.
The imported equivalence is source-statement-verified in Miy22; the finite representation consequences above were checked directly, without claiming a complete independent proof of the rational-series theorem.

## Scalar Rational Decay and the Printed Error

Corollary 2.9 states: if $A(z)=\sum_{n\geq0}\alpha_nz^n$ is rational and $\sum_n|\alpha_n|^2<\infty$, then there are $M>0$ and $0<c<1$ with

\[
|\alpha_n|\leq Mc^n.
\]

Including $n=0$ only changes $M$.
This is the form needed for [U004](Yin_U004.md#miy22-u004).

**Finding F01 (p. 8): the preceding paragraph's choice of rate is too strong.**
The source takes $c$ equal to the maximum modulus of a pole of its Laurent generating function.
For $0<r<1$,

\[
\alpha_n=(n+1)r^n,\qquad
\sum_{n\geq0}\alpha_nz^{-n-1}=\frac{z}{(z-r)^2}.
\]

There is a double pole at $r$, but $\alpha_n/r^n=n+1$ is unbounded.
Thus no fixed $M$ gives the printed bound at $c=r$, despite square summability.
This is a counterexample to that auxiliary estimate, not to Corollary 2.9 or the main theorem.

The repair is to choose a strictly larger rate $r<c<1$, absorbing the polynomial factors from repeated poles.
A direct analytic justification of the corollary is also available: square summability makes $A$ analytic in the unit disk and keeps its radial $L^2$ means bounded.
A genuine pole on the unit circle would make those means diverge; hence a rational $A$ has no poles on or inside that circle after cancellation.
Choose $R>1$ below its nearest pole modulus and apply Cauchy's coefficient estimate on $|z|=R$, obtaining $M R^{-n}$.
A polynomial has no pole obstruction and is covered by increasing $M$.

For completeness, near a pole of order $k\geq1$ at $e^{i\theta_0}$, the radial integral is bounded below by a constant times $(1-\rho)^{1-2k}$ on an angular interval of length comparable to $1-\rho$, as $\rho\uparrow1$.
This supplies the claimed divergence and avoids assuming a boundary estimate without justification.

## Hankel Interpretation and Limits

Theorem 2.8 concerns a **bounded** Hankel operator on $\ell^2(\mathbb Z_{\geq0})$, with matrix entries $\alpha_{m+n}$, and rational Laurent functions with poles strictly inside the unit disk.
Read the pole count with multiplicity after cancellation, including a possible pole at zero.
Algebraic rank of a formal infinite matrix alone is not a bounded-operator hypothesis; for example, exponentially growing coefficients cannot be silently admitted.

At the original 2026-09-08 audit, Theorem 2.8 was a classical input quoted by Miy22 via references [11] and [16], not independently checked against those originals.
The direct argument above verifies the specific decay consequence needed downstream.
The correction must be used wherever the printed sharp rate would otherwise be invoked.

Follow-up, 2026-09-09: [Miy22-U009](Yin_U009.md#miy22-u009) now supplies a complete locally reconstructed proof of the exact bounded-Hankel theorem, including the pole-multiplicity/rank equality, and compares it with Yin_C_F0004's divided-difference argument.
A selected modern primary book proof was also read.
The original Kronecker/Partington proofs remain unreviewed; the new reconstruction is not retrospectively attributed to the original Miy22 source audit.

## Use and Verification Boundary

This unit supplies the bridge from finite residual spaces to finite-state representations and the scalar exponential bound used in the norm-convergence argument.
The genuine formal-to-operator bridge is still [U004](Yin_U004.md#miy22-u004); rational formal syntax does not by itself make substitution converge.

The source statements, residual order, transpose convention, minimal-representation consequence, Hadamard/tensor mechanism, and repaired scalar decay were checked as described.
No external book audit, proof-assistant verification, numerical proof, or new project claim is asserted.
F01 is a local source correction documented for reuse under [Miy22 source audit](readme.md#miy22-source-audit).

## Source and inspection

Source edition: Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here.

Passages: Definition 2.4, Theorems 2.5-2.8 and Corollary 2.9, pp. 6-8. The later complete Kronecker proof is separately owned by U009.

Inspection: 2026-09-08: source statements, residual/transpose conventions and scalar decay checked; repeated-pole repair independently noticed by both Section 3 reviewers. Formal-series equivalence retains its imported scope. The initial Kronecker/Partington original proofs were unreviewed; the separately dated U009 follow-up does not retrospectively upgrade that original inspection. No complete external-book audit or formal verification.

---
author: Yin
---

# Capacity and the Polynomial Scaling Bound

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Source/version: registered full GGOW20 article, [PDF](../../../literature/pdf/GGOW20.pdf), published pp. 223-290.

Passages: Locators: Definitions 2.1-2.11 and Propositions 2.7-2.8, pp. 243-246 (PDF 21-24); Theorems 2.12/2.14 and Algorithm 1, pp. 246-249 (PDF 24-27); Lemmas 2.15/2.17, Corollary 2.16 and Theorems 2.18/2.20, pp. 249-253 (PDF 27-31).

Inspection: State: `Audited within scope`, with the corrections below.


<a id="ggow20-u002"></a>
## GGOW20-U002 - Capacity, scaling progress, and the integral lower bound

- Source/version: registered full GGOW20 article, [PDF](../../../literature/pdf/GGOW20.pdf), published pp. 223-290.
- Locators: Definitions 2.1-2.11 and Propositions 2.7-2.8, pp. 243-246 (PDF 21-24); Theorems 2.12/2.14 and Algorithm 1, pp. 246-249 (PDF 24-27); Lemmas 2.15/2.17, Corollary 2.16 and Theorems 2.18/2.20, pp. 249-253 (PDF 27-31).
- Record: 2026-09-12, the operator-scaling source reviewer, with independent review by the coordinating agent of Section 2.3 and its corrections.
Local proofs reviewed in full; the exact external free-field/blow-up interface and the finite-grid lemma remain identified foundations.
- State: `Audited within scope`, with the corrections below.
Bit complexity is a separate obligation handled in [U004](Yin_U004.md#ggow20-u004), rather than inferred from a polynomial iteration count.

### Definitions and normalization

For \(A_i\in M_n(\mathbb C)\), put \(T(X)=\sum_iA_iXA_i^*\) and \(T^*(Y)=\sum_iA_i^*YA_i\).
The adjoint is for the unnormalized matrix trace.
The finite-dimensional Kraus characterization of complete positivity is the convention in Definition 2.1; Remark 2.2 explicitly retains Choi's theorem relating it to positivity of all matrix amplifications.

Define

\[
 \operatorname{cap}(T)=\inf_{X>0,\ \det X=1}\det T(X)
 =\inf_{X>0}\frac{\det T(X)}{\det X},\qquad
 \operatorname{ds}(T)=\operatorname{Tr}(T(I)-I)^2+
                   \operatorname{Tr}(T^*(I)-I)^2.
\]

Here \(X>0\) means positive definite, \(*\) is conjugate transpose, and all traces are **unnormalized**.
Capacity is nonnegative; the infimum need not be attained.
It is not a channel's information-transmission capacity.
A map is right normalized when \(T^*(I)=I\), left normalized when \(T(I)=I\), and doubly stochastic when both hold.

For invertible \(B,C\in M_n(\mathbb C)\), let

\[
 T_{B,C}(X)=B T(CXC^*)B^*.
\]

The determinant change of variables in Proposition 2.7 gives

\[
 \operatorname{cap}(T_{B,C})=|\det B|^2|\det C|^2\operatorname{cap}(T).
\]

Proposition 2.8 gives \(\operatorname{cap}(T)\leq1\) if either marginal is \(I\), because \(\operatorname{cap}(T)\leq\det T(I)\leq(\operatorname{Tr}T(I)/n)^n=1\).
There is no such universal upper bound for an unnormalized map.

The [Gur04 capacity/scaling interface](../Gur04/Yin_U002.md#gur04-u002) supplies positivity of capacity exactly when the map is rank non-decreasing, and the existence of arbitrarily accurate doubly stochastic scalings.
These are approximate statements; attainment and exact scaling have separate conditions in [Gur04-U003](../Gur04/Yin_U003.md#gur04-u003).

### Scaling progress checked

Right normalization is \(T_R(X)=T(T^*(I)^{-1/2}XT^*(I)^{-1/2})\); left normalization is \(T_L(X)=T(I)^{-1/2}T(X)T(I)^{-1/2}\).
Algorithm 1 first tests both marginals for singularity.
A singular \(T(I)\) decreases the rank of \(I\); a vector in \(\ker T^*(I)\) lies in every \(\ker A_i\) and yields a rank-one obstruction.
If both marginals are nonsingular, invertible scaling preserves that property and preserves shrunk-space existence.

Theorem 2.12: a left or right normalized map with \(\operatorname{ds}(T)\leq1/(n+1)\) is rank non-decreasing.
For example take \(T(I)=I\), \(T^*(I)=I+E\), and a rank-\(r\) projection \(P\).
Positivity gives \(0\leq T(P)\leq I\), hence

\[
 \operatorname{rank}T(P)\geq\operatorname{Tr}T(P)
 =r+\operatorname{Tr}(EP)
 \geq r-\sqrt{r\operatorname{Tr}(E^2)}>r-1.
\]

The integer-valued rank and equality of the support of \(T(P)\) and \(T(X)\) for \(X\geq0\) with range \(P\mathbb C^n\) finish the proof.
The other normalization follows by the symmetric block/shrunk-space criterion, which is invariant under adjoint.

Algorithm 1 tests whether some normalized iterate has \(\operatorname{ds}\leq1/(6n)\).
The robust determinant estimate of Lemmas 5.1-5.2 gives an increase of capacity by at least \(e^{1/(36n)}\) per unsuccessful step.
If the first right-normalized map has capacity at least \(f>0\), then \(t\geq2+36n\log(1/f)\) steps force success, since every normalized capacity is at most one (Theorem 2.14).
Take an integer ceiling for an implementation.
The source's displayed proof accidentally writes an equality with \(f\) where its hypothesis gives a lower bound; the needed inequality is in the correct direction.

### Integral lower bound and complete proof chain

**Theorem 2.18.** If \(A_1,\ldots,A_m\in M_n(\mathbb Z)\) and \(T_A\) is rank non-decreasing, then

\[
 \operatorname{cap}(T_A)\geq n^{-2n}.
\]

The proof in the full paper differs materially from the conference sketch.
It uses existence of a finite matrix substitution, not a quantitative upper bound on its dimension.

1. The [U001](Yin_U001.md#ggow20-u001) blow-up interface yields a nonzero polynomial \(p(D)=\det\sum_iD_i\otimes A_i\) for some dimension \(d\).
   Its total degree is \(nd\), and each individual matrix-entry degree is at most \(n\).
2. Lemma 2.15, the finite-grid consequence of Alon's combinatorial Nullstellensatz, permits a nonzero value at nonnegative integer entries with total sum at most \(nd\) and each entry at most \(n\).
   Consequently \(\sum_{i,k,l}D_i(k,l)^2\leq n^2d\) (Corollary 2.16).
   The original Alon proof is retained externally; the degree conversion and application were checked.
   "Positive integers" in the proof paragraph is read as **nonnegative**, as in the lemma and corollary.
3. Since the \(A_i\) are integral, \(\left|\det\sum_iD_i\otimes A_i\right|\geq1\).
4. Fix \(X>0\) with determinant one and set \(C_i=T_A(X)^{-1/2}A_iX^{1/2}\).
   Rank non-decrease ensures \(T_A(X)>0\), and \(\sum_iC_iC_i^*=I\).
   For \(Y=\sum_iD_i\otimes C_i\), determinant multiplicativity gives \(\det(YY^*)\geq\det T_A(X)^{-d}\).
5. The Hilbert-Schmidt inequality from Lemma 2.17 gives
   \[
   \operatorname{Tr}(YY^*)\leq
   \left(\sum_i\|D_i\|_{\mathrm{HS}}^2\right)
   \left(\sum_i\|C_i\|_{\mathrm{HS}}^2\right)\leq n^3d.
   \]
   Applied in dimension \(nd\), arithmetic-geometric mean yields \(\det(YY^*)\leq(n^2)^{nd}\).
   Hence \(\det T_A(X)\geq n^{-2n}\), independently of \(d\); take the infimum.

**Correction F1, Lemma 2.17, p. 250:** the printed proof uses \(\operatorname{Tr}(XY^*)=\operatorname{Tr}(YX^*)\), which is false for general complex matrices (the quantities are conjugates).
The inequality is valid.
A direct replacement is

\[
 \left\|\sum_i C_i\otimes D_i\right\|_{\mathrm{HS}}
 \leq\sum_i\|C_i\|_{\mathrm{HS}}\|D_i\|_{\mathrm{HS}}
 \leq\left(\sum_i\|C_i\|_{\mathrm{HS}}^2\right)^{1/2}
       \left(\sum_i\|D_i\|_{\mathrm{HS}}^2\right)^{1/2}.
\]

This proves the stated complex-matrix estimate and was independently checked by the coordinating agent.

For integral input with \(|A_i(k,l)|\leq M\), \(M\geq1\), Theorem 2.20 gives

\[
 \operatorname{cap}((T_A)_R)\geq\exp[-4n\log(Mmn)].
\]

Indeed the sharper intermediate lower bound is \(n^{-2n}(M^2mn)^{-n}\), because \(\det T_A^*(I)\leq(M^2mn)^n\).
**Correction F2, p. 253:** every denominator and trace written there as \(T^*(I)\) must refer to the **original** \(T_A^*(I)\), before right normalization; the normalized \(T\) itself satisfies \(T^*(I)=I\).
Combining this corrected identity with Theorem 2.14 gives \(O(n^2\log(Mmn))\) scaling steps.

### Dependencies, applicability, and checks

The nonzero finite blow-up theorem and Lemma 2.15 are accepted external inputs with exact applications disclosed above; their original proofs are not part of the source's supplied Section 2.3 proof.
The finite-dimensional spectral theorem, determinant identities, positivity, Cauchy-Schwarz and arithmetic-geometric mean are the elementary foundations.
Lemmas 5.1-5.2 and the precision analysis are recorded in [U004](Yin_U004.md#ggow20-u004).

The capacity bound applies to **integer Kraus matrices**, not arbitrary complex matrices or normalized maps without a denominator adjustment.
Clearing rational denominators changes capacity and input bit size and must be tracked.
No lower spectral bound for a free-probability operator evaluation follows from this finite-dimensional capacity theorem.
[MS24](../MS24/readme.md) uses and strengthens the integral-capacity interface; citations there to the expanded work refer to this full version, not the former conference artifact.

All local arguments above were read and checked; Section 2.3 additionally received the coordinating agent's independent direct source/formula review on 2026-09-12.
Rendered PDF pp. 27-31 were used for the determinant, tensor and normalization formulas.
No computation was represented as a proof of these general statements, and no formal verification was performed.
Corrections F1-F2 repair the recorded proof interfaces and do not challenge the main capacity lower bound.
No existing project Claim is newly marked proved by this intake.

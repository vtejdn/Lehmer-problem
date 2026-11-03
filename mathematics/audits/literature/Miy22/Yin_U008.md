---
author: Yin
---

<a id="miy22-u008"></a>
# Miy22-U008 - Cofinite Commutation with Explicit Operator Domains

This source analysis comprises [U006](Yin_U006.md#miy22-u006), [U007](Yin_U007.md#miy22-u007), [U008](#miy22-u008).
Its [shared source, inspection and setting](Yin_U006.md#miy22-affiliated-operators-and-domain-sensitive-rationality) and [joint review dated 2026-09-08](#independent-cross-review-of-u006-u008) retain their original scopes.


- Kind: domain-sensitive characterization and reconstruction of a terse variant.
- Source locators: Proposition 4.12 and its proof, pp. 22-23; Remark 4.13, p. 24.
- Verification: both directions, finite-codimension constructions, pointwise domain identities, and the creation-operator variant reconstructed.
  One false optional auxiliary construction was found; the alternative supplied by the source suffices.

### Statement and Domain Conventions

Proposition 4.12 states that \(u\in U(M)\) belongs to \(D(s)\) if and only if there is a linear subspace \(V\subset\mathcal H\) of finite algebraic codimension such that
\[
V\cap\bigcap_{i=1}^d\operatorname{dom}(u r_i^*)
=V\cap\operatorname{dom}(u),
\qquad
r_i^*u=u r_i^*\quad\text{on }V\cap\operatorname{dom}(u)
\]
for every \(i\).
The source names this subspace \(M\); here \(V\) avoids collision with the von Neumann algebra.

In this statement \(\operatorname{dom}(u r_i^*)\) means the domain of the literal composition:
\[
\{\xi\in\mathcal H:r_i^*\xi\in\operatorname{dom}(u)\}.
\]
The left composition \(r_i^*u\) has domain \(\operatorname{dom}(u)\).
These must not be replaced by the domains of unspecified closed extensions.
The annihilation statement uses an intersection over all \(i\); it does not assert equality with each individual \(\operatorname{dom}(u r_i^*)\).

Finite codimension is algebraic.
The subspaces constructed using complements below need not be Hilbert-closed.
No Hilbert-density or graph-norm-density assertion about \(V\cap\operatorname{dom}(u)\) is made or needed.
For a bounded linear map \(T\), the notation \(T^{-1}(W)\) in this proof means a set-theoretic inverse image, even if \(T\) has no inverse operator.

### Sufficiency: Cofinite Commutation Implies Rationality

Choose bounded regular fractions \(u=f^{-1}a=bg^{-1}\).
The affiliated equality with \(bg^{-1}\) means that \(u\) extends the literal composition on \(\operatorname{ran}g\); therefore
\[
g\mathcal H\subset\operatorname{dom}(u),\qquad ug=b
\quad\text{on all of }\mathcal H.
\]
Also \(fu=a\) on \(\operatorname{dom}(u)\).
The inverse image \(W=g^{-1}(V)\) has finite algebraic codimension, since \(\mathcal H/W\) injects into \(\mathcal H/V\).

For \(\xi\in W\), \(g\xi\) lies in \(V\cap\operatorname{dom}(u)\).
The assumed domain equality permits \(u r_i^*g\xi\), and the commutation identity gives
\[
\Delta_i(f,a,b,g)\xi
=f(r_i^*u g\xi-u r_i^*g\xi)=0.
\]
This uses the formal commutator expression only on vectors where its two terms are defined.
A bounded linear operator vanishing on a cofinite algebraic subspace has finite-dimensional range: it factors through the finite-dimensional quotient.
No density or passage to a graph closure enters.
U007 now gives \(u\in D(s)\).

### Necessity: Rationality Supplies the Domains and Commutation

Use U007 to write \(u=f^{-1}a\), with \(a,f\in C_{\mathrm{div}}(s)\) and \(f\) regular.
The literal composition \(f^{-1}\circ a\) is closed: if \(\xi_n\to\xi\) and \(f^{-1}a\xi_n\to\eta\), boundedness of \(a\) and closedness of \(f^{-1}\) give \(a\xi\in\operatorname{dom}(f^{-1})\) and \(f^{-1}a\xi=\eta\).
Since the affiliated product is its closure, it coincides with this literal composition.
Thus
\[
\operatorname{dom}(u)=\{\xi:a\xi\in f\mathcal H\}.
\]

Set
\[
W=\bigcap_{i=1}^d\bigl(\ker[r_i^*,f]\cap\ker[r_i,f]\bigr).
\]
This is cofinite by bounded Theorem 3.1 and Remark 3.10.
Choose an algebraic complement \(L\) of \(f\mathcal H\) in \(\mathcal H\), and put
\[
V_1=fW\oplus L.
\]
Injectivity of \(f\) implies that \(fW\) is cofinite inside \(f\mathcal H\); hence \(V_1\) is cofinite in \(\mathcal H\), with \(V_1\cap f\mathcal H=fW\).

Use the source's inverse-image choice
\[
V_2^i=(r_i^*)^{-1}(V_1).
\]
It is cofinite.
If \(\zeta\in V_2^i\cap r_i f\mathcal H\), then
\[
r_i^*\zeta\in V_1\cap f\mathcal H=fW,\qquad
\zeta=r_i r_i^*\zeta\in r_i fW=f r_iW\subset f\mathcal H.
\]
Here \(r_i^*r_i=I\) and commutation of \(r_i\) with \(f\) on \(W\) justify the steps.
No invariance of \(W\) under \(r_i\) is required.

Now take the finite-codimensional subspace
\[
V=a^{-1}(\Omega^\perp)\cap a^{-1}(V_1)
\cap\bigcap_i\ker[r_i^*,a]
\cap\bigcap_i(r_i r_i^*a)^{-1}(V_2^i).
\]
All inverse images are under bounded maps; the finite intersection remains cofinite.

For \(\xi\in V\cap\operatorname{dom}(u)\), write \(a\xi=f\eta\) with \(\eta\in W\), using \(a\xi\in V_1\).
Then
\[
ar_i^*\xi=r_i^*a\xi=r_i^*f\eta=fr_i^*\eta.
\]
It follows that \(\xi\in\operatorname{dom}(u r_i^*)\) and \(u r_i^*\xi=r_i^*\eta=r_i^*u\xi\) for every \(i\).

Conversely, if \(\xi\in V\cap\bigcap_i\operatorname{dom}(u r_i^*)\), then
\[
r_i^*a\xi=ar_i^*\xi\in f\mathcal H.
\]
Consequently \(r_i r_i^*a\xi\in V_2^i\cap r_i f\mathcal H\subset f\mathcal H\).
The vacuum exclusion in \(V\) is used exactly here:
\[
a\xi=(I-P_\Omega)a\xi=\sum_i r_i r_i^*a\xi\in f\mathcal H.
\]
This proves \(\xi\in\operatorname{dom}(u)\).
It restores the reverse domain inclusion rather than merely proving commutation on a smaller unspecified domain.

### False Optional Construction on p. 23

The source also proposes taking \(V_2^i\) as \(r_i fW\) plus a complementary subspace of \(f\mathcal H\).
That proposed space need not be cofinite in \(\mathcal H\).
For \(f=I\), \(W=\mathcal H\), and \(d\ge2\), the complement of \(f\mathcal H=\mathcal H\) is zero, so the proposed \(V_2^i\) is \(\operatorname{ran}r_i\).
Its orthogonal complement is infinite-dimensional: Fock words ending in a different letter provide infinitely many independent vectors.

This is a false auxiliary construction, not a counterexample to Proposition 4.12.
The alternative \(V_2^i=(r_i^*)^{-1}(V_1)\) printed in the same sentence is valid, as checked above, and proves the proposition without that optional construction.
In particular, the problematic option must not be copied into a later proof without correction.
This finding was verified against the rendered p. 23.

### Remark 4.13: Creation Operators

The remark says that the creation version admits the stronger individual equalities
\[
V\cap\operatorname{dom}(u)=V\cap\operatorname{dom}(u r_i),
\qquad ur_i=r_i u\text{ on }V\cap\operatorname{dom}(u),
\]
for each \(i\).
Its proof is only indicated in the source.
The following reconstructs the indicated modification.

Keep \(W,V_1\) from the necessity proof and choose
\[
V'=a^{-1}(V_1)\cap
\bigcap_i\ker[r_i,a]\cap
\bigcap_i(r_i a)^{-1}(V_1).
\]
For \(\xi\in V'\cap\operatorname{dom}(u)\), writing \(a\xi=f\eta\), \(\eta\in W\), gives \(ar_i\xi=fr_i\eta\) and the desired forward inclusion and commutation.
For a fixed \(i\), if \(\xi\in V'\cap\operatorname{dom}(u r_i)\), then
\[
r_i a\xi=ar_i\xi\in V_1\cap f\mathcal H=fW.
\]
Write \(r_i a\xi=f\eta\), \(\eta\in W\).
Applying \(r_i^*\) gives
\[
a\xi=r_i^*f\eta=fr_i^*\eta\in f\mathcal H,
\]
so \(\xi\in\operatorname{dom}(u)\).
This uses \(r_i^*r_i=I\) and supplies each individual domain equality; no vacuum exclusion is necessary for this version.

The converse criterion follows as in the sufficiency proof with \(r_i\): the creation defects \(fr_i b-ar_i g\) vanish on a cofinite inverse image and have finite rank.
The bounded identity in corrected Remark 4.4 then yields finite-rank annihilation defects and U007 applies.
This is a reconstruction of the source's stated variant, not a separately registered project theorem.

### Dependencies, Limits, and Verification Facts

Depends on U006-U007, the bounded commutator result of Theorem 3.1, the Fock identities, and elementary algebraic finite-codimension arguments.
The domain proof requires no closure of \(fW\), no assertion that \(V\) is closed, and no graph-norm extension of a commutation relation.
Strengthening the conclusion to a closed cofinite subspace, an everywhere-defined commutator, or a different topology would require another argument.

Both directions of Proposition 4.12 and the Remark 4.13 modification were reconstructed on 2026-09-08 using text and rendered pp. 22-24.
The inverse-image construction resolves the identified auxiliary error within the source's own proof options; no unresolved local domain implication was identified under the shared assumptions.
Outside proofs, errata, formalization, computations, and external human review were not checked.
This is the initial unit audit; future uses should retain the p. 23 correction and the exact domain convention.

### Independent Cross-Review of U006-U008

On 2026-09-08, the analytic reviewer, who did not author this file, checked the reconstruction against source text and rendered pp. 19-24.
The review checked regular-denominator cancellation using injectivity and dense range separately; the bounded-intersection step before regularization in Theorem 4.5; the absence of reliance on the optional free-field identification; closedness of the literal fraction composition; the valid inverse-image choice and the counterexample to the other choice on p. 23; and both directions of the creation-domain variant.
No unresolved local implication was identified under the stated finite-tracial and affiliation inputs.
The coordinating agent also checked the source formulas and domain reconstruction.

This review did not assume invariance of the cofinite kernel space, graph density, or bounded invertibility of regular denominators.
It did not independently establish the external affiliation infrastructure or perform formal verification.
The version/errata search is recorded separately in the [integrated audit](readme.md).

## Source and inspection

Source edition: Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here.

Passages: Proposition 4.12 and proof, pp. 22-23; Remark 4.13, p. 24.

Inspection: 2026-09-08: both directions of Proposition 4.12 and the creation-domain variant reconstructed with literal domains; the invalid optional p. 23 construction was checked and the source's valid inverse-image alternative retained. The joint U006-U008 review does not assume graph density, invariant cofinite kernels or boundedly invertible regular denominators. External foundations were not independently proved; no closed-cofinite strengthening or formal verification.

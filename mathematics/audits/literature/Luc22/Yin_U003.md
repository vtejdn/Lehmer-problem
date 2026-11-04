---
author: Yin
---

<a id="luc22-u003"></a>
# Luc22-U003: Conditional quotient approximation and its precise failures

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Luc22, [retained PDF](../../../literature/pdf/Luc22.pdf), arXiv:1901.00827v2, 16 September 2020.

Passages: Complete Section 7, pp.11--15, with the determinant and subgroup interfaces in Sections 3--5 and 14, and the separate Section 8 comparison.

Inspection: 2026-10-06T06:51, human record author Yin.
The assigned AI reviewer read the complete source and checked this section's proof implications, net quantifiers and kernel/determinant limits.
Rendered pp.13--14 were inspected.
A separately assigned AI reviewer independently found and checked the reversed separation implication and the weak/nonweak transfer failure, then exchanged findings.
Both had the source and task context; the primary reviewer's findings were sent while the second check was in progress.
This is a targeted additional AI check, not independent human inspection or a second complete audit.


## Assessment

**Audited within scope** for Theorems 7.3 and 7.5 as explicitly conditional implications, with the retained von Neumann kernel-dimension approximation input.
**Questioned as printed** for Theorem 7.8: its first hypothesis is tautological, and its conclusion has the exact counterexample below.
The proof mechanism works with the corrected separation hypothesis and its stated external sub-approximation input.
Example 7.6's claimed unrestricted positive gap is not justified by its displayed assumptions.

This unit does not prove the determinant Approximation Conjecture, the Determinant Conjecture for all groups, the Atiyah Conjecture for all groups, or classical Lehmer positivity.

<a id="luc22-determinant-approximation"></a>
## Approximation conjecture and conditional transfer

Conjecture 7.1 considers a decreasing directed family of normal subgroups $G_i\triangleleft G$ with intersection $\{e\}$, quotient $Q_i=G/G_i$, and the image $A_i$ of each finite matrix $A$ over $\mathbb ZG$.
Its asserted equality is

$$
\det_{\mathcal N(G)}r_A^{(2)}
=\lim_i\det_{\mathcal N(Q_i)}r_{A_i}^{(2)}.
$$

It uses the [kernel-removed determinant](Yin_U001.md#luc22-kernel-removed-determinant).
For example, $1-t$ over $\mathbb Z$ is injective with determinant $1$; over $C_n$ it has a kernel, but its nonzero singular-value product is $n$, and the group determinant is $n^{1/n}\to1$.
Replacing this determinant by the unmodified one makes every finite value zero and changes the conjecture.
This is the same convention boundary identified for [Den09](../Den09/Yin_U002.md).

Theorem 7.3 assumes this equality for $G$ and the Determinant Conjecture for each $Q_i$.
It concludes

$$
\Lambda(G)\ge\limsup_i\Lambda(Q_i),\qquad
\Lambda_1(G)\ge\limsup_i\Lambda_1(Q_i).
$$

For a fixed admissible $A$, its limiting determinant is greater than $1$, so all sufficiently late quotient determinants are greater than $1$.
Each therefore bounds the corresponding quotient infimum from above.
Taking $\limsup$ and then the infimum over $A$ proves the assertion.
The same argument works for nets; it does not need a minimum to be attained.

For the weak constants an additional assumption is needed.
For each fixed matrix $A$, require an eventual positive gap $\beta(A)$ for nonzero dimensions of $\ker r_{A_i}^{(2)}$.
For $\Lambda_1^w$ only scalar matrices need this condition.
The source invokes [26, Theorem 13.19(2)] to obtain

$$
\dim_{\mathcal N(G)}\ker r_A^{(2)}
=\lim_i\dim_{\mathcal N(Q_i)}\ker r_{A_i}^{(2)}.
$$

The quotient-group subscript is essential.
If $r_A^{(2)}$ is injective, the left side is zero, and convergence together with the positive gap forces all sufficiently late quotient kernels to vanish.
Those square maps are then weak isomorphisms.
Applying the preceding determinant argument yields

$$
\Lambda^w(G)\ge\limsup_i\Lambda^w(Q_i),\qquad
\Lambda_1^w(G)\ge\limsup_i\Lambda_1^w(Q_i).
$$

The kernel-dimension approximation theorem is a retained, explicitly cited external interface; its original proof in [26] was not re-audited.
The source's assertion of its applicability uses the separating normal family, integral coefficients, uniform support norm bound and determinant condition on the quotients.
No injectivity is inferred merely from determinant positivity in the reduced convention.

Remark 7.4 supplies the gap if the quotients satisfy the strong Atiyah integrality assertion and there is a **single** integer $D$ divisible by the orders of every finite subgroup of every quotient: dimensions then lie in $D^{-1}\mathbb Z$, so $\beta=1/D$.
Separate bounds depending on $i$ would not suffice.
In Theorem 7.5 the quotients are torsionfree elementary amenable, so the cited Atiyah and determinant results supply $D=1$.
The theorem remains conditional on determinant approximation for $G$.
Its printed $Q_i,I$ are the sequence quotients $G/G_n$ and the natural-number index inherited from its hypotheses.

## The corrected sub-approximation mechanism

Theorem 7.8 allows arbitrary homomorphisms $q_i:G\to Q_i$ indexed by a directed set, without assuming quotient maps or a compatible inverse system.
Its necessary separation condition is

$$
\forall F\subset G\text{ finite}\ \exists i_0\
\forall i\ge i_0\ \forall f\in F:
\quad f\ne e\ \Longrightarrow\ q_i(f)\ne e.
$$

With this condition and the Determinant Conjecture for every $Q_i$, its intended conclusion is

$$
\det_{\mathcal N(G)}r_A^{(2)}
\ge\limsup_i\det_{\mathcal N(Q_i)}r_{A_i}^{(2)}
\quad(A\in M_{r,s}(\mathbb ZG)).
$$

The printed proof first replaces $A$ by $AA^*$ and uses the square-root identity, reducing to positive square operators.
Coefficient $\ell^1$ norms do not increase under homomorphisms, giving one uniform operator norm bound.
For every real polynomial $p$, the diagonal entries of $p(A)$ have finite support.
Correct separation prevents nonidentity coefficients in that support from contributing to the identity coefficient of $p(A_i)$.
Consequently the matrix traces eventually agree:

$$
\tau_G(p(A))=\tau_{Q_i}(p(A_i)).
$$

The source then invokes the logarithmic determinant upper-semicontinuity inequality at the end of [26, proof of Theorem 13.19, p.465].
This precise external inequality, together with the uniform norm and trace checks, is the retained analytic input; this audit has not independently read its original proof.
The corrected argument therefore verifies the in-paper dependency match, not a new proof of that external approximation result.

The determinant inequality alone gives no Lehmer gap transfer: determinants strictly greater than one on $G$ might have quotient determinants all equal to one.
Remark 7.9 correctly identifies extra conditions that would suffice.
Eventual quotient determinants greater than one give the corresponding $\limsup$ bound for $\Lambda$ or $\Lambda_1$.
Alternatively, a uniform eventual quotient gap $\lambda>1$, together with the implication $\limsup_i\det(A_i)=1\Rightarrow\det(A)=1$, gives a gap $\lambda$ on $G$.
Its argument uses the non-strict inequality $\det(A_i)\ge\Lambda(Q_i)$; the source's strict version need not hold when an infimum is attained.
These extra properties are assumptions, not consequences established by sub-approximation.

## Actionable findings

<a id="luc22-reversed-separation"></a>
### F10 — P1: Theorem 7.8 is false with its printed hypothesis

**Location:** p.14, first bullet of Theorem 7.8 and the repeated implication in the proof's last paragraph.
**Status:** newly recorded defect in existing v2.

The source prints $q_i(f)\ne e\Rightarrow f\ne e$, which is automatic for every group homomorphism.
It gives no control of elements collapsed to the identity and cannot imply trace convergence.

Take $G=\mathbb Z=\langle t\rangle$, every $Q_i=\{1\}$, all $q_i$ trivial, and $A=1+t$.
The directed system may be constant and satisfies every printed hypothesis; the trivial group satisfies the Determinant Conjecture.
But

$$
\det_{\mathcal N(\mathbb Z)}r_{1+t}=M(1+z)=1,
\qquad
\det_{\mathcal N(\{1\})}(2)=2,
$$

so its asserted $1\ge2$ is false.
This counterexample uses the source's own kernel-removed convention, and both displayed operators are injective.

**Repair:** reverse the implication in both places, as stated above.
In the last trace-limit display also restore $p$ on the right: $\lim_i\tau_{Q_i}(p(A_i))$, not $\lim_i\tau_{Q_i}(A_i)$.
Consumers must use the corrected hypothesis before invoking Theorem 7.8.
The later abelian specialization theorem has its own argument and is not invalidated by this typographical reversal.

<a id="luc22-weak-transfer-gap"></a>
### F11 — P2: Example 7.6 claims an unsupported unrestricted gap

**Location:** p.13, concluding paragraph of Example 7.6.
**Status:** newly recorded inference gap in existing v2.

The source passes from a virtually residually torsionfree nilpotent three-manifold group and the assumption $\Lambda^w(H)=\Lambda(\mathbb Z)$ for torsionfree nilpotent $H$ to $\Lambda(\pi)>1$.
Two steps are missing: the assumptions do not explicitly supply a positive gap $\Lambda(\mathbb Z)>1$, and Theorem 7.5 with the finite-index inequality controls **$\Lambda^w$**, not $\Lambda$.
Since $\Lambda\le\Lambda^w$, a lower bound on $\Lambda^w$ cannot be transferred downwards to $\Lambda$.

A valid conditional conclusion is the following: if a subgroup $\pi'\le\pi$ of index $n$ has a separating torsionfree nilpotent quotient chain, satisfies the needed approximation equality along that chain, and its quotient weak constants are eventually bounded below by some $\lambda>1$, then

$$
\Lambda^w(\pi')\ge\lambda,\qquad
\Lambda^w(\pi)\ge\lambda^{1/n}>1.
$$

To claim a lower bound for $\Lambda(\pi)$ instead, require the corresponding unrestricted quotient bounds and use Theorem 7.3(1).
The original phrase “any torsionfree nilpotent group” also includes the trivial group unless qualified; $\Lambda^w(\{1\})=2$ while $\Lambda(\mathbb Z)\le M(L)<2$, so that literal universal equality cannot serve as a realizable hypothesis.
Discarding initial trivial quotients does not fix the independent weak/unrestricted and positivity issues.

This finding concerns the attempted consequence, not the cited theorem that the relevant three-manifold groups are virtually residually torsionfree nilpotent.
That structural theorem is reported from [1, p.84]; its proof was not independently checked here.

### F12 — P3: Repair quotient labels and nearby references

In Theorem 7.3's proof, p.12, dimensions of quotient kernels have subscript $\mathcal N(Q_i)$, not $\mathcal N(G)$.
In Remark 7.9, p.15, the theorem with general homomorphisms and no determinant-approximation hypothesis is Theorem 7.8, not the repeated Theorem 7.3.
Replace the strict candidate comparison by $\ge$.
These errors do not replace the substantive additional assumptions described above.

## Review and remaining limits

The exact counterexample, correction direction, eventual-injectivity argument, finite-index power and weak/unrestricted distinction were checked directly; the separately assigned review independently confirmed F10 and the two substantive failures in F11.
Source claims about known cases of the approximation conjecture and complex-coefficient counterexamples are read as version-specific cited reports.
No exhaustive literature update, formalization, proof of a conjecture, or independent audit of [26]'s analytic approximation proof is claimed.
The abelian iterated-limit result and its different hypotheses are recorded in [Luc22-U002](Yin_U002.md#luc22-abelian-matrix-approximation).

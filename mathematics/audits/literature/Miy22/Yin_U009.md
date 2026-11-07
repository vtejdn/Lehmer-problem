---
author: Yin
---

<a id="miy22-u009"></a>
# Miy22-U009: Kronecker's Theorem and the One-Normal-Generator Criterion

- Source: [Miy22](../../../literature/pdf/Miy22.pdf), Section 2.3, printed/PDF pp. 7-8, especially Theorem 2.8; references [11] and [16] on p. 24.
- Date and authorization: 2026-09-09, the user requested the audit status and a comparison with the earlier one-normal-generator argument.
- Previous boundary: [U002](Yin_U002.md#miy22-u002) checked the theorem's statement, bounded-operator hypothesis and pole conventions, and independently proved the downstream decay consequence.
  It explicitly did not audit the complete original Kronecker or Partington proof.
  The original Miy22 source audit completion record retains that historical boundary.
- New scope: a complete local proof of the exact Theorem 2.8 statement, including the rank/pole equality, together with a proof-level comparison.
  The coordinating agent and the classical-proof reviewing agent independently reconstructed the state-space argument.
  The comparison reviewing agent independently checked the Haar block identities and the earlier one-normal-generator argument rank refinement.
  Exact final reviews are recorded below; no complete audit of either cited original or any book is claimed.

## Exact Statement and Conventions

For a complex sequence \((\alpha_n)_{n\ge0}\), let its formal Laurent series be

\[
a(z)=\sum_{n\ge0}\alpha_n z^{-n-1}.
\]

Then a is a rational function all of whose poles lie in the open unit disk if and only if the matrix \(H=(\alpha_{m+n})_{m,n\ge0}\) defines a bounded finite-rank operator on \(\ell^2(\mathbb N_0)\).
For nonzero a, write a=p/q in lowest terms.
The Laurent convention requires a(infinity)=0, so deg p<deg q, and

\[
\operatorname{rank}H=\deg q
=\text{total finite pole multiplicity of }a.
\]

Poles at zero and repeated poles are included.
For a=0 the Hankel operator has rank zero.
This is an ordinary complex operator rank, not tracial rank.
We describe H by its columns to avoid inner-product conjugation conventions.
A formal matrix of finite algebraic rank need not define a bounded operator on this Hilbert space.

The local p. 8 render confirms the source's Laurent indexing.
Its phrase "number of poles on f" refers to a and is interpreted with multiplicity after cancellation.
The test a(z)=z^{-m}, whose Hankel matrix is an m-by-m reversed identity block and zero elsewhere, verifies that zero must count as a pole of order m.

## Complete Local Proof

### Finite Hankel Rank Gives a Minimal Finite Representation

Suppose H is bounded of finite rank r>0.
Let c_j=H e_j and

\[
V=\operatorname{span}\{c_j:j\ge0\}=\operatorname{Ran}H.
\]

The equality holds because the image of finitely supported vectors is dense in Ran H and the latter has finite dimension.
The backward shift satisfies S*c_j=c_{j+1}.
Hence V is invariant, and we may define

\[
T=S^*|_V,\qquad b=c_0,\qquad \ell(v)=v_0.
\]

Then \(\alpha_n=\ell T^n b\), and as a formal expansion at infinity,

\[
a(z)=\ell(zI_V-T)^{-1}b.
\tag{1}
\]

This is a strictly proper rational function.
Every state is a linear combination of T^j b by construction.
Also, if \(\ell T^n v=0\) for all n, then v_n=0 for all n, so v=0.
These are respectively reachability and observability; both are explicit facts about the column space, not imported minimal-realization assumptions.

### The Hilbert-Space Condition Locates the Poles

If Tv=lambda v with v nonzero, then S*v=lambda v, so v_n=lambda^n v_0.
Necessarily v_0 is nonzero, and square summability implies |lambda|<1.
Thus every eigenvalue of T lies in the open disk.
Formula (1) shows that every pole of a is an eigenvalue of T, so every pole lies there as well.
No bound at the exact maximal eigenvalue modulus is asserted.

### No Cancellation Can Lower the Denominator Degree Below the Rank

Let a=p/q be reduced, with q of degree s.
The determinant denominator in (1) gives s<=r.
Write \(q(z)=\sum_{j=0}^{s}q_j z^j\), q_s nonzero.
Since qa=p has no negative powers, coefficient comparison gives the exact recurrence

\[
\sum_{j=0}^{s}q_j\alpha_{n+j}=0\qquad(n\ge0).
\]

Therefore \(\ell T^n q(T)b=0\) for all n.
Observability gives q(T)b=0.
Its leading coefficient is nonzero, so all T^j b with j>=s are linear combinations of b,Tb,...,T^{s-1}b.
Reachability now gives r<=s.
Hence s=r.
This proves exact rank and pole multiplicity, including a nilpotent state corresponding to a pole at zero.
If H=0, all alpha_n vanish and the zero case is immediate.

### Rationality with Interior Poles Gives a Bounded Finite-Rank Hankel Operator

Conversely, suppose a=p/q is nonzero, reduced and strictly proper, and all its poles lie in |z|<1.
Choose rho with 0<rho<1 strictly larger than every pole modulus.
Cauchy's Laurent coefficient formula on |z|=rho gives

\[
\alpha_n=\frac{1}{2\pi i}\int_{|z|=\rho}a(z)z^n\,dz,
\qquad |\alpha_n|\le C\rho^n.
\]

Consequently

\[
\sum_{m,n\ge0}|\alpha_{m+n}|^2
=\sum_{k\ge0}(k+1)|\alpha_k|^2<\infty.
\]

Thus the matrix defines a Hilbert-Schmidt, hence bounded, operator.
The same denominator recurrence expresses every column after the first s=deg q columns as a fixed linear combination of earlier columns, so the operator has finite rank at most s.
The already proved forward direction then gives equality with deg q.
This completes both implications and the exact rank formula.

This proof also explains U002's repeated-pole repair: one chooses a radius strictly beyond the largest pole modulus.
The stronger printed rate at the pole modulus itself fails for \(\alpha_n=(n+1)t^n\), 0<t<1.
Neither the theorem nor Corollary 2.9 fails.

## Historical one-normal-generator comparison: the same finite-dimensional mechanism

The original fixed proof is [original C_F0004](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/claims/Yin_C_F0004_v1.md#proof), including its [exact-rank refinement](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/claims/Yin_C_F0004_v1.md#exact-rank-refinement-and-the-kronecker-comparison).
The exact original findings are retained in [original R_F0003](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/audits/reviews/Yin_R_F0003_v1.md).
These are source-only locators in experimental-math-ai at fixed commit `f1ab0a38da990d7e62f5f79acff1dd2312149ca9`, checked against its local Git tree; remote access is unconfirmed.
The original one-generator finding has unknown initial-context relationship, while the 2026-09-09 exact-rank refinement finding is self-reviewed under that record's explicit relationships.
Current C_F0004 is an affine-capacity theorem and supplies neither this proof nor those findings.
The comparison below preserves its actual mathematical mechanism and 2026-09-09 review limits; no local Claim receipt, new adoption or retrospective independent review follows.

Under the earlier one-normal-generator argument, the normal spectral representation is \(M=L^\infty(S,\mu)\), X is multiplication by z, and \([D,X]=P_\Omega\) makes mu nonatomic.
For bounded f and finite-rank T_f=[D,f], scalar commutation gives

\[
[T_f,X]=[P_\Omega,f],\qquad
K_f(z,w)=\frac{f(z)-f(w)}{z-w}
\quad\text{almost everywhere}.
\]

The authoritative proof and its domain checks remain at the located original C_F0004 proof above.
The mechanisms compare as follows:

| Step | Kronecker / Miy22 Theorem 2.8 | the earlier one-normal-generator argument, one normal generator |
| --- | --- | --- |
| Column family | Tails \((\alpha_{n+j})_{n\ge0}\) | Divided differences \((f(z)-f(w))/(z-w)\) indexed by w |
| Finite-rank consequence | A finite backward-shift invariant state space | A finite-dimensional span of almost-everywhere defined difference columns |
| Algebraic extraction | A constant-coefficient recurrence, or \(\ell(zI-T)^{-1}b\) | Linear dependence at distinct w_i, followed by a common denominator, gives Bf=A |
| Analytic step | Square-summable shift eigenvectors force poles into the open disk | Essential boundedness and full support exclude genuine poles on S |
| Exact complexity | Rank equals the denominator degree of a strictly proper function | Rank equals max(deg p,deg q) of a reduced nonconstant function |
| Hypotheses supplying structure | A bounded Hankel operator on the standard sequence space | A bounded normal generator and a bounded dual on the tracial spectral space |

The pole statements are compatible.
In the earlier one-normal-generator argument a polynomial part is allowed, so total pole multiplicity is counted on the Riemann sphere, including infinity.
The rank-degree equality was added to the earlier one-normal-generator argument with a separate proof and review during this comparison.
It is not justified merely by an analogy with Kronecker's theorem.

For arbitrary compact spectral support and measure, the difference kernel need not be a Hankel matrix in an orthonormal monomial basis.
The monomials may not be total, much less orthonormal.
Therefore the earlier general one-normal-generator proof is not a direct application of the sequence-space theorem; it is a direct divided-difference argument with a measure-specific final pole exclusion.
No classification of measures admitting a bounded dual, and no novelty claim for this criterion, is made here.

## Two Precise Bridges

### Formal Coefficient Identity

Define \(F(z)=a(z^{-1})=\sum_{n\ge0}\alpha_n z^{n+1}\).
Then the formal two-variable identity is

\[
\frac{F(z)-F(w)}{z-w}
=\sum_{m,n\ge0}\alpha_{m+n}z^m w^n.
\tag{2}
\]

It follows by expanding each \((z^{k+1}-w^{k+1})/(z-w)\).
Thus the Hankel matrix is exactly the coefficient matrix of a divided difference, with this one-power shift.
Equation (2) is an algebraic identity; by itself it does not identify the Hilbert-space norms for an arbitrary spectral measure.

If instead one wants \(g(w)=\sum\alpha_n w^n\), the precise transformation is \(g(w)=w^{-1}a(w^{-1})\), with a removable value at zero.
The compressed change-of-variable wording immediately before Corollary 2.9 must not be used to shift these coefficients incorrectly.
The explicit identity avoids any ambiguity; a=1/z corresponds to F(z)=z and a rank-one difference kernel, whereas g=1 has zero ordinary divided difference.

### The Haar Model: Two Actual Hankel Blocks

On \(L^2(\mathbb T,m)\), let U=M_z, e_k=z^k for k in Z, and

\[
D e_k=\begin{cases}e_{k-1},&k\ge1,\\0,&k\le0.\end{cases}
\]

Then D is bounded and [D,U]=P_1.
For any f in L-infinity(T), write its L2 Fourier expansion \(f=\sum_{k\in\mathbb Z}\beta_k z^k\).
Direct coefficient calculation gives

\[
[D,M_f]e_{-m}
=\sum_{n\ge0}\beta_{m+n+1}e_n,
\qquad
[D,M_f]e_{m+1}
=-\sum_{n\ge0}\beta_{-m-n-1}e_{-n-1},
\quad m\ge0.
\tag{3}
\]

The domain spaces spanned by e_{-m} and e_{m+1} are orthogonal complements, as are the two displayed range spaces.
Hence the commutator has exactly the two Hankel blocks H_+ and -H_-, with coefficients \(\alpha_n^+=\beta_{n+1}\) and \(\alpha_n^-=\beta_{-n-1}\), and its rank is the sum of their ranks.
Both blocks are bounded as compressions of a bounded commutator.
There is no assumption that the separate Hardy projections of f are bounded multipliers.

If this rank is finite, apply Theorem 2.8 twice to obtain strictly proper rational functions a_+ and a_- with poles in the open disk.
Fourier uniqueness gives

\[
f(z)=\beta_0+a_+(z^{-1})+a_-(z)
\quad\text{almost everywhere on }\mathbb T.
\]

The right side is rational and has no pole on the unit circle, hence supplies a bounded scalar rational expression in U.
This proves the complete Haar instance of the earlier one-normal-generator reverse implication directly from Kronecker.
For any other bounded dual D', D'-D commutes with U, hence with U^{-1}=U* and W*(U); thus the commutators agree for all f.
The argument therefore retains the earlier one-normal-generator argument's quantifier over dual systems.

## External Source Search and Verification Boundary

The 2026-09-09 search was triggered by the explicit proof-comparison request and U002's declared imported-theorem boundary.
Searches used Partington's book title, Theorem 3.11, and Kronecker / finite Hankel rank / shift invariant proof.
The publisher's Partington chapter metadata was accessible, but the theorem and original proof were not.
Kronecker's 1881 original was not read.
These original-proof limits remain unchanged.

Later access update, 2026-09-09: the user supplied [Par88.pdf](../../../literature/pdf/Par88.pdf) for future reference.
Its lightweight intake confirms first publication in 1988 and locates Theorem 3.11 at printed p. 37 / PDF p. 45.
The book is now locally accessible; only the earlier search was access-limited.
Intake alone did not change this unit's reconstructed proof or mathematical assessment.
Subsequent strategy work directly audited Partington's proof in [Par88-U001](../Par88/Yin_U001.md#par88-u001), preserving the earlier review's historical scope and supplying the minimal-recurrence qualifications.

A modern primary treatment, [MAR07, Section 4.2](https://indico.math.cnrs.fr/category/609/attachments/3715/5144/Martinez-Rosenthal.pdf), Theorem 4.2.3 and its complete proof, printed pp. 138-140, and Corollary 4.2.4 with proof, p. 141, was read by the classical-proof reviewing agent.
It uses column relations, recurrences, rationality and the first column's Hardy-space membership.
Its symbol convention has one different Laurent power, so no exact pole-count formula is transferred without conversion.
Parsed primary text was inspected; external screenshot retrieval failed.
The complete proof above independently settles the exact Miy22 indexing and pole multiplicity, without an unreviewed original proof as a premise.

The coordinating agent read Miy22 pp. 6-8 and 24 and visually inspected p. 8.
The finite-state realization, recurrence, coefficient integral, Hilbert-Schmidt sum, zero-pole test, difference identity and Haar blocks were checked mathematically.
No numerical experiment, proof assistant, external human review, exhaustive historical search or novelty claim is asserted.

## Independent Review

The final written reviews follow.
The initial Miy22 source audit is not retrospectively described as having included this later proof reconstruction.

Comparison review, 2026-09-09, the comparison reviewing agent: independently checked the comparison and both bridge sections in the pre-review unit.
The one-power formal shift, the two Fourier blocks and signs, the orthogonal rank sum, and reconstruction by Fourier uniqueness are correct.
Bounded Hardy components are conclusions after Kronecker, not assumed before applying it.
The difference between arbitrary duals commutes with the entire Haar-generated algebra.
The exact-rank refinement of the earlier one-normal-generator argument has its own proof audit; it does not depend on this unit's classical theorem.
This review covers the comparison sections, complementing the complete classical-proof review below.

2026-09-09, independent review by the classical-proof reviewing agent: the complete written Theorem 2.8 reconstruction passes.
The span of the columns is a subspace of the finite-dimensional range, hence already closed; density from finitely supported inputs therefore gives the asserted equality with the range.
Restriction of the backward shift preserves that space, and coordinate evaluation proves both reachability and observability directly.
Comparing the coefficient of z^{-n-1} in qa gives the recurrence for every n>=0, without a missing initial segment.
Applying observability to q(T)b and then reachability proves the denominator lower bound, while the adjugate formula supplies the upper bound.
Thus cancellation, including at zero, cannot invalidate the exact rank statement.

The eigenvector recurrence has a nonzero zeroth coordinate and excludes eigenvalues on as well as outside the unit circle.
The Laurent integral is taken in the annulus outside every pole; its estimate has constant C=rho times the maximum modulus of a on the integration circle.
The resulting sum with weight k+1 proves Hilbert-Schmidt boundedness.
The denominator recurrence places every column in the finite closed span of the first deg q columns, so bounded extension introduces no additional range vectors.
The reversed-identity example correctly has rank m and a pole of order m at zero.
The geometric-decay radius is strictly larger than all pole moduli, preserving the repeated-pole correction.

The formal divided-difference identity and its one-power shift were independently recomputed; the two Haar coefficient formulas also match direct word/Fourier action.
The general spectral-measure comparison makes no orthonormal-monomial assumption and does not use the sequence theorem as a substitute for the earlier one-normal-generator argument's separate proof.
The stated source limits agree with the actual inspection: Miy22's exact local statement and the modern MAR07 passages were read, while the original Kronecker and Partington proofs remain unreviewed.
No substantive correction to this written proof was required.
This review is mathematical and source-scoped; it is not a numerical or proof-assistant verification.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here.

Passages: Theorem 2.8 in Section 2.3, pp. 7-8; references [11] and [16], p. 24. User-requested comparison and follow-up dated 2026-09-09.

Inspection: 2026-09-09: a complete local Kronecker reconstruction and the Haar/comparison calculations received distinct independent reviews. MAR07 Section 4.2, Theorem 4.2.3 and Corollary 4.2.4 proofs were read in primary parsed text; external screenshot retrieval failed. The historical review did not inspect original Kronecker or Partington proofs; later Par88 acquisition and separate proof audit retain their own dates. No exhaustive historical search, numerical experiment or formal verification.

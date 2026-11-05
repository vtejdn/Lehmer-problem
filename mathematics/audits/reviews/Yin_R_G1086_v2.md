---
author: Yin
---

# Independent whole review of the actual Salem radial-hull boundary

Review act: 2026-11-04T21:27 UTC.
The human record author is Yin.
This is a separately organized independent agent review of the entire [C855 v3 statement](../../claims/Yin_C_G0855_v3.md#statement), A--D, and its [complete argument](../../claims/Yin_C_G0855_v3.md#argument), SH1--SH10.
The reviewer had no role in substantive proof development and received no proof-generation dialogue, contributor explanation, mathematical development summary, temporary candidate or generation notes.
The fixed candidate and necessary fixed inputs were read directly; its provenance paragraphs supplied no evidence for correctness.
The obligations and initial mathematical findings were formed before consulting the earlier [R1086 v1 finding](Yin_R_G1086_v1.md#raw-p2-whole).
No rolling Draft was consulted and no substantive repair was supplied.
C855 v3 had no selected assessment during this review.

## Retained evidence and review scope

The [raw p=2 whole finding in R1086 v1](Yin_R_G1086_v1.md#raw-p2-whole) remains at its exact C855 v2 A--D/SC1--SC23 scope, with its original relationship, bindings, source limits and review time.
It was read after the present initial findings to check the retained capacity interfaces and the distinction between its conclusion and the new geometric boundary.
The present finding does not replace or repeat that entire earlier proof review.
[C855 v1](../../claims/Yin_C_G0855_v1.md#statement) remains unassessed and is neither a proof premise nor an independently reviewed result of this finding.
No C assessment, navigation or Task decision is changed by this record.

The new obligations are the finite Green comparison on the actual Salem hull, degree preservation for the original squared polynomial, quantitative angular-mesh control with every original root charged, the exact accepted arithmetic lower bound, and uniformity in degree, disk radius and rotation collections.
The final scope check compares this capacity statement with the direction of C855 v2's Hankel estimate and the unrestricted [G0001 objective](../../tasks/Yin_T_G0001_v1.md#contract).
The inspected erratum contained no current objection affecting these inputs.

<a id="salem-radial-hull-whole"></a>
## Whole Salem radial-hull finding

**Finding:** no unresolved mathematical gap was found in the whole C855 v3 statement A--D and argument SH1--SH10 under their exact hypotheses and accepted-source limits.
The proof gives the finite capacity bounds, the explicit degree-dependent mesh bound, a uniform eventual lower cost of \(m^2\) for every nonempty finite rotation collection, and the coefficient-four asymptotic for unrotated or singly rotated hulls on a hypothetical Salem near-one sequence.
The finding supplies no existence of such a sequence, no lower bound for actual Hankel determinants, and no resolution of the Salem minimum or unrestricted Mahler gap.
It makes no novelty, optimal-constant, numerical-threshold or formal-verification claim.

### Actual roots, topology and finite Green comparison: SH1--SH3

For an actual Salem number the unique conjugate of modulus greater than one is the positive real \(\lambda=e^m\); its inverse is the sole contracting conjugate and all others have modulus one.
The fourth power therefore supplies the full segment \([0,e^{4m}]\) in \(H\), and every other segment endpoint lies in the closed unit disk or on that same real segment.
This proves \(H\subseteq K_t\subseteq K_*\) for every \(t\ge0\), without deleting neutral or contracting endpoints.

The finite radial tree is a nonpolar connected compact set with connected exterior, simply connected on the sphere.
At every boundary point a nondegenerate segment in the tree supplies the usual explicit segment barrier, so the Green function tends continuously to zero there.
The comparison with a contained segment uses the bounded harmonic difference on the exterior, with infinity a removable interior point, rather than an assumed sign of the capacity difference at infinity.
The same principle applies to the disk with its attached slit.

Every point of the unit circle is within angular distance \(\Delta/2\) of a point of \(B\), and its Euclidean distance \(\delta\) to that point is at most \(\Delta/2\).
After rotation, the chosen endpoint becomes one and the exterior map of \([0,1]\) is the stated branch of \(2w-1+2\sqrt{w(w-1)}\), with leading coefficient four.
For \(|w|=1\), its modulus is at most \(1+2\delta+2\sqrt\delta\), so the logarithm is at most \(2\delta+2\sqrt\delta\).
When \(\Delta\le1\), this is at most \((1+\sqrt2)\sqrt\Delta\le4\sqrt\Delta\).
The same bound holds at the endpoints by continuity, establishing SH3 on the whole circle.

On the external slit of \(K_*\), \(g_H=0\) because that entire segment is already in \(H\).
On the circular part of the boundary, \(0\le g_H\le4\sqrt\Delta\), whereas \(g_{K_*}=0\).
The bounded harmonic difference \(g_H-g_{K_*}\) therefore has values between these constants throughout the exterior, including infinity.
Its value there is \(\log\operatorname{cap}K_*-\log\operatorname{cap}H\), with exactly the sign used in SH2.

The single-slit formula was checked directly in [C855 v2](../../claims/Yin_C_G0855_v2.md#a-disk-and-one-radial-slit): \(z+z^{-1}\) maps the relevant exterior onto the complement of an interval of length \(2+e^v+e^{-v}\), with leading coefficient one.
The interval-capacity normalization then gives \(\operatorname{cap}K(1,v,0)=\cosh^2(v/2)\).
For \(v=4m\), this is exactly \(\operatorname{cap}K_*=\cosh^2(2m)\).
Together with monotonicity, the comparison proves the complete finite sandwich SH2 uniformly in \(t\).
No unquantified Hausdorff-continuity theorem or limit in the disk radius is required.

### Original squared degree, the Lipschitz test and the finite guard: SH4--SH5

If two distinct Salem conjugates had a root-of-unity quotient, a Galois automorphism taking the numerator to \(\lambda\) would take the denominator to a distinct conjugate also of modulus \(\lambda\).
This contradicts uniqueness of the expanding conjugate.
Consequently distinct original conjugates have distinct positive powers, so every positive power has degree \(d\), and \(Q(z)=\prod_i(z-\alpha_i^2)\) is a monic integer polynomial of degree \(d\) with simple roots.
Its two off-circle roots are precisely \(\lambda^2,\lambda^{-2}\), and its ordinary Mahler measure is \(e^{2m}\).
The argument uses actual original degree and total measure, with no hidden powered-field multiplicity.

The midpoint of a largest empty neutral arc is at circular distance at least \(\Delta/2\) from each neutral root.
Since \(0<\Delta\le2\pi\), the corresponding chord distance is at least \(2\sin(\Delta/4)\ge\Delta/\pi\).
For \(r=\min\{1/4,\Delta/(4\pi)\}\), every neutral squared root thus lies outside the support of \(\varphi(z)=(r-|z-\zeta|)_+\).
This real function is globally one-Lipschitz, has support in \(|z|\le5/4\), and is bounded above by \(r\).
The two off-circle roots contribute at most \(2r/d\) to the complete normalized root sum; they are charged rather than silently discarded.
On the circle arc of angular distance at most \(r/2\) from \(\zeta\), chord distance is at most \(r/2\), so \(\varphi\ge r/2\) on an arc of total angular length \(r\).
Its normalized circle integral is therefore at least \(r^2/(4\pi)\).

The [canonical Pri11 U001 interface](../literature/Pri11/Yin_U001.md#pri11-u001) requires an integer polynomial with simple zeros and degree at least 55, with a real globally Lipschitz test of bounded support.
All hypotheses hold for this \(Q\) and \(\varphi\).
Because \(m\le1\), \(M(Q)\le e^2<55\le d\), and the theorem's logarithm is exactly \(\log d\).
The support constant is \(2R+1=7/2\), so its absolute discrepancy estimate yields precisely

\[
 \frac{r^2}{4\pi}\le\frac{2r}{d}
                  +\frac72\sqrt{\frac{\log d}{d}}.
\]

Multiplication by \(4\pi\) and \(r^2\le ar+b\Rightarrow r\le a+\sqrt b\) give the stated \(\rho_d\), including both numerical constants.
The function \(\log d/d\) decreases for real \(d>e\); hence \(\rho_d\) decreases on \(d\ge55\) and tends to zero.
Thus \(D_0\) exists as a finite integer without an asserted numerical evaluation.
For \(d\ge D_0\), \(r\le\rho_d\le1/(4\pi)<1/4\), so the capped branch \(r=1/4\) is impossible, including at the threshold equality.
It follows that \(r=\Delta/(4\pi)\) and \(\Delta\le4\pi\rho_d\le1\), supplying the finite guard needed for SH2--SH3.

### Arithmetic conversion and uniform limits: SH6--SH7

The exact input in [C147 v5's source scope](../../claims/Yin_C_G0147_v5.md#reuse-and-source-scope) is the accepted Smy08 numerical statement \(M(P)>1+(1/1200)(\log\log d/\log d)^3\), on the nontorsion algebraic-integer domain.
An actual Salem minimal polynomial lies in that domain, and \(m=\log M(P)\) is its total logarithmic measure.
For \(d\ge55\), the added term lies in \((0,1]\), and \(\log(1+x)\ge x/2\) gives SH6 with constant \(1/2400\).
No division by \(d\) is appropriate in this conversion, and no cyclic-norm conclusion of C147 is used as an angular input.

SH5 gives \(\sqrt\Delta=O(d^{-1/2}+(\log d/d)^{1/8})\), with absolute constants.
SH6 bounds \(m^{-2}\) by \(2400^2(\log d/\log\log d)^6\).
Their product tends to zero because the displayed negative powers of \(d\) dominate these logarithmic factors.
The same lower bound gives \(dm\ge(d/2400)(\log\log d/\log d)^3\longrightarrow\infty\).
Both comparisons depend only on the actual degree, so SH7 is uniform over all actual Salem inputs satisfying \(0<m\le1\), rather than just over one chosen sequence.

### Radius, rotations, sequences and the determinant boundary: SH8--SH10

For a hypothetical sequence with \(m_j\to0\), the expansion \(2\log\cosh(2m_j)=4m_j^2+O(m_j^4)\) and the two sides of SH2 bound the absolute normalized error by \(O(m_j^2)+4\sqrt{\Delta_j}/m_j^2\).
This bound is independent of \(t\) and tends to zero by SH7, proving the supremum statement SH8 without interchanging an uncontrolled radius limit and a degree limit.
Bounded degree and \(M(P)\le e\) bound every integral coefficient by \(\binom d k M(P)\), leaving finitely many possibilities; hence \(m_j\to0\) would itself force degree divergence.
Neither that implication nor the conditional asymptotic constructs a Salem near-one sequence.

A single rotation preserves capacity exactly and preserves the centered disk, so the same coefficient-four asymptotic applies.
Every nonempty finite collection of rotations contains a single rotated copy of \(H\), giving SH9 by capacity monotonicity.
This lower bound is independent of the number of rotations and their angles, including choices varying with the input.
No upper coefficient-four asymptotic for multiple rotations is inferred, and no upper inclusion in a single rotated \(K_*\) is needed for those collections.

For \(0<m\le1\), the displayed elementary inequalities give

\[
 2\log\cosh(2m)\ge\frac{4m^2}{1+2m^2}
                         \ge\frac43m^2.
\]

The uniform limit in SH7 makes \(4\sqrt\Delta\le m^2/3\) beyond an absolute degree threshold that can also include \(D_0\).
Thus SH9 implies \(\log\operatorname{cap}K_{t,\Theta}\ge m^2\) for all stated radii and collections, and division by the positive \(m/d\) gives SH10 with lower bound \(dm\to\infty\).
This rules out a uniform upper estimate of order \(m/d\) for these same capacities on the stated large-degree inputs.

The [C855 v2 determinant comparison](../../claims/Yin_C_G0855_v2.md#the-capacity-bound-applies-to-the-same-shifted-hankel-determinants) has the direction \(\limsup_h h^{-2}\log|\Delta_h|\le\log\operatorname{cap}K_t\).
A lower bound on that upper envelope does not lower-bound the determinants, so additional arithmetic cancellation remains logically possible.
The proof does not cover alternative or disconnected branch-cut topology or a different arithmetic comparison.
Accordingly it is a boundary for the specified radial-hull method and supplies no positive unrestricted total Mahler gap or G0001 completion.

### Source and verification limits

Pri11 is reused at the exact Theorem 3.1/(3.2) statement and applicability scope retained in the canonical U001, with its stated arXiv:1307.5734v1 edition and original potential-theory-proof limits.
C147 v5 supplies only its explicitly quoted Smy08 equation (11) numerical input at retained statement/applicability scope; the underlying Dobrowolski proof and the survey's defective resultant explanation were not used or newly audited.
The [Smy08 normalization and proof boundary](../literature/Smy08/Yin_U001.md#smy08-u001) were read to check the distinction between total measure and height.
The classical capacity normalization retains the exact accepted Dim19 scope in C855 v2, and the local single-slit derivation and all new Green comparisons were rechecked directly.
This review did not newly inspect the original source PDFs or independently re-audit their full proofs.
No numerical experiment, numerical evaluation of \(D_0\), native computation output or proof-assistant certificate is a premise of this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [C855 v3 statement](../../claims/Yin_C_G0855_v3.md#statement) | Complete A--D: finite comparison, explicit mesh and finite D0 guard, uniform lower cost for all nonempty finite rotation collections, exact single-hull hypothetical-sequence asymptotic, and all stated exclusions. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [C855 v3 argument](../../claims/Yin_C_G0855_v3.md#argument) | Complete SH1--SH10, all original conjugates and powered degree, topology and Green comparison, test support and constants, total-measure conversion, uniform limits and radius/rotation/sequence distinctions. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [C855 v3 source interfaces](../../claims/Yin_C_G0855_v3.md#sources-and-exact-proof-interfaces) | Exact accepted capacity, Pri11 Theorem 3.1 and C147 numerical interfaces, with retained source-proof limits and no cyclic-norm-to-angular substitution. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [C855 v2 single-slit identity](../../claims/Yin_C_G0855_v2.md#a-disk-and-one-radial-slit) | SC1 and its direct Joukowski derivation, applied with radius one and logarithmic slit length 4m; no new whole review of SC1--SC23. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [C855 v2 capacity normalization](../../claims/Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Only the retained Dim19 Green-function, capacity and exterior-map conventions and their source-proof limits. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [C855 v2 determinant comparison](../../claims/Yin_C_G0855_v2.md#the-capacity-bound-applies-to-the-same-shifted-hankel-determinants) | Only the actual upper-bound direction of SC7 needed to delimit the new capacity obstruction; no determinant lower bound or new whole arithmetic review. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [Canonical Pri11 U001](../literature/Pri11/Yin_U001.md#pri11-u001) | Exact Theorem 3.1/(3.2), simple integral polynomial of actual degree d at least 55, M(Q)=exp(2m), global Lipschitz constant one, support radius 5/4, constant 7/2 and normalized circle measure; accepted statement/applicability scope only. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [C147 v5 numerical source scope](../../claims/Yin_C_G0147_v5.md#reuse-and-source-scope) | Only accepted Smy08 equation (11), M(P)>1+(1/1200)(log log d/log d)^3 on the stated nontorsion algebraic-integer domain; fresh 1/2400 conversion and uniform limits checked in C855 v3, with no adoption of C147's cyclic-norm theorem. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [Smy08 normalization and source boundary](../literature/Smy08/Yin_U001.md#smy08-u001) | Total logarithmic Mahler measure versus degree-normalized height, accepted lower-bound statement scope, and exclusion of the defective resultant explanation and uninspected original proof. |
| [Whole Salem radial-hull finding](#salem-radial-hull-whole) | [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) | Original unrestricted total Mahler-gap objective compared for scope only; no Task completion review, near-one sequence existence or unrestricted gap conclusion. |

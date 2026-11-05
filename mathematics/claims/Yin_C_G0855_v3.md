---
author: Yin
---

# Actual Salem radial hulls retain a quadratic Mahler cost

This version fixes a boundary of the all-root radial capacity construction in C855 v2 on actual Salem conjugate sets.
The argument was developed for Yin on 2026-11-05 by the authoring research agent; the coordinating agent checked it as a contributor before this fixation.
The new statement and complete proof below have a selected independent whole assessment at their exact stated scope.
No unrestricted Mahler-gap conclusion or novelty claim is made.

## Retained versions and revision scope

[C855 v2's complete A--D and SC1--SC23](Yin_C_G0855_v2.md#statement) retain their [actual proved assessment](Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04) and [independent R1086 evidence](../audits/reviews/Yin_R_G1086_v1.md#raw-p2-whole).
They include the universal raw p=2 floor, the operator consequence only on the FM13 arithmetic set, the all-root upper contour estimate and its conditional total-Mahler return.
Those exact earlier conclusions and assessment are preserved, rather than replaced or independently reviewed by the new argument.
[C855 v1](Yin_C_G0855_v1.md#statement) remains the unassessed fixed home of its restricted Dobrowolski/support conclusions and original checking limits.
This version does not silently adopt or re-review v1.

The change is a lower estimate for the actual radial-hull capacity on the Salem domain.
It complements v2's upper estimate by showing that changing the disk radius or pricing the neutral angles more accurately cannot make those same capacities have order \(m/d\) on a hypothetical Salem near-one sequence.
This concerns the geometry used in one comparison for [the unrestricted G0001 Task](../tasks/Yin_T_G0001_v1.md#contract), not the actual Hankel growth or every possible branch-cut construction.

## Statement

All logarithms are natural, and angular gaps are measured in radians.
Let \(\lambda=e^m>1\) be an actual Salem number of degree \(d\ge4\), with \(0<m\le1\), and let \(\alpha_1,\ldots,\alpha_d\) be its complete original conjugate list.
Thus this list consists of \(\lambda,\lambda^{-1}\) and \(d-2\) unit-modulus roots, counted at all embeddings.
Let \(B\) be the unit-modulus members of \(\{\alpha_i^2\}\), let \(\Delta\) be their largest successive angular gap, and define
\[
 H=\bigcup_i[0,\alpha_i^2]\cup\bigcup_i[0,\alpha_i^4],
 \qquad K_t=H\cup\{z:|z|\le e^{-t}\}\quad(t\ge0).
\]
Every original neutral and contracting endpoint is retained.

**A. Finite capacity comparison.**
Whenever \(\Delta\le1\), one has, for every \(t\ge0\),
\[
 2\log\cosh(2m)-4\sqrt\Delta
 \le\log\operatorname{cap}H
 \le\log\operatorname{cap}K_t
 \le2\log\cosh(2m).
\]
This is the logarithmic capacity convention of C855 v2.

**B. Explicit mesh control from the original squared polynomial.**
Put
\[
 \rho_d=\frac{8\pi}{d}+\sqrt{14\pi}
                       \left(\frac{\log d}{d}\right)^{1/4}.
\]
For every \(d\ge55\),
\[
                  \min\{1/4,\Delta/(4\pi)\}\le\rho_d.
\]
Let \(D_0\) be the least integer at least 55 with \(\rho_{D_0}\le1/(4\pi)\).
It is finite, and every \(d\ge D_0\) satisfies
\[
 \Delta\le4\pi\rho_d
   =\frac{32\pi^2}{d}
     +4\pi\sqrt{14\pi}\left(\frac{\log d}{d}\right)^{1/4}
   \le1.
\]
No numerical evaluation of \(D_0\) is claimed.

**C. Uniform lower cost for arbitrary nonempty rotation collections.**
For any nonempty finite set \(\Theta\subset\{z:|z|=1\}\), put
\[
 K_{t,\Theta}=\{z:|z|\le e^{-t}\}
                    \cup\bigcup_{\eta\in\Theta}\eta H.
\]
For \(\Delta\le1\), all \(t\ge0\) and all such \(\Theta\) satisfy
\[
 \log\operatorname{cap}K_{t,\Theta}
                   \ge2\log\cosh(2m)-4\sqrt\Delta.
\]
There is an absolute degree threshold beyond which, for every actual Salem input with \(0<m\le1\), every \(t\ge0\), and every such \(\Theta\),
\[
                  \log\operatorname{cap}K_{t,\Theta}\ge m^2.
\]
Along any sequence of these actual inputs with \(d\to\infty\), uniformly over the disk parameters and nonempty rotation collections,
\[
 \frac{\log\operatorname{cap}K_{t,\Theta}}{m/d}
                                \ge dm\longrightarrow\infty.
\]
The rotation collections may vary in cardinality and angles with the polynomial.
Only this lower bound is asserted for multiple rotations.

**D. Exact unrotated asymptotic on a hypothetical near-one sequence.**
For every sequence of actual Salem inputs with \(m_j\to0\) and \(d_j\to\infty\),
\[
 \sup_{t\ge0}\left|
     \frac{\log\operatorname{cap}K_{t,j}}{m_j^2}-4\right|
                                      \longrightarrow0.
\]
The same equality holds after a single rotation of each hull.
No existence of such a sequence is asserted; degree divergence would in any case follow from \(m_j\to0\).

These statements rule out an upper estimate of order \(m/d\) for the specified radial-hull capacities on such actual inputs.
They do not lower-bound the corresponding Hankel determinants, exclude additional arithmetic cancellation, or exclude different and possibly disconnected admissible branch cuts.
They do not resolve the Salem minimum or the unrestricted total Mahler gap.

## Sources and exact proof interfaces

[C855 v2's argument](Yin_C_G0855_v2.md#argument) supplies its adopted Green-function normalization, comparison on the Riemann sphere and exact disk-plus-one-slit capacity.
The segment formula and complete lower comparison used here are given below; no external theorem on Hausdorff continuity of capacity is invoked.
The classical capacity inputs retain the selected Dim19 passage and source-proof limits recorded in v2, without a new whole-source audit.

[Pri11 U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) supplies Theorem 3.1 for an integer polynomial with simple roots and actual degree at least 55, and a real globally Lipschitz compactly supported test.
The proof constructs that test, uses the full squared polynomial of degree \(d\) and total logarithmic measure \(2m\), and separately charges its two off-circle roots.
This reuses the exact accepted statement and applicability scope, without a new inspection of the underlying potential-theory proof.

[C147 v5's source discussion](Yin_C_G0147_v5.md#reuse-and-source-scope) supplies the accepted numerical bound
\(M(P)>1+(1/1200)(\log\log d/\log d)^3\), at its retained Smy08 statement and source-proof scope.
Only that numerical input is used here; the separately proved cyclic-norm bound in C147 v5 is not inserted as an angular estimate.
The elementary logarithm conversion and all uniform limits are proved below.
No stronger Voutier constant or new original Dobrowolski proof review is claimed.

## Argument

### Original roots, hulls and the finite statement

Let \(\lambda=e^m>1\) be a Salem number of degree \(d\ge4\), with \(0<m\le1\), and let \(P\) be its monic irreducible polynomial.
Its complete conjugate list consists of \(\lambda,\lambda^{-1}\) and \(d-2\) unit-modulus roots, counted at all original embeddings.
Let \(B\) be the unit-modulus roots in the squared list \(\{\alpha_i^2\}_{i=1}^d\), and let \(\Delta\in(0,2\pi]\) be the largest successive angular gap in \(B\), measured in radians.
Define
\[
 H=\bigcup_{i=1}^d[0,\alpha_i^2]
           \cup\bigcup_{i=1}^d[0,\alpha_i^4],\qquad
 K_t=H\cup\{z:|z|\le e^{-t}\}\quad(t\ge0),
\]
\[
                  K_* =\overline{\mathbb D}\cup[1,e^{4m}].
                                                               \tag{SH1}
\]
These \(K_t\) are exactly C855's unrotated common-disk radial hulls.
All original branch endpoints remain present, including the two contracting powered endpoints and every neutral endpoint.
One has \(H\subseteq K_t\subseteq K_*\).

Whenever \(\Delta\le1\), the finite estimate is
\[
 2\log\cosh(2m)-4\sqrt\Delta
     \le\log\operatorname{cap}H
     \le\log\operatorname{cap}K_t
     \le2\log\cosh(2m),\qquad t\ge0.                       \tag{SH2}
\]
The constants in (SH2) do not depend on the degree, the positions of the neutral roots or the disk parameter.
The middle lower bound also holds after taking any nonempty finite collection of rotations of \(H\), even when that collection changes with the input.

### Exact Green comparison

The finite radial tree \(H\) has connected, simply connected exterior in the Riemann sphere and a Green function \(g_H\) with pole at infinity.
All its boundary points are regular: each lies on a nondegenerate segment contained in \(H\), and comparison with the explicit Green function of that segment gives continuity to zero there.
Use the normalization
\[
              g_A(z)=\log|z|-\log\operatorname{cap}A+o(1)
                        \quad(z\longrightarrow\infty).
\]
For any \(b\in B\), the inclusion \([0,b]\subseteq H\) gives
\(g_H\le g_{[0,b]}\) on the exterior of \(H\).
Indeed the bounded harmonic difference \(g_H-g_{[0,b]}\) is nonpositive on that exterior's finite boundary and extends harmonically across infinity, so the maximum principle applies on the sphere.

For \(z\) on the unit circle choose \(b\in B\) whose angular distance from \(z\) is at most \(\Delta/2\), and put \(\delta=|z-b|\le\Delta/2\).
Rotation reduces the segment calculation to \([0,1]\).
Its exterior map is
\[
       \Psi(w)=2w-1+2\sqrt{w(w-1)},\qquad \Psi(w)=4w+O(1)
                                      \quad(w\longrightarrow\infty),
\]
with \(g_{[0,1]}(w)=\log|\Psi(w)|\).
For \(|w|=1\) and \(\delta=|w-1|\), the triangle inequality gives
\[
 |\Psi(w)|\le1+2\delta+2\sqrt\delta,\qquad
 g_{[0,1]}(w)\le2\delta+2\sqrt\delta.
\]
For \(\Delta\le1\) it follows that
\[
                0\le g_H(z)\le4\sqrt\Delta
                                  \quad(|z|=1).             \tag{SH3}
\]
The points of \(H\) on the circle satisfy the same bound by continuity.

The actual expanding root supplies \([0,e^{4m}]\subseteq H\), so \(g_H=0\) on the entire external slit in \(K_*\).
Consequently \(g_H-g_{K_*}\) is a bounded harmonic function on \(\widehat{\mathbb C}\setminus K_*\), with boundary values between zero and \(4\sqrt\Delta\).
It extends harmonically across infinity.
The maximum principle therefore yields
\[
       \log\operatorname{cap}K_*-
       \log\operatorname{cap}H\le4\sqrt\Delta.
\]
The [C855 single-slit identity](Yin_C_G0855_v2.md#a-disk-and-one-radial-slit), with radius one and logarithmic slit length \(4m\), gives
\(\operatorname{cap}K_* =\cosh^2(2m)\).
Together with monotonicity, this proves (SH2).
No unspecified modulus of capacity continuity is needed.

### The mesh estimate uses the actual integral squared polynomial

Every positive power of a Salem root has degree \(d\).
To check this, suppose distinct original conjugates had a root-of-unity quotient and apply a Galois automorphism taking the numerator to \(\lambda\).
The image of the denominator would also have modulus \(\lambda>1\), contradicting uniqueness of the expanding conjugate.
Thus all powers of distinct original roots stay distinct.
In particular the monic integer squared polynomial
\[
                     Q(z)=\prod_{i=1}^d(z-\alpha_i^2)
\]
has \(d\) simple roots and total logarithmic Mahler measure \(2m\).
Its two off-circle roots are exactly \(\lambda^2\) and \(\lambda^{-2}\).

For \(d\ge55\), apply the accepted [Pri11 Theorem 3.1 interface](../audits/literature/Pri11/Yin_U001.md#pri11-u001), retaining its actual polynomial degree, simple-root hypothesis and total measure.
Let \(\zeta\) be the midpoint of a maximal neutral angular gap and set
\[
 r=\min\{1/4,\Delta/(4\pi)\},\qquad
                   \varphi(z)=(r-|z-\zeta|)_+.
\]
This is a real globally one-Lipschitz test with support in \(|z|\le5/4\).
Every neutral squared root has distance at least \(2\sin(\Delta/4)\ge\Delta/\pi>r\) from \(\zeta\), so contributes zero.
The two off-circle roots contribute at most \(2r/d\) to the complete normalized root sum.
On the circular arc of angular distance at most \(r/2\) from \(\zeta\), one has \(\varphi\ge r/2\); hence its normalized circle integral is at least \(r^2/(4\pi)\).
Since \(m\le1\), \(M(Q)=e^{2m}\le e^2<55\le d\), so the source's logarithm is exactly \(\log d\).
With its support factor \(2(5/4)+1=7/2\), the theorem therefore gives
\[
       \frac{r^2}{4\pi}\le\frac{2r}{d}
                     +\frac72\sqrt{\frac{\log d}{d}},
\]
\[
 r\le \rho_d:=\frac{8\pi}{d}
                 +\sqrt{14\pi}\left(\frac{\log d}{d}\right)^{1/4}.
                                                               \tag{SH4}
\]
For the last implication, use \(r^2\le ar+b\Rightarrow r\le a+\sqrt b\) for nonnegative \(r,a,b\).
The function \(\rho_d\) is decreasing for real \(d\ge55\) and tends to zero.
Let \(D_0\) be the least integer at least 55 for which \(\rho_{D_0}\le1/(4\pi)\).
This defines a finite threshold; no numerical evaluation of it is asserted.
For every \(d\ge D_0\), (SH4) makes the cap \(r=1/4\) impossible, and gives
\[
 \Delta\le4\pi\rho_d
     =\frac{32\pi^2}{d}
       +4\pi\sqrt{14\pi}\left(\frac{\log d}{d}\right)^{1/4}
     \le1.                                                  \tag{SH5}
\]
Thus the guard required in (SH2)--(SH3) is supplied on the actual original inputs.
The use of Pri11 is at its retained statement and applicability scope, not a new audit of its potential-theory proof.

### The accepted arithmetic lower bound fixes the order of the error

The exact numerical source input retained in [C147 v5](Yin_C_G0147_v5.md#reuse-and-source-scope) is
\[
 M(P)>1+\frac1{1200}
                \left(\frac{\log\log d}{\log d}\right)^3.
\]
For \(d\ge55\), its added term is at most one, so \(\log(1+x)\ge x/2\) gives
\[
 m\ge\frac1{2400}
                \left(\frac{\log\log d}{\log d}\right)^3.   \tag{SH6}
\]
This is the accepted Smy08 numerical Dobrowolski consequence at C147 v5's stated source-proof limit; no stronger constant or fresh original-proof audit is used.
Here \(m\) is the original total measure, with no missing factor of \(d\).
Combining (SH5)--(SH6) proves, uniformly for the stated actual Salem inputs as \(d\to\infty\),
\[
                     \frac{\sqrt\Delta}{m^2}\longrightarrow0,
                     \qquad dm\longrightarrow\infty.       \tag{SH7}
\]
For the first limit, the numerator is
\(O(d^{-1/2}+(\log d/d)^{1/8})\), whereas the denominator is bounded below by
\(2400^{-2}(\log\log d/\log d)^6\).
These are bounds in the actual degree; neither a degree-normalized substitute for \(m\) nor a free neutral configuration has entered.

### Exact asymptotic and its limitations for G0001

Suppose a sequence of actual Salem polynomials satisfies \(0<m_j\le1\), \(m_j\to0\), and \(d_j\to\infty\).
No existence of such a sequence is asserted.
The degree divergence would also follow from \(m_j\to0\): bounded degree and bounded Mahler measure bound every integer coefficient by the elementary root-product coefficient estimates, leaving finitely many polynomials.
The expansion \(2\log\cosh(2m)=4m^2+O(m^4)\), (SH2) and (SH7) yield
\[
 \sup_{t\ge0}\left|
       \frac{\log\operatorname{cap}K_{t,j}}{m_j^2}-4\right|
                                  \longrightarrow0.        \tag{SH8}
\]
The same conclusion holds for a single rotation of each \(K_{t,j}\), since capacity is rotation invariant.

For any nonempty finite set \(\Theta\) of unit complex numbers, define
\[
        K_{t,\Theta}=\{z:|z|\le e^{-t}\}
                       \cup\bigcup_{\eta\in\Theta}\eta H.
\]
It contains one rotated copy of \(H\), so (SH2) always supplies
\[
 \log\operatorname{cap}K_{t,\Theta}
                  \ge2\log\cosh(2m)-4\sqrt\Delta.           \tag{SH9}
\]
In particular the lower bound is uniform in \(t\), the number of rotations, their angles and any variation of those choices along the sequence.
For multiple rotations no matching upper asymptotic with coefficient four is asserted.
The odd-prime rotation unions in C855 are particular instances of (SH9).

For \(0<m\le1\), the elementary inequalities
\(\cosh(2m)\ge1+2m^2\) and \(\log(1+x)\ge x/(1+x)\) give
\(2\log\cosh(2m)\ge(4/3)m^2\).
Thus (SH7) implies, for every sufficiently large actual degree in this range,
\[
 \log\operatorname{cap}K_{t,\Theta}\ge m^2,
 \qquad
 \frac{\log\operatorname{cap}K_{t,\Theta}}{m/d}
                               \ge dm\longrightarrow\infty.
                                                               \tag{SH10}
\]
Consequently an upper bound of order \(m/d\) for these same radial-hull capacities cannot be obtained by optimizing their disk radius, retaining exact angular interactions, or adding rotations on such inputs.
The discrepancy arithmetic already forces enough neutral spines to retain the quadratic cost of the genuine expanding root.

This is a boundary of the specified geometric capacity return, not a lower bound on the actual Hankel determinants.
C855's determinant comparison is an upper bound, so additional arithmetic cancellation could still make those determinants smaller than their capacity envelope.
Different branch-cut topology, disconnected admissible cuts, or a different arithmetic comparison are not excluded.
The finding neither resolves the Salem minimum nor the unrestricted total Mahler gap.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T21:31 |
| status | proved |
| reason | Adopt complete A--D and SH1--SH10 after independent R1086 v2: actual Salem radial hulls retain a quadratic total-Mahler capacity cost uniformly in the disk radius and nonempty finite rotation collections, with the coefficient-four asymptotic only for unrotated or singly rotated hulls on hypothetical near-one sequences. The exact accepted source interfaces and their proof limits are retained. C855 v2's separately adopted raw p=2 result and v1's unassessed scope remain unchanged; neither this capacity boundary nor the earlier p=2 result resolves G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete A--D, including the finite mesh guard, uniform lower cost for nonempty rotation collections, hypothetical single-hull asymptotic and all exclusions. |
| argument | [Complete argument](#argument) | All SH1--SH10: original degree and roots, Green comparison, Lipschitz test and constants, numerical lower-bound conversion and uniform radius/rotation limits. |
| dependency | [Adopted single-slit capacity](Yin_C_G0855_v2.md#a-disk-and-one-radial-slit) | SC1 and its Joukowski derivation, with the retained classical capacity conventions. |
| dependency | [Earlier determinant direction](Yin_C_G0855_v2.md#the-capacity-bound-applies-to-the-same-shifted-hankel-determinants) | Only the upper-bound direction of SC7 delimiting this geometric boundary; no determinant lower bound is inferred. |
| dependency | [Exact numerical arithmetic input](Yin_C_G0147_v5.md#reuse-and-source-scope) | Accepted Smy08 equation (11), M(P)>1+(1/1200)(log log d/log d)^3, at retained statement/applicability scope; no cyclic-norm-to-angular substitution or new original-proof audit. |
| support | [Pri11 quantitative discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Exact Theorem 3.1/(3.2) for the simple original squared polynomial of degree d at least 55, global Lipschitz test and normalized circle measure, at the retained source-proof scope. |
| support | [Smy08 normalization and source boundary](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Total measure rather than normalized height, accepted numerical statement and exclusion of the defective resultant explanation and uninspected original proof. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1086_v2.md#salem-radial-hull-whole) | Complete A--D/SH1--SH10 and exact source interfaces, with no unrestricted gap, numerical D0 evaluation, near-one sequence existence or Hankel lower-bound conclusion. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)

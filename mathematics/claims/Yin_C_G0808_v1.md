---
author: Yin
---

# Explicit varying-source Mahler floor in the original global-eight sign window

Human author Yin.
The author agent semigroup_source_preparation derived the coefficient normalization, regularized averaging estimate, explicit cutoff and varying-source consequences below.
Root checked the retained Proposition 4.10 interface and the one-sided cutoff constants as an author-side assessment.
These are substantive author/checking roles, not independent review.
At author registration, this complete candidate was OPEN for isolated whole review and separate adoption.

## Statement

For each source independently, retain any complete ACTUAL primitive C799 source and its C801 globalF8/selected-X8 outputs in the domain of [adopted C804](Yin_C_G0804_v1.md#decision-whole-reviewed-2026-10-26).
Retain all original source factors and multiplicities, canonical divisor, sign choice, degree, gap, period, padding and full-product/core distinctions.
Write \(h,D,P_8,w_H\) for that source's original constants and \(N=1+2B_{\rm step}\Delta_{\rm crit}s\) for an ORIGINAL parameter with \(s\ge s_{\min}\).
The positive integers \(B_{\rm step},\Delta_{\rm crit}\) and the minimum \(s_{\min}\) are the actual source values, not newly chosen progression data.
The original legal window is
\[
W=[h,h+7P_8)\cap\mathbb Z,\qquad h+7P_8<N.
\]
Let \(b\ge1\) be an integer and let \(A(z)\ne0\) be an ACTUAL admissible zero-or-one low mask supported in \(W\), with \(\operatorname{wt}(A)\le b\).
The chosen original global8 sign is retained; no arbitrary zero-or-one mask is declared admissible.
All logarithmic Mahler measures use probability Haar measure and include every factor and its full multiplicity.

With C804's integer reciprocal prefix-difference polynomial \(A_H\), set
\[
F_A(z,Y)=(1-Y)(1+Y^2)(1-Y^4)A_H(z)
 -2\bigl[(1-z)A(z)+Y^7z^h(1-z^{-1})A(z^{-1})\bigr].
\]
C804 supplies
\[
(1-z)L_0=F_A(z,z^N),\qquad
m(P_N)=m(K_N)=m(L_0)=m(F_A(z,z^N)),
\qquad m_2(F_A)\ge\log2.
\]
The polynomial \(P_N\) here is the actual full height-one output; \(K_N\) is its actual equal-Mahler core.

Define the explicit source and mask-budget constants
\[
S=8w_H+4b,\qquad V=h+14P_8,\qquad L=4w_H+4b.
\]
In particular \(S\ge2\), \(V\ge7\) and \(L\ge1\) on this actual domain.
For every such original \(N>V\) and every \(0<\epsilon\le1\), the candidate estimate is
\[
\left|m(P_N)-m_2(F_A)\right|
 \le 1728S^4\epsilon^{1/(4(S-1))}
       +\frac{\pi VL}{N\sqrt{\epsilon}}
 =:E(S,V,L,N;\epsilon).                                      \tag{EW1}
\]
Consequently \(m(P_N)\ge\log2-E(S,V,L,N;\epsilon)\).
This pointwise estimate is uniform over all actual masks with this budget, without fixing a mask or passing to a subsequence.

For any \(0<\eta\le1\), put
\[
T_\eta(S,V,L)=
 \left\lceil\frac{8VL}{\eta}
       \left(\frac{3456S^4}{\eta}\right)^{2(S-1)}\right\rceil.
                                                               \tag{EW2}
\]
Every original \(N\ge T_\eta\) automatically satisfies \(N>V\), and
\[
m(P_N)\ge\log2-\eta.                                           \tag{EW3}
\]
An explicit original-parameter condition is
\[
s\ge\max\left\{s_{\min},
 \left\lceil\frac{T_\eta-1}{2B_{\rm step}\Delta_{\rm crit}}\right\rceil
 \right\}.
                                                               \tag{EW4}
\]
Thus the condition does not require leaving the original progression.

In particular \(\eta=1/2\) gives the source-independent positive floor
\[
m(P_N)\ge\log2-\tfrac12>0
\quad\hbox{if}\quad
N\ge\left\lceil16VL(6912S^4)^{2(S-1)}\right\rceil.               \tag{EW5}
\]
The cutoff is paid separately for each actual source and budget.

For a sequence of such sources and actual nonempty masks, possibly all different, if \(N_j\to\infty\) and
\[
S_j\log S_j=o(\log N_j),\qquad
V_jL_j=o(\sqrt{N_j}),
                                                               \tag{EW6}
\]
then \(\liminf_j m(P_{N_j})\ge\log2\).
No convergence of the changing values \(m_2(F_{A_j})\), no necessity of these sufficient conditions, and no implication from the original minimum-\(s\) inequality alone is claimed.

## Complete argument

<a id="effective-varying-window-proof"></a>
### 1. Existing inputs and precise source depth

The fixed-polynomial Lawton arguments in [C224](Yin_C_G0224_v1.md#joint-lawton-relation), [C271](Yin_C_G0271_v1.md#essential-family-measure-obstruction), [C339](Yin_C_G0339_v1.md#argument) and [C424](Yin_C_G0424_v1.md#argument) supply qualitative limits at their own scopes.
They do not already supply EW1 for varying C804 templates.
[C425](Yin_C_G0425_v1.md#argument) supplies the elementary equal-interval averaging mechanism, with an unregularized positive-modulus hypothesis for its own different family.
That hypothesis is not imported for \(F_A\), which may have torus zeros.
The complete averaging proof needed here is given below after regularization.

The external input is only the exact earlier Proposition 4.10 retained in [BGMP24-U001](../audits/literature/BGMP24/Yin_U001.md#bgmp24-u001).
For a nonzero \(n\)-variable Laurent polynomial \(R\), with \(k\ge2\) nonzero coefficients, coefficient maximum \(1\), coordinate support diameter \(d\), and an integer monomial-map matrix with relation parameter \(\rho>d\), it gives
\[
0\le\int\left(\tfrac12\log(|R|^2+\epsilon)-\log|R|\right)d\mu
 \le C_2(n,k,\alpha)\epsilon^{(1-\alpha)/(2(k-1))},
\]
\[
C_2(n,k,\alpha)
 =12k^2(18nk^2)^{n-1}\frac{\alpha^{1-n}}{1-\alpha}.
\]
Here the map measure is probability Haar pushforward.
At \(n=2\) and \(\alpha=1/2\), the constant is exactly \(1728k^4\).
The same interface applies to the identity map, whose relation parameter is infinite.

This reuses the source's checked statement, applicability and layer-cake proof depth; the underlying Theorem 4.6 remains an accepted external input rather than a newly audited proof.
[C433](Yin_C_G0433_v1.md#argument) already uses this constant at \(k=3,11\), but its fixed polynomial bounds are not substituted for the variable \(k,d,L\) below.
Neither the questioned final constant nor the later optimization in BGMP24 Theorem 4.1 is used.
The present application to varying \(k\) matches the retained general Proposition 4.10, rather than extrapolating the C433 numerical cutoff.

### 2. Exact height, support, length and coordinate width

Put \(J=\deg A\), \(M=J+1\) and \(B=(1-z)A\).
Then
\[
h\le J<h+7P_8,\qquad h<M\le h+7P_8.
\]
The integer \(A_H\) has coefficient set contained in \(\{-1,0,1\}\), support size and coefficient length \(w_H\), degree \(h\), and constant and leading coefficient \(1\).
These are C804's actual prefix-difference facts.

Let \(g=A_H-2B\).
Below exponent \(h\), \(g\) agrees with \(A_H\).
At exponent \(h\), since \(A_{h-1}=0\), its coefficient is \(1-2A_h\in\{-1,1\}\).
Above exponent \(h\), its coefficients are in \(\{-2,0,2\}\), because every coefficient of \(B\) is in \(\{-1,0,1\}\).
The coefficient of \(z^M\) in \(g\) is exactly \(2\).

The constant and degree-seven \(Y\) rows of \(F_A\) are \(g(z)\) and \(z^hg(z^{-1})\).
The six middle rows are copies of \(A_H\) with signs.
Their \(Y\) exponents differ, so no coefficient addition occurs between rows.
Therefore \(F_A\) has coefficient height exactly \(2\).
Since \(B\) has at most \(2\operatorname{wt}(A)\) monomials and coefficient length at most \(2\operatorname{wt}(A)\),
\[
k(F_A)\le6w_H+2(w_H+2b)=S,
\]
\[
\|F_A\|_1
 =6w_H+2\|g\|_1
 \le6w_H+2(w_H+4b)=2L.
\]
There are at least two distinct nonzero rows, so \(2\le k(F_A)\le S\); the exponent denominator \(S-1\) is positive.

The complete \(z\)-support lies between \(h-M\) and \(M\), with both endpoints present, and the \(Y\)-support lies between \(0\) and \(7\).
Thus its exact \(z\)-width is \(2M-h\le V\), and its coordinate diameter is at most \(V\), since \(V\ge7\).
The normalized monomial shift
\[
R(z,Y)=\tfrac12z^{M-h}F_A(z,Y)
\]
has coefficient height \(1\), length at most \(L\), \(k(R)=k(F_A)\), and all \(z\) exponents in \([0,2M-h]\).
Its full torus and specialized logarithmic measures are those of \(F_A\) minus \(\log2\).
Monomial multiplication changes neither measure nor the torus modulus.

The integer kernel of the substitution vector \((1,N)\) is
\(\mathbb Z(N,-1)\), so its relation parameter is \(N\).
For \(N>V\), distinct support monomials cannot collide: a collision with nonzero \(Y\)-difference would force \(N\le2M-h\le V\), and zero \(Y\)-difference forces identical \(z\)-exponents.
The source's strict diameter condition is therefore satisfied, and the specialized polynomial remains nonzero with its normalized coefficients.

### 3. Zero-compatible comparison and elementary averaging

Write
\[
H_\epsilon(\theta,\phi)
 =\tfrac12\log\left(|R(e^{i\theta},e^{i\phi})|^2+\epsilon\right).
\]
This is a smooth \(2\pi\)-periodic real function, even where \(R\) vanishes.
The two Proposition 4.10 applications give regularization costs
\[
0\le e_N:=\langle H_\epsilon(\theta,N\theta)\rangle_\theta
                -m(R(z,z^N))\le C,
\]
\[
0\le e_2:=\langle H_\epsilon\rangle_{\theta,\phi}
                -m_2(R)\le C,
\qquad
C=1728S^4\epsilon^{1/(4(S-1))}.
\]
Indeed \(k\le S\) and \(0<\epsilon\le1\), so
\(k^4\epsilon^{1/(4(k-1))}
 \le S^4\epsilon^{1/(4(S-1))}\).
This includes the endpoint \(k=2\) and does not require the original logarithm to be bounded below.

The monomial shift from the previous section gives
\[
|\partial_\theta R|\le(2M-h)\|R\|_1\le VL.
\]
For \(u\ge0\), \(u/(u^2+\epsilon)\le1/(2\sqrt\epsilon)\).
Consequently
\[
|\partial_\theta H_\epsilon|
 =\left|\frac{\operatorname{Re}((\partial_\theta R)\overline R)}
 {|R|^2+\epsilon}\right|
 \le \frac{VL}{2\sqrt\epsilon}.
\]
No \(Y\)-derivative or derivative along the fast diagonal is used.

Split the \(\theta\)-circle into \(N\) equal intervals.
On interval \(j\), write \(\theta=(2\pi j+\phi)/N\).
Periodicity gives
\[
\langle H_\epsilon(\theta,N\theta)\rangle_\theta
 =\frac1N\sum_{j=0}^{N-1}
   \left\langle H_\epsilon((2\pi j+\phi)/N,\phi)\right\rangle_\phi.
\]
The full torus mean equals
\[
\frac1N\sum_{j=0}^{N-1}
 \left\langle
 H_\epsilon((2\pi j+\psi)/N,\phi)
 \right\rangle_{\psi,\phi}.
\]
The two first coordinates differ by at most \(2\pi/N\).
The derivative bound proves
\[
\left|
 \langle H_\epsilon(\theta,N\theta)\rangle_\theta
 -\langle H_\epsilon\rangle_{\theta,\phi}
\right|
 \le\frac{\pi VL}{N\sqrt\epsilon}.
\]
Finally
\[
m(R(z,z^N))-m_2(R)
 =\bigl(\langle H_\epsilon(\theta,N\theta)\rangle_\theta
       -\langle H_\epsilon\rangle_{\theta,\phi}\bigr)-e_N+e_2.
\]
Both \(e_N,e_2\) lie in \([0,C]\), so \(|e_2-e_N|\le C\), not merely the coarser \(2C\).
This proves the full absolute comparison EW1.
For its lower-bound consequence alone, the nonnegativity of \(e_2\) suffices.
The scalar and monomial normalizations cancel in the difference.
C804's exact factorization and Jensen bound then give the asserted lower floor, retaining all torus zeros and all factors.

### 4. Explicit tolerance, original parameters and varying sources

For \(0<\eta\le1\), choose
\[
\epsilon=
 \left(\frac{\eta}{3456S^4}\right)^{4(S-1)}.
\]
It lies in \((0,1]\) and makes the regularization term in EW1 exactly \(\eta/2\).
Its square root is
\((\eta/(3456S^4))^{2(S-1)}\).
For every \(N\ge T_\eta\), the averaging term is at most
\[
\frac{\pi\eta}{8}<\frac{\eta}{2},
\]
using \(\pi<4\).
Moreover \(T_\eta\ge8VL/\eta>V\), since \(L\ge1\), \(V>0\) and the remaining power is greater than one.
Thus this cutoff itself supplies every extra diameter hypothesis.
The original progression is increasing with positive step \(2B_{\rm step}\Delta_{\rm crit}\), so EW4 implies \(N\ge T_\eta\).
All original \(s_{\min}\), window and sign conditions remain in force.
For \(\eta=1/2\), EW5 follows; \(\log2=\int_1^2dt/t>1/2\), so its lower bound is strictly positive.

For the varying-source assertion choose \(\epsilon_j=N_j^{-1}\) once \(N_j>V_j\).
Then
\[
E\le1728S_j^4
 \exp\left(-\frac{\log N_j}{4(S_j-1)}\right)
 +\frac{\pi V_jL_j}{\sqrt{N_j}}.
\]
The second term tends to zero by EW6.
The first tends to zero because
\[
\frac{\log N_j}{S_j\log S_j}\longrightarrow\infty,
\qquad S_j\ge2,
\]
so its negative exponential exponent dominates \(4\log S_j+\log1728\).
The second condition also gives \(V_j=o(\sqrt{N_j})\), since \(L_j\ge1\); hence \(N_j>V_j\) eventually.
This proves EW6's liminf statement without a fixed template or a finite-mask subsequence.

### 5. Actual available subfamilies and remaining frontier

C804 supplies a nonempty admissible output at every original \(s\) for
\[
b_+=7D+1,\qquad
S_+=8w_H+28D+4,\qquad L_+=4w_H+28D+4.
\]
It also supplies at least \(2^{7(P_8-D)}-1\) nonempty outputs in the full original window at each original \(s\), with
\[
b_{\rm win}=7P_8,\qquad
S_{\rm win}=8w_H+28P_8,\qquad L_{\rm win}=4w_H+28P_8.
\]
Either choice uses the same \(V=h+14P_8\).
Applying EW2--EW4 to these actual budgets therefore yields nonempty realized families, rather than an estimate only for hypothetical masks.
The \(7D+1\) and \(7P_8\) costs are not replaced by the older \(7D\) budget.

Sources, masks, selected signs and budgets may vary between members subject to the displayed paid condition.
For a fixed source, this makes C804's nonempty-mask threshold explicit; for varying sources it supplies the additional sufficient growth conditions.
It does not assert convergence of a changing-mask sequence to one integral.

The empty mask is excluded: its exact measure remains \(m(A_H)\), and its global8 admissibility is not resolved.
Masks with outside-window support are not covered.
No source checksum, height-one source construction, smaller-source realization or bound on individual irreducible factors is supplied.
The source-dependent cutoff is very large and is not claimed optimal or necessary.
This theorem does not imply that every original admissible \(s\) meets it, remove any source cost, transfer full-product residual precision to \(K_N\), or settle the unrestricted Mahler gap.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision effective-varying-window-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T17:01 |
| status | open |
| reason | Retain the complete author-derived zero-compatible variable-support comparison and explicit paid original-progression cutoff after author-side self-check. Isolated independent whole review and separate adoption remain required; source inspection depth, actual admissibility and all outside-window/empty-mask limitations remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact varying-source/window statement](#statement) | EW1--EW6 for actual nonempty original-window masks, exact constants, positive floor and paid progression, with no unrestricted source-uniform claim. |
| argument | [Complete effective comparison proof](#effective-varying-window-proof) | Exact height 2, support/length/diameter and monomial normalization, both zero-compatible regularization costs, smooth equal-interval averaging, tolerance arithmetic, varying-source conditions and actual nonempty subfamilies. |
| dependency | [Adopted complete C804 theorem](Yin_C_G0804_v1.md#decision-whole-reviewed-2026-10-26) | Actual source and original progression/window, exact integer template and equal-Mahler factorization, nonempty Jensen floor and separately paid \(7D+1\)/\(7P_8\) nonempty realizations. |
| dependency | [Retained Proposition 4.10 interface](../audits/literature/BGMP24/Yin_U001.md#bgmp24-u001) | General normalized \(k\ge2\), \(n=2\), \(\alpha=1/2\), \(\rho>\operatorname{diam}\) zero-compatible bound with exact constant \(1728k^4\), for \((1,N)\) and identity Haar; underlying Theorem 4.6 accepted at retained depth, no questioned final constant. |
| support | [Earlier elementary averaging proof](Yin_C_G0425_v1.md#argument) | Method precedent only; its special positive-modulus family and numerical seed are not dependencies of the complete regularized argument here. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T17:16 |
| status | proved |
| reason | Adopt the unchanged complete EW1--EW6 after reading the entire fixed statement/proof and independent R1028, including its direct general-k published Proposition 4.10 check. The true coefficient normalization, support/length/diameter bounds, zero-compatible regularization and smooth averaging give the explicit paid original-progression cutoff and varying-source liminf. Preserve every actual source/mask/sign budget, the accepted underlying sublevel-source depth, and the empty/outside-window/below-cutoff boundaries. No questioned later constant, necessary cutoff or unrestricted Mahler gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact varying-source/window statement](#statement) | EW1--EW6 for actual nonempty original-window masks, exact constants, positive floor and paid progression, with no unrestricted source-uniform claim. |
| argument | [Complete effective comparison proof](#effective-varying-window-proof) | Exact height 2, support/length/diameter and monomial normalization, both zero-compatible regularization costs, smooth equal-interval averaging, tolerance arithmetic, varying-source conditions and actual nonempty subfamilies. |
| dependency | [Adopted complete C804 theorem](Yin_C_G0804_v1.md#decision-whole-reviewed-2026-10-26) | Actual source and original progression/window, exact integer template and equal-Mahler factorization, nonempty Jensen floor and separately paid \(7D+1\)/\(7P_8\) nonempty realizations. |
| dependency | [Retained Proposition 4.10 interface](../audits/literature/BGMP24/Yin_U001.md#bgmp24-u001) | General normalized \(k\ge2\), \(n=2\), \(\alpha=1/2\), \(\rho>\operatorname{diam}\) zero-compatible bound with exact constant \(1728k^4\), for \((1,N)\) and identity Haar; underlying Theorem 4.6 accepted at retained depth, no questioned final constant. |
| support | [Earlier elementary averaging proof](Yin_C_G0425_v1.md#argument) | Method precedent only; its special positive-modulus family and numerical seed are not dependencies of the complete regularized argument here. |
| review | [Whole independent effective varying-window finding](../audits/reviews/Yin_R_G1028_v1.md#whole-effective-varying-window-finding) | Complete EW1--EW6 and all proof sections, exact C804 input scope, direct published general-k source statement/applicability and retained proof depth, all constants and realized budgets; no enormous polynomial or native numerical experiment. |


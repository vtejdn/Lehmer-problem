---
author: Yin
---

# Short-parameter reductions from complete boundary expansion

<a id="statement"></a>
## Exact expansion and arithmetic consequences

Use the positive integral lattice \(H\), standard integral hyperbolic plane \(U\), and permitted even-norm transvections \(E_v,F_w\) of [v4](Yin_C_G0885_v4.md#statement).
Every positive integral isometry fixes \(e,f\).
For every matrix word \(A\), let \(P_A(z)=\det(zI-A)\).
The [adopted v4 theorem](Yin_C_G0885_v4.md#decision-four-factor-exterior-tests) is retained in full, including its bounded-word and short-word gaps, complete four-scalar determinant, all projected exterior tests, twisted cyclic presentations and cusp-defect reductions.
The new statements below sharpen which parameter sizes can occur at low complete measure; they do not assert a general four-factor gap.

Let \(k\ge2\) be even, and consider the alternating word with all parameters nonzero,
\[
A=R E_{v_1}F_{w_1}\cdots E_{v_{k/2}}F_{w_{k/2}}.
\]
Put
\[
\ell_E=\min_i\|v_i\|_H,\qquad
\ell_F=\min_i\|w_i\|_H,\qquad s=\ell_E\ell_F.
\]
When \(s>8\), define
\[
\gamma(s)=\frac{s-4+\sqrt{s(s-8)}}4>1.
\]
Then the original complete characteristic polynomial has a positive real root \(\Lambda\) satisfying
\[
\Lambda\ge\gamma(s)^k,\qquad M(P_A)\ge\gamma(s)^k.        \tag{1}
\]
The bound is independent of rank, the positive lattice and its determinant, the order of \(R\), every parameter direction and all pairings among the vectors.
It is an estimate on a root of the full original matrix, with no removal of other exterior factors.

For nonzero even-norm integral parameters put
\[
a=\tfrac12\min_i(v_i,v_i),\qquad
b=\tfrac12\min_i(w_i,w_i).
\]
These are positive integers.
The complete low-measure condition implies the exact discrete bound
\[
M(P_A)\le2\quad\Longrightarrow\quad ab\le16.             \tag{2}
\]
In particular:

- For two factors with both parameters nonzero, \(M(P_A)\le2\) forces
  \[
  (v,v),(w,w)\le32,\qquad (v,v)(w,w)\le64.              \tag{3}
  \]
- For four nonzero factors \(A=R E_vF_wE_uF_t\), \(M(P_A)\le2\) admits one of the exact twisted cyclic presentations from v4 whose middle two parameters both have squared norm at most \(32\), with product of their squared norms at most \(64\).
  The two other parameter norms remain unrestricted by this statement.
- In the [opposite-root subclass](../ledger/Yin_L_G0462_v16.md#opposite-root-reduction), where either pair of opposite parameters has squared norm two, \(1<M(P_A)\le2\) forces both remaining squared norms to be at most \(72\).
  This improves the earlier retained numerical bound by using (3); it retains the exact opposite-root hypothesis and the strict positivity assumption.
- If every nonzero even-norm vector of \(H\) has squared norm at least \(10\), then every finite word in both fixed-cusp groups and arbitrary positive integral isometries satisfies
  \[
  M(P_A)=1\quad\hbox{or}\quad
  M(P_A)\ge\frac{7+3\sqrt5}{2}.                         \tag{4}
  \]
  No bound on the word length, lattice rank or positive-isometry orders is imposed.

Zero parameters are removed before (1)--(3) are used.
They can leave shorter or neutral words and do not imply bounds on the remaining displayed parameters.
For a general positive lattice and a four-factor low-measure word, the unresolved regime still includes two unbounded parameters after the bounded middle pair has been selected.

<a id="argument"></a>
## Complete boundary argument and retained inputs

The expansion proof is a direct calculation in the real extension of \(H\oplus U\).
It proves a root of the full matrix and returns to the actual integral characteristic polynomial by similarity.
No new external theorem, source audit, numerical root computation or mathematical program is used.
The subsequent arithmetic deductions use even integral norms, the actual [twisted cyclic identities](Yin_C_G0885_v4.md#twisted-cyclic-presentations), and the [independently reviewed opposite-root conjugacy](../ledger/Yin_L_G0462_v16.md#opposite-root-reduction).

<a id="real-balancing"></a>
### A real similarity balances the two minimum lengths

For \(c>0\), let \(D_c\) fix \(H_{\mathbb R}\) and send \(e\) to \(ce\), \(f\) to \(c^{-1}f\).
This is a real isometry of \(H_{\mathbb R}\oplus U_{\mathbb R}\), and it commutes with \(R\).
Direct substitution gives
\[
D_cE_vD_c^{-1}=E_{cv},\qquad
D_cF_wD_c^{-1}=F_{c^{-1}w}.
\]
Choose \(c=\sqrt{\ell_F/\ell_E}\).
The two minimum parameter lengths of the conjugated word are both
\[
L=\sqrt{\ell_E\ell_F}=\sqrt{s}.
\]
Every parameter of the conjugated word therefore has length at least \(L\).

This similarity preserves the entire characteristic polynomial.
It is not asserted to be an integral basis change, and its rescaled real parameters need not satisfy integral parity conditions.
The real proof below requires neither condition.
All arithmetic conclusions are later applied to the original integral parameters.

<a id="boundary-action"></a>
### Null vectors, inversion and every scalar multiplier

Put \(J=s_{e+f}\), so \(J\) fixes the positive space, sends \(e\) to \(-f\), and sends \(f\) to \(-e\).
For a real positive-space vector \(x\), define the null vector
\[
n(x)=f+x-\tfrac12\|x\|_H^2e.
\]
For \(x\ne0\), put
\[
I(x)=\frac{2x}{\|x\|_H^2}.
\]
The exact full-vector actions are
\[
E_v n(x)=n(x+v),\qquad
J n(x)=\frac{\|x\|_H^2}{2}\,n(I(x)),\qquad
R n(x)=n(Rx).                                          \tag{5}
\]
For the second identity, the positive scalar is essential and is retained.

Since \(JE_vJ=F_{-v}\), the balanced alternating word of even length can be written
\[
A'=R E_{p_1}J E_{p_2}J\cdots E_{p_k}J,                 \tag{6}
\]
where \(p_1=cv_1,p_2=-c^{-1}w_1,\ldots,p_k=-c^{-1}w_{k/2}\).
Every \(p_i\) has norm at least \(L\).
The boundary action of \(E_pJ\) is
\[
f_p(x)=p+I(x),
\]
and (5) shows that its multiplier on the corresponding actual null vector is exactly \(\|x\|_H^2/2\).
The final positive isometry \(R\) changes no multiplier.

<a id="exterior-contraction"></a>
### An invariant complete exterior set and an expanding eigenvector

Assume \(s>8\), equivalently \(L>2\sqrt2\), and choose
\[
r=\frac{L+\sqrt{L^2-8}}2>\sqrt2.
\]
It satisfies \(r+2/r=L\).
Let
\[
X=\{x\in H_{\mathbb R}:\|x\|_H\ge r\}.
\]
This is a nonempty closed, hence complete, subset of the finite-dimensional positive metric space.

For every \(p\) with \(\|p\|_H\ge L\) and \(x\in X\),
\[
\|f_p(x)\|_H\ge L-\frac2{\|x\|_H}
                     \ge L-\frac2r=r.
\]
Thus every \(f_p\) maps \(X\) into itself, and so does \(R\).
For all nonzero \(x,y\), direct expansion gives
\[
\|I(x)-I(y)\|_H
=\frac{2\|x-y\|_H}{\|x\|_H\|y\|_H}.
\]
Hence each \(f_p\) is Lipschitz on this actual exterior set with constant
\[
2/r^2<1.
\]
Convexity of \(X\) is unnecessary because this is a global distance identity on \(X\), not a derivative estimate along an unverified segment.

The boundary map of (6),
\[
F=R\circ f_{p_1}\circ\cdots\circ f_{p_k}:X\longrightarrow X,
\]
therefore has Lipschitz constant at most \((2/r^2)^k<1\).
Starting from any point of \(X\), its successive differences decrease geometrically under iteration of \(F\).
The resulting sequence is Cauchy, its limit remains in \(X\), and continuity makes that limit a fixed point \(x_*\).
This supplies the needed fixed point directly.

At \(x_*\), all intermediate boundary points in the right-to-left evaluation of (6) also lie in \(X\).
Multiplying every scalar in (5) yields
\[
A'n(x_*)=\Lambda n(x_*),\qquad
\Lambda=\prod_{j=1}^k\frac{\|x_j\|_H^2}{2}
                       \ge(r^2/2)^k>1.                \tag{7}
\]
Here \(x_j\) denotes the input to the corresponding \(E_{p_j}J\) factor; the order only determines those inputs and does not alter their lower bounds.
The null vector \(n(x_*)\) is nonzero because its f-coordinate is one.
Thus (7) gives an actual positive real eigenvalue of the full matrix.
Similarity transfers it to the original \(A\), with its complete polynomial unchanged.

Finally,
\[
r^2/2=\frac{s-4+\sqrt{s(s-8)}}4=\gamma(s).
\]
Every root contributes a factor at least one to the monic Mahler product, so the one eigenvalue in (7) proves (1).
There is no use of a small spectral radius as a substitute for total measure.

<a id="integer-short-pair"></a>
### The integer threshold and the bounded middle pair

For \(s>8\), the quantity \(\gamma(s)>1\) is characterized by
\[
s=4+2\bigl(\gamma(s)+\gamma(s)^{-1}\bigr),
\]
and is strictly increasing with \(s\).
For the original parameters, \(s=2\sqrt{ab}\).

The exact comparison
\[
2\sqrt{17}>4+3\sqrt2
\]
follows by squaring positive quantities:
\[
68>(4+3\sqrt2)^2=34+24\sqrt2,
\]
since \(17>12\sqrt2\), equivalently \(289>288\).
At \(s=4+3\sqrt2\), the corresponding value is \(\gamma(s)=\sqrt2\).
Consequently \(ab\ge17\) gives \(s\ge2\sqrt{17}>8\), and (1) gives
\[
M(P_A)\ge\gamma(s)^k>2^{k/2}\ge2.
\]
This proves the contrapositive of (2).
Since \(a,b\ge1\), each is at most \(16\) whenever \(M(P_A)\le2\).

For two factors these are the only two parameters, proving (3), including neutral outputs with both parameters nonzero.
A zero parameter is deliberately excluded from this norm assertion.

For four nonzero factors, choose an e-parameter attaining \(\ell_E\) and an f-parameter attaining \(\ell_F\).
Their squared norms are \(2a,2b\), each at most \(32\), and their product is at most \(64\).
In a four-factor alternating cycle, every e-position is adjacent to every f-position, counting the cyclic boundary.
The four actual [twisted cyclic transformations](Yin_C_G0885_v4.md#twisted-cyclic-presentations) put any such chosen edge into the middle position.
A vector crossing the boundary is transformed by \(R^{-1}\), which preserves its squared norm.
Thus one of those complete-polynomial-preserving presentations has the claimed bounded middle pair.
No bound on the other two norms follows from this argument.

<a id="opposite-root-improvement"></a>
### The opposite-root branch now has squared norms at most seventy-two

Suppose first that the f-parameters \(w,t\) of a four-factor word have squared norm two.
Use the exact [L462 v16 conjugacy](../ledger/Yin_L_G0462_v16.md#opposite-root-reduction):
\[
E_{-t}AE_t=R'E_pF_q,\qquad
v=w+R^{-1}t+Qp,\qquad u=w+t-s_tq,
\]
where \(Q,R',s_t\) are positive integral isometries at their stated scopes.
For \(1<M(P_A)\le2\), its transformed parameters \(p,q\) are both nonzero.
Applying (3) to this actual two-factor word gives
\[
\|p\|_H,\|q\|_H\le4\sqrt2.
\]
The two root contributions in each inverse formula then give
\[
\|v\|_H,\|u\|_H\le6\sqrt2,\qquad
(v,v),(u,u)\le72.                                     \tag{8}
\]
The inequalities are non-strict as stated.
The other opposite-pair orientation follows through the exact cyclic conjugacy in L462 v16, with norm preservation on the twisted parameter.
No part of this deduction applies to the neutral transformed-zero branch, where the other original norm may be unbounded.
The older bound remains valid at its original proof and review scope; (8) is a new stronger consequence of the present expansion estimate.

<a id="large-minimum-lattices"></a>
### Arbitrary words when every allowed nonzero parameter has squared norm at least ten

Assume the lattice condition in (4).
Move all positive-isometry factors to the left using covariance, and combine neighboring equal-cusp transvections by parameter addition.
Remove zero factors.
If an alternating word has odd length at least three, its first and last cusps coincide.
Conjugate by the last transvection, move it across the positive factor, and combine it with the first transvection.
The factor count decreases.
If the new parameter is zero, remove it and continue the same operations.
Every operation preserves the complete polynomial and the actual integral lattice.
Every new nonzero parameter still has even norm, so its squared norm is at least ten by the lattice hypothesis.

This finite reduction terminates at no transvection, one transvection, or an even alternating word with all parameters nonzero.
The first two cases are neutral by the retained zero/one-factor polynomial identity.
In the even case, \(\ell_E,\ell_F\ge\sqrt{10}\), so \(s\ge10\).
Equation (1) gives
\[
M(P_A)\ge\gamma(10)^k
 \ge\gamma(10)^2
 =\left(\frac{3+\sqrt5}{2}\right)^2
 =\frac{7+3\sqrt5}{2}.
\]
This proves (4).
The lattice hypothesis concerns actual nonzero even-norm vectors; it is not an assumption that every positive lattice has this minimum.
An empty positive summand is neutral and causes no exception.

<a id="limits"></a>
## The remaining four-factor construction problem

The new result confines a four-factor candidate with complete measure below \(6/5\) to a presentation with an actual bounded adjacent middle pair.
It sharpens the earlier crude norm-product bound for two factors and the opposite-root branch without changing their complete-polynomial scope.
Lattices having no nonzero permitted parameter of squared norm at most eight cannot produce a target value at any word length.

For the general four-factor case, the two remaining parameters can still be unbounded.
The projected exterior tests of v4, the exact short-pair and opposite-root reductions, and the [displayed-cusp neutrality classification](../ledger/Yin_L_G0462_v16.md#exact-cusp-return) remain applicable.
Passing those tests supplies neither a new nonneutral value nor a positive-to-one sequence.
A general reduction of the two unbounded parameters, or a concrete integer coupling escaping it with controlled complete measure, remains unresolved.

No new target polynomial or numerical search is reported.
These are necessary restrictions and proved subfamily exclusions within the unchanged [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).

## Assessment history

### Decision boundary-expansion-short-pair

| Field | Value |
| --- | --- |
| date | 2026-11-10T04:54 |
| status | proved |
| reason | The complete independent review verifies the real boundary contraction, every full-vector multiplier, the actual expanding eigenvalue, all arithmetic and cyclic consequences, the opposite-root improvement and the arbitrary-word large-minimum exclusion without an unresolved gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Expansion and arithmetic consequences](#statement) | All even lengths and positive lattices, full-polynomial expansion, the exact integer threshold, bounded middle pair, opposite-root bound and large-minimum all-word gap. |
| argument | [Complete boundary proof](#argument) | Real balancing, actual null-vector multipliers, global contraction, integral deductions and every retained-input interface. |
| dependency | [Adopted v4 theorem](Yin_C_G0885_v4.md#decision-four-factor-exterior-tests) | The unchanged bounded-word and short-word gaps, exterior tests, exact cyclic conjugacies and cusp-defect reductions. |
| dependency | [Integral transvections](../ledger/Yin_L_G0462_v13.md#integer-generators) | The actual pairing-preserving formulas, integral even-norm hypotheses and inverses. |
| dependency | [Addition and covariance](../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Finite integral normalization, positive-isometry movement and cyclic shortening, with the complete polynomial preserved. |
| dependency | [Opposite-root conjugacy](../ledger/Yin_L_G0462_v16.md#opposite-root-reduction) | Exact transformed two-factor word and inverse parameter relations for the stronger squared-norm bound seventy-two. |
| review | [Complete independent boundary finding](../audits/reviews/Yin_R_G1114_v12.md#boundary-expansion-short-parameter-review) | The entire statement, new proof, unchanged retained theorem and actual new interfaces, including zero branches and strict or non-strict endpoints. |

## Current assessment

[Selected decision](#decision-boundary-expansion-short-pair)

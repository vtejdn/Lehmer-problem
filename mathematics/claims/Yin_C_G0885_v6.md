---
author: Yin
---

# A uniform Mahler gap for at most five fixed-cusp transvections

<a id="statement"></a>
## Complete low-measure normalization and uniform gap

Use the positive integral lattice \(H\), standard hyperbolic plane \(U\), permitted even-norm integral parameters and two fixed-cusp transvections \(E_v,F_w\) of [v5](Yin_C_G0885_v5.md#statement).
Positive integral isometries of \(H\) are extended to fix \(e,f\).
All measures below are those of the full monic characteristic polynomial \(P_A(z)=\det(zI-A)\), with all roots and multiplicities.

There is an absolute constant \(\eta_5>0\) such that every word with at most five of these transvections and arbitrary intervening positive integral isometries satisfies
\[
m(P_A)=0\quad\hbox{or}\quad m(P_A)\ge\eta_5.             \tag{1}
\]
The constant is independent of lattice rank, determinant, basis, all positive-isometry orders and all displayed vector norms.

More precisely, put
\[
B=33282.
\]
Whenever such a word satisfies \(1<M(P_A)\le2\), it has an integral conjugate, on the same lattice, with at most four permitted transvections, one positive integral isometry on the left, and every parameter of squared norm at most \(B\).
No rational change of the original lattice or omission of factors in the characteristic polynomial is needed for this final representation.

For an alternating four-factor word with all parameters nonzero and \(1<M(P_A)\le2\), first choose the [v5 bounded middle presentation](Yin_C_G0885_v5.md#integer-short-pair),
\[
A=R E_vF_wE_uF_t,\qquad
a=(u,u)/2,\quad b=(w,w)/2,\quad ab\le16.
\]
Put \(\kappa=1-(u,w)+ab\).
If \(\kappa=0\), the exact retained integral relation shortens the word to at most three factors, hence to two.
If \(\kappa>0\) and \(1<M(P_A)\le2\), the original parameters in this chosen presentation already satisfy
\[
(v,v),(t,t)<33282,\qquad (u,u),(w,w)\le32.              \tag{2}
\]
Thus the two unbounded parameters left by v5 are bounded in every nonneutral low-measure case of this branch.

The [adopted v5 theorem](Yin_C_G0885_v5.md#decision-boundary-expansion-short-pair), including the complete v4 tests and earlier bounded-word results it retains, remains valid unchanged.
The present result closes the earlier general four-factor and five-factor gap questions for these two fixed cusps.
It neither supplies an effective exclusion of all values below \(6/5\) nor covers arbitrary word length, arbitrary isotropic base vectors or every integral indefinite-lattice isometry.
The unrestricted G0001 contract remains unresolved.

<a id="argument"></a>
## Proof and exact retained inputs

The new step is an exact decomposition of the bounded middle pair followed by a weighted boundary-expansion estimate.
The auxiliary positive isometry may be rational and need not have finite order.
Only its real orthogonality is used in that estimate.
The final bounded-norm theorem is applied to the actual original integral presentation, not to that auxiliary rational word.

The proof uses the [v5 short-pair theorem](Yin_C_G0885_v5.md#decision-boundary-expansion-short-pair), the [v4 zero-defect relation](Yin_C_G0885_v4.md#cusp-defect-reduction), exact [integer covariance and cyclic shortening](../ledger/Yin_L_G0462_v14.md#short-word-reduction), and the [adopted bounded-count/bounded-norm theorem](Yin_C_G0885_v3.md#decision-bounded-word-bounded-norm-gap).
No new numerical calculation, mathematical program or external theorem is required.
The rational pair decomposition and its zero branches were developed with an ordinary proof collaborator; that development is not independent review.

<a id="middle-pair-decomposition"></a>
### Exact decomposition with all rational costs retained

For this calculation take real vectors \(u,w\), put
\[
a=(u,u)/2,\quad b=(w,w)/2,\quad c=(u,w),\quad
\kappa=1-c+ab>0,
\]
and write
\[
h=u-aw,\qquad r=h/\kappa,\qquad q=(w-bu)/\kappa,
\qquad B_0=F_wE_u.
\]
Let \(D_s\) fix the positive space and send \(e\mapsto se\), \(f\mapsto s^{-1}f\).
Direct expansion gives
\[
(h,h)=2a\kappa,\qquad (w-bu,w-bu)=2b\kappa,
\qquad r^2=2a/\kappa,\quad q^2=2b/\kappa.                \tag{3}
\]
The actions on the two actual cusps are
\[
B_0f=-ae+h+\kappa f=\kappa E_r f,
\]
\[
B_0^{-1}e=\kappa e-w+bu-bf=\kappa F_{-q}e.              \tag{4}
\]

Define the real isometry
\[
S=D_\kappa E_{-r}B_0F_{-q}.
\]
Equation (4) gives \(Se=e\) and \(Sf=f\).
Hence \(S\) preserves their positive orthogonal complement.
Let \(Q\) be its restriction there, extended to fix \(e,f\).
It is a positive real isometry, and rearranging this exact definition proves
\[
F_wE_u=E_rD_{1/\kappa}QF_q.                            \tag{5}
\]
For an explicit expression, put \(j=(1-c)w+bu\).
Acting on a positive vector \(x\) gives
\[
Qx=x+\frac{h(w,x)-j(u,x)}{\kappa}.                     \tag{6}
\]
Indeed the positive component after \(B_0F_{-q}\) is
\(x-w(u,x)+h(q,x)\), its f-coordinate is zero, and
\(\kappa w+bh=j\).
The subsequent two factors in \(S\) leave that positive component unchanged.

For the actual integral middle pair, \(\kappa\) is an integer and (6) makes \(Q\) rational.
Neither integrality nor finite order of \(Q\) is asserted.
All denominators in the parameter shifts \(r,q\) are explicitly \(\kappa\).

Using covariance in (5), the entire original four-factor word is exactly
\[
A=R_0E_pD_{1/\kappa}F_T,\qquad
R_0=RQ,\quad p=Q^{-1}(v+r),\quad T=t+q.                 \tag{7}
\]
This is equality of real matrices on the same real vector space.
It is not an assertion that (7) is a permitted integral-generator presentation.
The positive operator \(R_0\) is orthogonal, which is all the next estimate requires.

<a id="effective-zero-branches"></a>
### Every effective-zero integral branch is neutral

If either \(p=0\) or \(T=0\), the matrix in (7) is block triangular in the order \((e,H,f)\).
Its diagonal blocks are \(\kappa^{-1},R_0,\kappa\).
Thus the complete identity is
\[
P_A(z)=\chi_{R_0}(z)(z-\kappa)(z-\kappa^{-1}).          \tag{8}
\]
Every root of \(\chi_{R_0}\) has modulus one.

In the actual integral setting, \(\kappa\) is a positive integer and \(P_A\) is monic integral.
Its root \(\kappa^{-1}\) forces \(\kappa=1\).
Explicitly, for a monic degree \(d\) integer polynomial vanishing at \(1/\kappa\), multiplication by \(\kappa^d\) gives \(1+\kappa N=0\) for some integer \(N\).
This is impossible for an integer \(\kappa>1\).
Consequently either effective-zero branch has \(M(P_A)=1\).
In particular neither effective vector vanishes when \(1<M(P_A)\le2\).

This argument uses the full original integral polynomial.
It does not pretend that the generally rational factor \(\chi_{R_0}\) is itself an integer cyclotomic polynomial.

<a id="weighted-boundary-expansion"></a>
### Expansion with a nontrivial cusp scaling

Consider any positive real isometry \(R_0\), any \(\kappa\ge1\), and nonzero real vectors \(p,T\) in
\[
A_0=R_0E_pD_{1/\kappa}F_T.
\]
Put \(s=\|p\|\|T\|\).
For \(s>8\), the exact estimate is
\[
P_{A_0}(\Lambda)=0,\qquad
\Lambda\ge\kappa\gamma(s)^2,\qquad
M(P_{A_0})\ge\kappa\gamma(s)^2,                         \tag{9}
\]
where \(\gamma\) is the explicit function in v5.
The measure here is the full monic characteristic-product measure, whether or not the auxiliary matrix is integral.

Conjugating by \(D_c\), with \(c=\sqrt{\|T\|/\|p\|}\), replaces the two parameter lengths by their common value \(L=\sqrt{s}\).
It commutes with \(R_0\) and \(D_{1/\kappa}\), so it preserves the complete polynomial and the displayed scaling.
Write the resulting vectors as \(p',T'\).

Use the actual null vector \(n(x)=f+x-\|x\|^2e/2\), inversion \(I(x)=2x/\|x\|^2\), and reflection \(J=s_{e+f}\) from [v5](Yin_C_G0885_v5.md#boundary-action).
The exact decomposition
\[
E_{p'}D_{1/\kappa}F_{T'}
=(E_{p'}D_{1/\kappa}J)(E_{-T'}J)
\]
has boundary maps and full-vector multipliers
\[
g_1(y)=p'+\kappa^{-1}I(y),\qquad
\mu_1(y)=\kappa\|y\|^2/2,
\]
\[
g_2(x)=-T'+I(x),\qquad
\mu_2(x)=\|x\|^2/2.                                    \tag{10}
\]
Here \(D_{1/\kappa}n(y)=\kappa n(y/\kappa)\), so the factor \(\kappa\) in \(\mu_1\) is retained.

Let
\[
\rho=\frac{L+\sqrt{L^2-8}}2>\sqrt2,\qquad
X=\{x:\|x\|\ge\rho\}.
\]
Since \(L-2/\rho=\rho\) and \(\kappa\ge1\), both maps in (10) preserve \(X\).
The exact inversion distance formula from v5 gives Lipschitz constants
\(2/(\kappa\rho^2)\) and \(2/\rho^2\), respectively.
Thus \(R_0\circ g_1\circ g_2\) is a strict contraction on this complete set.
The same geometric-tail iteration as in v5 supplies a fixed point \(x_*\in X\), with \(y_*=g_2(x_*)\in X\).

Multiplying the full-vector scalars yields the actual nonzero null eigenvector
\[
A_0' n(x_*)=
\frac{\kappa\|x_*\|^2\|y_*\|^2}{4}\,n(x_*).
\]
Its positive eigenvalue is at least
\(\kappa(\rho^2/2)^2=\kappa\gamma(s)^2\).
The balancing similarity returns the same eigenvalue to \(A_0\), proving (9) with the whole polynomial unchanged.

In particular, \(s\ge10\) gives
\[
M(P_{A_0})\ge\kappa\gamma(10)^2
\ge\frac{7+3\sqrt5}{2}>2.                              \tag{11}
\]
Hence \(M(P_{A_0})\le2\), with both effective vectors nonzero, implies \(s<10\).
No isometry-order bound, rational-integrality claim or Fourier argument has been used for \(R_0\).

<a id="four-factor-norm-bound"></a>
### Bounding both remaining original parameters

Return to a four-factor integral word with all parameters nonzero and \(1<M(P_A)\le2\).
The actual v5 twisted cyclic presentation ensures
\[
a,b\in\mathbb Z_{\ge1},\qquad ab\le16,\qquad a,b\le16.
\]
Cauchy--Schwarz gives
\[
0\le\kappa=1-c+ab\le1+2\sqrt{ab}+ab\le25.              \tag{12}
\]
The lower bound and its equality classification are also the retained exact v4 cusp-defect calculation.

If \(\kappa=0\), that calculation gives \(u=w\), \(u^2=w^2=2\).
Its exact integral identity reduces the whole word to three transvections.
The integer short-word conjugacy then reduces it to two.
Since \(1<M(P_A)\le2\), both resulting parameters are nonzero, and the v5 two-factor theorem bounds their squared norms by 32.

Suppose instead that \(\kappa>0\).
Equation (8) excludes either effective-zero branch.
For the nonzero parameters in (7), (11) gives
\[
\|p\|\|T\|<10.                                        \tag{13}
\]
The actual integer vectors
\[
\kappa(v+r)=\kappa v+u-aw,\qquad
\kappa T=\kappa t+w-bu
\]
have even norm: every summand is an integer multiple of a permitted vector, and all cross pairings are integral.
They are nonzero because \(Q\) is invertible and both effective vectors are nonzero.
Positive definiteness and even integrality therefore imply
\[
\|p\|=\|v+r\|\ge\frac{\sqrt2}{\kappa},
\qquad
\|T\|\ge\frac{\sqrt2}{\kappa}.                          \tag{14}
\]
Combining (13)--(14) bounds each effective length by
\[
\|p\|,\|T\|<5\sqrt2\,\kappa\le125\sqrt2.
\]
Equation (3) and \(a,b\le16,\kappa\ge1\) give
\[
\|r\|,\|q\|\le4\sqrt2.
\]
Since \(v=Qp-r\) and \(t=T-q\), the original lengths satisfy
\[
\|v\|,\|t\|<129\sqrt2,
\qquad
(v,v),(t,t)<2\cdot129^2=33282.
\]
Together with the bounded middle pair, this proves (2).
The bound applies to the original integral presentation selected before (5); no rational positive isometry is fed into the bounded-word theorem.

<a id="five-factor-gap"></a>
### All words with at most five factors and the final gap

For a general permitted word, move all positive factors to the left by exact covariance, combine neighboring same-cusp factors, and delete zero parameters.
These operations preserve its integral action and complete polynomial.
If the resulting alternating length is odd and at least three, the first and last cusps coincide.
Conjugating by the final transvection moves it past the positive factor, where its transformed parameter combines with the first.
The count decreases, and any zero sum is removed.
These are the same exact integer identities used in v5's finite shortening argument.

Starting with at most five factors, this leaves zero, one, two or four alternating transvections after any necessary cusp exchange.
Zero and one-factor outputs are neutral.
For \(1<M(P_A)\le2\), the two-factor case has both squared norms at most 32 by v5.
The four-factor case has the bounded presentation just proved, or its zero-defect branch reduces to that two-factor case.
Every actual conjugacy used here is an integral isometry of the same lattice.
An empty positive summand has only the neutral case.

Thus every nonneutral output with \(M(P_A)\le2\) has a permitted presentation with at most four transvections of squared norm at most \(B=33282\).
Apply the adopted v3 theorem at these fixed bounds:
\[
m(P_A)\ge\eta(4,33282)>0.
\]
For \(M(P_A)>2\), one instead has \(m(P_A)>\log2\).
Therefore the absolute choice
\[
\eta_5=\min\{\eta(4,33282),\log2\}>0
\]
proves (1), with no dependence on rank, lattice, isometry orders or the original displayed norms.

<a id="limits"></a>
## Consequences for counterexample construction

Within the specified two-cusp groups, a sequence with positive complete measures tending to one cannot have presentations containing at most five transvections, even if the positive lattices, ranks, isometries and all original parameters vary.
For such a sequence, eventually every permitted presentation must contain at least six transvections.
This is not a proof that its word lengths must tend to infinity: a fixed larger length remains outside this theorem.

The norm reduction preserves the complete polynomial and hence every possible finite target value.
It does not itself classify which values in \((1,6/5)\) occur among the bounded-parameter four-factor words.
The existing count-and-norm theorem supplies a positive constant, without an asserted numerical comparison with \(\log(6/5)\).

The [orthogonal-basis and neutral-embedding exclusions](Yin_C_G0886_v3.md#statement) retain their separate larger-word domains.
The earlier v5 all-word exclusion for lattices with allowed minimum squared norm at least ten also remains valid.
A new construction must respect the exclusions actually applicable to its lattice and presentation.
No new polynomial, finite sampling outcome or positive-to-one family is claimed.
The [unrestricted G0001 objective](../tasks/Yin_T_G0001_v1.md#contract) remains open.

## Assessment history

### Decision at-most-five-transvection-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T05:03 |
| status | proved |
| reason | The complete independent review verifies the exact rational pair decomposition, original-integral zero branches, weighted boundary multipliers, denominator-sensitive norm bounds, all integral shortenings and the final uniform-gap application without an unresolved gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform five-factor gap and normalization](#statement) | Every permitted word of length at most five, arbitrary positive integral lattices and isometries, the complete low-measure representation and all stated bounds and limits. |
| argument | [Complete proof](#argument) | Exact decomposition, effective-zero arithmetic, full real eigenvalue estimate, original parameter bounds and assembly through an actual bounded integral presentation. |
| dependency | [Adopted boundary and short-pair theorem](Yin_C_G0885_v5.md#decision-boundary-expansion-short-pair) | Bounded middle pair, two-factor norm bound, full-vector boundary identities and unchanged retained results. |
| dependency | [Adopted bounded-word theorem](Yin_C_G0885_v3.md#decision-bounded-word-bounded-norm-gap) | The positive complete-logarithmic gap at four factors and squared-norm bound 33282, applied only to the final original integral presentation. |
| dependency | [Exact zero-defect reduction](Yin_C_G0885_v4.md#cusp-defect-reduction) | Nonnegative integer defect, its norm-two equality case and the exact integral three-factor replacement. |
| dependency | [Integer covariance and cyclic shortening](../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Even parameter addition, positive-factor movement, integer inverses, cyclic conjugacy and the full characteristic polynomial. |
| review | [Complete independent five-factor finding](../audits/reviews/Yin_R_G1114_v13.md#at-most-five-transvection-gap-review) | Entire statement and proof, all actual dependencies and endpoint or degenerate cases, with no integrality or finite-order assumption on the auxiliary positive operator. |

## Current assessment

[Selected decision](#decision-at-most-five-transvection-gap)

---
author: Yin
---
# Rotated radicals: complex disk loss and binary relation constraints

The complex-disk argument below retains its original unreviewed scope.
The completed all-place and coherent-center construction is [C857 v2](../claims/Yin_C_G0857_v2.md#decision-whole-independent-review-2026-11-04); the exact fixed-center ranks and precision budget are [C860 v4](../claims/Yin_C_G0860_v4.md#decision-whole-independent-review-2026-11-04).
The remaining complex argument, finite coefficient test and research questions below retain their author-working scope; those fixed assessments do not independently review them.

<a id="neutral-disk"></a>
This working argument tests a necessary analytic hypothesis of the arithmetic holonomicity approach to the [Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract).
The estimates below are agent-S's argument for assessing a strategy and await mathematical review.

## Radius loss from one inner branch point

For a finite set \(B\) on the unit circle with at least five points, let \(R(B)\) be the supremum of \(|f'(0)|\) over holomorphic maps \(f:\mathbb D\to\mathbb C\) with \(f(0)=0\) and all preimages of every \(b\in B\) of even multiplicity.
Omitted values satisfy the condition.
The affine double cover \(y^2=\prod_{b\in B}(x-b)\) is hyperbolic by uniformization.
The projection \(\pi:\mathbb D\to\mathbb C\) from its universal cover, based over \(x=0\), realizes \(R(B)\) because every admissible map lifts by taking a holomorphic square root.
The inclusion of the open unit disk in the \(x\)-plane lifts to this cover, giving an inverse branch \(s:\mathbb D\to\mathbb D\) with \(s(0)=0\).

If \(0<|a|<1\) is an additional value with even preimages for \(f\), factor \(f=\pi\circ h\) with \(h(0)=0\).
The map \(h\) has even preimages at \(s(a)\), since \(\pi\) is unramified there.
Compose \(h\) with a disk automorphism sending \(s(a)\) to zero and take a holomorphic square root.
Schwarz--Pick at zero gives \(|h'(0)|\le 2\sqrt{|s(a)|}/(1+|s(a)|)\).
Schwarz's lemma gives \(|s(a)|\le |a|\), so
\[
 |f'(0)|\le R(B)\,\frac{2\sqrt{|a|}}{1+|a|}.
\]

<a id="regular-orbit"></a>
## A controlled comparison

Write \(\mu_N\) for the \(N\)-th roots of unity and fix \(N=5L\) odd.
If \(f\) is admissible for \(\mu_N\), then \(f^L\) is admissible for \(\mu_5\) and vanishes to order at least \(L\) at zero.
Lift \(f^L\) to the disk uniformizing the affine double cover for \(\mu_5\), which is hyperbolic since its compactification has genus two.
The order-\(L\) Schwarz lemma on the lift bounds the coefficient of \(z^L\) in \(f^L\) by \(R(\mu_5)\).
Thus \(R(\mu_N)\le R(\mu_5)^{1/L}\), also for a rotated polygon, by rotation invariance.
With an extra inner branch point of radius \(e^{-4u}\), the logarithm of the derivative is at most \(L^{-1}\log R(\mu_5)-\log\cosh(2u)\).
At \(u=(\log N)^{-2}\) this is strictly negative for large \(N\).

These constraints already occur in the real reciprocal configuration
\[
 (x-e^u)(x-e^{-u})(x^{2N}-2\cos(\theta)x^N+1),
 \qquad \theta/\pi\notin\mathbb Q .
\]
The second and fourth powers of its roots supply a rotated regular \(N\)-gon of simple branch points and the simple branch point \(e^{-4u}\).
This comparison uses free angles and has no claim to represent a single integral Galois orbit.

<a id="mesh-screen"></a>
## Transfer to a Salem conjugate set

A proposed extension bounds \(R(B)\) by \(1+C\Delta\) when the largest angular gap \(\Delta\), measured in radians, is small.
Here is the argument to check before using the extension to close the single-disk method.

At each point of the unit circle one can choose six members of \(B\) within \(O(\Delta)\), with pairwise distances at least \(c\Delta\), by choosing six separated arcs of length greater than \(\Delta\).
After translation and division by \(\Delta\), the six target values stay in a compact region and stay mutually separated.
Holomorphic maps of the disk based at zero with even preimages of these six normalized targets have uniformly bounded derivative at zero.
Indeed, a diverging derivative there gives a nonnormal family by Marty's criterion.
After taking a subsequence of target configurations, Zalcman's rescaling lemma would yield a nonconstant meromorphic function on \(\mathbb C\) whose preimages of each of the six distinct limits have even multiplicity by the argument principle.
The product of its six differences has only even zeros and even poles and therefore has a meromorphic square root on \(\mathbb C\).
The resulting map into the compact genus-two double cover lifts to the unit disk and is constant.
The classical rescaling input is the lemma of [Zalcman, pp. 814--815](https://www.math.stonybrook.edu/~bonifant/MAT402-s19/Zalcman.pdf).

Push forward the curvature-minus-one hyperbolic metric of the double cover to the plane with order-two cone points at \(B\).
The derivative bound just obtained gives density at least \(c'/\Delta\) along the unit circle by the covering characterization of the density, with divergence at a cone point.
For large absolute \(C\), the hyperbolic disk of radius \(1+C\Delta\) has smaller boundary density there.
The maximum principle on the unit disk compares the two densities since each satisfies \(\nabla^2\log\rho=\rho^2\) in its interior.
At zero the comparison gives \(R(B)\le 1+C\Delta\).

For a Salem number \(\lambda=e^u\) with \(0<u\le1\), take as \(B\) the unit-modulus roots of the polynomial with roots \(\alpha_i^2\), where the \(\alpha_i\) are the degree-\(d\) conjugates of \(\lambda\).
The powers remain distinct, and no square is a fourth power of another conjugate since their positive Weil heights differ.
Simplicity within each power also follows by sending one of two conjugates with torsion quotient to the unique expanding conjugate.
There are two real off-circle roots in the square orbit and the additional simple inner branch point \(a=e^{-4u}\) in the fourth-power orbit.
The squared polynomial is monic of measure \(e^{2u}\).
For \(d\ge55\) the compact Lipschitz discrepancy estimate in [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) gives \(\Delta=O((\log d/d)^{1/4}+1/d)\).
Indeed a unit-Lipschitz tent on a disk of radius comparable to the gap around its midpoint has circle integral \(\gg\Delta^2\) and its only possible root contributions are \(O(\Delta/d)\) from the two off-circle roots.
One may first cap the test radius at an absolute constant to exclude macroscopic gaps for large \(d\).

The proposed combined bound for maps supporting the unrotated radical is therefore
\[
 \log |f'(0)|\le O((\log d/d)^{1/4})-\log\cosh(2u).
\]
In particular the single chart would fail already at \(u\asymp(\log d)^{-2}\) for large \(d\), even when branching with even multiplicity is allowed.
The next check concerns the uniform moving-target estimate, its metric comparison and the finite discrepancy transfer.
This is a restriction on a specific complex analytic proof mechanism under the stated Salem hypotheses.

<a id="remaining-comparison"></a>
## Remaining comparison on the actual original input

The adopted C857 and C860 results above give the complete all-place test, coherent first lift and exact fixed-binomial rank and precision costs.
The elementary disk certificate cannot be repaired by trace cancellation in those fixed truncants or by coherent centers of degree below d with subexponential denominator coefficient norm.
[C860 v5](../claims/Yin_C_G0860_v5.md#decision-whole-independent-review-2026-11-04) now supplies exact dyadic Pade approximants and proves their minimum rational rank for a single radical under the explicit good-reduction hypothesis.
Changing centers with precision does not improve that minimum on this class.
[C860 v6](../claims/Yin_C_G0860_v6.md#decision-whole-independent-review-2026-11-04) supplies partial lower bounds under bad reduction, and [v7](../claims/Yin_C_G0860_v7.md#decision-whole-independent-review-2026-11-04) fixes the leading rank and precision of the supplied componentwise trace family.
Minimum rank for genuinely different joint approximants and centers changing with precision remains a separate question.
[C860 v8](../claims/Yin_C_G0860_v8.md#decision-whole-independent-review-2026-11-04) now resolves that minimum for coprime residual products and the original single radical with squarefree reduction; the several-mask and repeated-reduction cases remain separate.
The new [C855 v2 all-root contour](../claims/Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04) is fixed with its complete capacity proof, norm descent and universal raw p=2 floor.
The remaining total-Mahler return needs a uniform bound on d times the original radial square mass divided by m(P)^2, or a different arithmetic argument that also handles radial concentration.
That ratio is exactly d for Salem inputs; [C855 v3](../claims/Yin_C_G0855_v3.md#decision-whole-independent-review-2026-11-04) now fixes the quadratic capacity cost for the same radial hulls on that actual domain.
[C855 v6](../claims/Yin_C_G0855_v6.md#decision-whole-independent-review-2026-11-05) further gives a uniform lower capacity cost for every compact cut admitting the same original exterior trace.
Its arbitrary-cut estimate exceeds the controlled log d/d arithmetic scale on a hypothetical actual Salem near-one sequence, so replacing this trace's compact cut alone does not close the original return.
The [common-component recentering below](#common-as-recentering) tests higher-degree centers and the first joint Pade error at author-working scope, with its complete original precision and pole costs.
Every proposed approximation or contour improvement still owes its original-input supply, actual degree and complete analytic return.
The neutral-disk argument above remains unreviewed and is not an adopted obstruction to all such methods.

<a id="finite-laurent-test"></a>
## Retained finite pole-coefficient test

This author calculation remains useful for exact finite cancellation tests; it is not covered by the fixed claims' independent findings merely because their general asymptotic theorem is adopted.
Use the original P, U, V, D_J, N_J and nonempty-mask orbit O defined in [C860 v4 Part B](../claims/Yin_C_G0860_v4.md#statement), and an integer t>=1.
The test resolves finite pole losses in the original uncentered truncations; their asymptotic rank slope is already settled by C860 v4.
Let \(Z_J=N_J/D_J-1\), and let \(\beta\) be a zero of \(U(\zeta^jx)\).
The power-stable noncollision statement makes this a simple private denominator zero for that rotation.
For masks \(J\) containing \(j\), put
\[
 b_{J,\beta}(z)=zZ_J(\beta+z),\qquad
 b_{J,\beta}(0)=N_J(\beta)/D'_J(\beta)\ne0.
\]
For \(\sum_{J\in O}\sum_{v=0}^{t}\binom{1/2}{v}Z_J^v\), the coefficient of \((x-\beta)^{-h}\), \(1\le h\le t\), is exactly
\[
 A_{\beta,h,t}=
 \sum_{\substack{J\in O\\j\in J}}\;
 \sum_{v=h}^{t}\binom{1/2}{v}
           [z^{v-h}]\,b_{J,\beta}(z)^v.                     \tag{R9}
\]
The actual order is the largest \(h\) for which (R9) is nonzero, or zero if all these coefficients vanish.
In particular its top coefficient is
\[
 \binom{1/2}{t}
 \sum_{\substack{J\in O\\j\in J}}
             \left(N_J(\beta)/D'_J(\beta)\right)^t.          \tag{R10}
\]
Vanishing of (R10) removes only that top order; the lower orders require (R9) separately.
Nonvanishing of a power sum somewhere in a finite block does not prove a simultaneous rank-slope estimate for these different truncations.
For the centered trace of [C860 v4 Part C](../claims/Yin_C_G0860_v4.md#statement), the same Laurent-coefficient extraction applies to its actual denominator factors.
The shifted rank must include its polynomial part, as in that fixed claim's (R8).

<a id="salem-radial-hull-boundary"></a>
## Fixed home of the actual Salem radial-hull boundary

The complete SH1--SH10 argument is now retained in [C855 v3](../claims/Yin_C_G0855_v3.md#argument), with its [selected whole assessment](../claims/Yin_C_G0855_v3.md#decision-whole-independent-review-2026-11-04) and [independent R1086 v2 finding](../audits/reviews/Yin_R_G1086_v2.md#salem-radial-hull-whole).
It uses all original Salem conjugates and gives the quadratic lower capacity cost uniformly in the disk radius and any nonempty finite rotation collection; only a single hull has the coefficient-four near-one asymptotic.
Its proof and exact source limits are retained in that fixed home rather than duplicated here.
This capacity boundary neither lower-bounds the actual Hankel determinants nor excludes different admissible cuts or stronger arithmetic cancellation.
The separate neutral-disk argument, finite pole-coefficient calculation and following common-component work remain at their stated unreviewed scopes.

<a id="common-as-recentering"></a>
## Removing a common Artin--Schreier component has a paid precision budget

This is a complete author-working derivation by the precision-varying-approximants contributor for Yin.
It has no independent review or selected Claim assessment.
It tests a specific high-degree rational recentering on the actual original input, and retains a finite diagnostic for the remaining joint Padé question.
The adopted inputs are [C857 v2's all-place classification and coherent centers](../claims/Yin_C_G0857_v2.md#coherent-centers), [C860 v2's logarithm and cyclotomic coefficient calculation](../claims/Yin_C_G0860_v2.md#proper-mask-depth), [C860 v4's exact fixed-binomial trace rank and original-root interfaces](../claims/Yin_C_G0860_v4.md#statement), [C860 v5's normalized Padé error](../claims/Yin_C_G0860_v5.md#pade-integrality), and [C855 v2's all-root capacity comparison](../claims/Yin_C_G0855_v2.md#statement).
The new mixed resultant calculation below is explicit.
No numerical experiment, unidentified external input or novelty claim is used.

### Original input and a common residue component

Let \(P,U=P_2,V=P_4,d,m=m(P)\) be exactly the original monic irreducible reciprocal noncyclotomic power-stable input of C860 v4.
Choose
\[
 B,C\in\mathbb Z[x],\qquad B(0)=C(0)=1,\qquad
 C\equiv B\pmod2,\qquad
 e_B=\deg B<d,\quad e_C=\deg C<d.
\]
Put
\[
 N_B=\|B\|_1,\quad N_C=\|C\|_1,\qquad
 R_*(x)=\frac{V(x)B(x)^2}{U(x)C(x)^2}.
                                                               \tag{AS1}
\]
Then \(R_*-1\in4x\mathbb Z[[x]]\), by the same exact divisibility calculation as C860 v4.
The rational function \(R_*\), its inverse and all rotations have integral Taylor coefficients and constant term one.

For an odd prime \(q\), let \(K=\mathbb Q(\zeta_q)\), let \(\mathcal A=\mathcal O_K\otimes\mathbb Z_2\), and put \(R_j(x)=R_*(\zeta_q^j x)\), with \(R_0=R_*\).
All depths below mean simultaneous coefficient divisibility at every prime above two, or equivalently in \(\mathcal A[[x]]\).
They are not depths at a selected residue factor.
Write
\[
 \log R_*=\sum_{n\ge1}\ell_nx^n,\qquad
 \Lambda_q=\min_{\substack{n\ge1\\q\nmid n}}v_2(\ell_n).
                                                               \tag{AS2}
\]
The logarithm belongs to \(4x\mathbb Z_2[[x]]\).
A zero coefficient has valuation infinity.
The calculation below proves that \(\Lambda_q\) is finite.

For each nonzero \(j\bmod q\),
\[
       v_2(R_j/R_0-1)=\Lambda_q.                            \tag{AS3}
\]
Indeed its logarithm has coefficients \(\ell_n(\zeta_q^{jn}-1)\).
These vanish for \(q\mid n\).
For \(q\nmid n\), the factor \(\zeta_q^{jn}-1\) is a unit at every prime above two: a primitive odd-order root remains nontrivial in every residue field.
The exact-depth logarithm isometry from C860 v2 applies because all ratios belong to \(1+4x\mathcal A[[x]]\).
This proves (AS3), including its simultaneous interpretation.

For the particular coherent centers of C857 v2, \(\overline{(R_*-1)/4}=c\) is the normalized reduced Artin--Schreier representative.
That Claim gives \(c(\xi^j x)=c(x)\) in every residue factor when \(c=0\), or when \(c\ne0\) and \(q\mid g\).
Consequently \(\Lambda_q\ge3\) on these actual rich proper-mask classes.
This is an automatic common depth only on those stated classes.
It does not assert that every near-one input has such a prime or residue symmetry.

### A higher-degree center and its exact depth

Let \(I\) be a nonempty proper even mask, put \(k=|I|\), and let \(O\) be its full Galois orbit.
Thus \(2\le k<q\).
Write
\[
 \mathscr S=\bigcup_{J\in O}J,\qquad s=|\mathscr S|,
 \qquad \varepsilon=\boldsymbol1_{\{0\in I\}}.
\]
The indicator \(\varepsilon\) is the same for every \(J\in O\), since the Galois action fixes the position zero.
Use the original \(N_J,D_J,G_J\) of C857/C860 and define
\[
 S_J=\prod_{j\in J}\frac{C(\zeta_q^jx)}{B(\zeta_q^jx)},\qquad
 H_J=S_J R_0^{\,k/2},\qquad
 \widetilde R_J=\frac{N_J}{D_JH_J^2}
                =\prod_{j\in J}\frac{R_j}{R_0}.
                                                               \tag{AS4}
\]
The evenness of \(k\) makes \(H_J\) rational.
These are centers for the same original radicals:
\[
               G_J=H_J\sqrt{\widetilde R_J},
 \qquad G_J(0)=H_J(0)=\sqrt{\widetilde R_J}(0)=1.
\]
The square roots use their normalized formal branches.
Both \(H_J\) and \(H_J^{-1}\) have algebraic-integral Taylor coefficients, and \(H_J\equiv1\pmod2\).
Since \(R_0\) has rational coefficients, \(\sigma(H_J)=H_{\sigma J}\); every center is fixed by the stabilizer of its mask.
No division by a stabilizer order is needed.

The new centers need not have degree below \(d\).
Before cancellations, their numerator and denominator degrees are both
\[
                     \frac{k}{2}\bigl(d+2e_B+2e_C\bigr).
                                                               \tag{AS5}
\]
Indeed a numerator is \(C_J(VB^2)^{k/2}\) and a denominator is \(B_J(UC^2)^{k/2}\), where \(B_J,C_J\) are the corresponding rotation products.
Thus (AS4) genuinely tests centers outside C860 v4 Part E's low-degree class.

Every such mask has exactly the same new simultaneous depth:
\[
                 v_2(\widetilde R_J-1)=\Lambda_q.
                                                               \tag{AS6}
\]
To prove this, the logarithm of \(\widetilde R_J\) has coefficient
\[
             \ell_n\left(\sum_{j\in J}\zeta_q^{jn}-k\right).
\]
For \(q\mid n\), this coefficient is zero.
For \(q\nmid n\), the parenthesized coefficient is not in \(2\mathcal A\).
In fact \(k\) is even, so its reduction is the nonempty proper binary mask polynomial evaluated at a primitive root.
The only binary polynomials of degree at most \(q-1\) divisible by \(\Phi_q=1+x+\cdots+x^{q-1}\) are zero and the full mask polynomial.
Both are excluded.
This is the all-place cyclotomic-basis argument of C860 v2; it does not require \(\Phi_q\) to be irreducible modulo two.
Multiplication by the rational scalar \(\ell_n\) therefore has exact simultaneous depth \(v_2(\ell_n)\).
The same logarithm isometry proves (AS6).
Individual residue factors may have greater depth; (AS6) is the exact minimum across all of them.

### Mixed resultants bound the newly exposed precision

The following uniform bound includes both center coefficient norms:
\[
 \boxed{\displaystyle
 \Lambda_q\log2\le
 2\log(2d)+2\log N_B+2\log N_C+
 \left(20-\frac{10}{d}+\frac{4(e_B+e_C)}d\right)m.}
                                                               \tag{AS7}
\]
The coefficient multiplying \(m\) is less than \(28\).
Unlike C860 v4's single-center budget, this argument needs a bound on \(N_C\) as well as \(N_B\).

First, neither \(B\) nor \(C\) vanishes at any root-of-unity rotation of an original \(P_2\) or \(P_4\) root.
For if \(\gamma=\zeta_q^j\alpha^{-a}\), \(a=2\) or \(4\), were such a root, then power stability gives
\[
 d=[\mathbb Q(\gamma^q):\mathbb Q]
 \le[\mathbb Q(\gamma):\mathbb Q]
 \le\max(e_B,e_C)<d,
\]
a contradiction.
This is the exact low-degree exclusion already used in C860 v4.
All rotated original \(U\)-roots are distinct, and none is a rotated \(V\)-root, by C858's power-stable noncollision.

For a nonzero \(j\bmod q\), use subscripts for rotation and set
\[
 \Gamma_j=
 V_j B_j^2 U C^2-VB^2U_j C_j^2.
                                                               \tag{AS8}
\]
Here \(B_j=B(\zeta_q^jx)\) and \(C_j=C(\zeta_q^jx)\), rather than mask products.
The denominator of \(R_j/R_0-1\) is \(U_jC_j^2VB^2\), an integral polynomial with constant term one.
It preserves exact coefficient depth, so \(\Gamma_j\in2^{\Lambda_q}\mathcal O_K[x]\) whenever this depth is finite.
The following nonzero resultant also proves that the difference cannot vanish identically:
\[
 \begin{split}
 \operatorname{Res}(U,\Gamma_j)
   &=(-1)^d\operatorname{Res}(U,V)
        \operatorname{Res}(U,B)^2
        \operatorname{Res}(U,U_j)
        \operatorname{Res}(U,C_j)^2
       \ne0 .
 \end{split}                                                    \tag{AS9}
\]
Every factor is nonzero by the preceding exclusions.
Since \(U\) is monic and integral, evaluating the polynomial divisibility at all its \(d\) roots proves
\[
           \operatorname{Res}(U,\Gamma_j)
                        \in2^{d\Lambda_q}\mathcal O_K.
                                                               \tag{AS10}
\]
Taking the field norm to \(\mathbb Q\) retains all \(q-1\) conjugate factors.

The original cross-power estimate from C860 v4 is
\[
 \log|\operatorname{Res}(U,V)|
                  \le d\log(2d)+(12d-6)m.
                                                               \tag{AS11}
\]
The same Vandermonde calculation on all roots of \(U\) and \(U_j\) gives, at every complex embedding of \(K\),
\[
 \log|\operatorname{Res}(U,U_j)|
                  \le d\log(2d)+(8d-4)m.
                                                               \tag{AS12}
\]
For clarity, their combined \(2d\)-root Vandermonde determinant has squared absolute value at most
\[
       (2d)^{2d}\exp\bigl(8(2d-1)m\bigr).
\]
Its squared absolute value is
\[
 |\operatorname{disc}U|\,|\operatorname{disc}U_j|\,
 |\operatorname{Res}(U,U_j)|^2.
\]
The rotation only changes the leading coefficient and discriminant by complex numbers of modulus one, so
\(|\operatorname{disc}U_j|=|\operatorname{disc}U|\ge1\).
This proves (AS12); no unproved integer discriminant for the rotated polynomial is assumed.

At every complex embedding, the coefficient-norm estimate and \(m(U)=2m\) give
\[
 \begin{split}
 \log|\operatorname{Res}(U,B)|&\le d\log N_B+2e_Bm,\\
 \log|\operatorname{Res}(U,C_j)|&\le d\log N_C+2e_Cm.
 \end{split}                                                    \tag{AS13}
\]
Rotation preserves the coefficient norm and root moduli used in these inequalities.
Apply (AS11)--(AS13) to every conjugate of the nonzero algebraic integer in (AS9).
By (AS10), its norm has absolute value at least \(2^{d\Lambda_q(q-1)}\).
The upper estimates give
\[
 \begin{split}
 d\Lambda_q\log2
 \le{}&2d\log(2d)+2d\log N_B+2d\log N_C\\
     &+\bigl(20d-10+4e_B+4e_C\bigr)m.
 \end{split}
\]
This proves (AS7), with no factor of \(q\) left over and no assumption that \(qm\) is small.

For C857's zero-or-one lifts, \(\deg B=\deg C=e\le d/2\), \(N_B\le e+1\), and \(N_C\le3(e+1)\).
Thus the explicit sufficient budget becomes
\[
 \Lambda_q\log2\le
 2\log(2d)+4\log(d/2+1)+2\log3+24m.
                                                               \tag{AS14}
\]
The strengthened precision is therefore \(O(\log d)\) on any hypothetical near-one sequence using those lifts.
This conclusion concerns the exact new depth in (AS6), not merely the old depth-three construction.

### The shared pole cost and the original capacity return

Put \(a=\Lambda_q-2\), and suppose \(\Lambda_q\ge3\).
Apply fixed binomial truncation to the new residuals in (AS4):
\[
 F_t=\sum_{J\in O}H_J
              \sum_{v=0}^{t}\binom{1/2}{v}
                             (\widetilde R_J-1)^v,\qquad
 f=\sum_{J\in O}G_J.
\]
The supplied centers, residuals and complete orbit have the exact hypotheses of C860 v4's general fixed-binomial trace theorem.
They are fixed as \(t\) varies.
The integral centers and simultaneous depth give
\[
       f-F_t\in2^{a(t+1)+1}\mathbb Z[[x]],\qquad
       \rho(F_t)=\kappa t+O(1),
                                                               \tag{AS15}
\]
Here \(\kappa\) is the sum over projective points of the largest pole order among the \(\widetilde R_J-1\).
The arithmetic descent uses the equivariant orbit sum itself, with no stabilizer division.

This exact slope satisfies both paid bounds
\[
 \boxed{\displaystyle
 d(s+k-2\varepsilon)\le\kappa
 \le(s-\varepsilon)(d+2e_C)
                 +(k-\varepsilon)(d+2e_B).}
                                                               \tag{AS16}
\]
To prove the lower bound, for every nonzero \(j\in\mathscr S\), the \(d\) original \(U_j\)-roots remain simple poles in each residual whose mask contains \(j\).
All center factors are finite and nonzero there by the degree exclusion.
At each original \(V_0\)-root, every \(\widetilde R_J\) has a pole of order \(k-\varepsilon\).
These original pole sets are disjoint.
Their total contribution is \(d(s-\varepsilon)+d(k-\varepsilon)\).
Subtracting one from a rational function does not alter a genuine pole, so the same count applies to \(\widetilde R_J-1\).

For the upper bound, remove the trivial ratio \(R_0/R_0\) when \(0\in J\).
A common denominator of the residuals is
\[
 \left(\prod_{j\in\mathscr S\setminus\{0\}}U_j C_j^2\right)
                  V^{\,k-\varepsilon}B^{\,2(k-\varepsilon)}.
                                                               \tag{AS17}
\]
Every ratio \(R_j/R_0\) has a finite nonzero limit at infinity, even if \(e_B\ne e_C\).
There is therefore no uncounted pole at infinity.
The degree of (AS17) is the right-hand side of (AS16).
Possible center-factor overlaps or cancellations can only decrease that upper bound.

The actual function \(f\), its coefficients, its complete rotated branch endpoints and its used rotation set \(\mathscr S\) have not changed.
C855 v2's all-root contour therefore applies to these same shifted leading determinants.
Combining it with all precision levels in (AS15) gives
\[
       \frac{a\log2}{2\kappa}
           \le\limsup_{h\to\infty}h^{-2}\log|\Delta_h(f)|
           \le\inf_{\tau\ge0}\Phi_s(\tau).
                                                               \tag{AS18}
\]
All limits fix \(P,q,I,B,C\) first.
The lower inequality uses the infinitely many nonzero integral determinants supplied by [C858's adopted nonrationality criterion](../claims/Yin_C_G0858_v1.md#all-place-hankel-budget).
In C855's notation \(E_2=\sum_i(\log|\alpha_i|)_+^2\), and its explicit upper bounds yield
\[
 \begin{split}
 E_2&\ge\frac{a\log2}{10s\kappa},\\
 E_2&\ge\frac{a\log2}{20s\kappa}+\frac1{20ds^2}.
 \end{split}                                                    \tag{AS19}
\]
Because \(E_2\le m^2\), both right-hand sides give valid squared lower bounds for the original total \(m\).
No rank-normalized measure or powered replacement of the original input has entered.

Let
\[
 \mathcal B=
 2\log(2d)+2\log N_B+2\log N_C+
 \left(20-\frac{10}{d}+\frac{4(e_B+e_C)}d\right)m.
\]
The first displayed coarse total-measure certificate obeys
\[
 \left(\frac{a\log2}{10s\kappa}\right)^{1/2}
       \le
 \left(\frac{\mathcal B}
                  {10ds(s+k-2\varepsilon)}\right)^{1/2}.
                                                               \tag{AS20}
\]
The second certificate in (AS19) has the corresponding upper bound obtained by replacing its first term by
\(\mathcal B/[20ds(s+k-2\varepsilon)]\).
Thus both displayed certificates tend uniformly to zero along any hypothetical near-one sequence for which
\[
              \log N_B=o(d),\qquad \log N_C=o(d).
\]
Here \(d\to\infty\) by [the retained degree-escape argument](../claims/Yin_C_G0219_v1.md#discriminant-escape), \(s\ge k\ge2\), and \(s+k-2\varepsilon\ge2\).
The estimate is uniform in the odd prime and all eligible even masks, and it applies in particular to (AS14).
It requires both coefficient-norm hypotheses.

This uniform vanishing concerns only the explicit coarse certificates (AS19)--(AS20).
It is not a claim that the actual capacity, the actual Hankel growth or every use of C855's exact contour is incapable of improvement from additional root structure.
The recentering gives a real higher-degree construction and a larger potentially useful precision \(\Lambda_q\), but does not by itself supply a uniform total Mahler gap.
Finer arithmetic, a different approximation family and a genuinely joint Padé rank improvement remain possible.

### A finite test for the first joint Padé error

The same construction gives an explicit remaining calculation, rather than a presumed additivity of component ranks.
At each prime \(\mathfrak p\mid2\), let \(k_{\mathfrak p}\) be its residue field and define rational functions
\[
 b_{j,\mathfrak p}
    =\overline{\frac{R_j/R_0-1}{2^{\Lambda_q}}}
         \in k_{\mathfrak p}(x),\qquad b_{0,\mathfrak p}=0,
 \qquad
 z_{J,\mathfrak p}=\sum_{j\in J}b_{j,\mathfrak p}.
                                                               \tag{AS21}
\]
Their denominators have constant coefficient one, so these reductions also represent their actual Taylor series.
Expanding the product in (AS4) proves
\[
     z_{J,\mathfrak p}
       =\overline{(\widetilde R_J-1)/2^{\Lambda_q}}.
\]
The cross terms have at least one extra factor of two after division by \(2^{\Lambda_q}\).

For the odd Padé exponent \(n=2t+1\), let \(\widehat F_t\) be the orbit sum obtained by replacing each binomial truncation in (AS15) by C860 v5's rational Padé approximant.
The first possible common error level is \(an+1\).
Since \(H_J\equiv1\pmod2\), C860 v5's exact normalized-error formula gives, in each residue field,
\[
 \overline{\frac{f-\widehat F_t}{2^{an+1}}}
                =\sum_{J\in O}z_{J,\mathfrak p}^{\,n}.
                                                               \tag{AS22}
\]
These are the actual original orbit sum, its actual centers and its actual rational approximants.
If the displayed reduction is nonzero at a residue factor, the simultaneous error has exactly that depth.
If it is zero at every factor, the common error depth increases by at least one.
The full Galois-compatible trace descends to rational coefficients; the residue-factor computations retain that descent instead of replacing a global condition by an unrelated one-place mask test.

For any fixed residue factor, the right side of (AS22) vanishes for every positive odd exponent if and only if every distinct nonzero value among the rational functions \(z_{J,\mathfrak p}\) occurs an even number of times.
This is a finite test.
To prove it, list the distinct nonzero values as \(w_1,\ldots,w_L\), and let \(\epsilon_\ell\in\mathbb F_2\) be their multiplicities modulo two.
For \(t=0,\ldots,L-1\), the odd-power equations are
\[
               \sum_{\ell=1}^L
                       (\epsilon_\ell w_\ell)(w_\ell^2)^t=0.
                                                               \tag{AS23}
\]
The squares \(w_\ell^2\) are distinct in the field \(k_{\mathfrak p}(x)\).
The Vandermonde matrix in (AS23) is invertible, so all \(\epsilon_\ell w_\ell\) vanish, equivalently every multiplicity is even.
The converse follows by pairing equal values.
The empty list gives zero identically.
The same argument works for any \(L\) consecutive odd exponents after multiplying each column by the corresponding nonzero initial power.
Thus if the parity condition fails, these first-level errors cannot vanish on an arbitrarily long consecutive block of odd exponents.
For an all-place conclusion, apply the condition to every residue factor.

This criterion describes only the first normalized Padé error.
It neither identifies the behavior at the later binary levels when that error vanishes, nor proves minimum rank for a sum of several radicals.
The independent-component upper bound in C860 v5 remains available, but its degree sum cannot be declared minimal from (AS22)--(AS23).
Determining whether the actual finite residue data permit a smaller joint rank, with a corresponding favorable original-input capacity return, remains a continuing question.

<a id="joint-pade-orbit-frequency"></a>
## Exact frequency and orbit conditions for the first joint Padé error

This continuation is author-working mathematics by the same contributor for Yin, with no independent review.
It preserves (AS1)--(AS23) and makes their first-error test finite in the actual off-\(q\) logarithm data.
The bounded local reuse search found [C857 v1's cyclic-mask mechanism](../claims/Yin_C_G0857_v1.md#binary-cyclic-mask), [C857 v2's all-place coefficient argument](../claims/Yin_C_G0857_v2.md#four-spaces-symmetry), and the preceding common-component construction.
The Fourier argument below reuses that existing mechanism; no new general cyclic-code theorem is asserted.
The new deductions are the exact common rational function, the orbit incidence formula and the distinction between simultaneous injectivity and residue-factor parity.

### One rational function controls all the first errors

Keep all actual inputs and the exact \(\Lambda_q\) of (AS1)--(AS23).
Define the formal series
\[
 T(x)=\sum_{\substack{n\ge1\\q\nmid n}}
          \overline{2^{-\Lambda_q}\ell_n}\,x^n
                  \in\mathbb F_2[[x]].
                                                               \tag{OF1}
\]
Only the off-\(q\) coefficients are divided by \(2^{\Lambda_q}\); the full logarithm need not have that depth.
The series \(T\) is nonzero because the minimum in (AS2) is attained.
It has no Taylor coefficient whose exponent is divisible by \(q\).
In fact
\[
                         T\in\mathbb F_2(x).                \tag{OF2}
\]
To prove rationality and identify the local errors, fix a residue factor, write its primitive root as \(\xi\), and reduce the logarithm in (AS3) at its exact common depth.
The logarithm isometry gives
\[
 \begin{split}
 b_j(x)
   &=\sum_{q\nmid n}
        \overline{2^{-\Lambda_q}\ell_n}
                      (\xi^{jn}-1)x^n,\\
 \sum_{j=1}^{q-1}b_j(x)&=T(x).
 \end{split}                                                    \tag{OF3}
\]
For the second equality, \(\sum_{j=1}^{q-1}\xi^{jn}=-1=1\) in characteristic two, while \(q-1=0\) there.
Each \(b_j\) is the actual rational function in (AS21), so their sum is rational over the residue field.
Its Taylor coefficients lie in \(\mathbb F_2\); coefficient Frobenius fixes that rational function, proving its descent to \(\mathbb F_2(x)\).
Equivalently, uniqueness of its reduced numerator and denominator with denominator constant one gives the same descent.
Thus the same nonzero \(T\) works at every residue factor.

Equations (OF1)--(OF3) now give
\[
 b_j(x)=T(\xi^jx)+T(x),\qquad
 z_J(x)=\sum_{j\in J}T(\xi^jx)                              \tag{OF4}
\]
for every even mask \(J\).
This \(T\) is the newly exposed off-\(q\) logarithm component, not the earlier reduced Artin--Schreier representative \(c\).

### Finite frequency support and exact collision tests

Let
\[
 \mathcal F=\{r\in(\mathbb Z/q\mathbb Z)^\times:
                 [x^n]T\ne0
                 \text{ for some }n\equiv r\pmod q\}.
\]
This set is nonempty.
It can be computed from finitely many rational operations without an unbounded coefficient search.
Indeed
\[
 T_r(x)=\sum_{j=0}^{q-1}\xi^{-jr}T(\xi^jx)
       =\sum_{n\equiv r\;(\mathrm{mod}\ q)}[x^n]T\,x^n
                                                               \tag{OF5}
\]
is rational, and \(r\in\mathcal F\) exactly when \(T_r\ne0\).
The root-of-unity sum equals one for a matching residue, because the odd integer \(q\) equals one in the residue field, and equals zero otherwise.

For an even mask \(J\), put \(A_J(X)=\sum_{j\in J}X^j\).
Different \(T_r\) have disjoint Taylor exponent supports.
Consequently, at the selected residue factor,
\[
 \begin{split}
 z_J=z_L
 &\ \Longleftrightarrow\
 A_J(\xi^r)=A_L(\xi^r)\quad\text{for every }r\in\mathcal F,\\
 z_J=0
 &\ \Longleftrightarrow\
 A_J(\xi^r)=0\quad\text{for every }r\in\mathcal F .
 \end{split}                                                    \tag{OF6}
\]
Since these mask polynomials are binary, their vanishing conditions automatically extend to the Frobenius closure of \(\mathcal F\).
Equivalently one can test divisibility by the product of the distinct binary minimal polynomials of the roots \(\xi^r\), \(r\in\mathcal F\).
This is an exact finite collision criterion for the actual first-error functions.

Together with (AS23), (OF6) gives a finite criterion for all odd first-error moments to vanish at a residue factor: every nonzero vector
\[
              \bigl(A_J(\xi^r)\bigr)_{r\in\mathcal F},
                     \qquad J\in O,
                                                               \tag{OF7}
\]
must occur an even number of times.
Apply this at every residue factor for the simultaneous condition.
The criterion depends on the actual support \(\mathcal F\) and mask orbit, not only on the number of masks.

The simultaneous map from equal-size proper even masks to their complete collections of residue-factor values is injective.
For if \(z_J=z_L\) at every factor, choose any supported exponent \(n\) of \(T\).
It is not divisible by \(q\).
The residue-factor embeddings and their Frobenius conjugates range over all primitive \(q\)-th roots.
Thus \(A_J+A_L\) vanishes at every primitive root and is divisible by \(\Phi_q\).
It has degree at most \(q-1\), so it is either zero or the full mask polynomial.
The latter would mean that \(J\) and \(L\) are complements; they cannot have the same cardinality because \(q\) is odd.
Therefore \(J=L\).
The same argument shows that a nonempty proper even mask has a nonzero complete collection of values.
This does not assert injectivity after projection to one residue factor, and does not prohibit different even pairings at different factors.

If \(\operatorname{ord}_q(2)=q-1\), one residue factor already contains the full Frobenius orbit of every nonzero frequency.
In this case (OF6) is injective on equal-size proper even masks in that single field, and every value is nonzero.
Hence the first errors cannot vanish for every odd exponent.
More precisely, every \(|O|\) consecutive odd exponents contain a nonzero first error by (AS23).
No supply of primes satisfying this multiplicative-order condition, or bound on additional digits at the other indices, is asserted.

### The first odd moment is determined by orbit incidence

Let \(h=|\operatorname{Stab}(I)|\), \(M=|O|=(q-1)/h\), and retain \(k=|I|\) and \(\varepsilon=\boldsymbol1_{\{0\in I\}}\).
The stabilizer acts freely on nonzero positions, so \(h\mid(k-\varepsilon)\).
Each nonzero position occurs in exactly
\[
                            \nu=(k-\varepsilon)/h
\]
masks of the orbit.
The position zero occurs in all \(M\) masks if \(\varepsilon=1\), and in none otherwise.
Since \(T\) has no \(q\)-divisible Taylor exponents, \(\sum_{j=0}^{q-1}T(\xi^jx)=0\).
Summing (OF4) over the orbit therefore proves the exact formula
\[
              \sum_{J\in O}z_J
                   =(\nu+\varepsilon M)T,                 \tag{OF8}
\]
where the integer coefficient is reduced modulo two.
This formula holds at every residue factor and concerns the actual normalized error at exponent \(n=1\).

If \(\varepsilon=1\), then \(k-\varepsilon=k-1\) is odd.
Thus \(h\) and \(\nu\) are odd, whereas \(M\) is even, so the first error is exactly \(T\ne0\).
Such even masks acquire no extra binary digit at this first error.
Equivalently, \(v_2(f-\sum_{J\in O}H_J)=\Lambda_q-1\).
If \(\varepsilon=0\), the error is nonzero exactly when \(k/h\) is odd.
For example, an antipodal pair \(\{j,-j\}\) has \(h=2\) and nonzero first error.
A nonzero pair that is not antipodal has \(h=1\), so its first error vanishes and the actual trace gains at least one digit at \(n=1\).
For this pair orbit, \(v_2(f-\sum_{J\in O}H_J)\ge\Lambda_q\).
These conclusions use the original-input data of the preceding construction; they do not infer additive component ranks or a gain at every later exponent.

### A finite residue pattern allowing every odd first-error moment to vanish

The distinction between simultaneous injectivity and residue-factor parity is real.
Consider only the finite residue pattern \(q=7\), \(T(x)=x\), and \(I=\{1,2\}\).
This paragraph does not assert that an original \(P\), still less a near-one original \(P\), supplies that \(T\).
The orbit consists of the six distinct masks \(J_a=\{a,2a\}\), \(1\le a\le6\), and
\[
                        z_{J_a}=(\xi^a+\xi^{2a})x.
                                                               \tag{OF9}
\]
In a residue field \(\mathbb F_8\), the six values \(u=\xi^a\) are precisely the elements other than zero and one.
The map \(u\mapsto u+u^2\) pairs \(u\) with \(u+1\); each pair remains in this six-element set and has a nonzero common image.
Thus the three distinct nonzero values in (OF9) each occur twice, so every positive power sum, in particular every odd one, vanishes.

The pairings can be seen explicitly.
If \(\xi^3+\xi+1=0\), the pairs of indices are
\[
                         \{1,3\},\quad\{2,6\},\quad\{4,5\}.
\]
At the other residue factor, represented by \(\xi^3\), they become
\[
                         \{1,5\},\quad\{2,3\},\quad\{4,6\}.
\]
These different pairings have no common two-element fiber, consistently with simultaneous injectivity.
They nevertheless give even fibers at both residue factors.
Accordingly, complete Galois descent and all-place injectivity alone do not rule out persistent cancellation of the first normalized Padé error.

### What this establishes for the original return

Equations (OF1)--(OF8) give exact tests on an actual original input, and isolate where first-level cancellation is automatic and where it is absent.
The finite example (OF9) shows that one cannot replace those tests by simultaneous injectivity.
It supplies no original-input realization, no higher binary digits and no minimum-rank assertion.

Even a fixed number of extra digits at every odd exponent would add only an \(O(1)\) term to the precision \(a(2t+1)+1\).
For a fixed original input this does not change its leading precision-to-rank ratio or the quadratic coefficient obtained by summing all Hankel valuation levels.
A number of extra digits growing proportionally with the approximation index, or a proved decrease of the genuinely joint approximation rank, would be materially different.
Neither has been derived here.
There is still no proof that putative near-one original inputs force a favorable frequency pattern, a favorable higher-digit pattern, or a favorable joint rank.
The unresolved task is to connect such actual arithmetic data to the same original all-root capacity comparison, rather than to substitute component-rank additivity or a finite residue-pattern model.

<a id="bad-reduction-pole-excess"></a>
## Fixed home of the bad-reduction rank bound and original control

The complete BR1--BR18 proof is now [C860 v6](../claims/Yin_C_G0860_v6.md#argument), with its [selected whole assessment](../claims/Yin_C_G0860_v6.md#decision-whole-independent-review-2026-11-04) and [independent R1076 v5 finding](../audits/reviews/Yin_R_G1076_v5.md#bad-reduction-whole).
The fixed proof retains all original degrees, infinity factors, exact errors, global integrality and same-determinant costs; the duplicate working proof is retired here.

<a id="bad-reduction-statement"></a>
Its [general statement](../claims/Yin_C_G0860_v6.md#bad-reduction-statement) gives the projective gcd lower bounds for every integral rational approximant, every integer precision, exact first-step rank and fixed-unit comparison.

<a id="bad-reduction-argument"></a>
The [full lower-bound argument](../claims/Yin_C_G0860_v6.md#bad-reduction-argument) preserves the homogeneous divisor count, including losses at infinity, without assuming good reduction or additive component ranks.

<a id="actual-quadratic-bad-reduction-control"></a>
The [actual quadratic control](../claims/Yin_C_G0860_v6.md#actual-quadratic-bad-reduction-control) has minimum-rank slopes between one third and two thirds and exact rank-one precision limit four.
It is an original nonrational power-stable input already above log2, not near-one supply or a sharp all-rank formula.
The preceding finite Laurent, common-component and orbit-frequency calculations remain at their stated author-working scopes; this fixed assessment does not independently review those separate arguments.

<a id="joint-pade-logarithmic-cancellation"></a>
## Fixed home of the logarithmic joint-error bound

The complete LC1--LC13 argument is now [C860 v7's number-field valuation lemma](../claims/Yin_C_G0860_v7.md#coefficientwise-valuation-lemma), with its [selected whole assessment](../claims/Yin_C_G0860_v7.md#decision-whole-independent-review-2026-11-04) and [independent R1076 v6 finding](../audits/reviews/Yin_R_G1076_v6.md#componentwise-pade-whole).
It retains the fraction-field Gauss valuation, nonexpansive derivatives, fixed scalar polynomial norm bound, Cramer argument and eventual dominance of the first harmonic.
Its fixed-number-field and nonconstant-ratio hypotheses remain essential.
The [constant-ratio control](../claims/Yin_C_G0860_v7.md#nonconstant-ratio-boundary) is retained there as well.

The former LC14--LC18 application to the common-component centers above is now a specialization of the [supplied original-orbit theorem](../claims/Yin_C_G0860_v7.md#supplied-original-orbit-application) whenever those actual hypotheses have been supplied.
C860 v7 proves that conditional application for arbitrary fixed equivariant centers; it does not independently review the separate AS construction or OF residue calculations retained above.
For those working centers the intended parameter is a=Lambda_q-2, with the same original function and full orbit.

<a id="joint-pade-pole-rank"></a>
## Fixed home of the componentwise pole-rank theorem

The complete PR1--PR8 proof is [C860 v7's geometric rank argument](../claims/Yin_C_G0860_v7.md#componentwise-pole-rank).
It gives rank equal to the sum of component degrees times their respective indices, up to a fixed bounded error, including independent indices without an automatic rational-descent assertion.
The proof retains geometric square-class independence, the exact accepted rank-zero ESS application, every moving pole, infinity and center factor, and the original lower bound deg(R_J)>=d|J|.
Ranks are not assumed to add before that proof.

<a id="componentwise-pade-family-profile"></a>
## Fixed home of the exact supplied-family certificate

The combined argument is [C860 v7's family profile](../claims/Yin_C_G0860_v7.md#componentwise-family-profile), under its supplied fixed centers and exact all-place depth.
With Delta=sum_J deg(R_J) and a=lambda-2, it proves r_s^fam=Delta*s/(2a)+O(log(s+2)) and B_h^fam=(a/Delta)h^2+O(h log(h+2)).
Finite exceptional indices, nonrationality and the complete same-original-determinant contour return are retained in that fixed proof.
This is the exact leading certificate of the stated componentwise family, not an upper bound on actual determinant valuations or a minimum over arbitrary joint rational approximants.
The separate question of genuinely different joint approximants remains open.

<a id="factorwise-pade-sharing"></a>
## Approximate basic factors before forming the mask products

This is author-working mathematics for Yin, without independent review.
The coordinating agent proposed the factorwise construction and checked the stronger old comparators in the actual benchmark.
The precision-varying-approximants contributor developed the shared-denominator, precision and return calculations; a separate contributor checked the even-exponent antipodal refinement.
The bounded reuse search found [C857 v2's binomial union denominator](../claims/Yin_C_G0857_v2.md#coherent-centers) and [C860 v5's sum of maskwise Padé degrees](../claims/Yin_C_G0860_v5.md#multiple-radical-boundary), but no retained construction which first Padé-approximates the basic factors and then forms the mask products.
The distinction matters: [C860 v7](../claims/Yin_C_G0860_v7.md#statement) determines the maskwise family, not the product-sum family constructed here.
The positive result below is a paid upper bound for its rank, not an exact rank or all-rational minimum.

### The shared-denominator calculation

Keep the original cyclotomic Galois coefficient field \(K=\mathbb Q(\zeta_q)\), for a fixed odd prime \(q\).
Let \(\mathscr V\) be a finite set of basic factors, permuted by \(\operatorname{Gal}(K/\mathbb Q)\).
For each \(v\in\mathscr V\), let \(Y_v\) be a normalized integral germ with coefficients in \(K\), and let \(A_{v,t}\in K(x)\) be normalized rational approximants, integral at every place above two, such that
\[
 v_2(Y_v-A_{v,t})\ge 2at+b,\qquad
 \rho(A_{v,t})\le \delta_vt+c_v.
                                                               \tag{SF1}
\]
Here \(a\) and every \(\delta_v\) are positive integers, \(b\) is an integer, and the \(c_v\) are fixed nonnegative integers.
The valuation is simultaneous at all two-adic places, and both the germs and approximants are equivariant under the indicated permutation.
Every constant coefficient is one.
Assume the actual original target germs admit factorizations
\[
             G_J=H_J\prod_{v\in E_J}Y_v,\qquad J\in O.
                                                               \tag{SF2}
\]
Here \(E_J\subseteq\mathscr V\), \(\sigma(E_J)=E_{\sigma J}\), and the fixed centers \(H_J\in K(x)\), with \(H_J(0)=1\), are equivariant integral units at all places above two.
Use only factors which occur in some \(E_J\).
Each \(E_J\) is a set: repeated quadratic factors must already have been absorbed as exact rational square factors in \(H_J\).
Then
\[
       F_t=\sum_{J\in O}H_J\prod_{v\in E_J}A_{v,t}
\]
belongs to \(\mathbb Q(x)\cap\mathbb Z_2[[x]]\) and satisfies
\[
 f-F_t\in2^{2at+b}\mathbb Z_2[[x]],\qquad
 \rho(F_t)\le t\Xi+O(1),\qquad
          \Xi=\sum_{v\in\mathscr V}\delta_v,\qquad
          f=\sum_{J\in O}G_J.
                                                               \tag{SF3}
\]
The constants fix the original input and the factorization.

For the precision, subtract two products one factor at a time.
Every summand in the telescoping difference contains one factor \(Y_v-A_{v,t}\), with all other factors integral.
The fixed centers and the orbit sum introduce no loss.

For the rank, write each \(A_{v,t}=P_{v,t}/Q_{v,t}\) in reduced form with \(Q_{v,t}(0)=1\).
The denominator lemma of C860 v5 applies in each completion, so these numerator and denominator polynomials are integral at all places above two, with degrees at most \(\delta_vt+c_v\).
Their normalized reduced forms are equivariant by uniqueness.
Choose a fixed common denominator \(Q_H\), with constant coefficient one, for all \(H_J\), by taking the product of their normalized denominators.
It is likewise Galois invariant and integral at the two-adic places.
Set
\[
 \begin{split}
 Q_t&=Q_H\prod_{v\in\mathscr V}Q_{v,t},\\
 P_t&=\sum_{J\in O}(Q_HH_J)
            \prod_{v\in E_J}P_{v,t}
            \prod_{v\notin E_J}Q_{v,t}.
 \end{split}                                                    \tag{SF4}
\]
These are actual polynomial expressions, with \(F_t=P_t/Q_t\).
Both are Galois invariant; the denominator has constant term one.
The numerator degrees of the fixed polynomials \(Q_HH_J\), including any polynomial parts of the centers, contribute only a fixed constant.
Thus \(\deg P_t,\deg Q_t\le t\Xi+O(1)\), proving (SF3).
Every basic denominator occurs once in (SF4), regardless of how many masks use it.
There is no hidden exponent \(|O|\), division by a stabilizer order, or assumption that the sum's actual rank equals this bound.

### The actual precision has only a logarithmic excess

The applications below have a common exponent \(n=2t+1\) or \(n=2t\) and exact relative formulas
\[
       \frac{A_{v,t}}{Y_v}
                    =\frac{1+w_v^n}{1-w_v^n},
 \qquad
       \min_{v\in\mathscr V}v_{\mathfrak p}(w_v)=a>0
                         \quad\text{at every }\mathfrak p\mid2.
                                                               \tag{SF5}
\]
Each \(w_v\) is a fixed series in \(xK[[x]]\), integral at the selected place, and the ratios \(w_v/w_u\) are nonconstant for distinct basic factors.
Put
\[
                         B_v=\sum_{\substack{J\in O\\v\in E_J}}G_J.
\]
This is a nonzero integral series: its constant coefficient is the positive number of masks containing \(v\).
The general number-field lemma [C860 v7 (LC1)--(LC13)](../claims/Yin_C_G0860_v7.md#coefficientwise-valuation-lemma) therefore gives
\[
       v_{\mathfrak p}\!\left(
            \sum_v\frac{B_vw_v^n}{1-w_v^n}\right)
                           =an+O(\log(n+2)).
                                                               \tag{SF6}
\]
Indeed every \(B_v\) and \(w_v\) has coefficients in the same fixed number field, and the amplitudes need not have odd constant coefficients for that lemma.

Expand each product in (SF2) using
\((1+w_v^n)/(1-w_v^n)=1+2w_v^n/(1-w_v^n)\).
The first part of \(f-F_t\) is
\[
                        -2\sum_v\frac{B_vw_v^n}{1-w_v^n}.
\]
Every remaining term contains at least two of the basic errors and has depth at least \(2an+2\).
For sufficiently large \(n\), this is strictly greater than the depth of the first part in (SF6).
The ultrametric equality proves
\[
                v_2(f-F_t)=an+1+e_t,\qquad
                         0\le e_t\le C\log(n+2).
                                                               \tag{SF7}
\]
Rational descent allows the valuation to be read at any place above two.
This is an exact leading precision assertion for the new family.
It does not turn the upper rank bound (SF3) into an equality.

### Direct basic factors when the canonical reduced class vanishes

Use the original \(P,U,V\) and the coherent integer \(B,C\) of C857 v2, and write
\[
 S_j=\frac{C(\zeta_q^jx)}{B(\zeta_q^jx)},\qquad
 R_j=\left(\frac{VB^2}{UC^2}\right)(\zeta_q^jx).
\]
When the canonical Artin--Schreier representative is \(c=0\), one has
\[
 L_*:=v_2(R_0-1)\ge3.
\]
Every rotation has exactly that simultaneous depth.
For an arbitrary nonempty mask orbit, set \(\mathscr S=\bigcup_{J\in O}J\), \(s=|\mathscr S|\), and use the basic factors \(Y_j=\sqrt{R_j}\), \(j\in\mathscr S\).
The exact original identity is
\[
                   G_J=\left(\prod_{j\in J}S_j\right)
                                      \prod_{j\in J}\sqrt{R_j}.
\]
Replacing each basic square root by its odd Padé approximant \(\pi_t(R_j)\) gives (SF3) with
\[
 a=L_*-2,\quad b=a+1,\qquad
 \Xi_{\rm direct}=\sum_{j\in\mathscr S}\deg R_j.
                                                               \tag{SF8}
\]
The basic square classes are the original single-rotation classes, so their Cayley ratios are nonconstant by C860 v7's geometric argument.
Equivariance and the full used rotation set give the same minimum depth at every residue place.
Thus (SF7) also applies.
For the canonical degree-\(e\) lifts, \(e\le d/2\),
\[
                       ds\le\Xi_{\rm direct}\le s(d+2e).
\]
The lower bound preserves the original odd branch valuations, and the upper bound is the actual reduced-map degree bound.
Compared with C857's already retained unreduced binomial union-denominator bound \(s(d+2e)\), the same paid degree bound now has twice the leading precision.
This does not assert a factor-two improvement over every possible cancellation already present in an old exact binomial slope.

### Shared ratios in the common-AS construction

Keep (AS1)--(AS6), let \(I\) be a nonempty proper even mask, and put
\[
 k=|I|,\qquad \varepsilon=\boldsymbol1_{\{0\in I\}},\qquad
 s=|\mathscr S|,\qquad a=\Lambda_q-2\ge1.
\]
Use the basic ratios
\[
               T_j=R_j/R_0,\qquad j\in\mathscr S\setminus\{0\}.
\]
Their common simultaneous depth is exactly \(\Lambda_q\), and the original factorization is
\[
                 G_J=H_J\prod_{j\in J\setminus\{0\}}\sqrt{T_j},
                 \qquad H_J=S_JR_0^{k/2}.
                                                               \tag{SF9}
\]
Every branch is normalized at zero, so this identity has no sign ambiguity.
The index set, rational centers and basic Padé approximants are Galois equivariant.
The shared-denominator construction gives
\[
 \begin{split}
 F_t^{\rm star}
   &=\sum_{J\in O}H_J
           \prod_{j\in J\setminus\{0\}}\pi_t(T_j),\\
 v_2(f-F_t^{\rm star})&\ge a(2t+1)+1,\qquad
 \rho(F_t^{\rm star})\le t\Xi_{\rm star}+O(1),\\
 \Xi_{\rm star}
   &=\sum_{j\in\mathscr S\setminus\{0\}}\deg T_j .
 \end{split}                                                    \tag{SF10}
\]
The factors \(T_j\) have distinct original square classes \(\{0,j\}\).
Consequently their Cayley ratios are nonconstant, and the complete actual precision is given by (SF7).

All nonzero positions occur in the full orbit union, so \(s-\varepsilon=q-1\).
Every nonzero \(j\) has the same map degree \(\delta_b=\deg T_j\), by Galois invariance.
The original private \(U_j\)-poles and \(V_0\)-poles give the lower bound below, while the displayed numerator and denominator of \(R_j/R_0\) give the upper bound:
\[
 2d\le\delta_b\le2(d+e_B+e_C),\qquad
 2d(s-\varepsilon)\le\Xi_{\rm star}
                \le2(d+e_B+e_C)(s-\varepsilon).
                                                               \tag{SF11}
\]
The auxiliary rotation zero is not silently added to the original contour.
It cancels in the exact identity (SF9), so the target \(f\) and its original slit set stay unchanged.
All degree costs of the auxiliary ratios are nevertheless retained in \(\Xi_{\rm star}\).

For comparison, the maskwise Padé presentation with these same centers has exact leading rank
\[
       \Delta_{\rm mask}
          =\sum_{J\in O}\deg\widetilde R_J
          \ge2d|O|(k-\varepsilon).
\]
The bound counts the original \(U_j\)-poles for \(j\in J\setminus\{0\}\) and the original \(V_0\)-poles of order \(k-\varepsilon\).
Writing \(h=|\operatorname{Stab}(I)|\) and
\(\nu=(k-\varepsilon)/h=|O|(k-\varepsilon)/(q-1)\), one obtains
\[
       \frac{\Delta_{\rm mask}}{\Xi_{\rm star}}
                   \ge\frac{\nu}{1+(e_B+e_C)/d}.
\]
For canonical binary lifts this is at least \(\nu/2\), so the saving relative to that maskwise presentation can grow with orbit incidence.
The stronger pre-existing union-binomial competitor must still be compared separately; the benchmark below does so.

### An equivariant antipodal-pair refinement

Suppose the even mask is invariant under \(j\mapsto-j\).
It then excludes zero and is a union of unordered antipodal pairs.
Let \(e=\{j,-j\}\), and use the exponent-indexed Cayley rational function
\[
 \Theta_{2t}(Z)=
   \frac{\sum_{r=0}^{t}\binom{2t}{2r}Z^r}
        {\sum_{r=0}^{t-1}\binom{2t}{2r+1}Z^r},
                         \qquad t\ge1.
\]
This differs from the degree-indexed notation \(\pi_t=\Theta_{2t+1}\).
Reversing each coefficient list proves
\[
                         \Theta_{2t}(Z)=Z\Theta_{2t}(1/Z).
                                                               \tag{SF12}
\]
Consequently
\[
 A_{e,t}=S_jS_{-j}R_{-j}
                         \Theta_{2t}(R_j/R_{-j})
                                                               \tag{SF13}
\]
is independent of the choice of orientation of \(e\).
It is therefore permuted correctly by every Galois multiplier.
Using odd exponents in (SF13) would not have this orientation invariance; it cannot simply be assumed.

For \(T=R_j/R_{-j}\), set \(y=\sqrt T\), \(u=(1+y)/2\), \(v=(1-y)/2\).
After the common normalization by \(2^{2t-1}\), the numerator and denominator of \(\Theta_{2t}(T)\) are
\[
                   u^{2t}+v^{2t},\qquad
                   (u^{2t}-v^{2t})/y.
\]
The denominator is an integral power-series unit, and
\[
                   \Theta_{2t}(T)-y
                        =\frac{2v^{2t}}{(u^{2t}-v^{2t})/y}.
\]
Thus (SF13) is integral at all two-adic places and has exact common error depth \(2at+1\) relative to \(G_jG_{-j}\).
There is no additional division-by-two loss.
At \(t=1\), it is the visibly symmetric expression
\(S_jS_{-j}(R_j+R_{-j})/2\).

For any distinct \(j,l\),
\[
              R_j/R_l=(R_{j-l}/R_0)(\zeta_q^l x).
\]
Hence every such ratio has the same degree \(\delta_b\).
The pair approximant has rank at most \(t\delta_b+O(1)\), with its fixed rational multiplier fully charged.
Multiplying the pair approximants occurring in each mask, and then summing over the orbit, uses each pair denominator once.
The complete orbit uses all \((q-1)/2\) pairs, so
\[
 \begin{split}
 v_2(f-F_t^{\rm pair})&\ge2at+1,\qquad
 \rho(F_t^{\rm pair})\le t\Xi_{\rm pair}+O(1),\\
 \Xi_{\rm pair}&=\frac{q-1}{2}\delta_b
                    =\frac12\Xi_{\rm star},\\
 d(q-1)&\le\Xi_{\rm pair}
                    \le(d+e_B+e_C)(q-1).
 \end{split}                                                    \tag{SF14}
\]
For these pair factors, changing orientation sends the Cayley parameter \(w\) to \(-w\); the even exponent removes that sign.
Distinct pairs have distinct original quadratic square classes, so the nonconstant-ratio hypothesis for (SF6) holds.
The Galois action permutes the parameters up to these harmless signs and gives the same local minimum at every place.
Thus (SF7) also gives the actual leading precision for this pair family.

### An actual benchmark, including the stronger old competitors

Take
\[
 P(t)=t^2-3t+1,\quad \alpha=(3+\sqrt5)/2,\quad
 U=1-7x+x^2,\quad V=1-47x+x^2,\quad B=C=1.
\]
This is an irreducible reciprocal power-stable unit: its two positive conjugates are \(\alpha,\alpha^{-1}\), and their positive powers remain distinct.
Its total measure is \(\log\alpha>\log2\), so it is already outside the small-measure gap range.
The identity \(V-U=-40x\) gives \(c=0\) and \(L_*=3\).
The coefficient of \(x\) in \(\log(V/U)\) is \(-40\), so \(\Lambda_q=3\) for every odd prime.
All the relevant constructions have \(a=1\).

For \(q\ge5\), choose \(I=(\mathbb Z/q\mathbb Z)^\times\setminus\{1,2\}\).
Then \(k=q-3\) is even, its multiplier stabilizer is trivial, \(|O|=q-1\), and \(s=q-1\).
Indeed a multiplier preserving the removed pair either fixes it, hence is one, or swaps it, which would force \(4=1\bmod q\) and hence \(q=3\).
The same original \(f=\sum_{J\in O}G_J\) has the following paid comparisons.
This chosen mask is not negation invariant, so the antipodal-pair refinement is not a row of this comparison.

| Family | Leading rank or paid upper rank | Guaranteed leading precision | Guaranteed coefficient of \(h^2\) in \(v_2(\mathcal D_h(f))\) |
| --- | --- | --- | --- |
| Uncentered maskwise Padé, \(H_J=1\) | Exact \(2(q-1)(q-3)t+O(1)\) | At least \(2t+2\) | \(1/[2(q-1)(q-3)]\) |
| Recentered maskwise Padé, \(H_J=R_0^{k/2}\) | Exact \(4(q-1)(q-3)t+O(1)\) | At least \(2t+2\) | \(1/[4(q-1)(q-3)]\) |
| Shared star-ratio products | At most \(4(q-1)t+O(1)\) | At least \(2t+2\) | \(1/[4(q-1)]\) |
| Direct shared basic products | At most \(2(q-1)t+O(1)\) | At least \(2t+2\) | \(1/[2(q-1)]\) |
| Old uncentered union-binomial trace | Exact \(2(q-1)t+O(1)\) | At least \(t+2\) | \(1/[4(q-1)]\) |

The first two exact rank statements are C860 v7 applied to their different supplied centers.
Their depths are exactly three: the original logarithm has depth three and its \(x\) coefficient is multiplied by a nonempty proper mask value, which is not divisible by two at all residue factors simultaneously.
For the recentered presentation, the even-cardinality subtraction gives the same conclusion.
The radicand degrees are respectively \(2k\) and \(4k\), by the original private poles.
Each basic \(R_j\) has degree two, and each ratio \(R_j/R_0\), \(j\ne0\), has degree four.
The last row is the already adopted binomial union-denominator rank from C860 v4 with the original scalar precision.
No new arithmetic premise comes from a finite numerical experiment.

The shared star family therefore saves a factor \((q-3)/2\) relative to the stronger uncentered maskwise Padé comparator, and the direct family saves a factor \(q-3\), at the level of these leading paid rank coefficients.
This is a genuine different joint family, and the relative saving can be unbounded as \(q\) varies.
The stronger old union-binomial certificate already equals the star certificate in this benchmark.
The direct family only doubles that old certificate.
The comparison takes the approximation limit with each input and prime fixed; no uniform finite-index dominance as \(q\) varies is asserted.
An unbounded relative saving against a weaker comparator is not new Lehmer coverage, and the absolute cost here still grows with \(q\).

### Same-original return and the remaining questions

For any of the displayed uniform-depth families, (SF3) and the all-level elementary-divisor comparison give the guaranteed quadratic coefficient \(a/\Xi\).
The target \(f\), all its original conjugates and its used slit set are unchanged, so C855's actual contour gives
\[
                 \frac{a\log2}{\Xi}
                         \le\inf_{\tau\ge0}\Phi_s(\tau),
        \qquad E_2\ge\frac{a\log2}{5s\Xi},
        \qquad m(P)\ge\left(\frac{a\log2}{5s\Xi}\right)^{1/2}.
                                                               \tag{SF15}
\]
These are constructive lower-bound certificates based on the paid upper rank.
Neither an exact rank for the product-sum nor an upper bound on actual Hankel divisibility is inferred.

For the common-AS star family, (AS7) and (SF11) show that this displayed coarse total-measure certificate vanishes uniformly on hypothetical near-one sequences with both \(\log\|B\|_1=o(d)\) and \(\log\|C\|_1=o(d)\).
For canonical binary lifts the numerator budget is \(O(\log d)\), while \(\Xi_{\rm star}\ge2d(s-\varepsilon)\).
For the antipodal family, \(s=q-1\) and \(\Xi_{\rm pair}\ge d(q-1)\) give the same vanishing conclusion.
For the direct \(c=0\) family, C860 v4's original-center budget and \(\Xi_{\rm direct}\ge ds\) give the corresponding conclusion when \(\log\|B\|_1=o(d)\).
These statements concern the displayed coarse certificates only, not all uses of the actual contour or the new family's still-unknown exact rank.

The antipodal refinement is exactly twice the star certificate where it applies.
For canonical binary lifts, its ratio to the existing common-AS union-binomial coefficient obeys
\[
            1+\frac{k}{q-1}
                \le\frac{2\kappa_{\rm AS}}{\Xi_{\rm pair}}
                \le8,
\]
using the paid bounds (AS16).
Thus that improvement over the existing competitor stays bounded.
The star comparison with the same competitor is likewise bounded by four from above.
These finite-factor changes do not establish new unrestricted total-gap coverage.

The construction isolates a concrete remaining problem: determine the actual rank or a sharper denominator cancellation for these product-sums, and connect an improved paid ratio to genuinely uncovered near-one inputs.
A square-class basis or ratio tree is usable only with its actual rational corrections, integral precision and Galois equivariance verified; an arbitrary binary basis does not automatically supply an equivariant approximant.
No such further optimization, sharp all-rational minimum for these several-mask sums or original near-one supply is proved in this working construction.

<a id="coprime-block-minimum-rank"></a>
## Exact joint minimum rank for coprime residual blocks

The exact coprime-block minimum over all rational approximants, its \(\mathbb Q_2\)-to-\(\mathbb Q\) realization, the original squarefree-reduction dichotomy, normalized factor lifting, exact resultant depth budget and same-germ contour return are fixed in [C860 v8's statement](../claims/Yin_C_G0860_v8.md#statement) and [complete CB1--CB20 argument](../claims/Yin_C_G0860_v8.md#argument).
Its [selected adoption](../claims/Yin_C_G0860_v8.md#decision-whole-independent-review-2026-11-04) uses the [independent whole finding R1076 v7](../audits/reviews/Yin_R_G1076_v7.md#coprime-block-profile-whole), with the actual source, native-control and original-input limits retained there.

The continuing arithmetic questions are the minimum rational rank for several original mask radicals summed together, and the repeated-reduction case after canonical rational recentering.
Any useful improvement must supply its actual original near-one inputs and pay their full precision, rank and complex-contour costs.
The fixed theorem determines this single germ's rational-approximation certificate; it does not determine actual Hankel valuations or preclude additional arithmetic divisibility or sharper use of the original contour.
The unrestricted positive total logarithmic Mahler gap remains unresolved.

<a id="actual-hankel-first-residue"></a>
## Actual Hankel valuations on a nonrational first residue layer

The complete actual-valuation statement is fixed in [C858 v2](../claims/Yin_C_G0858_v2.md#statement), under its [selected whole assessment](../claims/Yin_C_G0858_v2.md#decision-whole-independent-review-2026-11-05) and [independent R1074 v3 finding](../audits/reviews/Yin_R_G1074_v3.md#actual-hankel-residue-whole).
It gives exact linear valuations along infinitely many indices whenever the first residue layer is nonrational, the original nonzero dyadic class without a squarefree premise, and unit determinants at infinitely many indices for each good odd prime.
The fixed proof retains the actual field-valued Kronecker source, shifted indexing, complete integrality and prime/liminf qualifications.

[C858 v3](../claims/Yin_C_G0858_v3.md#decision-whole-independent-review-2026-11-05) proves that synchronization by an exact shifted-kernel and polynomial-lattice argument, rather than by intersecting arbitrary infinite sets.
For a fixed finite set of nonrational odd residues and any nonzero dyadic class, all positive multiples of an input-dependent period give zero odd valuations and the exact linear dyadic valuation.
The remaining questions concern rational-residue primes, changing prime divisors, different selected index sets or determinants, and genuinely different original-input income beyond that local conclusion.
The original unrestricted G0001 objective remains unresolved.

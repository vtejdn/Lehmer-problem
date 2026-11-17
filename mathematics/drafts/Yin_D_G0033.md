---
author: Yin
---

# Why real-conjugate height bounds do not improve under integral root monomials

This is continuing author-side work for [G0001](../tasks/Yin_T_G0001_v1.md#contract), not a fixed claim or an independent review.
The agent-S researcher derived the real-conjugate fraction calculation and its consequence for the usual triangle-inequality transfer.
The coordinating researcher proposed using the actual height ratio instead, through the full-flip height lower bound.
The argument below proves that stronger obstruction and extends it to the even-flip group by character orthogonality.
The [Garza source inspection](../audits/literature/Gar07/Yin_U001.md#real-conjugates) supplies the exact classical bound and resolves a printed logarithm discrepancy from its proof.

<a id="statement"></a>
## Exact scope of the comparison

Let \(P\in\mathbb Z[X]\) be monic, irreducible and reciprocal of degree \(2m\), with nontorsion unit roots.
Choose representatives \(x_1,\ldots,x_m\) of its inverse pairs, and write \(\alpha=x_1\), \(\mu=\log M(P)=2m h(\alpha)>0\).
The splitting-field group \(G\) acts by signed permutations of the representatives; its permutation image \(H\) on the \(m\) pairs is transitive.
Assume either that \(G\) contains all independent pair inversions, or that \(m\ge3\) and \(G\) contains all inversions of an even number of pairs.
For an integer vector \(a\ne0\), put
\[
 \beta_a=\prod_{i=1}^m x_i^{a_i},\qquad
 S=\{i:a_i\ne0\},\qquad k=|S|.
\]
Then, without any signature assumption,
\[
       \|a\|_\infty h(\alpha)\le h(\beta_a)
                              \le\|a\|_1h(\alpha).                 \tag{1}
\]
In particular \(\beta_a\) is nontorsion.
The lower constant is sharp, as coordinate vectors already give equality.

Now suppose every exterior root of \(P\) is real, and let \(E\) be the set of its \(e\ge1\) nonneutral pair labels.
Let \(R(\gamma)\) denote the fraction of the distinct conjugates of an algebraic number \(\gamma\) that are real.
The exact fraction is
\[
 R(\beta_a)=\frac{\#\{h\in H:hS\subset E\}}{|H|}
                          \le\frac em=R(\alpha).                  \tag{2}
\]
If \(H=S_m\), this is
\[
                       R(\beta_a)=\frac{\binom e k}{\binom m k},  \tag{3}
\]
with numerator zero for \(k>e\).

Define \(f(0)=0\) and \(f(R)=(R/2)\operatorname{arsinh}(2^{-1/R})\) for \(0<R\le1\).
Garza's bound is \(h(\gamma)\ge f(R(\gamma))\) for nonzero nontorsion \(\gamma\).
Put \(r_a=h(\beta_a)/h(\alpha)\), its actual ratio rather than a triangle-inequality bound.
The height inequality obtained by applying Garza to \(\beta_a\) and converting with this ratio is
\[
       h(\alpha)\ge\frac{f(R(\beta_a))}{r_a},\qquad
       \frac{f(R(\beta_a))}{r_a}\le f(e/m).                        \tag{4}
\]
Thus even exact knowledge of the monomial's height cannot improve the lower bound already obtained by applying Garza directly to \(\alpha\).
A coordinate monomial attains equality in the comparison of the two lower bounds.
The weaker transfer \(h(\beta_a)\le\|a\|_1h(\alpha)\) has the same obstruction.

<a id="height"></a>
## Signed averaging proves the height lower bound

Let \(F\) be the splitting field, embedded in \(\mathbb C\).
For any unit \(u\in F\), its average logarithm over \(G\) is zero, and every embedding of \(\mathbb Q(u)\) has the same number of extensions to \(F\).
Consequently
\[
                  2h(u)=\frac1{|G|}\sum_{g\in G}|\log|gu||.        \tag{5}
\]
This uses the ordinary absolute height; no chosen-embedding height is substituted for it.

Let \(N\) be the full sign group, or the even sign group under the second hypothesis.
For a uniformly chosen \(\varepsilon\in N\), the coordinate characters satisfy
\[
                 \mathbb E(\varepsilon_i\varepsilon_j)=\delta_{ij}.
                                                                    \tag{6}
\]
In the even case, for \(i\ne j\) choose a third coordinate and flip it together with \(i\); this pairs signs with opposite values of \(\varepsilon_i\varepsilon_j\).
The argument explains the restriction \(m\ge3\), rather than assuming full statistical independence of even signs.
For any real vector \(v\), (6) gives
\[
 |v_j|=\left|\mathbb E\left[\varepsilon_j
                    \sum_i\varepsilon_i v_i\right]\right|
                           \le\mathbb E\left|\sum_i\varepsilon_i v_i\right|.
                                                                    \tag{7}
\]

For fixed \(g\in G\), use \(v_i=a_i\log|g x_i|\) in (7).
Right multiplication of a uniform element of \(G\) by a uniform sign element preserves its distribution.
Averaging (7) over \(g\) and using (5) twice yields
\[
 2h(\beta_a)\ge |a_j|\frac1{|G|}\sum_g|\log|g x_j||
                                      =2|a_j|h(\alpha).
\]
Choose \(j\) with maximal \(|a_j|\) to prove the lower half of (1).
The upper half is the ordinary product height inequality and conjugacy invariance.
This proof applies to real and nonreal exterior roots alike and to any initial complex embedding.

<a id="real-fraction"></a>
## The reality condition is a condition on support

First the chosen representatives are multiplicatively independent modulo torsion.
With full flips, apply the inversion of coordinate \(i\) to a torsion relation \(\prod_i x_i^{c_i}\) and divide to make \(x_i^{2c_i}\) torsion; hence \(c_i=0\).
With even flips, the pairs \(\{i,j\},\{i,k\},\{j,k\}\) for three distinct labels give three such relations.
Multiplying the first two and dividing by the third makes \(x_i^{4c_i}\) torsion, again forcing \(c_i=0\).
Clearing denominators gives independence also for rational exponent relations modulo torsion.

Assume now the all-real-exterior hypothesis.
Ordinary complex conjugation \(\tau\) fixes each representative on \(E\) and inverts each representative on its complement.
Indeed a real conjugate cannot equal \(1\) or \(-1\), and every remaining pair lies on the unit circle.
If \(ga\) denotes the signed exponent vector of \(g\beta_a\), reality means
\[
                     \tau(g\beta_a)=g\beta_a.
\]
Independence shows that this holds exactly when the exponent vector has zero entries outside \(E\), or equivalently \(gS\subset E\).
Uniform elements of \(G\) count each distinct conjugate of \(\beta_a\) equally often, and their permutation images are uniform in \(H\).
This proves the equality in (2).
For any fixed \(i\in S\), the event \(hS\subset E\) implies \(hi\in E\), whose probability is \(e/m\) by transitivity.
Under \(H=S_m\), the set \(hS\) is uniform among the \(k\)-subsets, proving (3).
The exact formula also holds for any \(k\)-homogeneous permutation image.

Multiplication of \(\beta_a\) by an arbitrary root of unity does not improve the conclusion in (4).
The height is unchanged, and in a common finite Galois extension reality still forces the exponent class to be fixed by complex conjugation.
Thus its real-conjugate fraction is at most the right side of the equality in (2), although equality can fail for a nonrational torsion multiplier.

<a id="barrier"></a>
## The classical endpoint bound and the remaining gap

The function \(f\) is strictly increasing on \((0,1]\): both \(R\) and \(\operatorname{arsinh}(2^{-1/R})\) are positive and strictly increasing.
Since \(a\) is a nonzero integer vector, (1) gives \(r_a\ge\|a\|_\infty\ge1\).
Together with (2), these facts prove (4), including \(R(\beta_a)=0\).
No upper bound, asymptotic estimate or approximate evaluation of \(r_a\) is used.

For comparison, applying Garza directly gives the classical degree-dependent inequality
\[
                       \mu\ge e\operatorname{arsinh}(2^{-m/e}).     \tag{8}
\]
In this reciprocal all-real-exterior case, the same expression follows from the two integer endpoint evaluations.
Choose exterior representatives \(|x_i|=e^{\ell_i}\) with \(\ell_i>0\), and write neutral representatives as \(e^{i\theta_j}\).
Their pair contributions give
\[
 1\le |P(1)P(-1)|
   =4^m\prod_{i\in E}\sinh^2\ell_i
                    \prod_{j\notin E}\sin^2\theta_j
   \le4^m\sinh^{2e}(\mu/e).                                      \tag{9}
\]
The last step uses \(\sin^2\theta_j\le1\) and concavity of \(\log\sinh\) on the positive axis.
Solving (9) is exactly (8); this is a source comparison, not a new lower bound.
Growing exterior count alone does not make its right side stay positive: for example the numerical regime \(e=\lfloor\sqrt m\rfloor\) makes it tend to zero.
This observation asserts compatibility of parameters with (8), not existence of an integral polynomial sequence with shrinking measure.

The [radial discriminant estimate](../claims/Yin_C_G0345_v280.md#statement) and the [local ramification fractions](../claims/Yin_C_G0345_v275.md#statement) use additional arithmetic inputs and are not consequences of (4).
The [earlier Cayley-coordinate sign averages](../claims/Yin_C_G0866_v3.md#argument) concern additive transformations and their integer norms, not the real fractions of root monomials computed here.
The [signed-product reduction](../claims/Yin_C_G0345_v304.md#statement) controls exterior count and measure cost in a radical saturation; it does not assert that its selected ordinary product improves a real-conjugate height estimate.
The present comparison explains that specific limitation when full or even pair flips are available.

The unresolved problem is still a direct positive measure bound at increasing degree in the possible shrinking regime, or an actual construction in that regime.
Equation (4) excludes one amplification mechanism; it does not exclude stronger estimates using neutral angles, integer values beyond the two endpoints, ramification, additive expressions, or other units in the splitting field.
It also does not cover radical exponents with denominators: for \(y^N=\zeta\beta_a\), one has \(h(y)=h(\beta_a)/N\), and the integer normalization \(\|a\|_\infty\ge1\) no longer bounds the height ratio of \(y\) by one.
The [prime-half-degree family](../claims/Yin_C_G0345_v306.md#statement) supplies a separate actual obstruction to bounded-exterior radical supply below the plastic number; its limiting measure is greater than one, and it does not fill this remaining direct-gap obligation.

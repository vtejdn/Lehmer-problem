---
author: Yin
---
# Independent review of dyadic Pade approximation and minimum rational rank

Review act: 2026-11-04T21:03 UTC.
The human record author is Yin.
This is a separately organized whole-proof agent review of the frozen [C0860v5 statement](../../claims/Yin_C_G0860_v5.md#pade-statement) and [complete argument](../../claims/Yin_C_G0860_v5.md#argument), including P1--P21, both boundary examples and the original-input and multiple-radical consequences.
The reviewer did not participate in substantive proof development and received no development dialogue, proposing-agent mathematical explanation, generation notes or previous verdict on the new proof.
The fixed candidate, necessary fixed dependencies and selected original source passages were read directly.
The final bounded source clarification identifying the two Kouba recurrence errors was also checked against the original; it changes no statement or P1--P21 argument.
The candidate's own contributor-check and provenance paragraphs were visible but supplied no review evidence.
Initial checks of the candidate preceded consultation of earlier dependency findings to delimit their applicable scope.
No rolling Draft or temporary development material was consulted, and no substantive project-proof repair was supplied.
The candidate had no selected assessment during this review.

## Earlier evidence remains fixed

The [R1076v1 finding](Yin_R_G1076_v1.md#precision-budget-whole) remains a review of C0860v1 A--E, the [v2 finding](Yin_R_G1076_v2.md#mask-depth-whole) remains a review of C0860v2 M1--M9, and the [v3 finding](Yin_R_G1076_v3.md#fixed-center-whole) remains a review of C0860v4 A--E.
Their dates, exact inputs, relationships, accepted-source limits and historical adoptions are unchanged.
None supplies review coverage of the new minimum-rank assertion by itself.
This same-topic physical version retains the actually performed new inspection without copying or replacing the earlier findings.
The old fixed-center theorem is reused only for the formal rank interface and the final Part E comparison; its entire general cancellation proof is not represented as newly re-audited here.

<a id="pade-minimum-rank-whole"></a>
## Whole Pade and minimum-rank finding

**Finding:** no unresolved mathematical gap was found in the complete C0860v5 statement and argument under the exact supplied hypotheses and source limits recorded here.
The proof establishes the integral explicit approximants, exact dyadic depths and ranks, the minimum over all integral rational Taylor series under P3, the fixed-unit comparison, the Cayley composition identity, the conditional original single-radical return and the stated multiple-radical upper bound.
The good-reduction and single-radical restrictions are essential to the minimum-rank conclusion.
The two incorrect intermediate recurrence displays in the cited Kouba source, identified below, are not premises of the project proof and do not invalidate its direct algebra.
This review selects no Claim assessment or Task decision and is not a completion review of G0001.

### Normalization, exact error and rational-map degree

The scaled-binomial valuation from C0860v1 is valid over the coefficient ring used here: for an index \(k\ge1\), its value is \(ak+s_2(k)\), where \(a=\lambda-2\ge1\).
The first term has depth \(a+1\), and every later term has at least one extra digit.
Since \(z(0)=0\), every formal coefficient receives only finitely many binomial contributions.
Thus \(y\) is integral, and \((y+1)/2\) is an integral unit congruent to one modulo two.
The identity \((y-1)(y+1)=2^\lambda z\), together with the nonzero reduction of \(z\), gives the claimed exact depth of \(y-1\).

Writing \(u=(1+y)/2\) and \(v=(1-y)/2\), one has \(uv=-2^a z\) and hence P7, including the exact normalized reduction.
The even and odd parts of \((1+y)^{2t+1}\) give P8 with precisely the normalization \(2^{-2t}\) in P1.
Both expressions are integral units with constant coefficient one and reduction one.
Multiplying by \(D^t\) clears all rational-function denominators; it gives polynomials of degree at most \(t\delta\).
Their Taylor integrality is their polynomial coefficient integrality, establishing P2's first line without assuming that the univariate polynomials themselves are integral over \(\mathbb Z_2\).

Subtracting P8 gives P9 exactly.
Its unit denominator cannot change the coefficientwise depth, so the error depth is \(a(2t+1)+1\) and the normalized reduction is \(\overline z^{\,2t+1}\ne0\).
This is a coefficientwise valuation statement, not just the source's order of vanishing in its argument variable.
At a common zero of \(p_t,q_t\), a chosen square root of that zero would force both \((1+y_0)^{2t+1}\) and \((1-y_0)^{2t+1}\) to vanish; the separate case \(y_0=0\) is excluded by \(p_t(0)\ne0\).
Thus the pair is reduced, both degrees are \(t\), and its rational map has degree \(t\).
The nonconstant map \(R\) has degree \(\delta\), since the affine transformation from \(z\) is invertible.
Homogeneous coprime pairs show that composition multiplies these degrees, including possible behavior at infinity.
The formal shifted-Hankel identity therefore gives \(\rho(T_t)=t\delta\), with the constant case \(t=0\) handled separately.
No good-reduction premise is used in these conclusions.

### The minimizing class and both degree cases

The normalized-denominator lemma applies to every member of the advertised minimizing class over \(\mathbb Q_2\).
An integral Taylor series converges at every algebraic point of absolute value less than one in the finite extension containing that point.
If a reduced denominator with constant coefficient one vanished there, evaluating its product with the convergent series would make the numerator vanish too, contradicting reducedness.
Its roots therefore all have absolute value at least one.
Factoring the normalized denominator and taking elementary symmetric functions of the inverse roots proves integrality of every denominator coefficient.
The numerator is then integral from the polynomial identity with the integral Taylor series.
This establishes P10 without a concealed bounded-denominator or rational-coefficient-in-\(\mathbb Q\) assumption.

For an approximation one digit deeper than \(s_t\), subtracting the explicit approximant leaves exactly its nonzero normalized error modulo two.
Multiplication by the integral unit \(BQ_t\) shows that the cross-product \(CQ_t-P_tB\) in P11 is divisible coefficientwise by \(2^{s_t}\) and has degree at most \(r+t\delta\).
Reduction gives P12 as an identity of rational functions, since all denominators have unit constant coefficient and rational expansion is injective.
The coprimality in P3 forces \(\overline D^{\,t+1}\mid\overline B\); neither \(\overline B\) nor \(\overline H\) is zero.
If \(\deg\overline D=\delta\), this already gives \(r\ge(t+1)\delta\).
Otherwise degree preservation makes \(\deg\overline E=\delta>\deg\overline D\); writing the quotient as \(J\ne0\) gives \(\deg\overline H=\deg J+(2t+1)\delta\), and the same lower bound follows.
This includes the polynomial residual case \(D=1\), where relying solely on a denominator degree would fail.

The constant one attains rank zero for every \(s\le a+1\).
For every other integer precision, the unique interval \(s_{t-1}<s\le s_t\) combines the lower bound at \(t-1\) with the explicit upper bound at \(t\).
This verifies the ceiling formula P4 at its endpoints and all intermediate levels, and hence P5.
In particular good reduction itself excludes a rational square root by the unbounded lower bound.
Multiplication and division by the fixed integral rational unit \(S\) preserve each coefficientwise congruence.
The two rational-map degree inequalities give the two directions of P6, including constant approximants and the polynomial part.
The minimum exists because the class is nonempty and its ranks are nonnegative integers.

The boundary identities were checked exactly.
For \(z=x+2x^2\), its characteristic-zero degree is two while its reduction has degree one, and \(1+8z=(1+4x)^2\).
For \(z=x(1+3x)/(1+x)^2\), the characteristic-zero pair is reduced of degree two and retains that maximum degree modulo two, but the reductions share \(1+x\); the square root is \((1+5x)/(1+x)\).
Each square root has shifted rank one at arbitrary precision, contradicting an extension of P4 obtained by dropping the respective P3 condition.
These are exact examples within the rational-approximation domain, with no claim that they arise from the original power-stable polynomial.

### Cayley composition and the original single radical

P9 gives P16 with the specified sign and odd exponent.
For any positive exponent \(n\), the even/odd construction yields the same Cayley ratio \(w^n\) and exact error depth \(an+1\).
When \(n\) is even, the numerator degree is \(n/2\) and the denominator degree is \(n/2-1\); their coprimality follows by the same simultaneous-vanishing argument.
Composition with \(R\) and multiplication by fixed \(S\) therefore give P17 with rank \(\lfloor n/2\rfloor\delta+O(1)\).
Reapplying the exponent-\(m\) operation raises the current Cayley ratio to its \(m\)-th power, giving \(w^{nm}\); inversion of that ratio determines exactly the member with exponent \(nm\).
The resulting limiting precision/rank ratio is \(2a/\delta\) as those exponents grow.
This family identity requires no good reduction; only its promotion to the optimum over all rational approximants uses P3.

The original-input return retains the actual polynomial, all conjugates, total logarithmic measure, original mask and original radical.
For a one-mask Galois orbit, the radical has rational Taylor coefficients; its centered representation with the supplied integral unit supplies integrality at two.
At odd primes, the original radicand has integral coefficients and unit constant coefficient, and the square-root recursion divides only by two, so these coefficients are integral there as well.
Thus the original determinants are integers even though a supplied center need not have globally integral coefficients.
The private-branch and nonrationality argument of C0858 uses the original geometric input and does not require importing its old uncentered modulo-eight premise into this centered argument.
It also excludes a constant residual for a rational center, so \(\delta>0\).
The normalized-denominator lemma applies to \((R-1)/2^\lambda\), and the affine change preserves \(\deg R=\delta\).

P18 supplies integral rational approximants with ranks at most \(\delta s/(2a)+O(1)\) at every positive precision.
The finite elementary-divisor implication applies to every such level of the same shifted Hankel matrix.
Summing \(\max(h-r_s,0)\) gives the quadratic coefficient \(a/\delta\) in P19; rounding and the fixed center cost contribute only \(O(h)\).
The original radical, regardless of artificial center zeros and poles, is holomorphic on the original disk \(|x|<H^{-4}\).
The Cauchy and Hadamard estimate has total factored exponent \(h^2\), and the shifted leading-Hankel criterion supplies infinitely many nonzero determinants of this nonrational series.
Fixing the input and radius first, taking that subsequence and then letting the radius tend to \(H^{-4}\) gives exactly P20.
The implication \(m(P)\ge\log H\) uses total measure without degree normalization.

For one component, the old fixed-binomial pole slope is \(\deg(R-1)=\delta\), so P20 is exactly twice the old certificate.
On the coherent integral low-degree cases selected from C0860v4 Part E, its H4--H5 bounds and uniform near-one conclusion therefore still force this doubled certificate to vanish under the same denominator-norm condition, including growing primes.
Under P3, P4--P6 exclude an improved asymptotic rational-rank slope from arbitrary precision-dependent centers for this same radical and same comparison.
They do not identify every determinant elementary divisor or rule out stronger divisibility from other mechanisms, a stronger complex estimate, or an altered original function.
When P3 fails, the claimed optimality is expressly unavailable.

### All-place multiple-radical boundary

The simultaneous local premises put each centered residual and its formal square root in every required completion with the stated precision.
The same normalization and upper-bound argument applies there; exact normalized reduction is unnecessary because the common depth need not be maximal for every component.
The centers are supplied equivariantly, so the rational sum \(F_t\) is fixed by the full Galois group and lies in \(\mathbb Q(x)\).
Integral Taylor coefficients at all primes above two descend to \(\mathbb Z_2\), as does their common \(2^{s_t}\) error.
No division by a stabilizer order is present in this construction.
Rational-map degree is subadditive under a finite sum and under multiplication, giving exactly P21's upper bound with \(\sum_J\delta_J\) and \(\sum_Jh_J\).
This reasoning does not assume that the new denominators share the old binomial union divisor.

The original sum is globally integral by the same odd-prime recursion and supplied two-adic integrality, and is nonrational by the original private-square-class character argument.
The C0858 all-level and original-disk interfaces therefore give the displayed paid bound \(a\log2/(4\sum_J\delta_J)\).
There is no lower-bound argument for the rank of this sum here.
In particular nonzero normalized errors of individual components may cancel, and the single-radical divisibility identity P12 cannot be assigned to the sum.
The text preserves this unresolved multiple-radical question and supplies no universal center-existence or unrestricted Mahler-gap conclusion.

### Selected source inspection and its limitations

The original Par88 Theorem 3.11, printed pages 37--38 / PDF pages 45--46, and BR10 Chapter 2, printed pages 30--31 / PDF pages 42--43, were read as source text together with their retained units.
The reduced minimal-recurrence qualification, formal field-valued matrix convention and polynomial contribution after the coefficient shift were checked.
The argument is algebraic over \(\mathbb Q_2\); the separate bounded-operator and complex pole-location assertions are not used.
BNZ22's retained original Section 2.2, printed/PDF pages 4--6, was read through Corollary 2.3, including the field convention and preceding finite approximation argument.
Applied to \((G-G(0))/x\), or the corresponding orbit sum, its determinant \(\Delta_{0,h-1}\) is exactly the shifted determinant used here.
No D-finiteness assumption from Section 2.3 is imported.

The retained [Kouba arXiv v2 original](../../literature/pdf/Kou11--arxiv-v2.pdf) was identified on its first page and read at definitions (4)--(6), Lemma 2.1 and Corollary 2.3 on printed/PDF pages 2--5.
Pages 3--5 were also inspected as complete rendered pages.
Lemma 2.1(a) and the explicit formula in Corollary 2.3 give \(V_{2t}(-Z)=p_t(1+Z)/q_t(1+Z)\), as claimed.
There is a concrete source caveat: the first two recurrence displays on page 4 incorrectly multiply the current Cayley error by the square or cube of the fixed initial error.
For Newton and Halley the current error itself must instead be squared or cubed; direct substitution in definitions (5)--(6) verifies this, and the stated conclusions \(F_n=V_{2^n-1}\), \(G_n=V_{3^n-1}\) agree with those correct identities.
The project's P16--P17 and composition argument prove the needed identities directly and do not invoke the incorrect intermediate displays.
Consequently the source is retained for the established mechanism and attribution with this explicit limitation, not as an unchecked proof premise for the dyadic or minimum-rank assertions.
No whole-paper, whole-book, priority or exhaustive novelty review is claimed.

The inspected project erratum had no current entry affecting the selected project inputs.
No numerical experiment, native output or proof-assistant certificate is a premise of this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole Pade finding](#pade-minimum-rank-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0860v5 statement](../../claims/Yin_C_G0860_v5.md#pade-statement) | Complete statement, P1--P6, arbitrary integral Q2-rational minimizing class, good-reduction conditions, exact ranks and all precision levels. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0860v5 argument](../../claims/Yin_C_G0860_v5.md#argument) | Entire P1--P21 proof and consequences, both boundary examples, source interfaces and original/multiple-radical restrictions. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [Integral Pade normalization](../../claims/Yin_C_G0860_v5.md#pade-integrality) | Exact coefficients, reductions, error depth, coprimality, map-degree multiplication and polynomial-inclusive shifted rank. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [Normalized denominator](../../claims/Yin_C_G0860_v5.md#integral-rational-denominator) | All reduced Q2-rational integral Taylor series; convergence, root exclusion and numerator/denominator integrality with degrees bounded by rank. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [Minimum rational rank](../../claims/Yin_C_G0860_v5.md#minimum-rational-rank) | P10--P15, both good-reduction degree cases, exact minimum at every integer precision, fixed-unit comparison and both exact boundary examples. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [Cayley recentering](../../claims/Yin_C_G0860_v5.md#pade-recentering) | P16--P17 for odd and even exponents, exact composition and precision/rank limit; source page-4 caveat retained in this finding. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [Original single radical](../../claims/Yin_C_G0860_v5.md#original-single-radical-return) | P18--P20, original integrality/nonrationality, every precision, fixed-input disk limits, factor two and exact scope of the coherent-center vanishing and optimality conclusions. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [Multiple-radical boundary](../../claims/Yin_C_G0860_v5.md#multiple-radical-boundary) | P21, supplied equivariant all-place premises, rational descent, sum-degree upper bound and paid disk consequence only; no minimum trace-rank assertion. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0860v1 binomial input](../../claims/Yin_C_G0860_v1.md#higher-depth-hankel-comparison) | Reused exact scaled-binomial valuation and formal remainder applicability; unrelated v1 conclusions keep their old scope. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0860v4 statement](../../claims/Yin_C_G0860_v4.md#statement) | Accepted polynomial-inclusive rational-rank convention and Part E's exact coherent integral low-degree/norm hypotheses and uniform conclusion only. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0860v4 precision budget](../../claims/Yin_C_G0860_v4.md#coherent-center-precision-budget) | H4--H5 and their actual one-component doubled-certificate application, retaining all original input, norm, degree and uniformity restrictions. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0858 original and Hankel interfaces](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Private-branch nonrationality, finite elementary-divisor implication and shifted leading-Hankel criterion; centered integrality checked separately without assuming its old uncentered congruence. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0858 disk comparison](../../claims/Yin_C_G0858_v1.md#cauchy-radius-cost) | Original H^(-4) radius, h-squared Cauchy exponent, nonzero determinant subsequence and order of limits only. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [Par88 canonical source unit](../literature/Par88/Yin_U001.md#par88-u001) | Only Theorem 3.11 reduced minimal-recurrence and formal rank mechanism, with original pages read and retained minimality qualification; no bounded-operator use. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [BR10 canonical source unit](../literature/BR10/Yin_U002.md#br10-u002) | Only Chapter 2 printed pages 30--31 formal Hankel matrix/rank and field conventions, with exact coefficient shift checked. |
| [Whole Pade finding](#pade-minimum-rank-whole) | [C0860v5 source interfaces](../../claims/Yin_C_G0860_v5.md#exact-inputs-and-source-scope) | Kouba v2 definitions, Lemma 2.1 and Corollary 2.3 at pages 2--5 with the explicit page-4 recurrence caveat; BNZ22 and accepted fixed-input boundaries as detailed above. |

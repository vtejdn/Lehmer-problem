---
author: Yin
---

# Complete arithmetic compatibility and the cost of near-positive integer moments

Date: 2026-11-05.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The responsible delegate developed the ghost and prefix-completion comparison; the coordinating agent supplied the explicit exterior-root lower-bound candidate, which the delegate checked below.
These are author derivations and ordinary checks, not independent review, a new Claim assessment or Task completion.

<a id="complete-arithmetic-near-psd-scope"></a>
## Question and relation to the earlier test

[L10 v2](Yin_L_G0010_v2.md#integer-moment-near-psd-scope) retains a three-by-three integer moment matrix with a vanishing negative eigenvalue, and a nonintegral reciprocal real-root model with the same first two moments and positive total measure tending to zero.
This version tests whether the complete integer ghost congruences and the original finite polynomial recurrence add a separately usable positive constraint.
It preserves v2's distinct small-measure nonintegral model and adds an integral reciprocal completion of its moment prefix whose total measure instead tends to infinity.
The two models must not be combined into one claimed original input.

The complete all-prime congruences are exactly the formal coefficient-integrality condition already encoded by [C240's integer Euler exponents](../claims/Yin_C_G0240_v1.md#finite-nettrace-repair).
When supplied by the same root polynomial, its initialized Newton identities and finite recurrence are the existing [C215 exact moment identities](../claims/Yin_C_G0215_v1.md#argument).
Their reformulation supplies no new sign or quantitative archimedean inequality.
The completion below shows that full arithmetic and this fixed near-positive moment block can coexist, but pays a divergent total measure.
A separate equally spaced angular control shows why small normalized polynomial measure, a small house and many vanishing low moments do not establish small total measure.

<a id="all-prime-ghost-equivalence"></a>
## All-prime congruences and integer formal coefficients

Let \((s_n)_{n\ge1}\) be an integer sequence, and put
\[
 b_n=\frac1n\sum_{e\mid n}\mu(n/e)s_e.
\tag{1}
\]
Then the following conditions are equivalent:
\[
 b_n\in\mathbb Z\quad\hbox{for every }n\ge1,
\tag{2}
\]
\[
 s_{ap^k}\equiv s_{ap^{k-1}}\pmod{p^k}
 \quad\hbox{for every prime }p,\ p\nmid a,\ k\ge1.
\tag{3}
\]
Mobius inversion gives \(s_n=\sum_{e\mid n}e b_e\).
For \(p\nmid a\), subtraction therefore gives
\[
 s_{ap^k}-s_{ap^{k-1}}
 =\sum_{e\mid a}ep^k b_{ep^k},
\]
which proves (3) from (2).
Conversely, for \(n=ap^k\) with \(p\nmid a\), separate the divisors in (1) according to their last two possible powers of \(p\) to obtain
\[
 n b_n=\sum_{e\mid a}\mu(a/e)
             \bigl(s_{ep^k}-s_{ep^{k-1}}\bigr).
\tag{4}
\]
Condition (3) makes this divisible by \(p^k\).
Applying this to each prime power dividing \(n\) proves \(n\mid n b_n\), hence (2).
The index \(n=1\) gives \(b_1=s_1\in\mathbb Z\) directly.

In formal power series over \(\mathbb Q\),
\[
 F(z)=\exp\!\left(-\sum_{n\ge1}\frac{s_nz^n}{n}\right)
     =\prod_{n\ge1}(1-z^n)^{b_n}.
\tag{5}
\]
For (2), each coefficient of the product involves only finitely many integral factors, including the integral formal expansions of negative integer powers, so \(F\in1+z\mathbb Z[[z]]\).
Conversely, the coefficient recursion in [C240](../claims/Yin_C_G0240_v1.md#finite-nettrace-repair) gives the unique integer Euler exponents of any \(F\in1+z\mathbb Z[[z]]\); formal logarithmic differentiation identifies them with (1).
Thus (3) is equivalent to integrality of all formal coefficients in (5).
The all-prime equivalence here is elementary divisor rearrangement of that retained identity, with no new external theorem or novelty claim.
No boundary convergence is used.
The obstruction in [L133 v2](Yin_L_G0133_v2.md#raw-euler-truncations-cannot-converge-in-boundary-l1) specifically prevents treating these raw Euler products as an available boundary \(L^1\) approximation when the original integral unit polynomial has positive measure.

For an actual finite multiset \(\alpha_1,\ldots,\alpha_d\) and its power sums, (5) is precisely
\[
 F(z)=\prod_{i=1}^d(1-\alpha_i z).
\tag{6}
\]
Consequently the complete ghost congruences encode the integer coefficients of this very polynomial.
They add no independent arithmetic predicate after those coefficients have already been required to be integral.
They do not assert nonnegativity of the Euler exponents.
C240's separate nonnegative orbit-count repair requires its Perron domain and retains uncontrolled cycle padding and realization complexity.

<a id="initialized-recurrence-and-prefix-completion"></a>
## The recurrence must belong to the same polynomial

Write \(F(z)=1+c_1z+\cdots+c_dz^d\), with \(c_0=1\).
The formal identity \(-zF'(z)=F(z)\sum_{n\ge1}s_nz^n\) gives
\[
 s_n+c_1s_{n-1}+\cdots+c_{n-1}s_1+n c_n=0
             \qquad(1\le n\le d),
\tag{7}
\]
\[
 s_n+c_1s_{n-1}+\cdots+c_ds_{n-d}=0
             \qquad(n>d).
\tag{8}
\]
These are exactly the initialization and recurrence retained in C215.
Conversely, (7) and (8) for the same coefficients imply the formal logarithmic-derivative identity, and the constant coefficient \(F(0)=1\) identifies (5) with this polynomial.
An arbitrary integer recurrence without (7) does not certify that the sequence consists of the unweighted power sums of its characteristic roots.
For example, \(s_n=-1\) for every \(n\ge1\) satisfies an order-one integer recurrence and (3), but (5) is \((1-z)^{-1}\), not a polynomial.
Thus recurrence order, initialization and the finite polynomial requirement cannot be silently interchanged.

There is nevertheless a direct complete-arithmetic extension of every integer Newton prefix.
Suppose prescribed \(s_1,\ldots,s_r\) yield integers \(c_1,\ldots,c_r\) recursively through (7).
For every integer \(d>2r\), define
\[
 P_d(X)=X^d+\sum_{j=1}^r c_jX^{d-j}
                   +\sum_{j=1}^r c_jX^j+1.
\tag{9}
\]
The displayed supports do not overlap.
This is a monic integral reciprocal polynomial of degree \(d\) and constant term one.
Its first \(r\) power sums agree with the prescribed ones by (7), while its entire sequence obeys (3), (7) and (8).
It makes no assertion of irreducibility, squarefreeness, all-power degree preservation or small total measure.
In particular, satisfying every later arithmetic congruence is not itself a quantitative continuation of the initial radial geometry.

<a id="pell-integral-completion-and-measure-price"></a>
## The Pell prefix has a full integral completion with divergent total measure

Use precisely [v2's integer pairs](Yin_L_G0010_v2.md#integer-near-psd-three-moment-construction):
\[
 d\ge32,\quad a\ge23,\quad d\text{ even},\quad a\text{ odd},
 \qquad 2a^2=d^2+d+2,
\tag{10}
\]
with \(d,a\to\infty\) along the explicit recurrence retained there.
Put \(b=(a^2-1)/2\), and take the completion
\[
 P_{d,a}(X)=X^d-aX^{d-1}+bX^{d-2}+bX^2-aX+1.
\tag{11}
\]
This notation denotes the new integral completion, not v2's nonintegral real-root polynomial.
Its moments are \(s_0=d,s_1=a,s_2=a^2-2b=1\), so its three-by-three Toeplitz block is exactly v2's matrix.
In particular,
\[
 \det T=-2(d-1),\qquad
 \lambda_{\min}(T)
 =\frac{-4}{\sqrt{(2d+1)^2+8}+2d+1}\longrightarrow0^-.
\tag{12}
\]
The fixed-diagonal positive comparison and elimination ratio retained in v2 therefore apply to the same prefix of a complete integral reciprocal polynomial.

Its actual total measure has the two-sided price
\[
 2\log(a/4)<m(P_{d,a})\le2\log(a+1).
\tag{13}
\]
For the upper bound, the normalized logarithmic-integral identity retained in [Den09-U001](../audits/literature/Den09/Yin_U001.md#mahler-measure) gives
\[
 m(P_{d,a})\le\log\|P_{d,a}\|_{\mathbb T}
 \le\log\bigl(2+2a+2b\bigr)=2\log(a+1).
\]
All six displayed coefficients occupy distinct positions because \(d\ge32\).

For the lower bound, put
\[
 A(X)=X^2-aX+b,\qquad A^*(X)=1-aX+bX^2,
 \qquad R=a/4>1.
\]
Then \(P_{d,a}=X^{d-2}A+A^*\).
On \(|X|=R\),
\[
 |A(X)|\ge b-aR-R^2
       =\frac{3a^2-8}{16}\ge\frac{a^2}{8},
\tag{14}
\]
\[
 |A^*(X)|\le1+aR+bR^2
       =1+\frac{7a^2}{32}+\frac{a^4}{32}
       \le\frac{a^4}{16}.
\tag{15}
\]
The final inequality follows from \(a^4-7a^2-32\ge0\) for \(a\ge23\).
Since \(d-2\ge4\) and \(R>1\),
\[
 |X^{d-2}A(X)|\ge R^{d-2}\frac{a^2}{8}
       \ge\frac{a^6}{2048}>\frac{a^4}{16},
\tag{16}
\]
where the strict inequality uses \(a^2>128\).
The discriminant of \(A\) is \(2-a^2<0\), and its two conjugate roots have modulus \(\sqrt b>R\).
Thus \(X^{d-2}A\) has exactly \(d-2\) roots in \(|X|<R\), counted with multiplicity.
Rouche's theorem and (14)--(16) give the same count for \(P_{d,a}\), with no root on the circle.
Exactly two roots of \(P_{d,a}\) lie outside radius \(R\), proving the strict lower bound in (13).
No location claim for its other roots, irreducibility claim or numerical root computation is needed.

The precise Rouche input is Jacob Shapiro, *Complex Analysis with Applications*, MAT330 Spring 2023 notes, Corollary 7.44, printed page 83.
The existing [C857 application](../claims/Yin_C_G0857_v1.md#large-period-full-mask) and [R1074 source check](../audits/reviews/Yin_R_G1074_v1.md#binary-masks-whole) identify this source and record direct local-PDF inspection of that corollary and its strict-boundary comparison hypothesis.
That adequate source inspection is reused here; both compared functions are polynomials and (16) verifies the required strict inequality on the circle of radius \(R\).
No new original-source access, whole-source proof audit or transfer of R1074's independent review to the present argument is asserted.

Equation (13) proves \(m(P_{d,a})\to\infty\), whereas (10) and the upper bound give \(m(P_{d,a})/d\to0\).
The latter is normalized polynomial measure; its identification with a chosen root's absolute height requires the corresponding minimal-polynomial normalization, which is not supplied here.
Small normalized measure alone therefore cannot control these untruncated first power sums.
This does not show a failure of angular equidistribution: large roots can contribute substantially to \(s_1\) without their radial projections having a large average angle.
The ordinary all-root bound in [C1](../claims/Yin_C_G0001_v1.md#integer-trace-low-mode-question),
\[
 \left|s_n-\sum_i e^{in\theta_i}\right|
       \le2n e^{n m(P)}m(P),
\tag{17}
\]
becomes small at fixed \(n\) when total \(m(P)\to0\), not merely when \(m(P)/d\to0\).
For the actual monic irreducible polynomial of a nontorsion unit, [C570's angular estimate](../claims/Yin_C_G0570_v1.md#uniform-powered-angular-coherence) bounds the first angular average by a quantity tending to zero as \(m(P)/d\to0\), retaining the actual powered-degree multiplicities.
In a genuine irreducible small-total-measure sequence, that bound together with (17) excludes the Pell ratio \(s_1/d\to1/\sqrt2\).
Neither the present completion nor v2's nonintegral model satisfies that combined original-input situation.

<a id="delayed-angular-control-and-power-drop"></a>
## A complete-arithmetic angular control with fixed positive measure

A different control preserves small low angular moments explicitly:
\[
 Q_k(X)=X^{2k}-3X^k+1,\qquad
 \lambda=(3+\sqrt5)/2>1,\qquad k\ge1.
\tag{18}
\]
This family already occurs in the inspected [MS26-U001 central case](../audits/literature/MS26/Yin_U001.md#ms26-u001).
The more general composition and vanishing-low-mode warning is retained in [C4](../claims/Yin_C_G0004_v1.md#exact-damped-polynomial); no new source result or family is claimed here.
The following root formulas are direct calculations, not a use of the source's Salem classification.

The roots are \(\lambda^{1/k}\zeta_k^j\) and \(\lambda^{-1/k}\zeta_k^j\), for \(0\le j<k\), so
\[
 d=2k,\qquad m(Q_k)=\log\lambda,\qquad
 \operatorname{house}(Q_k)=\lambda^{1/k}\longrightarrow1.
\tag{19}
\]
Their normalized angular measure is the uniform \(k\)-point grid, with each angle occurring twice in the full root multiset.
For every circular arc its mass differs from normalized arc length by at most \(2/k\), by counting grid points between its two endpoints.
In particular,
\[
 \frac1{2k}\sum_i e^{in\theta_i}
 =\begin{cases}0&k\nmid n,\\1&k\mid n,\end{cases}
 \qquad
 s_n=\begin{cases}0&k\nmid n,\\
 k(\lambda^\ell+\lambda^{-\ell})&n=k\ell.
 \end{cases}
\tag{20}
\]
The numbers \(u_\ell=\lambda^\ell+\lambda^{-\ell}\) are integers by \(u_0=2,u_1=3,u_{\ell+1}=3u_\ell-u_{\ell-1}\).
The complete sequence has the same original polynomial recurrence
\[
 s_{n+2k}=3s_{n+k}-s_n\qquad(n\ge0),\qquad s_0=2k,
\]
and every all-prime congruence follows from its integer polynomial.
All angular modes and traces vanish throughout \(1\le n<k=d/2\), although total measure stays fixed and positive.
At the first nonzero mode, \(n=k\), the normalized trace is \(s_k/d=3/2\), the angular moment is one, and \(n m(Q_k)/d=\log\lambda/2\), which does not tend to zero.
Thus this is not a violation of an angular estimate requiring small frequency-scaled height.

These are complete polynomial controls, with no assertion that \(Q_k\) is irreducible.
For the actual root \(\alpha=\lambda^{1/k}\) and \(k\ge3\), \(\deg\alpha>2\) whereas \(\deg(\alpha^k)=2\), so a power-degree drop really occurs.
Indeed \(\lambda\in\mathbb Q(\alpha)\), and degree at most two would force \(\mathbb Q(\alpha)=\mathbb Q(\sqrt5)\).
The conjugate of \(\alpha\) in that field would be \(\pm\alpha^{-1}\), because \(\alpha\) is a real integer unit.
Its integer trace would then be either \(\alpha+\alpha^{-1}\), strictly between 2 and 3, or \(\alpha-\alpha^{-1}\), strictly between 0 and 1.
The latter bounds use \(1<\alpha<\sqrt\lambda\) for \(k\ge3\), with \(\sqrt\lambda-1/\sqrt\lambda=1\); both trace alternatives are impossible.
This control is therefore outside [C231's all-positive-power endpoint](../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) and is not an endpoint near-one counterexample.
Equation (19) computes the whole polynomial's normalized measure; a chosen root's original degree and minimal-factor measure require separate factor or power accounting.
No such degree or minimal-factor identity is inferred from (19), regardless of whether a further argument identifies the corresponding absolute height.

<a id="complete-ghost-return-boundary"></a>
## Remaining original-input bridge and checking scope

The complete congruences, same-polynomial Newton initialization and recurrence must be retained, but restating them supplies no new quantitative gain.
The integral Pell completion establishes that the fixed near-positive moment block survives full coefficient integrality at a divergent total-measure price.
The delayed control establishes that a small house, vanishing normalized polynomial measure and many zero low angular moments can coexist with fixed positive total measure and a power-degree drop.
Neither control is a candidate sequence for the unrestricted zero-gap conclusion.

The first unsupported bridge remains a quantitative implication from genuinely small total \(m(P)\), on the actual irreducible original input or a legitimate endpoint, to a useful restriction on its complete coefficient/ghost sequence with the degree, recurrence and archimedean costs paid.
This might take the form of a short original integral relation or a useful full norm inequality, but neither is supplied by congruence divisibility alone.
The inspected [D13 comparison](../drafts/Yin_D_G0013.md#automatic-multiple-and-frobenius-supply) already retains the unsupported compression of height-one multiples to fixed support in a degree-linear window and the lack of strict surplus from a normalized Frobenius value.
The [S4 arithmetic allocation](../strategies/Yin_S_G0004.md#arithmetic-resultant-route) retains those original-input supply costs.
No alternative positive compatibility mechanism was found by this bounded test, and no further parameter scan is justified by this reformulation alone.

The local comparison inspected L10 v2, C215, C240, L133 v2, C1's low-mode question, C4's composition controls, C570's angular statement and its retained L229 argument, D13, the relevant S4 allocation, MS26-U001 and C231's endpoint descent.
The source checks needed for the new measure price were adequately available in Den09-U001 and the explicit Sha23 inspection in R1074; no new external search or pending source identification is needed for these uses.
The delegate checked the prime-by-prime divisibility equivalence, formal signs, Newton initialization, nonoverlapping reciprocal completion, both measure estimates and root counts, angular formulas, normalization and actual power-drop argument.
The coordinating agent contributed the exterior-root lower-bound mechanism, so neither contributor is an independent reviewer of that argument.
No native mathematical program, numerical experiment, formal review or new Claim adoption was used or created.

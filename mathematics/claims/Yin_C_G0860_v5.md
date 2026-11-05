---
author: Yin
---
# Dyadic square-root Padé approximation and exact minimum rational rank under good reduction

This project deduction strengthens the approximation-rank question using a different rational approximation family from the fixed binomial truncations of [C860 v4](Yin_C_G0860_v4.md#statement).
The complete original A--E conclusions remain at [v1](Yin_C_G0860_v1.md#statement), with their [selected assessment](Yin_C_G0860_v1.md#decision-whole-independent-review-2026-11-04).
The complete M1--M9 conclusions remain at [v2](Yin_C_G0860_v2.md#statement), with their [selected assessment](Yin_C_G0860_v2.md#decision-whole-independent-review-2026-11-04).
The complete fixed-center rank and precision-budget theorem remains at [v4](Yin_C_G0860_v4.md#statement), with its [selected assessment](Yin_C_G0860_v4.md#decision-whole-independent-review-2026-11-04).
Those fixed statements, proofs and reviews are preserved rather than copied here, and their acceptance is not transferred to the new mathematics.
The precision-varying-approximants contributor developed this argument for Yin, and the coordinating main agent checked its algebra, normalization and minimum-rank degree cases as a contributor.
Neither check is an independent review.
The [selected assessment](#decision-whole-independent-review-2026-11-04) adopts the complete new theorem and its stated consequences through the separate independent R1076 v4 finding.
No rolling Draft or temporary file is a mathematical premise.
The original unrestricted positive total logarithmic Mahler gap remains unresolved.

<a id="pade-statement"></a>
## Statement

Let \(z=E/D\in\mathbb Q_2(x)\) be nonconstant and reduced, with
\[
 E,D\in\mathbb Z_2[x],\qquad E(0)=0,\qquad D(0)=1,
 \qquad
 \delta=\max(\deg E,\deg D)\ge1.
\]
Assume \(z\notin2\mathbb Z_2[[x]]\).
Let \(\lambda\ge3\) be an integer, put \(a=\lambda-2\), and set
\[
 R=1+2^\lambda z,\qquad y=R^{1/2},\qquad y(0)=1.
\]
The square root means its formal binomial expansion.
For a rational power series \(T\), write \(\rho(T)\) for the rank over \(\mathbb Q_2\) of its infinite shifted coefficient Hankel matrix.
Equivalently, for nonconstant reduced \(T=A/B\), regular at zero and normalized by \(B(0)=1\), this rank is \(\max(\deg A,\deg B)\); the rank of a constant is zero.
This is the formal rational-rank convention already used in C860 v4, including the polynomial part.

For each \(t\ge0\), put \(n=2t+1\) and define
\[
 \begin{split}
 p_t(T)&=2^{-2t}\sum_{j=0}^{t}\binom{2t+1}{2j}T^j,\\
 q_t(T)&=2^{-2t}\sum_{j=0}^{t}\binom{2t+1}{2j+1}T^j,\\
 P_t(x)&=D(x)^t p_t(R(x)),\\
 Q_t(x)&=D(x)^t q_t(R(x)),\qquad T_t=P_t/Q_t,\\
 s_t&=a(2t+1)+1.
 \end{split}                                                    \tag{P1}
\]
Then \(P_t,Q_t\in\mathbb Z_2[x]\), \(P_t(0)=Q_t(0)=1\), their degrees are at most \(t\delta\), and
\[
 \begin{split}
 \overline {P_t}&=\overline D^{\,t},\qquad
 \overline {Q_t}=\overline D^{\,t},\\
 y-T_t&\in2^{s_t}\mathbb Z_2[[x]],\\
 \overline{(y-T_t)/2^{s_t}}
   &=(\overline E/\overline D)^{2t+1}.
 \end{split}                                                    \tag{P2}
\]
Here bars denote coefficient reduction and the last equality is in \(\mathbb F_2[[x]]\), equivalently between the displayed rational functions in \(\mathbb F_2(x)\).
The last expression is nonzero, so the displayed depth is exact.
Also \(\rho(T_t)=t\delta\).
No good-reduction assumption is needed for (P1)--(P2) or this rank assertion.

Suppose in addition that the normalized residual has good reduction in the following explicit sense:
\[
 \gcd(\overline E,\overline D)=1,\qquad
 \max(\deg\overline E,\deg\overline D)=\delta.                \tag{P3}
\]
For \(s\ge1\), let \(r_s(y)\) be the least shifted Hankel rank among all \(T\in\mathbb Q_2(x)\cap\mathbb Z_2[[x]]\) such that \(y-T\in2^s\mathbb Z_2[[x]]\).
There is no restriction that \(T\) be a function of \(z\), arise from Padé approximation, have a fixed center, or have rational coefficients in \(\mathbb Q\).
Then
\[
 r_s(y)=
 \delta\max\!\left(0,
             \left\lceil\frac{s-a-1}{2a}\right\rceil\right).
                                                               \tag{P4}
\]
In particular the whole precision-dependent class, not only the explicit approximants, has asymptotic minimum rank
\[
                     r_s(y)=\frac{\delta}{2a}s+O(1).        \tag{P5}
\]

If \(S\in\mathbb Q_2(x)\) is regular at zero and both \(S,S^{-1}\) belong to \(\mathbb Z_2[[x]]\), put \(G=Sy\).
Define \(r_s(G)\) by the same minimizing class and congruence condition with \(G\) in place of \(y\).
Writing \(h=\rho(S)\), one has
\[
 |r_s(G)-r_s(y)|\le h,\qquad
 \rho(S T_t)=t\delta+O(1).                                  \tag{P6}
\]
Thus (P5) remains valid for \(G\), with the same slope.
The constant in (P6) depends on the fixed center and does not depend on \(s\) or \(t\).

## Exact inputs and source scope

The formal rational-rank identity is reused from [C860 v4's adopted reduced-pole/minimal-recurrence interface](Yin_C_G0860_v4.md#statement) and its [Par88](../audits/literature/Par88/Yin_U001.md#proof-mechanism-and-minimality)/[BR10](../audits/literature/BR10/Yin_U002.md#formal-hankel-rank) source scopes.
Its algebraic proof applies unchanged over \(\mathbb Q_2\): a denominator recurrence gives the upper bound, and a smaller recurrence would contradict the reduced rational expression; the polynomial part is counted after the coefficient shift.
The finite elementary-divisor comparison, nonrationality of the actual original radicals and infinitely many nonzero shifted leading Hankel determinants are reused only at [C858's exact adopted scope](Yin_C_G0858_v1.md#all-place-hankel-budget), with its [selected assessment](Yin_C_G0858_v1.md#decision-whole-independent-review-2026-11-04).
The complex return uses only [its original-radius and quadratic Cauchy estimate](Yin_C_G0858_v1.md#cauchy-radius-cost).
The formal binomial valuation is reused from [C860 v1](Yin_C_G0860_v1.md#statement), with the selected assessment linked above.
The final vanishing-certificate comparison uses only [C860 v4 Part E and its proof](Yin_C_G0860_v4.md#coherent-center-precision-budget), at its selected assessment linked above.

The square-root Cayley identity and its Newton/Halley specialization are established source mathematics.
The selected original is Omran Kouba, *Partial Fraction Expansions for Newton's and Halley's Iterations for Square Roots*, arXiv:1104.4175v2, 1 May 2011.
The [retained original ten-page PDF](../literature/pdf/Kou11--arxiv-v2.pdf) is the [specified arXiv v2](https://arxiv.org/pdf/1104.4175v2).
The [source notes](../audits/literature/Kou11/readme.md) own its edition and inspection scope.
The definitions (4)--(6) on printed/PDF page 2, Lemma 2.1 and its proof on pages 3--4, and Corollary 2.3 and its displayed proof on pages 4--5 were read in the original.
The source's \(V_{2t}(-Z)\), where \(Z=R-1\), is the rational function in (P1).
These passages supply attribution for the Cayley and approximation-order mechanism, not a source statement of (P2)--(P6).
The dyadic integral normalization, exact coefficientwise depth, optimality among all \(x\)-rational approximants, and original-input comparison below are proved here.
No whole-paper inspection, source-priority claim or novelty claim is made.
The [source notes](../audits/literature/Kou11/readme.md) record two erroneous displayed recurrences in Lemma 2.1(b)'s proof; the project identities (P16)--(P17) are derived directly below and do not use those displays.

The bounded preparation searched the current Claims, ledgers, drafts and source audits for square-root Padé approximation, minimal recurrence and precision-dependent rational centers.
It found the existing rational-rank and determinant interfaces but no result supplying the optimality assertion (P4).
A necessary external primary-source search identified the inspected Kouba passages; this was sufficient to attribute the recognized mechanism.
The search does not assert absence of other prior versions of (P4).

<a id="argument"></a>
<a id="pade-integrality"></a>
## Explicit dyadic normalization and exact error

The standard binomial valuation already used in C860 gives
\[
 y\in1+2^{\lambda-1}x\mathbb Z_2[[x]].
\]
For example, the first nonconstant binomial term is \(2^{\lambda-1}z\), while every subsequent term is divisible by \(2^\lambda\).
The equality
\[
                (y-1)(y+1)=2^\lambda z
\]
then shows directly that the exact coefficientwise depth of \(y-1\) is \(\lambda-1\).
Indeed \((y+1)/2\) is an integral power-series unit congruent to one modulo two, and the reduction of \(z\) is nonzero.

Set
\[
             u=(1+y)/2,\qquad v=(1-y)/2.
\]
These are integral series, \(u\equiv1\pmod2\), \(v(0)=0\), and
\[
             v=-2^a z/u,\qquad
             \overline{v/2^a}=\overline z.                 \tag{P7}
\]
Expanding the odd power \(n=2t+1\) and separating its even and odd powers of \(y\) gives the exact identities
\[
              p_t(R)=u^n+v^n,\qquad
              q_t(R)=(u^n-v^n)/y.                         \tag{P8}
\]
Both right sides belong to \(1+2x\mathbb Z_2[[x]]\).
Multiplication by \(D^t\) in (P1) clears the rational denominators and yields polynomials of degree at most \(t\delta\).
Since these polynomial expressions have integral Taylor coefficients by (P8), every coefficient of \(P_t,Q_t\) is integral.
Their constant terms and reductions are the first line of (P2).

Subtracting the two identities in (P8) yields
\[
        T_t-y=\frac{2v^n}{q_t(R)}
              =\frac{2y\,v^n}{u^n-v^n}.                  \tag{P9}
\]
The denominators in (P9) are integral power-series units congruent to one modulo two.
Using (P7) proves both the divisibility and the nonzero normalized reduction in (P2).
Signs disappear in characteristic two.
In particular the exact depth is \(an+1\), rather than merely a Taylor order in the variable \(Z\).

The univariate polynomials \(p_t,q_t\) both have degree \(t\).
They are coprime over characteristic zero.
To check this, suppose a common zero is \(T_0\), choose \(y_0^2=T_0\), and first consider \(y_0=0\).
Then \(p_t(0)=2^{-2t}\ne0\), so this case is impossible.
For \(y_0\ne0\), the even/odd expansions imply that both \((1+y_0)^n\) and \((1-y_0)^n\) vanish, also impossible.
Thus the rational map \(p_t/q_t\) has degree \(t\).
The nonconstant map \(R=1+2^\lambda z\) has degree \(\delta\).
Their composition therefore has degree \(t\delta\).
One can verify the multiplication of degrees directly by homogenizing the two coprime numerator/denominator pairs: composition gives homogeneous forms of degree \(t\delta\), and a common zero would give a common zero in one of the two original pairs.
The formal rational-rank identity gives \(\rho(T_t)=t\delta\).
For \(t=0\), the approximant is the constant one and the same formula gives zero.

<a id="integral-rational-denominator"></a>
## Integral rational series have an integral normalized denominator

Let \(T=A/B\in\mathbb Q_2(x)\cap\mathbb Z_2[[x]]\) be reduced and regular at zero, with \(B(0)=1\).
Then \(A,B\in\mathbb Z_2[x]\).
Here is a direct argument covering arbitrary approximants in (P4).

The integral Taylor series of \(T\) converges at every point with two-adic absolute value less than one, in any finite extension containing that point.
If \(B\) had a root \(\beta\) with \(|\beta|_2<1\), evaluating the convergent identity \(B T=A\) at \(\beta\) would give \(A(\beta)=0\), contrary to reducedness.
All roots \(\beta\) of \(B\) therefore have \(|\beta|_2\ge1\).
Factor \(B(x)=\prod_\beta(1-x/\beta)\), with multiplicities, in a splitting field.
Every coefficient is an elementary symmetric sum of numbers with absolute value at most one.
It is consequently two-adically integral; since it lies in \(\mathbb Q_2\), it belongs to \(\mathbb Z_2\).
Finally \(A=B T\) has integral Taylor coefficients and is a polynomial, proving the assertion.

In particular a rational series of shifted rank \(r\) can always be written in this integral normalized form with
\[
                         \deg A,\deg B\le r.              \tag{P10}
\]
No unproved restriction on denominator size or denominator coefficients has been placed on the minimizing class.

<a id="minimum-rational-rank"></a>
## Lower bound for every rational approximant

Assume (P3), and fix \(t\ge0\).
Suppose \(C/B\) is any integral rational power series of shifted rank \(r\) satisfying
\[
                  y-C/B\in2^{s_t+1}\mathbb Z_2[[x]].
\]
Choose its reduced integral representation supplied above, with \(B(0)=1\) and \(\deg C,\deg B\le r\).
By (P2), the difference \(C/B-P_t/Q_t\) has depth exactly \(s_t\), with normalized reduction \(\overline z^{\,2t+1}\).
Since \(B Q_t\) is an integral power-series unit, the polynomial
\[
                    H=(C Q_t-P_t B)/2^{s_t}               \tag{P11}
\]
has integral coefficients and degree at most \(r+t\delta\).
Reduction of (P11) and use of \(\overline{Q_t}=\overline D^t\) give
\[
        \overline H=
           \frac{\overline B\,\overline E^{\,2t+1}}
                {\overline D^{\,t+1}}.                    \tag{P12}
\]
The numerator and denominator powers of \(\overline E,\overline D\) are coprime.
Because the left side is a polynomial, (P12) forces
\[
                       \overline D^{\,t+1}\mid\overline B.
                                                               \tag{P13}
\]
The polynomial \(\overline B\) is nonzero because its constant term is one.
The polynomial \(\overline H\) is nonzero because \(\overline E\ne0\).

If \(\deg\overline D=\delta\), (P13) gives
\[
                         r\ge(t+1)\delta.
                                                               \tag{P14}
\]
This includes the case in which both reduced degrees equal \(\delta\).

Otherwise (P3) gives \(\deg\overline E=\delta>\deg\overline D\).
Write \(\overline B=\overline D^{\,t+1}J\), where \(J\ne0\).
Equation (P12) becomes \(\overline H=J\overline E^{\,2t+1}\), and therefore
\[
       r+t\delta\ge\deg\overline H
                 =\deg J+(2t+1)\delta
                 \ge(2t+1)\delta.
                                                               \tag{P15}
\]
This again proves (P14), and explicitly includes a polynomial residual \(D=1\).

For \(s\le s_0=a+1\), the constant one is an approximant of rank zero.
For \(s>s_0\), let \(t\ge1\) be the unique integer with \(s_{t-1}<s\le s_t\).
The construction \(T_t\) gives rank \(t\delta\), while (P14) applied at \(t-1\) gives the matching lower bound.
This proves the exact formula (P4), including all integer precision levels.
In particular \(y\) cannot itself be rational under (P3), since a rational \(y\) would contradict the unbounded lower bound.

For the fixed rational unit \(S\), multiplication and division by \(S\) preserve coefficientwise congruence modulo \(2^s\).
For any two rational functions their map degrees obey
\[
 \deg(F_1F_2)\le\deg F_1+\deg F_2,\qquad
 \deg F_1\le\deg(F_1F_2)+\deg F_2.
\]
These follow by multiplying numerator/denominator pairs and then cancelling, and applying the first inequality to \((F_1F_2)/F_2\).
The rational-rank identity and multiplication by \(S\) or \(S^{-1}\) prove (P6).

### Why both good-reduction conditions are necessary

The conditions in (P3) cannot simply be dropped.
For \(\lambda=3\), the residual \(z=x+2x^2\) has reduced degree two, while its reduction has degree one.
Here \(1+8z=(1+4x)^2\), so the square root is already rational of shifted rank one at every precision.
The reduced numerator and denominator modulo two are coprime, but degree preservation fails.

Independently, take \(z=x(1+3x)/(1+x)^2\), still with \(\lambda=3\).
The numerator and denominator are coprime over \(\mathbb Q_2\), and their reduced maximum degree is still two.
Their reductions share the factor \(1+x\), however, and
\[
            1+8z=\left(\frac{1+5x}{1+x}\right)^2.
\]
Again the square root has rank one at every precision.
These are exact boundary checks on the rational-approximation theorem, not admissible original power-stable Lehmer counterexamples.

<a id="pade-recentering"></a>
## Precision-dependent Cayley recentering does not compound the gain

Keep \(G=Sy\), and put \(w=(S-G)/(S+G)=(1-y)/(1+y)\).
Equation (P9) is equivalent to
\[
             \frac{S T_t-G}{S T_t+G}=w^{2t+1}.             \tag{P16}
\]
More generally the same even/odd power construction works for every positive exponent \(n\).
Its rational approximant \(\mathcal T_n\) satisfies
\[
 \frac{\mathcal T_n-G}{\mathcal T_n+G}=w^n,\qquad
 v_2(G-\mathcal T_n)=an+1,\qquad
 \rho(\mathcal T_n)=\lfloor n/2\rfloor\delta+O(1).
                                                               \tag{P17}
\]
The valuation is coefficientwise; its exactness follows from (P7)--(P9).
For even \(n\), the even numerator has degree \(n/2\) and the odd denominator has degree \(n/2-1\), so the same coprimality and composition argument proves the degree assertion.
The fixed factor \(S\) changes rank by at most \(\rho(S)\).

If \(\mathcal T_n\) is used as a new center and the exponent-\(m\) construction is then applied, its Cayley error is \((w^n)^m=w^{nm}\).
Solving this identity for the approximant shows that the resulting function is exactly \(\mathcal T_{nm}\).
Thus arbitrary successive Newton, Halley or odd diagonal Padé steps are already members of this single family.
Their centers may have arbitrarily growing degree, but their limiting precision/rank ratio remains \(2a/\delta\).
The composition identity requires no good reduction.
Under (P3), (P4)--(P6) strengthen this family calculation to optimality among all rational approximants of the single radical.

<a id="original-single-radical-return"></a>
## Return to one actual original radical

Use exactly the original power-stable monic irreducible reciprocal noncyclotomic polynomial \(P\), its degree \(d\), all conjugates, total logarithmic measure \(m(P)\), house \(H\), and rotated products \(D_I,N_I\) of C860 v4.
Suppose the mask \(I\) is fixed by the full Galois group of \(\mathbb Q(\zeta_q)/\mathbb Q\), so that its orbit contains one mask and
\[
                       G=(N_I/D_I)^{1/2}\in\mathbb Z[[x]]
\]
is the actual single original radical.
Examples of Galois-invariant masks are \(\{0\}\), the set of all nonzero residues, and the full mask; their arithmetic depth remains a supplied condition.
No existence of a favorable such mask on every near-one input is asserted.

Choose a supplied rational center \(S=C/B\in\mathbb Q(x)\), with \(B(0)=C(0)=1\), such that \(S,S^{-1}\in\mathbb Z_2[[x]]\), and suppose
\[
 R=\frac{N_I B^2}{D_I C^2},\qquad
 \lambda=v_2(R-1)\ge3.
\]
Write the exact normalized residual \(z=(R-1)/2^\lambda=E/D\) in reduced form.
The preceding denominator lemma gives \(E,D\in\mathbb Z_2[x]\), \(D(0)=1\), and \(E(0)=0\).
Its degree is \(\delta=\deg R=\deg(R-1)\).
The power-stable private-branch argument retained in C858 ensures that \(G\) is nonrational.
The same argument ensures \(R\) is nonconstant for a rational center.

The explicitly supplied approximants \(S T_t\) satisfy
\[
 G-S T_t\in2^{a(2t+1)+1}\mathbb Z_2[[x]],\qquad
 \rho(S T_t)=t\delta+O(1).                                 \tag{P18}
\]
Consequently the all-level elementary-divisor argument of C858, applied to the same shifted leading determinants \(\Delta_h(G)\), gives
\[
        v_2(\Delta_h(G))
             \ge\frac{a}{\delta}h^2+O(h).                 \tag{P19}
\]
To see the coefficient explicitly, choose \(t=\max(0,\lceil(s-a-1)/(2a)\rceil)\) at each precision \(s\).
Then the rational ranks are at most \(\delta s/(2a)+O(1)\).
Summing \(\max(h-r_s,0)\) over all positive precision levels gives \(a h^2/\delta+O(h)\).
All constants and the original input are fixed before \(h\) tends to infinity.

The actual \(G\), independently of the artificial center's zeros and poles, is holomorphic on \(|x|<H^{-4}\).
C858's Cauchy estimate therefore gives
\[
        \log|\Delta_h(G)|
          \le-h^2\log r+O(h\log h),\qquad 0<r<H^{-4}.
\]
Infinitely many of these integral determinants are nonzero by the same adopted nonrationality/Hankel criterion.
Comparing (P19), taking that subsequence, dividing by \(h^2\), and finally increasing \(r\) to \(H^{-4}\), proves the paid original-input consequence
\[
                  \log H\ge\frac{a\log2}{4\delta},
                  \qquad m(P)\ge\frac{a\log2}{4\delta}.    \tag{P20}
\]
This is a factor of two improvement over the fixed-binomial single-radical certificate with the same center, since its \(K_{\rm pole}\) equals \(\delta\).
It remains a house-based, generally degree-dependent certificate.

If the normalized residual additionally satisfies (P3), then (P5)--(P6) show that changing centers with precision, using arbitrary \(\mathbb Q_2\)-rational approximants, or allowing their coefficients and degrees to grow cannot improve the asymptotic rational-approximation rank slope used in this specific all-level/disk comparison.
This conclusion concerns that precise rational-rank route.
It does not assert that no other determinant divisibility argument or stronger complex estimate can improve (P20).

For the single-mask cases of C860 v4 Part E, with coherent starting polynomials \(B_0,C_0\) of degree less than \(d\), the exact \(\delta\) is its single-radical \(K_{\rm pole}\).
The Padé certificate (P20) is exactly twice its \(\eta\).
Therefore on a hypothetical near-one sequence satisfying \(\log\|B_0\|_1=o(d)\), its uniformly vanishing bounds (H4)--(H5) still imply a vanishing Padé certificate, even when the odd rotation prime grows.
When (P3) holds, this also excludes an improvement by arbitrary precision-dependent rational approximants of that same single radical within the same disk comparison.
When (P3) fails, the exact minimum-rank assertion is not available; residual numerator/denominator cancellation or degree loss modulo two remains a concrete possible source of a different rank profile.

## Multiple-radical boundary

Keep the original power-stable input, an odd prime \(q\), \(K=\mathbb Q(\zeta_q)\), a nonempty mask \(I\), its full Galois orbit \(O\), and the original \(D_J,N_J,G_J\) from C860 v4.
For each \(J\in O\), supply a rational center \(S_J\in K(x)\), regular at zero with \(S_J(0)=1\), and impose
\[
 \sigma(S_J)=S_{\sigma J}
 \quad\text{for every }\sigma\in\operatorname{Gal}(K/\mathbb Q).
\]
At every prime \(\mathfrak p\) of \(K\) above two, assume both \(S_J\) and \(S_J^{-1}\) belong to \(\mathcal O_{K_{\mathfrak p}}[[x]]\), and require one common valid depth \(\lambda\ge3\) such that
\[
 R_J=\frac{N_J}{D_JS_J^2},\qquad
 R_J-1\in2^\lambda x\mathcal O_{K_{\mathfrak p}}[[x]]
 \quad\text{for every }J\in O\text{ and every }\mathfrak p\mid2.
\]
These are supplied simultaneous arithmetic premises, not one-place Artin--Schreier consequences.
Let \(\delta_J=\deg R_J\), let \(h_J\) be the rational map degree of \(S_J\), and put \(a=\lambda-2\).
No good-reduction condition is required for the following upper bound.
Apply the even/odd polynomial formulas to \(R_J\) and form
\[
 F_t=\sum_{J\in O}S_J\,\frac{p_t(R_J)}{q_t(R_J)},\qquad
 f=\sum_{J\in O}G_J.
\]
The coefficientwise integral normalization and precision proof above apply in every completion \(K_{\mathfrak p}\).
Equivariance makes \(F_t\) rational over \(\mathbb Q\), and simultaneous local integrality makes its rational Taylor coefficients two-adically integral.
There is no division by a stabilizer order.
The resulting approximants satisfy
\[
  f-F_t\in2^{a(2t+1)+1}\mathbb Z_2[[x]],\qquad
  \rho(F_t)\le t\sum_{J\in O}\delta_J+\sum_{J\in O}h_J.
                                                               \tag{P21}
\]
This is a paid upper bound using the sum of component degrees.
It does not automatically inherit the old binomial denominator sharing across overlapping masks.
Its direct disk consequence is only
\[
               m(P)\ge
                 \frac{a\log2}{4\sum_{J\in O}\delta_J}.
\]
No exact trace-rank or minimum-rank assertion for these sums is proved here.
In particular the single-radical divisibility argument (P12)--(P15) cannot be applied to a sum of several radicals merely because its individual normalized residuals satisfy (P3).
Possible cancellation in the sum of normalized errors and overlap of reduced pole divisors must be controlled separately.
This is a remaining mathematical question, not an implicit extension of (P4).

## Actual mathematical status

The contributor checked the parity and dyadic normalization, both lower-bound degree cases, denominator normalization for arbitrary integral rational series, the center-composition identity, original-variable rank costs and the order of limits in the complex return.
These checks belong to the proof developer and supply no independent review.
No numerical experiment is a premise.
The good-reduction hypothesis, single-radical restriction and actual starting-center supply are explicit.
Neither an unrestricted positive total Mahler gap nor a counterexample family has been established.

## Current assessment
[Selected decision](#decision-whole-independent-review-2026-11-04)

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T21:05 |
| status | proved |
| reason | Adopt complete P1--P21 after independent R1076 v4: exact dyadic Pade normalization, ranks and all-precision minimum under explicit good reduction, fixed-unit and Cayley-composition identities, both boundary examples and the paid original-input return. Arbitrary single-radical rational approximants are covered only at the stated good-reduction scope; multiple-radical optimality and unrestricted near-one supply remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact general statement](#pade-statement) | Complete P1--P6, explicit good-reduction conditions, all integral Q2-rational approximants and integer precision levels, including the fixed rational-unit comparison. |
| argument | [Complete proof and consequences](#argument) | Entire P1--P21, denominator lemma, exact boundary examples, Cayley recentering, single-original-radical return and explicitly limited multi-radical consequence. |
| dependency | [Scaled-binomial input](Yin_C_G0860_v1.md#higher-depth-hankel-comparison) | Exact integral valuations and formal square-root remainder in the verified depth domain. |
| dependency | [Earlier rank and precision scope](Yin_C_G0860_v4.md#statement) | Formal rational-rank convention and the exact coherent low-degree/norm hypotheses and vanishing conclusion used in the doubled-certificate comparison. |
| dependency | [Original and finite Hankel inputs](Yin_C_G0858_v1.md#all-place-hankel-budget) | Original private-branch nonrationality, finite elementary-divisor implication and shifted leading-Hankel criterion; new centered integrality is checked here. |
| dependency | [Original disk comparison](Yin_C_G0858_v1.md#cauchy-radius-cost) | Same original radius, quadratic exponent, nonzero determinant sequence and fixed-input order of limits. |
| support | [Formal reduced rational rank](../audits/literature/Par88/Yin_U001.md#par88-u001) | Only the reduced minimal-recurrence mechanism at its retained qualification, extended by the explicit algebra over Q2, without bounded-operator use. |
| support | [Formal matrix convention](../audits/literature/BR10/Yin_U002.md#br10-u002) | Only the field-valued formal Hankel rank and coefficient-index convention. |
| review | [Independent whole Pade finding](../audits/reviews/Yin_R_G1076_v4.md#pade-minimum-rank-whole) | Complete new theorem and consequences, exact dependency/source interfaces, both Kou11 recurrence caveats and all original/multiple-radical limitations. |

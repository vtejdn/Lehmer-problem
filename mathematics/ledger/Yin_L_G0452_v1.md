---
author: Yin
---

# Finite cyclotomic logarithmic auxiliaries: the mean and radial budget tradeoff

Date: 2026-11-05.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating agent posed the input-dependent and growing-frequency auxiliary test; the responsible delegate derived and checked the finite Fourier constraint, budget tradeoff and explicit regularization comparison below.
These are ordinary author calculations and source-interface checks, not independent review, a new Claim assessment or Task completion.

<a id="finite-cyclotomic-budget-scope"></a>
## Question and relation to existing material

The question is whether a finite harmonic polynomial combined with nonnegative cyclotomic logarithms can eliminate the degree-sized constant cost while retaining a degree-uniform return to the original total logarithmic Mahler measure.
The coefficients, cyclotomic orders, number of factors and harmonic degree may depend on the original input.
[L10 v4](Yin_L_G0010_v4.md#cyclotomic-two-trace-bound) supplies the motivating fixed \(\Phi_6\) auxiliary, but its core result concerns the arithmetic price of a particular Pell moment prefix.
The present question concerns the costs of a class of auxiliary functions, and does not revise that prefix theorem.

The positive-Fourier-coefficient argument is already used in [C4](../claims/Yin_C_G0004_v1.md#coefficient-size-tail-control).
Its application here gives an explicit tradeoff for this different auxiliary and its stated radial envelope.
[C4's cyclotomic smoothing](../claims/Yin_C_G0004_v1.md#damped-cyclotomic-norm-inequalities), [C570's complete resultant bound](../claims/Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound), [C139's finite logarithmic transfer](../claims/Yin_C_G0139_v1.md#argument), and [C141's zero removal](../claims/Yin_C_G0141_v1.md#reuse-zero-removal) retain their original arithmetic and quantitative hypotheses.
[L133 v2](Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap) concerns separation between two integer cyclotomic blocks and a delayed-polynomial construction, rather than a finite harmonic correction with real nonnegative logarithmic weights.
These actual scopes distinguish the present exploration from the existing families.
No novelty claim about auxiliary functions, Fourier positivity or logarithmic regularization is made.

The result below excludes a cheap use of the explicitly defined envelope in a single-cyclotomic class, uniformly even as its order grows.
It gives a weaker quantified bound for multiple orders.
It is not a lower bound for an actual sum over original roots and does not exclude a different estimate using their correlations.

<a id="finite-log-auxiliary-setting"></a>
## Finite auxiliary and complete circle conventions

Let \(N\ge0\) and
\[
 A(z)=\sum_{n=1}^N a_nz^n,\qquad a_n\in\mathbb C.
\tag{1}
\]
Let \(q_1,\ldots,q_J\) be positive integers and \(b_1,\ldots,b_J\) positive real numbers, with \(J\) finite.
Zero-weight factors are omitted; repeated orders may either be retained or combined by adding their weights.
The empty list \(J=0\) is allowed.
Assume that a real \(c\) satisfies
\[
 H(z):=\Re A(z)-c+\sum_{j=1}^Jb_j\log|\Phi_{q_j}(z)|
                         \le0\qquad(|z|=1).
\tag{2}
\]
At any zero of a positive-weight factor the sum has value \(-\infty\).
A constant term in \(A\) has been subtracted from \(A\) and its real part absorbed into \(c\); thus \(A(0)=0\) is the normalization used throughout.

For a positive integer \(q\), define the real Ramanujan sum
\[
 c_q(n)=\sum_{\zeta\ {\rm primitive}\ q}\zeta^n.
\]
Reality follows by conjugating the complete primitive-root set, including the orders one and two.
Put
\[
 D=\sum_jb_j\varphi(q_j),\qquad
 B_n=\sum_jb_jc_{q_j}(n),\qquad
 \ell=\operatorname{lcm}(q_1,\ldots,q_J)
\tag{3}
\]
when \(J>0\).
For \(J=0\), put \(D=B_n=0\) and \(\ell=1\).
All later sums over roots, factors and coefficients retain their actual multiplicities and weights.

Each logarithm in (2) is integrable on the circle and has mean zero.
Indeed it is a finite sum of rotations of \(\log|1-e^{i\theta}|\), whose integral is zero.
The logarithmic integrability and its \(L^1\) Abel passage are the already retained [C1 circle-kernel calculation](../claims/Yin_C_G0001_v1.md#two-frequency-linear-coupling-control).
The constant coefficient of \(\Re A\) is zero, so
\[
                             \int_{\mathbb T}H=-c.
\tag{4}
\]
Here and below the circle measure is normalized Haar probability.
Consequently \(c\ge0\).

<a id="zero-mean-and-disk-extension"></a>
## Zero mean and the disk extension with real weights

If \(c=0\), (2)--(4) force \(H=0\) almost everywhere.
If any \(b_j>0\), choose a circle zero of its cyclotomic factor.
Near that point \(\Re A\) is bounded and all other logarithmic terms are bounded above, whereas the selected logarithm tends to \(-\infty\).
Thus \(H\) is strictly negative on an arc of positive measure, contradicting \(H=0\) almost everywhere.
It follows that \(J=0\).
Then \(\Re A=0\) on the circle, so all its nonconstant Fourier coefficients vanish and \(A=0\).
Therefore
\[
                 c=0\quad\Longrightarrow\quad J=0,\ A=0.
\tag{5}
\]
This conclusion applies separately to every finite input-dependent choice; it is not a positive uniform lower bound for \(c\) without a scale normalization.

For use on original roots one must extend (2) to the disk even when the weights are not integers and the coefficients of \(A\) are complex.
For each primitive root \(\zeta\), the number \(1-z/\zeta\) has positive real part when \(|z|<1\).
Use the holomorphic logarithm on that right half-plane, normalized to be zero at \(z=0\), and define
\[
 F(z)=\exp A(z)\prod_{j=1}^J
       \prod_{\zeta\ {\rm primitive}\ q_j}
       \exp\!\bigl(b_j\operatorname{Log}(1-z/\zeta)\bigr)
       \qquad(|z|<1).
\tag{6}
\]
This is a single-valued holomorphic function with \(F(0)=1\).
Since \(|\Phi_q(0)|=1\),
\[
                 \log|F(z)|=\Re A(z)+\sum_jb_j\log|\Phi_{q_j}(z)|.
\]
Away from the finitely many boundary zeros, every factor in (6) extends continuously to the circle.
At a boundary zero, a positive-weight factor has modulus tending to zero; all other factors are bounded and its argument remains bounded in the chosen half-plane branch.
Thus \(F\) extends continuously there by zero.
Equation (2) gives \(|F|\le e^c\) on the entire boundary, including those zero values.
The maximum modulus principle therefore proves
\[
                              H(z)\le0\qquad(|z|\le1).
\tag{7}
\]
In particular \(H(0)=-c\), so a zero original root causes no inverse or logarithm-of-zero problem.

The maximum modulus input is the same established interface actually inspected for [L10 v4](Yin_L_G0010_v4.md#phi-six-circle-auxiliary): Jacob Shapiro, Complex Analysis with Applications, MAT330 Spring 2023 notes, typeset 14 May 2023, Sha23, Corollary 7.52 on printed/PDF page 88 and its proof on page 89.
Those passages in the retained PDF were directly text-read in the preceding bounded test and are reused at that unchanged scope.
For (6), holomorphy in the disk, continuity on its compact closure and the boundary bound were verified explicitly above; the constant-function case has the same bound directly.
No audit of the complete notes or their proof dependencies is claimed.

<a id="finite-log-fourier-constraint"></a>
## Fourier positivity fixes the uncancelled coefficients

With Fourier convention \(\widehat f(n)=\int_{\mathbb T} f(z)z^{-n}\), the cyclotomic logarithm has coefficient
\[
             \widehat{\log|\Phi_q|}(n)=-\frac{c_q(n)}{2n}
                           \qquad(n\ge1).
\tag{8}
\]
This follows by summing the elementary logarithmic power series over the complete primitive-root set and taking its \(L^1\) Abel limit.
The conjugate root sum equals the same real \(c_q(n)\).
The retained C1 endpoint and C4 cyclotomic convention justify this finite-factor passage without asserting pointwise convergence at a circle zero.

Let \(U=-H\).
It is a nonnegative integrable function with mean \(c\).
Extend \(a_n\) by zero for \(n>N\).
Then
\[
                 \widehat U(n)=\frac12(B_n/n-a_n),
                 \qquad |\widehat U(n)|\le\int_{\mathbb T}U=c,
\]
and therefore
\[
                       \boxed{|a_n-B_n/n|\le2c\qquad(n\ge1).}
\tag{9}
\]
This is exactly the positive-Fourier-coefficient method already retained in C4, applied to the current \(U\).
It requires neither integral coefficients for \(A\) nor integer weights \(b_j\).

<a id="full-original-root-radial-envelope"></a>
## The stated radial envelope and every original root

For \(|z|=r>1\), put \(w=1/\bar z\).
For every \(|\zeta|=1\),
\[
                             |z-\zeta|=r|w-\zeta|.
\]
Multiplication over every primitive root gives
\[
                      |\Phi_q(z)|=r^{\varphi(q)}|\Phi_q(w)|.
\tag{10}
\]
Neither \(z\) nor \(w\) is a zero of these cyclotomic polynomials.
If \(z=re^{i\theta}\), then \(w=r^{-1}e^{i\theta}\), so
\[
 \Re\bigl(A(z)-A(w)\bigr)
       \le\sum_{n=1}^N|a_n|(r^n-r^{-n}).
\]
This reflection keeps the same angle and is valid for complex \(a_n\).
Equations (7) and (10) imply
\[
 H(z)\le R(\log r),\qquad
 R(t):=Dt+2\sum_{n=1}^N|a_n|\sinh(nt)\quad(t\ge0).
\tag{11}
\]
The function \(R\) is nonnegative, vanishes at zero, and is superadditive on nonnegative arguments because each hyperbolic sine is superadditive there.

Let \(P\in\mathbb Z[X]\) be monic of degree \(d\ge0\), with every root \(\alpha_i\) counted with its full multiplicity.
Assume it is relatively prime to every positive-weight \(\Phi_{q_j}\).
Put
\[
 s_n=\sum_i\alpha_i^n,\qquad
 m(P)=\sum_i\log^+|\alpha_i|,\qquad
 \Delta_A(P)=\Re\sum_{n=1}^N a_ns_n-cd,
\tag{12}
\]
where \(\log^+0=0\).
The nonzero full resultants are rational integers, and
\[
\begin{aligned}
 \Delta_A(P)+\sum_jb_j\log|\operatorname{Res}(P,\Phi_{q_j})|
 &=\sum_iH(\alpha_i)\\
 &\le\sum_{|\alpha_i|>1}R(\log|\alpha_i|)\\
 &\le R(m(P)).
\end{aligned}
\tag{13}
\]
Every root and logarithmic weight remains in the equality.
Roots in the closed disk contribute nonpositively; zero roots have \(H(0)=-c\).
The empty root list and \(P=1\) obey the same formulas.
The arithmetic floor in each logarithmic resultant is zero, not an automatically supplied positive amount proportional to \(d\).

The traces \(s_n\) are integers, but arbitrary complex \(a_n\) and real \(c\) do not make \(\Delta_A(P)\) an integer.
Any discrete positive-certificate claim must retain its actual coefficient normalization and, when applicable, its denominator.
Multiplying \(A,c,b_j\) by a positive scalar scales both sides and every possible arithmetic income by that scalar.
Shrinking the weights alone is therefore no gain.

<a id="mean-times-radial-slope-bound"></a>
## The explicit mean-times-slope tradeoff

Define the zero-point slope of the stated envelope by
\[
                         K=R'(0)=D+2\sum_{n=1}^Nn|a_n|.
\tag{14}
\]
Assume \(J>0\), so \(D>0\) and (5) gives \(c>0\).
At every positive multiple of \(\ell\), each primitive root has that power equal to one, so
\[
                              B_{\ell k}=D\qquad(k\ge1).
\tag{15}
\]
It follows from (9) that
\[
                              \boxed{cK\ge D^2/(4\ell).}
\tag{16}
\]

Here is the full finite proof.
If \(c\ge D/(4\ell)\), use \(K\ge D\).
Otherwise put
\[
 x=\frac{D}{4c\ell}>1,\qquad
 J_0=\lfloor N/\ell\rfloor,\qquad M=\lfloor x\rfloor.
\]
The index \(\ell(J_0+1)>N\) has \(a_{\ell(J_0+1)}=0\).
Equations (9) and (15) give
\[
              \frac{D}{\ell(J_0+1)}\le2c,\qquad
              J_0\ge2x-1\ge x,
\]
hence \(M\le J_0\).
For \(1\le k\le M\), the reverse triangle inequality in (9) gives
\[
        \ell k|a_{\ell k}|
                    \ge D-2c\ell k\ge D/2.
\]
Retaining just these actual coefficient positions in (14), obtain
\[
                   K\ge D+MD=D(1+M)>Dx=\frac{D^2}{4c\ell}.
\]
This proves (16) in the remaining case.
If \(J=0\), its right-hand side is zero and no positive tradeoff is claimed.

For a single term \(b\log|\Phi_q|\), (16) becomes
\[
                 cK\ge \frac{b^2\varphi(q)^2}{4q}\ge\frac{b^2}{8}.
\tag{17}
\]
The second inequality is uniform over every positive integer \(q\).
Indeed, multiplicativity gives
\[
                 \frac{\varphi(q)^2}{q}
                 =\prod_{p^e\parallel q}p^{e-2}(p-1)^2.
\]
For odd \(p\) each factor is at least \(4/3\).
For \(p=2\) the only factor below one occurs at \(e=1\) and equals \(1/2\); the empty product for \(q=1\) equals one.
This proves the lower bound \(1/2\) used in (17).

The \(\Phi_6\) term with weight \(b=1/2\) from L10 v4 consequently satisfies \(cK\ge1/24\), regardless of which new finite \(A\) is chosen.
For the complete cyclotomic product \(b\log|1-z^q|\), use \(\sum_{r\mid q}\varphi(r)=q\) and \(\operatorname{lcm}_{r\mid q}r=q\) in (16) to obtain
\[
                               cK\ge b^2q/4.
\tag{18}
\]

For fixed positive \(b\), requiring \(cd\le B\) with a fixed \(B>0\) in the single-cyclotomic case forces \(K\ge b^2d/(8B)\).
Since \(\sinh(nt)\ge nt\),
\[
                                  R(t)\ge Kt\qquad(t\ge0).
\tag{19}
\]
Thus this exact envelope cannot then obey \(R(t)\le Ct\) on any positive interval with a degree-independent \(C\).
A bound on \(K\) is only necessary for such an upper comparison; it is not sufficient because high frequencies may further enlarge \(R(t)\) away from zero.

For multiple orders, (16) retains the actual \(\ell\).
If \(\ell\) grows much faster than \(D^2\), its right-hand side can become small, and no uniform exclusion follows from this argument.
Positive logarithmic weights can cancel some Ramanujan coefficients; the proof only uses their common positive values at multiples of \(\ell\).
Whether orthogonality of the Ramanujan sums can yield a useful bound without this least-common-multiple dependence remains an untested possibility here; no such estimate is used.
Neither that cancellation nor an input-dependent selection has supplied a positive original arithmetic certificate here.
Most importantly, (16)--(19) concern the envelope (11), not a necessary lower bound on the actual sum \(\sum_iH(\alpha_i)\).
A different estimate exploiting root correlations or cancellation remains outside this obstruction.

<a id="abel-truncation-complete-cost"></a>
## An actual small-mean family and all of its costs

Take the single logarithm \(\log|1-z|=\log|\Phi_1(z)|\) with weight one.
For \(0<t<1\), define
\[
 A_{t,N}(z)=\sum_{n=1}^N\frac{t^nz^n}{n},\qquad
 A_{t,\infty}(z)=-\operatorname{Log}(1-tz).
\tag{20}
\]
The infinite series is absolutely convergent on the unit circle.
Writing \(x=\cos\theta\), one has
\[
 \left|\frac{1-e^{i\theta}}{1-te^{i\theta}}\right|^2
                  =\frac{2-2x}{1+t^2-2tx}.
\]
Its derivative with respect to \(x\) is \(-2(1-t)^2/(1+t^2-2tx)^2\), so its maximum occurs at \(x=-1\).
Consequently the exact circle maximum for the infinite correction is
\[
             c_t=\log\frac2{1+t},\qquad
             \Re A_{t,\infty}(z)+\log|1-z|\le c_t.
\tag{21}
\]
At \(z=1\) the logarithmic term is \(-\infty\), with no missing boundary case.

The tail on the circle has the finite upper bound
\[
 \left|A_{t,\infty}-A_{t,N}\right|
       \le E_{t,N}:=\frac{t^{N+1}}{(N+1)(1-t)}.
\]
Thus the finite polynomial in (20) satisfies (2) with
\[
       c=c_t+E_{t,N},\qquad
       R_N(u)=u+2\sum_{n=1}^N\frac{t^n}{n}\sinh(nu),\qquad
       K_N=1+\frac{2t(1-t^N)}{1-t}.
\tag{22}
\]
These are costs of an actual finite auxiliary, with the complete coefficients and frequency cutoff.

Put \(t=e^{-\eta}\), where \(0<\eta<1\) tends to zero, and choose
\[
                  N=\left\lceil2\eta^{-1}\log(1/\eta)\right\rceil.
\]
Then \(E_{t,N}=o(\eta)\), \(c_t\sim\eta/2\), and \(K_N\sim2/\eta\).
Hence
\[
                              c\sim\eta/2,\qquad cK_N\to1.
\tag{23}
\]
For example, taking \(\eta=1/d\) gives \(cd\to1/2\) while \(K_N\sim2d\) and \(N\sim2d\log d\).
The degree-sized mean cost is genuinely reduced in this construction, but the specified radial envelope loses a degree-uniform slope.

The infinite coefficient envelope is finite exactly in its stated positive-argument range \(0\le u<\eta\):
\[
\begin{aligned}
 R_\infty(u)
 &=u+\sum_{n\ge1}\frac{(te^u)^n-(te^{-u})^n}{n}\\
 &=u+\log\frac{1-te^{-u}}{1-te^u},\qquad
 R_\infty'(0)=\frac{1+t}{1-t}.
\end{aligned}
\tag{24}
\]
At \(u\ge\eta>0\), the first positive series diverges, so this infinite envelope gives no finite return.
At \(u=0\) it is zero as displayed.
In particular, choosing \(\eta=1/d\) does not justify using (24) for an arbitrary hypothetical sequence with \(m(P)\to0\); that would also require \(m(P)<1/d\).
The finite envelope (22) remains valid without that extra hypothesis, but retains every growing-frequency term.

The exact relation to C4's retained Abel smoothing cost is
\[
                 c_t=\eta/2-\log\cosh(\eta/2)\le\eta/2,
                 \qquad -\tfrac12\log t=\eta/2.
\tag{25}
\]
Thus the improvement in the circle constant does not remove the old \(d\eta\) scale or the subsequent truncation and radial costs.

<a id="rational-regularization-and-zero-boundary"></a>
## Rational denominators, formal cancellation and zero removal

Using the full logarithm at a rational parameter does not supply a free integer norm.
If \(t=p/v\) with integers \(0<p<v\), then, whenever both resultants are nonzero,
\[
 \sum_i\bigl(\log|1-\alpha_i|-\log|1-t\alpha_i|\bigr)
  =\log|\operatorname{Res}(P,1-X)|
   -\log|\operatorname{Res}(P,v-pX)|+d\log v.
\tag{26}
\]
The right side is the difference of logarithms of two nonzero integers, together with the actual denominator term.
The second norm has a negative sign and cannot be dropped in a lower-income argument.
At a zero of either polynomial this finite identity is unavailable.
Even away from those zeros, using the absolutely convergent trace series from (20) at every original root would require \(t|\alpha_i|<1\) for every \(i\); the sufficient condition \(m(P)<-\log t\) keeps that restriction visible.
The absolute-value product identity (26) itself needs only its displayed nonvanishing conditions.

Likewise, the formal analytic choice
\[
 A(z)=-\sum_jb_j\operatorname{Log}
                    \bigl(\Phi_{q_j}(z)/\Phi_{q_j}(0)\bigr)
\]
would make the corresponding real parts cancel identically in the open disk.
It has boundary logarithmic singularities and is not a finite polynomial or a bounded continuous correction at the relevant boundary zeros.
Its Taylor series has radius one when a positive-weight factor is present, and does not supply an absolutely convergent original-trace sum at expanding conjugates.
This observation does not contradict (5); it changes the class and leaves precisely the missing continuation, tail or arithmetic denominator control.

For the finite class, a monic irreducible nontorsion original polynomial is relatively prime to every cyclotomic auxiliary, so zero removal gives no further case on that domain.
For a reducible \(P\), remove all shared cyclotomic factors into a monic \(C\) and write \(P=CP_0\).
Then \(m(P)=m(P_0)\), but the exact trace functional changes by
\[
                            \Delta_A(P)=\Delta_A(P_0)+\Delta_A(C).
\tag{27}
\]
Only \(P_0\) has the nonzero resultants required in (13).
There is no general reason for \(\Delta_A(C)\) to vanish.
The zero contribution of each removed \(\Phi_6\) in L10 v4 is its particular computed identity, not a general removal rule for a different \(A,c\) or several factors.

<a id="finite-log-budget-original-return"></a>
## Existing arithmetic transfer and the remaining original-input issue

The accepted [C139 statement](../claims/Yin_C_G0139_v1.md#statement) requires a supplied bounded-term, bounded-coefficient, degree-linear auxiliary \(F\), an actual nonzero algebraic integer \(F(\alpha)/q\), and a fixed positive margin \(m(F)\le\log q-\eta\).
Its complete finite majorant retains the frequency \(JT\), coefficient cost \(2^J\), regularization parameter and radial cost.
Those hypotheses provide genuine \(d\log q\) norm income; ordinary nonzero cyclotomic resultants in (13) only provide the zero floor.
The present circle construction does not automatically supply C139's stronger arithmetic data.

[C141's exact zero-removal argument](../claims/Yin_C_G0141_v1.md#reuse-zero-removal) assembles the existing short-annihilator theorem with that supplied-class result.
Its [finite-prime avoidance theorem](../claims/Yin_C_G0141_v1.md#statement) concerns actual inputs whose measure is explicitly bounded away from zero; it does not refute an auxiliary theorem restricted to sufficiently small total measure.
Neither result removes the original-input supply obligation.
[C570](../claims/Yin_C_G0570_v1.md#congruence-only-net-income-gate) likewise retains the same auxiliary's full norm income, coefficient energy, effective support and degree expense.

The single-cyclotomic test therefore returns to a quantified mean-versus-radial cost within the envelope (11), and the explicit Abel family exhibits that cost directly.
The multi-order bound is only (16), with its genuine least-common-multiple limitation.
No positive certificate useful on every original small-total-measure input, new source of integral income, or strict counterexample to the original Task has been obtained.
An actual correlated estimate with uniformly paid costs or a different automatically supplied arithmetic object would be a new obligation, rather than a consequence of cancelling formal circle means.

The author checked the normalization of \(A(0)\), logarithmic integrability, real-weight branches and continuity, complex-coefficient reflection, all-root multiplicities and nonvanishing, Fourier factors of two, every cutoff in (16), the totient product bound, the explicit Abel maximum and tail, the infinite-series domain, denominator signs and the exact zero-removal correction.
The literature reuse is confined to the stated C1, C4, C570, C139, C141 and Sha23 interfaces; no new external theorem, numerical experiment, native computation or independent review is asserted.

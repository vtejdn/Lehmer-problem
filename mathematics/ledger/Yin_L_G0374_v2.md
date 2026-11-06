---
author: Yin
---

# Cyclotomic stabilization of integer central descent: critical barriers and complete root cost

Date: 2026-11-06.
This ordinary author exploration for Yin tests whether multiplying the Lehmer trace polynomial by a growing cyclotomic trace factor can make a unit central-coefficient move preserve the real trace spectrum and lower the complete positive Mahler measure.
It extends the central-descent topic of [L374 v1](Yin_L_G0374_v1.md#central-descent-source-and-domain), whose fixed argument and review scope remain unchanged.
The main research agent proposed the stabilization question, and the assigned bottleneck-diagnosis agent developed and checked the construction and its full costs.
A second participating agent checked the conditional Jensen formula and its singular-point treatment within the same author discussion.
These are ordinary author contributions and checks, not a formal project review, independent-review finding, new Claim adoption or resolution of the unrestricted Lehmer goal.

<a id="stabilization-inputs-and-question"></a>
## Exact question, inputs and reuse boundary

The adopted [C414 central-descent argument](../claims/Yin_C_G0414_v1.md#argument) treats a fixed genuine Salem trace polynomial and a constant shift.
Its [Rolle criterion](../claims/Yin_C_G0414_v1.md#real-trace-shift-criterion) and [Lehmer calibration](../claims/Yin_C_G0414_v1.md#capacity-and-lehmer-central-control) are the directly used elementary inputs.
The present object changes the trace polynomial itself by multiplication before taking the unit shift.
Because that product is reducible, the irreducible-source statement of C414 is not invoked wholesale; the needed real-root and Rolle arguments are established directly below.

Let
\[
\begin{aligned}
P_L(z)&=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1,\\
Q(y)&=y^5+y^4-5y^3-5y^2+4y+3,\\
P_L(z)&=z^5Q(z+z^{-1}).
\end{aligned}                                                     \tag{1}
\]
The accepted original Lehmer input is monic, irreducible and reciprocal, with one real exterior root \(\beta>1\), its inverse, and eight unit-circle roots that are not roots of unity.
Consequently \(Q\) has four distinct roots in \((-2,2)\) and one root
\[
x_0=\beta+\beta^{-1}>2,\qquad m(P_L)=\log\beta.
\]
The identity
\[
Q(y)+1=(y^2-4)(y+1)^2(y-1)
\]
gives \(Q(2)=Q(-2)=-1\) and \(Q'(2)=36\).
It is the existing calibration in C414, not a new factorization claim.

For an integer \(N\ge1\), select only the first-kind Chebyshev trace factor
\[
C_N(y)=2T_N(y/2),\qquad
C_N(z+z^{-1})=z^N+z^{-N}.
\]
The recurrence \(C_0=2\), \(C_1=y\), \(C_{N+1}=yC_N-C_{N-1}\) shows that \(C_N\) is monic integral of degree \(N\) for \(N\ge1\).
Its simple roots are
\[
2\cos\frac{(2j-1)\pi}{2N},\qquad 1\le j\le N,
\]
and
\[
z^NC_N(z+z^{-1})=z^{2N}+1
\]
is an actual cyclotomic product.
Set
\[
H_N(y)=Q(y)C_N(y),\qquad
A_{N,\varepsilon}(z)
=z^{N+5}\bigl(H_N(z+z^{-1})+\varepsilon\bigr),
\qquad \varepsilon\in\{1,-1\}.
\]
The exact lift is
\[
\boxed{\;
A_{N,\varepsilon}(z)
=P_L(z)(z^{2N}+1)+\varepsilon z^{N+5}.
\;}                                                               \tag{2}
\]
It is monic integral reciprocal of actual degree \(2N+10\), with constant term \(1\).
No irreducibility of the output is assumed, and all root and factor multiplicities remain charged.
The two signs, all integers \(N\ge1\), and this specific \(C_N\) stabilizer are the entire construction under examination.

<a id="stabilization-positive-root-and-floor"></a>
## Positive output, the unique real exterior trace and an explicit floor

The roots of \(Q\) and \(C_N\) are disjoint.
Indeed a common trace root would lift to a root of both \(P_L\) and \(z^{2N}+1\), contradicting the accepted noncyclotomic irreducible Lehmer input.
Thus \(H_N\) has \(N+5\) distinct real roots, exactly one of them above \(2\), namely \(x_0\), and all others in \((-2,2)\).
Its \(N+4\) derivative roots are simple and strictly interlace these roots.
In particular, no derivative root is at or below \(-2\), and at most the last derivative root can be above \(2\).

For either sign,
\[
H_N(2)+\varepsilon=-2+\varepsilon<0,\qquad
H_N(-2)+\varepsilon=-2(-1)^N+\varepsilon.                          \tag{3}
\]
The second expression has sign \((-1)^{N+5}\), the sign of the monic degree-\(N+5\) polynomial at negative infinity.
On \((-\infty,-2]\) there is no critical point, so the shifted polynomial has no root there.
On \([2,\infty)\), it is either strictly increasing, or first decreases to its last minimum and then strictly increases.
Its value at \(2\) is negative, so it has exactly one root \(x_{N,\varepsilon}>2\), on the final increasing branch.
This root is simple, and there is no endpoint root at either \(2\) or \(-2\).

At \(x_0\), the shifted value is \(\varepsilon\).
The signs in (3), uniqueness, and the positive leading coefficient therefore give
\[
2<x_{N,+}<x_0<x_{N,-}.                                           \tag{4}
\]
Each output is positive in logarithmic Mahler measure, irrespective of any nonreal trace roots.
In particular the minus move satisfies
\[
m(A_{N,-})>\log\beta=m(P_L)
\quad\text{for every }N\ge1.                                    \tag{5}
\]

There is also an explicit uniform bound for the whole output that requires no sparse-polynomial theorem.
Let
\[
x_*=\frac{201}{100}.
\]
Substitution into (1) gives the exact rational identities
\[
Q(x_*)=-\frac{6330568899}{10^{10}},\qquad
x_*Q(x_*)+1=-\frac{272444348699}{10^{12}}<0.                      \tag{6}
\]
For \(y>2\), put
\[
\rho(y)=\frac{y+\sqrt{y^2-4}}2>1.
\]
Then \(C_N(y)=\rho(y)^N+\rho(y)^{-N}\ge C_1(y)=y\) for every \(N\ge1\).
Since \(Q(x_*)<0\),
\[
H_N(x_*)+\varepsilon
\le Q(x_*)x_*+1<0.
\]
The unique root to the right of \(2\) consequently lies to the right of \(x_*\), and
\[
\boxed{\;
m(A_{N,\varepsilon})
\ge\operatorname{arcosh}(x_{N,\varepsilon}/2)
>\operatorname{arcosh}(201/200)>0.
\;}                                                               \tag{7}
\]
Equations (6) are direct polynomial substitutions, not numerical approximations or results of a parameter scan.

The decrease of the selected real root under the plus move is not sustained as \(N\) grows.
For \(2<y<x_0\), \(Q(y)<0\), while \(C_N(y)\) is strictly increasing in \(N\) and tends to infinity.
At \(x_{N,+}\), this gives \(H_{N+1}(x_{N,+})+1<0\), so uniqueness implies \(x_{N+1,+}>x_{N,+}\).
For any fixed \(2<t<x_0\), eventually \(H_N(t)+1<0\), hence \(x_{N,+}>t\).
Similarly \(Q(y)>0\) for \(y>x_0\), so the minus root strictly decreases with \(N\), and eventually lies below every fixed \(t>x_0\).
Thus
\[
x_{N,+}\uparrow x_0,\qquad x_{N,-}\downarrow x_0.                 \tag{8}
\]
Both selected real-root costs tend to \(\log\beta\).

<a id="stabilization-critical-barrier-loss"></a>
## Exact critical criterion and the new weak barriers

Define
\[
a_N=\min_{\substack{H_N'(c)=0\\c\ {\rm a\ local\ minimum}}}
          \bigl(-H_N(c)\bigr),\qquad
b_N=\min_{\substack{H_N'(c)=0\\c\ {\rm a\ local\ maximum}}}
          H_N(c).
\]
Every unshifted local minimum is negative and every local maximum positive.
Both sets are nonempty because \(H_N\) has at least six distinct real roots.
The unchanged simple derivative roots give the exact conditions
\[
\begin{aligned}
H_N+1\text{ has all roots real, with multiplicities}
   &\iff a_N\ge1,\\
H_N-1\text{ has all roots real, with multiplicities}
   &\iff b_N\ge1.
\end{aligned}                                                     \tag{9}
\]
For sufficiency, the extrema have the alternating weak signs needed to supply all roots on their monotonicity intervals.
A critical equality is an exactly double root, since the derivative root is simple.
For necessity, if all roots are real, Rolle counting exhausts the unchanged derivative roots and forces every local minimum to be nonpositive and every local maximum nonnegative.
This is the elementary argument of the cited C414 criterion, now applied directly to the product \(H_N\).

When either condition in (9) holds, (3) and the exterior-root argument show that every other trace root lies in \((-2,2)\).
Then the complete measure is exactly
\[
m(A_{N,\varepsilon})=\operatorname{arcosh}(x_{N,\varepsilon}/2).
\]
In particular a plus output satisfying (9) would be a genuine positive descent in total measure.
Failure of (9) alone does not determine the sign of the total measure change; the new nonreal roots must be charged separately.

To test whether stabilization raises all dangerous barriers, use the fixed interior root \(a\) of \(Q\) in \((9/10,1)\).
The exact values
\[
\begin{gathered}
Q(-2)=-1,\quad Q(-3/2)=3/32,\quad Q(-1)=-1,\quad Q(0)=3,\\
Q(9/10)=15159/100000>0,\qquad Q(1)=-1
\end{gathered}
\]
locate three negative roots and the root \(a\); together with \(x_0\), they exhaust the degree.
Hence \(a\) is the only \(Q\)-root in \([1/2,3/2]\).

For \(N\ge16\), let \(u_N<a<v_N\) be the adjacent \(C_N\)-roots bracketing \(a\).
Their existence follows from the displayed Chebyshev roots, and the cosine parametrization gives
\[
v_N-u_N\le\frac{2\pi}{N}.
\]
Since \(2\pi/16<2/5\), both roots lie in \([1/2,3/2]\).
The intervals \((u_N,a)\) and \((a,v_N)\) are consecutive root intervals of \(H_N\), with opposite signs.
Strict derivative interlacing supplies exactly one critical point in each interval, one positive local maximum and one negative local minimum.

On \([-2,2]\), the direct coefficient bound
\[
|Q'(y)|
=|5y^4+4y^3-15y^2-10y+4|
\le80+32+60+20+4=196
\]
and the inequality \(|C_N(y)|\le2\) imply, throughout these two intervals,
\[
|H_N(y)|
\le2\cdot196\,|y-a|
\le\frac{784\pi}{N}.
\]
Consequently
\[
0<a_N\le\frac{784\pi}{N},\qquad
0<b_N\le\frac{784\pi}{N}
\quad(N\ge16).                                                   \tag{10}
\]
In particular \(N\ge2500\) forces both bounds below \(1\), so neither unit shift retains an all-real trace spectrum.
The explicit threshold is sufficient, not optimized.
This is a concrete failure of the proposed barrier-lifting mechanism: inserting denser cyclotomic trace roots creates a small positive and a small negative critical barrier beside a fixed old interior trace root.

<a id="stabilization-complete-root-account"></a>
## Complete root accounting and the strictly more expensive limit

For any complex trace value \(t\), define
\[
\ell(t)=
\log\max\left\{
\left|\frac{t+\sqrt{t^2-4}}2\right|,
\left|\frac{t-\sqrt{t^2-4}}2\right|
\right\}.
\]
Changing the square-root branch exchanges the two entries.
Their product has absolute value \(1\), so \(\ell(t)\ge0\).
The quantity vanishes exactly when \(t\) is real and belongs to \([-2,2]\).
Each trace root, counted with its multiplicity, supplies the two roots of \(z^2-tz+1\).
For the monic lift (2), it follows that
\[
m(A_{N,\varepsilon})
=\operatorname{arcosh}(x_{N,\varepsilon}/2)+E_{N,\varepsilon},
\qquad
E_{N,\varepsilon}
=\sum_{\substack{t:\ H_N(t)+\varepsilon=0\\t\notin\mathbb R}}\ell(t)
\ge0,                                                           \tag{11}
\]
where the sum includes all multiplicities.
There are no other real exterior trace roots by (3).
Thus (11) charges every new nonreal conjugate pair, rather than identifying the full measure with the selected real-root cost after the trace shape has failed.

For an exact asymptotic account, use the fixed two-variable polynomial
\[
F_\varepsilon(z,w)
=P_L(z)(w^2+1)+\varepsilon z^5w.
\]
Equation (2) gives \(A_{N,\varepsilon}(z)=F_\varepsilon(z,z^N)\).
The shortest nonzero integer relation for \((1,N)\) has sup norm \(N\).
The accepted full Lawton theorem therefore gives
\[
m(A_{N,\varepsilon})\longrightarrow m_2(F_\varepsilon)
\quad\text{as }N\longrightarrow\infty.                           \tag{12}
\]
This uses the polynomial theorem including torus zeros, not the nonvanishing-only determinant approximation.

For \(z=e^{i\theta}\), write
\[
q(\theta)=Q(2\cos\theta)\in\mathbb R,\qquad
P_L(e^{i\theta})=e^{5i\theta}q(\theta).
\]
For \(q\ne0\), the conditional \(w\)-polynomial differs by a modulus-one scalar from
\[
q(w^2+1)+\varepsilon w
=q\bigl(w^2+(\varepsilon/q)w+1\bigr).
\]
Its two roots have product \(1\).
They are on the unit circle when \(|q|\ge1/2\), and otherwise their total positive logarithmic root cost is \(\operatorname{arcosh}(1/(2|q|))\).
Jensen's formula thus yields
\[
m_w(F_\varepsilon(e^{i\theta},w))
=\log|q(\theta)|+
\begin{cases}
\operatorname{arcosh}(1/(2|q(\theta)|)),&0<|q(\theta)|<1/2,\\
0,&|q(\theta)|\ge1/2.
\end{cases}                                                     \tag{13}
\]
The sign \(\varepsilon\) has no effect on this expression.

At \(q=0\), the conditional polynomial is a modulus-one scalar times \(\varepsilon w\), so its measure is \(0\).
Moreover the sum on the right of (13) tends to \(0\) as \(q\to0\).
Separately, both terms in (13) are integrable: \(q\) is a nonzero trigonometric polynomial with finitely many finite-order zeros, and
\[
0\le\operatorname{arcosh}(1/(2|q|))
\le\log(1/|q|)
\quad(0<|q|<1/2).
\]
Thus the finite zero set contributes no missing term.
The usual polynomial Mahler integral and conditional Jensen/Fubini calculation apply with these logarithmic singularities retained.

Define \(h(q)=\operatorname{arcosh}(1/(2|q|))\) for \(0<|q|<1/2\), and \(h(q)=0\) for \(|q|\ge1/2\).
Its values at the finite set \(q=0\) may be assigned arbitrarily for integration.
Integrating (13), and using \(\int\log|q(\theta)|\,d\theta/(2\pi)=m(P_L)\), gives
\[
\boxed{\;
m_2(F_\varepsilon)=m(P_L)+\Delta_C,\qquad
\Delta_C=\frac1{2\pi}\int_0^{2\pi}h(Q(2\cos\theta))\,d\theta>0.
\;}                                                               \tag{14}
\]
The strict positivity follows because any interior trace root of \(Q\) produces a nonempty open arc on which \(0<|q|<1/2\).
The integral is finite by the preceding singularity estimate.
Combining (8), (11), (12) and (14) gives the complete conclusion
\[
m(A_{N,\varepsilon})\longrightarrow m(P_L)+\Delta_C>m(P_L),
\qquad E_{N,\varepsilon}\longrightarrow\Delta_C>0.                \tag{15}
\]
In particular both signs eventually have total measure larger than the seed, although the plus sign always has a smaller selected real exterior root.

<a id="stabilization-source-scope"></a>
## Source applicability and existing mechanisms

The full original degree-ten Lehmer polynomial, trace spectrum and elementary constant-shift argument were read in [C414](../claims/Yin_C_G0414_v1.md#central-descent-source-and-domain), with the existing [L374 v1](Yin_L_G0374_v1.md#central-descent-source-and-domain) retained as the earlier topic account.
Their previous formal reviews do not automatically cover the changed product \(QC_N\) or this new exploration.

The precise external input in (12) is Lawton's full fixed-polynomial specialization theorem as recorded in [Den09 U002](../audits/literature/Den09/Yin_U002.md#den09-u002), Theorem 14 and Example 15 of arXiv:0905.0604v1, 5 May 2009.
It allows arbitrary integer specialization vectors with the sup-norm relation length tending to infinity and includes torus zeros.
The source record accepts that theorem at its stated interface; Lawton's original proof is not claimed to have been independently audited here.
No effective convergence rate, uniformity over changing templates or theorem about individual irreducible factors is imported.

The local comparison also read the applicable fixed-template discussion in [L133 v2](Yin_L_G0133_v2.md).
The use of fixed-template Lawton and conditional Jensen is an existing mechanism; this note supplies its exact specialization and full extra-cost formula for (2), not a new general limit theorem.
No primary-source acquisition or new PDF proof inspection was performed for this test.

As a separate existing filter, (2) has at most \(2\cdot9+1=19\) nonzero coefficients, including all overlaps and cancellations.
The accepted [DS17 fixed-support input](../audits/literature/DS17/Yin_U001.md#ds17-u001) therefore supplies some positive \(\eta_{19}\) with \(m(A_{N,\varepsilon})\ge\eta_{19}\), since positivity has already been proved.
This uses total logarithmic measure of the actual integer output and does not require irreducibility.
No numerical value for \(\eta_{19}\) or new source-proof audit is asserted.
The explicit bound (7) already proves the needed whole-output floor without this additional external input.

<a id="stabilization-factor-boundary-and-outcome"></a>
## What fails and what remains possible

The proposed \(C_N\) stabilization does not raise every dangerous critical barrier.
Equations (9)--(10) show that both unit shifts eventually destroy the all-real trace shape.
The plus move shrinks the unique positive real exterior root, but that gain tends to zero and the full nonreal-root cost tends to the strictly positive amount in (14).
The minus move already increases the real-root cost for every \(N\).
Equations (7) and (15) exclude a sequence of these complete outputs with positive total logarithmic measure tending to zero.

This does not prove that every finite small-\(N\) plus output has measure at least \(m(P_L)\).
No finite parameter scan, exhaustive critical classification below the displayed threshold or irreducibility classification was performed.
The question of a finite plus descent is distinct from the ruled-out asymptotic whole-output mechanism.

Most importantly, a lower bound on the whole measure is not a lower bound on every positive irreducible factor.
Writing the actual integer factorization with multiplicities gives
\[
m(A_{N,\varepsilon})
=\sum_j e_{j,N,\varepsilon}\,m(f_{j,N,\varepsilon}),
\]
where cyclotomic factors contribute zero.
A fixed positive lower bound on this sum does not prevent an individual positive summand from being small.
Removing all cyclotomic factors preserves the same total measure, but selecting just one remaining irreducible factor changes the object.
This note establishes no bound on the number of positive irreducible factors and does not decide whether some such factors along this family can have measures tending to zero.
A bounded-total-measure argument combined with a growing number of positive factors would require its own actual factor-supply result and applicable theorem; neither is assumed here.

Accordingly, this finding closes the specific whole-output, real-trace-preserving \(C_N\) stabilization test.
It does not impose Salem shape on the full Task, eliminate other stabilizers or varying seeds, or exclude factor extraction without additional evidence.

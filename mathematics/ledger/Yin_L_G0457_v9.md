---
author: Yin
---

# Cyclotomic factors forced by the length of a neutral prefix

<a id="forced-factors"></a>
## Divisibility and a restriction on the conductor

Use the [exceptional parent](Yin_L_G0457_v7.md#effective-cutoff)
\[
 F_s(z)=(1+z^2)^2(1-z^{2s})/(1-z^2),\qquad s\ge2 .
\]
Let \(p=2n+1>4s+3\) be odd, \(m=n-s\), and write \(E(2\cos\theta)=\sin(s\theta)/\sin\theta\) and \(B_a(2\cos\theta)=\sin((2a+1)\theta/2)/\sin(\theta/2)\).
Take \(H\in\mathbb Z[t]\) nonzero of degree \(h\le n-2\), and set \(L=n-h\), \(Q_0=t^2 E B_m,\ Q=Q_0+H,\ P(z)=z^{n+1}Q(z+z^{-1})\).
Then \(P\) agrees with \(F_s/(1-z)\) through coefficient index \(L\).
Suppose that the residues \(Q(b_j)/B_n'(b_j)\) on \(b_j=2\cos(2\pi j/p)\), \(1\le j\le n\), are strictly positive through a cut \(1\le c<n\) and strictly negative thereafter.

For fixed \(s\) there is a constant \(C_s\) such that \(L>C_s p^{1/3}\) forces every distinct cyclotomic factor of \(F_s\) to divide \(P\).
It also forces \(\gcd(s,p)=1\).
At the central factor one has the sharper implication \(\Phi_4\mid P\) once \(L>C(s^2p)^{1/5}\) for even \(s\), with an absolute constant \(C\).
For each fixed \(q\ge3,\ q\ne4\), there is a constant \(C_q\) such that all \(s\) with \(q\mid2s\) satisfy
\[
 L>C_q(s^2p)^{1/3}\quad\Longrightarrow\quad
                      \Phi_q\mid P,\qquad q\nmid p.                  \tag{1}
\]
In particular, if a fixed odd prime \(q\) divides both \(s\) and \(p\), the strict signs require \(L\le C_q(s^2p)^{1/3}\).
These implications use the residues alone.
With the additional strict endpoint \(Q(-2)/B_n(-2)<0\), every forced factor occurs exactly once by the [all-cut real-root count](../claims/Yin_C_G0881_v10.md#nonreal-pair).
For even \(s\), \(\Phi_4\) already occurs in the geometric factor \((1-z^{2s})/(1-z^2)\), so the divisibility assertion counts it only once.

The construction contributor derived these restrictions by evaluating the residue transform at all conjugates of each torsion trace, including those lying on the grid.
The [central prefix obstruction](../claims/Yin_C_G0891_v2.md#prefix-bound) uses the central value and derivative, while the argument below treats whole conjugacy classes and conductors sharing a factor with \(s\).

<a id="separation"></a>
## Separating the sign cut from a fixed set of angles

Put \(\theta_j=2\pi j/p\), and let \(\mu,\mu_0\) be the discrete measures supported at \(b_j\) with masses \(Q(b_j)/B_n'(b_j)\) and \(Q_0(b_j)/B_n'(b_j)\).
The [grid formula](Yin_L_G0457_v7.md#effective-cutoff) and \(4-b_j^2=4\sin^2\theta_j\) give
\[
 \mu_0(\{b_j\})=(4-b_j^2)b_j^2 E(b_j)^2/p
                =4b_j^2\sin^2(s\theta_j)/p.
\]
The difference \(\delta=\mu-\mu_0\) has Cauchy transform
\[
 \sum_j\frac{\delta(\{b_j\})}{t-b_j}=\frac{H(t)}{B_n(t)}=O(t^{-L})
 \quad(t\to\infty).
\]
Here the partial fractions follow from interpolation at the simple roots and \(h<n\).
Thus \(\delta\) annihilates every polynomial of degree at most \(L-2\).
Choose \(\tau\in(b_{c+1},b_c)\).
The measure \(\nu=(b-\tau)\mu\) is positive, and \(\lambda=(b-\tau)\delta\) annihilates polynomials of degree at most \(L-3\).

Fix an interior lower bound \(v>-2\).
For all sufficiently large \(L\) (depending only on \(v\)), one has \(\tau<v\), uniformly in the permitted \(s,p\).
To see this, for a positive integer \(a\) with \(2a+1\le L-2\) use positivity and matching to obtain
\[
 \tau\le \frac{\int b(2-b)^{2a}\,d\mu_0}{\int (2-b)^{2a}\,d\mu_0}.
 \tag{2}
\]
The denominator is positive since \(\mu_0\) has positive mass at the first node.
For \(p>2s+2a+3\) both sums equal their angular integrals with a common normalization.
Indeed their even trigonometric polynomials in \(\theta\) have degree less than \(p\), vanish at \(\theta=0\), and the full equally spaced grid average extracts the constant term exactly.
The zero frequency normalization cancels in (2).
For \(s>(2a+3)/2\), orthogonality also allows \(\sin^2(s\theta)\) to be replaced by \(1/2\) in both integrals.
For weight \(b^2\) on the angular variable, the weighted mean in (2) tends to \(-2\) as \(a\to\infty\).
Indeed, each left endpoint neighborhood has positive mass, and the multiplier \((2-b)^{2a}\) grows exponentially faster on a smaller such neighborhood than on the complement of the larger one.
First choose \(a_0\) giving a mean below \(v\) for this weight.
This handles \(s>(2a_0+3)/2\).
For the finitely many remaining \(s\), use the same concentration argument with weight \(b^2\sin^2(s\theta)\), which is positive on a subinterval of each endpoint neighborhood, and choose \(a_s\) separately.
The resulting finitely many quadratures and moment conditions all hold for sufficiently large \(L\) because \(p\ge2L+1\) and \(2s<p/2\).
This proves the asserted separation.

<a id="torsion-evaluation"></a>
## Values of the integral perturbation at torsion traces

Let \(\alpha=2\pi k/q\) with \(0<k<q/2,\ \gcd(k,q)=1\), and \(\beta=2\cos\alpha\).
For \(q\mid2s\), \(\sin(s\alpha)=0\).
The estimates will also cover \(\alpha=\pi/2\) for all \(s\).
For each case below the neutral weight satisfies, uniformly in \(\theta_j\),
\[
 \mu_0(\{b_j\})\le C A|\theta_j-\alpha|^{2e}/p,\qquad
 (e,A)=
 \begin{cases}
 (1,s^2),&q\mid2s,\ \alpha\ne\pi/2,\\
 (1,1),&\alpha=\pi/2,\\
 (2,s^2),&\alpha=\pi/2,\ s\text{ even}.
 \end{cases}                                                       \tag{3}
\]
These follow respectively from \(|\sin(s\theta_j)|\le s|\theta_j-\alpha|\), from \(|b_j|\le2|\theta_j-\pi/2|\), and from both inequalities together.
Apply (2) with \(v<\beta\) between \(-2\) and the smallest trace in the fixed conjugacy class.
Hence \(\beta-\tau\) is bounded below by a positive constant depending only on \(q\), once \(L\) exceeds a constant depending only on \(q\).

Write \(\ell=e+1\), \(N=\lfloor(L-3)/\ell\rfloor+1\), and
\[
 J_N(u)=\left(\frac{\sin(Nu/2)}{N\sin(u/2)}\right)^{2\ell},
 \qquad
 k(2\cos\theta)=
     \frac{J_N(\theta-\alpha)+J_N(\theta+\alpha)}{1+J_N(2\alpha)} ,
\]
using continuous values at removable singularities.
The even trigonometric polynomial \(k(2\cos\theta)\) corresponds to a polynomial in \(t=2\cos\theta\) of degree at most \(\ell(N-1)\le L-3\).
It is nonnegative and \(k(\beta)=1\).
On \(0\le\theta\le\pi\), one has \(k(2\cos\theta)\le C_q(1+N|\theta-\alpha|)^{-2\ell}\).
For the first summand use \(|\sin(Nu/2)|\le\min(1,N|\sin(u/2)|)\) and \(|\sin(u/2)|\ge |u|/\pi\) for \(|u|\le\pi\).
In the reflected summand \(\sin((\theta+\alpha)/2)\) stays bounded away from zero.
Each range \(a/N\le|\theta_j-\alpha|<(a+1)/N\) contains at most \(2+p/(\pi N)\) grid points.
Since \(N\le p\), (3) and the convergence of \(\sum_{a\ge0}(a+1)^{-2}\) now give
\[
 \int k\,d\mu_0\le C_q A L^{-(2e+1)} .
\]
Positivity of \(\nu\), nonnegativity of \(k\), and \(\int k\,d\lambda=0\) yield
\[
 \int k\,d|\lambda|
 \le \int k\,d\nu+\int k|b-\tau|\,d\mu_0
 \le 8\int k\,d\mu_0 .
 \tag{4}
\]

If \(\beta\) is off the grid then \(|\theta_j-\alpha|\ge2\pi/(pq)\).
The cosine difference formula bounds \(|b_j-\beta|\) below by \(c_q|\theta_j-\alpha|\) with \(c_q>0\), because \(\sin((\theta_j+\alpha)/2)\) is bounded below.
Since \((1-k(t))/(\beta-t)\) is a polynomial of degree at most \(L-3\), and \(\int d\delta=0\),
\[
 \frac{(\beta-\tau)H(\beta)}{B_n(\beta)}
 =\int\frac{d\lambda(b)}{\beta-b}
 =\int\frac{k(b)\,d\lambda(b)}{\beta-b}.
\]
The factor \(|B_n(\beta)|=|\sin(p\alpha/2)/\sin(\alpha/2)|\) is bounded by a constant depending only on \(q\).
From the separation and (4), it follows that
\[
                          |H(\beta)|\le C_q A p/L^{2e+1}.          \tag{5}
\]
If \(\beta=b_j\) is itself a node, then \(\lambda(\{\beta\})=(\beta-\tau)H(\beta)/B_n'(\beta)\).
Its absolute value is bounded by (4) since \(k(\beta)=1\).
The [grid derivative](Yin_L_G0457_v4.md#residue-formula) gives \(|B_n'(\beta)|=p/(4\sin\alpha\,\sin(\alpha/2))\), proving the same (5).

<a id="conjugates"></a>
## Integral norms and shared cyclotomic factors

The traces of the primitive \(q\)-th roots form the full conjugacy class of \(\beta\), by the [cyclotomic conjugacy input](../audits/literature/Bel17/Yin_U001.md#bel17-u001).
The estimate (5) holds simultaneously at each of these finitely many traces with one \(C_q\).
If \(L^{2e+1}>C_q A p\), enlarging the constant to enforce the preceding separation and size requirements, every conjugate of \(H(\beta)\) has modulus less than one.
The field norm of a nonzero algebraic integer is a nonzero integer, so \(H(\beta)=0\).
Since \(Q_0(\beta)=0\), this yields \(Q(\beta)=0\), hence \(\Phi_q\mid P\).
When \(q\mid p\) one of these traces is a grid node, where \(Q(b_j)=0\) would violate the strict cut.
This proves (1) and the separate central-factor assertion.

For fixed \(s\), the complete list of orders in \(F_s\) consists of \(q\mid2s,\ q>2\), and \(q=4\).
Applying (5) to this finite list gives the threshold \(L>C_s p^{1/3}\).
Any common prime divisor of \(p,s\) is odd and belongs to that list, giving the stated coprimality restriction.
Even when all these factors occur, the degree of their product is bounded for fixed \(s\).
The [separate resultant bound](../claims/Yin_C_G0892_v2.md#statement) also bounds \(L\) independently of the conductor for each fixed \(s\), including on coprime grids.
The [independent torsion review](../audits/reviews/Yin_R_G1107_v51.md#torsion-prefix-review) checks the conjugacy and resonant-node implications for the parameter ranges stated here.

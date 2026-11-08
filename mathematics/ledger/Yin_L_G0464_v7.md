---
author: Yin
---

# Coefficient height and prefix length in the odd-grid shrinking shell

Agent-S derived and self-checked the following obstruction for Yin's [Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract) on 2026-11-08.
The first part tests whether independent integer coefficients from a fixed alphabet can supply positive probability at every radius.
The second part gives a finite test for constructions based on the five limiting coefficient profiles.

<a id="height-escape"></a>
## Every fixed coefficient alphabet has a gap

Use the [full odd grid and strict chamber](Yin_L_G0464_v5.md#odd-grid-product) with \(p=2n+1\ge5\), \(b_j=2\cos(2\pi j/p)\), \(Q=(t-a)B+C\), \(P=z^{n+1}Q(z+z^{-1})\) and \(r_j=C(b_j)/B'(b_j)\).
Let \(k\) be the number of negative residues in increasing pole order, \(c=-2\cos(2\pi k/p)\) the angular midpoint, \(\delta=2+c\), and \(\mu_j=(b_j-c)r_j>0\).
Write \(H(S)=\max_i|[z^i]S|\) for the coefficient height.
Along every hypothetical sequence with \(1<M(P)\to1\), for every fixed nonzero \(D\in\mathbb Z[z]\) and every fixed integer \(h\ge0\),
\[
                       H(DP)\,\delta^h\longrightarrow\infty.                 \tag{1}
\]
In particular a discrete law supported on any fixed height alphabet has probability zero in a sufficiently small positive shell in this chamber, uniformly in the conductor and independently of the joint law of the coefficients.
More generally, fixing \(D,h,A\) gives a uniform gap on \(H(DP)\delta^h\le A\).
Indeed, failure would give a shrinking sequence, necessarily with unbounded degrees tending to infinity by the usual coefficient bound for monic polynomials of bounded degree and bounded measure.
The [positive atom with probability \(9^{-10}\)](../computations/programs/Yin_J_G0147/readme.md#unique-input) at \(p=19\) and radius \(6/5\) falls under the fixed-height conclusion at smaller radii.
The argument gives no numerical gap and leaves unbounded-height ensembles outside these budgets open.

<a id="cyclic-height"></a>
## The cyclic Fourier coefficients of the actual residues

For any real weights \(s_j\), define the real function \(F_s\) on \(\mathbb Z/p\mathbb Z\) by
\[
 F_s(l)=\sum_{j=1}^n s_j(\zeta^{jl}+\zeta^{-jl}),\qquad \zeta=e^{2\pi i/p}.
\]
All \(2n\) characters are distinct, so \(\|F_s\|_A=2\sum_j|s_j|\) in the [normalized Fourier convention](../audits/literature/San20/Yin_U001.md#finite-abelian-fourier-algebra-norm).
For any \(W\in\mathbb Z[t]\), \(F_{W(b)r}\) takes integer values by the [integral Laurent moments](../claims/Yin_C_G0880_v1.md#fourier).
In detail, \(WQ/B\) has integral Laurent coefficients at infinity, and \(\zeta^{jl}+\zeta^{-jl}\) is the value of an integer polynomial at \(b_j\).

With \(K=\sum_jr_j\), the [generating function](../claims/Yin_C_G0880_v1.md#sparse-completion) and \(zQ/B=(1-z)P/(1-z^p)\) give
\[
 \sum_{l\ge0}F_r(l)z^l
 =K+\frac{1-z^2}{z^2}\left(\frac{(1-z)P}{1-z^p}-(1-az+z^2)\right).
\]
For \(l\ge3\) its coefficient is \([z^{l+2}](1-z^2)(1-z)P/(1-z^p)\).
Hence on the whole cyclic group \(F_r(l)\) is the sum of the coefficients of \((1-z^2)(1-z)P\) in the residue class \(l+2\bmod p\), as seen by taking \(l\) sufficiently large in each class.
The polynomial has degree \(p+4<2p\), so \(\|F_r\|_\infty\le8H(P)\).

For fixed nonzero \(D\) define the nonzero \(W\in\mathbb Z[t]\) by \(W(z+z^{-1})=D(z)D(1/z)\), using symmetry of the integral Laurent polynomial.
Multiplication by \(W(b_j)\) on the character coefficients acts on the cyclic sequence \(F_r\) by the corresponding symmetric finite sum of shifts.
Consequently \(F_{W(b)r}(l)\) is the cyclic coefficient at \(l+2\) of \((1-z^2)(1-z)D(1/z)(DP)(z)\).
For \(p>4+2\deg D\) the width of this Laurent polynomial is at most \(p+4+2\deg D<2p\).
Each cyclic coefficient sums at most two ordinary coefficients, each bounded by \(4\|D\|_1H(DP)\), where \(\|D\|_1\) sums absolute coefficients.
In particular
\[
                         \|F_{W(b)r}\|_\infty\le8\|D\|_1H(DP).               \tag{2}
\]

<a id="rounding"></a>
## Rounding the bounded Fourier norm

For every fixed \(M\ge1\) there are \(e_M>0\) and \(B_M<\infty\) such that a real function \(f\) on a finite abelian group with \(\|f\|_A\le M\), lying within \(e_M\) in supremum norm of an integer function \(I\), satisfies \(\|I\|_A\le B_M\).
To obtain the required qualitative statement from [Sanders, Lemma 10.2](../audits/literature/San20/Yin_U001.md#near-integer-iteration), put \(N=\lceil2M\rceil+1\), \(\tau=\min(e^{-CM},1/8)\) with the lemma's constant, and \(e_M=\eta=2^{-N-3}\tau\).
At an unfinished step with nonzero nearest integer function and rounding error \(e\), the lemma supplies \(g\) within \(e+\eta\) of a coset sum \(J\) of total coefficient mass at most \(B(M,\eta)\).
The residual \(f-g\) is within \(2e+\eta\) of \(I-J\) and its Fourier norm decreases by at least \(1-e-\eta\).
Through \(N\) steps the iterated error bound is at most \(2^N(e_M+\eta)<\tau\), so nearest integers are unique, the lemma remains applicable while the rounded residual is nonzero, and the norm decreases by at least \(1/2\) each time.
Nonnegativity of the norm forces termination by step \(N\).
Thus \(I\) is a sum of at most \(N\) such coset sums, and each coset indicator has algebra norm one by character orthogonality on its subgroup.
This gives \(B_M=N B(M,\eta)\).

Now fix \(D\) with \(W\) as above and a positive integer \(s\).
For \(A(t)=W(t)(2+t)^s\), put \(I=F_{A(b)r}\) and subtract the small multiple of the unweighted power term,
\[
                            f=I-\delta^sF_{W(b)r}.
\]
The weights of \(f\) on the nodes are \(W(b_j)\mu_j[(2+b_j)^s-\delta^s]/(b_j-c)\), whose absolute values sum to at most \(\|W\|_{\infty,[-2,2]}s4^{s-1}\sum_j\mu_j\).
The [first three trace sums](Yin_L_G0464_v5.md#fixed-radius-unit-magnitudes) bound \(\sum_j\mu_j\) throughout \(M(P)\le2\), including nonunit inputs and both types of exceptional roots.
Therefore a single \(M_s\ge1\), depending on \(W,s\), bounds \(\|f\|_A\) there.
If \(8\|D\|_1H(DP)\delta^s\le e_{M_s}\), equation (2) makes \(I\) the rounded function and gives
\[
              2\sum_j |A(b_j)r_j|=\|I\|_A\le B_{M_s}.
\]
The [fixed-weight gap](../claims/Yin_C_G0880_v2.md#statement) requires this sum to diverge on a positive shrinking sequence for every fixed nonzero integral \(A\).
Consequently \(H(DP)\delta^s>e_{M_s}/(8\|D\|_1)\) eventually.
Taking \(s=h+1\) and using [\(\delta\to0\)](Yin_L_G0464_v5.md#only-left-endpoint) proves (1).

<a id="prefix-cut"></a>
## A finite bound for every surviving prefix

Let \(x\in\{-2,-1,0,1,2\}\), and suppose the actual \(P\) in this chamber agrees with the [profile \(P_{*,x}\)](Yin_L_G0464_v5.md#only-left-endpoint) through coefficient index \(5\le L<p\).
Set \(m=\lfloor(L+1)/2\rfloor\).
Then
\[
          k\le\frac{3p}{4m},\qquad
          \delta\le2-2\cos\!\left(\frac{3\pi}{2m}\right)
                 \le\frac{9\pi^2}{4m^2}.                                     \tag{3}
\]
This finite test needs no upper bound on \(M(P)\) or \(H(P)\).

Write \(d\alpha(b)=db/(\pi\sqrt{4-b^2})\) for the arcsine probability measure on \((-2,2)\).
At infinity the limiting function for \(R_p=Q/B\) has the exact representation
\[
 R_*(t)=\frac{(t-x)^2}{\sqrt{t^2-4}}
       =t-2x+\int_{-2}^2\frac{(b-x)^2}{t-b}\,d\alpha(b),
 \qquad \sqrt{t^2-4}\sim t .
\]
Indeed the arcsine Cauchy transform is \(1/\sqrt{t^2-4}\), from the circle integral of \(1/(t-2\cos\theta)\), and polynomial division gives the displayed polynomial part since \(\int b\,d\alpha=0\).
As \(L<p\), prefix agreement gives \(R_p-R_*=O(t^{-L})\), by \(zR_p=P(1-z)/(1-z^p)\), \(zR_*=P_{*,x}(1-z)\), and \(z=t^{-1}+O(t^{-3})\).
Thus the signed residue measure \(\sum_j r_j\delta_{b_j}\) and \((b-x)^2d\alpha(b)\) agree on polynomials through degree \(L-2\).

Use the \(m\) nodes \(u_i=-2\cos((2i-1)\pi/(2m))\) of equal-weight arcsine quadrature in increasing order.
Exactness through degree \(2m-1\) follows by summing the cosines of frequencies \(1,\ldots,2m-1\) at the midpoints, whose means vanish.
Choose \(g=\prod_{i=3}^m(t-u_i)\).
The polynomial \((t-c)g^2\) has degree \(2m-3\le L-2\), so the sign chamber gives
\[
 0\le\sum_j\mu_jg(b_j)^2
     =\int(t-c)g(t)^2(t-x)^2\,d\alpha(t)
     =\frac1m\sum_{i=1}^2 (u_i-c)g(u_i)^2(u_i-x)^2 .
\]
At least one of the two weights is positive since \(u_1\ne u_2\), and the integrand has degree \(2m-1\).
It follows that \(c\le u_2\), which gives (3) by \(c=-2\cos(2\pi k/p)\).

On a positive shrinking sequence take \(L\) to be the longest agreement with any of the five profiles, capped at \(n+1\).
Compactness and the [five-profile conclusion](Yin_L_G0464_v5.md#only-left-endpoint) force \(L\to\infty\).
Since [\(\log k/\log p\to1\)](Yin_L_G0464_v5.md#endpoint-index-exponent), (3) gives \(\log L/\log p\to0\).
Combining (1) and (3) also gives \(H(DP)/L^{2h}\to\infty\) for every fixed \(h\ge0\) and nonzero \(D\).
At bounded height the five profiles alone already leave only \(x=2\), since the other four have a double pole at \(z=1\) and linearly growing coefficients along a subsequence.
The remaining candidate \(P_{*,2}=(1-z)^2/(1+z)=1-3z+4z^2-4z^3+\cdots\) excludes heights at most three directly.
The rounding argument excludes every fixed height even for this last profile.

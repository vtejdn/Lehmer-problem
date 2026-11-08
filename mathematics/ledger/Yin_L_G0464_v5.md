---
author: Yin
---

# Cuts, prefixes and unit magnitudes on the odd-conductor trace grid

The [circular-unit sampling law](../computations/programs/Yin_J_G0146/readme.md#unit-law) uses the real traces of the nontrivial \(p\)-th roots of unity for a prime \(p\).
This grid has the same limiting semicircle weights as the [Chebyshev coefficient argument](../claims/Yin_C_G0881_v1.md#moments), with a different finite denominator and a different original coefficient limit.
A delegated AI agent derived and self-checked this transfer for Yin on 2026-11-08.

<a id="odd-grid-product"></a>
## The odd grid and its geometric mean

Let \(p=2n+1\ge5\) be any odd integer and take the full grid \(\theta_j=2\pi j/p,\ b_j=2\cos\theta_j,\ 1\le j\le n\), in decreasing trace order.
For composite \(p\) this uses all these nodes, including those arising from nonprimitive roots.
Write \(B_k(t)=U_k(t/2)+U_{k-1}(t/2)\) with \(U_{-1}=0\), and \(B=B_n\).
Then
\[
 B_k(2\cos\theta)=\frac{\sin((2k+1)\theta/2)}{\sin(\theta/2)},\qquad
 B^*(z)=z^nB(z+z^{-1})=\frac{1-z^p}{1-z}.
\]
The sine formula and differentiation give
\[
 B'(b_j)=\frac{(-1)^{j+1}p}{4\sin\theta_j\sin(\theta_j/2)},\qquad
 B_{n-1}(b_j)=(-1)^{j+1}2\cos(\theta_j/2),\qquad
 \nu_j=\frac{B_{n-1}(b_j)}{B'(b_j)}=\frac4p\sin^2\theta_j .
\]
In particular \(B_{n-1}/B=\sum_j\nu_j/(t-b_j)\).
These weights integrate each polynomial of degree at most \(p-3\) against \(d\nu(t)=\sqrt{4-t^2}\,dt/(2\pi)\) exactly.
For the basis polynomial \(U_h(t/2)\), the discrete sum is the full cyclic mean of \(\cos(h\theta)-\cos((h+2)\theta)\), since the term at zero vanishes and the opposite angles pair.
For \(0\le h\le p-3\) this is \(\mathbf 1_{h=0}\), the semicircle integral.

Take \(Q=(t-a)B+C\) monic integral with \(\deg C<n\) and \(P=z^{n+1}Q(z+z^{-1})\).
Write \(r_j=C(b_j)/B'(b_j)\) and assume \(r_j>0\) up to some \(1\le r<n\), \(r_j<0\) thereafter, and \(Q(-2)/B(-2)<0\).
For the angular midpoint \(\theta_c=(2r+1)\pi/p,\ c_p=2\cos\theta_c\), put \(\mu_j=(b_j-c_p)r_j>0\).
The products of \(2\sin(\theta_j/2)\) and of \(2\sin\theta_j\) over \(1\le j\le n\) both equal \(\sqrt p\).
The first follows from evaluating \((1-z^p)/(1-z)\) at one and pairing conjugates, and the second follows because multiplication by two permutes the nonzero residues modulo \(p\) up to sign.
Thus \(\prod_j|B'(b_j)|=p^{n-1}\), and \(|B(c_p)|=1/\sin(\theta_c/2)\ge1\).
With \(\Delta=|\operatorname{Res}(B,Q)|\) the exact product is
\[
                 \prod_{j=1}^n n\mu_j
                   =p(n/p)^n |B(c_p)|\,\Delta .
\]
Here \(\Delta\) is a positive integer and equals one in the prime circular-unit law.
Even at finite \(p\), \(n^{-1}\sum_j\log(n\mu_j)\ge-\log 2\), since \(p(1-1/p)^n\ge pe^{-1/2}>1\).
For \(\Delta=1\) this mean tends to \(-\log 2\) uniformly in \(r\), using \(1\le |B(c_p)|\le p\).

<a id="five-cuts-and-original-profiles"></a>
## Five limiting cuts and the original coefficient profiles

Suppose \(p\to\infty\) and \(1<M(P)\to1\) for the whole original lifts in this strict chamber.
Every accumulation point \(c_*\) of the separators is in \(\{-2,-1,0,1,2\}\).
Every coefficientwise limit of \(P\) is \((1+z)H(z+z^{-1})\), with \(H=N/D\) reduced and \(N,D\) monic integral of equal degree at most three, all their roots being torsion traces.
For an interior limit \(c_*\) the possibilities for \(H(t)\) are
\[
       \frac{t-c_*}{t-2},\qquad \frac{t-2}{t-c_*},\qquad
       \frac{(t-b)^2}{(t-2)(t-c_*)},
       \qquad b\in\{-2,-1,0,1\}\setminus\{c_*\}.
\]
These are necessary profiles and impose no condition that the two exceptional trace roots be nonreal.

To transplant the argument, first use the [grid-independent rationality and cyclotomic limit](Yin_L_G0464_v2.md#cyclotomic-prefix) for \(F_p=zQ/B=P(1-z)/(1-z^p)\), with bounded weighted mass from the [first three trace sums](Yin_L_G0462_v2.md#central-sign-test).
Take a subsequence with \(c_p\to c_*\) and \(F_p\to F\) locally uniformly, so \(F\) is a cyclotomic rational function with constant coefficient one.
Decompose \(F/z=J(t)+zg(t)\), choose the cyclotomic trace denominator \(A\) of [C881 v1](../claims/Yin_C_G0881_v1.md#moments), and put \(w=A^2,\ G=wg\in\mathbb Z[t]\).
The fixed moments of \(wr_j\) agree eventually and exactly with those of \(G(b_j)\nu_j\) by coefficient integrality and the quadrature above.
Consequently the measures \(n^{-1}\sum_j X_j\delta_{\theta_j}\), \(X_j=nw(b_j)\mu_j\), converge weakly to \(f(\theta)d\theta/\pi\) with \(f=2\sin^2\theta\,(t-c_*)G(t)\).
Here \(n\nu_j=2(1-1/p)\sin^2\theta_j\) and the unweighted angles are asymptotically uniform.
The [product equality argument](../claims/Yin_C_G0881_v1.md#saturation) has its same threshold \(-\log 2\).
Removing the bounded number of zeros of \(A\) costs at most \(O(\log p)\) in the log product because \(\sum\mu_j=O(1)\), and the remaining factors \(\prod |A(b_j)|\ge1\) form an absolute nonzero integral resultant.

Let \(D_0\) be the numerator degree of \(F\) minus its denominator degree, with reversal sign \(s\).
For \(D_0\ne2\) the logarithmic mean of \(f\) equals \(-\log 2\) by the [cyclotomic phase computation](../claims/Yin_C_G0881_v1.md#integer-recurrence).
Equality forces \(\sum_j|(b_j-c_p)e_j|\to0\), where \(e_j=w(b_j)r_j-G(b_j)\nu_j\), using \(n\nu_j=2(1-1/p)\sin^2\theta_j\).
The cosine moments of both terms are integers by expansion at infinity of the two integral rational functions \(wQ/B\) and \(GB_{n-1}/B\).
The same integer recurrence therefore forces every \(e_j=0\) eventually, contradicting the [fixed-weight gap](../claims/Yin_C_G0880_v2.md#statement) since \(\sum\nu_j=1\).
For \(D_0=2,s=1\), \(g=0\) contradicts the positive geometric mean and weak convergence.
Thus \(D_0=2,s=-1\), and \(H=F/(1-z^2)\) is invariant under \(z\mapsto z^{-1}\).
Since \(F/z=(z^{-1}-z)H(t)\), the same limiting density \(-2(t-c_*)H(t)\) relative to \(\nu\) governs the poles and signs of \(H\).
The [integrability and five-cut argument](../claims/Yin_C_G0881_v1.md#five-cuts) and the [reduced interior list](../claims/Yin_C_G0881_v2.md#interior-list) thus apply to \(H\) without changing their endpoints or sign order.
The original lift has \(P_*=F/(1-z)=(1+z)H(t)\) because \(B^*\to(1-z)^{-1}\).

<a id="only-left-endpoint"></a>
## The integral left endpoint forces \(c_p\to-2\)

On this odd grid \(B(-2)=(-1)^n\), so the strict left endpoint has the uniform margin \(R_p(-2)=-P(-1)\le-1\), where \(R_p=Q/B\).
Write \(K_p=\sum_jr_j\), and recall that the integers \(a_p=a\) and \(K_p\) are bounded by the first two trace sums in a bounded whole-measure shell.
For \(v\le-2\) the function
\[
 S_p(v)=(v-c_p)R_p(v)-(v-c_p)(v-a_p)-K_p
       =\sum_j\frac{\mu_j}{v-b_j}
\]
is decreasing, since each \(\mu_j>0\).
For each \(v<-2\), \(S_p(-2)\le S_p(v)\) gives the exact one-sided bound
\[
 2+c_p\ \le\ (2+c_p)P(-1)\ \le\
 (-2-c_p)(-2-a_p)+(v-c_p)\big[R_p(v)-(v-a_p)\big].               \tag{1}
\]
On any subsequence with a joint cut and coefficient limit, \(a_p\) is eventually constant and \(R_p(v)\to R_*(v)=(z^{-1}-z)H(v)\) with \(z\in(-1,0)\) and \(v=z+z^{-1}\).
If \(c_*>-2\), the density \(-2(t-c_*)H(t)\) makes \(H\) positive immediately to the right of \(-2\).
Integrability against \(\nu\) allows at most a simple pole at \(-2\), since that endpoint would be distinct from the cut.
If \(H\) is regular there, \(R_*(v)\to0\) as \(v\uparrow-2\).
If there is a simple pole, its residue is positive, so \(H(v)\to-\infty\) from outside and \(R_*(v)\to+\infty\), since \(z^{-1}-z=-\sqrt{v^2-4}\).
Taking \(p\to\infty\) in (1) first, and then \(v\uparrow-2\), gives a right side tending to zero in the regular case and to \(-\infty\) in the pole case.
Both contradict the positive left limit \(2+c_*\).
Every sequence in the strict positive shrinking shell therefore has \(c_p\to-2\).

At this remaining cut \(H\) is negative throughout \((-2,2)\) except at its zeros.
Its reduced denominator has the form \((t-2)^a(t+2)^b\) with \(a=0,1\) and \(b=0,1,2\), by integrability of \(-(t+2)H\) against \(\nu\).
If \(a=0\), a negative monic numerator must have an odd multiplicity at \(2\) and even multiplicities at its interior zeros.
The constant case fails the sign, and for \(b>0\) reducedness excludes \(-2\) as a zero, leaving only \(b=1\) and numerator \(t-2\).
If \(a=1\), the numerator is positive away from its zeros and coprime to \(t-2\).
For \(b=0\) its sole root must be \(-2\).
For \(b=1\) both endpoints are excluded, so its two roots are a double interior root, necessarily a rational algebraic integer.
For \(b=2\), three interior roots counted with multiplicity cannot all have even multiplicity.
Thus in a positive shrinking shell the actual possible coefficient limits reduce to the following necessary list, with the formulas understood after cancellation at \(x=\pm2\):
\[
 H_x(t)=\frac{(t-x)^2}{t^2-4},\qquad
 P_{*,x}(z)=\frac{(1+z)(1-xz+z^2)^2}{(1-z^2)^2},
 \qquad x\in\{-2,-1,0,1,2\}.
\]
Expansion at infinity of \(R_*=(z^{-1}-z)H_x\) gives \(a_p=2x\) eventually along the corresponding coefficient subsequence.
Each \(H_x\) has at most a simple pole at \(-2\), so \((v+2)R_*(v)\to0\) as \(v\uparrow-2\).
Applying (1) again gives \((2+c_p)P(-1)\to0\) in the shrinking shell.

<a id="nonreal-pair-limit"></a>
## The nonreal pair determines the surviving profile

Suppose the two exceptional trace roots form a nonreal pair \(v_p,\bar v_p\), with positive imaginary part for \(v_p\), along a subsequence with profile \(H_x\).
Since \(M(P)\to1\) and the two exterior reciprocal roots account for the whole measure, every further subsequential limit \(y\) of \(v_p\) belongs to \([-2,2]\).
The positive measures with masses \(\omega_j=\mu_j/|b_j-v_p|^2\) have total less than four by the [positive resolvent identity](Yin_L_G0464_v1.md#positive-resolvent).
Away from the endpoints, \(y\), and the finitely many clearing zeros of \(A\), the limiting measure of the \(\mu_j\)'s has density \(2(t-x)^2/(2-t)\) relative to \(\nu\).
The weak limit of any further convergent subsequence of the \(\omega_j\)'s therefore has density
\[
                     \frac{2(t-x)^2}{(2-t)(t-y)^2}\,d\nu(t)
\]
on the same open set, by uniform convergence of the multiplier on compact subsets.
If \(x\ne y\), this density is nonintegrable at \(y\), with order \(|t-y|^{-2}\) at an interior point, \((2-t)^{-5/2}\) at \(2\), and \((t+2)^{-3/2}\) at \(-2\) in the trace coordinate.
This contradicts the finite mass bound even if the candidate point was one of the finitely many exclusions.
Thus \(v_p\to x\).

The resulting interior density is \(2\,d\nu(t)/(2-t)\), whose integral against \(1/(2+t)\) equals one by the arcsine integral.
The nonnegative lower semicontinuous function \(1/(2+t)\), extended by \(+\infty\) at \(-2\), gives \(\liminf_p\sum_j\omega_j/(2+b_j)\ge1\) on every weakly convergent subsequence.
The actual endpoint in the [same resolvent identity](Yin_L_G0464_v1.md#positive-resolvent) gives
\[
          0<\sum_j\frac{\omega_j}{2+b_j}
             =1-\frac{(2+c_p)P(-1)}{|2+v_p|^2}<1 .
\]
Consequently \((2+c_p)P(-1)/|2+v_p|^2\to0\), also when the pair approaches the left endpoint itself.

<a id="odd-central-prefix"></a>
## A forbidden prefix even at fixed measure bounds

For every odd \(p\ge8193\), the strict chamber has no input agreeing through coefficient index \(2047\) with
\[
                  P_*^\circ=\frac{(1+z)(1+z^2)}{1-z}.
\]
This assertion holds without a Mahler bound.
Such agreement gives \(F_p\) the prefix of \((1+z)(1+z^2)\) to the same index.
Thus \(a=-1\), and the moments of \(r_j\) through degree \(2045\) agree with those of \(t\,d\nu\).
The [quadrature localization and positive filter](../claims/Yin_C_G0881_v2.md#finite-filter) give \(|c_p|<0.007\) and, with \(m=512,\ f=1-\cos(4\theta),\ X_j=n\mu_j,\ Y_j=h_m(\theta_j)X_j\), the exact mean \(\mathbb E Y=1+1/m\).
Here \(\mathbb E\) denotes the mean over the \(n\) nodes.

For the [finite product estimate](../claims/Yin_C_G0881_v2.md#finite-product), \(e^{4i\theta_j}\) now traverses all \(p\)-th roots on the full \(p\)-point grid since \(\gcd(4,p)=1\).
The half-grid mean of an even function is its full-grid sum minus the value at zero, divided by \(p-1\).
With the same \(S,K,h_m\) as in that estimate, the zero bound on \(S\) therefore gives
\[
       \mathbb E\log h_m\ \ge\ \log2-
       \frac{2(m-1)/2000+2\log((m+1)/2)}{p-1}
       >\log2-\frac1{600}.
\]
The full-grid mean of \(|K|^2\) is \(1/m\) by orthogonality, and removing \(K(1)=1\) only lowers that mean.
Together with the finite geometric-mean bound for \(X_j\) above, these are precisely the hypotheses for \(\mathbb E|X-f|<0.436\) in the [finite filter proof](../claims/Yin_C_G0881_v2.md#finite-product).
The replacement of \(f\) by \(n(b_j-c_p)b_j\nu_j\) costs at most \(2/p+|c_p|\) in mean absolute value, since \(0\le f\le2\), \(n\nu_j=2(1-1/p)\sin^2\theta_j\), and \(\sum_j |b_j|\nu_j\le1\).
Hence \(\sum_j|(b_j-c_p)(r_j-b_j\nu_j)|<1/2\).
The two initial moments vanish by prefix agreement and odd-grid quadrature, so the [integer recurrence](../claims/Yin_C_G0881_v1.md#integer-recurrence) gives \(r_j=b_j\nu_j\) exactly.
These residues and \(a=-1\) determine \(Q^\circ=t(B_n+B_{n-1})\), whose lift is \((1+z)(1+z^2)(1-z^{p-1})/(1-z)\).
Since \(B_k(-2)=(-1)^k\), \(Q^\circ(-2)=0\), contradicting the strict left endpoint condition.

<a id="unit-signatures-and-bounded-offsets"></a>
## The three admissible gaps at conductor \(29\)

At \(p=29\) the [calculated signature image](../computations/programs/Yin_J_G0146/readme.md#replay) has precisely \(r=4,7,9\).
Their open gaps actually contain \(+1,0,-1\), respectively, since \(29/6,\ 29/4,\ 29/3\) lie strictly in \((4,5),\ (7,8),\ (9,10)\).
Whenever the open gap at any conductor contains one of these three fixed values, choose that value as separator and apply the fixed-weight gap with the corresponding linear weight.
The union of those three classes has a uniform gap above measure one for positive whole measures.
The signature calculation at \(29\) supplies no endpoint, magnitude or shell count, and no assertion about the signature image of a different prime.

<a id="endpoint-index-exponent"></a>
## The number of negative poles has logarithmic exponent one

In a strict positive shrinking shell put \(k=n-r\), the number of negative residues.
The endpoint localization gives \(k/p\to0\).
Nevertheless
\[
       \frac{k^{\,2h+1}}{p^{\,2h}}\longrightarrow\infty
       \quad\text{for every fixed integer }h\ge1,
       \qquad \frac{\log k}{\log p}\longrightarrow1 .
\]
These restrictions apply to the full odd grid and in particular to candidate prime-conductor signatures, with real or nonreal exceptional trace roots.

Write \(\delta=2+c_p=2-2\cos(2\pi k/p)\asymp(k/p)^2\) and \(\Delta=\min_j|b_j-c_p|\asymp k/p^2\).
For the minimum, the two neighboring angles differ from \(\theta_c=\pi-2\pi k/p\) by \(\pi/p\).
The cosine difference formula gives both trace distances of order \(k/p^2\) for \(1\le k=o(p)\).
At any fixed upper bound \(M(P)\le R\) the signed sum \(K_p\) and \(a_p\) are bounded in terms of \(R\).
The endpoint identity gives
\[
 0<\sum_j\frac{\mu_j}{2+b_j}
   =K_p+\delta\big(2+a_p-P(-1)\big)\ll_R1 .
\]
On \(2+b_j\le2\delta\), summing \(|r_j|=\mu_j/|b_j-c_p|\) costs at most \(2\delta/\Delta\) times this last sum, hence \(O_R(k)\).
On \(2+b_j>2\delta\), one has \(b_j-c_p\ge (2+b_j)/2\), so the variation on that complement is \(O_R(1)\).
Therefore
\[
              \sum_j |(2+b_j)^h r_j|\ll_{R,h}1+\delta^h k .
\]
The [fixed polynomial weight gap](../claims/Yin_C_G0880_v2.md#statement) with \(A(t)=(t+2)^h\) requires this variation to tend to infinity for each fixed \(h\).
It follows that \(\delta^h k\to\infty\), which proves the first assertion.
This gives \(\liminf\log k/\log p\ge 2h/(2h+1)\) for every \(h\), and \(k<p\) gives the upper bound one.
In particular a fixed \(\varepsilon>0\) and \(k\le p^{1-\varepsilon}\) exclude arbitrarily small positive whole measures throughout that class.

<a id="fixed-radius-unit-magnitudes"></a>
## A conductor-uniform height test for sampling at a fixed radius

At prime \(p\), write \(u=C(b_1)\) for the actual sampled unit and \(C_j=C(b_j)\) for its real conjugates.
For a fixed whole bound \(M(P)\le R\), \(R\ge1\), define \(L=R+R^{-1}\), \(D_h=3\cdot2^h+2L^h\) for \(h=1,2,3\), and
\[
 A_R=D_1,\qquad K_R=(A_R^2+D_2)/2,\qquad
 T_R=(A_R^3+3A_R K_R+D_3)/3+2K_R .
\]
The same disjoint root matching bounds \(|\Delta_h|\le D_h\), since the variation of \(t^h\) is \(2^{h+1}\), one unmatched pole contributes at most \(2^h\), and the two remaining trace roots have modulus at most \(L\).
The three Newton identities give \(|a|\le A_R,\ |\sum r_j|\le K_R,\ T=\sum\mu_j\le T_R\).
In the case of a nonreal exceptional pair \(v,\bar v\), the [positive resolvent](Yin_L_G0464_v1.md#positive-resolvent) sharpens the last bound to \(T<4(2+\sqrt R+1/\sqrt R)^2\), since \(\sum_j\mu_j/|b_j-v|^2<4\) and \(M(P)\) is the square of the exterior radius.

Put \(d_j=n|b_j-c_p|/|B'(b_j)|\).
Their product is \(p(n/p)^n|B(c_p)|\) and \(d_j\le8\) by the derivative formula.
Consequently their mean \(\log d_j\) is at least \(-\log2\) and their mean \(\log^+(1/d_j)\) is at most \(\log16\).
The exact signed chamber gives \(\mathbb E(d_j|C_j|)=T\).
Since the unit has no finite-place height contribution, Jensen's inequality gives
\[
 h(u)=\mathbb E\log^+|C_j|
     \le \mathbb E\log(1+d_j|C_j|)+\mathbb E\log^+(1/d_j)
     \le \log\big(16(1+T_R)\big).
\]
The norm has absolute value one, so \(\mathbb E|\log|C_j||=2h(u)\).
Thus a proposed signed exponent vector \((e_a)\) in the prime circular-unit generators can be rejected at fixed \(R\) if
\[
 \frac1n\sum_{j=1}^n\left|\sum_{a=2}^n e_a
           \log\left|\frac{\sin(2\pi a j/p)}{\sin(2\pi j/p)}\right|\right|
           >2\log\big(16(1+T_R)\big).
\]
The sharper bound on \(T\) can be used when testing the single-nonreal-pair target.
For an actual cut \(r\) the sharper individual test is the necessary inequality \(\mathbb E(d_j|C_j|)\le T_R\) itself, which is independent of \(a\) in \(Q=(t-a)B+C\).
Neither test requires restricting the exponents to \(\{-1,0,1\}\), and passing them leaves the true whole-root cost to be checked.

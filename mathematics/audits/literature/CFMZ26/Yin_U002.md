---
author: Yin
---

# CFMZ26-U002: independent analytic inspection of strict quartic Salem collision-pressure improvement

<a id="cfmz26-u002"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Guozheng Cheng, Xiang Fang, Xueqing Ma and Hongli Zhang, *Strict correlation-dimension drop for quartic Salem Bernoulli convolutions*, arXiv:2610.09902v1; [retained original HTML](../../../literature/pdf/CFMZ26/arxiv-v1.html), with acquisition facts at the artifact.

Passages: Introduction Theorem 1.1 and equations (1.1)--(1.3); complete Sections 2--5, especially Proposition 2.1, Lemmas 2.2--2.3, Theorem 2.4, Corollary 2.5, Lemma 3.1, Definition 3.2, Lemma 3.3, Proposition 3.4, Corollary 3.5, Lemma 4.1, Definition 4.2, Lemmas 4.3--4.4, Lemma 5.1, Theorem 5.2 and the subsequent proof of Theorem 1.1.

Inspection: On 2026-10-26, quartic_source_check independently inspected the original fixed paper's complete analytic proof chain in Sections 2--5, checked its exact hypotheses and original digit-law applicability, and found no mathematical gap within this scope. Quantitative appendix proofs, source programs, native verification release, formal code and the companion manuscript were excluded.


The review relationship is **independently reviewed** at this source-inspection scope.
The reviewer received an isolated assignment with the original source and intended probability specialization, without proof-development discussion or another source verdict before completing the inspection.
The reviewer had not contributed to the source proof or its project adaptation.
The completed finding was communicated before reading the neighboring source unit for retention and scope coordination.
This file retains that reviewer's own finding; it is not a coordinating agent's rewrite of the independent assessment.

The coverage state for the specified qualitative analytic chain is **Audited within scope**.
The decision is to accept Theorem 1.1's qualitative result, and its exact collision-pressure consequence below, as a source input within the checked hypotheses.
This is neither a project Claim acceptance nor a project R review, and it does not complete [G0001](../../../tasks/Yin_T_G0001_v1.md).
The neighboring [CFMZ26-U001](Yin_U001.md#cfmz26-u001) supplies the separately retained original-law and complete-return interfaces; the present unit retains the independent inspection of the critical strict-drop construction.

## Exact statement, conventions and specialization

Fix
\[
 P(X)=X^4-X^3-X^2-X+1,
\]
and let \(\beta>1\) be its exterior root, \(r=\beta^{-1}\), and \(\zeta=e^{i\varphi}\) its unit-circle root with positive imaginary part.
The source also proves the result for \(X^4-2X^3+X^2-2X+1\); its common two-parameter argument was inspected, but the intended application here is the first polynomial.
All logarithms are natural.
For independent fair signs \(\varepsilon_j\in\{-1,1\}\), let
\[
 X_n=\sum_{j=0}^{n-1}\varepsilon_jr^j,
 \qquad \nu_r=\operatorname{Law}\left(\sum_{j=0}^{\infty}\varepsilon_jr^j\right),
 \qquad Q_n=\Pr(X_n=X_n'),
\]
where the prime denotes an independent copy and \(Q_0=1\).
Equal finite atoms are merged before computing \(Q_n=\sum_x\Pr(X_n=x)^2\).
The source's correlation dimension is the energy threshold
\[
 D_2(\nu)=\sup\bigl(\{0\}\cup\{s\in(0,1): I_s(\nu)<\infty\}\bigr),
 \qquad I_s(\nu)=\iint|x-y|^{-s}\,d\nu(x)\,d\nu(y).
\]
Theorem 1.1 asserts \(D_2(\nu_r)<1\) for every quartic Salem parameter \(\beta\in(1,2)\).

For the intended original process, define independent digits by
\[
 \Pr(U_j=-1)=\Pr(U_j=1)=\tfrac14,
 \qquad \Pr(U_j=0)=\tfrac12,
 \qquad p_n=\Pr\left(\sum_{j=0}^{n-1}U_j\beta^j=0\right).
\]
The half-differences \((\varepsilon_j-\varepsilon_j')/2\) have precisely this law.
Multiplying the half-difference sum at \(r\) by \(r^{-(n-1)}\) and reversing the iid digit vector gives \(p_n=Q_n\) exactly.
This preserves every word's probability and multiplicity and imposes no intermediate-return restriction.
The source's notation \(p_n(x)\) for an atom mass is different from the project's scalar \(p_n\).

Independent zero events on consecutive blocks imply \(p_{n+m}\ge p_np_m\).
Consequently Fekete's lemma gives
\[
 \varrho=\lim_{n\to\infty}p_n^{1/n}=\sup_{n\ge1}p_n^{1/n},
 \qquad
 R=\exp\left(\lim_{n\to\infty}\frac{-\log p_n}{n}\right)=\varrho^{-1}.
\]
The inspected construction proves \(\beta^np_n>1\) for some finite \(n\), hence directly \(R<\beta\).
Section 2 also proves \(\varrho<1\), so the full conclusion is
\[
 1<R<\beta,
 \qquad R=\beta^{D_2(\nu_r)}.
\]
The strict collision-pressure conclusion does not require first inferring it from the dimension statement: the proof itself constructs the finite collision inequality.

## Complete packet definitions used in the review

<a id="positive-torus-and-localized-packet"></a>
Write \((\mathcal Sy)_j=y_{j+1}\).
For either source polynomial \(P(X)=X^4-AX^3+BX^2-AX+1\),
\[
 (P(\mathcal S)y)_j=y_j-Ay_{j+1}+By_{j+2}-Ay_{j+3}+y_{j+4}.
\]
Set
\[
 \operatorname{can}(t)=t-\lfloor t+1/2\rfloor\in[-1/2,1/2),
 \qquad V(t)=-\log\cos^2(\pi t)\quad(|t|<1/2).
\]
The centering boundary is \(\mathbb Z+1/2\).
The companion torus automorphism is
\[
 T_P(x_0,x_1,x_2,x_3)
 =(x_1,x_2,x_3,-x_0+Ax_1-Bx_2+Ax_3)\pmod{\mathbb Z^4}.
\]
Its canonical first-coordinate observation at time \(j\in\mathbb Z\) is denoted by \(y_j(x)\).

In [Definition 3.2](https://arxiv.org/html/2610.09902v1#S3.Thmtheorem2), a packet with fixed constants \(0<\eta<1/4\), \(h>0\) consists of real bilateral sequences \(Y,H\), an integer \(\ell\ge1\), and \(\gamma\in\mathbb C\setminus\{0\}\), such that
\[
 \kappa=P(\mathcal S)Y\in\mathbb Z^{\mathbb Z}\setminus\{0\},
 \qquad \operatorname{supp}\kappa\subset[0,\ell-1],
\]
\[
 Y_j=H_j+\mathbf1_{\{j\ge\ell\}}2\Re(\gamma\zeta^{j-\ell}),
 \qquad |H_j|\le\tfrac12-2\eta,
\]
and, outside the core \([0,\ell-1]\cap\mathbb Z\),
\[
 |H_j|\le h r^{\operatorname{dist}(j,[0,\ell-1])}.
\]
Its neutral amplitude, localized action and derivative sum are
\[
 \Delta=2|\gamma|,
 \qquad E=\sum_{j\in\mathbb Z}V(H_j),
 \qquad\mathcal V=\sum_{j\in\mathbb Z}|V'(H_j)|.
\]
The action and derivative sums converge because the tails are geometric and \(V(t)=O(t^2)\), \(V'(t)=O(|t|)\) near zero.
The localization removes only the outgoing neutral oscillation, not the stable real tail.

<a id="centered-reciprocal-packet"></a>
For [Definition 4.2](https://arxiv.org/html/2610.09902v1#S4.Thmtheorem2), take a nonzero integral Laurent polynomial \(K\) satisfying
\[
 K(X^{-1})=\sigma X^{-2c_K}K(X),
 \qquad \sigma\in\{-1,1\},\quad c_K\in\mathbb Z,\quad K(\zeta)\ne0.
\]
For every root \(\lambda\) of \(P\), set \(C_\lambda=1/P'(\lambda)\), and define
\[
 j_*=4-2c_K,
 \quad \xi_i=-C_\beta\beta^{i-1}K(\beta),
 \quad \chi_i=2\Re(C_\zeta\zeta^{i-1}K(\zeta)),
 \quad \Delta=2|C_\zeta K(\zeta)|.
\]
Irreducibility and \(K(\zeta)\ne0\) imply \(K(\beta)\ne0\).
A centered reciprocal packet is \(Y_i=\operatorname{can}(\xi_i)\), with \(\xi_i\notin\mathbb Z+1/2\) for every \(i\), nonzero integral forcing supported in an integer core \([a,b]\), \(a+b=j_*\), \(\ell=b-a+1\ge4\), and tail identities
\[
 Y_i=\xi_i\quad(i<a),
 \qquad Y_i=\sigma\xi_{j_*-i}+\chi_i\quad(i>b).
\]
Its localization is \(H_i=Y_i\) for \(i\le b\) and \(H_i=\sigma\xi_{j_*-i}\) for \(i>b\).
Writing \(h_0=|\xi_a|\), the two localized real tails have absolute values \(h_0r^j\), \(j\ge1\).
The core derivative sum is \(\mathcal V_{\rm core}=\sum_{i=a}^b|V'(Y_i)|\), and the full action is \(E=\sum_iV(H_i)\).
A global localized boundary distance means a uniform positive lower bound for \(1/2-|H_i|\).
Translating the core to \([0,\ell-1]\) produces Definition 3.2 when that bound is at least \(2\eta\); translation changes the neutral phase but not its amplitude.

## Independent proof inspection

### Algebraic preliminaries and the collision interface

[Section 2](https://arxiv.org/html/2610.09902v1#S2) was inspected in full.
The trace factorization is \(P_i(X)=X^2F_i(X+X^{-1})\), with \(F_1(T)=T^2-T-3\), \(F_2(T)=T^2-2T-1\).
For \(P_1\), the trace roots are \((1\pm\sqrt{13})/2\); for \(P_2\), they are \(1\pm\sqrt2\).
They give one real reciprocal pair and one nonreal unit-circle pair.
The other real embedding of the quadratic trace field sends the positive discriminant \(u_i^2-4\) to \(v_i^2-4<0\), excluding its being a square and proving quartic irreducibility.
The classification in Proposition 2.1 follows by checking the possible integer coefficients \(A\in\{1,2,3,4\}\) and the displayed open ranges for \(B=Au-u^2+2\).
The trace values establish \(5/3<\beta<2\), \(1/2<r<3/5\), \(|1-\zeta|>3/2\), \(|1-\zeta^2|>3/2\), and \(|P'(\zeta)|>1\).
Irreducibility excludes \(\zeta\) and \(\zeta^2\) being roots of unity.

Lemma 2.2's four homogeneous modes are independent by the Vandermonde determinant.
Decay at negative infinity removes the stable real mode and both neutral modes, and boundedness at positive infinity then removes the expanding real mode.
Thus a homogeneous bilateral solution with those two end conditions is zero.

For distinct atoms \(x,y\), write \(x-y=2r^{n-1}F(\beta)\) with coefficients of \(F\) in \(\{-1,0,1\}\).
The nonzero integer norm and bounds \(|F(r)|\le(1-r)^{-1}\), \(|F(\zeta)|,|F(\bar\zeta)|\le n\) give
\[
 |x-y|\ge2(\beta-1)r^n n^{-2}.
\]
This concerns distinct atoms after identifying exact overlaps; it does not assert separation of all symbolic words.
Packing the atoms and applying Cauchy--Schwarz give \(\varrho\ge r\).
Conditioning on every sign except those at positions \(0,k,2k,\ldots\), where \(r^k<1/2\), makes the remaining sparse sum injective, so every atom has mass at most \(2^{-\lceil n/k\rceil}\) and \(\varrho<1\).
The separation estimate bounds each atom's neighbors at distance \(O(r^n)\) by \(O(1+n^2)\).
Using \(ab\le(a^2+b^2)/2\) therefore yields the approximate-collision bound \(\Pr(|X-X'|\le r^n)\le C(1+n^2)Q_n\).
The geometric-shell estimate proves finite \(s\)-energy below \(-\log\varrho/\log\beta\), and repeated independent exact-collision blocks prove infinite \(s\)-energy above it.
Theorem 2.4 and Corollary 2.5 follow with the stated strict finite-block implications.

### Positive torus formula and amplification

In [Lemma 3.1](https://arxiv.org/html/2610.09902v1#S3.Thmtheorem1), the vectors \(v_j=(\mathsf T^j)^{\mathsf T}e_0\) satisfy the polynomial recurrence, and \(v_0,v_1,v_2,v_3\) are the standard basis.
Division by the monic \(P\) gives
\[
 \sum_jc_jv_j=0\quad\Longleftrightarrow\quad P\mid\sum_jc_jX^j
 \quad\Longleftrightarrow\quad\sum_jc_j\beta^j=0.
\]
Expanding \(\cos^2(\pi t)=(e^{2\pi it}+2+e^{-2\pi it})/4\) and integrating over Haar probability therefore gives exactly
\[
 Q_n=\int_{\mathbb T^4}\prod_{j=0}^{n-1}\cos^2(\pi y_j(x))\,dx.
\]
The coefficients are precisely the required digit probabilities.
Integral forcing makes the recurrence homogeneous modulo integers, and invertibility of the integer companion matrix gives the unique canonical torus orbit in both time directions.

Lemma 3.3's steering estimate is valid uniformly for \(|z|\le8\).
Geometric sums using \(|1-\zeta|,|1-\zeta^2|>3/2\) give a small first moment and a second moment greater than \(3/8\) on every eleven consecutive powers.
If all normalized real parts were at least \(-1/8\), the quadratic inequality in the paper would instead bound that second moment by \(15/64\).
Thus some power gives \(|\zeta^mz+1|\le8\).

For a packet and integer \(N>2\ell+4\), define
\[
 b_N=\lfloor N/11\rfloor,\quad d_N=\lfloor(N-\ell)/2\rfloor,
 \quad e_N=\frac{2hr^{d_N}}{1-r^N},\quad u_N=8\Delta+e_N,
\]
\[
 C_\eta=2\pi^2\csc^2(\pi\eta),\quad
 C_N=E+u_N\mathcal V+C_\eta Nu_N^2,
 \qquad\Theta_N=\log b_N-C_N.
\]
In [Proposition 3.4](https://arxiv.org/html/2610.09902v1#S3.Thmtheorem4), each successive spacing lies in \([N,2N-1]\), and the eleven-step lemma supplies at least \(b_N\) admissible choices preserving the neutral-state bound.
The recurrence \(\psi_j=\zeta^{\tau_j-\tau_{j-1}}\psi_{j-1}+1\) has the correct phase for the sum of all waves emitted by the preceding packet copies.
Every emitted prefix has modulus at most eight, so the total neutral perturbation is bounded by \(8\Delta\).
Assigning a site to a nearest core bounds all other localized tails by \(e_N\), with further cores separated by at least \(N\).
When \(u_N<\eta\), all observations stay canonical and Taylor's theorem bounds the action through \(n=\tau_{M-1}+\ell+4\) by \(MC_N\).

The distinctness argument does not count coincident placements multiple times.
For the nonempty set \(F=\operatorname{supp}\kappa\subset[0,\ell-1]\), internal gaps in a copy of \(F\) are at most \(\ell-1\), whereas gaps between copies exceed \(\ell\).
The supports are disjoint, so there is no cancellation, and splitting the total support at gaps greater than \(\ell\) recovers every start by subtracting \(\min F\).
The observed forcing indices \(0,\ldots,n-5\) include the final support coordinate \(\tau_{M-1}+\ell-1\).
After selecting a common length, at least \(b_N^{M-1}/(MN)\) distinct observed forcing words remain.

Four-mode homogeneous perturbations have expanding coefficient bounded by \(\rho_{\rm box}\beta^{-(n-1)}/n\) and the other three coefficients bounded by \(\rho_{\rm box}/n\), with \(0<\rho_{\rm box}\le\eta/64\).
Their coordinate size is at most \(4\rho_{\rm box}/n\), their action increment is less than one, and their volume is \(|\det R_P|(2\rho_{\rm box})^4\beta^{-(n-1)}n^{-4}\), where \(R_P\) is the four-mode matrix in (3.13).
Its invertibility follows from Lemma 2.2.
Each box projects injectively to the torus, and two boxes with distinct observed forcing words cannot overlap because canonical observations and homogeneous perturbation preserve that word.
Thus integrating over the boxes is legitimate even across fundamental-cube boundaries.
The polynomial losses give exactly
\[
 \log(\beta^nQ_n)>
 M\Theta_N-\log b_N-5\log M-5\log N-4\log2+\log c(P,\eta),
 \qquad 5\le n<2NM.
\]
In particular, \(\Theta_N>0\) gives a finite \(n\) with \(\beta^nQ_n>1\), and \(\Theta_N>1\) gives the stated \(1-1/(8N)\) energy bound.
Corollary 3.5 correctly reduces this to packets with common margin and tail bound, \(\Delta_k\to0\), \(\Delta_k\ell_k\to0\), and \(E_k=o(\log(1/\Delta_k))\).

### Reciprocal mirror and algebraic seed

[Section 4](https://arxiv.org/html/2610.09902v1#S4) was checked algebraically, including the signs, reflection shift and regional action accounting.
Reciprocity gives \(P'(\lambda^{-1})=-\lambda^{-2}P'(\lambda)\).
The trace sums \(\sum_{P(\lambda)=0}\lambda^m/P'(\lambda)\) equal \(0,0,0,1\) for \(m=0,1,2,3\), and the monic recurrence with constant coefficient one propagates integrality in both directions.
It follows that
\[
 \xi_i\equiv\sigma\xi_{j_*-i}+\chi_i\pmod{\mathbb Z},
 \qquad\chi_{j_*-i}=-\sigma\chi_i.
\]

For an even delay \(L>\ell\), replace \(K\) by \(K^+=(1-X^{-L})K\).
The new sign is \(-\sigma\), its reflection index is \(j_*+L\), and
\[
 \Delta^+=\Delta|1-\zeta^L|,
 \qquad h_0^+=(1-r^L)h_0\le h_0.
\]
The new amplitude is nonzero because \(\zeta\) is not a root of unity.
Put \(g=L-\ell\), \(\rho_L=h_0r^{g+1}\), and \(U=\Delta+2h_0r\).
If the old core has boundary distance at least \(\vartheta\), the source assumes \(\Delta^++\rho_L\le\vartheta/2\), \(U<1/2\), and \(\Delta^++h_0r<1/2\).
On the first core \(Y_i^+=Y_i-\xi_{i-L}\), while for \(i=L+j_*-k\) on the second core,
\[
 Y_i^+=\sigma\bigl(-Y_k+\xi_{k-L}+\chi_k^+\bigr).
\]
The second identity follows by applying the old trace congruence to \(\xi_i\) and \(\xi_{i-L}\) and using \(\chi_{j_*-k}=-\sigma\chi_k\).
Its error uses the new small amplitude \(\Delta^+\), which is essential.
The regional estimates ensure these expressions are canonical and give the global localized boundary distance in (4.4).

On the gap the canonical sequence is \(x_j+z_j+\chi_{b+j}\), where \(|x_j|=h_0r^j\) and \(|z_j|=h_0r^{g+1-j}\).
Integrating the mixed derivative of \(V\), then Taylor-expanding the oscillatory term, gives (4.7).
Summing the neutral square by a geometric series at \(\zeta^2\) gives the term \(\Delta^2(g/4+1/(2|1-\zeta^2|))\).
With \(C_{\rm core}=2\pi^2\csc^2(\pi\vartheta/2)\) and \(C_U=2\pi^2\sec^2(\pi U)\), the resulting full estimate is
\[
\begin{aligned}
 E^+\le{}&2E+\mathcal V_{\rm core}(\Delta^++2\rho_L)
 +C_{\rm core}\ell(\Delta^++\rho_L)^2\\
 &+C_U\left\{h_0^2gr^{g+1}+\frac{2\Delta h_0r}{1-r}
 +\Delta^2\left(\frac g4+\frac1{2|1-\zeta^2|}\right)\right\}.
\end{aligned}
\]
There is no missing tail cost: the two gap base-tail sums plus the two new exterior tails fit within the four old tail sums already included in \(2E\).
The first four old-core coordinates suffice to verify that the five-term forcing vanishes before the new core, and the stable--neutral tail verifies vanishing after it.
Centering gives integral forcing.
If it vanished identically, Lemma 2.2 would force the new sequence to be zero, contradicting its nonzero expanding tail.
Thus the required support and nonvanishing survive each mirror.

Lemma 4.4 uses \(K_i=U_i^{10}\), where \(U_1=1+X+X^{-1}\), \(U_2=X+X^{-1}\), with \(0<|U_i(\zeta_i)|<1/2\).
Hence \(0<\Delta_{\rm seed}<1/100\).
The embedding \(\beta\mapsto\zeta\) sends every \(\xi_j\) to a number of modulus \(\Delta_{\rm seed}/2<1/200\).
If \(\xi_j\) were a half-integer, it would be rational and fixed by that embedding, with modulus at least \(1/2\), a contradiction.
Choosing a sufficiently negative \(a\) makes \(h=|\xi_a|<1/100\), and \(b=4-a\) gives the required symmetric finite core and homogeneous tails.
The core contains finitely many values avoiding the boundary, so its minimum boundary distance is strictly positive without requiring numerical evaluation.
The localized action is finite and the forcing is nonzero by the same homogeneous-solution argument.

### Controlled returns and final amplification

[Section 5](https://arxiv.org/html/2610.09902v1#S5) requires no bounded-type hypothesis or quantitative irrationality exponent.
Put \(\omega=\zeta^2\), \(\operatorname{err}(q)=|1-\omega^q|\), and let \(q(R)\) be the least positive minimizer of this error over \(1\le q\le R\).
The finite pigeonhole argument gives \(0<\operatorname{err}(q(R))\le2\pi/R\), and \(q(R)\to\infty\).
A strict improvement over the minimum for \(R_*\) must use a denominator greater than \(R_*\), a fact stronger than merely exceeding its previous minimizing denominator.

The preparatory mirror yields \(\ell_0<3q_0\), \(0<\Delta_0<\min\{e^{-16},\eta/4\}\), \(hr^{\ell_0}/(1-r^{\ell_0})<\eta/4\), and localized boundary distance at least \(4\eta\), with \(\eta=\min\{\vartheta_{\rm seed}/8,1/100\}>0\).
The parameters can be chosen simultaneously because the minimizing denominator tends to infinity while its error tends to zero.
The potentially very large initial action remains a finite constant.

For \(k\ge1\), Theorem 5.2 sets
\[
 m_k=3^k,\quad
 R_k=\left\lfloor\frac{\Delta_{k-1}^{-3/2}}{2m_k}\right\rfloor,
 \quad q_k=q(R_k),\quad L_k=2m_kq_k.
\]
The inductive amplitude bound implies \(28\cdot9^k\sqrt{\Delta_{k-1}}<1\), so the floor is harmless and
\[
 \operatorname{err}(q_k)<28m_k\Delta_{k-1}^{3/2}
 <\frac{\Delta_{k-1}}{m_{k-1}}
 <\operatorname{err}(q_{k-1}).
\]
The final inequality follows from the preceding amplitude identity and \(\Delta_{k-2}<1\), with the preparatory step interpreted as in the paper.
Strict improvement forces \(q_k>q_{k-1}\), and the invariant \(\ell_{k-1}<3^kq_{k-1}\) gives
\[
 L_k>2\ell_{k-1},\qquad L_k\le\Delta_{k-1}^{-3/2},
 \qquad \ell_k<3^{k+1}q_k.
\]
Thus core separation is proved rather than assumed from an unstated bound on consecutive return denominators.
The amplitude estimate is
\[
 0<\Delta_k
 =\Delta_{k-1}|1-\omega^{m_kq_k}|
 <28\cdot9^k\Delta_{k-1}^{5/2}
 \le\Delta_{k-1}^2.
\]
It yields \(\Delta_k\le e^{-16\cdot2^k}\).
Writing \(x_k=\log(1/\Delta_k)\), summing \(x_k\ge(5/2)x_{k-1}-\log28-2k\log3\) gives \(x_k\ge10(5/2)^k\); the displayed geometric sums bound the total normalized loss by less than six.

The lengths grow by a factor greater than three, so the real-tail interaction errors have total less than \(\eta/4\).
The sum of the new amplitudes is also less than \(\eta/4\).
Consequently all old cores retain boundary distance greater than \(3\eta\), while gap and exterior-tail bounds stay much farther from the boundary.
Every mirror's hypotheses remain valid, with a common upper bound \(h\) for its tail coefficient.
For the action estimate, \(\ell_{k-1}\Delta_k<1\), \(\Delta_{k-1}^2(L_k-\ell_{k-1})\le\sqrt{\Delta_{k-1}}<1\), and geometric-series bounds control the real-tail cross terms.
Each error term in (4.5) is therefore uniformly bounded, giving
\[
 E_k\le2E_{k-1}+C_*,\qquad E_k\le C_E2^k,
 \qquad\mathcal V_k\le C_{\mathcal V}(\ell_k+1).
\]
The constants can depend on the fixed initial packet and boundary margin but not on \(k\).
Finally,
\[
 \ell_k\le\tfrac32\Delta_{k-1}^{-3/2},
 \qquad\Delta_k\ell_k\le42\cdot9^k\Delta_{k-1}\longrightarrow0.
\]

Take \(N_k=\lceil\Delta_k^{-1}\rceil\).
Then \(\ell_k/N_k\to0\), \(e_{N_k}/\Delta_k\to0\), \(u_{N_k}\mathcal V_k\to0\), and \(N_ku_{N_k}^2\to0\).
The geometric tail estimate uses \(d_{N_k}\ge N_k/4-1\) eventually, so it beats the factor \(1/\Delta_k\).
As \(b_{N_k}\ge N_k/22\) eventually,
\[
 \Theta_{N_k}\ge10(5/2)^k-C_E2^k-\log22-o(1)\longrightarrow+\infty.
\]
Some finite packet therefore satisfies Proposition 3.4 with \(\Theta_{N_k}>1\).
This proves Theorem 1.1 and the finite strict collision inequality, and hence the claimed \(1<R<\beta\) for the original iid law.
The post-theorem no-\(L^2\)-density consequence follows from the standard convolution Cauchy--Schwarz bound on close pairs and a shell decomposition.

## Retained inputs, evidence and limits

The proof inspection retains elementary polynomial division, algebraic embeddings and integer norms, Lagrange interpolation, the Vandermonde determinant, Fekete's lemma, finite pigeonhole approximation, geometric sums, Taylor's theorem, Cauchy--Schwarz and Haar character orthogonality as standard inputs.
Their needed interfaces and applicability were checked in the source argument; this unit does not re-prove their general textbook forms.
No unresolved nonstandard external theorem is needed for the inspected strict-drop chain.
No original-paper citation was used as a substitute for checking its critical packet construction.

The original HTML was read directly, with its displayed mathematics extracted from the source's TeX alternatives for inspection.
Before fixing this unit, the inspected original was compared with the retained registered HTML and found byte-identical; no separate persistent is introduced here.
The main algebraic identities, support boundaries, action accounting, denominator induction and asymptotic comparisons were checked analytically.
No numerical seed search, quantitative certificate computation, source program execution or formal proof-assistant check was performed.
No separate erratum search or later-version comparison was performed, so the finding remains specific to arXiv v1.

Theorem 1.2's numerical deficits, Appendices A--D and their verification artifacts are outside this unit's proof verdict.
A nonconstructive finite choice of the packet index and repetition count does not supply a practically computed original-law certificate or a numerical value of \(R\).
The analytic result is restricted to the two stated quartic Salem polynomials and does not establish the analogous assertion for higher Salem degree or arbitrary algebraic parameters.
Correlation-dimension drop alone does not assert a Hausdorff-dimension drop or singularity; the companion manuscript was not inspected here.
No concrete mathematical objection remained at the end of this source inspection.
A materially changed source version or a use beyond these hypotheses requires an affected-scope recheck.

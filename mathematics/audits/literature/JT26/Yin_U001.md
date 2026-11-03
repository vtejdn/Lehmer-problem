---
author: Yin
---
# JT26-U001: fixed coefficient-congruence Mahler gaps and explicit constants

<a id="jt26-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Jha--Thangadurai, On Lehmer's Problem, arXiv:2610.33631v1, 24 October 2026; [retained 40-page original](../../../literature/pdf/JT26--arxiv-v1.pdf).

Passages: Theorem 1.1, printed/PDF p.2; Corollary 1.1 and equations (1.1)--(1.5), p.3; necessary Section 2 conventions and Theorem 2.6, pp.5--10; complete Section 3, pp.10--16.

Inspection: Independent targeted inspection of the complete Theorem 1.1/Corollary 1.1 proof chain, including Lemmas 3.1--3.4, Propositions 3.1--3.2, all residue and degree cases, and the exact external interfaces below. This is not a whole-paper review; later alternating-coefficient results, examples and stronger bounds are outside scope.


Review performed on 2026-10-28; human record author Yin.
The source inspector was separately assigned the identified primary paper and intended G0001 use, without the main agent's proof-development discussion or previous JT26 assessment.
The main agent had checked bibliographic identity and the initial statement only.
A further isolated agent inspected the DNS17 primary interface from the stated mathematical requirements.
Neither inspector participated in developing JT26's proof.
Existing Bil97 evidence is reused only at its expressly accepted source-statement scope.

**State: Audited within scope; accepted for use with the fixed-modulus and fixed-residue hypotheses stated below.**
No unresolved mathematical dependency was found in this selected chain.
The distinction between the original DNS17 metric and JT26's restatement is explicit below.
Acceptance of the established external inputs does not assert fresh audits of their complete proofs.

<a id="statement-and-constants"></a>
## Exact source statement and constants

Fix integers \(m\ge2\) and \(0\le r<m\).
The source class \(\mathscr P_{m,r}\) consists of the monic polynomials
\[
P(x)=x^d+a_{d-1}x^{d-1}+\cdots+a_1x+1\in\mathbb Z[x]
\]
which are reciprocal, irreducible over \(\mathbb Q\), noncyclotomic, have \(d\ge2\), and satisfy \(a_j\equiv r\pmod m\) for every \(1\le j<d\).
Here reciprocity is \(x^dP(1/x)=P(x)\).
An odd degree would force the root \(-1\), so every polynomial in this class has even degree.
Irreducibility and noncyclotomicity exclude every root of unity, including \(1\) and \(-1\).

Use the existing [Mahler/absolute-height normalization](../Smy08/Yin_U001.md#smy08-height-normalization):
\[
M(P)=\prod_{P(\beta)=0}\max(1,|\beta|),\qquad
H=\log M(P),\qquad h(\alpha)=H/d
\]
for any root \(\alpha\) of this monic irreducible polynomial.
Roots count with multiplicity; irreducibility in characteristic zero also makes this particular polynomial separable.
The lower bound is for total \(H\), not for a degree-normalized quantity.

Theorem 1.1 gives a computable \(c_{r,m}>1\), depending only on the fixed pair, such that \(M(P)\ge c_{r,m}\) for every degree in this class.
For \(1\le r<m\), choose an integer \(c\equiv r-1\pmod m\) of minimum absolute value and put \(\delta=|c|\le m/2\).
At an even-modulus tie either sign is allowed.
Corollary 1.1 supplies
\[
c_{r,m}=
\begin{cases}
\sqrt{m^2+1}/2,&r=0,\\
(\sqrt{m^2+1}/2)^{2/3},&r=1,\\
m^{1/123341},&r=2,\ m\ge3,\\
(\sqrt{(m/2)^2+1}/2)^{2/3},&m\ge4\text{ even},\ \delta=m/2,\\
\exp(\eta(m,\delta)),&\delta\ge2,\ 2\delta<m.
\end{cases}
\]
These are positive lower-bound constants, not asserted optimal values or attained infima.

In the last case set
\[
\Delta=\log\frac{m}{2\delta}>0,\quad K_\delta=\frac{36\pi}{\delta-1},\qquad
8K_\delta\sqrt{\frac{\log(D_0+1)}{D_0}}\le\frac{\Delta}{4},
\]
where \(D_0\ge4\) is the least even integer satisfying the displayed inequality.
Since \(\log(x+1)/x\) decreases to zero, such an integer exists and the inequality holds for all \(d\ge D_0\).
The remaining constants are
\[
V(D_0)=\min_{\substack{4\le d<D_0\\d\ {\rm even}}}
 \frac14\left(\frac{\log\log d}{\log d}\right)^3,
\quad
\eta(m,\delta)=\min\left\{
\log\frac32,\log\frac{3+\sqrt5}{2},V(D_0),
\frac{\Delta}{40},\frac{9\Delta^2}{128K_\delta^2}
\right\}.
\]
The empty minimum is \(+\infty\).
Every nonempty finite-minimum term is positive because \(d\ge4\).
All auxiliary choices depend only on \(m,\delta\); no hidden degree-dependent positive gap is substituted for the claimed bound.

<a id="polynomial-conventions"></a>
## Polynomial conventions needed by the proof

For nonzero polynomials \(A(x)=a\prod_{j=1}^n(x-\alpha_j)\) and \(B\) over \(\mathbb C\), of degrees \(n\) and \(s\), respectively, use
\[
\operatorname{Res}(A,B)=a^s\prod_{j=1}^n B(\alpha_j).
\]
The roots are counted with multiplicity.
In particular, when \(A\) is monic, no leading-coefficient factor remains.
Only absolute resultants are used in the inequalities, so swapping the two polynomials cannot change them.
For \(F(x)=\sum_j f_jx^j\), its coefficient length and circle supremum are
\[
L(F)=\sum_j|f_j|,\qquad \|F\|_{\infty,\mathbb T}=\max_{|z|=1}|F(z)|.
\]
These are the conventions of JT26 Section 2; the resultant product formula makes its implicit normalization explicit.
The complete definitions are registered in the [concept index](../../../definitions/index.md#mahler-heights-and-house).
The actual comparison polynomials below are instances in the proof, not additional versions of these definitions.

<a id="proof-chain"></a>
## Checked internal proof chain

For \(r=0\), write \(P=(x^d+1)+mS\).
Both \(\operatorname{Res}(P,x^d-1)\) and \(\operatorname{Res}(P,x^d+1)\) are nonzero integers, and the second is divisible by \(m^d\).
With \(D=m^2+1\) and \(G(y)=(1-y)(1+y)^{m^2}\), direct maximization on the unit circle gives
\[
\|G\|_{\infty,\mathbb T}=\frac{2^D m^{m^2}}{D^{D/2}}.
\]
The elementary polynomial bound
\[
|G(z)|\le\|G\|_{\infty,\mathbb T}\max(1,|z|)^D
\]
follows by the maximum principle inside the unit disk and its reciprocal-polynomial version outside.
Multiplication over the roots yields
\[
m^{dm^2}\le
|\operatorname{Res}(P,x^d-1)|\,|\operatorname{Res}(P,x^d+1)|^{m^2}
\le\|G\|_{\infty,\mathbb T}^{d}M(P)^{dD}.
\]
Taking the \(dD\)-th root cancels \(m^{m^2/D}\) and proves \(M(P)\ge\sqrt{D}/2\).
This checks Lemma 3.1, including the powers of \(d\) and \(m\); its exclusion of cyclotomic factors is necessary.

For the generic case define
\[
R_{d,c}=x^d+(1+c)(x^{d-1}+\cdots+x)+1,\qquad
A_{d,c}=(x-1)R_{d,c}=x^d(x+c)-(1+cx).
\]
If \(P\ne R_{d,c}\), then \(P-R_{d,c}=mS\) with nonzero integral \(S\) of degree below \(d\).
Irreducibility makes \(\gcd(P,S)=1\), whence
\[
|\operatorname{Res}(P,R_{d,c})|\ge m^d,\qquad
|\operatorname{Res}(P,A_{d,c})|\ge m^d.
\]
The second statement also uses the nonzero integer \(P(1)\).
This is Lemma 3.2; congruence alone would not give its nonvanishing.

Lemma 3.3 controls the excluded equality case.
For \(c\ge2\), \(A_{d,c}(-c)=c^2-1>0\), while the odd-degree monic polynomial tends to \(-\infty\) to the left, giving a root below \(-c\).
For \(c=-b\le-2\) and even \(d\ge4\), evaluation at \(3/2\) is negative because
\[
A_{d,-b}(3/2)\le-\tfrac12(3/2)^d+2<0,
\]
while the polynomial tends to \(+\infty\) to the right.
The resulting root exceeds \(3/2\).
For \(d=2\), a reciprocal monic integral \(x^2+ax+1\) is irreducible and noncyclotomic only if \(|a|\ge3\), and its measure is at least \((3+\sqrt5)/2\).
Consequently \(H<\log(3/2)\) excludes \(P=R_{d,c}\).

Under this small-measure assumption, reciprocity gives \(2/3<|\beta|<3/2\) for every root.
Pair roots as \(\alpha,\alpha^{-1}\), with \(|\alpha|\ge1\); circle roots cause no problem, and \(\pm1\) are excluded.
Then
\[
\sum_{\rm pairs}\log|\alpha|=H,\quad
A_{d,c}(\alpha^{-1})=-\alpha^{-(d+1)}A_{d,c}(\alpha).
\]
Set \(f(z)=\log|z+c|\) and \(g(z)=\log|(1+cz)/(z+c)|\).
For real \(c\) with \(|c|\ge2\),
\[
|1+cz|^2-|z+c|^2=(c^2-1)(|z|^2-1).
\]
Thus the ratio has modulus at least one outside the unit disk.
The factorization of \(A_{d,c}\), the triangle inequality, and
\(f(\alpha^{-1})=f(\alpha)+g(\alpha)-\log|\alpha|\) give
\[
\log|A_{d,c}(\alpha)A_{d,c}(\alpha^{-1})|
\le d\log|\alpha|+f(\alpha)+f(\alpha^{-1})+g(\alpha)+2\log2.
\]
Along the radial segment from the circle to \(\alpha\), the source bounds the absolute radial derivative of \(g\) by \(7<8\).
All denominators stay away from zero on the indicated annulus, so \(g(\alpha)\le8\log|\alpha|\).
Summing the paired estimate proves the complete Lemma 3.4 inequality
\[
\log m\le
\frac1d\log|\operatorname{Res}(P,A_{d,c})|
\le(1+8/d)H+\frac1d\sum_{P(\beta)=0}\log|\beta+c|+\log2.
\tag{A}
\]

For the qualitative Proposition 3.1, JT26 Theorem 2.6(1)--(2) is applicable.
A sequence of distinct integral polynomials with \(M(P_\nu)\to1\) cannot have bounded degrees, because coefficient bounds give only finitely many possibilities in each bounded degree range.
For example the source's looser bound \(|a_j|\le4^D\) suffices when \(d\le D\) and \(M(P)\le2\).
Every root is nontorsion and its absolute height is \(H_\nu/d_\nu\to0\).
The one-dimensional Bilu strictness condition is satisfied, and all conjugates eventually lie in a fixed annulus about the circle.
A continuous radial cutoff supported away from \(-c\) therefore makes \(\log|z+c|\) a legitimate bounded compactly supported test.
Bilu's limit and the circle mean \(\log\delta\) turn (A) into \(\log m\le\log(2\delta)\), contrary to \(m>2\delta\).
No equidistribution theorem is applied directly to a singular unbounded logarithm.

Theorem 2.6(3), although unnecessary for this result, was also checked at its stated interface.
The tuple \((\alpha_\nu,\alpha_\nu^{d_\nu})\) has projective height \(d_\nu h(\alpha_\nu)=H_\nu\to0\).
A fixed nontrivial character relation forces \(r+sd_\nu=0\); because \(d_\nu\to\infty\), only finitely many indexed terms can satisfy it.
This is the required strictness, and does not assert that each individual tuple is multiplicatively independent.

<a id="effective-test-conventions"></a>
## Effective test, metric and Fourier conventions

Write \(z=e^{u+2\pi i\theta}\), \(w=e^{v+2\pi i\phi}\), with real \(u,v\) and \(\theta,\phi\in\mathbb R/\mathbb Z\).
JT26 uses the geodesic product metric
\[
\rho_{\rm geo}(z,w)^2=(u-v)^2+\min_{k\in\mathbb Z}|\theta-\phi+k|^2.
\]
DNS17 instead uses the normalized chord product metric
\[
\rho_{\rm ch}(z,w)^2=(u-v)^2+
  |e^{2\pi i\theta}-e^{2\pi i\phi}|^2/(2\pi)^2.
\]
For either specified metric, \(\operatorname{Lip}_\rho(F)\) is the supremum of
\(|F(z)-F(w)|/\rho(z,w)\) over distinct \(z,w\in\mathbb C^*\).
For a periodic differentiable real function \(f\), use
\[
\widehat{f'}(n)=\int_0^1f'(\theta)e^{-2\pi in\theta}\,d\theta,\qquad
\|\widehat{f'}\|_{\ell^1}=\sum_{n\in\mathbb Z}|\widehat{f'}(n)|.
\]
This is not the \(L^1\) norm of the derivative on the circle.
Haar probability is \(d\theta\), equivalently \(dt/(2\pi)\).
These distinct metrics and the Fourier normalization are registered in the concept index.

For the actual source test
\[
F_c(z)=\log|c+z/|z||,\qquad f_c(\theta)=\log|c+e^{2\pi i\theta}|,
\]
the circle restriction is real and \(C^\infty\), and its mean is \(\log\delta\).
For circle points \(a,b\), the elementary logarithm estimate gives
\[
|\log|c+a|-\log|c+b||\le |a-b|/(\delta-1).
\]
Consequently the same bound
\(\operatorname{Lip}_{\rho_{\rm ch}}(F_c)\le2\pi/(\delta-1)\)
holds for the ORIGINAL DNS17 metric.
The Fourier expansion
\[
f_c(\theta)=\log\delta+
\operatorname{Re}\sum_{k\ge1}\frac{(-1)^{k+1}e^{2\pi ik\theta}}{kc^k}
\]
is absolutely convergent, and differentiation yields
\(\|\widehat{f_c'}\|_{\ell^1}=2\pi/(\delta-1)\).
Thus DNS17 directly permits \(c(F_c)\le36\pi/(\delta-1)=K_\delta\).
The constant is independent of \(d\), including for negative \(c\).

The literal geodesic wording of JT26 Theorem 2.2 is not an exact quotation of DNS17's metric.
The needed application above uses the original theorem directly and needs no replacement argument.
The DNS17 inspector also checked the source's radial/angular split: Proposition 3.2 uses global Lipschitz control only for radial pairs, whose two distances agree; Proposition 3.5 separately controls the angular Fourier term.
That explains the geodesic restatement as an adaptation, rather than silently identifying the metrics.

<a id="explicit-degree-split"></a>
## Effective inequality and all degree/residue cases

The accepted DNS17 theorem, with \(h(\alpha)=H/d<1\), gives
\[
\left|\frac1d\sum_{P(\beta)=0}F_c(\beta)-\log\delta\right|
\le K_\delta\sqrt{\frac{4H+64\log(d+1)}d}.
\]
On \(2/3<|z|<3/2\), direct radial differentiation gives
\[
|\log|z+c|-F_c(z)|\le R_\delta|\log|z||,\qquad
R_\delta=\frac3{2\delta-3}\le3.
\]
Reciprocity gives the exact identity \(\sum_\beta|\log|\beta||=2H\).
Combining these facts with (A) proves JT26 equation (3.21):
\[
\Delta\le \left(1+\frac{8+2R_\delta}{d}\right)H
 +K_\delta\sqrt{\frac{4H+64\log(d+1)}d}.
\]
The coefficient of \(H\) is at most \(15\), a harmless loose bound.
For \(d\ge D_0\), split the square root to obtain
\[
3\Delta/4\le15H+2K_\delta\sqrt{H/d}.
\]
If \(H\ge\Delta/40\), the required minimum bound follows.
Otherwise \(15H<3\Delta/8\), and squaring the remaining positive inequality gives
\[
H\ge\frac{9\Delta^2d}{256K_\delta^2}
 \ge\frac{9\Delta^2}{128K_\delta^2}.
\]
For even \(4\le d<D_0\), Voutier supplies \(H>V(D_0)>0\).
For \(d=2\), the earlier reciprocal quadratic estimate supplies
\(H\ge\log((3+\sqrt5)/2)\).
The branch \(H\ge\log(3/2)\) was already handled.
This checks Proposition 3.2 and its effective uniformity over all degrees.

For \(r=1\), BDM07 gives the bound with exponent \(d/(d+1)\ge2/3\).
When \(m=2\), its stronger constant is \(\log5/4\); this implies JT26's weaker \(\log(\sqrt5/2)\) constant.
The same observation handles \(q=m/2=2\) in the even-modulus tie case.
For \(r=2\), necessarily \(m\ge3\), and
\[
R_{d,1}=(x+1)(1+x+\cdots+x^{d-1})
\]
shows the needed divisibility modulo \(m\).
Silverman's Lemma 2.1 applies with its \(D=n=d\), since \(\log m\ge\log2>1/16\).
For even \(m\ge4\) and \(\delta=m/2\), reduction modulo \(q=m/2\) places every coefficient in the class \(1\bmod q\).
Finally, after removing \(r=0,1,2\), a minimum representative cannot have \(\delta=0\) or \(1\): the representative \(-1\) would give \(r=0\).
The remaining cases are precisely the tie branch or \(\delta\ge2,\ 2\delta<m\).
In particular both classes for \(m=2\) are covered separately.

<a id="external-inputs"></a>
## Accepted external interfaces and actual inspection limits

| Input | Exact primary statement and applicability | Inspection and acceptance boundary |
| --- | --- | --- |
| Bilu 1997 | [Bil97-U001](../Bil97/Yin_U001.md#strict-small-points-and-orbit-measures), Theorem 1.1: fixed-dimensional strict small-height sequences have full Galois-orbit measures converging to Haar probability on the unit polycircle. | Reuse the existing checked primary statement and conventions; the application above was independently checked. No fresh audit of Bilu's complete proof. |
| BDM07 | [Published original](../../../literature/pdf/BDM07.pdf), printed 348--349 and 355--356/PDF 2--3 and 9--10: class \(D_m\), Corollaries 3.4--3.5. For degree \(d\), all coefficients \(1\bmod m\), no cyclotomic factors, \(\log M\ge d\,b_m/(d+1)\), with \(b_2=\log5/4\), \(b_m=\log(\sqrt{m^2+1}/2)\) for \(m>2\). | Newly checked exact statements and required congruence/degree interface, with printed 355/PDF 9 rendered. The existing [BDM07-U001](../BDM07/Yin_U001.md#bdm07-u001) had a narrower auxiliary-attribution scope; it is not silently expanded. Accept these established statements; no full BDM07 proof audit. |
| Silverman 2012 | [Published original](../../../literature/pdf/Sil12--published.pdf), Remark 1.2 and geometric-sum convention printed 755/PDF 6; Lemma 2.1 printed 760/PDF 11. Its \(\Phi_{n-1}\) means \(1+x+\cdots+x^{n-1}\), not the single standard cyclotomic polynomial. For monic degree \(D\), no roots of unity, this divisor modulo \(m\), and \(\log m\ge D/(16n)\), \(\sum h(\alpha)\ge(\log m)/123341\). | Complete relevant statement, normalization and first-case applicability checked; printed 760 rendered. For our irreducible \(P\), the height sum is exactly \(d h(\alpha)=H\). Accept the established lemma; no complete Silverman proof or elliptic-curve review. |
| Voutier 1996 | [Author rendering arXiv:1211.3110v1](../../../literature/pdf/Vou96--arxiv-v1.pdf), definition p.1 and unnumbered Theorem p.3: nonzero algebraic \(\alpha\), \(d\ge2\), not a root of unity, gives \(d h(\alpha)>\tfrac14(\log\log d/\log d)^3\). | Exact statement and normalization read, p.3 rendered; it is sufficient for even \(d\ge4\). Accept this established theorem. The full original proof and its numerical subarguments were not re-audited; the retained 17-page author layout is not claimed to be the 15-page published layout. |
| DNS17 | [Published original](../../../literature/pdf/DNS17--published.pdf), Theorem 1.2 and following constant bound printed 1630/PDF 6; metric p.1629/PDF 5; Fourier normalization p.1631/PDF 7; generalized degree p.1636/PDF 12. | The isolated inspector checked these exact interfaces and selected radial/angular proof steps at printed 1639--1640, 1644--1647/PDF 15--16, 20--23, with all listed pages rendered. Accept the established theorem in the exact original metric; its complete proof, Favre--Rivera-Letelier input and appendices were not fully audited. |

For DNS17, the actual one-dimensional theorem permits real global Lipschitz \(F\) for \(\rho_{\rm ch}\), circle restriction \(C^2\), any nonzero algebraic \(\alpha\) of height at most one, and discrepancy bounded by
\[
\left(2\operatorname{Lip}_{\rho_{\rm ch}}(F)+16\|\widehat{F_0'}\|_{\ell^1}\right)
\sqrt{4h(\alpha)+64\log(d+1)/d}.
\]
There is no compact-support, global \(C^2\), or nontorsion requirement.
The generalized degree is
\(\mathcal D(\alpha)=\min_{n\ne0}|n|[\mathbb Q(\alpha^n):\mathbb Q]=d\),
as explicitly proved in DNS17 Section 2.3.
The inequality \(d\le |n|[\mathbb Q(\alpha^n):\mathbb Q]\) follows from the degree-at-most-\(|n|\) equation over \(\mathbb Q(\alpha^n)\), and \(n=1\) supplies equality.
Thus neither the Fourier norm nor the degree in the effective error has been replaced by an uncontrolled quantity.

<a id="scope-and-search"></a>
## G0001 scope and stopping point

This source supplies a family of rigorously inspected positive gaps for the [unrestricted G0001 task](../../../tasks/Yin_T_G0001_v1.md).
It does not supply a covering theorem for arbitrary coefficient vectors.
For each application \(m,r\) are fixed before the degrees vary.
The source gives no uniform positive infimum of these displayed constants over all possible \(m,r\), and no reduction of all irreducible reciprocal integral polynomials to one such class.
Arbitrary residue patterns, factors that fail the inherited congruence, nonmonic polynomials, and the unrestricted Lehmer conclusion are not consequences of this unit.

The abstract's isolated reference to an irreducible polynomial \(Q\), while the displayed polynomial is \(P\), is treated as a notation slip; the complete Theorem 1.1 statement fixes the intended object.
Theorems 1.2--1.5, Sections 4--10, alternating residue classes and example irreducibility claims are not accepted or reviewed here.
Section 2 preliminaries serving only those later results were read for orientation but are outside this proof verdict.

The bounded source search checked the existing bibliography and source units, reused Bil97/BDM07, and located the three missing exact primary interfaces above.
Searches used the authors, exact titles and, for Silverman, the distinctive constant 123341.
The source follow-up stopped after those interfaces and the metric issue were resolved.
No current-best-bound or literature-priority assertion is made.
No source code or formalization was inspected, no numerical experiment is a premise, and no project Claim or Task assessment is changed by this unit.

The JT26 statement, Sections 2--3 and all necessary argument text were inspected from the retained PDF extraction.
Printed/PDF pages 3, 8 and 11--16 were additionally rendered and visually checked for constants, exponents, radicals, pair identities and the final degree split.
The new external primary sources and their actual editions are registered independently of this inspection account.

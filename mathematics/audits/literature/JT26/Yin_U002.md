---
author: Yin
---
# JT26-U002: alternating coefficient classes and the explicit modulus-five gap

<a id="jt26-u002"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Jha--Thangadurai, On Lehmer's Problem, arXiv:2610.33631v1, 24 October 2026; [retained original](../../../literature/pdf/JT26--arxiv-v1.pdf), exact.

Passages: Theorem 1.3, printed/PDF p.4; complete Section 7, pp.26--29; complete Section 8, pp.29--34; necessary Lemmas 2.1--2.2, p.5, and Theorem 2.6(1), pp.9--10.

Inspection: Independent complete inspection of the general fixed-\((m,a,b)\) proof and the separate explicit \((5,4,2)\) proof, with the precise retained external inputs below. Theorems 1.2, 1.4 and 1.5, Sections 4--6 and 9--10, are outside this verdict.


Review performed on 2026-10-28; human record author Yin.
The source inspector received the identified Theorem 1.3 statement and fixed source, without the main agent's application development or proof assessment.
A separate source-inspection subagent checked Section 7 from its statement and primary paper without a previous Section 7 assessment or proof-development discussion.
The first inspector checked Section 8 and integrated the two nonoverlapping findings.
Both inspectors were outside development of the external proof.
The earlier [JT26-U001](Yin_U001.md#jt26-u001) remains fixed at its Theorem 1.1/Corollary 1.1 scope.

**State: Audited within scope; accepted for use under the exact coefficient, irreducibility and fixed-parameter restrictions below.**
No unresolved mathematical dependency or concrete proof defect was found in these selected chains.
The general existence argument is qualitative; only the specified modulus-five case has the explicit constant checked here.

<a id="mahler-and-orbit-conventions"></a>
## Exact statement and conventions

Fix \(m\ge3\) and distinct residues \(a,b\in\{0,\ldots,m-1\}\).
Write the full degree as \(n=2d\ge2\), and let
\[
P(x)=x^n+c_{n-1}x^{n-1}+\cdots+c_1x+1\in\mathbb Z[x]
\]
be monic, reciprocal, irreducible over \(\mathbb Q\), and noncyclotomic.
The coefficient conditions are
\[
c_{n-j}=c_j,\qquad
c_{2j+1}\equiv a\pmod m\ (0\le j<d),\qquad
c_{2j}\equiv b\pmod m\ (1\le j<d).
\]
For \(d=1\) the even-interior condition is empty.
Theorem 1.3 asserts a number \(c_{m,a,b}>1\), depending only on the fixed triple, such that every such \(P\), in every even degree, satisfies \(M(P)\ge c_{m,a,b}\).
It further asserts
\[
c_{5,4,2}\ge(976/975)^{1/3}.
\]
Section 7 uses \(d\) for the full degree, while the statement and Section 8 use \(2d\).
All degree-dependent estimates below use \(n\) for the full degree.

Use the complete [one-variable normalization](../Smy08/Yin_U001.md#smy08-height-normalization) and [resultant/length conventions](Yin_U001.md#polynomial-conventions).
Thus \(H=\log M(P)=n h(\alpha)\) for any root \(\alpha\).
The [two-variable Mahler integral](../Den09/Yin_U001.md#mahler-measure) is
\(m_2(F)=\int_{\mathbb T^2}\log|F|\,d\lambda\), with natural logarithms, normalized Haar probability, and ordinary integrable logarithmic singularities.
JT26 writes \(\mathcal M(F)\) for this logarithmic quantity; it is not the multiplicative \(M(P)\).
The joint orbit probabilities, projective tuple height and strictness are those in [Bil97-U001](../Bil97/Yin_U001.md#strict-small-points-and-orbit-measures).
These existing complete definition homes are reused without introducing new normalizations.

<a id="finite-quadratic-lifts"></a>
## Section 8: a fixed finite choice with a nonzero remainder

Choose integral \(A,E\) with \(A\equiv a\pmod m\) and \(E\equiv b-1\pmod m\), and put
\[
G_{A,E}(x)=x^2+Ax+E,\quad
G_{A,E}^*(x)=x^2G_{A,E}(1/x)=1+Ax+Ex^2,
\]
\[
Q_{d,A,E}(x)=x^{2d}+1+
 A\sum_{j=0}^{d-1}x^{2j+1}+(E+1)\sum_{j=1}^{d-1}x^{2j}.
\]
The star uses this fixed degree-two reversal, even when \(E=0\) lowers the degree of the reversed polynomial.
The source identity is exactly
\[
(x^2-1)Q_{d,A,E}=x^{2d}G_{A,E}-G_{A,E}^*.
\tag{1}
\]
It follows by telescoping the two parity sums.
Every allowed \(P\) has \(P=Q_{d,A,E}+mR_{A,E}\) with integral \(R_{A,E}\) of degree below \(2d\).

Lemma 8.1 constructs a fixed set \(S\) of at most two pairs, depending only on \(m,a,b\), such that \(M(G_{A,E})<m\) for every pair and some pair gives \(R_{A,E}\ne0\) for every allowed \(P\) of degree at least four.
Here are the complete necessary estimates.

Jensen's inequality and Parseval give
\[
M(x^2+Ax+E)\le\sqrt{1+A^2+E^2}.
\]
Take centered representatives \(A_0,E_0\) with absolute values at most \(m/2\).
Then \(1+A_0^2+E_0^2\le1+m^2/2<m^2\).
If both are zero, use \(S=\{(0,0)\}\).
Otherwise put \(u=\max(|A_0|,|E_0|)\), \(v=\min(|A_0|,|E_0|)\), so \(1\le u\le m/2\), \(0\le v\le u\).
Shift a coordinate having absolute value \(u\) by \(-m\) times its sign, leaving the other unchanged.
The second pair is distinct, has the same residues, and satisfies
\[
m^2-\{1+(m-u)^2+v^2\}
=2mu-u^2-v^2-1\ge2u^2-1>0.
\]
Thus both pairs give strictly smaller Mahler measure than \(m\).

For two distinct pairs, the two \(Q\)'s cannot agree when \(d\ge2\): their difference has one coefficient difference on the nonempty odd block and the other on the nonempty even-interior block.
Therefore a fixed \(P\) cannot equal both comparisons.
In the singleton case,
\[
Q_{d,0,0}=1+x^2+\cdots+x^{2d}
=\frac{x^{2d+2}-1}{x^2-1}
\]
is a product of cyclotomic polynomials, so it cannot equal the allowed irreducible noncyclotomic \(P\).
This checks the nonzero-remainder guard without assuming it from congruence alone.
The extra \(m=2\) calculation in the lemma is outside the selected Theorem 1.3 statement; no extension of its stated modulus range is adopted.

<a id="general-bilu-proof"></a>
## Section 8: full orbit, truncation and contradiction

Suppose the infimum in the fixed triple were one.
Every allowed polynomial has measure above one, so the source can choose infinitely many distinct \(P_k\) with \(H_k=\log M(P_k)\to0\).
The bounded-degree coefficient argument from Theorem 2.6(1), already checked in [JT26-U001](Yin_U001.md#proof-chain), gives \(n_k=\deg P_k\to\infty\).
In particular the quadratic case is eventually absent.
For each \(P_k\), choose one pair in the fixed finite \(S\) for which the remainder is nonzero.
Passing to an infinite subsequence fixes a single pair \((A,E)\) and hence a single polynomial \(G\), with \(M(G)<m\).
This fixedness is essential before applying equidistribution.

For a root \(\alpha_k\) put \(\xi_k=(\alpha_k,\alpha_k^{n_k})\).
Its projective height tends to zero, since
\[
h(\xi_k)\le h(\alpha_k)+h(\alpha_k^{n_k})
=(1+1/n_k)H_k\longrightarrow0.
\]
If a fixed proper algebraic subgroup contained infinitely many such points, a fixed nonzero integer character \((r,s)\) would give
\(\alpha_k^{r+sn_k}=1\).
No \(\alpha_k\) is a root of unity, so \(r+sn_k=0\), which can hold for only finitely many indexed terms as \(n_k\to\infty\).
Thus the sequence is strict in the precise Bilu sense.
The joint orbit has exactly \(n_k\) points, because its first coordinate is \(\alpha_k\); no unverified output-degree identification is used.

Define the fixed nonzero polynomial
\[
F(z,w)=wG(z)-G^*(z).
\]
Equation (1), with \(P_k=Q_{n_k/2,A,E}+mR_k\), gives at every conjugate \(\alpha\)
\[
F(\alpha,\alpha^{n_k})=-m(\alpha^2-1)R_k(\alpha).
\]
Irreducibility, \(R_k\ne0\), \(\deg R_k<n_k\), and exclusion of \(\pm1\) prove that
\(\operatorname{Res}(P_k,(x^2-1)R_k)\) is a nonzero integer.
Consequently the full embedding average satisfies
\[
\frac1{n_k}\sum_\alpha\log|F(\alpha,\alpha^{n_k})|
=\log m+\frac1{n_k}\log|\operatorname{Res}(P_k,(x^2-1)R_k)|
\ge\log m.
\tag{2}
\]
The absolute-value bars in this displayed source argument were visually verified.

With \(L=2(1+|A|+|E|)\), the triangle inequality gives
\[
|F(z,w)|\le L\max(1,|z|)^2\max(1,|w|).
\]
Hence
\[
\Psi(z,w)=\log|F(z,w)|-\log L-2\log^+|z|-\log^+|w|\le0,
\]
with value \(-\infty\) on the zero set of \(F\).
For the joint orbit probability \(\mu_k\), the height sums and (2) yield
\[
\int\Psi\,d\mu_k\ge\log m-\log L-(1+2/n_k)H_k.
\tag{3}
\]
All these orbit values are finite by the resultant guard.

For \(T>0\), \(\Psi_T=\max(\Psi,-T)\) is bounded and continuous on \((\mathbb C^*)^2\), including at zeros of \(F\).
Bilu applies to these tests.
The source's compact-cutoff justification is also valid: reciprocity gives
\[
\int\bigl(|\log|z||+|\log|w||\bigr)\,d\mu_k
=(2/n_k+2)H_k\longrightarrow0.
\]
For every fixed positive annular width, Markov's inequality makes the mass outside the corresponding compact neighborhood tend to zero.
The cutoff error for the bounded test is at most \(T\) times that vanishing mass.
This is concentration of mass; it does not assert that every conjugate of \(\alpha_k^{n_k}\) lies in one fixed annulus.
Thus
\[
\int\Psi_T\,d\mu_k\longrightarrow\int_{\mathbb T^2}\Psi_T\,d\lambda.
\]
Since \(\Psi\le\Psi_T\), (3) gives
\[
\log m-\log L\le\int_{\mathbb T^2}\Psi_T\,d\lambda
\]
for every fixed \(T\).
Monotone convergence applied to \(0\le-\Psi_T\uparrow-\Psi\), using the retained integrability fact for nonzero Laurent polynomials, permits \(T\to\infty\).
The logarithmic terms \(\log^+|z|,\log^+|w|\) vanish on the torus, so
\[
\log m\le m_2(F).
\tag{4}
\]
No exchange of an unbounded singular test with a weak limit is assumed.

For almost every circle point \(z\), Jensen's formula in \(w\) gives
\[
\frac1{2\pi}\int_0^{2\pi}\log|G(z)e^{it}-G^*(z)|\,dt
=\log\max(|G(z)|,|G^*(z)|).
\]
Real coefficients and \(|z|=1\) give \(G^*(z)=z^2\overline{G(z)}\), with the conjugation visually checked in the source.
The finitely many circle zeros of \(G\) have measure zero and retain integrable logarithmic singularities.
Fubini and Jensen therefore yield
\[
m_2(F)=\frac1{2\pi}\int_0^{2\pi}\log|G(e^{it})|\,dt
=\log M(G)<\log m,
\]
contradicting (4).
This checks the complete general proof.

For \(n=2\), a reciprocal monic integral irreducible noncyclotomic \(x^2+ux+1\) has \(|u|\ge3\), hence \(M(P)\ge(3+\sqrt5)/2\).
Thus no low-degree family is left outside the original quantifier.

<a id="modulus-five-certificate"></a>
## Section 7: the explicit modulus-five certificate

Here \(n\ge2\) is even and denotes full degree.
Put
\[
U=1-x+x^2,\quad V=-3-2x+2x^2,\quad V^*=2-2x-3x^2,
\]
\[
A_n=U(1-x^n),\qquad B_n=V-x^nV^*.
\]
The section proves
\[
\|A_nB_n\|_{\infty,\mathbb T}\le25\frac{975}{976}<25.
\tag{5}
\]
The following exact estimates, not numerical maximization, justify its constant.

On \(z=e^{it}\), set \(c=\cos t\), \(s=\sin t\), \(u=z^n\) and
\(w=-(c+2)+5is\).
Then \(z^{-1}U=2c-1\), \(z^{-1}V=w\), \(z^{-1}V^*=\overline w\), and \(w\ne0\).
The sine-product identity for \(u=e^{i\phi}\) bounds the product by
\[
B(c)=2|2c-1|\{\sqrt{29+4c-24c^2}+c+2\}.
\]
Here \(B(c)\) is the scalar function called \(F(c)\) in the source, distinct from the two-variable \(F\) above.

The two exact polynomial identities are
\[
\begin{aligned}
&(25-2(2c-1)(c+2))^2-4(2c-1)^2(29+4c-24c^2)\\
&\qquad=25\{(4c^2-2c-5)^2+(4c-2)^2\},\\
&(25-2(1-2c)(c+2))^2-4(1-2c)^2(29+4c-24c^2)\\
&\qquad=25\{(4c^2-2c-3)^2+(4c+2)^2\}.
\end{aligned}
\tag{6}
\]
The first applies when \(c\ge1/2\), the second when \(c\le1/2\).
Their algebra was independently checked, including an exact integer-coefficient expansion with zero residuals.
The retained identities and interval estimates are the proof evidence; no continuing program or numerical dataset is needed.

For \(1/2\le c\le1\), the first square in its bracket is at least \(9\).
For \(-1\le c\le1/2\), either \(|4c+2|\ge1/4\), or
\[
-9/16<c<-7/16,\qquad 4c^2-2c-3\le-39/64,
\]
so the second bracket is at least \(1/16\).
Let \(t_0=|2c-1|\le3\) and \(Y=2t_0\sqrt{29+4c-24c^2}\).
Then \(25-2t_0(c+2)\ge7>0\), the brackets in (6) are positive, and \(Y<36\).
Consequently \(B(c)<25\), and the positive denominator
\(25-2t_0(c+2)+Y\) is at most \(61\).
Factoring the left side of (6) therefore gives
\[
25-B(c)\ge\frac{25}{16\cdot61}=\frac{25}{976},
\]
which proves (5).

For the allowed odd/even residue pattern \((-1,2)\bmod5\),
\[
R_{\rm alt}=U(1+x^2+\cdots+x^{n-2})
\]
has exactly the required coefficients, including the endpoints.
Since \(V\equiv V^*\equiv2U\pmod5\),
\[
A_n\equiv(1-x^2)P,\qquad B_n\equiv2(1-x^2)P\pmod5.
\]
Evaluation at every root of monic \(P\) gives
\[
5^n\mid\operatorname{Res}(P,A_n),\qquad
5^n\mid\operatorname{Res}(P,B_n).
\]
Noncyclotomicity makes the first resultant nonzero, since \(U=\Phi_6\) and every zero of \(1-x^n\) is a root of unity.
For \(n\ge4\), if the second vanished, irreducibility would force
\(B_n=(3x^2+bx-3)P\) with integral \(b\).
The \(x\) and \(x^{n+1}\) coefficients, with reciprocity, give
\[
-3c_1+b=-2,\qquad 3c_1+b=2,
\]
hence \(6c_1=4\), impossible for integral \(c_1\).
The low/high terms do not overlap in this degree range.

JT26 Lemma 2.2 gives the resultant bound
\[
|\operatorname{Res}(Q,H)|
\le\|H\|_{\infty,\mathbb T}^{\deg Q}M(Q)^{\deg H}.
\]
Its complete proof by applying the coefficient-length estimate to \(H^k\) and taking \(k\)-th roots was checked.
The required length limit is verified at the precise BDM07 interface below.
Applying it with \(\deg(A_nB_n)=2n+4\), the two nonzero resultants and (5) give
\[
25^n\le|\operatorname{Res}(P,A_nB_n)|
\le(25\cdot975/976)^n M(P)^{2n+4}.
\]
Thus
\[
M(P)\ge(976/975)^{n/(2n+4)}
\ge(976/975)^{1/3}\qquad(n\ge4).
\]
In Theorem 1.3's half-degree notation the stronger exponent is \(d/(2d+2)\), for \(d\ge2\).

For \(n=2\), the only inner coefficient satisfies \(c_1\equiv-1\pmod5\).
The value \(-1\) gives \(\Phi_6\) and is excluded; every other such integer has absolute value at least \(4\).
Therefore \(M(P)\ge2+\sqrt3>(976/975)^{1/3}\).
The even-interior congruence is correctly vacuous in this case.

<a id="dependencies-and-limits"></a>
## External interfaces, verification facts and limits

The general proof reuses Bilu's exact fixed-dimensional strict-sequence theorem from [Bil97-U001](../Bil97/Yin_U001.md#strict-small-points-and-orbit-measures), with its original-proof limits unchanged.
The projective height, full joint orbit, strictness and bounded-test applicability were rechecked above.
The source's Theorem 2.6 degree escape is reused from U001's actual proof check.
Neither DNS17's effective theorem nor Voutier's bound is a dependency of this Section 8 argument.

The nonzero Laurent-polynomial logarithmic-integrability statement and the one-variable Jensen normalization are accepted at the retained standard-input scope in [Den09-U001](../Den09/Yin_U001.md#mahler-measure) and [Smy08-U001](../Smy08/Yin_U001.md#smy08-height-normalization).
This uses neither Den09's separately questioned normalized-height sentence nor a new audit of its operator-algebra results.
The elementary Parseval/Jensen inequality and the final scalar-in-\(w\) Jensen application were checked with their actual normalized Haar integrals.

For Section 7, the inspector directly read the retained [BDM07 published original](../../../literature/pdf/BDM07.pdf), Lemma 3.2, printed 353/PDF 7, including its short proof that
\[
\lim_{k\to\infty}L(H^k)^{1/k}=\|H\|_{\infty,\mathbb T}.
\]
The coefficient \(\ell^1/\ell^2\) estimate, Parseval and the circle supremum give the stated squeeze, with the degree of \(H^k\) growing only linearly in \(k\).
This is newly performed coverage beyond [BDM07-U001](../BDM07/Yin_U001.md#bdm07-u001), retained here without expanding that earlier unit's recorded inspection.
The complete JT26 Lemma 2.2 proof and its actual resultant application were also checked.
The special case does not use Bilu, DNS17 or a numerical maximization.

Section 8 text and rendered complete PDF pages 29--34 were inspected.
The separate Section 7 inspector read its complete text and visually inspected JT26 PDF pages 5 and 26--29 and BDM07 PDF page 7.
Adjacent unselected material sharing those pages does not receive proof coverage.
The exact sum-of-squares checks are algebraic diagnostics of (6); the retained mathematical argument includes all inequalities needed for the constant.
No formalization or external proof-assistant code was inspected.

For [G0001](../../../tasks/Yin_T_G0001_v1.md), this provides positive gaps for each fixed modulus and each fixed alternating pair.
It does not cover arbitrary residue patterns, a varying period, or unrestricted coefficients, and does not remove irreducibility or the noncyclotomic restriction.
The general proof supplies no displayed numerical or effective value of \(c_{m,a,b}\).
The inspected value \((976/975)^{1/3}\) belongs to the stated \((5,4,2)\) family only.
No project Claim adoption or Task completion follows from this source unit.

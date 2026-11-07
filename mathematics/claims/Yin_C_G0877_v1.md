---
author: Yin
---

# Eventual irreducibility of the odd-prime square family

Provenance: project deduction for Yin in the bounded discussion of the November 2026 commit.
The coordinating agent developed the logarithmic test at the poles and the factor-count argument, and a contributing agent checked the pole count, specialization and symmetry.
The quantitative discrepancy input is the published theorem at the precise scope cited below.

<a id="statement"></a>
## Irreducibility and its consequence for Lehmer's problem

Let \(p\) run over the odd primes, put \(A_p=(z-1)\Phi_{8p}(z)\), \(B_p=(z+1)\Phi_{4p}(z)^2\), and set
\[
                         H_p=(A_p^2+B_p^2)/2 .
\]
For all sufficiently large primes \(p\), \(H_p\) is irreducible over \(\mathbb Q\).
In particular there is a constant \(c>0\) such that \(m(f)=\log M(f)\ge c\) for every odd prime \(p\) and every nonconstant monic integral divisor \(f\) of \(H_p\).
There is no sequence of irreducible factors of degree \(o(p)\) as \(p\) tends to infinity.
This proof gives neither a numerical irreducibility threshold nor a gap for unrestricted monic integer polynomials.

<a id="factor-inputs"></a>
## Gaussian factors, a small norm and the degree estimate

Put \(K=\mathbb Q(i)\), \(U=(z-1)(z^2+1)^2\), \(V=(z+1)(z^4+1)\),
\[
 a=(U-iV)/(1-i),\qquad b=2iV/(1-i),\qquad q(z,t)=a(z)(t^2+1)-b(z)t.
\]
Here \(a\) is monic of degree five, \(a,b\in\mathbb Z[i][z]\) have no common zero, and
\[
 q(z,z^{2p})=D(z) (A_p-iB_p)/(1-i),\qquad D=(z^4+1)(z^2+1)^2 .
\]
Use the [Gaussian component identity](../ledger/Yin_L_G0458_v5.md#prime-template-specialization-limit), [C871 squarefreeness](Yin_C_G0871_v1.md#statement), the [factorwise height bound](Yin_C_G0873_v1.md#argument) and the [exact dyadic norm](Yin_C_G0873_v1.md#dyadic-identity).

For any rational irreducible factor \(f\mid H_p\), select a root \(\beta\) with \(A_p(\beta)/B_p(\beta)=i\), and write \(g\in\mathbb Z[i][z]\) for its monic minimal polynomial over \(K\).
The inclusion \(K\subset\mathbb Q(\beta)\) gives \(n=\deg g=e/2\), where \(e=\deg f\), and the full rational conjugates consist of the roots of \(g\) and their complex conjugates.
The roots of \(g\) are precisely the conjugates on the selected Gaussian component.
Thus \(\log M(g)/n=h(\beta)\ll p^{-1}\).
By the exact dyadic norm, \(|N_{\mathbb Q(\beta)/\mathbb Q}(a(\beta))|=2^\delta\) with \(\delta\in\{0,2\}\).
Complex conjugation identifies the absolute values of the two relative norm products, so
\[
                 \frac1n\sum_{g(z)=0}\log|a(z)|=\frac{\delta\log 2}{e}.       \tag{1}
\]
The nonzero discriminant of \(g\) is a Gaussian integer, hence \(|\operatorname{disc}(g)|\ge1\).

All original roots are nontorsion units, as shown by the [cyclotomic exclusion](../ledger/Yin_L_G0458_v4.md#prime-square-no-cyclotomic-factors).
The [checked Voutier inequality](../audits/literature/JT26/Yin_U001.md#external-inputs) gives \(e h(\beta)>\frac14(\log\log e/\log e)^3\).
Here \(e\to\infty\) uniformly by Northcott finiteness and \(e\le 8p-6\).
For large \(p\), \(\log\log e\ge1\) and hence \(e\gg p/(\log(8p))^3\).
In particular \(n\gg\sqrt p\), which suffices for the quantitative argument.

<a id="poles"></a>
## A unique exterior pole and a unique exterior root near it

Under the Cayley substitution \(z=(1+iu)/(1-iu)\) one has
\[
 (U-iV)(z)=\frac{4i}{(1-iu)^5} S(u),\qquad
 S(u)=2u^5-u^4-4u^3+6u^2+2u-1.
\]
The identity follows by expanding \(z-1,z+1,z^2+1,z^4+1\) with their common denominators.
Also \(a(-1)\ne0\) and \(S(-i)\ne0\), so the Möbius coordinate loses no root.
The Sturm sequence after \(S,S'\), up to positive constant rescaling, is
\[
 21u^3-42u^2-23u+12,\quad -13u^2-10u+3,\quad -1123u+60,\quad -1.
\]
Each member is a positive multiple of the negative remainder of the preceding two.
The signs at \(-\infty\) and \(+\infty\) give respectively four and one variations.
Hence \(S\) has three real roots and one nonreal conjugate pair, all simple.
It follows that \(a\) has three simple zeros on the circle and exactly one pair \(\lambda_+,\lambda_-\) off it, where \(|\lambda_+|>1\) and \(\lambda_-=1/\overline{\lambda_+}\).
In particular \(m(a)=\log|\lambda_+|>0\) by the monic root-product formula.

Fix a small open disk \(B\) around \(\lambda_+\) whose closure lies in \(|z|>1\) and contains no other zero of \(a\).
On its boundary,
\[
 z^{-4p}q(z,z^{2p})=a(z)(1+z^{-4p})-b(z)z^{-2p}\longrightarrow a(z)
\]
uniformly.
Rouché's theorem gives exactly one root, counted with multiplicity, of \(q(z,z^{2p})\) in \(B\) for all sufficiently large \(p\).
Choose a fixed \(\eta>0\) so small that the closed radius-\(\eta\) neighborhoods of the off-circle zeros miss the unit circle, the one at \(\lambda_+\) lies in \(B\), and \(z\mapsto1/\bar z\) sends the one at \(\lambda_-\) into \(B\).

<a id="singular-test"></a>
## Passing the logarithmic test on an individual Gaussian orbit

We prove that every \(g\) as above has a zero within distance \(\eta\) of an off-circle zero of \(a\) for all sufficiently large \(p\).
Suppose to the contrary that a sequence with \(p\to\infty\) avoids both neighborhoods.

First, for any unit-circle zero \(\gamma\) of \(a\), all roots of \(g\) have \(|z-\gamma|>1/p\) for large \(p\).
Indeed, on that disk both \(|z^{2p}|\) and its reciprocal are bounded by an absolute constant independent of \(p\), since \(1-1/p\le|z|\le1+1/p\).
The exact equation \(b(z)=a(z)(z^{2p}+z^{-2p})\) for a root of \(g\) would force \(b(z)=O(1/p)\) there.
Continuity and \(b(\gamma)\ne0\) exclude this uniformly over the three disks.

All roots of \(q(z,z^{2p})\) lie in a fixed disk: it is monic with coefficient one-norm at most \(2\|a\|_1+\|b\|_1\), so the elementary Cauchy bound applies.
Fix a compactly supported real Lipschitz cutoff \(\chi\), equal to one on a disk containing these roots, the closed unit disk and all zeros of \(a\), tapering linearly to zero in a fixed surrounding annulus.
For \(\gamma\) among the five zeros put \(r_\gamma=1/p\) on the circle and \(r_\gamma=\eta\) off it.
Use the real compactly supported function
\[
 \phi_p(z)=\chi(z)\sum_{a(\gamma)=0}\log\max(|z-\gamma|,r_\gamma).
\]
On every selected root this equals \(\log|a(z)|\).
Its Lipschitz constant is \(O(p)\), and its planar Dirichlet integral is \(O(1+\log p)\).
Indeed the gradient of each truncated logarithm vanishes inside its cutoff disk and has modulus \(1/|z-\gamma|\) outside.
Integration of its square on a bounded annulus gives \(2\pi\log(R/r_\gamma)\) for a fixed sufficiently large \(R\).
The finite sum costs only a constant factor by Cauchy-Schwarz, and the gradient of \(\chi\) is supported a fixed positive distance from every zero, where all logarithms are uniformly bounded.

Apply [Pritsker's Theorem 4.2, (4.16)](../audits/literature/Pri11/Yin_U002.md#pri11-u002) to the monic polynomial \(g\) with simple zeros and the admissible varying test \(\phi_p\), choosing \(\epsilon=p^{-3}\).
With \(\mu\) normalized angular measure, the resulting bound is
\[
 \left|\frac1n\sum_{g(z)=0}\phi_p(z)-\int\phi_p\,d\mu\right|
 \ll p^{-2}
 +\sqrt{1+\log p}\,
      \sqrt{\,2h(\beta)+3\log(p)/n+4p^{-3}\,}=o(1).
\]
The negative discriminant term was dropped using its sign above.
The source statement allows complex polynomial coefficients, and neither a varying test nor a Gaussian coefficient introduces a uniformity assumption on the source theorem.
All the changing test costs appear explicitly.
On the circle the off-circle cutoffs are inactive and the three remaining truncated logarithms converge in \(L^1(\mu)\) to their actual logarithms, since each circle logarithmic singularity is integrable.
Therefore \(\int\phi_p\,d\mu\to m(a)>0\), whereas its empirical mean tends to zero by (1).
This contradiction proves the required localization uniformly in the rational factor.

<a id="irreducibility"></a>
## Why every factor needs the same root

Let \(B'\) be the image of \(B\) under \(z\mapsto1/\bar z\).
Each selected Gaussian root in \(B\) corresponds to one in \(B'\) and vice versa.
Indeed \(A_p\) is real and anti-reciprocal, \(B_p\) is real and reciprocal of the same degree, and hence
\[
 \frac{A_p(1/\bar z)}{B_p(1/\bar z)}
       =-\overline{\frac{A_p(z)}{B_p(z)}}=i
 \qquad\text{if }A_p(z)/B_p(z)=i .
\]
The extra factor \(D\) has only unit-circle roots, so the root count in \(B\) gives exactly one selected Gaussian root in each of \(B,B'\).
By the preceding localization each rational irreducible factor has a selected root in their union.

By [C871](Yin_C_G0871_v1.md#statement) exactly one rational irreducible factor \(f_*\) carries the binary block \((z+1)^2\).
The monic reciprocal associate of \(f_*\) is again a factor of the reciprocal \(H_p\), and reversal preserves divisibility by \(z+1\) modulo two since the constant coefficient is a unit.
Uniqueness therefore makes \(f_*\) reciprocal up to sign.
Its roots are closed under \(z\mapsto1/\bar z\), which also preserves the selected Gaussian component by the preceding identity.
Thus \(f_*\) contains both of the only two selected roots in \(B\cup B'\).
A second rational irreducible factor could contain neither root, contradicting localization.
Squarefreeness now proves irreducibility.

The [complete-measure bound](../ledger/Yin_L_G0458_v4.md#prime-square-original-factor-cost) gives \(m(H_p)>(8p-6)\log 2/(16p)\) in its stated range.
For all sufficiently large primes the only monic nonconstant divisor is \(H_p\) itself.
The finitely many smaller primes have finitely many divisors, each of positive logarithmic measure by cyclotomic exclusion and Kronecker's theorem.
Their finite minimum together with the complete-measure lower bound gives the asserted family gap.

## Assessment history

### Decision whole-proof

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:06 |
| status | proved |
| reason | The full proof including the unique binary endpoint factor and the logarithmic discrepancy estimate passed independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Eventual rational irreducibility, the uniform positive family gap and exclusion of sublinear factor degrees. |
| argument | [Proof section](#factor-inputs) | Relative Gaussian factors, the exact arithmetic mean and uniform degree growth. |
| argument | [Proof section](#poles) | Exact Sturm count and the single exterior root in a fixed disk. |
| argument | [Proof section](#singular-test) | Truncation, plane energy, discrepancy and forced proximity to an off-circle zero. |
| argument | [Proof section](#irreducibility) | The unique endpoint factor occupies both possible roots, squarefreeness and the family-wide gap. |
| review | [Independent finding](../audits/reviews/Yin_R_G1102_v1.md#whole-proof) | All of the selected statement and argument at the source scope specified in the finding. |

## Current assessment

[Selected decision](#decision-whole-proof)


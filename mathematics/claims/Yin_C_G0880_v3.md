---
author: Yin
---

# A whole-measure gap for moving linear cut factors times arbitrary integer squares

<a id="statement"></a>
## The full odd-grid family

Let \(p=2n+1\ge5\) be any odd integer, put \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\), and set
\[
 B_k(t)=U_k(t/2)+U_{k-1}(t/2),\qquad B=B_n,\qquad D=B_{n-1},
 \qquad U_{-1}=0.
\]
Choose an integer \(r\ge2\), an arbitrary \(v\in\mathbb Z[t]\), and \(a\in\mathbb Z\).
Define
\[
 c=-2+\frac1r,\qquad h(t)=(r(t+2)-1)v(t)^2,\qquad
 C=\operatorname{rem}_B(Dh),\qquad
 Q=(t-a)B+C,\qquad P(z)=z^{n+1}Q(z+z^{-1}).
 \tag{1}
\]
Assume \(v(b_j)\ne0\) at every grid point, that both \(b_j<c\) and \(b_j>c\) occur, and that \(Q(-2)/B(-2)<0\).
The residues of \(Q/B\) then have the strict single negative-to-positive transition in increasing trace order.
There is a constant \(\eta>0\), independent of every parameter in (1), such that
\[
                         m(P)=0\quad\hbox{or}\quad m(P)\ge\eta.
 \tag{2}
\]
Here \(m(P)=\log M(P)\) is the complete logarithmic Mahler measure of the monic reciprocal integer polynomial of degree \(2n+2\).
There is no unit assumption, degree bound, coefficient bound or fixed-resultant assumption on \(v\).
Both real and nonreal exceptional trace roots are included.

The parameter \(r=1\), whose trace \(c=-1\) has a torsion lift, is outside this statement.
It gives a fixed algebraic separator and is already covered, whenever the strict chamber is nonempty, by the [fixed-cut consequence](Yin_C_G0880_v2.md#moving-cut).
If \(3\mid p\), that parameter instead vanishes at a grid point and fails the strict hypotheses.

<a id="inputs"></a>
## Exact inputs and external-theorem scope

The [odd-grid identities](../ledger/Yin_L_G0464_v5.md#odd-grid-product) give the residue normalization and integral lift in (1).
The [resultant ceiling](../ledger/Yin_L_G0464_v6.md#norm-ceiling) applies to every sequence in this strict chamber with \(p\to\infty\) and \(1<M(P)\to1\):
\[
        \limsup |\operatorname{Res}(B,Q)|^{1/n}
                     <2\exp(-2^{-22}).
 \tag{3}
\]
Its scope includes arbitrary nonzero integer resultants.

The only external transcendence input is the bounded-height interface already retained in [Dim16-U001](../audits/literature/Dim16/Yin_U001.md#dim16-reported-bound).
For a nontorsion algebraic number \(\beta\) of degree \(d\ge2\), height \(h_{\rm W}(\beta)\le1\), and integer \(b\ge2\), that interface supplies an absolute constant \(\kappa\) with
\[
 -\log|\beta^b-1|
 \le \kappa d^4\log d\,
              \max\{h_{\rm W}(\beta),1/d\}\log b.
 \tag{4}
\]
The source is Dimitrov's arXiv:1611.04664v2, printed/PDF p.29, equation (9.1), reporting a Baker--Wustholz estimate.
The retained source inspection and the newly read text of pp.29--30 establish the stated interface and its bounded-height restriction.
The original Baker--Wustholz proof and a numerical value of \(\kappa\) are not audited here.
The root extraction below keeps every application within \(h_{\rm W}\le1\); it does not extend the accepted source statement to unbounded height.

<a id="norm-bound"></a>
## A uniform lower bound for the cut-factor norm

The consecutive recurrence \(B_k=tB_{k-1}-B_{k-2}\), with \(B_0=1\), implies \(|\operatorname{Res}(B,D)|=1\).
Since \(Q(b_j)=C(b_j)=D(b_j)h(b_j)\), the positive integer
\[
 \Delta=|\operatorname{Res}(B,Q)|
       =|\operatorname{Res}(B,h)|
       =r^n|B(c)|\,|\operatorname{Res}(B,v)|^2
       \ge r^n|B(c)|
 \tag{5}
\]
uses the full grid, including imprimitive nodes for composite \(p\).
The last resultant is a nonzero integer by the hypotheses.
Also \(D(b_j)/B'(b_j)=(4-b_j^2)/p>0\), verifying the asserted residue signs.

Let \(\alpha\) be a root of
\[
                   r z^2+(2r-1)z+r=0.
\]
The polynomial is primitive, irreducible of degree two, and has two roots on the unit circle, since its discriminant is \(1-4r<0\).
Thus \(\alpha+\alpha^{-1}=c\) and \(h_{\rm W}(\alpha)=\tfrac12\log r\).
It is nontorsion: otherwise the rational number \(c\) would be an algebraic integer, whereas \(-2+1/r\notin\mathbb Z\) for \(r\ge2\).
The cyclotomic grid identity gives
\[
              |B(c)|=\frac{|\alpha^p-1|}{|\alpha-1|}
                        \ge \frac12|\alpha^p-1|.
 \tag{6}
\]

Put \(q=\lceil\log r\rceil\ge1\) and choose any algebraic \(\beta\) satisfying \(\beta^q=\alpha\).
It is nontorsion, has degree \(2\le d\le2q\), and
\[
              h_{\rm W}(\beta)=\frac{\log r}{2q}\le1.
\]
Apply (4) with exponent \(pq\ge2\).
Since \(\max\{h_{\rm W}(\beta),1/d\}\le1\) and \(\beta^{pq}=\alpha^p\), it gives
\[
 -\log|\alpha^p-1|
           \le \kappa(2q)^4\log(2q)\log(pq).
 \tag{7}
\]
The existence of a negative block implies
\[
 r(2-2\cos(\pi/p))<1,\qquad
                 r<\frac1{2-2\cos(\pi/p)}\le\frac{p^2}{4}<p^2,
 \tag{8}
\]
where \(\sin x\ge2x/\pi\) on \([0,\pi/2]\) proves the middle inequality.
Consequently \(q\le1+2\log p\).
Combining (5)--(8), for an absolute constant \(K\) and all allowed parameters,
\[
 \frac{\log\Delta}{n}
 \ge\log r-
       K\frac{(1+\log p)^5\log(2+\log p)}{n}.
 \tag{9}
\]
In particular every sequence in this family with \(p\to\infty\) satisfies
\[
                      \liminf\Delta^{1/n}\ge2.
 \tag{10}
\]
If \(r\to\infty\), the same estimate forces \(\Delta^{1/n}\to\infty\).
No sparse-support condition on \(v\) or approximation of a particular grid pole is used.

<a id="gap-proof"></a>
## Completion for the whole polynomial

Suppose (2) fails.
There is then a sequence of whole polynomials in (1) with \(0<m(P)\to0\), and we may restrict to \(M(P)\le2\).
If the conductors are unbounded, pass to a subsequence with \(p\to\infty\).
The same strict-chamber resultant satisfies both (3) and (10), a contradiction.

If the conductors are bounded, the degrees of the monic integer polynomials \(P\) are bounded.
For a monic degree-\(d\) polynomial with \(M(P)\le2\), its \(j\)-th coefficient has absolute value at most \(2\binom dj\), by expanding its roots into elementary symmetric sums.
There are therefore only finitely many such integer polynomials over all the allowed bounded degrees.
Their strictly positive logarithmic measures cannot converge to zero.
This completes the gap argument.
The proof gives no explicit numerical value of \(\eta\).

The family (1) was proposed to remove the unit-orbit restriction while making the cut signs automatic.
Its total resultant cost already prevents the desired near-one sequence.
This conclusion does not exclude general low-norm sign representatives, arbitrary nonunit inputs in the odd-grid chamber, or the unrestricted Task.

## Assessment history

### Decision moving-linear-square-gap

| Field | Value |
| --- | --- |
| date | 2026-11-09T12:21 |
| status | proved |
| reason | Independent whole-proof review verified the all-parameter resultant lower bound, its conflict with the strict ceiling, both conductor cases and the guarded external logarithmic-form interface. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Moving linear cut family](#statement) | Every specified odd conductor, integral parameter and square factor, with a uniform qualitative whole-measure gap. |
| argument | [Exact input interfaces](#inputs) | Nonunit resultant ceiling and the bounded-height logarithmic-form theorem. |
| argument | [Uniform norm bound](#norm-bound) | Full-grid resultant, root extraction and the conductor-uniform error. |
| argument | [Complete-family gap](#gap-proof) | Unbounded and bounded conductors, including all exceptional-root types. |
| dependency | [Resultant ceiling](../ledger/Yin_L_G0464_v6.md#norm-ceiling) | The strict norm-rate ceiling for a positive shrinking sequence. |
| dependency | [Reported logarithmic-form source unit](../audits/literature/Dim16/Yin_U001.md#dim16-u001) | Only its adopted logarithmic-form interface: bounded Weil height, algebraic degree and exponent at least two; original transcendence proof and numerical constant remain external. |
| review | [Independent linear-cut finding](../audits/reviews/Yin_R_G1106_v7.md#linear-cut-square-review) | Complete new statement and argument, local ceiling support chain and exact source applicability. |

## Current assessment

[Selected decision](#decision-moving-linear-square-gap)

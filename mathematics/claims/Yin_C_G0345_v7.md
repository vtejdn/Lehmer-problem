---
author: Yin
---

# An obstruction from the interlacing numerator of a positive-constant Pisot polynomial

<a id="statement"></a>
## Exclusion of the first integer branch

Let \(f\) be the monic minimal polynomial of a Pisot number \(\theta\), with positive constant \(q=f(0)\ge2\).
Write \(g=f^*\), \(D=zf+g\), \(\delta=\theta-q\) and \(j=[z](f/g)-q^2+1\ge1\), with the coefficient taken at zero.
There is an absolute \(\eta>0\) such that every input with \(j=1\) has \(\theta-q\ge\eta\).
In particular the [necessary limiting profiles](Yin_C_G0345_v5.md#radial-limits) on that branch cannot occur as \(q\to\infty\).

More generally the [trace numerator](#trace) \(C\) has degree one less than its monic trace denominator \(B\), leading coefficient \(j\), and all its zeros in \((-2,2)\).
Write \(C=tUA\), where \(t\) is the positive integer content, \(U\) is the product of the monic irreducible factors of its primitive part, and \(A\) is the remaining primitive factor of positive leading coefficient \(c=j/t\).
An empty product is \(1\).
Along every sequence with \(\delta\to0\),
\[
  \inf_{\substack{G\in A\mathbb Z[x]\\G(2)\ne0}}
      \frac{\max_{-2\le x\le2}|G(x)|^2}{c}\ \longrightarrow\ \infty .       \tag{1}
\]
Consequently a bounded \(j\) requires an irreducible nonmonic factor of unbounded degree, in the sense that the maximum such degree tends to infinity.
At \(j=2\) exactly one primitive irreducible factor of leading coefficient two must occur eventually.
The main researcher obtained the trace transform, the torsion obstruction and the first-branch exclusion.
Agent-S contributed the integral multiplier argument for a general primitive part.

<a id="trace"></a>
## A positive partial fraction expansion

Put \(x=z+z^{-1}\), \(Y=f/D\), and define \(R\) by
\[
     R(x)=(1-z^2)Y(z)-(q-z)=\frac{zK_q(z)}{1-z^2}.
\]
Here \(K_q\) is the [integral series](../ledger/Yin_L_G0462_v36.md#limit) with constant \(j\).
The identity \(Y(1/z)=z-z^2Y(z)\) follows from \(D=zf+g\) and reciprocity.
Thus \(R\) is invariant under \(z\mapsto1/z\) and is rational in \(x\), since this involution generates the quadratic extension \(\mathbb Q(z)/\mathbb Q(x)\).
Choosing the branch \(z\to0\) at infinity gives \(R(x)=j/x+O(x^{-2})\).

The associate \(D\) has [one simple exterior root](../ledger/Yin_L_G0462_v32.md#boyd-return) \(\sigma>1\), its inverse, and [simple upward crossings](../ledger/Yin_L_G0462_v34.md#crossings) at its unit-circle roots for \(W=zf/g\) at value \(-1\).
It has no root at \(1\) because \(D(1)=2f(1)<0\).
By simplicity and reciprocal pairing, \(-1\) is present exactly when the degree is odd, and the factor \(1-z^2\) cancels its pole in \(R\).
For degree \(2m\) or \(2m+1\), respectively, write \(D=z^m B(x)\) or \(D=(z+1)z^m B(x)\).
In each case \(B\) is monic in \(\mathbb Z[x]\), since a symmetric integral Laurent polynomial is an integer polynomial in \(x\) by the recurrence for \(z^k+z^{-k}\).
It has distinct real roots, one at \(T=\sigma+\sigma^{-1}>2\) and the others in \((-2,2)\).

At a neutral root \(\zeta=e^{iu}\ne\pm1\), write \(\Psi\) for the local argument of \(W(e^{iu})\).
Since \(D=g(1+W)\) and \(W(\zeta)=-1\), the residue of \(Y\) in the \(z\) variable is \(-1/(\zeta W'(\zeta))=1/\Psi'(u)>0\).
Multiplying by \((1-\zeta^2)(1-\zeta^{-2})=4\sin^2u\) gives the residue of \(R\) at the trace.
At \(\sigma\) the corresponding residue is \((1-\sigma^2)(1-\sigma^{-2}) f(\sigma)/D'(\sigma)>0\).
Indeed the [two-point estimate](Yin_C_G0345_v4.md#two-points) gives \(\sigma<T\le2+(1-1/\theta)\delta<2+\delta\le\theta\), hence \(f(\sigma)<0\), and \(D'(\sigma)>0\) since \(\sigma\) is the largest root and is simple.
All roots of \(B\) are genuine poles with positive residues summing to \(j\).

It follows that \(C=BR\) is a polynomial of degree \(m-1\) with leading coefficient \(j\).
Its coefficients are integers since \(z=x^{-1}(1+z^2)\) has a solution in \(x^{-1}\mathbb Z[[x^{-1}]]\), and \(zK_q/(1-z^2)\) has integral coefficients in \(z\).
Between consecutive poles \(R\) decreases strictly from positive infinity to negative infinity, so there is one simple zero in each gap.
The last such zero lies below 2 since \(R(2)=1-q<0\), obtained by putting \(z=1\).
For \(m=1\) there are no zeros.
Every monic irreducible factor \(U_0\) of \(C\) has only traces of roots of unity as roots, by Kronecker's theorem applied to \(z^{\deg U_0}U_0(z+z^{-1})\).

<a id="strip"></a>
## Removing the nonmonic poles by an integral multiplier

The residues of \(R_0=R/j\) give a probability measure on the roots of \(B\).
Let \(a\) be its mean and put \(L(x)=x-a-1/R_0(x)\).
This is strictly proper by the first two terms of the expansion of \(R_0\) at infinity.
It is the transform \(\int(x-y)^{-1}\,d\lambda(y)\) of a positive measure on the zeros of \(C\), since the residues there are \(-1/R_0'(y)>0\).
The measure is zero if \(C\) is constant.
Since \(a>-2\),
\[
   0\le s=L(2)=2-a+\frac{j}{q-1}\le4+\frac{j}{q-1}.                       \tag{2}
\]

For \(G=AH\) in (1), put \(d\lambda'(y)=G(y)^2\,d\lambda(y)/c\).
Its support consists of traces of roots of unity and excludes both endpoints.
Its transform \(L'\) is the strictly proper part at infinity of \(G(x)^2L(x)/c\), since \((G(x)^2-G(y)^2)/(x-y)\) is polynomial in \(x\).
Using \(1/R_0=cB/(UA)\), divide \(AH^2B=UV+E\) by the monic \(U\) in \(\mathbb Z[x]\) with \(\deg E<\deg U\), allowing \(E=0\).
Then \(L'=-E/U\) and all its moments are integers by expansion at infinity.
Also \(B(2)/C(2)=-1/(q-1)\) and neither factor vanishes there, so
\[
   s'=L'(2)=V(2)+\frac{tG(2)^2}{q-1},
   \qquad 0\le s'\le\frac{\|G\|_{[-2,2]}^2}{c}\,s .                        \tag{3}
\]
These identities also hold for \(U=1\), when \(L'=0\).

<a id="atom"></a>
## A torsion atom approaching one from below

Lift \(\lambda'\) to the circle by distributing each mass equally between the two points \(v,v^{-1}\) over \(y=v+v^{-1}\), and call the resulting measure \(\widetilde\lambda\).
It has integer total mass and \(2\int v^k\,d\widetilde\lambda(v)\) is an integer for \(k\ge1\), since \(v^k+v^{-k}\) is a polynomial in \(y\) with integer coefficients.
Its support misses 1 and \(\int |1-v|^{-2}\,d\widetilde\lambda=s'\).
The positive torsion measure
\[
  \nu=\frac{2\,\widetilde\lambda}{|1-v|^2}
          +\bigl(\lceil2s'\rceil-2s'\bigr)\delta_1
\]
has integer total mass \(k_0=\lceil2s'\rceil\).
For \(n\ge1\), symmetry gives
\[
  \int v^n\,d\nu=k_0-\int|1+v+\cdots+v^{n-1}|^2\,d\widetilde\lambda.
\]
The last integral is integer by expanding the square into its constant and conjugate pairs of terms.
Thus all Fourier coefficients of \(\nu\) are integers.

The [exact derivative identity](../ledger/Yin_L_G0462_v36.md#second) gives \(j/\delta=q+\theta^{-1}-H'_q(0)\) with \(|H'_q(0)|\le2\).
If \(\delta\to0\), then \(q\to\infty\) by \(j\ge1\), and \(j/(q-1)\to0\).
Conversely fixed \(j\) and \(q\to\infty\) imply \(\delta\to0\).
If (1) fails, pass to a subsequence and choose admissible \(G\) with uniformly bounded \(\|G\|^2/c\).
Equations (2) and (3) bound \(k_0\), while
\[
  0<h=\frac{tG(2)^2}{q-1}\le
       \frac{j}{q-1}\frac{\|G\|^2}{c}\longrightarrow0.
\]
Since \(V(2)\) is integral, eventually \(\nu(\{1\})=1-2h\) approaches one strictly from below.
This contradicts [one-sided isolation](Yin_C_G0345_v6.md#isolation), proving (1).
When \(j=1\) we have \(A=1\), and \(G=1\) excludes any sequence with \(\delta\to0\).
More generally each primitive nonmonic irreducible factor has leading coefficient at least two, so there are at most \(\log_2 j\) such factors.
For bounded \(j\) and bounded degrees of these factors the product \(A\) has bounded degree, and \(\|A\|\le c4^{\deg A}\) because its roots lie in \((-2,2)\).
Taking \(G=A\) in (1) yields the remaining assertions.

## Assessment history

### Decision trace-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:40 |
| status | open |
| reason | Submit the integral trace obstruction and its consequences for the first and subsequent branches. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Trace obstruction](#statement) | Uniform excess on the first branch and escape of every normalized integral multiplier. |
| argument | [Trace fractions](#trace) | Integral numerator, both degree parities, all residue signs and locations of the interlacing zeros. |
| argument | [Nonmonic factors](#strip) | Positive measure, division by the monic factor and weighted trace moments. |
| argument | [Torsion measure](#atom) | Fourier integrality, endpoint fraction and consequences for bounded branch index. |
| dependency | [Atom isolation](Yin_C_G0345_v6.md#statement) | Positive finite torsion measures with bounded mass and integer Fourier coefficients. |
| dependency | [Coefficient identity](../ledger/Yin_L_G0462_v36.md#second) | Control of the branch index relative to the positive constant. |
| dependency | [Integral series](../ledger/Yin_L_G0462_v36.md#limit) | Trace transform near infinity. |
| dependency | [Crossings](../ledger/Yin_L_G0462_v34.md#crossings) | Simplicity and positive angular orientation of neutral roots. |
| dependency | [Two-point bound](Yin_C_G0345_v4.md#statement) | Order of the two exterior roots. |

### Decision trace-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:53 |
| status | proved |
| reason | Adopt the uniform first-branch gap and the multiplier obstruction after independent review for varying branch index. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Trace obstruction](#statement) | Uniform excess on the first branch and escape of every normalized integral multiplier. |
| argument | [Trace fractions](#trace) | Integral numerator, both degree parities, all residue signs and locations of the interlacing zeros. |
| argument | [Nonmonic factors](#strip) | Positive measure, division by the monic factor and weighted trace moments. |
| argument | [Torsion measure](#atom) | Fourier integrality, endpoint fraction and consequences for bounded branch index. |
| dependency | [Atom isolation](Yin_C_G0345_v6.md#statement) | Positive finite torsion measures with bounded mass and integer Fourier coefficients. |
| dependency | [Coefficient identity](../ledger/Yin_L_G0462_v36.md#second) | Control of the branch index relative to the positive constant. |
| dependency | [Integral series](../ledger/Yin_L_G0462_v36.md#limit) | Trace transform near infinity. |
| dependency | [Crossings](../ledger/Yin_L_G0462_v34.md#crossings) | Simplicity and positive angular orientation of neutral roots. |
| dependency | [Two-point bound](Yin_C_G0345_v4.md#statement) | Order of the two exterior roots. |
| dependency | [Delay-one associate](../ledger/Yin_L_G0462_v32.md#boyd-return) | Unique real exterior root and its reciprocal, with all other roots neutral. |
| dependency | [Kronecker's theorem](../audits/literature/MV226/Yin_U001.md#mv226-u001) | Monic polynomials with all roots on the circle have torsion roots. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v7.md#trace-obstruction-review) | Both degree parities, residue signs, integral weighted transform, endpoint fraction and varying-index consequence. |

## Current assessment

[Selected decision](#decision-trace-reviewed)

---
author: Yin
---

# A two-point Pisot bound and all integral preimages of a Salem polynomial

<a id="statement"></a>
## The finite excess and the integral inverse problem

Let \(f\) be the minimal polynomial of a Pisot number \(\theta\), with positive constant \(q=f(0)\ge2\), and let \(\delta=\theta-q\).
Put \(f^*=z^{\deg f} f(1/z)\).
The [positive delay-one return](../ledger/Yin_L_G0462_v32.md#boyd-return) gives a single exterior root \(\sigma>1\) of \(zf+f^*\).
With \(T=\sigma+\sigma^{-1}\) one has
\[
            T-2\le (1-1/\theta)\delta,\qquad
            (1+1/\theta)\delta\le T+2 .                              \tag{1}
\]
Both inequalities are strict in degrees greater than two.
The lower inequality is attained by the quadratics \(z^2-(q+2)z+q\).
In particular the infimum of \(\delta\) over all positive constants \(q\ge2\) equals the infimum of \(\sigma+\sigma^{-1}-2\) over Salem numbers, by (1) and the [limiting envelope](../ledger/Yin_L_G0462_v33.md#least-excess), which also treats quadratic outputs.

Fix now a Salem minimal polynomial \(P=z^m Q(z+z^{-1})\) of degree \(2m\), put \(h=m-1\), and let \(x_1<\cdots<x_h\) be the roots of the monic \(H=Q/(x-T)\) in \((-2,2)\).
At every integer \(q\ge2\), the [open simplex below](#simplex) describes precisely all Pisot minimal polynomials of degree \(2m\) with constant \(q\) and \(zf+f^*=(z+1)P\).
Their number is asymptotic to
\[
   \frac{q^h}{h!}\prod_j(2+x_j)\prod_{i<j}(x_j-x_i)                \tag{2}
\]
as \(q\to\infty\) at fixed \(P\).
If \(a_q(P)\) denotes the least \(\theta-q\) in this fiber for large \(q\), then
\[
          \liminf_{q\to\infty}q\big(a_q(P)-(T-2)\big)=T-2.           \tag{3}
\]
Thus the order \(1/q\) in the [fixed-output inverse](Yin_C_G0345_v2.md#optimum) cannot be reduced even along a favorable sequence of positive constants.

<a id="two-points"></a>
## Schwarz–Pick at the reciprocals of the two exterior roots

The pole at \(1/\theta\) is removed in the disk function
\[
       F(z)=\frac{1-\theta z}{z-\theta}\frac{f(z)}{f^*(z)} .
\]
This is a finite Blaschke product up to a sign, with one factor for each of the \(\deg f-1\) interior roots of \(f\), and \(F(0)=-q/\theta\).
Since \(zf+f^*\) is reciprocal, \(1/\sigma\) is a root and
\[
          F(1/\sigma)=\frac{\sigma(\sigma-\theta)}{\theta\sigma-1} .
\]
Indeed \(f\) and \(f^*\) are coprime since the irreducible \(f\) has positive constant \(q>1\) and cannot be proportional to its reversal.
In particular the evaluation is away from the pole of \(f/f^*\).
Schwarz–Pick at \(0\) and \(1/\sigma\), with real values at both points, gives
\[
 -\frac{q\sigma+\theta}{\theta\sigma+q}\ \le\ F(1/\sigma)\ \le
             \frac{\theta-q\sigma}{\theta\sigma-q} .
\]
The denominators are positive because \(\theta>q\) and \(\sigma>1\).
Substitute the preceding value and clear denominators; the right inequality reduces after cancellation of \((\sigma+1)\theta\sigma\) to \(T-2\le\delta(1-1/\theta)\), and the left after cancellation of \((\sigma-1)\theta\sigma\) gives the other inequality in (1).
Equality in Schwarz–Pick at distinct disk points requires a disk automorphism, which excludes \(\deg f>2\).
For the displayed quadratics one has \(zf+f^*=(z+1)(z^2-3z+1)\) and \((\theta-1)(\theta-q)=\theta\).

<a id="simplex"></a>
## Exact enumeration by positive residues

At a given constant \(q\), every monic integral solution of the reciprocal identity is uniquely of the form
\[
 f(z)=P(z)+(z-1)z^{m-1}R(z+z^{-1}),\qquad
 R=(1-q)x^h+\sum_{i=0}^{h-1}r_ix^i,\quad r_i\in\mathbb Z .           \tag{4}
\]
Indeed \(A=f-P\) satisfies \(A(z)=-z^{2m-1}A(1/z)\), so \(A/(z-1)\) is integral and reciprocal in the formal degree \(2m-2\).
After division by \(z^{m-1}\) the resulting symmetric Laurent polynomial lies in \(\mathbb Z[z+z^{-1}]\), by the recurrence for \(z^j+z^{-j}\).
The constant term of \(f\) fixes the leading coefficient of \(R\), and the converse follows from the same identity.
Put
\[
    b_j=-R(x_j)/H'(x_j),\qquad
    \frac{R(x)}{H(x)}=1-q-\sum_{j=1}^h\frac{b_j}{x-x_j} .
\]
The exact conditions for \(f\) to be a Pisot minimal polynomial are
\[
              b_j>0\quad(1\le j\le h),\qquad
              \sum_{j=1}^h\frac{b_j}{2+x_j}<q+T/2 .                   \tag{5}
\]
For the proof use the real polynomial \(F_0=p_q V\) and the circle-root derivative in the [inverse construction](Yin_C_G0345_v2.md#inward), before its choice of rounding direction.
Here \(p_q=z^2-(q+T-1)z+q\) and \(V=z^{m-1}H(z+z^{-1})\).
For \(\zeta=e^{it}\) with \(2\cos t=x_j\), \(0<t<\pi\), the value of \(C=f-F_0\) is \(2i\sin(t/2)e^{i(m-1/2)t}R(x_j)\).
Consequently the conjugate pair at \(x_j\) moves strictly inward along \(F_0+sC\) at \(s=0\) precisely when \(b_j>0\), and outward when \(b_j<0\).
A vanishing \(b_j\) would give unit-circle roots of \(f\).
Also \(F_0(-1)=(2q+T)V(-1)>0\) and \(f(-1)=(-1)^m[Q(-2)+2R(-2)]\).
Using \((-1)^{m-1}H(-2)>0\), the condition \(f(-1)>0\) is exactly the last inequality of (5).
Whenever it holds and every \(b_j\ne0\), the path has no unit root at any \(s\in(0,1]\), since the only possible locations are the unit roots of \((z+1)P\), and none can vanish there after the initial displacement.
The exterior count is then exactly one plus twice the number of negative \(b_j\).
At \(1\) one has \(f(1)=P(1)<0\); a single exterior root must therefore be real and greater than one, and strict interiority of all other roots forces irreducibility by the integer constant term of a putative remaining factor.
Conversely a Pisot solution has no unit roots and satisfies \(f(-1)>0\) by its even degree and its root signs.
The same count forces every \(b_j>0\).

The linear map from the lower coefficients \((r_i)\) to the residues, with the leading term held fixed, has absolute determinant \(1/\Delta\) for \(\Delta=\prod_{i<j}(x_j-x_i)\).
Indeed the evaluation determinant is \(\Delta\), and \(\prod_j|H'(x_j)|=\Delta^2\).
Thus (5) counts a translate of a fixed lattice of covolume \(1/\Delta\) in an open simplex of volume \((q+T/2)^h\prod_j(2+x_j)/h!\).
Tiling by any fixed bounded fundamental parallelepiped compares the count times its covolume with the volume up to \(O_P(q^{h-1})\), since only cells within bounded distance of a facet contribute to the error, uniformly in the translate.
This proves (2), also for \(h=1\).

<a id="second-order"></a>
## The smallest excess along favorable constants

At \(x_\theta=\theta+\theta^{-1}>2\), equation (4) becomes \(\theta(x_\theta-T)+(\theta-1)R(x_\theta)/H(x_\theta)=0\).
Substitution of the partial fractions gives the exact formula
\[
       \delta=\frac{\theta}{\theta-1}(T-2)+
                   \sum_{j=1}^h\frac{b_j}{x_\theta-x_j}.              \tag{6}
\]
In particular every excess in the fiber satisfies \(\delta\le T+2\) by (1), so \(\theta=q+O_P(1)\) uniformly over its points.
The positive terms in (6) give the lower bound in (3).

For the other direction write \(H=x^h+\sum_{i<h}h_i x^i\).
The numbers \(1,h_{h-1},\ldots,h_0\) are rationally independent because division of the monic integral \(Q\) by \(x-T\) makes them monic integer polynomials in \(T\) of successive degrees \(0,\ldots,h\).
Indeed \([\mathbb Q(T):\mathbb Q]=m=h+1\), since \(\sigma\) satisfies a quadratic over \(\mathbb Q(T)\) and the degree-\(m\) trace polynomial vanishes at \(T\).
The translates \((q-1)(h_0,\ldots,h_{h-1})\) modulo \(\mathbb Z^h\) are therefore equidistributed as \(q\) ranges over consecutive positive integers, by summing each nonconstant Fourier character as a geometric progression and approximating continuous functions by trigonometric polynomials.
The lower coefficients of \(R-(1-q)H\) run through these translates plus \(\mathbb Z^h\), and the residues are the image of those lower coefficients under the fixed invertible evaluation map above.
Hence for every \(\varepsilon>0\) there are arbitrarily large \(q\) and integer coefficient choices for which all \(b_j\in(0,\varepsilon)\), since the image modulo the lattice of this open box is a nonempty open set.
For large \(q\) the last inequality of (5) then holds as well.
Choose a sequence with \(\max_j b_j\to0\), and multiply (6) after subtracting \(T-2\) by \(q\).
Here \(q/(\theta-1)\to1\) and \(q/(x_\theta-x_j)\to1\) for every \(j\), giving the upper bound for the lower limit in (3).
The argument determines the optimum for a fixed Salem polynomial and supplies no sequence of distinct Salem numbers tending to one.

## Assessment history

### Decision simplex-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:01 |
| status | open |
| reason | Submit the sharp two-point bound, complete integral parametrization, fiber count and second-order optimum for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Excess and counting](#statement) | All positive-constant Pisot inputs and the exact fixed Salem fiber. |
| argument | [Two-point evaluation](#two-points) | The two inequalities, equality example and degree restriction. |
| argument | [Integral residues](#simplex) | Every integer solution, necessary and sufficient inequalities and asymptotic count. |
| argument | [Optimal second order](#second-order) | Positive correction and density of translates at fixed output. |
| dependency | [Positive return](../ledger/Yin_L_G0462_v32.md#boyd-return) | Single exterior reciprocal pair and positive root. |
| dependency | [Root motion](Yin_C_G0345_v2.md#inward) | Sign of the initial radial displacement at each neutral trace conjugate. |
| dependency | [Envelope](../ledger/Yin_L_G0462_v33.md#least-excess) | Limiting infimum, including the quadratic possibility. |

### Decision simplex-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:12 |
| status | proved |
| reason | Adopt the two-point bound and the full fixed-output inverse count and optimum after independent review at these exact scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Excess and counting](#statement) | All positive-constant Pisot inputs and the exact fixed Salem fiber. |
| argument | [Two-point evaluation](#two-points) | The two inequalities, equality example and degree restriction. |
| argument | [Integral residues](#simplex) | Every integer solution, necessary and sufficient inequalities and asymptotic count. |
| argument | [Optimal second order](#second-order) | Positive correction and density of translates at fixed output. |
| dependency | [Positive return](../ledger/Yin_L_G0462_v32.md#boyd-return) | Single exterior reciprocal pair and positive root. |
| dependency | [Root motion](Yin_C_G0345_v2.md#inward) | Sign of the initial radial displacement at each neutral trace conjugate. |
| dependency | [Envelope](../ledger/Yin_L_G0462_v33.md#least-excess) | Limiting infimum, including the quadratic possibility. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v4.md#pisot-simplex-review) | All four sections, source interfaces, equality, both endpoint signs, lattice count and second-order lower limit. |

## Current assessment

[Selected decision](#decision-simplex-reviewed)

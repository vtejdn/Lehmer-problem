---
author: Yin
---

# Integer pole mass bounds the negative-one prefix length

<a id="scope"></a>
## Arithmetic addition to the odd-grid prefix mechanism

This result adds a pointwise integer constraint to the full odd-grid prefix mechanism of [v3](Yin_C_G0881_v3.md#statement).
The conductor is divisible by three, so the rational point \(-1\) is an actual trace pole.
The argument uses the proved coordinate and quadrature interfaces of v3, then compares one mandatory integer pole contribution with an exact positive moment.
No endpoint condition, prior Mahler bound or claim of integer existence is used.

<a id="statement"></a>
## Exact integer pole bound

Let \(p=2n+1\) be an odd positive integer divisible by three.
Use \(E_{-1}=0,E_0=1,E_1=t,E_{i+1}=tE_i-E_{i-1}\), \(B_n=E_n+E_{n-1}\), and the decreasing grid
\[
                  b_j=2\cos(2\pi j/p)\qquad(1\le j\le n).
\]
Let
\[
 h=\sum_{i=0}^{n-1}a_iE_i\in\mathbb Z[t],\qquad
 \nu_j=(4-b_j^2)/p,\qquad r_j=\nu_jh(b_j).
\]
Assume a strict single cut: for some \(1\le\kappa<n\), the residues are positive for \(j\le n-\kappa\) and negative for \(j>n-\kappa\).
Choose a separator
\[
                    b_{n-\kappa+1}<c<b_{n-\kappa},
                    \qquad c<-1.
\]
Suppose the \(x=-1\) prefix coordinates hold through length \(L\):
\[
 a_0=3,\qquad a_i=4\ (i\text{ odd}),\qquad
 a_i=5\ (i\ge2\text{ even}),\qquad 0\le i\le L-2.
                                                               \tag{1}
\]
For every integer \(a\ge1\) satisfying
\[
                           6a-1\le L\le n+1,                \tag{2}
\]
one necessarily has
\[
                               27a^3\le4p.                  \tag{3}
\]

By [v3's exact coordinate identity](Yin_C_G0881_v3.md#prefix-coordinates), condition (1) is equivalent to agreement through coefficient index \(L\) with
\[
                 P_{*,-1}(z)=\frac{(1+z+z^2)^2}{(1-z)^2(1+z)}
\]
for the complete lift
\[
 C=B_{n-1}h\bmod B_n,\qquad Q=(t+2)B_n+C,\qquad
 P=z^{n+1}Q(z+z^{-1}).
\]
Here coefficient indices include zero, and the degree of \(P\) is \(2n+2\).
Only the algebraic prefix equivalence from v3 is used; its endpoint hypothesis for the separate Mahler upper bound is not needed for (3).

In particular, at \(p=19683\), no such integer input can match through any index \(L\) with
\[
                               89\le L\le9842.
\]
This excludes the stated prefix on this conductor, not the unrestricted Lehmer problem or all-conductor integer supply.

<a id="prefix-density"></a>
## The exact positive moment supplied by the prefix

Let \(d\alpha(t)=dt/(\pi\sqrt{4-t^2})\) on \((-2,2)\).
The [full odd-grid orthogonality](Yin_C_G0881_v3.md#prefix-cut-compatibility) is
\[
        \sum_j\nu_jE_i(b_j)E_k(b_j)=\delta_{ik}
                            \qquad(0\le i,k<n).
\]
Its proof uses polynomial products through degree \(2n-2\) and cyclotomic frequencies at most \(2n=p-1\), so it applies to the present composite conductor as well as to odd primes.

For the arcsine measure one has
\[
 \int E_i\,d\alpha=
 \begin{cases}1,&i\text{ even},\\0,&i\text{ odd},\end{cases}
 \qquad
 \int tE_i\,d\alpha=
 \begin{cases}0,&i\text{ even},\\2,&i\text{ odd},\end{cases}
\]
and
\[
 \int t^2E_i\,d\alpha=
 \begin{cases}
 2,&i=0,\\
 4,&i\ge2\text{ even},\\
 0,&i\text{ odd}.
 \end{cases}
\]
These follow from \(t=2\cos\theta\) and the finite sine expansion of \(E_i\).
Consequently \(\int(t+1)^2E_i\,d\alpha\) equals exactly the coordinate value in (1).
Discrete orthogonality and linearity therefore give
\[
 \sum_jr_j f(b_j)=\int (t+1)^2f(t)\,d\alpha(t)
                        \qquad(\deg f\le L-2).             \tag{4}
\]
All coordinates occurring in this calculation lie below \(n\), by (2).

Define
\[
                             \mu_j=(b_j-c)r_j>0.
\]
It follows that
\[
 \sum_j\mu_j q(b_j)=
       \int(t-c)(t+1)^2q(t)\,d\alpha(t)
                       \qquad(\deg q+1\le L-2).            \tag{5}
\]
This is an exact identity on the actual grid, not a continuous approximation to an integer input.

<a id="test-polynomial"></a>
## A polynomial normalized at the rational pole

Let \(T_m\) be the trace Chebyshev polynomial, with
\[
                       T_m(z+z^{-1})=z^m+z^{-m}.
\]
For \(a\ge1\), put
\[
 g_a(t)=\frac{2-T_{3a}(t)}{3a^2(t+1)^2},\qquad
 f_a(t)=\frac{2-T_{3a}(t)}{t+1}.                            \tag{6}
\]
Both are polynomials: \(f_a\in\mathbb Z[t]\), \(g_a\in\mathbb Q[t]\).

To see the divisibility and normalization without a limiting singular expression, define
\[
 H_a(s)=\frac{2-T_a(s)}{2-s}\in\mathbb Z[s].
\]
The identities \(T_{3a}=T_a(T_3)\) and \(2-T_3=(2-t)(t+1)^2\) give
\[
                         g_a(t)=\frac{(2-t)H_a(T_3(t))}{3a^2}.
\]
The recurrence for \(T_a\) gives \(T_a(2)=2\) and \(T_a'(2)=a^2\), so \(H_a(2)=a^2\).
It follows that
\[
                         g_a(-1)=1,\qquad \deg g_a=3a-2.    \tag{7}
\]
In particular \((t-c)g_a^2\) has degree \(6a-3\), which is at most \(L-2\) by (2).

<a id="laurent-count"></a>
## Exact Laurent coefficient count and adjacent inner product

Write \(F_a(z)=f_a(z+z^{-1})\).
Using \(t+1=(z^3-1)/(z(z-1))\) gives the exact Laurent identity
\[
 F_a(z)
 =-z^{1-3a}(z-1)(z^{3a}-1)\sum_{r=0}^{a-1}z^{3r}.          \tag{8}
\]
The product \((z^{3a}-1)\sum_{r=0}^{a-1}z^{3r}\) has \(2a\) monomials, each of coefficient \(1\) or \(-1\), whose exponents are distinct multiples of three.
Multiplication by \(z-1\) makes \(2a\) disjoint adjacent pairs of coefficients, each pair consisting of one \(1\) and one \(-1\).
Different pairs are separated by one zero coefficient.
The Laurent monomial shift and the overall sign preserve these facts.

Write \(F_a=\sum_k d_kz^k\).
There are exactly \(4a\) nonzero coefficients, all equal to \(1\) or \(-1\), and
\[
                \sum_kd_k^2=4a,\qquad
                \sum_kd_kd_{k+1}=-2a.                     \tag{9}
\]
Since \(F_a\) comes from a real polynomial in \(z+z^{-1}\), it satisfies \(d_{-k}=d_k\).
Arcsine integration is the constant Laurent coefficient, so (9) proves
\[
                 \int f_a^2\,d\alpha=4a,\qquad
                 \int t f_a^2\,d\alpha=-4a.                \tag{10}
\]

<a id="integer-mass"></a>
## The one integer value pays a fixed positive mass

From (6), \((t+1)^2g_a^2=f_a^2/(9a^4)\).
Apply (5) with \(q=g_a^2\), using the degree check in (7).
Equations (10) give
\[
 \sum_j\mu_jg_a(b_j)^2
     =\frac1{9a^4}\int(t-c)f_a(t)^2\,d\alpha(t)
     =\frac{4(-1-c)}{9a^3}.                                \tag{11}
\]

Because \(3\mid p\), the grid contains
\[
                          b_{p/3}=-1.
\]
This index lies between \(1\) and \(n\).
Since \(c<-1\), its residue is positive.
Therefore \(h(-1)\) is a positive integer and hence at least one.
At this node
\[
 r_{p/3}=\frac3p h(-1)\ge\frac3p,\qquad
 \mu_{p/3}\ge\frac{3(-1-c)}p.
\]
Its value of \(g_a^2\) is one by (7), while every other term on the left of (11) is nonnegative.
Consequently
\[
                 \frac{3(-1-c)}p
                     \le\frac{4(-1-c)}{9a^3}.
\]
Cancelling the positive factor \(-1-c\) gives (3).
Integrality is used at the specific original value \(h(-1)\), not inferred from a continuous measure or a resultant budget.

<a id="fixed-conductor"></a>
## The conductor-19683 consequence and the surviving scale

At \(p=19683\), one has \(n=9841\).
Choose \(a=15\), so \(\deg g_a=43\), the moment degree is 87, and \(6a-1=89\).
The necessary comparison fails:
\[
                 27\cdot15^3=91125>78732=4\cdot19683.
\]
Thus every matching length from 89 through 9842 is excluded under the stated integer and sign hypotheses.

More generally, taking \(a=\lfloor(L+1)/6\rfloor\) gives the necessary finite inequality
\[
                  27\left\lfloor\frac{L+1}{6}\right\rfloor^3
                       \le4p\qquad(L\ge5).
\]
Along a growing sequence this requires
\[
                        \limsup\frac{L^3}{p}\le32.
\]
It does not exclude matching lengths of logarithmic order, or prove any integer completion at a surviving length.
For conductors not divisible by three, \(-1\) is not a grid node and the mandatory integer pole-mass argument does not apply.

## Assessment history

### Decision integer-pole-prefix

| Field | Value |
| --- | --- |
| date | 2026-11-09T16:13 |
| status | proved |
| reason | Complete independent review verifies the exact integer pole bound, all stated odd conductors divisible by three, and the conductor-19683 exclusion; surviving integer supply and arbitrary-radius positive counts remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact integer pole statement](#statement) | Every stated integral strict-cut input and permitted prefix length, the cubic inequality and fixed-conductor consequence. |
| argument | [Prefix density](#prefix-density) | Composite odd-grid orthogonality, all arcsine parity cases and the exact moment range. |
| argument | [Normalized test polynomial](#test-polynomial) | Polynomial divisibility, value at the rational pole and precise degree requirements. |
| argument | [Laurent coefficient count](#laurent-count) | Exact coefficients and adjacent products for every positive integer a. |
| argument | [Mandatory integer mass](#integer-mass) | Positive integer h(-1), its original grid mass and the exact comparison. |
| argument | [Fixed and growing consequences](#fixed-conductor) | Lengths 89 through 9842 at conductor 19683 and the conditional cubic scale. |
| dependency | [Prior prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) | Algebraic original-lift and prefix equivalence, without importing the separate upper-bound endpoint assumption. |
| dependency | [Prior grid orthogonality](Yin_C_G0881_v3.md#prefix-cut-compatibility) | Full odd-grid identity through the stated degree, independent of the zero-profile specialization. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1107_v26.md#integer-pole-review) | Entire fixed statement and argument, actual input applicability and the single exact conductor-19683 calculation. |

## Current assessment

[Selected decision](#decision-integer-pole-prefix)

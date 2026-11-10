---
author: Yin
---

# Prefix rigidity for rational linear cuts times integer squares

<a id="scope"></a>
## Exact question and existing coverage

This version classifies the integer-square inputs with the first two exact \(x=0\) prefix coordinates when the unreduced input has degree below the full odd-grid denominator.
It also gives the integral quadratic forms for the prefix and endpoint, and a complete-measure control at the smallest surviving conductor.
The main research agent and the trace-deformation agent jointly developed this proof for Yin.
Put
\[
 p=2n+1,\quad n\ge2,\quad b_j=2\cos(2\pi j/p)\ (1\le j\le n),\quad
 B=B_n=E_n+E_{n-1},\quad D=B_{n-1},
\]
where \(E_{-1}=0,E_0=1,E_1=t,E_{i+1}=tE_i-E_{i-1}\).
Take
\[
 A\in\mathbb Z_{\ge1},\quad \beta\in\mathbb Z,\quad |\beta|<2A,\quad
 0\ne g\in\mathbb Z[t],\quad
 h=(At+\beta)g^2,\quad \deg h<n,
 \tag{1}
\]
and define the original lift
\[
 C=Dh\bmod B,\qquad Q=tB+C,\qquad
 P(z)=z^{n+1}Q(z+z^{-1}).
 \tag{2}
\]
The restriction in (1) concerns \(h\) itself, so none of its Chebyshev coefficients are folded modulo \(B\).
The usual remainder in the definition of \(C\) is retained.
The linear factor has its rational cut \(c=-\beta/A\) strictly inside \((-2,2)\).

The initially proposed subfamily is \(A=N,\beta=2N-1\), or \(h=[N(t+2)-1]g^2\), for an integer \(N\ge1\).
For \(N\ge2\), that subfamily is contained in [adopted C880v3](../claims/Yin_C_G0880_v3.md#statement), with its \(r=N,v=g,a=0\).
That theorem allows arbitrary integer \(g\), with no unit, degree, support, coefficient or fixed-resultant restriction.
When \(g\) has no grid zero, the separator \(c=-2+1/N\) lies strictly inside a nonempty grid gap with nodes on both sides, and \(P(-1)>0\), it supplies a uniform qualitative gap for the complete positive logarithmic Mahler measure.
Its explicitly stated \(N=1\) exception is covered by [C880v2's fixed algebraic cut consequence](../claims/Yin_C_G0880_v2.md#moving-cut), whenever the strict chamber is nonempty.
Thus growth of the support of \(g\) in that subfamily does not escape the existing whole-measure obstruction.
Those results supply no numerical gap sufficient to exclude every isolated value \(1<M(P)<6/5\).
No such whole-measure gap is asserted here for arbitrary pairs \((A,\beta)\).

The [earlier residual reduction](../ledger/Yin_L_G0462_v6.md#integer-residual) already treated the subfamily \(\beta=2A-1\) on the full quotient lattice, including the \(x=-1\) target and an integer residual sphere.
The [positive-unit square ellipsoid](../ledger/Yin_L_G0464_v10.md#moment-ellipsoid) treats a chosen sign representative times a unit square and does not assert that every positive square input has a long prefix.
The new content here is a direct classification at the first two \(x=0\) prefix coordinates under (1), before signs, endpoint or a Mahler estimate are imposed.
It does not re-prove or enlarge C880v3.

<a id="statement"></a>
## The first two coordinates determine the input

Write \(h=\sum_{i=0}^{n-1}a_iE_i\).
Under (1), the equations
\[
                         a_0=2,\qquad a_1=0               \tag{3}
\]
hold if and only if
\[
                   (A,\beta)=(2,3),\qquad g=\pm(t-1).       \tag{4}
\]
The degree condition then requires \(n\ge4\).
In the subfamily \(A=N,\beta=2N-1\), this is exactly \(N=2\).
For this input,
\[
              h=2E_0-E_2+2E_3,\qquad a_2=-1.              \tag{5}
\]
Consequently no input (1) satisfies the true \(x=0\) prefix through index \(L\ge4\), which requires \(a_0=2,a_1=0,a_2=4\).
The [exact prefix interface](../claims/Yin_C_G0881_v3.md#prefix-coordinates) uses \(2\le L\le n+1\) and fixes \(a_i\) through \(i=L-2\).
The impossibility is independent of the choice of cut, nonvanishing on the grid and endpoint.
The unique input (4) satisfies the strict original single-cut signs and endpoint for every odd \(p\ge9\), with \(P(-1)=1\).
At \(p=9\), its complete polynomial has \(M(P)\ge(21/10)^{1/4}>6/5\).
For every input (1), equations (6)--(12) give the exact integral quadratic forms for its prefix and endpoint, with the finite-grid scope stated there.
The classification proof uses Chebyshev orthogonality, the residual norm (13) and integer coefficient arithmetic; the comparison with C880v3 above is not a proof dependency.

<a id="quadratic-forms"></a>
## Semicircle normalization and integer quadratic forms

Use the probability measure
\[
                  d\mu(t)=\frac{\sqrt{4-t^2}}{2\pi}\,dt
                  \quad(-2\le t\le2).
\]
The substitution \(t=2\cos\theta\) and sine orthogonality give
\(\int E_iE_j\,d\mu=\delta_{ij}\).
Write \(d=\deg g\) and \(g=\sum_{i=0}^d u_iE_i\), with all \(u_i\in\mathbb Z\).
Then \(2d+1<n\).

For \(k\ge0\), define the symmetric integer matrix
\[
 (H_k)_{ij}=
 \begin{cases}
 1,&|i-j|\le k\le i+j,\quad k\equiv i+j\pmod2,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad 0\le i,j\le d,
 \qquad H_{-1}=0.
\]
The product identity
\[
                  E_iE_j=\sum_{\ell=0}^{\min(i,j)}E_{i+j-2\ell}
\]
proves that \((H_k)_{ij}=\int E_iE_jE_k\,d\mu\).
The recurrence for \(E_k\) now gives every actual prefix coordinate as the exact quadratic form
\[
 a_k=\mathbf u^{\mathsf T}
       \bigl[A(H_{k+1}+H_{k-1})+\beta H_k\bigr]\mathbf u.
 \tag{6}
\]
Thus the required \(x=0\) values are \(2\) for \(k=0\), \(0\) for odd \(k\), and \(4\) for positive even \(k\), up to the selected prefix limit.

Set
\[
                        M_j=\int(t+2)^j g(t)^2\,d\mu(t)
                        \quad(j\in\mathbb Z_{\ge-1}).
\]
The negative moment exists because the density divided by \(t+2\) is integrable at \(-2\).
For nonnegative \(j\), these are integer quadratic forms.
In particular, with \(u_i=0\) outside \(0\le i\le d\),
\[
 \begin{split}
 M_0&=\sum_{i=0}^d u_i^2,\\
 M_1&=2\sum_{i=0}^d u_i^2+2\sum_{i=0}^{d-1}u_iu_{i+1},\\
 y_i&=u_{i-1}+2u_i+u_{i+1}\quad(0\le i\le d+1),\\
 M_2&=\sum_{i=0}^{d+1}y_i^2,\\
 M_3&=2\sum_{i=0}^{d+1}y_i^2+2\sum_{i=0}^{d}y_iy_{i+1}.
 \end{split}                                                    \tag{7}
\]
Since \((t+2)^2=E_2+4E_1+5E_0\), the three prefix equations \(a_0=2,a_1=0,a_2=4\) are equivalent to
\[
             AM_1+(\beta-2A)M_0=2,\qquad
             AM_2+(\beta-2A)M_1=4,\qquad
             AM_3+(\beta-2A)M_2=14.                          \tag{8}
\]
The first two equations alone are equivalent to (3).
For \(A=N,\beta=2N-1\), these become exactly
\[
             NM_1-M_0=2,\qquad NM_2-M_1=4,\qquad NM_3-M_2=14.
\]

These integrals are compatible with the actual finite grid, not an asymptotic replacement.
The [full odd-grid quadrature](../ledger/Yin_L_G0464_v5.md#odd-grid-product), with \(\nu_j=(4-b_j^2)/p\), is exact for polynomial degree at most \(2n-2\).
For any coordinate test \(E_k\) with \(0\le k<n\), the product \(hE_k\) has degree at most \(2n-2\), so (6) equals \(\sum_j\nu_j h(b_j)E_k(b_j)\).
Similarly \(M_\ell=\sum_{j=1}^n\nu_j(b_j+2)^\ell g(b_j)^2\) for integers \(\ell\ge0\) whenever \(2d+\ell\le2n-2\).
The first two equations of (8) therefore hold on the finite grid for every allowed \(n\ge2\).
The third, when \(a_2\) is an available prefix coordinate, has \(n\ge3\) and the same exactness.
No claim of unrestricted rational-function quadrature is used.

<a id="endpoint"></a>
## The endpoint is another exact integer quadratic form

Define \(I_k=\int E_k(t)/(t+2)\,d\mu(t)\).
The substitution above gives
\[
 I_0=\frac1\pi\int_0^\pi(1-\cos\theta)\,d\theta=1,\qquad
 I_1=1-2I_0=-1.
\]
For \(k\ge1\), the Chebyshev recurrence yields \(I_{k+1}=-2I_k-I_{k-1}\), since \(\int E_k\,d\mu=0\).
Induction proves \(I_k=(-1)^k\) for all \(k\ge0\).
Consequently
\[
 U:=\sum_{i=0}^{n-1}(-1)^ia_i
   =\int\frac{h(t)}{t+2}\,d\mu(t)
   =AM_0+(\beta-2A)M_{-1}.                                 \tag{9}
\]
The product identity also gives
\[
 \int\frac{E_iE_j}{t+2}\,d\mu
     =(-1)^{i+j}(\min(i,j)+1),
\]
and hence the explicit integral quadratic form
\[
 M_{-1}=
 \sum_{i,j=0}^d(-1)^{i+j}(\min(i,j)+1)u_iu_j
 =\sum_{k=0}^d\left(\sum_{i=k}^d(-1)^i u_i\right)^2.        \tag{10}
\]

To check (9) against the finite endpoint, let
\(W_n=\sum_{i=0}^{n-1}(-1)^iE_i\).
The recurrence telescopes to
\[
                  (t+2)W_n=1+(-1)^{n-1}B_n.
\]
Thus \(W_n(b_j)=1/(b_j+2)\).
Finite orthogonality, applied to \(hW_n\), gives
\[
            U=\sum_j\frac{\nu_jh(b_j)}{b_j+2}.
\]
Partial fractions in the original lift (2) now give
\[
        Q(-2)/B(-2)=-2-U,\qquad P(-1)=2+U.                 \tag{11}
\]
In particular the required integer endpoint is exactly
\[
 A\sum_{i=0}^d u_i^2
 +(\beta-2A)\sum_{k=0}^d\left(\sum_{i=k}^d(-1)^i u_i\right)^2
 \ge-1.                                                   \tag{12}
\]
This establishes the actual relation to \(M_{-1}\) rather than assuming a continuum endpoint approximation.
In the originally proposed subfamily it is \(U=NM_0-M_{-1}\).
The finite sum for \(M_{-1}\) itself also agrees with (10) in the present domain: apply the same \(W_n\) identity to \(g^2\), whose degree is less than \(n\).

<a id="classification-proof"></a>
## A short residual norm classifies the first two coordinates

Let
\[
              w(t)=(At+\beta)g(t)=\sum_i w_iE_i(t).
\]
Under (3), orthogonality gives
\[
 \langle g,w\rangle_\mu=2,\qquad
 \|w\|_\mu^2
 =\int(At+\beta)h\,d\mu
 =Aa_1+\beta a_0=2\beta.                                  \tag{13}
\]
The leading Chebyshev coefficient of \(w\) is \(Au_d\ne0\).
Thus \(\beta>0\) and \(A^2\le2\beta<4A\), so \(A\le3\).
For \(A=1,2,3\), the integers \(A^2/2\le \beta<2A\) give exactly
\[
                         (A,\beta)=(1,1),(2,2),(2,3),(3,5).
\]
Replacing \(g\) by \(-g\) does not change \(h\); in each remaining case the squared norm makes \(u_d=1\) after this replacement.
All coefficient comparisons below take \(u_i=0\) outside \(0\le i\le d\).
The coefficient recurrence is \(w_i=A(u_{i-1}+u_{i+1})+\beta u_i\) for \(i\ge0\).

For \((A,\beta)=(2,2)\), the squared norm is \(4\), already exhausted by the leading coefficient \(2\).
Hence \(w=2E_{d+1}\), which has \(\langle g,w\rangle_\mu=0\), contrary to (13).

For \((A,\beta)=(3,5)\), the squared norm is \(10\) and the leading coefficient is \(3\).
The constant case \(d=0\) would also have \(w_0=5\), which is impossible.
For \(d\ge1\), the coefficient \(w_d=5+3u_{d-1}\) is nonzero and must have absolute value one.
Its residue modulo three forces \(w_d=-1\), so \(u_{d-1}=-2\), and all lower \(w_i\) vanish.
But \(w\equiv2g\pmod3\) in the integral Chebyshev basis, so \(w_{d-1}=0\) requires \(3\mid u_{d-1}\), a contradiction.

For \((A,\beta)=(1,1)\), the squared norm is \(2\), so for some \(0\le q\le d\) and \(\delta\in\{-1,1\}\),
\[
                         w=E_{d+1}+\delta E_q.
\]
In \(w=(t+1)g\), the coefficients above index \(q\) give the descending recurrence \(u_{i-1}+u_i+u_{i+1}=0\), starting from \(u_{d+1}=0,u_d=1\).
Its descending values through index \(q\) follow the periodic list \(1,-1,0,1,-1,0,\ldots\).
It follows that \(u_q\in\{-1,0,1\}\), including \(q=d\).
Therefore \(\langle g,w\rangle_\mu=\delta u_q\) cannot equal \(2\).

For \((A,\beta)=(2,3)\), the squared norm is \(6\), with leading coefficient \(w_{d+1}=2\).
The case \(d=0\) is impossible because \(w_0=3\).
For \(d\ge1\), \(w_d=3+2u_{d-1}\) is odd.
The remaining squared norm is two, so
\[
 w=2E_{d+1}+\varepsilon E_d+\delta E_q,\qquad
 0\le q<d,\qquad \varepsilon,\delta\in\{-1,1\}.              \tag{14}
\]
Moreover \(w\equiv g\pmod2\).

If \(\varepsilon=1\), then \(u_{d-1}=-1\), so parity forces \(q=d-1\).
The coefficient equation at \(d-1\) is \(\delta=-1+2u_{d-2}\).
For \(d=1\), the boundary gives \(u_{d-2}=0\).
For \(d\ge2\), parity makes \(u_{d-2}\) even, and \(\delta=\pm1\) again forces \(u_{d-2}=0,\delta=-1\).
If \(d=2\), the next equation \(w_{d-2}=0\) would read \(-2=0\).
If \(d\ge3\), it forces \(u_{d-3}=1\), contradicting parity at the zero coefficient \(w_{d-3}\).
Thus \(d=1\), and \(g=E_1-E_0=t-1\).

If \(\varepsilon=-1\), then \(u_{d-1}=-2\).
Parity and the next coefficient equation force \(d\ge2\), \(q\le d-2\) and \(u_{d-2}=2\).
Parity again gives \(q\le d-3\), so \(d\ge3\).
The equation at \(d-2\) then forces \(u_{d-3}=-1\), and hence \(q=d-3\).
At index \(d-3\), one has \(\delta=1+2u_{d-4}\).
The boundary when \(d=3\), or parity when \(d\ge4\), gives \(u_{d-4}=0,\delta=1\).
If \(d=4\), the next zero coefficient would read \(-2=0\); if \(d\ge5\), it forces the parity contradiction \(u_{d-5}=1\).
Thus the only polynomial in this branch is
\[
           g=E_3-2E_2+2E_1-E_0,\qquad w=2E_4-E_3+E_0.
\]
It has \(\langle g,w\rangle_\mu=-2\), contrary to (13).
This exhausts (14).
Finally direct multiplication for the first branch gives (5), verifying both equations (3) and proving (4).

<a id="small-control"></a>
## Endpoint success and a complete small-measure failure

For the unique input (4), (10) gives \(M_0=2,M_{-1}=5\), and hence \(U=-1\) and \(P(-1)=1\).
For every odd \(p\ge9\), its degree-three \(h\) satisfies (1).
The square factor \(g=t-1\) never vanishes at an odd-grid node, because \(2\cos(2\pi j/p)=1\) would require \(p=6j\).
The separator \(c=-3/2\) is not a grid node, since a rational root of the monic integer polynomial \(B_n\) would be integral.
There are grid nodes on both sides of it: \(b_1>0\) and \(b_n=-2\cos(\pi/p)<-3/2\).
Thus the same integer input actually satisfies the strict signs and endpoint for all these conductors.
Its next prefix coordinate fails, so the early obstruction is not an endpoint failure in disguise.

The smallest allowed conductor is \(p=9,n=4\).
The exact coordinate lift is
\[
 Q=tB_4+2B_3-B_1+2B_0=t^5+t^4-t^3-4t-1,
\]
and its complete reciprocal lift is
\[
 P(z)=z^{10}+z^9+4z^8+4z^7+3z^6+5z^5
                    +3z^4+4z^3+4z^2+z+1.                \tag{15}
\]
Newton's identities for the leading coefficient list \(1,1,4,4,3\) give the power sums
\[
                     s_1=-1,\quad s_2=-7,\quad
                     s_3=-1,\quad s_4=21.
\]
For the largest root modulus \(R\), the triangle inequality gives \(21\le10R^4\).
Since the complete Mahler measure is at least \(R\),
\[
                    M(P)\ge(21/10)^{1/4}>6/5,             \tag{16}
\]
where \(21/10>(6/5)^4\).
This proves nonneutrality and exclusion from the target interval for this full input without dropping factors, using a real-root proxy or running numerical root isolation.
It does not give the complete measure for the larger-conductor versions of (4).

<a id="limits"></a>
## Consequence and remaining boundary

In the proposed no-wrap domain, the attempt fails already at \(a_2=4\), before there can be a long prefix from which to infer a small complete measure.
The endpoint quadratic form is exact and useful for comparison, but is not needed for that impossibility.
The surviving length-three prefix gives a nonempty strict chamber with an integral endpoint, so the proof distinguishes actual supply at that short length from the missing long-prefix input.
The \(p=9\) control additionally fails the finite \(6/5\) target for the complete polynomial.

Allowing reduction of a higher-degree \(h\) modulo \(B_n\) invalidates the identification of the actual prefix with the continuum integrals in (13); the leading-coefficient norm argument therefore does not give this classification in that enlarged domain.
For the original subfamily \((A,\beta)=(N,2N-1)\), arbitrary higher-degree squares still fall under the already adopted C880v3/C880v2 whole-measure gap when their strict sign and endpoint hypotheses hold.
That comparison supplies no whole-measure theorem for arbitrary varying pairs \((A,\beta)\), with or without reduction modulo \(B_n\).
The qualitative theorem for the original subfamily does not settle every finite \(6/5\) test in its larger domain.
Neither this bounded calculation nor that existing family theorem excludes general sign representatives without the forced linear divisor, arbitrary growing collections of perturbations, or the unrestricted Task.

## Assessment history

### Decision rational-cut-prefix-rigidity

| Field | Value |
| --- | --- |
| date | 2026-11-09T19:45 |
| status | proved |
| reason | The complete all-degree integer classification, finite-grid and endpoint interfaces, and full-polynomial small control passed independent whole-proof review. This closes the stated unreduced rational linear-cut square construction for prefixes of length at least four, without asserting the unrestricted Lehmer gap or the corresponding reduced-input classification. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Rational linear-cut prefix rigidity](#statement) | The exact if-and-only-if classification, next-prefix obstruction, all-conductor short-prefix supply and complete p=9 lower bound. |
| argument | [Integer quadratic forms](#quadratic-forms) | Exact coordinate and moment forms, including their finite-grid degree limits. |
| argument | [Original endpoint](#endpoint) | Negative moment, integer tail-square form and the original strict endpoint equivalence. |
| argument | [All-degree classification](#classification-proof) | Residual norm, four parameter pairs and every degree and sign branch. |
| argument | [Complete small control](#small-control) | Actual strict signs and endpoint at all allowed conductors and the complete p=9 Newton lower bound. |
| dependency | [Odd-grid quadrature and lift](../ledger/Yin_L_G0464_v5.md#odd-grid-product) | Residue weights, integral lift and quadrature through degree 2n-2. |
| dependency | [Exact zero-profile prefix](Yin_C_G0881_v3.md#prefix-coordinates) | The true coordinate requirements and permitted prefix range. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_G1113_v1.md#linear-cut-prefix-review) | All selected mathematics and exact dependency interfaces, with the unreduced-input and older-subfamily scope limits retained. |

## Current assessment

[Selected decision](#decision-rational-cut-prefix-rigidity)


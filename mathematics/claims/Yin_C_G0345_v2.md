---
author: Yin
---

# An optimal positive-constant Pisot representation of each Salem polynomial

<a id="statement"></a>
## The size of the Pisot root at prescribed constant coefficient

Let \(P\) be the minimal polynomial of a Salem number \(\sigma\), put \(r=\deg P=2m\), and write \(T=\sigma+\sigma^{-1}>2\).
For every sufficiently large integer \(q\) there is a monic Pisot minimal polynomial \(f_q\) of degree \(r\) with positive constant coefficient \(q\), exterior root \(\theta_q\), and
\[
 z f_q(z)+f_q^*(z)=(z+1)P(z),\qquad
 \theta_q-q=T-2+O_P(q^{-1}),\qquad f_q^*(z)=z^r f_q(1/z).                \tag{1}
\]
For this fixed \(P\), the minimum of \(\theta-q\) over all such representations at constant \(q\) is also \(T-2+O_P(q^{-1})\).
In particular, there are Salem numbers tending to one if and only if there are Pisot minimal polynomials with positive constant \(q\ge2\) and \(\theta-q\to0\).
In the reverse construction one can prescribe arbitrarily large lower bounds on the successive \(q\)'s.
This equivalence concerns Salem measures within the unrestricted Lehmer problem.

[Boyd's representation theorem as stated by McKee and Smyth](../audits/literature/MS12b/Yin_U001.md#ms12b-u001) already gives infinitely many Pisot polynomials at each fixed Salem number, with plus cofactor \(z^2+1\).
Here the plus cofactor is \(z+1\), and the construction controls both the positive constant and the excess of the Pisot root over it.
The constants and the threshold on \(q\) in (1) may depend on \(P\).

<a id="rounding"></a>
## Rounding a polynomial with the prescribed reciprocal sum

Write \(P=z^m Q(z+z^{-1})\), where \(Q=(x-T)H(x)\) and \(H\) is real monic of degree \(m-1\) with simple roots \(x_j\in(-2,2)\).
These trace roots come from conjugate pairs of unit-circle roots of \(P\).
The polynomial \(V=z^{m-1}H(z+z^{-1})\) is real, monic and reciprocal.
For each \(q\ge2\), define
\[
 p_q=z^2-(q+T-1)z+q,\qquad F_0=p_q V,\qquad
 E=(1-z)z^{m-1}H'(z+z^{-1}).
\]
Here \(zp_q+p_q^*=(z+1)(z^2-Tz+1)\), so \(zF_0+F_0^*=(z+1)P=:D\).
The quadratic \(p_q\) has one root in \((0,1)\) and one above \(q\), since \(p_q(0)>0\), \(p_q(1)=2-T<0\), and \(p_q(q)=q(2-T)<0\).
The polynomial \(E\) has zero constant, degree at most \(r-2\), and \(E(z)=-z^{r-1}E(1/z)\).
Consequently \(F_0+L E\) has the same reciprocal sum for every real \(L\).

For any real monic solution \(A=\sum a_i z^i\) of this sum with constant \(q\), the coefficient pairs satisfy \(a_i+a_{r-1-i}=[z^{i+1}]D\) for \(0\le i\le r-1\).
The positions in each pair differ since \(r\) is even, and both coefficients in the endpoint pair are already integers.
In each other pair of \(F_0+LE\), round one coefficient to a nearest integer and fix the other by the prescribed integral sum.
This gives a monic integer polynomial \(f_q=F_0+C\), where \(C=LE+U\), \(C(z)=-z^{r-1}C(1/z)\), and \(\deg C\le r-2\).
The rounding error \(U\) has coefficients of absolute value at most \(1/2\), so \(\sup_{|z|=1}|U(z)|\le m\) for every \(L,q\).
In particular \(f_q(0)=q\) and \(zf_q+f_q^*=D\).

<a id="inward"></a>
## Moving every unit-circle root strictly inside

Put \(\zeta=e^{it}\), with \(0<t<\pi\), for a root of \(V\), and write \(x_j=2\cos t\).
Use \(e^{i(m-1/2)t}\) for the half-integer power along this arc.
The antisymmetry gives \(C(\zeta)=i c_j e^{i(m-1/2)t}\) with \(c_j\) real.
The contribution from \(LE\) to \(c_j\) is \(-2L\sin(t/2)H'(x_j)\).
Choose \(L>0\) depending only on \(P\) so that this contribution has absolute value greater than \(m\) at every \(x_j\).
After rounding, \(c_j/H'(x_j)<0\) and \(C(\zeta)\ne0\) at each such root.

Consider \(F_s=F_0+sC\), \(0\le s\le1\).
At the simple root \(\zeta\) of \(F_0\), the derivative of its log modulus as \(s\) increases from zero is \(-\Re(C(\zeta)/(\zeta F_0'(\zeta)))\).
At this root,
\[
 \zeta V'(\zeta)=e^{i(m-1)t}\,2i\sin(t)H'(x_j),\qquad
 \Re\big(e^{-it/2}p_q(\zeta)\big)=\cos(t/2)(x_j-T)<0 .
\]
Therefore
\[
 \Re\frac{C(\zeta)}{\zeta F_0'(\zeta)}
 =\frac{c_j}{2\sin(t)H'(x_j)}
       \Re\frac{1}{e^{-it/2}p_q(\zeta)}>0 .
\]
The conjugate root has the same radial derivative, so all roots of \(V\) enter the open disk for small positive \(s\).
Any later root on the circle would also be a zero of \(zF_s+F_s^*=D\), by real coefficients.
At the unit-circle roots of \(P\) we have \(F_s(\zeta)=sC(\zeta)\ne0\) for \(s>0\).
At the only other possible point, \(-1\), the magnitude of \(F_0(-1)=(2q+T)V(-1)\) grows with \(q\), whereas \(|C(-1)|\) is uniformly bounded.
Thus for all large \(q\) there is exactly one exterior root of \(f_q\), counted with multiplicity, and all its other roots lie in the open disk.
Moreover \(2f_q(1)=D(1)=2P(1)<0\), since \(Q(2)=(2-T)H(2)<0\).
The exterior root is consequently real and greater than one.
Any other monic integer factor would have a nonzero integer constant of modulus strictly less than one, which proves irreducibility.
In particular \(q=\theta_q\prod_{\beta\ne\theta_q}|\beta|<\theta_q\).

<a id="optimum"></a>
## The excess and its optimality

The degree-\((r-1)\) coefficient of \(f_q\) is \([z^r]D-q\).
The sum of its \(r-1\) interior roots is bounded uniformly in \(q\), so \(\theta_q=q+O_P(1)\).
The coefficients of \(C\) are bounded in terms of \(P\), and \(\deg C\le\deg V=r-2\).
Evaluating \(f_q=p_q V+C\) at \(\theta_q\) therefore gives \(p_q(\theta_q)=O_P(1)\).
Division by \(\theta_q\) yields
\[
 \theta_q-q=T-1-q/\theta_q+O_P(1/q)=T-2+O_P(1/q).
\]
For any admissible representation giving \(D\), [Boyd's inequality](../audits/literature/Boy78/Yin_U001.md#near-integer-lemma) gives the matching lower bound
\[
                 \theta-q\ \ge\ (T-2)\frac{q(q-1)}{(q+1)^2}.
\]
At a fixed sufficiently large \(q\) a minimizer exists, since degree and measure are bounded upon restricting to competitors no larger than the constructed \(\theta_q\).
Indeed each coefficient is then bounded by the measure times the corresponding binomial coefficient.
This proves the stated minimum estimate.
If \(\sigma_i\to1\), apply (1) to each fixed \(P_i\), then choose \(q_i\) large enough to make the error smaller than \(1/i\).
Conversely, the [positive delay-one return](../ledger/Yin_L_G0462_v32.md#boyd-return) sends any positive-constant Pisot sequence with \(\theta_i-q_i\to0\) to Salem numbers tending to one.
The argument does not assert that such a sequence exists.

## Assessment history

### Decision prescribed-constant-inverse

| Field | Value |
| --- | --- |
| date | 2026-11-16T12:48 |
| status | open |
| reason | Submit the construction for each sufficiently large positive constant, the optimal asymptotic excess and the Salem equivalence for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prescribed positive constant](#statement) | Fixed Salem output, every large integer constant and the Salem near-one equivalence. |
| argument | [Integral rounding](#rounding) | Reciprocal sum, exact endpoints and uniformly bounded rounding errors. |
| argument | [Strict root locations](#inward) | Every circular root moves inside and the path preserves the strict Pisot root count. |
| argument | [Optimal excess](#optimum) | Upper and lower errors at fixed output and the diagonal choice of constants. |
| dependency | [Boyd's equation (38)](../audits/literature/Boy78/Yin_U001.md#boy78-u001) | Lower bound for the excess for competitors giving the fixed Salem output. |
| dependency | [Positive delay-one return](../ledger/Yin_L_G0462_v32.md#boyd-return) | The forward implication from positive-constant Pisot seeds to Salem measures approaching one. |

### Decision prescribed-constant-inverse-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:05 |
| status | proved |
| reason | Rounding at every sufficiently large constant produces a strict Pisot minimal polynomial, and Boyd's lower estimate gives the optimal limiting excess. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prescribed positive constant](#statement) | Fixed Salem output, every large integer constant and the Salem near-one equivalence. |
| argument | [Integral rounding](#rounding) | Reciprocal sum, exact endpoints and uniformly bounded rounding errors. |
| argument | [Strict root locations](#inward) | Every circular root moves inside and the path preserves the strict Pisot root count. |
| argument | [Optimal excess](#optimum) | Upper and lower errors at fixed output and the diagonal choice of constants. |
| dependency | [Boyd's equation (38)](../audits/literature/Boy78/Yin_U001.md#boy78-u001) | Lower bound for the excess for competitors giving the fixed Salem output. |
| dependency | [Positive delay-one return](../ledger/Yin_L_G0462_v32.md#boyd-return) | The forward implication from positive-constant Pisot seeds to Salem measures approaching one. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v2.md#prescribed-constant-inverse-review) | Prescribed constants, all root displacements, absence of recrossing, optimality and equivalence at Salem outputs. |

## Current assessment

[Selected decision](#decision-prescribed-constant-inverse-reviewed)

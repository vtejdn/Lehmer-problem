---
author: Yin
---

# Trace interlacing with signed residues and a test at the central separator

The [earlier trace cells and degree-18 example](Yin_L_G0462_v1.md#complex-trace-cells) place every root of the reciprocal lift.
The signed-residue proposal seeks the same control from gaps between poles while the conductor varies.
The [whole-output gap](../claims/Yin_C_G0880_v1.md#statement) rules out all positive residues and, more generally, any uniformly bounded total variation.
The [earlier circular interlacing construction](../audits/literature/MS05/Yin_U001.md#ms05-circular-interlacing) supplies a source comparison for positive partial fractions.

<a id="chebyshev-variation"></a>
## A necessary test on the original trace polynomial

For any monic reciprocal \(P(z)=z^dQ(z+z^{-1})\) in \(\mathbb Z[z]\) of degree \(2d\), \(Q\) is monic integral of degree \(d\), by successively subtracting the symmetric power sums.
Take \(d\ge2\), \(B=U_{d-1}(t/2)\), and divide \(Q=(t-a)B+C\) with \(a\in\mathbb Z\) and \(\deg C<d-1\).
The roots \(b_j=2\cos(\pi j/d)\), \(1\le j<d\), are simple and interior.
Differentiating \(U_{d-1}(\cos\theta)=\sin(d\theta)/\sin\theta\) gives \(|B'(b_j)|=d/(2\sin^2(\pi j/d))\).
Thus every sequence of such original inputs with \(0<m(P)\to0\) necessarily satisfies
\[
     \sum_j |C(b_j)/B'(b_j)|
      =\frac2d\sum_{j=1}^{d-1}\sin^2(\pi j/d)\,
        |Q(2\cos(\pi j/d))|\ \longrightarrow\ \infty .
\]
A bounded subsequence would contradict C880 with a single common bound.
Zero residues at shared roots are allowed here.
This criterion also applies to each original positive reciprocal irreducible candidate on its own grid.
Increasing the sum by multiplying a candidate by extra cyclotomic factors gives no evidence that the positive factor meets this test on its own grid.

<a id="seed"></a>
## Positive residues realize an existing two-exterior-root control

For the [degree-nine trace \(Q_9\)](Yin_L_G0462_v1.md#complex-trace-cells), set
\[
 B=(t-2)t(t^2-2)(t^4-4t^2+2),\qquad
 C=1-22t-9t^2+48t^3+9t^4-26t^5-2t^6+4t^7 .
\]
Direct expansion gives \(Q_9=(t+3)B+C\).
In increasing order the roots of \(B\) are \(2\cos(j\pi/8)\), \(j=7,6,\ldots,0\).
The signs of \(Q_9\) there are respectively \(-,+,-,+,-,+,-,+\), hence the signs of \(B'\) there.
Indeed \(Q_9\) has remainder \(-(1+t)^2\) modulo \(t^4-4t^2+2\) and remainder \(3+2t\) modulo \(t^2-2\), with \(3-2\sqrt2>0\).
At both \(0\) and \(2\) its value is one.
The eight residues are positive with sum four, the leading coefficient of \(C\).
The complete measure bound \(1.2013475236<M(P)<1.20143521\) is the certified [J144 control](../computations/programs/Yin_J_G0144/readme.md).
This example verifies that the positive-residue class contains an actual low-measure lift.

<a id="central-sign-test"></a>
## A single sign change and its central obstruction

Take a general monic integral \(B\) of degree \(n\ge2\) with simple poles \(-2<b_1<\cdots<b_n<2\), and the notation \(Q,P,r_i\) of C880.
Suppose that \(r_i<0\) on an initial nonempty block, \(r_i>0\) on the remaining nonempty block, and \(Q(-2)/B(-2)<0\).
Across every same-sign gap the secular function has opposite infinite one-sided limits.
At the first pole its limit from the left is \(+\infty\), so the endpoint condition supplies another zero in \((-2,b_1)\).
These \(n-1\) disjoint intervals already contain \(n-1\) roots of \(Q\).
If the other two roots are a nonreal pair \(q,\bar q\), then \(m(P)=2\log|\lambda|\), where \(\lambda+\lambda^{-1}=q\) and \(|\lambda|>1\).

Test the first choice of a sign transition at the central trace \(0\), so \(b_i r_i\ge0\) for every \(i\).
Under \(m(P)\le\log2\), the unsigned mass of the weighted residues \(b_i r_i\) is bounded independently of \(n\).
Indeed, for \(h=1,2,3\), put \(\Delta_h=\sum_{Q(q)=0}q^h-\sum_i b_i^h\), counting all roots with multiplicity.
Match the leftmost chosen real zero to \(b_1\) and each gap zero to the right endpoint of its gap.
Only one pole remains unmatched, and the matching intervals have disjoint interiors.
Their contribution is bounded by the variation of \(t^h\) on \([-2,2]\), while the unmatched pole has modulus at most two and both remaining trace roots have modulus at most \(5/2\).
Thus the three \(\Delta_h\) are bounded by absolute constants.
Writing \(k=\sum r_i\) and \(l=\sum b_i r_i\), expansion of \(\log(Q/B)\) at infinity gives
\[
              a=\Delta_1,\qquad 2k=a^2-\Delta_2,\qquad
              3l=a^3-3ak-\Delta_3 .
\]
In particular \(\sum|b_i r_i|=l\) is bounded.

The proper rational function \(C_1/B=tC/B-k\), with \(C_1=tC-kB\) integral, has residues \(b_i r_i\).
Apply the [Fourier and coset argument](../claims/Yin_C_G0880_v1.md#fourier) to this proper part.
As in the [cleared identity](../claims/Yin_C_G0880_v1.md#sparse-completion), its generating function \(S_1\) is a bounded sum of signed geometric series and \(C_1/B=z(S_1-l)/(1-z^2)\) at \(t=z+z^{-1}\).
Now \(tQ/B=t(t-a)+k+C_1/B\).
Multiplying this identity by \(z^2(1-z^2)D\), where \(D\) is the product of the boundedly many coset denominators, gives an integer polynomial with bounded support whose ratio to \(P/B^*\) is \((1+z^2)(1-z^2)D\).
Its constant coefficient is one, and each cleared factor, including \(1+z^2\), has logarithmic measure zero.
The Dobrowolski–Smyth gap used in C880 therefore excludes positive whole measures tending to zero in this central sign configuration as well.
This last weighted test is a main-agent derivation with author checking.

<a id="moving-sign-test"></a>
## The remaining construction test

Use the Chebyshev grid on the original polynomial, allow the sign transition to move between adjacent poles, and retain the left endpoint sign.
The first target is an unbounded-degree sequence of actual integral candidates with a single nonreal pair in one fixed ellipse of exterior radius \(\rho>1\), together with growing total residue variation on the positive factor's own grid.
Require the root count, the variation and the full cost on the same candidates before tightening \(\rho\) toward one.
Checking the variation of the whole lift suffices only when it is itself the candidate for which the root and cost statements are made.
The fixed ellipse tests simultaneous feasibility and supplies no vanishing measure by itself.
A varying transition with bounded variation still falls under C880, and the central trace with the endpoint sign falls under the weighted test above.
The first explicit sequence meeting the moving-sign requirements and the subsequent shrinkage of the exterior radius both remain open.

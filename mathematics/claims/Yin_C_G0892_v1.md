---
author: Yin
---

# A uniform linear bound for integer matching lengths at the exceptional parents

<a id="statement"></a>
## Statement and construction

There is an absolute finite constant \(C\) with the following property.
Let \(s\ge2\) be an integer, \(r>2s+3\) odd, \(m=(r-1)/2\), \(n=m+s\) and \(p=2n+1\).
Put \(t=z+z^{-1}\), \(E_{-1}=0\), \(E_0=1\), \(E_{k+1}=tE_k-E_{k-1}\), \(B_k=E_k+E_{k-1}\), and
\[
 F_s(z)=(1+z^2)^2(1+z^2+\cdots+z^{2s-2}),\qquad
 Q_0(t)=t^2E_{s-1}(t)B_m(t).
\]
For any \(H\in\mathbb Z[t]\) with \(\deg H\le n-2\), including zero, set \(Q=Q_0+H\) and \(P(z)=z^{n+1}Q(z+z^{-1})\).
Write \(b_j=2\cos(2\pi j/p)\) and \(\rho_j=Q(b_j)/B_n'(b_j)\) for \(1\le j\le n\).
Suppose that some \(1\le c<n\) gives \(\rho_j>0\) for \(j\le c\) and \(\rho_j<0\) for \(j>c\).
If \(P-F_s/(1-z)=O(z^{L+1})\), so that the coefficients through index \(L\) agree, then \(L\le Cs\).

Thus every fixed exceptional parent, including \(F_2=(1+z^2)^3\), has bounded integral matching length over all permitted conductors, cuts and perturbation coefficients.
The proof uses the strict signs alone and permits unrestricted integer coefficient heights.
It gives no numerical value for \(C\) and leaves open whether integral examples exist with both \(s\) and \(L\) growing and \(L/s\) bounded.
The [conductor-21 optimum](../ledger/Yin_L_G0457_v8.md#optimal-prefix) gives an example with \(s=2\) and \(L=7\).

<a id="moments"></a>
## The first changed residue moment

The neutral lift is \(z^{n+1}Q_0(z+z^{-1})=F_s(z)(1-z^r)/(1-z)\), by the [trace identities of the exceptional construction](../ledger/Yin_L_G0457_v7.md#effective-cutoff).
Set \(\theta_j=2\pi j/p\), \(D=B_{n-1}\), \(\nu_j=(4-b_j^2)/p\), and \(h_0(t)=t^2 E_{s-1}(t)^2\).
The sine formulas for \(B_m,B_n\) give
\[
 D(b_j)=(-1)^{j+1}2\cos(\theta_j/2),\qquad
 B_m(b_j)=D(b_j)E_{s-1}(b_j),\qquad D(b_j)/B_n'(b_j)=\nu_j.
\]
Thus the neutral residues are \(\rho^0_j=\nu_jh_0(b_j)\ge0\), and the strict negative block forces \(H\ne0\).
If \(d=\deg H\), the first differing coefficient has index \(n+1-d<r\) and equals the nonzero leading coefficient of \(H\), since the difference of the lifts is \(z^{n+1}H(t)\) and the neutral reference first changes at \(r\).
Take \(L=n-d\), the largest matching index, which suffices for the claimed upper bound.
In particular \(L\le n\).
Expansion at infinity gives
\[
 \frac{H(t)}{B_n(t)}=\sum_{j=1}^n\frac{\rho_j-\rho^0_j}{t-b_j}
   =\sum_{k\ge0}\frac{\Delta_k}{t^{k+1}},\qquad
 \Delta_k=\sum_{j=1}^n b_j^k(\rho_j-\rho^0_j).
\]
Consequently \(\Delta_k=0\) for \(0\le k\le L-2\) and \(\Delta_{L-1}=\operatorname{lc}(H)\) is a nonzero integer.

<a id="saturation"></a>
## The determinant lower bound and a positive comparison

Suppose for a contradiction that a sequence of these inputs has \(L/s\to\infty\).
Then \(L,p\to\infty\) and \(s=o(L)\).
Use the angular midpoint \(a=2\cos((2c+1)\pi/p)\) of the sign gap and the average \(\mathbb E\) over \(1\le j\le n\).
With \(b=b_j\), put
\[
 X_j=p(b-a)\rho_j>0,\qquad
 G_j=p(b-a)\rho^0_j=(b-a)(4-b^2)h_0(b),\qquad
 f_s(b)=(b+2)(4-b^2)h_0(b).
\]
For \(b=2\cos\theta\), the identity \((4-b^2)h_0(b)=4b^2\sin^2(s\theta)\) shows that \(0\le f_s\le64\), \(|G_j|\le64\), and \(G_j\le f_s(b_j)\).
For every polynomial \(A\) of degree at most \(L-3\) the moment identities give
\[
                 \mathbb E\,X_j A(b_j)=\mathbb E\,G_j A(b_j).
                 \tag{1}
\]
In particular \(0<\mathbb E X_j\le64\) eventually.

The sine formula gives \(|B_n(a)|=1/\sin((2c+1)\pi/(2p))\ge1\).
Since \(B_n(2)=p\) and \(B_n(-2)=(-1)^n\), the products of \(4-b_j^2\) and \(|D(b_j)|\) over the full grid are respectively \(p\) and \(1\), using \(D(b_j)^2=2+b_j\).
All \(Q(b_j)\) are nonzero by strictness, so their product is the nonzero integer resultant of the monic \(B_n\) and the integral \(Q\).
Multiplying \(X_j=(b_j-a)(4-b_j^2)Q(b_j)/D(b_j)\) gives
\[
                         \mathbb E\log X_j\ge0.                \tag{2}
\]
These products use every pole, including the imprimitive ones at composite \(p\).

Write \(\langle v\rangle=\pi^{-1}\int_0^\pi v(2\cos\theta)\,d\theta\).
For every polynomial \(v\) of degree less than \(p\), summing its cosine frequencies over all \(p\)-th roots of unity gives
\[
                   \mathbb E\,v(b_j)=
                   \frac{p\langle v\rangle-v(2)}{p-1}.       \tag{3}
\]
The degree of \(f_s\) is \(2s+3\).
For any fixed continuous function \(\phi\) on \([0,64]\), uniform polynomial approximation on that interval and (3) therefore give
\(\mathbb E\phi(f_s(b_j))-\langle\phi(f_s)\rangle\to0\).
Indeed a fixed approximating polynomial composed with \(f_s\) has degree \(O_\phi(s)<p\) eventually for each fixed approximation error, and its supremum norm is uniformly bounded.

Fix \(\epsilon>0\) and write \(Y_j=X_j/(f_s(b_j)+\epsilon)\).
For any accuracy \(\eta>0\) choose a polynomial \(A_\eta(u)\) uniformly within \(\eta\) of \(1/(u+\epsilon)\) on \([0,64]\).
Because \(s=o(L)\), the degree of \(A_\eta(f_s(t))\) is at most \(L-3\) eventually.
Using (1), the bounds \(\mathbb E X_j\le64\) and \(|G_j|\le64\), and the positive denominator, we obtain
\[
 \mathbb E Y_j\le\mathbb E\frac{G_j}{f_s(b_j)+\epsilon}+128\eta
 \le\mathbb E\frac{f_s(b_j)}{f_s(b_j)+\epsilon}+128\eta .
\]
Use (3) with continuous approximation as above, then let \(\eta\downarrow0\).
Together with (2) and the same quadrature for \(\log(f_s+\epsilon)\), this gives for \(\psi(y)=y-1-\log y\)
\[
 \limsup\mathbb E\psi(Y_j)\le
 \sup_{s\ge2}\left\langle
 \frac{f_s}{f_s+\epsilon}-1+\log(f_s+\epsilon)\right\rangle ,
 \qquad \limsup\mathbb E Y_j\le1.                            \tag{4}
\]

The factorization \(f_s(2\cos\theta)=4(2+2\cos\theta)(2\cos\theta)^2\sin^2(s\theta)\) gives \(\langle\log f_s\rangle=0\).
Indeed \(\pi^{-1}\int_0^\pi\log(2\sin\theta)\,d\theta=0\) by symmetry and the double-angle formula, and periodicity gives the same normalized logarithmic mean for \(2|\sin(s\theta)|\).
The two remaining factors \(2+2\cos\theta=4\cos^2(\theta/2)\) and \(|2\cos\theta|\) each have logarithmic mean zero by the same identity.
All zeros here are integrable logarithmic singularities.
More quantitatively \(\sup_{s\ge2}\langle f_s^{-1/12}\rangle<\infty\).
By Hölder's inequality with three exponents equal to three it suffices to bound the integrals of \((2+2\cos\theta)^{-1/4}\), \(|2\cos\theta|^{-1/2}\) and \(|\sin(s\theta)|^{-1/2}\).
Each singularity of the first two is at most of order one half, and the integral of the last equals that for \(s=1\) by periodicity.
The right side of (4) is thus bounded above by \(\sup_s\langle\log(1+\epsilon/f_s)\rangle=O(\epsilon^{1/12})\), using \(\log(1+x)\le12x^{1/12}\) for \(x\ge0\).

<a id="rigidity"></a>
## Convergence and the integer contradiction

For \(y>0\), \((y-1)^2\le2(1+y)\psi(y)\), by integrating \(\psi'(y)=(y-1)/y\) on the interval with endpoints \(1,y\).
Cauchy-Schwarz and (4) imply that \(\limsup\mathbb E|Y_j-1|\) tends to zero as \(\epsilon\downarrow0\).
The bound \(|X_j-f_s(b_j)|\le(64+\epsilon)|Y_j-1|+\epsilon\) now yields \(\mathbb E|X_j-f_s(b_j)|\to0\) along the proposed sequence.
Since \(f_s\ge G_j\) on the grid, (1) with \(A=1\) gives
\[
 \mathbb E|f_s(b_j)-G_j|=\mathbb E(f_s(b_j)-X_j)\to0,
 \qquad \mathbb E|X_j-G_j|\to0.                               \tag{5}
\]
The first mean in (5) equals \((2+a)\mathbb E[4b_j^2\sin^2(s\theta_j)]\).
The latter average equals \(4p/(p-1)\) by (3) and cosine orthogonality for \(s\ge2\), so the separator tends to \(-2\).

For \(k=L-1\), eventually \(k\ge2\).
The trace polynomial \(T_{k-1}(2\cos\theta)=2\cos((k-1)\theta)\) is monic of degree \(k-1\) and bounded in absolute value by two on \([-2,2]\).
Thus \((t-a)T_{k-1}(t)\) is monic of degree \(k\), so its sum against \(\rho_j-\rho_j^0\) equals the nonzero integer \(\Delta_k\) by vanishing of all the lower moments.
But its absolute value is at most
\[
       2\sum_j|(b_j-a)(\rho_j-\rho^0_j)|
       =\frac{2n}{p}\mathbb E|X_j-G_j|\longrightarrow0 .
\]
This rules out every sequence with \(L/s\to\infty\), proving the asserted existence of a single finite \(C\).

The proof is a project deduction for [G0001](../tasks/Yin_T_G0001_v1.md#contract).
The main researcher and the computational researcher developed the resultant comparison concurrently, using the [earlier positive product argument on a different grid](Yin_C_G0881_v2.md#finite-filter) as a precedent.
The one-sided comparison \(G_j\le f_s(b_j)\), regularization uniform in \(s\), and the first changed integer moment give the stated exceptional-parent bound.

## Assessment history

### Decision integral-prefix-bound-draft

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:32 |
| status | open |
| reason | Retain the uniform exceptional-parent argument for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform prefix bound](#statement) | All permitted conductors, integer heights, exceptional parents and strict terminal cuts. |
| argument | [Neutral and perturbed moments](#moments) | Longest matching index and first nonzero integer moment. |
| argument | [Product and positive comparison](#saturation) | Full-grid resultant and quadrature, with uniform regularization for changing \(s\). |
| argument | [Integer rigidity](#rigidity) | Convergence of the weighted discrepancy and the contradiction. |
| dependency | [Exceptional-parent construction](../ledger/Yin_L_G0457_v7.md#effective-cutoff) | The neutral trace lift and the original grid and residue conventions. |

## Current assessment

[Selected decision](#decision-integral-prefix-bound-draft)

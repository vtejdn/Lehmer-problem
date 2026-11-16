---
author: Yin
---

# Integral and rational central perturbations of the exceptional cyclotomic parent

The [angular matching bound for squarefree parents](../claims/Yin_C_G0890_v1.md#statement) and its [extension allowing repeated factors](../claims/Yin_C_G0890_v2.md#statement) single out the following family when the parent is allowed to have multiple roots.
For \(s\ge2\) let
\[
 F_s(z)=(1+z^2)^2\frac{1-z^{2s}}{1-z^2},\qquad d=s+1.
\]
Choose an odd \(r>2d+1\), and put \(m=(r-1)/2\), \(N=m+d\), \(n=N-1\), and \(p=2n+1=r+2s\).
Write \(E_j(2\cos\theta)=\sin((j+1)\theta)/\sin\theta\), \(B_j=E_j+E_{j-1}\), and \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\).
The trace identity is \(F_s(z)=z^d C_s(z+z^{-1})\) with \(C_s(t)=t^2E_{s-1}(t)\).
For a polynomial \(H\) of degree at most \(h\), with the zero polynomial allowed, set \(Q=C_s B_m+H\) and \(\rho_j=Q(b_j)/B_n'(b_j)\).
We seek a cut \(1\le c<n\) with \(\rho_j>0\) through \(c\), \(\rho_j<0\) thereafter, and \(Q(-2)/B_n(-2)<0\).
The following calculation for Yin's [Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract) gives an effective upper bound for \(p\) when \(H\) is integral and constructs rational perturbations of degree four for arbitrarily large \(p\).
The [independent review](../audits/reviews/Yin_R_G1107_v45.md#integral-exception-review) checks this bound, the finite coefficient test and the rational construction.

<a id="effective-cutoff"></a>
## Effective conductor bound for integral perturbations

Let \(h\ge0\) be an integer and put \(A_h=2\sum_{k=1}^h k^2\).
If \(H\in\mathbb Z[t]\) satisfies the cut and endpoint conditions, then
\[
                         p<128\pi(1+A_h)^2.                    \tag{1}
\]
The bound is uniform in \(s\) and the coefficients of \(H\).

At \(\theta=2\pi j/p\) the [grid derivative and sine identity](Yin_L_G0457_v4.md#residue-formula) give \(\rho_j\) the sign of \(W(b_j)+(-1)^{j+1}H(b_j)\), where
\[
 W(t)=\sqrt{2+t}\,D(t),\qquad D(t)=t^2E_{s-1}(t)^2.
\]
Indeed \(C_s(2\cos\theta)\sin(s\theta)/\sin(\theta/2)\) equals the displayed \(W(2\cos\theta)\) since \(\sin\theta/\sin(\theta/2)=2\cos(\theta/2)\).
In particular \(W\ge0\) throughout the grid.
Thus the \(\kappa=n-c\) consecutive negative residues force \(H\) to take strictly alternating nonzero signs on their nodes, so \(\kappa\le h+1\).
For \(-1\le t\le1\), the corresponding \(\pi/3\le\theta\le2\pi/3\) also gives the uniform bound
\[
               0\le W(t)
               =\frac{t^2\sin^2(s\theta)}{\sin\theta\sin(\theta/2)}
               \le\frac4{\sqrt3}t^2<3t^2\quad(t\ne0).        \tag{2}
\]
At \(t=0\) the phase vanishes.

Suppose \(p\ge128\pi(1+A_h)^2\) and write \(\delta=8\pi/p\).
Then \(p\ge6h+9\), so every node \(b_j\in[-1,1]\) has \(j\le p/3\le n-h-1\le c\).
Nodes of either selected parity have angular spacing \(4\pi/p\), and \(t=2\cos\theta\) has derivative of absolute value at most two.
The interval \([\pi/3,2\pi/3]\) has length greater than \(4\pi/p\), so each \(t\in[-1,1]\) lies within \(\delta\) of a node of each parity in that interval, including at its endpoints.
Applying the same spacing argument to \([\pi/3,\pi/2]\) gives nodes of both parities with \(0<b_j\le\delta\), since odd \(p\) puts no node at \(0\).

For any real polynomial \(T\) of degree at most \(h\), take its supremum norm on \([-1,1]\).
Expanding \(T(\cos\theta)\) in \(\cos(k\theta)\), orthogonality on \([0,\pi]\) bounds each nonconstant coefficient by \(2\|T\|\).
The corresponding derivative in \(t=\cos\theta\) has magnitude at most \(k^2\), by \(\lvert\sin(k\theta)\rvert\le k\sin\theta\).
Consequently \(\|T'\|\le A_h\|T\|\), and applying the same bound once more gives \(\|T''\|\le A_h^2\|T\|\).

At a point where \(\lvert H\rvert\) attains \(M=\|H\|\), choose a nearby even node if \(H\) is positive, or an odd node if \(H\) is negative.
Positive residues give \(H(b_j)<W(b_j)\) at the even node and \(H(b_j)>-W(b_j)\) at the odd one.
By (2) and the derivative bound, \(M\le3+\delta A_h M\), hence \(M\le6\) since \(\delta\le1/[16(1+A_h)^2]\).
The conclusion also holds for \(H=0\).
Using the two parities with \(0<b_j\le\delta\) now gives
\[
              |H(0)|\le3\delta^2+6A_h\delta<1,
\]
so the integer \(H(0)\) vanishes.
Taylor's estimate \(\lvert H(t)/t-H'(0)\rvert\le3A_h^2t\) for \(0<t\le1\), applied at the same two nodes, then gives
\[
               |H'(0)|\le(3+3A_h^2)\delta<1.
\]
The integer \(H'(0)\) also vanishes, and therefore \(t^2\) divides both \(H\) and \(Q\).

Under the assumed lower bound for \(p\), one has \(h\le n-2\).
The neutral lift \(F_s(z)(1-z^r)/(1-z)\) has first coefficients \(1,1,4,4\), as in the [trace division of the central construction](Yin_L_G0457_v4.md#integer-family).
In particular \(C_s B_m\) and \(tB_n\) have the same leading two coefficients, and their coefficients of \(t^{n-1}\) differ by \(4-(n+1)+(n-1)=2\).
Adding \(H\) thus gives \(Q=tB_n+C\) with \(C\in\mathbb Z[t]\) of degree \(n-1\) and leading coefficient two.
Under the stipulated signs and endpoint, the [all-cut root count](../claims/Yin_C_G0881_v10.md#nonreal-pair) puts one real root in each of \(n-1\) disjoint intervals and leaves precisely two nonreal roots of \(Q\), counted with multiplicity.
Every real root is consequently simple, contradicting \(t^2\mid Q\) and proving (1).

<a id="finite-test"></a>
## A finite test with integral coefficients of unrestricted height

For each \(h\), (1) leaves finitely many odd \(p\), and \(p>4s+3\) bounds the possible \(s\).
In the domain \(h\le n-2\), each remaining triple \(p,s,c\) requires testing only finitely many integral coefficient vectors.
To see this, replace the cut and endpoint inequalities by their weak versions to obtain a closed polyhedron in the \(h+1\) coefficients of \(H\).
In a direction \(T\) along which it can remain feasible indefinitely, the required weak signs of \(T(b_j)\) are \((-1)^{j+1}\) before and through \(c\), and \((-1)^j\) thereafter.
At the further point \(-2\) the required weak sign of \(T(-2)\) is \((-1)^{n+1}\), since \(B_n(-2)=(-1)^n\).
In decreasing order of the arguments only \(b_c,b_{c+1}\) have the same required sign.
Omit \(b_c\) to leave \(n\) distinct nodes \(x_1>\cdots>x_n\) with alternating required signs.
For any such \(T\) the leading coefficient in its Lagrange interpolation at these nodes is
\[
                \sum_{j=1}^n\frac{T(x_j)}
                                {\prod_{i\ne j}(x_j-x_i)}=0
\]
because \(\deg T\le n-2\).
All summands have the same weak sign, so \(T\) vanishes at the \(n\) nodes and is zero.
An unbounded sequence of feasible vectors, divided by their norms and passed to a convergent subsequence, would yield a nonzero such direction.
The feasible polyhedron is therefore bounded whenever nonempty.
Its defining coefficients are real algebraic numbers, so exact linear programming bounds each coefficient of \(H\), after which each integral vector in the resulting box can be tested against the original strict inequalities.
This gives a terminating decision procedure for the positive-residue-sum domain, taking \(h\) to be the smaller of a prescribed cap and \(n-2\) at each remaining conductor.

<a id="rational-witness"></a>
## A rational witness of degree four at arbitrarily large conductors

Take any allowed \(p\) coprime to \(s\).
Odd \(p\) excludes \(b_j=0\), and \(\sin(2\pi sj/p)=0\) would give \(p\mid2sj\), impossible for \(1\le j\le n\).
Thus the polynomial \(D=t^2E_{s-1}^2\) is strictly positive at every node.
At the final node, \(\sqrt{2+b_n}=2\sin(\pi/(2p))<\pi/p<1/s\), since \(p>4s+3\).
Also \(\sqrt{2+b_{n-1}}>\sqrt{2+b_n}\), so one can choose a rational \(k\) and set
\[
 \sqrt{2+b_n}<k<\min\{\sqrt{2+b_{n-1}},1/s\},
 \qquad H(t)=(-1)^n kD(t).
\]
The explicit choice \(k=4/p\) works throughout this range, because \(4/p<1/s\) and
\[
              \sqrt{2+b_{n-1}}=2\sin(3\pi/(2p))\ge 6/p>4/p
\]
by concavity of sine on \([0,\pi/2]\).
At every earlier node both \(\sqrt{2+b_j}+k\) and \(\sqrt{2+b_j}-k\) are positive.
At the last node the sign expression is \(D(b_n)(\sqrt{2+b_n}-k)<0\).
Thus \(c=n-1\) gives all the required signs.
Using \(E_{s-1}(-2)=(-1)^{s-1}s\), \(B_m(-2)=(-1)^m\) and \(n=m+s\), the endpoint is
\[
                           \frac{Q(-2)}{B_n(-2)}
                              =-4s+4s^2 k<0.
\]
For \(s=2\), \(D=t^4\), and every odd \(p\ge13\) is allowed and coprime to \(s\).
The rational quartics \(H=(-1)^n(4/p)t^4\) therefore satisfy the same strict signs and endpoint for unbounded \(p\), while \(t^3\) divides the corresponding traces \(Q=t^3B_m+H\).

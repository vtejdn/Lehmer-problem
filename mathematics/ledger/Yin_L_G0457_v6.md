---
author: Yin
---

# A degree obstruction for central perturbations of squarefree cyclotomic parents

The [previous construction](Yin_L_G0457_v4.md#integer-family) gives a long initial coefficient agreement with a neutral rational function.
The [fixed-parent exclusion](Yin_L_G0457_v5.md#endpoint-repair-test) found two intervals of opposite phase for one endpoint-compatible parent.
On 2026-11-16T07:34 the construction and strategy collaborators for Yin obtained such intervals for every squarefree parent in that coefficient profile and used them to bound the degree required of a central perturbation.

<a id="degree-obstruction"></a>
## Grid and perturbation degree

Let \(A\) be a squarefree product of cyclotomic polynomials of orders \(q\ge3\), of degree \(2d\) with \(d\ge2\), and suppose
\[
A(z)=1+3z^2+O(z^4).
\]
Write \(A(z)=z^d C_A(z+z^{-1})\) and \(S=2(d-1)\).
For odd \(r>2d+1\), put \(m=(r-1)/2\), \(N=m+d\), \(n=N-1\) and \(p=2n+1=r+S\).
Let \(B_k(2\cos\theta)=\sin((2k+1)\theta/2)/\sin(\theta/2)\), and let \(H\) be any real polynomial of degree at most \(h\), where \(h\ge0\) is an integer and \(H=0\) is allowed.
Consider
\[
 Q_H(t)=C_A(t)B_m(t)+H(t),\qquad b_j=2\cos(2\pi j/p),\qquad
 \rho_j=Q_H(b_j)/B_n'(b_j),\quad 1\le j\le n.
\]
Put \(D=\max(\{S\}\cup\{q:\Phi_q\mid A\})\).
For a strict terminal cut there must be an integer \(1\le s<n\) with \(\rho_j>0\) for \(j\le s\) and \(\rho_j<0\) for \(j>s\).
Every such cut requires
\[
                        p\le (h+2) S D.                    \tag{1}
\]
This condition applies before imposing any endpoint inequality.
For the central subtraction \(H=-1\), it gives \(p\le 4(d-1)D\), and in particular \(p\le 2D^2\).

<a id="two-phase-intervals"></a>
## Two intervals of opposite phase

In the angle coordinate \(0<u<1/2\), put
\[
 W(u)=C_A(2\cos(2\pi u))\frac{\sin(2\pi(d-1)u)}{\sin(\pi u)}.
\]
The phase can vanish at a reduced primitive fraction \(a/q\) of a parent order, or at \(u=k/S\) for \(1\le k\le d-2\).
The first factor has simple zeros because all parent roots are simple and \(u\mapsto 2\cos(2\pi u)\) is strictly decreasing with nonzero derivative in the open interval.

At least one of the interior sine zeros is not a parent zero.
Indeed, \(d=2\) cannot occur, since reciprocity would give \(A(z)=1+3z^2+z^4\), whose two roots in \(z^2\) are real negative reciprocals of distinct absolute values.
For \(d\ge3\), if every interior sine zero were a parent zero, complex conjugation would imply that \(A\) vanishes on every \(S\)-th root of unity except \(1,-1\).
Then
\[
 F(z)=\frac{z^S-1}{z^2-1}=1+z^2+\cdots+z^{S-2}
\]
divides \(A\).
The quotient is a monic reciprocal quartic with constant coefficient one.
Its linear coefficient is zero and its quadratic coefficient is two by the displayed coefficients of \(F\) and \(A\).
Thus \(A/F=(1+z^2)^2\), contradicting squarefreeness.

At such an unmatched \(k/S\), the phase has a simple zero and changes sign.
Let \(I\) be the open interval on its negative side up to the nearest other phase zero or endpoint.
All the breakpoints, including \(0,1/2\), are rational of reduced denominator at most \(D\).
The difference of two distinct reduced fractions of denominators \(a,b\) has magnitude at least \(1/(ab)\).
Since \(k/S\) has denominator at most \(S\), it follows that \(|I|\ge1/(SD)\).

Let \(J\) be the final open interval between the last phase zero and \(1/2\).
All \(d\) trace roots of the monic \(C_A\) lie in \((-2,2)\), so \(C_A\) has sign \((-1)^d\) near \(-2\).
The sine in the numerator also has sign \((-1)^d\) as \(u\) approaches \(1/2\) from below.
Hence \(W>0\) on \(J\), which follows \(I\), and \(|J|\ge1/(2D)\).

<a id="alternation"></a>
## Alternation forced on the perturbation

The [grid derivative and phase identity](Yin_L_G0457_v4.md#residue-formula) give, for \(\theta_j=2\pi j/p\),
\[
 \rho_j=\frac{4\sin\theta_j\sin(\theta_j/2)}p
        \left(W(j/p)+(-1)^{j+1}H(b_j)\right).
\]
The prefactor is positive.
Suppose \(I\) contains \(M\ge h+2\) consecutive grid nodes and every corresponding residue is nonnegative.
At these nodes \((-1)^{j+1}H(b_j)\ge -W(j/p)>0\).
Thus \(H\) takes strictly alternating signs on \(M\) consecutive, strictly decreasing trace values.
It has a distinct real zero in each of the \(M-1>h\) gaps, which is impossible for a nonzero polynomial of degree at most \(h\).
The strict inequality already excludes \(H=0\).
There is consequently a negative residue in \(I\).
On \(J\), if every residue on \(M\ge h+2\) consecutive nodes were nonpositive, then \((-1)^{j+1}H(b_j)\le -W(j/p)<0\), giving the same contradiction.
There is then a later positive residue, excluding every strict terminal cut.

Writing \(M_U=\#\{j:1\le j\le n,\ j/p\in U\}\), the more precise necessary condition is
\[
                      h\ge\min(M_I,M_J)-1.                  \tag{2}
\]
An open interval of length greater than \((h+2)/p\) in \((0,1/2)\) contains at least \(h+2\) consecutive grid nodes.
If \(p>(h+2)SD\), both intervals have this length, by \(S\ge2\) and the bounds just proved.
This proves (1), without bounds on the coefficients or number of terms of \(H\).

<a id="construction-return"></a>
## Consequences for the integer construction

There is an elementary bound in terms of the parent degree alone.
For each order \(q\) with \(\Phi_q\mid A\), the degree of that factor satisfies \(\varphi(q)\le2d\).
Writing \(\ell^e\parallel q\) for the exact prime powers,
\[
 \frac{\varphi(q)^2}{q}=\prod_{\ell^e\parallel q}\ell^{e-2}(\ell-1)^2\ge\frac12,
\]
since only the prime power \(2^1\) contributes a factor less than one.
Thus \(q\le8d^2\).
If \(q\) has \(k\) distinct prime factors, the \(i\)-th in increasing order is at least \(i+1\), so
\[
 \frac{q}{\varphi(q)}
 \le\prod_{i=1}^{k}\frac{i+1}{i}=k+1\le1+\log_2 q .
\]
It follows that \(D\le2d(1+\log_2(8d^2))\), and hence every admissible central subtraction satisfies \(p\le 8d(d-1)(1+\log_2(8d^2))\).

When \(H\) is integral and \(h\le n-2\), the trace perturbation preserves the \(tB_n+C\) form with integral \(C\) of degree \(n-1\) and leading coefficient two from the [squarefree-parent calculation](Yin_L_G0457_v4.md#integer-family).
Its reciprocal lift is
\[
 P_H(z)= A(z)\frac{1-z^r}{1-z}+z^N H(z+z^{-1}).
\]
Since \(N<r\), this agrees with \(A(z)/(1-z)\) through coefficient index \(N-h-1\).
For fixed \(A\), (1) excludes every sequence of such perturbations with \(p\to\infty\) and \(h=o(p)\) from the required sign chamber, including sequences with unbounded coefficients and unbounded numbers of terms.
The [fixed-support obstruction](Yin_L_G0464_v19.md#fixed-number-of-terms) concerns a different perturbation family and controls its complete measure for a fixed number of terms.
Here the conclusion is the failure of the sign condition in this squarefree-parent family.
Moving parents with \(p\le(h+2)SD\) and fixed parents with sufficiently large perturbation degree remain possible on this test.
Producing integer inputs with all the signs, the endpoint and an adequate long prefix for the [conditional positive-to-one argument](../claims/Yin_C_G0881_v10.md#statement) remains open.

---
author: Yin
---

# Review of the moving rational cut and its degree obstruction

<a id="rational-family-review"></a>
## Independent finding on the original lift

At 2026-11-08T03:11 UTC a separately assigned AI reviewer for Yin checked all three sections of [L464 v4](../../ledger/Yin_L_G0464_v4.md#moving-rational-family) and the matching and Newton-sum argument it uses from [L462 v2](../../ledger/Yin_L_G0462_v2.md#central-sign-test).
The reviewer had no role in developing this argument and received no proof-generation dialogue, author explanation or previous verdict on v4.
The independent derivation verifies the exact count of crossed poles, the variation asymptotic, the whole measure of the constructed lifts and the uniform degree obstruction under the stated hypotheses.

### The moving cut and the full measure

Differentiating the sine formula at the poles gives \(D(b_j)/B'(b_j)=w_j\), and the first three moments of these weights are \(1,0,1\) for \(d\ge3\).
For \(d=4\lfloor\pi m^2\rfloor+1\), the angle \(\theta_c\) has \(d\theta_c/\pi=d/2-2m+O(m^{-1})\).
The half-integer \(d/2\) therefore gives exactly \(2m\) nodes in \((0,1/m)\) for all sufficiently large \(m\).
The same phase gives \(B(c)\to1\) and \(G(c)=O(m^{-1})\).
Dividing each monomial difference by \(mt-1\) gives the integral geometric sum in v4, so the displayed \(h\) has integral coefficients even though \(s=u/m\) need not be integral.
For its residues the moment identities give \(\sum (b_j-c)r_j=5s\), \(K/s=4+c-(2+c)^2G(c)\) and \(Q(-2)/B(-2)=-2-s[1-(2+c)G(c)]<0\) eventually.

Writing \(A=\sin\theta_c(2+c)^2\), the summand of \(V/s\) before the grid average is \(A/|\theta-\theta_c|+O(1)\) uniformly on \([0,\pi]\) away from the singular point.
Taylor expansion gives the uniform remainder near the cut because \(\sin\theta_c\) stays bounded below, and the denominator stays separated from zero outside a fixed neighborhood.
For large \(m\) the cut lies in the middle third of the angular range, at least a third of a grid step from each pole.
The two harmonic sums therefore give \(V/s=(2A/\pi)\log d+O(1)\sim(8/\pi)\log d\).

The two nonempty sign blocks give \(d-3\) same-sign gaps, and the left endpoint gives a further disjoint zero interval.
On a fixed circle of radius less than \(1/2\) about either \(i\) or \(-i\), subtracting \(v+1/v\) from \(Q(\sqrt K\,v)/(\sqrt K\,B(\sqrt K\,v))\) costs \(O(V/K^{3/2})=o(1)\).
This follows termwise from \(|b_j|\le2\), since \(|v|\ge1/2\) and \(K\sim4s\to\infty\).
Rouché's theorem gives exactly one zero in each disk, leaving precisely the \(d-2\) interior real traces already counted.
The upper trace \(x\) satisfies \(x/\sqrt K\to i\), and its exterior lift \(\lambda\) satisfies \(\lambda=x-\lambda^{-1}\sim x\).
Only \(\lambda\) and its conjugate contribute to the full measure, giving the exact equality \(M(P)=|\lambda|^2\) and the asymptotic \(M(P)\sim K\sim4m^{d-2}\).

### Uniformity and the smallest scalar

For reduced \(c=p/q\in(-2,2)\) with \(q\ge2\), evaluation at \(c\) has kernel \((qt-p)\) by primitivity and image \(\mathbb Z[1/q]\) by Bézout.
With \(n=d-1\), the integer \(u=q^nB(c)\) is prime to \(q\) and nonzero, so the additional quotient by \(B\) is \(\mathbb Z/|u|\mathbb Z\).
For \(k=\deg W\) and \(g=q^kW(c)\ne0\), the congruence is thus soluble precisely when \(u\mid Ng\), giving the stated least positive scalar for the congruence itself.
For example, \(d=5,c=1/2,W=(2+t)^2\) gives \(u=5,g=25\), and \((2t-1)(-10t^3-5t^2+28t+16)=W-20B\) realizes the least scalar \(1\).

For \(W(b_j)>0\), \(N>0\), both sign blocks nonempty and \(Q(-2)/B(-2)<0\), the disjoint interval matching leaves one pole and two trace roots.
Each remaining trace has modulus at most \(M+1\) for \(M=M(P)\ge1\), whether it is real or nonreal.
The matched contributions to the \(h\)-th power-sum difference are bounded by the variation \(2^{h+1}\) of \(t^h\) on \([-2,2]\) for \(h=1,2,3\).
Including the unmatched pole gives \(|\Delta_h|\le5\cdot2^hM^h\).
Expanding \(\log(Q/(tB))\) to order three then gives \(|a|\le10M\), \(|K|\le60M^2\) and \(|J|\le947M^3\) for \(J=\sum b_jr_j\).
In particular \(0<T=J-cK\le1067M^3\).

For \(0\le k\le d-2\), the coefficients of \(\widetilde W=(N/q)W\) in the discrete orthonormal basis \(E_\ell=U_\ell(t/2)\) satisfy \(|A_\ell|\le(\ell+1)T\) by positivity at all nodes.
The divided-difference functional has \(L_c(E_0)=0\) and \(L_c(E_\ell)=E_{\ell-1}(c)\) for \(1\le\ell\le k\), by the Chebyshev recurrence and orthogonality to \(E_0\).
Consequently both \(|\widetilde W(c)|\) and \(|L_c(\widetilde W)|\) are at most \((k+1)^3T\), and \(\widetilde W(c)G(c)=L_c(\widetilde W)-K\).
The nonzero integer \(Ng/u\) gives \(q^{n-k-1}|B(c)|\le|\widetilde W(c)|\) and the corresponding bound for \(D(c)=B(c)G(c)\).
Since \(1=B(c)^2+D(c)^2-cB(c)D(c)\le(|B(c)|+|D(c)|)^2\), these bounds give
\[
 q^{d-k-2}\le 2(k+1)^3T+|K|\le2200(k+1)^3M(P)^3.
\]
This constant is uniform in the cut's distance from every pole, the numerator coefficients and the integer shift \(a\).
Taking logarithms gives the claimed degree deficit for bounded \(M(P)\), including a bounded deficit when \(q\ge d^\varepsilon\) for fixed \(\varepsilon>0\).
The argument requires \(W(c)\ne0\).
When \(W(c)=0\), primitivity already gives \(qt-p\mid W\).
The bound leaves open whether numerators in its allowed degree range can give a moving cut, growing variation and one nonreal trace pair in a fixed exterior ellipse on the same lift.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Rational-family finding](#rational-family-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Rational-family finding](#rational-family-review) | [Integral family](../../ledger/Yin_L_G0464_v4.md#moving-rational-family) | Grid placement, integrality, residue signs, moments and endpoint. |
| [Rational-family finding](#rational-family-review) | [Variation and whole measure](../../ledger/Yin_L_G0464_v4.md#variation-and-whole-measure) | Uniform variation asymptotic, all trace roots and cost of both exterior lifts. |
| [Rational-family finding](#rational-family-review) | [Degree obstruction](../../ledger/Yin_L_G0464_v4.md#numerator-degree-obstruction) | Least scalar for the congruence, uniform bound and its degree consequences under the stated assumptions. |
| [Rational-family finding](#rational-family-review) | [Matching and Newton sums](../../ledger/Yin_L_G0462_v2.md#central-sign-test) | Disjoint matching and first three power-sum identities used in the general bound. |

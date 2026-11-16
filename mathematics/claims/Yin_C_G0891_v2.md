---
author: Yin
---

# Sublinear bounds on the integer matching prefix for exceptional parents

<a id="prefix-bound"></a>
## The permitted length of the prefix

Take \(s\ge2\), odd \(p=2n+1>4s+3\), \(r=p-2s\), \(m=(r-1)/2\), \(\theta_j=2\pi j/p\), \(b_j=2\cos\theta_j\) for \(1\le j\le n\), and
\[
 F_s(z)=(1+z^2)^2(1-z^{2s})/(1-z^2),\qquad Q_0(t)=t^2E_{s-1}(t)B_m(t).
\]
Here \(E_{s-1}(2\cos\theta)=\sin(s\theta)/\sin\theta\) and \(B_k(2\cos\theta)=\sin((2k+1)\theta/2)/\sin(\theta/2)\).
For a nonzero integral polynomial \(H\) set \(Q=Q_0+H\), \(L=n-\deg H\), and assume \(L\ge4\).
Suppose the residues \(\rho_j=Q(b_j)/B_n'(b_j)\) are strictly positive for \(j\le c\) and strictly negative for \(j>c\), for some \(1\le c<n\), and \(Q(-2)/B_n(-2)<0\).
Then for all \(s\),
\[
 L<3+6(8C_2p^2)^{1/3},\qquad C_2=2\pi^2/3.                     \tag{1}
\]
For even \(s\) there is the additional bound
\[
 L<3+6(2C_4s^2p^2)^{1/5},\qquad C_4=6\pi^4/5.                \tag{2}
\]
The reciprocal lift agrees with \(F_s/(1-z)\) through coefficient \(L\), and the next coefficient differs by the leading coefficient of \(H\), since \(r>n+1\).
Thus (1) requires \(\deg H\ge n-O(p^{2/3})\) uniformly over the whole exceptional family, and (2) gives \(\deg H\ge n-O_s(p^{2/5})\) for fixed even \(s\).
Zero perturbation has no negative residue in this family.
The [earlier local estimate](Yin_C_G0891_v1.md#statement) tests arbitrary phases on a middle arc and requires only a small fixed fraction of \(p\) as the perturbation degree.
Here the moment identities on the full grid also control degrees close to \(n\).
The main researcher and two research contributors derived the signed moment reduction and the prefix exponents for Yin's [unrestricted Task](../tasks/Yin_T_G0001_v1.md#contract).

<a id="moments"></a>
## A separator bounded away from the middle

Write \(\mu_j=Q_0(b_j)/B_n'(b_j)\), and choose \(b_{c+1}<a<b_c\).
The [exceptional phase and grid derivative](../ledger/Yin_L_G0457_v7.md#effective-cutoff) give
\[
 \mu_j=\frac4p b_j^2\sin^2(s\theta_j)\ge0.
\]
For a polynomial \(T\) of degree at most \(L-2\), one has
\[
 \sum_{j=1}^n(\rho_j-\mu_j)T(b_j)=0.
\]
Indeed \(HT\) has degree at most \(n-2\), so its coefficient of \(t^{n-1}\) in Lagrange interpolation on the roots of the monic \(B_n\) is zero.
The first three moments of \(\mu\) are
\[
 \sum\mu_j=2,\qquad \sum b_j\mu_j=0,\qquad
 d_2=\sum b_j^2\mu_j=6-\boldsymbol{1}_{s=2}.
\]
For the moment of order \(k=0,1,2\), include both conjugate halves of the \(p\)-grid and its zero-angle node, whose sine factor vanishes.
The desired moment is the full-grid average of \((2\cos\theta)^{k+2}(1-\cos(2s\theta))\).
All nonzero frequencies have absolute value at most \(2s+4<p\), hence average to zero.
The constant term is as displayed, since the outer coefficients of \((z+z^{-1})^4\) at degrees \(4,-4\) are both one.

Now \((b_j-a)\rho_j>0\) at every node.
Testing \((t-a)(2-t)\) in the moment identity gives
\[
 0<\sum (b_j-a)(2-b_j)\rho_j=-d_2-4a,\qquad a<-d_2/4\le-5/4 .
\]
Set \(G(t)=(t-a)H(t)\) and \(\lambda_j=G(b_j)/B_n'(b_j)\).
Then \(\lambda\) annihilates all polynomials of degree at most \(L-3\), and
\(\lambda_j=(b_j-a)(\rho_j-\mu_j)\ge-4\mu_j\).
Consequently for every polynomial \(D\) of degree at most \(L-3\) nonnegative on the grid,
\[
 \sum_j |\lambda_j|D(b_j)
   =2\sum_{\lambda_j<0}(-\lambda_j)D(b_j)
   \le 8\sum_j\mu_jD(b_j).                                    \tag{3}
\]

<a id="kernel"></a>
## Concentrating the moment test at trace zero

Put \(M=1+\lfloor(L-3)/6\rfloor\), \(u=\theta-\pi/2\), and take the continuous values in
\[
 D(2\cos\theta)=\left(\frac{\sin(Mu)}{M\sin u}\right)^6 .
\]
This is an even polynomial in \(t=2\cos\theta\) of degree at most \(6(M-1)\).
Indeed the sine quotient before taking the sixth power is a polynomial of definite parity in \(\cos u=\sin\theta\), and \(\sin^2\theta=1-t^2/4\).
It satisfies \(D(0)=1,\ D'(0)=0,\ 0\le D\le1\) on \([-2,2]\).
For \(k=2,4\) the full-grid mean of \(t^kD(t)\) equals its circle mean, because this trigonometric polynomial has degree at most \(L+1<p\).
Let \(v\in[0,\pi/2]\) be the angular distance to the nearest zero of \(\cos\theta\).
Then \(|t|=2\sin v\le2v\) and \(D\le\min(1,(\pi/(2Mv))^6)\), using \(\sin v\ge2v/\pi\).
Splitting the integral at \(\pi/(2M)\), and extending the upper bound on the second part to infinity, gives
\[
 \frac1{2\pi}\int_0^{2\pi} |2\cos\theta|^kD(2\cos\theta)\,d\theta
 \le \frac{\pi^k}{M^{k+1}}\left(\frac1{k+1}+\frac1{5-k}\right)
 = C_k/M^{k+1}.
\]
For all \(s\), \(\mu_j\le4b_j^2/p\).
For even \(s\), also \(|\sin(s\theta)|=|\sin(su)|\le s|\sin u|=s|t|/2\), giving \(\mu_j\le s^2 b_j^4/p\).
Extending the nonnegative half-grid sums to the full grid, (3) gives
\[
 A_D:=\sum|\lambda_j|D(b_j)\le32C_2/M^3,\qquad
 A_D\le8s^2 C_4/M^5\quad(s\ {\rm even}).                     \tag{4}
\]

<a id="integrality"></a>
## Two inverse moments and simple real roots

The odd grid avoids zero and \(\min_j|b_j|\ge2\sin(\pi/(2p))\ge2/p\).
Also \(|B_n(0)|=1\) by its sine formula at \(\pi/2\).
Use the partial fractions \(R(t)=G(t)/B_n(t)=\sum_j\lambda_j/(t-b_j)\), valid because \(\deg G<n\).
Both \((1-D(t))/t\) and \((1-D(t))/t^2\) are polynomials annihilated by \(\lambda\).
Thus
\[
 |R(0)|=\left|\sum \lambda_jD(b_j)/b_j\right|\le(p/2)A_D,
 \qquad |R'(0)|=\left|\sum \lambda_jD(b_j)/b_j^2\right|\le(p^2/4)A_D .
\]
If \(A_D<4/p^2\), then \(|aH(0)|=|R(0)|<2/p\), forcing the integer \(H(0)\) to vanish since \(|a|>1\).
Now also \(G(0)=0\) and \(|aH'(0)|=|R'(0)|<1\), so the integer \(H'(0)\) vanishes.
Both \(Q_0\) and \(H\) are divisible by \(t^2\).
The [trace division](../ledger/Yin_L_G0457_v7.md#effective-cutoff) gives \(Q=tB_n+C\) with integer \(C\) of degree \(n-1\) and leading coefficient two, since \(\deg H\le n-4\).
The [all-cut count](Yin_C_G0881_v10.md#nonreal-pair) then makes every real root of \(Q\) simple under the signs and endpoint.
The contradiction proves \(A_D\ge4/p^2\).
Combining this with (4) and \(L<6M+3\) proves (1) and (2).

## Assessment history

### Decision prefix-power-draft

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:35 |
| status | open |
| reason | Retain the uniform and even-parameter prefix estimates for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prefix bounds](#prefix-bound) | Matching lengths for integral perturbations for all exceptional parents and all cuts, with the endpoint. |
| argument | [Signed moments](#moments) | Separator location, matching degrees and total weighted variation. |
| argument | [Concentrated test](#kernel) | Exact grid averaging, continuous estimates and parity-dependent vanishing. |
| argument | [Integral conditions](#integrality) | Two inverse moments, integrality, real-root simplicity and final constants. |
| dependency | [Exceptional trace and grid](../ledger/Yin_L_G0457_v7.md#effective-cutoff) | Neutral phase weights and the integer remainder. |
| dependency | [All-cut multiplicities](Yin_C_G0881_v10.md#nonreal-pair) | Simplicity of all real trace roots under the endpoint and integer hypotheses. |


### Decision sublinear-prefix-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:48 |
| status | proved |
| reason | Adopt the uniform and even-parameter prefix bounds after independent inspection of the signed moments, concentration and integral root count. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prefix bounds](#prefix-bound) | Matching lengths for integral perturbations for all exceptional parents and all cuts, with the endpoint. |
| argument | [Signed moments](#moments) | Separator location, matching degrees and total weighted variation. |
| argument | [Concentrated test](#kernel) | Exact grid averaging, continuous estimates and parity-dependent vanishing. |
| argument | [Integral conditions](#integrality) | Two inverse moments, integrality, real-root simplicity and final constants. |
| dependency | [Exceptional trace and grid](../ledger/Yin_L_G0457_v7.md#effective-cutoff) | Neutral phase weights and the integer remainder. |
| dependency | [All-cut multiplicities](Yin_C_G0881_v10.md#nonreal-pair) | Simplicity of all real trace roots under the endpoint and integer hypotheses. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v51.md#prefix-power-review) | Complete matching-length bounds, including the endpoint hypothesis, constants and all moment and root-count interfaces. |

## Current assessment
[Selected decision](#decision-sublinear-prefix-reviewed)

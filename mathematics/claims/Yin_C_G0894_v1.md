---
author: Yin
---

# Both coefficient parities are necessary in a shrinking odd-grid sequence

<a id="statement"></a>
## Weighted variation in each parity

Use the [full odd-grid chamber](../ledger/Yin_L_G0464_v5.md#odd-grid-product), with \(p=2n+1\), \(b_j=2\cos(2\pi j/p)\), and \(1\le j\le n\).
The integral lift \(P=z^{n+1}Q(z+z^{-1})\) has residues \(\rho_j=Q(b_j)/B_n'(b_j)\) positive through \(c\), negative thereafter, and \(Q(-2)/B_n(-2)<0\).
In the [integral trace coordinates](Yin_C_G0881_v3.md#prefix-coordinates) write
\[
 Z(t)=(4-t^2)h(t),\qquad Z(b_j)=p\rho_j,\qquad h=\sum_{i=0}^{n-1}a_i E_i,\qquad a_i\in\mathbb Z .
\]
Decompose \(Z=Z_e+Z_o\) into its even and odd parts in \(t\).
The parity of \(E_i\) is the parity of \(i\), so this is the same split as the even and odd coefficients \(a_i\).
For every sequence \(p\to\infty,\ 1<M(P)\to1\) in this chamber, and every fixed \(0\ne A\in\mathbb Z[t]\),
\[
 \frac1n\sum_{j=1}^n |A(b_j) Z_e(b_j)|\ \longrightarrow\ \infty,
 \qquad
 \frac1n\sum_{j=1}^n |A(b_j) Z_o(b_j)|\ \longrightarrow\ \infty.       \tag{1}
\]
In particular a uniform positive Mahler gap holds in this chamber when either one of these means is bounded by a fixed constant for a fixed \(A\).
This applies to every even \(h\), allowing arbitrary degrees and coefficient heights.
The [conductor-55 integer example](../computations/programs/Yin_J_G0155/versions/v3/readme.md#first-conductor) has all odd coordinates zero.

<a id="separator"></a>
## Resolving the negative block on the doubled angles

Write \(\kappa=n-c\), \(a=-2\cos(2\pi\kappa/p)\), and \(\mathbb E_p\) for the uniform mean on the \(n\) traces.
The [cut and block estimates](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) give \(\kappa\to\infty\) and \(\kappa/p\to0\).
The nonnegative masses \(X_j=(b_j-a)Z(b_j)\) have bounded mean, for example by the [first two residue moments](Yin_C_G0880_v2.md#moving-cut).
Thus \(\mathbb E_p[{\bf1}_{b_j\ge-1}|Z(b_j)|]\) is bounded since \(a\to-2\) and \(Z>0\) there eventually.

For a negative trace \(b_j\) put \(\phi_j=2\pi(p-2j)/p\in(0,\pi)\), so \(2\cos\phi_j=b_j^2-2\).
The sign of \(Z(b_j)\) is negative when \(p-2j\le2\kappa-1\) and positive when \(p-2j\ge2\kappa+1\).
Write \(\alpha=4\pi\kappa/p,\ \delta=2\pi/p,\ m=\lfloor p/8\rfloor\).
Every such \(\phi_j\) is either at most \(\alpha-\delta\) or at least \(\alpha+\delta\).
We construct a real polynomial \(W_p\) of degree at most \(m-1\) and an absolute \(\gamma>0\) such that eventually
\[
  \sup_{[-2,2]}|W_p|\le1,\qquad
  W_p(b_j^2-2)\,Z(b_j)\ge\gamma|Z(b_j)|\quad (b_j<0).                 \tag{2}
\]

Use the even \(2\pi\)-periodic Fejér kernel
\[
 K_m(v)=\frac1{2\pi m}\left(\frac{\sin(mv/2)}{\sin(v/2)}\right)^2 .
\]
It has integral one over the circle and frequencies through \(m-1\), by expansion as the squared modulus of a geometric sum.
Define \(W_p(2\cos\phi)=1-2\int_{\phi-\alpha}^{\phi+\alpha}K_m(v)\,dv\).
The convolution is even with frequencies through \(m-1\), hence defines a polynomial of the required degree and takes values in \([-1,1]\) after the indicated rescaling.
Put \(I=\int_0^\delta K_m\), \(J=\int_\alpha^\pi K_m\).
On \(0\le v\le\delta\), \(mv/2\le\pi/8\), so \(\sin(mv/2)/\sin(v/2)\ge 2m/\pi\).
It follows that \(I\ge4m/(\pi^2p)\).
Using \(\sin(v/2)\ge v/\pi\) gives \(J\le\pi/(2m\alpha)\to0\).
In particular \(2(I-J)\) is eventually bounded below by a fixed \(\gamma>0\).

If \(0\le\phi\le\alpha-\delta\), the integration interval contains \([-\delta,\alpha]\), with mass \(1/2+I-J\).
If \(\alpha+\delta\le\phi\le\pi\), its part below \(\pi\) lies in \([\delta,\pi]\) and has mass at most \(1/2-I\).
The part above \(\pi\) has mass at most \(J\) by reflection, since \(\alpha\le\pi/2\) eventually.
These two bounds prove the sign and margin in (2).

<a id="parity"></a>
## Exact odd moments and the two variations

Let \(D\in\mathbb R[t]\) be any fixed even polynomial nonnegative on the trace interval and set \(W=W_p(t^2-2)\).
For all sufficiently large \(p\) one has the two exact cancellations
\[
                    \mathbb E_p[b_j W(b_j)D(b_j)Z_e(b_j)]=0,
        \qquad      \mathbb E_p[W(b_j)D(b_j)Z_o(b_j)]=0.              \tag{3}
\]
Both integrands are odd trace polynomials of degree at most \(n+2+2(m-1)+\deg D<p\).
At \(t=z+z^{-1}\) their Laurent expansions have only odd exponents of absolute value less than \(p\), hence their complete \(p\)-point means vanish.
Their value at \(t=2\) is zero because both parity parts of \(Z\) contain \(4-t^2\).
Pairing opposite angles gives (3) on the half grid.

Write \(V_D=\mathbb E_p|DZ|\), with polynomials now evaluated at \(b_j\).
The contribution to \(V_D\) from \(b_j\ge-1\) is \(O_D(1)\) by the bounded positive mass.
On \(b_j<0\), (2) gives \(WDZ\ge\gamma |DZ|\).
Separating the positive and negative trace ranges in the second identity of (3) yields
\[
 \gamma\,\mathbb E_p[{\bf1}_{b_j<0}|DZ|]
   \le |\mathbb E_p WDZ|+\mathbb E_p[{\bf1}_{b_j\ge0}|DZ|]
   \le \mathbb E_p|DZ_e|+O_D(1).
\]
For the other parity, \(b_j WDZ\) is nonpositive on \(b_j<0\), and its negative there dominates \(\gamma |DZ|\) on \(b_j\le-1\).
By the first identity in (3),
\[
 \gamma\,\mathbb E_p[{\bf1}_{b_j\le-1}|DZ|]
    \le |\mathbb E_p[b_j WDZ]|+2\mathbb E_p[{\bf1}_{b_j\ge0}|DZ|]
    \le 2\mathbb E_p|DZ_o|+O_D(1).
\]
Thus both parity means control \(V_D\), with constants independent of the coefficients of \(h\).

For the given \(A\) take \(D(t)=(A(t)A(-t))^2\).
The [fixed integral weight gap](Yin_C_G0880_v2.md#statement) implies \(V_D=(p/n)\sum_j |D(b_j)\rho_j|\to\infty\).
Since \(0\le D(t)\le C_A|A(t)|\) on \([-2,2]\), the two estimates imply (1).
A hypothetical failure of a uniform positive gap under a bound on either mean selects a sequence of positive measures tending to one.
Its degrees must be unbounded since a bound on degree and Mahler measure bounds all integral coefficients by expansion in the roots.
Passing to increasing conductors gives the contradiction with (1).

## Assessment history

### Decision parity-variation

| Field | Value |
| --- | --- |
| date | 2026-11-16T09:23 |
| status | open |
| reason | Record the parity obstruction suggested by the even conductor-55 example for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Both parity variations](#statement) | Divergence under every fixed integer weight and the resulting uniform gaps. |
| argument | [Doubled angles](#separator) | Frequencies and uniform sign margin on the negative trace half of the grid. |
| argument | [Odd grid identities](#parity) | Degree allowance, exact cancellations, both variation estimates and the weight transfer. |
| dependency | [Terminal block](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Shrinking normalized block and divergent number of negative nodes. |
| dependency | [Weighted variation gap](Yin_C_G0880_v2.md#statement) | Divergence of the total variation after a fixed even nonnegative weight. |


### Decision parity-variation-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T09:28 |
| status | proved |
| reason | Adopt the weighted variation obstruction for each parity and the resulting uniform gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Both parity variations](#statement) | Divergence under every fixed integer weight and the resulting uniform gaps. |
| argument | [Doubled angles](#separator) | Frequencies and uniform sign margin on the negative trace half of the grid. |
| argument | [Odd grid identities](#parity) | Degree allowance, exact cancellations, both variation estimates and the weight transfer. |
| dependency | [Terminal block](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Shrinking normalized block and divergent number of negative nodes. |
| dependency | [Weighted variation gap](Yin_C_G0880_v2.md#statement) | Divergence of the total variation after a fixed even nonnegative weight. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v60.md#parity-variation-review) | Independent check of the chamber, sign margin after angle doubling, exact cancellations, both parity estimates and uniform conclusion. |

## Current assessment
[Selected decision](#decision-parity-variation-reviewed)

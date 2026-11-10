---
author: Yin
---

# A single terminal negative residue forces a noncyclotomic endpoint root

<a id="statement"></a>
## Scope and statements

Retain the [v7 kernel and integer-branch results](Yin_C_G0881_v7.md#statement) at their stated scopes.
Use the [original odd-grid construction](Yin_C_G0881_v3.md#original-domain) with
\[
p=2n+1\ge5,\qquad x=0,\qquad a_0=2,\qquad \kappa=1.
\]
Thus \(Q=tB_n+C\), \(C=B_{n-1}h\bmod B_n\), \(h=\sum_{i=0}^{n-1}a_iE_i\), and \(P(z)=z^{n+1}Q(z+z^{-1})\).
Assume the original strict residue signs and endpoint:
\[
r_j>0\quad(1\le j<n),\qquad r_n<0,\qquad
\frac{Q(-2)}{B_n(-2)}<0.
\]
There is no primality, irreducibility or coefficient-height assumption.

For real coefficients, \(Q\) has no real root above \(b_1=2\cos(2\pi/p)>0\), and has a real root in \((-2,b_n)\).
If every \(a_i\) is an integer, no root of \(Q\) in that endpoint interval is the trace of a root of unity.
Consequently the complete integer polynomial satisfies \(M(P)>1\), and its cyclotomic factors can have orders only in \(3\le m<p\).
Every such integer input has exactly two roots of \(P\) outside the unit circle and exactly two inside, counted with multiplicity.
Equivalently, it has exactly four roots off the unit circle.
Those four roots are nonreal, and the two exterior roots form a complex conjugate pair.

With the zero-profile prefix through length \(2\le L\le n+1\), the complete bound is therefore
\[
1<M(P)\le
\bigl(8\lfloor L/2\rfloor+8\bigr)^{2/\lfloor L/2\rfloor}.
\]
At length 140 this is \(1<M(P)\le568^{1/35}<6/5\).
For a sequence of such integer inputs with \(L\to\infty\), no separate noncyclotomic hypothesis is needed to obtain \(0<\log M(P)=O(\log L/L)\to0\).
The existence of those integer inputs is not asserted.

Finally, let \(F\in\mathbb Z[z]\) be a monic reciprocal Salem polynomial: its only roots off the unit circle are a simple positive real pair \(\lambda,\lambda^{-1}\), with \(\lambda>1\).
For any integer \(k\ge1\), sign \(\varepsilon\in\{1,-1\}\), and product \(H\) of cyclotomic polynomials, no polynomial
\[
H(z)F(\varepsilon z^k)
\]
is an input in the integer domain above.
This excludes that single-seed source at every substitution degree and with arbitrary cyclotomic multiplicities; it makes no assertion about arbitrary other noncyclotomic factors or several unrelated seeds.

<a id="argument"></a>
## Inputs and proof boundary

The original lift, residue formula and interval-root count are those of [C881 v3](Yin_C_G0881_v3.md#original-domain).
Its [prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) and [whole-measure bound](Yin_C_G0881_v3.md#whole-measure-upper) supply the conditional shrinking upper bound without a new root approximation.
The new argument below removes the independent nonneutrality premise in precisely the stated single-negative-node zero-profile domain.
The main researcher and a strategy collaborator developed it; no independent-review relationship is claimed for that development.

The cyclotomic irreducibility and full primitive-root description are accepted standard inputs inspected in [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001), Bell's 2017 notes, pages 3 and 6--7.
Only those statements are used, not the integer-ring or discriminant assertions.
The measure-one characterization is the product-with-multiplicities form retained in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), printed page 322.
The original proofs of these accepted standard inputs are not newly audited here.

<a id="endpoint-nontorsion"></a>
## No upper root and no torsion endpoint root

The exact partial fractions are
\[
\frac{Q(t)}{B_n(t)}=t+\sum_{j=1}^n\frac{r_j}{t-b_j}.
\]
The coefficient identity \(C=\sum_i a_iB_{n-i-1}\) gives leading coefficient \(a_0\) in degree \(n-1\).
Comparing coefficients of \(t^{-1}\) at infinity consequently gives \(\sum_jr_j=a_0=2\).
For \(t>b_1>0\), eliminating \(r_n\) now gives
\[
\frac{Q(t)}{B_n(t)}
=t+\frac2{t-b_n}
 +\sum_{j<n}r_j
 \left(\frac1{t-b_j}-\frac1{t-b_n}\right)>0.
\]
Every displayed denominator is positive, and each bracket is strictly positive because \(b_j>b_n\).
Since \(B_n\) has no zero above \(b_1\), neither does \(Q\).

On \((-2,b_n)\), the same ratio is continuous, negative at \(-2\), and tends to positive infinity as \(t\to b_n^-\), because \(r_n<0\).
It therefore has a zero \(u\) in that interval.
Suppose any such zero has a root-of-unity lift of exact order \(m\).
After replacing that root by its inverse if needed, write
\[
u=2\cos(2\pi k/m),\qquad 0<k<m/2,\qquad \gcd(k,m)=1.
\]
The identity \(b_n=-2\cos(\pi/p)\) and the strict position of \(u\) imply
\[
0<\pi-\frac{2\pi k}{m}<\frac\pi p,
\qquad 0<m-2k<\frac m p.
\]
The positive integer \(m-2k\) is at least one, so \(m>p\).

Now use integer coefficients: the lift \(P\) is monic in \(\mathbb Z[z]\), and the minimal polynomial \(\Phi_m\) of that primitive root divides \(P\).
Thus \(\exp(2\pi i/m)\) is also a root of \(P\), and its trace is a root of \(Q\).
But
\[
2\cos(2\pi/m)>2\cos(2\pi/p)=b_1,
\]
contradicting the upper-root exclusion.
Every endpoint-interval root is therefore nontorsion in the claimed sense.

The monic integer \(P\) has constant coefficient one.
If \(M(P)=1\), the accepted Kronecker characterization makes it a product of cyclotomic polynomials, so all its roots are roots of unity.
The endpoint root contradicts this, proving \(M(P)>1\).

A cyclotomic factor of order \(m>p\) is excluded by the same upper-root argument.
Order one gives the forbidden trace 2, and order two gives the forbidden endpoint \(-2\).
Order \(p\) gives a zero at the original pole \(b_1\), whereas \(Q(b_1)=r_1B_n'(b_1)\ne0\).
Hence every actual cyclotomic factor has \(3\le m<p\), including when \(p\) is composite.

<a id="complete-root-count"></a>
## Exactly two exterior roots

The original strict signs and endpoint supply \(n-1\) distinct selected trace roots in \((-2,2)\), one in each same-sign interval and one in \((-2,b_n)\).
After removing one copy of each, the remaining factor of \(Q\) is a real monic quadratic with roots \(v_1,v_2\), including multiplicity.
The selected roots lift only to the unit circle.

If the quadratic has nonreal conjugate roots, each reciprocal equation \(z^2-v_i z+1=0\) has exactly one root outside and one inside the unit circle.
Indeed a unit-circle root would give a real trace, and the product of each reciprocal pair is one.
This gives exactly two exterior and two interior roots.

If the remaining roots are real, the upper-root exclusion gives \(v_i\le b_1<2\).
Let \(A\) be the product of the \(n-1\) selected monic linear factors.
Since each selected root is greater than \(-2\), \(A(-2)\) has sign \((-1)^{n-1}\), while \(B_n(-2)=(-1)^n\).
The strict endpoint therefore implies
\[
(-2-v_1)(-2-v_2)>0.
\]
Both remaining roots lie below \(-2\), or both lie above \(-2\).
The latter option puts every trace root in \([-2,2]\), making \(M(P)=1\), which was excluded above.
Thus both roots lie below \(-2\), and each contributes exactly one exterior and one interior root to \(P\).
Repeated remaining roots and overlap with selected roots retain their original multiplicities throughout the argument.

<a id="nonreal-exterior-pair"></a>
## The real exceptional pair is impossible

The coefficient of degree \(n\) in \(Q=tB_n+C\) equals the coefficient of degree \(n-1\) in \(B_n\), because \(\deg C\le n-1\).
Hence the sum of all trace roots of \(Q\) equals the sum of the poles \(b_j\).
Match each selected root to the right pole of its interval as in [v3's paired variation argument](Yin_C_G0881_v3.md#paired-variation).
For \(\kappa=1\), these poles are \(b_1,\ldots,b_{n-2},b_n\), and the unpaired pole is \(b_{n-1}\).
Every selected root \(u\) is strictly less than its matched pole \(b\), so
\[
v_1+v_2=b_{n-1}+\sum_{\text{matched }(u,b)}(b-u)
        >b_{n-1}>-2.
\]
This contradicts \(v_1,v_2<-2\), which would give \(v_1+v_2<-4\).
Thus the residual quadratic has a nonreal conjugate pair.
Its reciprocal lifts are all nonreal, since every nonzero real lift has real trace.
Complex conjugation pairs the two exterior lifts, which have the same modulus \(\rho>1\), and the complete measure is \(M(P)=\rho^2\).

<a id="salem-seed-exclusion"></a>
## A single Salem seed and cyclotomic padding cannot supply this domain

The polynomial \(F(\varepsilon z^k)\) has exactly \(k\) exterior roots and \(k\) interior roots, because each of the two off-circle roots of \(F\) has exactly \(k\) distinct preimages of the corresponding modulus.
Cyclotomic multiplication changes neither count.
The exact count just proved forces \(k=2\).

For \(\varepsilon=1\), the positive exterior root \(\sqrt\lambda\) of \(F(z^2)\) gives a real trace greater than 2, contradicting the upper-root exclusion.
For \(\varepsilon=-1\), select the forced endpoint root \(u\in(-2,b_n)\) and one of its unit-circle lifts \(\zeta\).
This lift is not a root of unity, so it cannot be a zero of the cyclotomic factor \(H\).
It must be a zero of the even polynomial \(F(-z^2)\), which also vanishes at \(-\zeta\).
The latter trace is \(-u\), and
\[
-u>-b_n=2\cos(\pi/p)>2\cos(2\pi/p)=b_1.
\]
This again contradicts the upper-root exclusion.
No cancellation of roots or factors occurs, because the proposed source is the actual polynomial product.

<a id="construction-consequence"></a>
## What the result removes and what remains

The v3 upper bound combined with the new strict lower bound proves the length-dependent statement above for every actual integer input in this domain.
In particular, v7's four derivative branches cover every integer sign-and-endpoint input at conductor 2003 and length 140, without adding a separate \(M(P)>1\) hypothesis.
The conductor-1009 application and rational witnesses keep their own [J159 scope and evidence](../computations/programs/Yin_J_G0159/readme.md#p1009-branch).
The new theorem does not apply its integer conjugacy step to those nonintegral witnesses.

The remaining existence problem is simultaneous integer satisfaction of the original strict signs and endpoint with the required prefix.
A bounded candidate still requires exact input checks and a complete Mahler certificate before it can be reported as a new value.
The single-Salem-seed exclusion explains why recovery of the earlier known seeds under monomial substitution and cyclotomic padding does not establish supply for this cell.
No general integer source, admissible example, uniform positive gap or unrestricted G0001 resolution is obtained here.

## Current assessment

[Selected decision](#decision-endpoint-nontorsion-nonreal-pair)

## Assessment history

### Decision endpoint-nontorsion-nonreal-pair

| Field | Value |
| --- | --- |
| date | 2026-11-10T07:41 |
| status | proved |
| reason | Complete independent review verifies the integer endpoint-conjugacy argument, strict full measure, all cyclotomic orders, the exact nonreal exterior pair with multiplicities, every single-Salem-seed substitution and the complete prefix transfer. Integer supply remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statements](#statement) | Entire odd-conductor single-negative-node theorem, complete nonreal root count, single-Salem-seed exclusion and conditional prefix consequence. |
| argument | [Whole argument and inputs](#argument) | Complete fixed proof and accepted external-input limits. |
| argument | [Nontorsion endpoint](#endpoint-nontorsion) | Upper-root exclusion, every endpoint root, integer conjugacy and complete strict measure. |
| argument | [Complete root count](#complete-root-count) | Both remaining quadratic types and all original multiplicities. |
| argument | [Nonreal exterior pair](#nonreal-exterior-pair) | Exact first-moment matching and exclusion of the remaining real alternative. |
| argument | [Single seed exclusion](#salem-seed-exclusion) | Every substitution degree, both signs and arbitrary cyclotomic padding. |
| argument | [Construction consequences](#construction-consequence) | Prefix upper bound and precise unresolved integer-supply boundary. |
| dependency | [Retained v7 statement](Yin_C_G0881_v7.md#statement) | Earlier kernel and four-branch results at their unchanged scopes. |
| dependency | [Original domain](Yin_C_G0881_v3.md#original-domain) | Full reciprocal lift, residues, strict endpoint and required interval roots. |
| dependency | [Prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) | Complete integer basis and permitted coefficient prefix. |
| dependency | [Paired interval roots](Yin_C_G0881_v3.md#paired-variation) | Actual right-pole matching and unpaired pole. |
| dependency | [Complete upper bound](Yin_C_G0881_v3.md#whole-measure-upper) | All factors and multiplicities at every permitted prefix length. |
| dependency | [Cyclotomic statements](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | General irreducibility and primitive-root description, at the retained accepted statement depth. |
| dependency | [Kronecker precision](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Complete measure-one characterization in the height-normalization section, with products and multiplicities; no new original-proof audit. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v35.md#endpoint-nontorsion-nonreal-pair-review) | Entire final statement, proof, necessary inputs and construction limits. |

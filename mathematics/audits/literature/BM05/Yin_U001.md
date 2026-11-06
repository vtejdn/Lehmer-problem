---
author: Yin
---

# BM05: cyclotomic reciprocal quadratics and the L133 control family

<a id="bm05-u001"></a>
## Source and scope

The inspected edition and actual online access are identified in the [source notes](readme.md#yin-source-edition).
This unit compares source families with the [reciprocal three-block setting of L133 v3](../../../ledger/Yin_L_G0133_v3.md#three-block-integral).
It records source statements and elementary notation conversions, not an independent review of L133 or a full audit of BM05.

The directly inspected passages are §1, pp. 403–405, for normalization, substitutions and the limit-point qualification; §2, pp. 405–406, especially (2–1), (2–2), (2–4) and (2–5); §3, pp. 406–407, especially (3–1), (3–2) and the ensuing quadratic integral; §4.2–4.3, pp. 409–410, for the six-term comparison and bounded searches; and §6, pp. 411–412, for the proposed genuine-limit-point argument.
The numerical searches, their completeness within the stated boxes, and the paper's other explicit-value formulas were not independently reproduced or audited.
The local conversions below are checked directly.

Use normalized Haar measure on each torus and write \(m_k(H)=\int_{\mathbb T^k}\log|H|\), with \(M(H)=\exp(m_k(H))\).
This agrees with BM05 (1–1) and its logarithmic convention.
The subscript only displays the number of variables; it is not division by degree.
The cyclotomic-product hypotheses and the integrability of the present three-block logarithm are retained in [L133 v3](../../../ledger/Yin_L_G0133_v3.md#three-block-integral).

<a id="source-quadratic-families"></a>
## The source families and the common Jensen reduction

For positive integers \(a,b\), put \(h=\max(a-b,0)\) and \(\phi_a(X)=(X^a-1)/(X-1)\).
The source's §2 formulas are
\[
 P_{a,b}(X,W)
 =X^h\{\phi_a(X)+\phi_b(X)W+X^{b-a}\phi_a(X)W^2\},
 \tag{BM05 2–2}
\]
and
\[
 Q_{a,b}(X,W)
 =X^h\{1+X^a+(1+X^b)W+X^{b-a}(1+X^a)W^2\}.
 \tag{BM05 2–5}
\]
Its search representatives impose \(\gcd(a,b)=1\), and additionally \(a+b\) odd for \(Q\).
The displayed algebraic identities below do not need these restrictions.

For a polynomial \(H(X,W)=a_0(X)\prod_{j=1}^d(W-w_j(X))\), source (3–1) is
\[
 m_2(H)=m_1(a_0)+
 \sum_{j=1}^d\int_0^1\log^+|w_j(e^{2\pi it})|\,dt.
\]
For \(P_{a,b}\), source (3–2), after removal of a nonzero scalar factor at generic \(t\), is
\[
 e^{\pi i(b-a)t}\sin(a\pi t)W^2
 +\sin(b\pi t)W
 +e^{-\pi i(b-a)t}\sin(a\pi t)=0.
\]
Writing \(\zeta=e^{\pi i(b-a)t}W\) gives
\[
 \zeta^2+\frac{\sin(b\pi t)}{\sin(a\pi t)}\zeta+1=0.
\]
The coefficients of this last quadratic are real and its roots have product \(1\).
Consequently the contribution of the root outside the unit disk is
\[
 g(s)=
 \begin{cases}
 0,&|s|\leq2,\\
 \operatorname{arcosh}(|s|/2),&|s|>2,
 \end{cases}
 \qquad s=\frac{\sin(b\pi t)}{\sin(a\pi t)}.
\]
The finitely many zero denominators are handled by the logarithmic integral, not by assigning a finite value to the quotient there.
Since the leading coefficient is cyclotomic up to a monomial, \(m_1(a_0)=0\).
This is precisely the quadratic Jensen mechanism underlying the \(|B/A|>2\) integral in L133 v3.
The source uses it to locate integration intervals and evaluate measures numerically; quadratic Jensen reduction itself is therefore an established source mechanism.

<a id="finite-cover-and-exact-control"></a>
## Exact comparison with the local cyclotomic family

Let \(A_0,B_0\) be monic reciprocal cyclotomic products of even degrees \(2r,2s\) and constant term \(1\), and set
\[
 F_{A_0,B_0}(z,Y)
 =z^{-r}A_0(z)(Y+Y^{-1})-z^{-s}B_0(z).
\]
These are the local hypotheses; no assertion is made that BM05 explicitly treats every such pair.

Use the substitution
\[
 X=z^2,\qquad W=-z^{a-b}Y.
\]
For \(A_0(z)=\phi_a(z^2)\), \(B_0(z)=\phi_b(z^2)\), one has \(r=a-1\), \(s=b-1\), and direct expansion gives
\[
 P_{a,b}(z^2,-z^{a-b}Y)
 =z^{2h+a-1}Y F_{\phi_a(z^2),\phi_b(z^2)}(z,Y).
\]
For \(A_0(z)=1+z^{2a}\), \(B_0(z)=1+z^{2b}\), one has \(r=a\), \(s=b\), and
\[
 Q_{a,b}(z^2,-z^{a-b}Y)
 =z^{2h+a}Y F_{1+z^{2a},1+z^{2b}}(z,Y).
\]
In both cases the apparent three blocks become
\(A_0(z)(1+Y^2)-z^{a-b}B_0(z)Y\) before restoring the outside monomial.
The two displayed choices of \(A_0,B_0\) are indeed cyclotomic products with the stated even degrees and constant terms, including \(\phi_1=1\).

Here the map of tori has exponent matrix
\[
 \begin{pmatrix}2&0\\a-b&1\end{pmatrix},
 \qquad \det=2,
\]
followed by a translation by \((1,-1)\).
It is surjective: for any \((X,W)\in\mathbb T^2\), choose either square root \(z\) of \(X\), then put \(Y=-Wz^{b-a}\).
For completeness, a surjective continuous homomorphism of compact groups pushes normalized Haar measure to normalized Haar measure: the pushforward is a probability measure, and translation by any target element is induced by translation by one of its preimages, so the pushforward is translation-invariant.
The final sign translation also preserves Haar measure.
Thus substitution preserves the integral of the integrable logarithm; outside monomials have absolute value \(1\) and contribute zero.
In particular,
\[
 m_2(P_{a,b})=m_2(F_{\phi_a(z^2),\phi_b(z^2)}),\qquad
 m_2(Q_{a,b})=m_2(F_{1+z^{2a},1+z^{2b}}).
\]
Unimodularity is unnecessary: these substitutions are finite covers of degree \(2\), not invertible integer changes of variables.

The [coprime positive control in L133 v3](../../../ledger/Yin_L_G0133_v3.md#positive-controls) is
\[
 F_n(z,Y)
 =(z^{n+1}+z^{-(n+1)})(Y+Y^{-1})-(z^n+z^{-n}),
 \qquad n\geq1.
\]
Taking \(a=n+1\), \(b=n\), \(h=1\), gives the exact identity
\[
 Q_{n+1,n}(z^2,-zY)=z^{n+3}YF_n(z,Y),
 \qquad m_2(Q_{n+1,n})=m_2(F_n).
\]
Here \(\gcd(n+1,n)=1\) and \(a+b=2n+1\) is odd, so these parameters satisfy the source's representative restrictions.
This control family is therefore a source subfamily after an explicit measure-preserving cover, rather than a new cyclotomic quadratic family.

<a id="six-term-limit-comparison"></a>
## The source comparison for the control's positive limit

Source §4.2, printed p. 409, displays the six-term value
\[
 M(H)=1.3813564445184977933\ldots,\qquad
 H(a,b,c)=a+a^{-1}+b+b^{-1}+c+c^{-1},
\]
and subsequently identifies it with \(M(1+X+Y)\).
The six-term display is unnumbered.
The immediately following seven-term display, which includes an extra constant \(1\), bears the label (4–3); that label must not be assigned to the six-term equality.
The decimal above is a reported source value, not a numerical computation performed here.

The local limiting polynomial is
\[
 G(u,v,Y)=(v+v^{-1})(Y+Y^{-1})-(u+u^{-1}).
\]
Set
\[
 a=vY,\qquad b=v/Y,\qquad c=-u.
\]
Then \(G(u,v,Y)=H(a,b,c)\).
In input coordinates \((v,Y,u)\), the exponent matrix has rows
\((1,1,0),(1,-1,0),(0,0,1)\), hence determinant \(-2\).
Given \((a,b,c)\in\mathbb T^3\), choose \(v^2=ab\), put \(Y=a/v\) and \(u=-c\), so this map is a surjective degree-two cover followed by a translation.
The preceding Haar argument proves \(m_3(G)=m_3(H)\).

The reduction to the source's §2 polynomial can also be checked without numerical input.
Put
\[
 K(X,Y,Z)=X+Y+Z+XY+YZ+ZX
\]
as in BM05 (2–1).
Under \(X=ab,\ Y=ac,\ Z=bc\),
\[
 K(ab,ac,bc)=abc\,H(a,b,c).
\]
This exponent matrix again has determinant \(-2\) and is surjective: choose \(a^2=XY/Z\), then \(b=X/a,\ c=Y/a\).
Therefore \(m_3(K)=m_3(H)\).
Finally,
\[
 K(X,Y,Z)=Z(1+X+Y)+(X+Y+XY).
\]
On \(\mathbb T^2\), the two coefficients have equal absolute value, since
\(X+Y+XY=XY(1+X^{-1}+Y^{-1})\).
Jensen's formula in \(Z\), the same calculation given after source (2–1), yields
\[
 m_3(G)=m_3(H)=m_3(K)=m_2(1+X+Y).
\]
This identifies the already positive fixed limit in L133 v3; it supplies no uniform gap for arbitrary pairs \(A_0,B_0\), and no convergence rate uniform in such pairs.

<a id="numerical-scope-and-prefix-boundary"></a>
## Numerical scope and the boundary of the comparison

The proposed minimum \( \min_b M(P_{a,b})=M(P_{a,2a-1}) \) in source (2–4), and monotonicity in \(a\), are numerical suggestions.
Section 4.3 includes \(Q_{a,b}\) with \(a,b\leq20\) and reciprocal quadratics of height \(1\) with \(\deg_X\leq9\); these finite searches do not establish a positive lower bound over arbitrary cyclotomic products, degrees or multiplicities.
The source contains genuine analytic identities as well as numerical families, but the inspected passages supply no unrestricted uniform positive gap.

The closest common mechanism is the quadratic Jensen reduction and the cyclotomic coefficient subfamilies.
The integer Taylor-prefix estimate and its Poisson/Parseval argument in [L133 v3](../../../ledger/Yin_L_G0133_v3.md#integer-prefix-estimate), and the subsequent compactness mechanism in [L133 v4](../../../ledger/Yin_L_G0133_v4.md#short-local-limits), were not found in the inspected source passages.
Section 6 instead discusses whether specializations give genuine accumulation points, and §1 (1–6) explicitly separates convergence of measures from that stronger conclusion.
This bounded comparison does not establish originality or absence elsewhere in the literature, nor does it invalidate the local prefix estimate.
The comparison preserves the original unrestricted total-Mahler objective and does not replace it with the source's finite searches.

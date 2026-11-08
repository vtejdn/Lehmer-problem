---
author: Yin
---

# Independent review of the fourth-root bound for a central prefix

<a id="fourth-root-review"></a>
## The neutral example and the scale of prefix agreement

At 2026-11-08T02:14 UTC a separately assigned agent for Yin checked all four sections of [L464 v3](../../ledger/Yin_L_G0464_v3.md#central-control).
The reviewer took no part in developing this proof and received the fixed material and dependency locators without development dialogue, author explanation or an earlier verdict on v3.
The earlier reviews of the [fixed-weight gap](Yin_R_G1105_v2.md#weighted-lift-review) and the [coefficient limits in v2](Yin_R_G1105_v3.md#prefix-rigidity-review) were available.
Only the fixed-weight gap is needed for the deduction below.

**Odd-degree control.**
At \(\theta=j\pi/d\) the two sine identities give \(B'(b_j)=(-1)^{j+1}d/(2\sin^2\theta)\) and \(U_{d-2}(b_j/2)=(-1)^{j+1}\).
Thus the residue is \(2b_j\sin^2\theta/d\), strictly of the sign of \(b_j\) for odd \(d\), and evaluation at \(-2\) gives \(Q_0(-2)/B(-2)=-2/d\).
Lifting \(tB\) and \(tU_{d-2}(t/2)\) and adding yields \((1+z^2)(1+z-z^{2d-1}-z^{2d})/(1-z^2)\), the claimed geometric sum times \(1+z^2\).
All its zeros are roots of unity, and its two limits are the stated \(P_*\) and \((1-z^2)P_*=F_0\).

**Moments and positivity.**
Modulo \(z^{L+1}\), multiplication by \(1/B^*\) is multiplication by \(1-z^2\) for \(L\le d\), and the latter has invertible constant term.
Comparison of the coefficient of \(z\) and of each \(z^{j+2}\) in the secular expansion gives \(a=-1\) and \(\int U_j(t/2)\,d\sigma=\mathbf 1_{\{j=1\}}\) through \(j=L-2\).
Under \(t=2\cos\theta\), the semicircle law becomes \((2/\pi)\sin^2\theta\,d\theta\) on \([0,\pi]\), so it has mass one and the \(U_j(t/2)\) are orthonormal.
Since \(t=U_1(t/2)\), the signed measures \(\sigma\) and \(t\nu\) agree on the claimed polynomial space.
In particular \(\int (t-c)\,d\sigma=1\) when \(L\ge3\), and each atom of \(\mu=(t-c)\sigma\) is positive by the separator choice.

**Cut localization.**
For a polynomial of degree at most \(2h-1\), the quotient on division by \(U_h(t/2)\) has degree at most \(h-1\), so the multiple has zero \(\nu\)-integral.
The stated quadrature weights integrate the remainder on its \(U_0,\ldots,U_{h-1}\) basis by discrete sine orthogonality.
For large \(L\) the largest allowed odd \(h\) is at least three and \(h\asymp L\).
Taking \(g\) to be the product of the \(h-2\) linear factors at the other nodes, the moment comparison tests \((t-c)g^2\) of degree \(2h-3\le L-2\), and quadrature tests \(t(t-c)g^2\) of degree \(2h-2\le2h-1\).
The zero node contributes nothing, and the other surviving term has the sign of \(v(v-c)\) or \((-v)(-v-c)\), respectively.
Thus \(-v\le c\le v\) with \(v=2\sin(\pi/(h+1))=O(L^{-1})\).

**Localized mass and quantifiers.**
Choose odd \(m\asymp L\) with the ratio \(m/L\) small enough to meet both \(4(m-1)+1\le L-2\) and \(m|c|\le1/2\), using the uniform constant in the preceding cut bound.
With \(s=\arcsin(t/2)\), the upper bound follows from \(|\sin(ms)|\le m|\sin s|\) and \(|\sin(ms)|\le1\).
For \(|t|\le1/m\), \(|s|\le\pi|t|/4\) and \(|s|\ge |t|/2\), so \(|\sin(ms)|\ge2m|s|/\pi\) gives the stated lower bound, including the removable value in modulus at zero.
The moment test now has degree \(4(m-1)+1\).
In the comparison integral the term \(-ctG_m^4\) even integrates to zero by parity.
Using the bounded density of \(\nu\), the \(t^2\) term is \(O(m^{-3})\) on \(|t|\le1/m\) and at most a constant times \(m^{-4}\int_{1/m}^2 t^{-2}\,dt=O(m^{-3})\) outside.
The lower bound then gives the same upper bound for the positive \(\mu\)-mass of the inner interval.

For neighboring poles with angular midpoint \(\phi\) and half-spacing \(\delta=\pi/(2d)\), their arithmetic midpoint is \(2\cos\phi\cos\delta=c\) and their separation is \(4\sin\phi\sin\delta\).
Since \(c=O(1/L)\), this separation is bounded below by a constant times \(d^{-1}\) for large \(L\).
All poles are at least half this separation from the cut, while outside \([-1/m,1/m]\) their distance is at least \(1/(2m)\).
With total \(\mu\)-mass one this proves \(V\ll d m^{-3}+m\), hence \(|c|V\ll1+d/L^4\).
The [fixed-weight statement with \(A(t)=t\)](../../claims/Yin_C_G0880_v2.md#statement) forces \(\sum |b_i r_i|\to\infty\) along every positive shrinking-shell sequence.
Here \(\sum |b_i r_i|\le\sum |b_i-c|\,|r_i|+|c|V=1+|c|V\), verifying the required interface directly.
Any subsequence with \(L\ge\varepsilon d^{1/4}\) for fixed \(\varepsilon>0\) would have \(L\to\infty\) and bounded \(|c|V\), a contradiction.

The four sections establish \(L=o(d^{1/4})\) under the stated prefix, grid, sign and positive shrinking-measure hypotheses.
The neutral example shows why positivity of the logarithmic measure matters.
The review uses the accepted fixed-weight theorem at its stated scope and supplies no optimality claim for the exponent or consequence for a different prefix.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Central prefix bound](#fourth-root-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Central prefix bound](#fourth-root-review) | [Neutral example](../../ledger/Yin_L_G0464_v3.md#central-control) | Strict signs for odd degree, left endpoint, exact lift, measure and coefficient limits. |
| [Central prefix bound](#fourth-root-review) | [Fourth-root statement](../../ledger/Yin_L_G0464_v3.md#fourth-root) | Quantifiers, equivalence of prefixes, signed moments and weighted probability measure. |
| [Central prefix bound](#fourth-root-review) | [Cut localization](../../ledger/Yin_L_G0464_v3.md#cut-localization) | Quadrature exactness, the two polynomial degree budgets and the uniform bound on the midpoint. |
| [Central prefix bound](#fourth-root-review) | [Mass and rate](../../ledger/Yin_L_G0464_v3.md#localized-mass) | Chebyshev estimates, inner mass, midpoint separation, variation and little-o conclusion. |
| [Central prefix bound](#fourth-root-review) | [Fixed-weight escape](../../claims/Yin_C_G0880_v2.md#moving-cut) | Application with algebraic cut zero and weight \(t\) to the positive shrinking shell. |

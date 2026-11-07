---
author: Yin
---

# Classification below Smyth's bound for a single integral normalized derivative

Provenance: project deduction from the two fixed inputs below.
This argument concerns the full domain of a single normalized derivative in the bounded discussion of the November 2026 commit.
It requires no divisibility condition on higher derivatives.

<a id="statement"></a>
## Classification of the integral domain below the threshold

Let \(\theta>1\) be the real root of \(x^3-x-1\).
For a monic \(P\in\mathbb Z[x]\) of degree \(d\ge1\), suppose \(P'/d\in\mathbb Z[x]\) and \(M(P)<\theta\).
Then either \(P=x^d\), or
\[
      P=(x^k+\xi)^{d/k},\qquad k\mid d,\quad \xi\in\{1,-1\}.
\]
Conversely each polynomial in this list has an integral normalized derivative and Mahler measure one.
Consequently every monic \(P\) with \(1<M(P)<\theta\) has a nonintegral normalized derivative, even after multiplication by any monic integer polynomial of measure one and normalization by the new degree.

<a id="argument"></a>
## Proof

Write \(P=x^s H\) with \(H\) monic and \(H(0)\ne0\).
The pure monomial case is immediate.
Otherwise the integer \(H(0)\) has absolute value at most \(M(P)<2\), so \(H(0)=\pm1\).
If \(0<s<d\), the coefficient of \(x^{s-1}\) in \(P'/d\) equals \(sH(0)/d\), which cannot be an integer.
Hence \(s=0\) and \(\varepsilon=P(0)=\pm1\).

For a monic integer polynomial of measure less than \(\theta\), its nonzero-root core is reciprocal up to its constant sign.
This follows by multiplicativity, Kronecker's theorem for the measure-one factors and [Smyth's nonreciprocal bound](../audits/literature/Smy71/Yin_U001.md#smy71-statement-and-conventions) for positive-measure irreducible factors, as detailed in the [coefficient-box argument](Yin_C_G0870_v1.md#reciprocity-of-the-nonzero-root-core).
For a polynomial of degree at most \(j\) write \(\operatorname{rev}_j F=x^j F(1/x)\).
The core property gives \(P=\varepsilon\operatorname{rev}_d P\).
Put \(Q=P'/d\).
By [Mahler's derivative inequality](../ledger/Yin_L_G0461_v1.md#normalized-derivative-descent), \(M(Q)\le M(P)<\theta\).
The monic polynomial \(Q\) is integral by hypothesis, so writing \(Q=x^{k-1}R\) with \(R(0)\ne0\) gives \(1\le k\le d\), \(\eta=R(0)=\pm1\) and \(\operatorname{rev}_{d-k}R=\eta R\).
These conventions also cover \(Q=x^{d-1}\) and \(R=1\).

Differentiate \(P=\varepsilon x^dP(1/x)\) to get \(P=xQ+\varepsilon\operatorname{rev}_{d-1}Q\).
Substitution and cancellation of the nonzero polynomial \(R\) in the field of rational functions yield
\[
 P=(x^k+\varepsilon\eta)R,\qquad
 \frac{P'}{P}=\frac{d\,x^{k-1}}{x^k+\varepsilon\eta}.
\]
Every root of \(x^k+\varepsilon\eta\) is nonzero and simple, and the residue of the right side there is \(d/k\).
The poles of a polynomial's logarithmic derivative are precisely its roots and their residues are their positive integer multiplicities.
Hence \(k\mid d\) and monicity determines \(P\) as claimed.
In the converse direction the normalized derivative of \((x^k+\xi)^{d/k}\) is \(x^{k-1}(x^k+\xi)^{d/k-1}\), and all roots have modulus one.
The padding statement follows since the product remains monic, integral and of the same positive logarithmic measure.

This excludes the entire small-positive interval from the one-step integral domain in [L461](../ledger/Yin_L_G0461_v1.md#normalized-derivative-descent).
The sharp bound on the more restrictive fully binomially divisible class is a separate [coefficient-window result](Yin_C_G0872_v1.md#statement).
The proof gives no optimal lower bound for the one-step integral domain above \(\theta\) and imposes no restriction on the Mahler measure of a nonintegral normalized derivative beyond the cited analytic inequality.

## Assessment history

### Decision integral-normalized-derivative

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:03 |
| status | proved |
| reason | The single-step classification, converse and measure-one padding conclusion passed complete independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every monic integer input below the strict Smyth threshold with integral normalized derivative. |
| argument | [Proof section](#argument) | Reciprocal cores, the rational logarithmic derivative and both directions. |
| review | [Independent finding](../audits/reviews/Yin_R_G1100_v1.md#integral-normalized-derivative) | All of the selected statement and argument at the source scope specified in the finding. |

## Current assessment

[Selected decision](#decision-integral-normalized-derivative)


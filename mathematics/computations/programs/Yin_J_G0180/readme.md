---
author: Yin
---

# Exact two-term projection at Lehmer's unit

<a id="projection"></a>
## A signed terminal tuple of weight eight

Let \(\alpha>1\) be Lehmer's real unit with minimal polynomial \(X^{10}+X^9-X^7-X^6-X^5-X^4-X^3+X+1\), and let \(R=\mathbb Z[\alpha]\) with involution \(\iota(\alpha)=\alpha^{-1}\).
For the ordered coefficients \((1,1,-1,-2,-2,-1,1,1)\), require eight distinct increasing exponents of span at most 32 and normalize the minimum to zero.
Delete the two terms with coefficient \(-2\).
Write \(x_1=0<x_2<\cdots<x_6\le32\) for the remaining exponents and \(z\) for their signed sum with coefficients \((1,1,-1,-1,1,1)\).
The missing terms must satisfy \(z=2(\alpha^s+\alpha^t)\) with \(x_3<s<t<x_4\).
The [reciprocal two-term projection](../../../ledger/Yin_L_G0462_v313.md#recovery) determines the gap from \(z\iota(z)=8+4(\alpha^{t-s}+\alpha^{s-t})\).
The second count below divides each six-exponent list by its own positive gcd independently at each stage, so a primitive shape qualifies whenever at least one dilation passes the stated test.

| Test on the six exponents | Lists | Primitive shapes |
| --- | ---: | ---: |
| All lists | 201376 | 196751 |
| \(z\iota(z)\in4R\) | 566 | 562 |
| \(z\in2R\) | 188 | 184 |
| Exact trace for some gap from 1 through 32 | 140 | 139 |
| Exact equality \(z=2(\alpha^s+\alpha^t)\) at that gap with unrestricted integer start | 36 | 35 |
| Equality with total span at most 32 | 36 | 35 |
| Equality with both large terms in the prescribed positions | 2 | 2 |
| Terminal for all rational multiples of arbitrary powers | 2 | 2 |

The residual divisibility and exact trace tests branch separately from \(z\iota(z)\in4R\).
Precisely 36 of the 140 exact-trace lists have \(z\in2R\), and these are exactly the 36 admitting the two positive powers with the prescribed coefficients before the order test.
None of the 140 lists has \(z=-2(\alpha^s+\alpha^t)\) at the trace gap.
Thus 104 failures of the trace to give the required positive phase are already detected by residual parity here.
The two terminal full lists are \((0,1,5,6,7,8,12,13)\) and \((0,3,4,5,13,14,15,18)\).
These conclusions are confined to the stated polynomial, coefficient order and window.

<a id="reproduce"></a>
## Reproduction and bounds for the exhaustive checks

Run `python mathematics/computations/programs/Yin_J_G0180/projection.py` from the repository root.
The [executed program](projection.py) uses Python integer arithmetic and the coefficient basis \(1,\alpha,\ldots,\alpha^9\) for both positive and negative powers.
It sums the six diagonal contributions and fifteen signed gap traces to obtain \(z\iota(z)\).
For the modular screen it stores each of the ten residues modulo 4 in its own base-1024 digit, with at most \(6+15\cdot3\) in any digit before reduction.
A separate binary-polynomial recurrence over every six-position support checks the count for \(z\in2R\) and confirms that \(X\) has order 31 modulo the reduced minimal polynomial.

The polynomial is negative at \(7/6\) and has its unique root above one at \(\alpha\), so \(\alpha>7/6\).
For either phase sign, the positive real embedding bounds \(2\alpha^t\le6\alpha^{32}\) and the reciprocal embedding gives \(2\alpha^{-s}\le6\).
Thus checking both exponents in \([-16,48]\) covers every possible start at the required gap, since \((7/6)^{16}>10\).
For a [rational terminal split](../../../claims/Yin_C_G0345_v584.md#statement), any nonzero subset sum equal to \(c\alpha^k\) has \(c\in\mathbb Z\), since the subset sum and \(\alpha^{-k}\) are algebraic integers.
For a completed list in \([0,32]\) every subset has sum of absolute coefficient magnitudes at most 10.
At the growing and contracting real embeddings this gives \(|c|\alpha^k\le10\alpha^{32}\) and \(|c|\alpha^{-k}\le10\), so the same exponent interval suffices.
The program checks every subset of size one through four for zero and every subset of size two through four for a rational multiple of one of the tested powers by comparing primitive signed coefficient vectors.
The complementary subset in the zero relation handles the larger allowed sizes.

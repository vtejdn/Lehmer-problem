---
author: Yin
---

# Exact coefficient minima through row width five

The [quartic minimum-support computation](versions/v5/readme.md#sample) gives the exact coefficient norms at widths eight and nine for four exponents, including the costs of omitting each position at width nine.
The [complete width-nine calculation](versions/v6/readme.md#minima) also allows all ten coefficients and finds the first two independent minima at five exponents.
The [cyclic quotient calculation](versions/v7/readme.md#approximation) determines the two modular approximation minima and the orders of both quotients at 55 exponents.

<a id="census"></a>
## The fallback is the minimum at every odd prime through 1009

In the [finite minimum of C408](../../../claims/Yin_C_G0345_v408.md#statement), \(M_{p,b}=2^p\) for every \(1\le b\le5\) and every odd prime \(3\le p\le1009\).
There is no qualifying pair even at equality with the cutoff.
The [quartic trace classification](../../../ledger/Yin_L_G0462_v242.md#short) reduces this range exactly to the two inputs \(P_A=X^4-X^3-X^2-X+1\), \(P_B=X^4-2X^3+X^2-2X+1\), up to changing the variable sign.
The test at width five includes all smaller row widths.
There are 168 odd primes and 336 seed/prime cases.
In 334 cases one squared-length comparison suffices after reducing the two integral lattices.
In the remaining cases the final searches give the following counts of vectors of one-norm at most \(2^{p+1}\), identifying a vector with its negative within each eigenspace.

| Prime | Seed | Shortest squared lengths in the two lattices | Counts of eligible nonzero vectors by sign space | Passing pairs |
| ---: | --- | --- | --- | ---: |
| 3 | \(P_A\) | \(19,34\) | \(5,1\) | 0 |
| 5 | \(P_B\) | \(2224,892\) | \(0,1\) | 0 |

<a id="controls"></a>
## Least qualifying costs before imposing the cutoff

The uncapped minima concern the indicated seed and prime, so a witness exceeding \(2^p\) does not enter the finite minimum.
The polynomial gcd, unequal row moduli and double divisibility of every positive witness are checked by exact arithmetic.

| Prime | Seed | Width four | Width five |
| ---: | --- | ---: | ---: |
| 3 | \(P_A\) | No pair | 45 |
| 3 | \(P_B\) | 516 | 60 |
| 5 | \(P_A\) | 752 | 164 |
| 5 | \(P_B\) | 248 | 180 |
| 7 | \(P_A\) | 633243 | 6886 |
| 7 | \(P_B\) | 562539 | 14161 |

Width four uses the [two-line formula](../../../ledger/Yin_L_G0462_v242.md#lines), including its zero determinant case.
At width five we double the height ceiling until the first nonempty search.
That search computes the least cost throughout the entire ceiling and certifies the indicated minimum.
The output includes the attaining rows and the exceptional two lines for the empty width-four case.

<a id="method"></a>
## Exhausting the two integral eigenspaces

For width \(b\) use formal reversal \(A^*(Y)=Y^b A(1/Y)\).
Reversing a graph about \(pb+1\) preserves its double factor and acts on rows by \((U,V)\mapsto(V^*,U^*)\).
For either sign, the integral first coordinates in its eigenspace are the integral nullspace of a matrix with column \(i\) the coefficients of
\[
                    x^{pi}\pm x^{p(b-i)+1}\pmod {P(x)^2},
                    \qquad 0\le i\le b .
\]
Multiply by \(x\) and reduce by the monic \(P^2\) to compute these columns over \(\mathbb Z\).
For every tested width-five input the two rational nullspaces have dimension two.
Any qualifying integral row with cost at most \(H\) gives two nonzero integral vectors \(A=U+V^*\), \(C=U-V^*\) of one-norm at most \(2H\), one from each respective eigenspace.
Conversely they recover integral rows \((U,V^*)=((A+C)/2,(A-C)/2)\) exactly when the coefficients have the same parities.
Changes of either eigenvector sign negate both rows or exchange them with their reversals, up to an overall sign.
Common nonzero roots are carried to their reciprocals; at zero the two formal reversals can introduce a common monomial.
The program removes every common power of \(Y\) in the reconstructed pair, preserving both coefficient sums, the degree cap, and double divisibility because the seed is a unit polynomial.
Thus one representative of each sign suffices for the existence and least cost with ordinary gcd one.

For saturation, rational elimination first expresses all coordinates in two free coordinates, which must themselves be integers.
If the next linear coordinate is \((ai+bj)/D\), put \(g=\gcd(a,b)>0\) and choose \(s,t\) with \(as+bt=g\).
The unimodular basis \((s,t),(b/g,-a/g)\) turns integrality into the requirement that its first coordinate be divisible by \(D/\gcd(D,g)\).
Imposing each coordinate in turn therefore gives the full integer lattice.
A one-dimensional rational kernel instead gives its primitive generator by clearing denominators in a vector with free coordinate one.

Gauss reduction in a plane basis \(u,v\) uses only unimodular swaps and integral subtractions.
At termination \(A=u\cdot u,\ B=u\cdot v,\ C=v\cdot v\) satisfy \(A\le C,\ 2|B|\le A\).
Thus \(A\) is the shortest nonzero squared length, as follows from \(Ai^2+2Bij+Cj^2\ge A(i^2-|ij|+j^2)\).
If either lattice has \(A>(2H)^2\), no qualifying row exists.
Otherwise set \(D=AC-B^2\) and enumerate the full ellipse
\[
                    (Ai+Bj)^2+Dj^2\le A(2H)^2.
\]
Exact integer square roots determine the coefficient bounds, after which filtering by one-norm gives every candidate up to sign.
For both eigenvectors the program checks parity and actual cost before checking autocorrelations and the rational polynomial gcd.
An attained minimum is also checked against the original remainder columns.

<a id="reproduction"></a>
## Reproducing the prime census

Run the following command from the repository root with Python 3.10 or later.
The program uses the standard library and contains the two seed coefficient lists and the inclusive prime bound.

```text
python mathematics/computations/programs/Yin_J_G0177/minimum.py
```

The [program](minimum.py) generates the [per-seed and per-prime output](../../outputs/Yin_J_G0177/results.json) in the local generated-data directory.
It records the two shortest squared lengths for each of the 336 cases, the vector counts when enumeration was needed, the finite-height result and the six uncapped controls.
The exact seed reduction, width-four formula, and a factored positive witness are retained in [L242](../../../ledger/Yin_L_G0462_v242.md#examples).
No floating-point approximation to a root, lattice length or coefficient cutoff enters the calculation.

The [width-nine calculation](versions/v2/readme.md#census) uses the same lattice methods to obtain the uncapped minima for one octic at all odd primes through 251.

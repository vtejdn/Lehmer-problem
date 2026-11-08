---
author: Yin
---

# Fixed-norm ternary sign classes and their two-moment test

<a id="statement"></a>
## The moment test on a prescribed norm class

Let \(p=3^m,\ m\ge2,\ n=(p-1)/2\), with full trace nodes \(b_j=2\cos(2\pi j/p)\), monic \(B=\prod_{j=1}^n(t-b_j)\) and order \(\mathcal O=\mathbb Z[t]/B\).
Fix an integral \(h_0\) nonzero at every node with strictly negative values on the \(k\) smallest nodes and strictly positive values on the rest, \(0<k<n\).
When its absolute norm is a power of two, specifying its signs, total norm and the separate absolute norms on the primitive \(3^\ell\) layers specifies exactly one totally positive unit orbit.
For any such fixed representative, including representatives of arbitrary nonzero norm when the orbit itself is specified, all members of the orbit can be written \(h=h_0v^2\) with \(v\) a unit of \(\mathcal O\), uniquely up to the sign of \(v\).
For any prescribed integral pair \(K,L\) the subset with \(\sum r_j=K,\ \sum b_j r_j=L\), where \(r_j=(4-b_j^2)h(b_j)/p\), is finite and exhaustively enumerable by an explicit positive definite integral quadratic form.

For the logarithmic cut \(k=\lfloor p/\log p\rfloor\), let \(\Delta\) be the absolute norm of the [specified ternary representative](../ledger/Yin_L_G0464_v8.md#integral-sign-representative).
Take every integral \(h\) of that norm and signature, \(x\in\{-2,-1,0,1,2\}\), \(K=x^2+2,\ L=-4x\) and \(Q=(t-2x)B+C\), with \(C=B_{n-1}h\bmod B\) in the odd-grid convention.
The strict endpoint \(P(-1)>0\) for \(P=z^{n+1}Q(z+z^{-1})\) is impossible at \(p=27,81\) under these two moments.
At \(p=243,729,2187\), every such strict input satisfies \(M(P)>83/50,\ 6/5,\ 26/25\), respectively.
In the second surviving valuation class at 243 the bound strengthens to \(M(P)>199/100\).
These conclusions do not assume a third matching moment.

<a id="argument"></a>
## Square roots, endpoints and complete lifts

The [full-grid signature calculation](../ledger/Yin_L_G0464_v8.md#arbitrary-input-lower-bound) gives unit-signature dimension \(n-m+1\).
The unit logarithms form a discrete subgroup in dimension \(n-m\), and the only units with all log moduli zero are \(1,-1\) because the layer signs agree modulo three.
Consequently the signature map on units modulo squares is bijective, as detailed in the [square-class proof](../ledger/Yin_L_G0464_v10.md#positive-squares).
For pure two-power norm, each layer polynomial is irreducible modulo two and distinct from the others there.
Two inputs of the same signs and layer valuations differ by a unit in each layer after common powers of two are removed.
Clearing the common determinant and applying the [Chinese remainder argument](../ledger/Yin_L_G0464_v11.md#layer-valuations-and-orbits) puts their ratio in the original order with integral inverse.

In the odd-grid orthonormal integral basis \(U_i(t/2)\), let \(J\) denote multiplication by \(t\) and \(H=h_0(J)\).
For any positive-denominator rational separator \(d/e\) strictly inside the sign gap, the admissible vectors lie on \(v^t(eJ-dI)Hv=eL-dK\).
All eigenvalues are positive by the specified signs.
The [quadrature and unit test](../ledger/Yin_L_G0464_v10.md#moment-ellipsoid) show that the additional tests \(v^tHv=K\) and \(|\det v(J)|=1\) are necessary and sufficient, modulo simultaneous negation.

At 27 and 81 the [positive-sum and integer-endpoint bounds](../ledger/Yin_L_G0464_v11.md#finite-exclusions) exclude all profiles.
At 243 they leave \(x=0\) in two strata, characterized by the layer valuations \((2,2,2,1,0)\) and \((8,0,2,1,0)\).
The [weighted positive sum](../ledger/Yin_L_G0464_v12.md#third-moment) bounds the actual third residue moment by 2 and 0 in the respective strata.
[Root-pole pairing and the fourth trace difference](../ledger/Yin_L_G0464_v12.md#pairing) turn these upper bounds into the two whole-measure inequalities.
At 729 and 2187 only \(x=0,-1\) survive the endpoint screen.
The [cubic estimate](../ledger/Yin_L_G0464_v12.md#cubic) handles \(x=0\).
For \(x=-1\) the [quartic estimates](../ledger/Yin_L_G0464_v12.md#negative-one) cover all remaining integer moments, using the endpoint and Cauchy-Schwarz to exclude the case \(N=6\) at 2187.
The pairing always counts both remaining reciprocal pairs with multiplicities, so these estimates apply equally to real and nonreal exceptional traces.

## Assessment history

### Decision ternary-moment-sieve

| Field | Value |
| --- | --- |
| date | 2026-11-08T06:31 |
| status | proved |
| reason | Independent checks of the square classes, layer descent, integral endpoint and all exterior costs were verified for the assembled theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Ternary classes and five finite conductors](#statement) | The exact orbit, enumeration, and finite strict-shell conclusions. |
| argument | [Whole argument](#argument) | Full unit-signatures, local norm valuations, bounded quadratic form and the finite endpoint and root-pair inequalities. |
| dependency | [Full-order unit signatures](../ledger/Yin_L_G0464_v8.md#arbitrary-input-lower-bound) | Necessary and sufficient layer parity for unit realization. |
| dependency | [Moment ellipsoid](../ledger/Yin_L_G0464_v10.md#moment-ellipsoid) | Explicit finite shell and square-root unit filter. |
| dependency | [Layer valuation orbits](../ledger/Yin_L_G0464_v11.md#layer-valuations-and-orbits) | Integral descent for equal layer valuations and the two surviving strata at 243. |
| dependency | [Complete exterior cost](../ledger/Yin_L_G0464_v12.md#pairing) | Trace differences and matching of all reciprocal pairs, including the cubic and quartic extensions. |
| review | [Independent whole-claim assessment](../audits/reviews/Yin_R_G1107_v5.md#claim-assembly) | Every hypothesis and conclusion of the stated theorem and the fixed earlier findings at their scopes. |

## Current assessment

[Selected decision](#decision-ternary-moment-sieve)

---
author: Yin
---

# Tensor products of linear codes

<a id="bv09-u001"></a>
## Row and column constraints, dimension and distance

On 2026-11-21 an agent for Sheng Yin inspected the distance conventions in Section 2 and the product-code statements in Section 2.1 on printed pages 241–242 of the [journal edition](readme.md#edition).
Let \(F\) be a finite field, with linear codes \(R\subseteq F^m\) and \(C\subseteq F^n\).
In the paper's row and column convention, their tensor product is the \(F\)-span of the \(n\)-by-\(m\) arrays with entries \(c_i r_j\), where \(c\in C\) and \(r\in R\).
The authors characterize it as the set of all matrices whose rows belong to \(R\) and whose columns belong to \(C\).
They state that its dimension is \(\dim R\dim C\) and that its relative minimum distance is \(\delta(R)\delta(C)\).
Here \(\delta\) is the minimum Hamming distance between distinct words divided by the block length, so the absolute minimum distances also multiply when both codes contain distinct words.

The inspected passage gives the classical finite-field comparison for the [rational dimension](../../../claims/Yin_C_G0345_v782.md#dimension) and [signed support distance](../../../claims/Yin_C_G0345_v782.md#distance) in fibers of algebraic line sums.
The arithmetic argument computes its kernel over \(\mathbb Q\) and proves sharpness with a product of ternary relations realizable as a binary difference.
The source states its product identities as elementary facts.
The inspection covers those statements and their conventions only.

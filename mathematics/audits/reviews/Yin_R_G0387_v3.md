---
author: Yin
---

# Reciprocal units with sparse Frobenius matching and bounded coefficients

At 2026-11-16T11:07 UTC a reviewer outside the proof development independently checked both finite-prime constructions in G0162v2 for Yin.
The reviewer used the fixed statement, its construction and the two source units below, without consulting development discussions or previous review conclusions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite-prime constructions](#finite-pool-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite-prime constructions](#finite-pool-finding) | [Statement](../../claims/Yin_C_G0162_v2.md#statement) | The two final existence assertions for every finite nonempty prime set and each prime \(\ell\ge5\), including the coefficient, Mahler measure and absolute height bounds. |
| [Finite-prime constructions](#finite-pool-finding) | [Construction](../../claims/Yin_C_G0162_v2.md#finite-pool) | Both sets of local prescriptions, their simultaneous realization, the splitting-field action, the compatible-pair count and the archimedean estimates. |
| [Finite-prime constructions](#finite-pool-finding) | [Finite-field input](../literature/Hun74/Yin_U006.md#hun74-u006) | Existence of extensions and irreducibles of the prescribed degrees, separability and Frobenius cycles. |
| [Finite-prime constructions](#finite-pool-finding) | [Residue action](../literature/The26b/Yin_U001.md#the26b-u001) | Inertia as the kernel on residues and the lift of the residue-field Frobenius. |

<a id="finite-pool-finding"></a>
## Finding

For each \(p\in S\), the order \(p^\ell+1\) of \(\lambda\) divides \(p^{2\ell}-1\) and exceeds \(p^j-1\) for every proper divisor \(j\) of \(2\ell\).
Thus \(\lambda\) has degree \(2\ell\), and \(\lambda^{p^\ell}=\lambda^{-1}\) puts its trace in degree \(\ell\), with equality since the lift is at most quadratic.
The prescribed reciprocal reduction is consequently the separable minimal polynomial of \(\lambda\), including at \(p=2\).
Irreducibility at one such \(p\) suffices over \(\mathbb Q\).
At each auxiliary prime the distinct trace roots avoid \(\pm2\), so their quadratic lifts have distinct roots throughout.
At every prescribed prime an inertia element must therefore fix every root in the splitting field, and the lifted Frobenius cycles have the reduction factor degrees.
The two source units supply the finite-field and residue-action statements at their recorded inspection depth.

For the first construction the large auxiliary primes provide the required linear factors and both types of linear trace, since inversion pairs all eligible elements of the split and norm-one groups.
For the bounded family fix distinct \(q,q'\ge7\) outside \(S\), and put \(k=\ell-2\).
At \(q\) the block action has cycle lengths \(2,k\), so its \(k\)-th power is a block transposition.
At \(q'\) a generator \(u\) of \(\mathbb F_{q'^k}^{\times}\) has degree \(k\), and its trace has degree \(k\) since the relative degree is at most two and divides the odd integer \(k\).
If \(u^{q'^j}=u^{-1}\), then \(k\mid 2j\), hence \(k\mid j\) and \(u=u^{-1}\), contrary to its order.
The two degree-\(k\) cycles therefore disappear upon taking the \(k\)-th power, leaving precisely the exchange above the nonsplit linear trace.

In both constructions a designated prime supplies an \(\ell\)-cycle on the blocks.
Its translates of the transposition form the edges of a connected graph because the step is nonzero modulo the prime \(\ell\).
Thus the block image is \(S_\ell\), and conjugating the single exchange supplies the full kernel of independent exchanges.
The wreath group acts transitively on ordered pairs drawn from different blocks.
Distinct reductions give exactly one Frobenius successor per root, always in a different block, so the unique compatible orbit has \(d\) matching pairs among its \(d(d-2)\) pairs.

In the first family the constant trace coefficient may increase without bound in its residue class, forcing an unbounded trace root and hence an unbounded reciprocal lift for fixed \(\ell\).
For the bounded family the modulus \(N=qq'\prod_{p\in S}p\) is independent of \(\ell\).
Each symmetric coefficient pair needs only one residue representative, and the prescribed interval for \(a_{d-1}=a_1\) contains exactly \(N\) consecutive integers.
The symmetric Laurent expression recovers the monic integral trace polynomial, so this direct lift realizes the same local actions.
Every coefficient has absolute value at most \(4N+4\), while all \(a_j\) for \(0\le j\le d-2\) satisfy the one-sided bound \(a_j\le N\), including the negative \(a_1\).
Consequently \(2^{1-d}P(2)\le 2+a_{d-1}+N(1-2^{1-d})<0\), and monicity gives a real root greater than two.
The geometric mean of \(|P|\) on the circle is at most its quadratic mean, which orthogonality identifies with \((\sum_j |a_j|^2)^{1/2}\).
Thus \(\log 2<m\le \frac12\log(d+1)+\log(4N+4)\), and \(h=m/d\) tends to zero.
Both existence assertions follow throughout their stated ranges.
The local norm inequalities and the growing-degree estimate lie outside this finding.

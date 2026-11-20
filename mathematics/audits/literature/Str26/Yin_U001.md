---
author: Yin
---

<a id="str26-u001"></a>
# Strict Garsia entropy at units with no conjugate on the unit circle

<a id="rate"></a>
## Entropy and the strict inequality

For independent identically distributed integer digits with finite law \(\nu\), set \(X_n=\sum_{i=0}^{n-1}\xi_i\lambda^i\).
Streck uses natural logarithms and the Shannon entropy rate \(h_\lambda(\nu)=\lim_n H(X_n)/n=\inf_n H(X_n)/n\), by subadditivity.
Maximal entropy means equality with \(\log M(\lambda)\). [§1.1, pp. 2–3](../../../literature/pdf/Str26--arxiv-v2.pdf#page=2)

Theorem 1.1 gives \(h_\lambda(\nu)<\log M(\lambda)\) whenever \(\lambda\) is algebraic, \(|\lambda|<1\), no conjugate has modulus one and at least one has modulus greater than one.
The contraction may be complex.
For a unit the absolute norm equals one, so a contracting conjugate entails an expanding one.
Conjugation preserves all equalities of digit sums and hence their Shannon entropies. [Theorem 1.1, p. 6](../../../literature/pdf/Str26--arxiv-v2.pdf#page=6)

<a id="obstruction"></a>
## Arithmetic obstruction for fair binary digits

Theorem 3.1 derives from maximal entropy a necessary Fourier zero of the digit polynomial along the two-sided orbit of every admissible character parameter.
With no unit-circle conjugate, the admissible parameters include the Laurent order and hence 1.
For a unit there are no contracting finite places, and the character at this parameter and orbit time \(k\) is the exponential of \(2\pi i\) times the sum of \(\sigma(\lambda)^k\) over contracting embeddings, up to sign convention.
For every integer \(k\), including negative \(k\), this sum is an algebraic integer because \(\lambda\) is a unit.
For independent fair digits in \(\{0,1\}\), the digit polynomial \((1+z)/2\) vanishes only at \(-1\).
Hitting this zero would require a rational half-integer of odd numerator for the partial sum of conjugates, which contradicts integrality.
This specializes the character test directly to the binary unit case. [Theorem 3.1 and subsequent discussion, pp. 15–16](../../../literature/pdf/Str26--arxiv-v2.pdf#page=15)

For general finite digit laws, §4 uses the nonrationality of a proper nonempty partial trace, a lattice-point count to avoid zeros for intermediate orbit times, and contraction of the appropriate conjugates for the two tails.
The constants in the tail estimates depend on the algebraic input. [Lemmas 4.1–4.2, Claim 4.3 and proof of Theorem 1.1, pp. 20–23](../../../literature/pdf/Str26--arxiv-v2.pdf#page=20)

Strictness implies that enumerating the finite binary sums eventually produces an \(n\) with \(H(X_n)/n<\log M(\lambda)\), giving a certified positive deficit for that input with sufficiently precise arithmetic.
The inspected proof neither specifies that length nor supplies a lower bound for the deficit relative to \(\log M(\lambda)\) along a sequence where measures shrink.
Conjugates on the unit circle, including those of Salem numbers, lie outside Theorem 1.1.
The inspection covered the entropy normalization, the two theorem statements and the arithmetic contradiction in §4, taking the analytic implication in Theorem 3.1 at statement level. [Edition](readme.md#edition)

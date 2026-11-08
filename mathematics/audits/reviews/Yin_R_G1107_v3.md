---
author: Yin
---

# Signatures, resultant bounds and Mahler measure at conductors \(3^m\)

<a id="three-power-review"></a>
## Independent review of L464 v8

At 2026-11-08T03:47 UTC, a separate agent for Yin checked the whole fixed argument in L464 v8, including the stated range of each family in its final section.
The reviewer had no involvement in its development and received no proof-generation discussion, author explanations or earlier findings on v8.
The odd-grid identities, endpoint exponent, shrinking-shell ceiling and real-root count were checked at the cited interfaces.
The circular-unit reference supplies context, and the earlier review of the ceiling was consulted for its applicability to the comparison \(\sqrt2<2\exp(-2^{-22})\).

The absolute resultant of \(D=B_{n-1}\) with \(B_n\) is one because its square is \(\prod_{j=1}^{p-1}|1+\exp(2\pi i j/p)|=1\).
The positive weights \(D(b_j)/B'(b_j)=4\sin^2(2\pi j/p)/p\) transfer the signature of \(h\) to the residues, and \(\Delta\) is the product of the absolute layer norms of \(h\).
For the primitive layers the three distinct traces above a lower trace \(y\) have sum zero and product \(y\ne0\).
Their sign bits sum to the lower bit and vary on the fiber.
Consequently the span of the translates of the top cosine bit vector contains a nonzero vector in \(\ker N\), obtained by adding its three-translate sum to the original vector.
The order of \(2\) modulo \(3^h\) is \(2\cdot3^{h-1}\), since \(v_3(4^{3^i}-1)=1+i\).
The regular module on the \(3^{\ell-1}\) sign classes at layer \(\ell\) has square-free shift polynomial, and the part complementary to the lower permutation module has polynomial \(\Phi_{3^{\ell-1}}\), irreducible over \(\mathbb F_2\) by that order.
Thus the span contains the whole kernel and maps onto the lower layer by induction.
For the full grid, taking consecutive layer differences is invertible.
Within the group of columns with \(v_3(a)=e\), the top primitive vector recovers every lower difference by successive norms, and the reverse reconstruction uses \(w_h+I v_{h-1}=v_h\).
This identifies the group's image with one summand \(I^e W_{\ell-e}\) in every layer \(\ell>e\), filling those summands independently.
Summing over \(e\) exhausts the full grid without a rank assumption on the circular units.

An odd positive representative \(u\) exists because the modulus \(3^{m-e}\) is odd.
The quotient \(T_u(X)/X\) is integral and has value one at \(X=2\).
On layers above \(e\), multiplication of the primitive indices by \(u\) permutes the numerator and denominator values in its layer product, so its signed norm is \(+1\).
The remaining factor \(T_{3^e}\) has signed norm \(-1\) on these layers by cubic descent with odd lift multiplicities, and equals two at every node of the lower layers.
Parity compression therefore gives \(\epsilon_e=\eta_{e+1}-\eta_e\bmod 2\) and exactly the stated power of two, with \(E\le (n-m)/2<n/2\).
As finite checks, direct bit elimination gave full ranks \(4,13,40,121,364\) for \(m=2,\ldots,6\).
Integral multiplication determinants in \(\mathbb Z[t]/B\) reproduced the predicted absolute norms of the constructed \(h\) for all 16 signatures at \(p=9\) and gave \(32\) for the three terminal negatives at \(p=27\).

For arbitrary integral \(C\), the unit determinant of multiplication by \(D\) gives an integral representative \(h\).
The real trace polynomial reduces to \((t-2)^{d_\ell}\) modulo three by the cyclotomic lift, giving the common signed norm residue \(h(2)\) since \(d_\ell\) is odd.
If this residue is zero, every nonzero absolute layer norm contributes at least three.
Otherwise the full cyclotomic quotient has cardinality \(A_\ell^2\) prime to three, and every \(1-\xi^j\), \(0<j<3^\ell\), is invertible there since it divides three in the cyclotomic ring.
Every nonzero orbit under multiplication by \(\xi\) consequently has length \(3^\ell\), giving \(A_\ell^2\equiv1\bmod 3^\ell\), also when \(A_\ell=1\).
At most one of \(A_\ell-1,A_\ell+1\) is divisible by three, so the signed residue modulo three selects the sign of \(A_\ell\bmod 3^\ell\).
Each parity mismatch forces \(A_\ell\ge3^\ell-1\).
Conversely, common layer parity permits only the cost-free change at \(e=0\), giving exactly the asserted criterion for a unit signature.

For the last \(k\) nodes in decreasing trace order, the odd distances \(d=1,3,\ldots,2k-1\) give \(K_i=\lfloor k/3^i+1/2\rfloor\) on counting the odd multiples of \(3^i\).
Rounding to the nearest integer at successive scales gives \(K_i-3K_{i+1}\in\{-1,0,1\}\) and \(K_m=0\).
If all layer counts were even, every digit would be even and hence zero, contrary to \(k>0\).
The odd-count layer has order at least \(L=p/(2k-1)\), whereas the largest power of three strictly below \(L>3\) lies in \([L/3,L)\) and its layer contains no negative node.
The available mismatch for either nonzero residue class, or the bound \(p\) in the divisible case, proves \(\Delta\ge L/3-1\) independently of the exceptional roots.
For \(k=3^{m-s}\) with \(1<s<m\), the count at layer \(s\) is one, all higher counts are even and all lower counts vanish, giving \(\Delta=2^{2\cdot3^{s-1}-1}\).
For \(s=\lceil\log_3m\rceil\) and large \(m\), \(m\le3^s<3m\) gives the asserted polynomial bound.
For \(k=\lfloor p/\log p\rfloor\), \(m\ge3\) ensures both sign blocks are nonempty, and \(k^{2h+1}/p^{2h}\sim p/(\log p)^{2h+1}\to\infty\) for each fixed \(h\).
At \(m=2\) this same formula for \(k\) gives \(k=n=4\), explaining the domain of the endpoint construction.
The normalized upper bound \(\sqrt2\) lies below \(2\exp(-2^{-22})\).

For the stated cuts the first residue is positive, and the ratio of every other multiplier base \(2+b_j\) to \(2+b_1\) lies strictly below one.
This proves existence of a finite \(d\) at each conductor satisfying all three inequalities, while \(|B(-2)|=1\) preserves the resultant.
The first endpoint contribution is at least \(A/4\), and the remaining absolute contributions total at most \(A/8\), giving the strict endpoint for all five choices of \(a\).
After \(t=\sqrt A\,w\), bounded poles collapse to zero and the scaled tail is uniformly \(O(1/p)\) on each compact subset away from zero.
The limiting function \(w+1/w\) has simple zeros at \(\pm i\), so the two exceptional traces form a conjugate pair with \(q/\sqrt A\to i\) in the upper half-plane.
In increasing trace order the same-sign gaps give \(n-2\) roots and the strict left endpoint gives one more, all distinct in \((-2,2)\).
These exhaust the degree together with the conjugate pair.
The two exterior reciprocal-lift roots each have modulus \((1+o(1))\sqrt A\), since \(\lambda=q-\lambda^{-1}\) and \(|\lambda^{-1}|<1\).
Thus the whole multiplicative Mahler measure is \((1+o(1))A\to\infty\) for the selected magnitudes.
Whether other representatives of these signatures can give whole measures tending to one from above remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Three-power review](#three-power-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Three-power review](#three-power-review) | [Cost statement](../../ledger/Yin_L_G0464_v8.md#three-power-cost) | Every full-grid signature, integral representative, residue transfer and resultant exponent. |
| [Three-power review](#three-power-review) | [Cosine signs](../../ledger/Yin_L_G0464_v8.md#cosine-sign-basis) | Primitive-layer and full-grid basis proofs for all \(m\ge2\). |
| [Three-power review](#three-power-review) | [Integral construction](../../ledger/Yin_L_G0464_v8.md#integral-sign-representative) | Polynomial integrality, signed layer norms and parity compression. |
| [Three-power review](#three-power-review) | [Arbitrary inputs](../../ledger/Yin_L_G0464_v8.md#arbitrary-input-lower-bound) | Orbit congruence, unit characterization and uniform terminal-block lower bound. |
| [Three-power review](#three-power-review) | [Terminal blocks and measure](../../ledger/Yin_L_G0464_v8.md#small-norm-terminal-block) | Parameter ranges, constructive norm budgets, strict endpoint and divergent whole measure. |
| [Three-power review](#three-power-review) | [Odd grid](../../ledger/Yin_L_G0464_v5.md#odd-grid-product) | Decreasing full list of nodes, the two grid polynomials and their residue weights. |
| [Three-power review](#three-power-review) | [Endpoint exponent](../../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Comparison with the necessary block growth in a shrinking shell. |
| [Three-power review](#three-power-review) | [Resultant ceiling](../../ledger/Yin_L_G0464_v6.md#norm-ceiling) | Comparison with the necessary normalized ceiling in the strict odd-grid chamber. |
| [Three-power review](#three-power-review) | [Gap count and lift](../../ledger/Yin_L_G0464_v1.md#positive-resolvent) | Nonempty sign blocks, left endpoint and multiplicative Mahler measure of the conjugate pair. |

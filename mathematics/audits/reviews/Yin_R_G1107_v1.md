---
author: Yin
---

# Coefficient height, prefix length and sampling tails on the full odd trace grid

<a id="height-review"></a>
## Independent review of the height obstruction and the prefix test

At 2026-11-08T03:45 an independent AI reviewer for Yin checked all four sections of [L464 v7](../../ledger/Yin_L_G0464_v7.md#height-escape), including the source application, both constants in the prefix bound and the finite probability example.
The argument establishes the stated height divergence and prefix bounds for whole monic integral lifts in the [strict odd-grid chamber](../../ledger/Yin_L_G0464_v5.md#odd-grid-product).
The conductor can be any odd integer \(p=2n+1\ge5\), and either type of exceptional trace roots is allowed.

**Cyclic coefficients.**
The nonzero characters \(j,-j\) on the full grid occur exactly once, and monic division gives integral moments for the proper part of \(WQ/B\).
Thus each weighted integer function has algebra norm exactly twice its weighted residue variation.
Expanding the two geometric series for each pole and using \(B^*=(1-z^p)/(1-z)\) gives the coefficient shift \(l+2\) after discarding the polynomial part for \(l\ge3\).
Taking a sufficiently large representative of each residue class completes the cyclic sum.
The Laurent multiplier \(D(z)D(1/z)\) is symmetric, so convolution has the same effect as multiplication by \(W(b_j)\) at both frequencies.
The Laurent support of \((1-z^2)(1-z)D(1/z)(DP)(z)\) lies in an interval of width at most \(p+4+2\deg D\).
For \(p>4+2\deg D\), at most two coefficients enter any one class, each bounded by \(4\|D\|_1H(DP)\).
Fixed small conductors cause no exception along a shrinking sequence, since bounded measure bounds the coefficients in each bounded degree.

**Rounding and height.**
The normalized transform in Section 1 and the hypotheses and conclusions of Lemma 10.2 agree in [Sanders's arXiv v5, pp. 1–2 and 43–44](../literature/San20/readme.md#arxiv-v5) and the [published paper, Sections 1 and 10](https://link.springer.com/article/10.1007/s00041-020-09732-y).
The lemma accepts a function close to integers, provided its nearest integer function is nonzero and the approximation error meets the stated threshold.
With \(e_0=\eta=2^{-N-3}\tau\), the residual error after \(j\) applications is at most \(2^je_0+(2^j-1)\eta<\tau/4\) for \(j\le N\).
At each unfinished step the nearest integer function of the residual is the previous one minus the coset sum, and the algebra norm drops by at least \(1/2\).
Since \(N=\lceil2M\rceil+1>2M\), iteration ends with zero rounded residual and \(\|I\|_A\le N B(M,\eta)\) by the norm-one coset calculation.
This checks the application of the published lemma at statement level.

For \(s\ge1\) the difference quotient of \((2+t)^s\) on \([-2,2]\) is bounded by \(s4^{s-1}\).
The first three trace identities bound \(\sum\mu_j=\sum b_jr_j-c\sum r_j\) uniformly when \(M(P)\le2\), by matching \(n-1\) disjoint real intervals, with one unmatched pole and two remaining roots of modulus at most \(5/2\).
This uses positivity of the weighted residues and permits every nonzero resultant in the chamber.
The fixed polynomial \(W(t)(2+t)^s\) is nonzero because \(D(z)D(1/z)\ne0\).
Whenever the proposed approximation error is at most \(e_{M_s}\), rounding bounds the corresponding variation, contrary to [C880 v2](../../claims/Yin_C_G0880_v2.md#statement) on any infinite shrinking subsequence.
The resulting eventual positive lower bound for \(H(DP)\delta^{h+1}\), together with \(0<\delta\to0\), gives \(H(DP)\delta^h\to\infty\) for every fixed nonzero \(D\) and integer \(h\ge0\).
Thus for each fixed height budget there is one positive shell width valid for every conductor and every joint law supported on that budget.
The proof gives a qualitative width.

**Prefix test.**
For the branch \(\sqrt{t^2-4}\sim t\), integration against the arcsine measure gives the polynomial part \(t-2x\) and the residue density \((b-x)^2d\alpha(b)\).
Agreement through \(L<p\) gives \(z(R_p-R_*)=O(z^{L+1})\) because \(p\ge L+1\), hence equality of moments through degree \(L-2\).
For \(m=\lfloor(L+1)/2\rfloor\), the test polynomial \((t-c)g^2\) has degree \(2m-3\le L-2\), and multiplication by \((t-x)^2\) gives exactly degree \(2m-1\), the last degree of exact midpoint arcsine quadrature.
At \(L=5\) one has \(m=3\), so two distinct nodes still survive.
The factors \(g(u_1),g(u_2)\) are nonzero and \(x\) can equal at most one node, including for \(x=\pm2\).
If \(c>u_2\) the weighted sum is strictly negative, contradicting \(\mu_j>0\).
Monotonicity of \(-2\cos\theta\) on \([0,\pi]\) gives \(k\le3p/(4m)\), and \(2-2\cos y\le y^2\) gives \(\delta\le9\pi^2/(4m^2)\).
This finite argument uses no Mahler or coefficient-height bound.

For the longest prefix capped at \(n+1\), compactness in the integer coefficient coordinates and the five possible coefficient limits force \(L\to\infty\) along a positive shrinking sequence.
Since \(m\ge L/2\), the finite estimate gives \(L\le3p/(2k)\), and the [exponent of \(k\)](../../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) therefore gives \(\log L/\log p\to0\).
The bound on \(\delta L^2\) then transfers height divergence to \(H(DP)/L^{2h}\).
At \(x\ne2\) there is a double pole at \(z=1\) and at most a simple pole at \(-1\), giving unbounded coefficients.
At \(x=2\) the cancellation gives \(1-3z+4z^2-4z^3+\cdots\).

**Finite probability example and limits.**
Replaying [J147 at degree 20](../../computations/programs/Yin_J_G0147/readme.md#replay) returned 850 strict-shell polynomials and precisely one in the chamber, with height four, one negative residue and absolute resultant 4313.
Under the stated independent uniform draws this one vector among \(9^{10}\) has probability \(9^{-10}\) at radius \(6/5\).
The uniform zero probability at sufficiently small radii follows from the deterministic gap, so independence plays no role in that assertion.
The five-profile classification and fixed-weight gap were checked at their stated interfaces, and the proof of Sanders's source lemma was outside this review.
The argument leaves the existence of a positive shrinking sequence with unrestricted heights unresolved.

<a id="tail-review"></a>
## Independent review of sampling at the logarithmic cut

At 2026-11-08T03:47 the independent reviewer for Yin checked both sections of [L464 v9](../../ledger/Yin_L_G0464_v9.md#rare-shell), using the height obstruction reviewed above.
For \(k=\lfloor p/\log p\rfloor\), the inequality \(2-2\cos u\le u^2\) gives \(\delta\le4\pi^2/(\log p)^2\).
For every fixed \(A>0\), a positive shrinking sequence with \(H(P)\le(\log p)^A\) would therefore satisfy \(H(P)\delta^h\to0\) for any integer \(h>A/2\), contradicting v7 with \(D=1\).
Bounded conductors cannot supply such a sequence, since bounded degree and measure give finitely many monic integral inputs.
This gives a deterministic shell width for each chosen \(A\).

Fix any \(b>0\) and choose \(A\alpha>\max(b,1)\).
For a sufficiently large odd conductor \(p\), a draw in this shell requires at least one free coefficient of magnitude greater than \((\log p)^A\).
The union bound over its coordinates uses only the uniform marginal tail hypothesis and yields \(C(p+1)\exp(-c_0(\log p)^{A\alpha})\).
Its logarithm is eventually at most \(-2(\log p)^b\).
For a deterministic sequence \(\varepsilon_p\downarrow0\), taking \(b=2\) puts the requested event inside that fixed shell for large \(p\), and \(\exp(-2(\log p)^2)<p^{-r}\) eventually for every fixed \(r>0\).
The same upper bounds hold with an additional resultant condition by event inclusion.

For up to \(\lceil\exp((\log p)^b)\rceil\) draws satisfying the same marginal bound, the stronger union estimate over all draws at \(p\) is eventually at most \(p^{-2}\), since \((\log p)^{A\alpha}\) dominates both \((\log p)^b\) and \(\log p\).
The first Borel–Cantelli lemma applies without independence across draws or conductors.
Almost surely only finitely many conductors contribute a success in the fixed shell, and each of those conductors has finitely many draws.
The infimum of all sampled admissible measures greater than one then exceeds one and can depend on the outcome, with infinite infimum for the empty sample set.

Under the distinct full-support mixture law, every specified finite coefficient vector at a conductor of positive mass has positive unconditional probability, the product of that mass and finitely many positive coordinate probabilities.
Conversely an empty strict event has zero probability, so at each fixed radius positivity is equivalent to existence, with the same equivalence for nonunit resultants.
In the per-conductor bound the coefficients are sampled without conditioning on chamber success.
For the mixture, \(\mathbb P(p\text{ drawn and shell success})=\mathbb P(p\text{ drawn})\mathbb P(\text{shell success}\mid p)\), and the preceding tail estimate applies to the second factor whenever the conditional coordinate marginals satisfy the uniform hypothesis.
Under any one fixed law, every outcome with \(M(P)>1\) eventually fails \(M(P)<1+1/j\), while an outcome with \(M(P)=1\) already fails strict positivity.
The decreasing sequence of strict events thus has empty intersection, and continuity from above gives probabilities tending to zero even when each event has positive probability.
Neither the upper tail bounds nor the existence equivalence supplies a witness at arbitrarily small radii.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Height and prefix review](#height-review) | independently reviewed |
| [Sampling-tail review](#tail-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Height and prefix review](#height-review) | [Height escape](../../ledger/Yin_L_G0464_v7.md#height-escape) | Fixed \(D,h\), every positive shrinking sequence and the uniform support consequence. |
| [Height and prefix review](#height-review) | [Cyclic coefficient identity](../../ledger/Yin_L_G0464_v7.md#cyclic-height) | Integral moments, exact character norm, support width and filtered height constant. |
| [Height and prefix review](#height-review) | [Rounding argument](../../ledger/Yin_L_G0464_v7.md#rounding) | Lemma 10.2, residual errors and the application to a fixed nonzero weight. |
| [Height and prefix review](#height-review) | [Prefix test](../../ledger/Yin_L_G0464_v7.md#prefix-cut) | Both finite inequalities, all five profiles and both asymptotic consequences. |
| [Height and prefix review](#height-review) | [Source lemma](../literature/San20/Yin_U001.md#near-integer-iteration) | Statement and application at normalized Fourier algebra norm. |
| [Height and prefix review](#height-review) | [Integral Fourier moments](../../claims/Yin_C_G0880_v1.md#fourier) | Monic division and integer trace polynomials for all cyclic indices. |
| [Height and prefix review](#height-review) | [Generating series](../../claims/Yin_C_G0880_v1.md#sparse-completion) | Geometric-series identity at \(t=z+z^{-1}\). |
| [Height and prefix review](#height-review) | [Weighted gap](../../claims/Yin_C_G0880_v2.md#statement) | Divergence for each fixed nonzero integral polynomial on a positive shrinking sequence. |
| [Height and prefix review](#height-review) | [Trace bounds](../../ledger/Yin_L_G0464_v5.md#fixed-radius-unit-magnitudes) | Only the first three trace sums, allowing all conductors and both types of exceptional roots. |
| [Height and prefix review](#height-review) | [Cut and coefficient limits](../../ledger/Yin_L_G0464_v5.md#only-left-endpoint) | Convergence to the left endpoint and the five possible subsequential limits. |
| [Height and prefix review](#height-review) | [Cut index exponent](../../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Logarithmic exponent one for \(k\) in the strict chamber. |
| [Height and prefix review](#height-review) | [Finite atom](../../computations/programs/Yin_J_G0147/readme.md#unique-input) | Degree-20 shell counts, actual coefficient height and probability under the specified law. |
| [Sampling-tail review](#tail-review) | [Rare-shell statement and proof](../../ledger/Yin_L_G0464_v9.md#rare-shell) | Fixed log cut, quantifiers in the shell and marginal bounds, and almost-sure sampling conclusion. |
| [Sampling-tail review](#tail-review) | [Full-support sampling](../../ledger/Yin_L_G0464_v9.md#positive-support) | Positivity versus existence at each radius, including the nonunit subevent, and convergence of fixed-law probabilities to zero. |
| [Sampling-tail review](#tail-review) | [Height divergence](../../ledger/Yin_L_G0464_v7.md#height-escape) | The case \(D=1\), used with any fixed integer \(h>A/2\). |

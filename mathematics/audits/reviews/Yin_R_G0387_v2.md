---
author: Yin
---

# Independent review of Frobenius matching in the ratio field

An agent outside the development of C162v2 reviewed the ratio-field inequalities, prior coverage and arbitrarily large measure construction for Yin on 2026-11-16T11:03 UTC.
The assignment identified the fixed text and its obligations before the first inspection, without development discussion or an earlier verdict.
The reviewer checked the mathematical arguments and their cited interfaces, identified an ambiguous quantifier in the historical comparison and rechecked the author's clarification against C483v1.

<a id="ramification-matching-review"></a>
## Norm bounds, growing degree and the finite-prime construction

Both coordinate projections of the ordered-pair orbit are equivariant surjections onto the transitive set of \(d\) roots, so each has fibers of size \(s\).
The same argument for the ratio map gives fibers of size \(sd/D\) over the embeddings of \(E=\mathbb Q(x^p/y)\).
Fixing the prime of the normal closure identifies the selected primes of \(E\) through restriction of embeddings, with local degree \(e_{\mathfrak q}f_{\mathfrak q}\) embeddings inducing each such prime.
Congruence is constant on each ratio fiber since the second coordinate is a unit.
This gives \(\beta=D^{-1}\sum e_{\mathfrak q}f_{\mathfrak q}\), including when some distinct values have the same reduction.
The ratio is a unit and has height at most \((p+1)m/d\) by subadditivity and invariance of height on conjugates.
If \(x^{pv}=y^v\), iterating an automorphism carrying \(x\) to \(y\) through its order \(j\) gives \(x^{v(p^j-1)}=1\), contradicting the hypothesis.

At a selected prime the normalized valuation of \(\rho-1\) is at least \(1/e_{\mathfrak q}\).
The two extreme terms and the \(p\)-divisibility of the intermediate binomial coefficients give the lower recurrence \(v(u^p-1)\ge\min(pv(u-1),1+v(u-1))\).
Its iteration gives \(v(\rho^t-1)\ge\min(1,t/e_{\mathfrak q})\) for every specified \(t=p^a\), including \(a=0\) and \(p=2\).
The rational norm is a nonzero integer whose \(p\)-valuation sums the normalized valuations with weights \(e_{\mathfrak q}f_{\mathfrak q}\).
The remaining local terms are nonnegative, which proves the \(B(t)\log p\) lower bound after division by \(D\).
At \(t=1\) the primes above \(p\) with a nonzero contribution are exactly the selected ones.

Set \(u=t h(\rho)\) and \(\tau=B(t)\log p>0\).
If \(u\le H_5(\tau)\), then \(u\le e^{-40}\) and monotonicity yields \(\Phi_5(u)\le \tau/2\) on both branches of the capped inverse.
The C147v5 upper bound on the complete cyclic norm in the original ratio degree contradicts the lower bound \(\tau\).
This proves the strict (1), irrespective of whether powering drops the degree.
Under the small-height premise of (2), the same upper bound at exponent one gives \(B(1)\log p\le\Phi_5((p+1)m/d)\).
The weighted harmonic mean satisfies \(e_{\mathrm h}/\beta=1/B(1)\).
The Frobenius graph contains \(\gamma d\) selected edges in this orbit, and each selected \(e_{\mathfrak q}\) divides \(e_L\) by the ramification tower in the normal closure.
Thus \(\beta\ge\gamma/s\) and \(e_{\mathrm h}/\beta\le e_Ls/\gamma\), in the required direction.
The least \(p\)-power \(t\) at least \(e_*\) satisfies \(t<p e_*\), even when \(e_*=1\), and gives \(B(t)=\beta\).
This proves (3).

The field \(\mathbb Q(x,y)\) has degree \(sd\) and contains \(E\).
Multiplying \(\rho^t-1\) by \(y^t\) gives \(x^{pt}-y^t\), and this unit factor has absolute rational norm one.
The two norm towers give the claimed absolute norm of the returned algebraic integer with multiplicity \(sd/D\).
Its product over the embeddings above \(\mathbb Q(x)\) has \(s\) factors, hence total conjugate exponent at most \(spt\).

At fixed \(p\), substitution of \(\tau=(\log p)/k\) in the small-argument asymptotic for \(H_5\) gives (4), including the positive third power of \(\log\log k\) and the negative fifth power of \(\log k\).
With \(e_*=1\) and \(k\le d^{1/2-\epsilon}\), the factor \(d/k^2\ge d^{2\epsilon}\) dominates the logarithmic loss.
For the Frobenius orbit, monotonicity permits the weaker inputs \(s/\gamma\ge k\) and \(e_L\ge e_*\) directly in (3).
The former full-resultant floor \(p^d\) over \(d^2\) pairs contributes \((\log p)/d\) in that normalization, while the older single-orbit bound powered to \(D\) uses \(D\le sd\).
The comparison now distinguishes the independent-pair rank-two estimate from the earlier all-pair bound, which at fixed \(p\) requires bounded \(s\) and a uniform positive lower bound for \(\gamma\).
For a dependent pair, equal positive heights make the two nonzero exponents in a dependence relation equal in absolute value, so \(y=\zeta x^{\pm1}\).
At a reciprocal endpoint with all positive powers degree-preserving, both possible comparison roots \(x^{\pm1}\) are present and raising to the order of \(\zeta\) is injective on the roots.
The cited descent ensures existence in its small-measure domain and supplies no persistence of the original local orbit.

For every \(p\) in the finite set, an element \(\lambda\) of order \(p^\ell+1\) exists in the cyclic group of order \(p^{2\ell}-1\).
Every proper subfield has degree \(j\mid 2\ell\) with \(j\le\ell\), and its multiplicative order \(p^j-1\) is too small to contain \(\lambda\).
Conjugation by the \(\ell\)-th Frobenius power gives inversion, so \(v=\lambda+\lambda^{-1}\) has degree at most \(\ell\) and at least \(\ell\) by the quadratic trace equation.
The degree \(2\ell\) monic reciprocal lift of the minimal polynomial of \(v\) vanishes at \(\lambda\) and is therefore its separable minimal polynomial, also at \(p=2\).
At \(q\) there are enough linear roots away from \(\pm2\) to realize the prescribed quadratic and \(\ell-2\) linear factors.
At \(q'\) the two fixed elements of inversion are excluded from each of the split and nonsplit tori.
Inversion then gives \((q'-3)/2\) split and \((q'-1)/2\) nonsplit traces, disjoint because each trace determines the unordered pair of quadratic roots.
The size hypotheses supply all required choices, and coefficientwise CRT preserves monicity.
Squarefreeness gives distinct reductions of all roots, making inertia trivial by its faithful action on the splitting field's roots.
Residue Frobenius consequently has the prescribed factor cycles, while irreducibility at any designated prime proves irreducibility over \(\mathbb Q\).

On the \(\ell\) reciprocal blocks the Galois group contains an \(\ell\)-cycle and a transposition.
Translating the transposition by the cycle gives edges of a fixed nonzero step in \(\mathbb Z/\ell\mathbb Z\), so their graph is connected and they generate \(S_\ell\).
The Frobenius at \(q'\) flips exactly the one nonsplit block.
Conjugation supplies every coordinate flip and therefore the entire wreath group.
The orbital sizes for equality, inversion and different blocks are \(d,d,d(d-2)\).
At each designated \(p\) distinct reductions specify exactly one compatible partner for each root, and the block cycle places all \(d\) edges in the last orbit.
Thus the only positive density is \(1/(d-2)\).
Changing the constant of the trace polynomial by multiples of the CRT modulus preserves these data and makes some trace arbitrarily large in modulus by the product of its roots.
A trace of modulus \(R\) has a reciprocal lift of modulus at least \(R/2\), proving the asserted unbounded logarithmic Mahler measure and providing nontorsion examples.

The statement, proof and comparisons pass at these scopes.
The construction rules out a universal square-root matching bound at a prescribed finite pool across all units.
The existence of sufficiently favorable local data at small original measure remains open.

<a id="bounded-coefficient-check"></a>
## Fixed auxiliary primes and bounded coefficients

On 2026-11-16T11:06 UTC the same reviewer checked the added bounded-coefficient assertion and its proof for Yin.
The coordinating author had supplied a mathematical summary of the strengthening before the reviewer read its fixed text.
This check therefore has a self-reviewed relationship under the project rules.

With \(n=\ell-2\) odd and at least three, distinct irreducibles of degrees \(2,n\) over the fixed \(q\) give a block permutation whose \(n\)-th power is a transposition.
At the second fixed prime \(q'\), the split and nonsplit linear traces are distinct and avoid \(\pm2\), with both types available for \(q'\ge7\).
A generator \(u\) of the multiplicative group of \(\mathbb F_{q'^n}\) lies in no proper subfield by its order.
Its degree over its trace field divides \(n\) and is at most two, hence equals one.
If Frobenius to the power \(j\) took \(u\) to \(u^{-1}\), then \(n\mid 2j\), hence \(n\mid j\), which would force \(u^2=1\).
The two lift cycles are therefore disjoint and each has length \(n\).
The \(n\)-th power of residue Frobenius at \(q'\) fixes them pointwise and keeps the one nonsplit linear flip, yielding the same wreath group and matching density.
All new local polynomials are squarefree, so the earlier unramified Frobenius argument applies.

The common CRT modulus \(N\) is independent of \(\ell\).
The specified half-open interval has length \(N\) and contains a representative of each residue class at the symmetric positions \(1,d-1\).
All remaining interior coefficient classes admit representatives of absolute value at most \(N\).
The recurrence for \(z^j+z^{-j}\) in \(z+z^{-1}\) gives back the monic integral trace polynomial.
At \(2\), the coefficients of degrees \(0\) to \(d-2\) are all bounded above by \(N\), including the negative linear coefficient.
After division by \(2^{d-1}\) their contribution is at most \(N(1-2^{-(d-1)})\).
Thus \(P(2)<0\) and monicity gives a real root greater than two.
Jensen's formula followed by the circle mean-square bound and orthogonality gives \(M(P)\le\|P\|_2\le (4N+4)\sqrt{d+1}\), where the norm is the Euclidean norm of its coefficients.
The irreducible polynomials therefore have \(m>\log 2\) and \(h=m/d\to0\) with bounded coefficients and the same sparse matching.
This check found no further mathematical issue.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Ratio bounds and arbitrarily large measure family](#ramification-matching-review) | independently reviewed |
| [Bounded-coefficient family](#bounded-coefficient-check) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C162v2 statement](../../claims/Yin_C_G0162_v2.md#statement) | Every orbit with positive compatible mass, all \(p\)-power exponents, the harmonic mean and strict gap, growing degrees and all designated prime sets. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C162v2 local argument](../../claims/Yin_C_G0162_v2.md#local-proof) | Constant fibers, local degrees and depth, capped inverse and original-field norm tower. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C162v2 degree range](../../claims/Yin_C_G0162_v2.md#degree-range) | Fixed-prime asymptotic, quantitative prior coverage and the dependent-pair endpoint comparison. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C162v2 construction](../../claims/Yin_C_G0162_v2.md#finite-pool) | Simultaneous congruences including characteristic two, separability, ramification, full Galois group, unique density and arbitrarily large measure. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C147v5 cyclic norm](../../claims/Yin_C_G0147_v5.md#statement) | Full numerator in the original ratio degree, monotone upper modulus, capped inverse and asymptotic at zero. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C477v1 pair fields](../../claims/Yin_C_G0477_v1.md#statement) | Pair and ratio degrees, constant fibers, nontorsion, absolute height and the full mixed-resultant floor. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C162v1 orbital norm](../../claims/Yin_C_G0162_v1.md#argument) | Earlier exponent and Frobenius matching, original-field return and conjugate exponent cost. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C256v1 ideal norm](../../claims/Yin_C_G0256_v1.md#content-versus-ideal-norm) | Exact valuation with residue-degree weights in the ratio field. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [The26b local interface](../literature/The26b/Yin_U001.md#the26b-u001) | Decomposition, local degrees and residue-Frobenius lifts at the recorded source scope. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [Hun74 finite fields](../literature/Hun74/Yin_U006.md#hun74-u006) | Finite-field degrees and Frobenius cycles at the recorded source scope. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C231v1 descent](../../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Existence, small-measure reciprocity and injectivity on roots for each positive power of the endpoint. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C483v1 rank and dependence](../../claims/Yin_C_G0483_v1.md#independent-and-dependent-pairs) | Rank-two height bound and the equal-height dependence calculation. |
| [Ratio bounds and large-measure family](#ramification-matching-review) | [C483v1 prior coverage](../../claims/Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Scope and hypotheses of the previous all-pair residue-mass and independent-pair estimates. |
| [Bounded-coefficient family](#bounded-coefficient-check) | [C162v2 statement](../../claims/Yin_C_G0162_v2.md#statement) | The added bounded-coefficient family, vanishing absolute height, strict lower bound for total measure and fixed-prime compatibility. |
| [Bounded-coefficient family](#bounded-coefficient-check) | [C162v2 construction](../../claims/Yin_C_G0162_v2.md#finite-pool) | The final construction with fixed auxiliary primes, odd-cycle powers, direct coefficient lifts and the two-sided measure bound. |
| [Bounded-coefficient family](#bounded-coefficient-check) | [Hun74 finite fields](../literature/Hun74/Yin_U006.md#hun74-u006) | Finite-field degrees and factor cycles at both fixed auxiliary primes. |
| [Bounded-coefficient family](#bounded-coefficient-check) | [The26b local interface](../literature/The26b/Yin_U001.md#the26b-u001) | Squarefree reduction, unramified primes and residue Frobenius at the stated scope. |

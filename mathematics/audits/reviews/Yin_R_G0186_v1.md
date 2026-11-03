---
author: Yin
---
# Primitive prediction cofactors and minimal integer normalizers: independent whole-proof review

Date and human attribution: 2026-10-11T11:16.
Human record author Yin; mathematical inspection by the separately assigned assess_bv19b_current AI reviewer.
No personal human proof reading or formal verification is asserted.

## Arrangement, input sequence and exact artifact

This is an initial whole-proof review of [D_G0009](../../ledger/Yin_L_G0363_v1.md), the root-authored 2026-10-11 revision frozen through Sections1--5, equations(1)--(11), ending with its complete author self-check and pending-review notice.
The reviewer supplied none of the rational-optimizer scout, primitive-cofactor/cokernel derivation, denominator-divergence proof or exact all-s cancellation.
The separate scout's contribution and root's subsequent derivations are explicitly credited in the draft and were not treated as independent review.

The reviewer shares G0001 conversation/repository context with the author.
It previously performed the actual whole-proof D_G0005 inspection recorded in R256 and its repair closure R257, and has authored separate arithmetic quotient/moment drafts D_G0002/D_G0006.
These roles are disclosed; they did not contribute to D_G0009's derivation.
The review assignment specified the obligations to emphasize.
No scout proof-generation dialogue or additional author derivation was consulted before forming the present findings.
The current draft itself, including its self-check, was read in full; self-check statements were not substituted for reconstruction.

Before the freeze the reviewer refreshed [L359](../../ledger/Yin_L_G0359_v1.md#integer-multiplier-variational-formula), the fixed successor of the D5 account it had actually reviewed, and the earlier [L4 finite Toeplitz boundary](../../ledger/Yin_L_G0004_v1.md#degree-window-tests).
The complete current D9 proof was then checked forward and backward.
The necessary direct Mahler/Jensen, coefficient norm and fixed-input circle-zero approximation interfaces retain the exact inspection scope in the prior D5 review and fixed L359.
No original Szego proof, old computation or external source search is part of this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof outcome](#primitive-normalizer-whole-proof-outcome) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof outcome](#primitive-normalizer-whole-proof-outcome) | [D9 exact optimizer and primitive normalizer](../../ledger/Yin_L_G0363_v1.md#primitive-prediction-normalizer) | Complete Section1: full integer positive Gram matrices, rational optimizer, cofactor indexing, least denominator and strict closed-disk root exclusion including circle zeros of P. |
| [Whole-proof outcome](#primitive-normalizer-whole-proof-outcome) | [D9 cokernel denominator identity](../../ledger/Yin_L_G0363_v1.md#cokernel-denominator-identity) | Complete Section2: exact selected cokernel element order, Smith/cardinality distinction, primitive energy and necessary divisibility with its nonconverse scope. |
| [Whole-proof outcome](#primitive-normalizer-whole-proof-outcome) | [D9 normalizer divergence](../../ledger/Yin_L_G0363_v1.md#normalizer-divergence) | Complete Section3: fixed-input residual convergence from L359 approximation, strict finite nonattainment, finite-rational-value proof of k_n tending to infinity and all scope limits. |
| [Whole-proof outcome](#primitive-normalizer-whole-proof-outcome) | [D9 cyclotomic cofactor cancellation](../../ledger/Yin_L_G0363_v1.md#cyclotomic-cofactor-cancellation) | Complete Sections4--5: every n=sL+r, all block counts and wraparound cases, exact optimizer/minimal k/gcd/energy, moving-window exponential cancellation and non-gap/non-novelty boundaries. |
| [Whole-proof outcome](#primitive-normalizer-whole-proof-outcome) | [L359 multiplier representation](../../ledger/Yin_L_G0359_v1.md#integer-multiplier-variational-formula) | Direct input: Jensen lower inequality, strict finite nonattainment and fixed-input rational zero-free approximation, with circle-root and denominator/rate limits as independently inspected in R256/R257. |
| [Whole-proof outcome](#primitive-normalizer-whole-proof-outcome) | [L359 exact cyclotomic control](../../ledger/Yin_L_G0359_v1.md#cyclotomic-exact-window-normalizer) | Comparison and supporting residue-chain mechanism only; the changed real optimizer and cofactor/cokernel formulas in D9 were independently derived here. |

## Reconstructed obligations and decisive checks

### 1. Actual Gram object, minimizer and cofactor index

For nonzero integer P, B=|P|^2 is real and positive except at finitely many circle zeros.
Every finite polynomial coefficient Gram form is positive definite.
Its Fourier entries are integer real autocorrelations; no squarefree, monic, nonzero-constant or bounded-inverse assumption is needed.
All G_n are therefore invertible, with positive integer D_n.

The finite complex affine minimizer is unique by strict convexity.
The normal equations set every positive-coordinate component of G_(n+1)q to zero.
Hence q is G_(n+1)^(-1)e0 divided by its positive zeroth coordinate.
The trailing n-by-n section is exactly G_n by translation invariance of the circle inner product.
Thus the zeroth cofactor is D_n, and q_n=adj(G_(n+1))e0/D_n.
Multiplication by q's coefficient vector gives residual energy D_(n+1)/D_n.
This independently verifies the indexing in(1), which differs by one from a notation starting residuals at the first Toeplitz ratio.

With v0=D_n>0, the positive gcd g of the complete integer cofactor vector divides D_n.
To clear the rational vector v/D_n, an integer k must satisfy D_n dividing kv_j for every j.
Prime by prime, the least such k is D_n/gcd(D_n,v1,...,vn)=D_n/g.
This covers zero cofactors and any vanished trailing coefficient.
Dividing v by g gives a primitive complete integer coefficient vector and positive constant k.
The separate n=0 convention q0=Q0=1,k0=1 is correct.
A monomial P is harmless here: B is constant, all off-diagonal correlations vanish and k_n=1, as expected.

### 2. Strict root exclusion without a spectral lower bound

For a root zeta of q_n, write q_n=(z-zeta)a.
The polynomial za lies in the span of z,...,z^n; orthogonality gives0=||a||_B^2-zeta<a,za>_B.
Circle multiplication is an isometry, so both norms in Cauchy--Schwarz are||a||_B.
Equality would force za to be a constant multiple of a B-almost everywhere.
Since B>0 almost everywhere and a is nonzero, that would make a nonzero polynomial vanish at infinitely many circle points.
It is impossible.
Thus |<a,za>_B|<||a||_B^2, its denominator is nonzero by the displayed identity, and |zeta|>1.
The root-free condition is strict on the closed disk; circle zeros of P do not impair it.
A constant q_n has no roots and meets the condition vacuously.
This supplies exactly the O_(k_n) membership required by L359.

### 3. Cokernel element, group size and energy divisibility

Partitioning the full Gram matrix gives lower block T_n=G_n and the exact remaining coefficients-T_n^(-1)b.
In A_n=Z^n/T_n Z^n, an integer k kills[b] if and only if kT_n^(-1)b is integral.
Thus its element order equals the least normalizer just proved, including order1 for the zero class.
A finite Smith decomposition implies that the element order divides the largest invariant factor and the group cardinality D_n.
It need not equal either.
These are classical integer linear algebra consequences; no new external theorem estimate is invoked.

Since Q_n=k_n q_n, its complete coefficient energy is k_n^2 D_(n+1)/D_n=D_n D_(n+1)/g_n^2, a positive integer.
Reducing the residual fraction shows that D_n/gcd(D_n,D_(n+1)) divides k_n^2.
The draft correctly states this only as a necessary condition: it does not recover k_n from the reduced residual denominator or confuse cardinality with exponent.
Scalar content is retained in P and Q_n throughout.

### 4. Residual limit and the entire fixed-input divergence argument

The affine spaces increase, so r_n is weakly decreasing.
Zero-freeness and L359's Jensen inequality give r_n>=M(P)^2.
L359 supplies, for this fixed P including its circle zeros, finite-degree rational zero-free trials with constant1 and energies arbitrarily close to that lower value.
Once the degree fits, minimization gives at most that trial energy at every later n.
This proves convergence without requiring a quantitative Szego rate.

For nonmonomial P, every finite r_n is strictly above M(P)^2 by the already checked nonattainment mechanism.
If k_n<=K for a fixed positive integer K, r_n lies in the finite set of values E/k^2 with integer1<=k<=K and positive integer E<=K^2 r0.
Intersecting with actually attained values gives a finite set strictly above the limit, so convergence excludes it after some index.
This proves k_n tending to infinity, not merely unboundedness.
It does not assume rationality of M(P)^2, strict decrease of the residuals, or monotonicity of k_n.
The proof applies to every fixed nonmonomial P, including cyclotomic or scalar-content examples, and no uniform rate follows.

### 5. Every residue-chain index and the exact all-s cancellation

For P=1-t^s, Gram entries are2 on the diagonal and-1 exactly at lag s.
Permuting coefficient indices modulo s gives tridiagonal blocks.
A block of length j has determinant j+1, including j=0 with determinant1.
For n=sL+r,0<=r<s, precisely r blocks have length L+1 and s-r have length L.
This gives D_n=(L+2)^r(L+1)^(s-r).
When r<s-1, increasing r by one gives ratio(L+2)/(L+1).
At the wraparound r=s-1, D_(n+1)=(L+2)^s and D_n=(L+2)^(s-1)(L+1), giving the same ratio.
The n=0 case also gives D0=1,D1=2.

The optimizer of degree<=n has exactly L+1 coefficients available in residue chain0; other chains add positive energy independently and have zero minimizing coefficients.
On the active chain the real differences sum to1 and there are L+1 of them after the fixed initial coefficient.
Their unique minimum uses equal differences1/(L+1).
Thus q_n has coefficients1,L/(L+1),... ,1/(L+1) in powers t^s.
For L>=1 the final coefficient proves the least denominator L+1, while L=0 gives q=1,k=1.
This checks(10) independently of a presumed cofactor gcd.

Combining with the already proved identity g_n=D_n/k_n gives(11); the primitive polynomial has product energy(L+1)^2+(L+1)=(L+1)(L+2).
At n=s one indeed has D_n=2^s,k_n=2,g_n=2^(s-1).
The determinant may grow exponentially in this moving window while the actual normalizer stays2.
This example is entirely cyclotomic and reducible for s>1.
The draft properly restricts the obstruction to determinant-integrality-only reasoning and does not claim to refute a noncyclotomic-specific theorem.

<a id="primitive-normalizer-whole-proof-outcome"></a>

## Whole-proof outcome and limits

**Pass at the stated complete restricted scope.**
No actionable mathematical defect, index error, hidden spectral separation or uncharged denominator assumption was found in the frozen Sections1--5 and equations(1)--(11).
The proof identifies the actual optimal normalizer with one finite Gram-cokernel element order, proves fixed-input divergence, and exhibits exact large cofactor cancellation across every positive integer s and every window n.
These conclusions are sufficient for the recorded bounded exploration account, not for G0001 completion.

The circle-root approximation and ordinary Jensen interfaces retain their accepted/local independent-review limits; no new source result, historical priority or full Toeplitz-source re-audit is certified.
Classical finite prediction and Smith form are recognized as such.
No normalizer-rate bound uniform in input or degree, no irreducible near-one control, no numerical parameter run, and no uniform Mahler lower gap is supplied by this review or the argument.
The residuals remain upper estimates for M(P)^2, and the draft preserves that direction.
No program, new J, formal verification or original computation rerun was needed.

This fixed finding covers the exact frozen author account identified above.
A later substantive extension of the cokernel, zero-free, normalizer-growth or cancellation statement needs review at its actual changed scope.

## Actual relationship clarification

The recorded reviewer read the complete target author account including its self-check before the initial findings.
That actual exposure makes the whole relationship SELF; absence of proof contribution does not establish isolation.
The exact original date, complete finding, mathematical/source scope and all bindings remain unchanged.

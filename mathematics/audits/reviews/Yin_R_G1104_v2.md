---
author: Yin
---

# Independent review of the fixed-template factor bounds and the dyadic application

<a id="general-template-whole"></a>
## Finding on C879 v2

At 2026-11-07T17:58 UTC an independently assigned reviewer for Yin found that both factor bounds and the dyadic application follow under the hypotheses of [C879 v2](../../claims/Yin_C_G0879_v2.md#statement).
The reviewer did not participate in proof development and received no development discussion or author explanation.
The fixed proof and its cited mathematical inputs were available, including the assessments embedded in those inputs.
After checking the present deductions, the reviewer consulted the [earlier quadratic finding](Yin_R_G1104_v1.md#fixed-template-whole) and the [review of the arithmetic input](Yin_R_G1086_v1.md#raw-p2-whole) for their respective scopes.

For each outer coefficient \(A\), \(M(A)=1\) forces a unit leading coefficient and all roots into the closed disk.
After removing the zero roots, the modulus of the remaining constant term is at least one and equals the product of the root moduli, so every remaining root lies on the circle.
For \(N\) greater than all the coefficient degrees, the occupied degree blocks of \(A_j(z)z^{jN}\) are disjoint.
The normalized specialization therefore has unit leading and constant terms and degree \(sN+\deg A_s-\operatorname{ord}_0 A_0\).
The bounded coefficient one-norm and unit endpoints give the stated fixed annulus by applying the root bound in both directions.

For \(r>1\), dividing the lower powers by \(|w|^{s-1}\) leaves terms of modulus at most the corresponding coefficient moduli.
For \(r<1\), factoring \(|w|\) from the upper powers has the same effect.
Each division uses the appropriate outer coefficient away from its nonzero roots.
On the fixed annulus, \(|r-1|\gg_F|\log r|\) and the angular chord to any unit-circle zero is at least \(2\delta/\pi\).
These give the claimed product lower bound for each denominator with its own multiplicities, using \(\min(1,\max(v,\delta))\) in every factor.
The degrees can consequently be bounded by their maximum on both sides of the circle.
The cutoff \(v=1/N\) covers a root on a pole ray, and unit-circle roots contribute zero even at common zeros of all the coefficients.
Constant or monomial outer coefficients have an annular lower bound directly, including when both pole sets are empty.

In the [sector estimate](../../claims/Yin_C_G0879_v1.md#angular-count), a rotation on each zero-free bounding ray gives a nonzero real-part polynomial with at most \(L\) terms.
Its at most \(L-1\) positive zeros cut the ray into at most \(L\) half-plane intervals, each with net argument change of magnitude at most \(\pi\).
The argument principle with the outer and inner circular arcs gives the angular count with multiplicity, and outward perturbations include boundary rays.
Summing over the fixed pole directions bounds the tail by \(O_F(Ne^{-u}+1)\) for \(0<u\le\log N\).
The integrated constant contributes \(O((\log N)^j)\) to the \(j\)-th moment of the cutoff, absorbed in \(O_F(N)\) for \(j=2,3\).
After dividing the radial bounds by \(N^j\), coefficient conjugation doubles the resulting whole-root moment sums for the norm.

A positive rational irreducible monic factor of that integral norm has constant term \(\pm1\) and all its conjugates are nontorsion units.
The accepted [C855 v2, Part A](../../claims/Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04) counts each rational embedding, so it yields \(\sum v_\alpha^2\ge1/(10d)\) at the actual degree \(d\) of this factor.
This input was checked at its adopted statement and application scope, without a fresh review of its original arithmetic or capacity proofs.
The whole-root second-moment bound implies \(d\gg_F N\).
For the measure estimate one uses the upper bound \(d\le BN\) from the norm degree.
Since the root moduli multiply to one, Cauchy–Schwarz gives \((10BN)^{-2}\le(\sum v_\alpha^2)^2\le2m(f)\sum v_\alpha^3\).
The upper bound \(C_3/N^2\) for the last sum gives \(m(f)\ge1/(200B^2 C_3)\), allowing a positive choice of \(C_3\).
For a Gaussian irreducible monic \(g\), the rational minimal polynomial of a root divides \(g\bar g\) and contains every distinct coefficient conjugate of \(g\).
It is thus \(g\) or \(g\bar g\), divides the norm, and has positive logarithmic measure with degree and measure each at most twice those of \(g\).
The omitted scalar unit and zero roots have zero logarithmic measure.

Substitution of \(N=n/2\) into the displayed template gives exactly the six terms of the [dyadic completion](../../ledger/Yin_L_G0458_v5.md#dyadic-rational-rotation).
Both endpoints have multiplicative measure one, and each rational factor of \(Q_n\) divides the rational specialization and its coefficient norm.
The finitely many excluded small \(k\) contribute finitely many positive factor measures and degree-to-\(n\) ratios, each strictly positive.
Every integral divisor has leading coefficient \(\pm1\) because \(Q_n\) is monic, so a positive divisor has at least one positive irreducible constituent and all other constituents have nonnegative measure.
The claimed lower bound on all such divisors follows.

For a complete cubic orbit, averaging the six terms leaves just the constant and \(z^{N+1}\) when \(n\equiv1\bmod3\), or the constant and \(z^{2n+2}\) when \(n\equiv2\bmod3\).
These exhaust powers of two and give a positive power of each orbit member equal to one.
The example \(V(z)=z-2\) gives the two roots \(2\omega,2\omega^2\) of the rotated product, demonstrating that a partial orbit is possible.
Other choices of \(V\) can give all three orbit members, for example \(V(z)=z^3-8\).
The constants depend on the template, and the irreducibility of \(Q_n\) lies outside the finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#general-template-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#general-template-whole) | [C879 v2 statement](../../claims/Yin_C_G0879_v2.md#statement) | Fixed templates of every positive degree in the specialization variable, both coefficient fields and both bounds on each positive factor. |
| [Whole finding](#general-template-whole) | [C879 v2 radial bounds](../../claims/Yin_C_G0879_v2.md#outer-coefficient-bound) | Unequal measure-one endpoints, normalization, the uniform annulus and both radial regimes including degenerate pole sets. |
| [Whole finding](#general-template-whole) | [C879 v2 moments and factors](../../claims/Yin_C_G0879_v2.md#all-roots-to-factors) | Sector count and moment sums, arithmetic input, factor bounds and Gaussian field passage. |
| [Whole finding](#general-template-whole) | [C879 v2 dyadic application](../../claims/Yin_C_G0879_v2.md#dyadic-application) | Completion, all small and large indices, positive integral divisors, the two residues in the cubic orbit calculation and the partial-orbit example. |

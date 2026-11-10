---
author: Yin
---

# RS03: correlated proposals and reciprocal coordinate descent

<a id="rs03-u001"></a>
## Inspected scope

Use the [identified five-page author upload](readme.md#author-upload).
The reading covers Sections 2--4, printed pages 458--461, with the abstract and contents on page 457.
This is direct inspection of the online PDF's extracted text, with the visual/index limitation below; it is not reproduction of the computations or an independent proof review.
No new theorem or historical completeness claim is adopted.

<a id="statistical-proposal"></a>
## Statistical proposal

Section 2 proposes a multivariate-normal draw for the free half-coefficients of monic reciprocal polynomials of even degree, centered at the coefficients of \(x^{2n}+1\).
Its heuristic covariance has diagonal entries 0.22; the full matrices are relegated to external resources not inspected here.
The inspected paper does not specify how continuous draws become integers.
It removes cyclotomic factors and also examines irreducible factors.
Reported high-degree hits concentrate near then-known limit points, and the search extends to degree 300.

<a id="reciprocal-neighborhood"></a>
## Reciprocal coordinate neighborhood and actual seed dependence

**Definition (reciprocal coefficient neighborhood, in explicit paired-index notation).**
For \(n\ge1\) and \(a\in\mathbb Z^n\), write the monic reciprocal integer polynomial of degree \(2n\) as
\[
 P_a(x)=x^{2n}+1+\sum_{i=1}^{n}a_i b_i(x),\qquad
 b_i(x)=x^i+x^{2n-i}\ (i<n),\qquad b_n(x)=x^n.
\]
This is the independent-coefficient convention for the source's verbal instruction to change a coefficient and its reciprocal mate together.
Its one-coordinate neighborhood is \(P_a+\delta b_i\), with \(\delta=\pm1\), also allowing \(\pm2\) at degrees at most 40.
Section 3 evaluates all neighbors, keeps a minimum-measure polynomial and repeats until unchanged.
For restarts, it alters a known small-measure seed's central coefficient: nonzero becomes zero, and zero becomes one.
Seeds come from the existing list or Section 2's search.
The source warns of local minima and reports high-degree discovery yield about one tenth of its statistical method, without an equal-budget comparison.
The degree-ten examples recover Lehmer's known value.

The extracted displayed formula on printed page 459 has \(x^{n-i}+x^i\) for a stated degree \(2n\).
That pair is not reciprocal at degree \(2n\); the formula above follows the surrounding verbal instruction and uses \(2n-i\).
Without a successful rendered-page check, this is an unresolved extraction/typesetting ambiguity, not a confirmed author error.
An implementation must state its actual paired indices, treatment of equal measures, inclusion of the current point and numerical comparison rule rather than silently treating those choices as reproduced source code.

<a id="positive-core-boundary"></a>
## What transfers, and the first unsupported step

The paired move is an exact integer operation and its definition is usable independently of the missing Gaussian rounding rule.
At fixed degree, testing all \(2n\) unit-step neighbors consumes \(2n\) measure evaluations before any selected move; allowing both step sizes doubles this count.
Thus a comparison with a one-proposal mutation control must charge evaluations, not just iterations or accepted outputs.
Changing one pair supplies no reason for a new positive measure or a new noncyclotomic core.
A descent objective equal to total \(M\) also rewards neutral outputs with \(M=1\); a nonneutral selection policy would be an additional design choice.

A whole-output success in \(1<M(P)<1.2\) and a small factor extracted from a larger-measure parent are different observations.
The latter can be useful arithmetic input, but it needs the factor's own identity, degree, measure and parent cost.
Removing cyclotomic factors preserves measure; extracting an arbitrary noncyclotomic factor need not do so.
The first unsupported experimental step is whether seed perturbation plus charged coordinate descent finds a previously unseen nonneutral core in the desired whole-output shell more often than the specified mutation control under the same seeds and budget.
A useful comparison must retain the unmodified seed and raw offspring, count neutral or return-to-seed outcomes, and separate known-core recovery from genuinely different factor/core identities.
Neither the source's high-degree list growth nor its recovery of a familiar small value establishes that step, much less a sequence with positive total logarithmic measure tending to zero.

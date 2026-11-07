---
author: Yin
---

# Searching for positive Mahler measures in reciprocal integer polynomials

The objective is to construct monic integer polynomials with \(0<m(P)=\log M(P)\to0\).
Three delegates developed the factor, trace-root and coefficient-prefix routes for Yin in this bounded strategy investigation on 2026-11-07.
The [coefficient-box support criterion](../claims/Yin_C_G0870_v1.md#statement) identifies a positive integer count in each shrinking shell as sufficient.
The following searches retain the unnormalized cost and give different meanings to their finite controls.

<a id="factor-reconstruction"></a>
## Finding a small integer factor by its binary reduction

Use the [odd-prime square family](Yin_L_G0458_v4.md#prime-square-family-inputs) \(H_p\), which has no cyclotomic factors.
For \(p>5\) each irreducible factor of degree \(e\) satisfies
\[
 e\log(2)/(16p)<m(f)\le9e\log(2)/(2p-10).
\]
Consequently producing an actual factor of degree \(o(p)\) along an unbounded prime sequence is equivalent to producing a counterexample sequence within this family.
This uses the [complete original-factor estimate](Yin_L_G0458_v4.md#prime-square-sublinear-factor-criterion).
For a reducible divisor \(F\) the upper bound still holds with \(e=\deg F\) by addition over factors, and its measure is strictly positive.
Changing the source polynomial avoids the [fixed-unit substitution obstruction](Yin_L_G0450_v1.md#unit-ray-saturation).
[C877](../claims/Yin_C_G0877_v1.md#statement) proves that \(H_p\) is irreducible over \(\mathbb Q\) for all sufficiently large primes, so its only nonconstant monic integral divisor then has degree \(8p-6\).
Thus this family cannot realize the \(o(p)\) criterion, and its nonconstant monic integral divisors have a uniform positive lower bound on \(m\).
The proof gives no numerical irreducibility threshold.

[C871](../claims/Yin_C_G0871_v1.md#statement) gives indivisible multiplicity-eight binary Frobenius blocks.
For a reciprocal factor, inversion pairs distinct orbits if \(\rho=\operatorname{ord}_p(2)\) is odd.
Using the rational exponent \(7/30\) for a target \(M<2^{7/30}\), the sufficient height test is \(270e<7(2p-10)\).
It forces reciprocity for every qualifying irreducible input by the [Smyth threshold](../claims/Yin_C_G0870_v1.md#source-interfaces).
At \(p=2113\) the former degree candidates 88 and 90 violate the block restriction.
The original [degree screen](../computations/programs/Yin_J_G0145/readme.md) tested all primes \(7\le p\le13367\) and retained \(8191\) and \(13367\) for this sufficient height test.
This scope allows smaller actual measures at degrees outside the test.
At \(p=8191\), \(\rho=13\), and the 630 primitive binary irreducibles of degree 13 form 315 unordered pairs under inversion.
Candidate original degrees are \(208,210,416,418\).
The corresponding trace degrees are \(104,105,208,209\), but the following search works on the original reciprocal polynomial.

For \(e=208\) the binary candidate consists of the eighth powers of the two members of a single such pair.
For \(e=210\) include the binary endpoint block \((z+1)^2\).
There are exactly 315 choices of reduction in each degree.
For \(416,418\) use two distinct pairs, giving \(\binom{315}{2}=49455\) choices in each degree before arithmetic filters.
Each candidate \(b\) is coprime in \(\mathbb F_2[z]\) to \(\bar H_p/b\), even though \(b\) has multiple roots.
The monic coprime split lifts uniquely modulo \(2^k\) at every precision.
Indeed at a one-bit lift, the corrections to the two factors have degrees below the respective monic degrees and solve a linear equation with a unique solution by coprimality.
Thus each candidate gives a single coefficient vector modulo \(2^k\).
An actual integer divisor at any of the four selected degrees has \(M(F)<2\) and \(|[z^j]F|\le \binom ej M(F)<2^{e+1}\).
At \(k=e+2\) its centered integer representative is therefore unique.
Exact monic division by the reconstructed candidate in \(\mathbb Z[z]\) decides whether it divides \(H_p\).
The motivation for testing \(e=208,210\) was the bound \(1<M(F)\le2^{9e/16372}<1.084\) for any divisor of either degree, below the degree-ten control.

The two endpoint values allow earlier rejection.
The polynomial \(H_p\) has no real roots, so any of its monic nonconstant divisors has even degree and is positive on the real axis.
Since \(H_p(1)=H_p(-1)=2\), a divisor omitting the endpoint block must have \(F(1)=F(-1)=1\), and one containing it must have \(F(1)=F(-1)=2\).
A modular candidate violating either equality modulo its current precision can be discarded.
Endpoint residues for a union of blocks are products of the values of its lifted blocks.
In particular the endpoint block itself has residues twice the inverse of the product of all 315 odd paired-block values at the respective endpoint.
Shared data and the actual finite lifting scope are owned by [J145](../computations/programs/Yin_J_G0145/readme.md).
At \(p=8191\) the endpoint test modulo \(2^{15}\) eliminates all 99540 candidates in the four target degrees.
The full product of local factors was also checked through every coefficient modulo \(2^{16}\).
At \(p=13367\), where \(\rho=41\), the [subsequent endpoint computation in J145](../computations/programs/Yin_J_G0145/readme.md#prime-13367) constructs a primitive \(p\)-th root \(u\) in \(\mathbb F_{2^{41}}\) by raising a nonzero field element to \((2^{41}-1)/p\) and checking that the result differs from one.
For each doubling orbit \(O\) in \((\mathbb Z/p\mathbb Z)^\times\), the product \(\prod_{a\in O}(z-u^a)\) gives one of the 326 binary irreducibles of degree 41.
Each of the 163 inversion pairs gives one candidate of degree 656 and, with the endpoint block, one of degree 658.
The endpoint test eliminates all candidates in both degrees modulo 512, and the product of all lifted blocks agrees with \(H_{13367}\) coefficient by coefficient modulo 4096.

<a id="complex-trace-cells"></a>
## Constructing a positive witness with a nonreal conjugate trace pair

Write \(P(z)=z^n Q(z+z^{-1})\) with \(Q\) monic integral of degree \(n\).
A real trace in \([-2,2]\) contributes zero to \(m(P)\).
For a nonreal trace \(w\), the two lift roots have reciprocal moduli and exactly one exceeds one.
The level curve for the larger modulus \(\rho>1\) is the ellipse
\[
 \frac{(\Re w)^2}{(\rho+\rho^{-1})^2}
 +\frac{(\Im w)^2}{(\rho-\rho^{-1})^2}=1,
\]
as follows by writing the exterior root as \(\rho e^{it}\).
Place \(n-2\) disjoint real brackets inside \([-2,2]\) and require opposite signs at their endpoints.
Place an upper half-plane disk \(D(c,r)\) inside the open ellipse of radius parameter \(\rho\).
For \(b_k=Q^{(k)}(c)/k!\), impose
\[
 |b_0|+\sum_{k=2}^n|b_k|r^k<r|b_1|.
\]
Rouché's theorem counts one root in the disk, conjugation supplies the lower root and the real brackets exhaust the remaining degree.
This certifies the full inequality \(1<M(P)<\rho^2\), including positivity.
Take rational endpoints and radius and rational real and imaginary parts of \(c\).
Choose a sign orientation in each bracket and a signed real or imaginary component of \(b_1\) for a lower bound on \(|b_1|\).
Replacing norms on the left by sums of absolute components yields sufficient rational linear inequalities in the free integer coefficients, using auxiliary real variables for absolute values.
For a finite search bound the free coefficients and fix the brackets, center, radius and orientations.
The sharper ellipse budget permits cells close to either endpoint of the trace interval.
An optional cheap test, when \(Q(a)\ne0\) for an integer \(a\), is
\[
 1\le (|c-a|+r)^2\prod_j \max_{t\in I_j}|t-a|.
\]
It follows by evaluating the factorization at \(a\).
A failed test is valid only under the stated nonvanishing condition.
Fixed cells and the selected single-pair signature leave many admissible input polynomials outside the search.

The degree-18 input is the \(v=2\) row of Michael Mossinghoff's [table by exterior root count](https://github.com/mossinghoff/Mahler-Measure-Database/blob/main/BestByRootCount_200.txt), dated 31 May 2026 in the data file.
The trace coefficients in ascending order are \((1,2,-13,-16,19,20,-8,-8,1,1)\).
[J144](../computations/programs/Yin_J_G0144/readme.md) verifies the original coefficient list, seven real brackets, one upper disk and the conjugate disk, giving the rigorous enclosure
\[
             1.2013475236<M(P)<1.20143521.
\]
A first inverse search seeds brackets from this \(Q\) multiplied by distinct real cyclotomic trace factors with no common root.
Allow the free integer coefficients to change, vary the brackets and impose \(\rho^2<6/5\).
This excludes every cyclotomic multiple of the control by its certified lower bound.
It also avoids the [nearest-integer rounding failure](Yin_L_G0456_v1.md#nearest-chebyshev-integer-rounding) by asking for an integer point directly inside a root-certified cell.
The remaining problem is integer feasibility as the outward cost shrinks.
An infeasible finite cell settles only that cell.
For a concrete degree-64 pilot, take the control \(Q_9\) and the degree-23 trace polynomial \(\Psi_{47}\) satisfying \(\Phi_{47}(z)=z^{23}\Psi_{47}(z+z^{-1})\).
The product \(Q_9\Psi_{47}\) has 30 simple real roots in \((-2,2)\), since the cyclotomic trace factor is irreducible of degree 23 and the seven original real brackets are disjoint.
Its reciprocal lift is the product of the known degree-18 input and \(\Phi_{47}\), with coefficient height three by direct convolution with 47 consecutive ones.
The [31 rational separators](../computations/programs/Yin_J_G0144/trace64_cell.py) include the outer endpoints \(-2,2\) and bracket the ordered real roots in 30 open gaps, with the signs of the seed alternating at the separators.
The target is the closed disk with center \((-177624+8300i)/100000\) and radius \(1/10000\), inside the ellipse with parameter \(219/200\).
At the outer bounding-box corner, the ellipse expression is less than \(992/1000\) by rational substitution, so the positive-measure target is \(M<(219/200)^2=1.199025\).
The seed supplies bracket orientations and is excluded by that very threshold.
[C876 v1](../claims/Yin_C_G0876_v1.md#statement) excludes the configuration for reciprocal lifts of coefficient height at most three.
[C876 v2](../claims/Yin_C_G0876_v2.md#statement) proves that at any coefficient height there is no monic integral trace polynomial of degree 32 with a root in each of these 30 open gaps and another in the specified closed disk.
The exclusion for reciprocal degree 64 is confined to those separators and that disk.

<a id="newton-prefix-search"></a>
## Pruning coefficient prefixes using circle moments

For a unit reciprocal \(P\) of even degree \(d\) with real integer coefficients, let \(s_k=\sum_\alpha\alpha^k\) and let \(t_k=\sum_\alpha(\alpha/|\alpha|)^k\), including multiplicities.
If \(M(P)\le R\), put \(E_k=R^k+R^{-k}-2\).
The reciprocal-conjugate pair \(r e^{it},r^{-1}e^{it}\) with \(r>1\) contributes \(e^{ikt}(r^k+r^{-k}-2)\) to \(s_k-t_k\).
The function \(\cosh x-1\) is superadditive for \(x\ge0\) by the addition formula.
Summing the radii with \(\sum_{r>1}\log r=\log M(P)\) gives \(|s_k-t_k|\le E_k\).
In particular \(|s_k|\le d+E_k\).
For any integer vector \(v=(v_0,\ldots,v_k)\), set \(c_\ell=\sum_{i=0}^{k-\ell}v_i v_{i+\ell}\).
Positivity of the sum of the squared absolute values of \(\sum v_j u^j\) over the projected unit roots \(u\) gives the necessary inequality
\[
 d c_0+2\sum_{\ell=1}^k c_\ell s_\ell+2\sum_{\ell=1}^k |c_\ell|E_\ell\ge0 .
\]
Both moment sequences are real by conjugation.
Newton's identity \(s_k=-k a_k-\sum_{j=1}^{k-1}a_j s_{k-j}\) uses only the first \(k\) coefficients below the leading term.
Any failed inequality therefore eliminates every continuation of the prefix.
The root count need not be known and these tests permit several nonreal escaping roots.
A finite list of \(v\)'s gives necessary conditions only.
The explicit upper bound for \(s_k\) also supplies a finite range of \(a_k\) in a search without a fixed height cap.

The [degree-ten census](../computations/programs/Yin_J_G0144/readme.md) compares the joint cuts with the single-moment cuts, then classifies every complete polynomial in two full reciprocal boxes using cyclotomic extraction and the [Graeffe coefficient certificate](../claims/Yin_C_G0263_v1.md#graeffe-mahler-upper).
The two sign variants of the degree-ten Lehmer polynomial are precisely the positive hits at \(R=6/5\) in both boxes.
They have the same Mahler measure.
The finite box counts validate the pruning and supply no sequence approaching one.
Use this branch as a calibration and cross-check for a constructor, with the unpruned denominator retained whenever reporting a probability.

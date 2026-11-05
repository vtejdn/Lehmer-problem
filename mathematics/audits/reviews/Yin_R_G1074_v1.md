---
author: Yin
---
# Independent review of binary rotation masks and all-place Hankel costs

Review act: 2026-11-04T16:24 UTC.
The human record author is Yin.
This is a separately organized agent review of the fixed C0857 and C0858 candidates, covering their complete stated arguments and the necessary input interfaces identified below.
The reviewer did not participate in either proof's development and received no substantive proof-development conversation, proposing-agent mathematical summary or earlier review conclusion for either candidate.
The fixed statements and proofs, repository rules, Task contract and necessary mathematical inputs were read directly.
D11, D12 and L445 were not consulted; the two fixed proofs supply the mathematical objects and arguments needed here.
No substantive proof repair was supplied or incorporated by this reviewer.

This review does not select a C assessment or complete the unrestricted Lehmer Task.
No mathematical program or numerical experiment was used as evidence, and no proof-assistant verification is asserted.

<a id="binary-masks-whole"></a>
## F1: Complete binary-mask and high-precision construction review

**Finding:** no unresolved mathematical gap was found in the exact three-part [C0857 statement](../../claims/Yin_C_G0857_v1.md#statement) and [complete argument](../../claims/Yin_C_G0857_v1.md#argument), under their stated hypotheses.
This finding covers both the general mask classification and the actual infinite polynomial construction, including the comparison limits.

The quotient by the Artin--Schreier image is used only as an F2-vector space.
Rotation preserves that image, so the map from F2[z]/(z^q-1) is a module map and its kernel is the ideal of a unique monic divisor, including the zero and full ideals.
The derivative of z^q-1 is nonzero at every root because q is odd.
The nontrivial Frobenius orbits have size ord_q(2), which gives the stated dimension formula and, when that order is q-1, exactly the four listed ideals.
The description of the even-weight case requires the common class to be nonzero; the full-kernel case is separately correct.
The smallest allowed prime q=3 and the full-mask versus proper-mask distinction introduce no exception.

For the proper simple-pole case, a pole of v of order a gives v^2+v a pole of order 2a without cancellation of the highest order.
If there are no finite poles, a proper rational function in the Artin--Schreier image must instead be zero; a nonzero constant is excluded by properness.
The same check applies to differences of rotations.
All poles of a nonzero invariant function are nonzero and partition into free q-orbits over an algebraic closure, so the reduced denominator degree is a positive multiple of q.
The coprime numerator and squarefree denominator hypotheses correctly identify that reduced degree with d in the specialization.
No repeated-pole conclusion is inferred.

For n=2^a, the exact order of 2 modulo N=2^n+1 is 2n: it divides the power of two 2n and does not divide n.
This argument does not require N to be prime.
A root of order N therefore has the claimed degree, and its inverse is its n-fold Frobenius conjugate.
The finite-field root set is simple, reciprocal and has constant term one.
The needed complete-ring, unit, Hensel and finite-order Frobenius arguments were checked directly in [C241's local construction](../../claims/Yin_C_G0241_v1.md#direct-etale-frobenius-lift).
Those arguments apply to the monic lift with irreducible reduction used here; C241's separate nontorsion norm result is not needed.
The lifted roots of t^N-1 have exact order N, their Frobenius orbit is stable under squaring, and fixed coefficients lie in Z2 by successive binary expansion.
Reciprocity permits a simultaneous reciprocal integer lift modulo 2^L.

The added term 2^L T(t^(d-1)+t) preserves degree, monicity, reciprocity, constant term and irreducible reduction.
The stated strict inequality on the circle of radius two gives the Rouche comparison, with exactly d-1 roots inside and exactly one outside; d=4, the smallest allowed degree, is included.
Infinitely many distinct positive integers T satisfy that inequality, and the outside root gives m(P)>log 2.
If two distinct conjugates had a root-of-unity quotient, a Galois automorphism carrying the first to the unique outside root would carry the second to a distinct root of the same outside modulus, which is impossible.
Consequently every positive power retains the original degree.

Powered polynomial coefficients are integral polynomial expressions in the original coefficients, with the reciprocal convention matching the displayed P_b.
Thus the coefficient congruence to the same Q_* holds for both P_2 and P_4.
The square-root expansions are formal because A(0)=0 and U(0)=1.
The binomial coefficients have only powers of two in their reduced denominators; equivalently, for j>=1, binom(1/2,j)=(-1)^(j-1) Catalan_(j-1)/2^(2j-1).
Together with the displayed exact 2-adic valuation, this verifies integer coefficients, the congruence modulo 2^(L-1), and the asserted integral F.
Reduction gives the full mask space at every odd rotation prime.
Evaluation at a root of exact order N forces one binomial-cover exponent to be divisible by N, yielding the stated unbounded total-exponent-to-degree ratio.

The comparison was checked against the binary scalar condition in [C244](../../claims/Yin_C_G0244_v1.md#balanced-scalar-congruence-gap) and the complete divisibility hypothesis and total exponent D in the [C135v2 statement](../../claims/Yin_C_G0135_v2.md#statement).
These are hypothesis comparisons; their entire separate proofs are not adopted or re-audited here.
The construction's large measure and the absence of a near-one conclusion are essential limitations, correctly retained in C0857.
It does not rule out alternative primes or other sufficient gap criteria, and it does not settle the Task.

Primary-source checks used the actual local PDFs: [Rod21](../../literature/pdf/Rod21.pdf), Section 1.1, Theorem 7, Propositions 8--9 and Lemma 10, PDF/printed pages 2--4; [Bel16](../../literature/pdf/Bel16.pdf), Theorem 19 and Corollary 20, pages 16--17; and [Sha23](../../literature/pdf/Sha23.pdf), Corollary 7.44, page 83.
The cyclic-code attribution, existence of the required finite-field order and exact Rouche hypothesis match the uses above.
The project arguments were checked in full; these source readings do not constitute whole-source proof audits or an exhaustive novelty search.

<a id="hankel-all-place-whole"></a>
## F2: Complete all-place Hankel and disk-cost review

**Finding:** no unresolved mathematical gap was found in the exact [C0858 statement](../../claims/Yin_C_G0858_v1.md#statement) and complete argument beginning at [the all-place Hankel section](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) and continuing through [the disk comparison](../../claims/Yin_C_G0858_v1.md#cauchy-radius-cost).
This is a proof of the conditional determinant and degree-dependent bounds, with the global divisibility premise supplied as stated.

The binomial coefficient 8^n binom(1/2,n) is an integer for every n>=1 and has exact valuation n+s2(n).
The constant term of A_J is zero, so each coefficient involves only finitely many terms.
All G_J coefficients are algebraic integers, and uniqueness of the square root with constant term one makes the full mask orbit Galois equivariant.
Summing that complete orbit, without division by its size, therefore gives integer coefficients.
The premise N_J-D_J in 8 O_K[x] is genuinely global and supplies every place above two; a relation at a single residue place is not substituted for it.

For s>=2, the omitted binomial terms begin at n=s-1 and all have valuation at least s.
For s=2 the retained approximation is constant; s=1 is also correctly handled by a constant approximation.
The product denominator has constant coefficient one and degree at most B max(s-2,0), and the summed numerator has the same degree bound.
Both descend to Z[x] because the entire rational construction is Galois invariant and integral.
The formal coefficient congruence descends to 2^s Z[[x]], with no missing orbit-size, ramification or trace factor.
Cancellation could lower the degree but is not required for this upper bound.

After subtracting the constant term and dividing by x, the approximating numerator has degree strictly less than b_s.
The finite coefficient recurrence consequently gives shifted Hankel rank at most b_s over Q2, including b_s=0.
The Smith-coordinate comparison is valid over Z2: when e_(b_s+1)<s, factoring 2^e_i from the relevant rows of the approximant leaves an identity matrix modulo two and hence a nonzero forbidden minor.
Applying all s-level bounds to the same matrix and summing the counts gives exactly 2k+sum_(l>=1) max(k-lB,0).
The stated L=floor((k-1)/B) formula includes k<=B, exact multiples of B and zero determinants, and its quadratic coefficient is 1/(2B).

Power-stability excludes root-of-unity quotients between distinct conjugates.
Positive absolute height, its invariance under conjugacy and roots of unity, and h(alpha^r)=r h(alpha) exclude coincidence between a rotated squared root and a rotated fourth-powered root.
Thus every basic rotated radicand has simple zeros not shared by another rotation.
Odd zero valuations imply independence of all these square classes over K(x); the multiquadratic character basis then separates distinct nonempty mask products, even when the orbit has one member or I is the full mask.
The rational factors 1/D_J are nonzero, so they cannot create a cancellation to a rational sum.
This verifies that f is nonrational.

The actual [BNZ22 arXiv v3 PDF](../../literature/pdf/BNZ22.pdf), dated 21 November 2022, was read at Section 2.2, PDF/printed pages 4--6, including the ambient field convention, determinant indexing, Lemma 2.1, Corollary 2.2 and Corollary 2.3.
The selected finite Pade argument and its application were checked; no D-finiteness assumption from the later subsection is imported.
For g=(f-f(0))/x, the source determinant Delta_(0,k-1)(g) equals the claimed k-square shifted determinant.
The criterion therefore gives infinitely many nonzero Delta_k.
This is selected-source checking, not a proof audit of the entire paper.

For fixed rho<H^(-4), every normalized factor is holomorphic on the disk because both its numerator and denominator are nonvanishing there and the normalized square root exists on that simply connected disk.
Cauchy's coefficient bound and the finite Hadamard row bound give the stated upper estimate, with total factored exponent exactly k^2.
The maximum M_rho is fixed before taking k to infinity, so its contribution and (k/2)log k vanish after division by k^2.
Comparison along the nonzero determinants, followed by rho increasing to H^(-4), yields log H>=log 2/(8B), and m(P)>=log H gives the second conclusion.
No degree normalization of m(P) is used.

The formal-Hankel conventions were checked against the selected [HR08 inspection](../literature/HR08/readme.md#selected-hankel-factorization-inspection) and [BR10 definition](../literature/BR10/Yin_U002.md#formal-hankel-rank); the finite recurrence above is the actual rank argument.
The stronger comparison bound log H>=log 2/(4d) was reused only at its existing statement-inspection scope in [Smy08 U001](../literature/Smy08/Yin_U001.md#smy08-house), which identifies Dimitrov's 2019 v1 Theorem 1 and expressly excludes a proof audit.
Since |I||O|>=1, C0858 is weaker than that comparison bound even when its extra mask premise is available.
It neither supplies such masks automatically nor proves a degree-independent Mahler gap; the [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) remains outside the conclusion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [F1](#binary-masks-whole) | independently reviewed |
| [F2](#hankel-all-place-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [F1](#binary-masks-whole) | [C0857 statement](../../claims/Yin_C_G0857_v1.md#statement) | All three parts, all hypotheses and quantifiers, infinite actual input construction, precision and coverage limits. |
| [F1](#binary-masks-whole) | [C0857 argument](../../claims/Yin_C_G0857_v1.md#argument) | Complete binary-cyclic-mask and large-period-full-mask arguments, necessary C241 local interface, comparison premises and source scope. |
| [F2](#hankel-all-place-whole) | [C0858 statement](../../claims/Yin_C_G0858_v1.md#statement) | Integral nonrational series, every shifted determinant valuation bound, conditional house and total Mahler bounds, original-task limits. |
| [F2](#hankel-all-place-whole) | [C0858 complete argument](../../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) | Entire argument from simultaneous rank bounds through nonrationality and the disk-cost conclusion; all-place descent, finite rank, valuation summation and source interfaces. |
| [F2](#hankel-all-place-whole) | [C0858 disk comparison](../../claims/Yin_C_G0858_v1.md#cauchy-radius-cost) | Exact radius, k-squared exponent, limit order, constant 1/(8B) and comparison with the retained unconditional house bound. |

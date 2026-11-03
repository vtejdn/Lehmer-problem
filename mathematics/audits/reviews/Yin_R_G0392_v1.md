---
author: Yin
---
# Independent applicability review of the Bilu fixed-function graph consequence

Date: 2026-10-18T12:25.
Human record author Yin.
Root separately assigned review of the fixed Bil97-U001 source/application account.
Root and the angular_envelope_review author contributed to its graph, strict/non-strict and own-degree arguments; the entropy_attainment_bridge reviewer contributed to none of them.
The reviewer previously worked on other G0001 source applications and reviewed C165, but those activities supply no review of the new graph consequence.
This is an independent statement/applicability review, not an independent proof audit of Bilu's equidistribution theorem, Zhang's theorem or the Bombieri--Zannier proof.

The arrangement is non-blind.
The reviewer received the exact requested source passages and application scope, read the complete fixed U, then directly text-read and visually inspected the actual retained printed465--467 and474--475/PDF1--3 and10--11.
Visual inspection resolved the symbols omitted by extraction in the height definition, weak-limit statement and Theorem5.1(b).

No computation of mathematical examples or contribution to a varying-function inquiry was performed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | [Bil97-U001 complete account](../literature/Bil97/Yin_U001.md#bil97-u001) | Complete selected source statements on printed465--467 and474--475, graph and alternative applications, own-degree/measure consequence, Salem specialization and exclusions; original source proofs not audited. |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | [Strictness and orbit conventions](../literature/Bil97/Yin_U001.md#strict-small-points-and-orbit-measures) | Fixed-rank tuple height, full joint Galois orbit measure, bounded-continuous weak topology, proper algebraic subgroups and the fixed-closed-support lemma. |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | [Exact torsion complement](../literature/Bil97/Yin_U001.md#torus-bogomolov-complement) | Theorem5.1's removal of all torsion subvarieties, including points and X itself when applicable, nonempty-complement positive infimum and fixed-X dependence. |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | [Graph and alternative applications](../literature/Bil97/Yin_U001.md#fixed-rational-function-height-gap) | Irreducible fixed graph, independent-base avoidance of torsion subvarieties, uniform output-height bound, strict/non-strict alternative, rational unit-modulus caveat and denominator restrictions. |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | [Own-degree and measure consequence](../literature/Bil97/Yin_U001.md#fixed-function-own-degree-divergence) | Nonconstant function, fixed-coefficient height upper bound, primitive-polynomial finiteness, rational fixed-fiber contradiction, actual own degree, leading coefficient and constant/monomial boundaries. |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | [Salem independence interface](../../ledger/Yin_L_G0176_v1.md#salem-joint-phase-density) | Only the classical Galois/modulus independence mechanism used in the final fixed-rank Salem application; no neutral-control, original gap or monomial theorem imported. |
| [Fixed-function applicability finding](#fixed-function-applicability-finding) | [Classical attribution boundary](../literature/Dub23/readme.md) | Existing exact Salem-angle attribution and original-monograph limits, unchanged; no additional source or theorem accepted through a citation alone. |

## Fixed-function applicability finding

**PASS within the stated source-statement and local-application scope.**
No substantive defect, omitted domain condition or required correction was found in the fixed account.
The conclusions are correctly separated:

- Every fixed nonzero rational F which is not plus or minus a Laurent monomial has a uniform positive output-height lower bound on sufficiently small independent input tuples, with constants depending on F and the fixed rank.
- Every fixed NONCONSTANT rational F has output own degree tending to infinity along admitted independent small-input sequences, including nonconstant torsion monomials.
- Combining those two conclusions gives own total logarithmic Mahler measure tending to infinity only for nonconstant F outside the torsion-monomial exceptions.

Non-torsion rational constants retain a fixed positive output measure and are not covered by divergence.
No uniformity over moving functions, rank, supports or coefficient denominators is supplied.
This finding is not evidence for the later varying-Mobius inquiry.

### Exact source and topology

The actual retained Bil97 published artifact is selected by the source-version and source-locator fields in the bound U unit.
Printed465 defines tuple height as the projective height of(1:x_1:...:x_N), with every local degree and the factor[K:Q]^(-1).
The unit's inequalities max h(x_i)<=H_N(x)<=sum h(x_i) follow place by place and have the stated fixed-N boundary.
Its orbit probability averages every complex embedding of a common field with actual multiplicities, equivalently the distinct joint orbit with equal weights.
The limiting measure is Haar measure on the unit polycircle inside(C*)^N, and weak convergence uses all bounded continuous tests there.

Theorem1.1 assumes strictness against each FIXED proper algebraic subgroup and tuple height tending to zero.
Lemma2.1(d), printed467, preserves support on a fixed closed subset.
Neither statement permits a singular logarithm or arbitrary unbounded test, and the application uses neither.
After applying the closed-support lemma, a nonzero Laurent polynomial cannot vanish almost everywhere on the polycircle: its characters are orthogonal and its squared L2 norm is the positive sum of coefficient squares.
That algebraic observation is not used as an unbounded test in weak convergence.

Theorem5.1, printed474, does not require irreducibility of X.
Its X* removes ALL contained torsion subvarieties and has positive height infimum when nonempty.
The trivial subtorus is included; printed475 also explicitly uses that X* has no torsion points.
The constant depends on the fixed X, and the source supplies no effective value here.
The attribution to Zhang and the distinct Bombieri--Zannier proof is correctly retained without claiming a proof audit.
Reading the adjacent Section5 discussion does not enlarge this finding to the original source proofs.

### Direct graph application

The graph of F=A/B on AB!=0 is irreducible of dimension r, and its closure in the torus lies in A-yB=0.
The primitive degree-one polynomial in y gives the graph component; closure introduces no separate irreducible component.
Possible lower-dimensional behavior at simultaneous numerator/denominator zeros does not change this fact, and those evaluations are outside the valid domain.
Rational coefficients ensure that every conjugate of a valid graph point remains valid with nonzero numerator and denominator.

Projection of a torsion translate under a coordinate-torus homomorphism is a closed torsion translate of a subtorus.
If the image is proper, its integer character lattice gives a nonzero character with a root-of-unity value at x.
Taking a positive power contradicts multiplicative independence.
A torsion subvariety containing an independent-base graph point must therefore project surjectively to the base.
Its dimension is at least r, so containment in the irreducible dimension-r graph forces equality with the graph.

A codimension-one torsion graph has an integer character relation x^a y^b=zeta, and its dominant base projection forces b!=0.
The identity F^b X^a=zeta has zero valuation at every nonunit Laurent irreducible factor, so unique factorization forces F=c X^e.
Rationality gives c in Q; c^b torsion gives c torsion, hence c=+1 or-1.
This is exactly the excluded class, including zero-exponent constants.
Zero-dimensional torsion subvarieties are also excluded by independence.
Thus every admissible independent-base graph point lies in X*.

Theorem5.1 and the tuple-height inequality give

    eta_X<=H_(r+1)(x,F(x))<=sum_i h(x_i)+h(F(x)).

Therefore delta_F=eta_X/(2r), c_F=eta_X/2 and the stronger sequence bound liminf h(F(x_k))>=eta_X are correct.
If no admissible point exists the assertion is vacuous, as stated.
The local inequality retains every finite-place contribution and rational denominator cost.

### Strict/non-strict alternative

An independent tuple belongs to no proper algebraic subgroup.
For disconnected subgroups, a positive multiple of a character annihilating the connected component annihilates the finite component group as well.
This agrees with the finite-torsion-coset structure explicitly used on printed475.
Hence every independent base sequence and its subsequences are strict.

A strict small lifted sequence would put full(r+1)-torus Haar measure on the fixed graph hypersurface by Theorem1.1 and Lemma2.1(d), impossible for its nonzero Laurent equation.
Failure of lifted strictness instead supplies ONE fixed proper subgroup containing infinitely many indexed terms.
Its fixed annihilating character gives x^a F(x)^b=1 on that subsequence.
Independence forces b!=0, and reversing exponents makes b positive.
Clearing the fixed denominator gives the rational Laurent equation x^a A^b-B^b=0.
Every full base Galois orbit lies in its fixed zero set, so base equidistribution forces that polynomial to be identically zero.
The resulting identity gives exactly the excluded torsion monomials.

No common character is selected from merely varying pointwise relations.
The rational unit-modulus warning is correct: (X-2)/(2X-1) is nonmonomial but has modulus one on the circle.
The valid contradiction uses its graph in an additional coordinate, not a false modulus-only classification.

### Own degree and total measure

For fixed integer ordinary P,Q representing F, the archimedean bound is

    max(|P(x)|,|Q(x)|)
       <=C product_i max(1,|x_i|)^(D_i),

where C=max(||P||_1,||Q||_1).
At finite places the same bound holds without C.
Summing normalized local contributions and rescaling projectively by the product formula proves the stated bound h(F(x))<=log C+sum_i D_i h(x_i).
No output integrality or denominator saving is assumed.
All outputs along an admitted small-input sequence therefore have bounded absolute height.

Bounded degree and bounded height leave finitely many primitive integer minimal polynomials, using the verified coefficient estimate binomial(n,j)exp(nH).
This includes the primitive leading coefficient when the output is not integral.
A bounded-own-degree infinite subsequence would have a further infinite constant-value subsequence y_0.
For its rational minimal polynomial q, the fixed polynomial Q^s q(P/Q) vanishes on that subsequence.
It is nonzero for nonconstant F: factor q over Qbar in the rational function field, where a zero product would force F to equal a constant root.
Rational coefficients put each full base orbit in this fixed zero set, contradicting base Bilu as above.
The proof therefore establishes own degree tending to infinity, not merely an unbounded degree subsequence or growth of an ambient field.

Combining this with the positive output-height floor proves the divergence of deg(y_k)h(y_k) in the stated nonconstant non-torsion-monomial class.
This is precisely own total logarithmic Mahler measure, including its leading-coefficient contribution.
No input degree is substituted for the actual output degree, and no convergence rate is asserted.

### Domain, constants, monomials and Salem use

Zero functions and zero or undefined values are excluded.
Independent small tuples eventually avoid any fixed nonzero rational numerator or denominator zero set, since infinitely many exceptions would contradict the same base closed-support argument.
The explicit domain restriction remains appropriate.

For rational constants c!=0, own degree is one and own measure equals h(c), zero only for c=+1 or-1.
They are not assigned divergence.
For F=c X^a, applying both height triangle inequalities gives

    |h(F(x))-h(c)|<=sum_i |a_i|h(x_i).

If a!=0, own degree still tends to infinity.
For c not equal to+/-1 the limiting height is positive; for c=+/-1 it tends to zero and total measure requires separate arithmetic.
The zero exponent vector returns to the constant case.

The Salem application fixes the number of selected roots, takes distinct inverse pairs and uses their classical independence with the real-pair representative explicitly covered.
Bounded original total measure together with d tending to infinity gives coordinate heights m(alpha)/d tending to zero; unbounded d alone does not.
No normal-trace or subdegree assumption, separate C165 adoption, or moving-coefficient conclusion is imported.
All functions, coefficients, supports and rank remain fixed before the sequence varies.

This completes only the selected source-statement and local-application review.
Original equidistribution and Bogomolov proofs remain accepted external inputs at their declared inspection limits.
No U mutation or subsequent route, Claim, Task or execution adoption is performed here.

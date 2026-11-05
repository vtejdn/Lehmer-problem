---
author: Yin
---
# Independent whole review of Mahler-preserving block descent and finite raw-p2 attainment

Review performed at 2026-11-05T01:47, in UTC, for human author Yin.
This is a separately organized whole-proof review of the fixed C866 v7 candidate.
The reviewer did not participate in its proof development and received no inherited substantive proof-development discussion, author explanation, exploration notes or earlier review conclusions.
The fixed candidate and its actual source and comparison inputs were read directly.
D1 and the contributing agents' conversations were not consulted.
Administrative confirmation that the candidate was stable, and a subsequent narrowing of its source-absence wording to the inspected passages, supplied no mathematical premise.
The new finding concerns the general inverse-Mahler block reduction; earlier C866 and R1088 versions retain their own statements and evidence.

## Exact inputs and source depth

The primary input is [C866 v7](../../claims/Yin_C_G0866_v7.md#statement), including its complete argument through BD11 and its BD12 boundary.
The explicit BD11 equality now collected in that statement was compared directly with the unchanged finite-attainment section: it uses the same linked F_alpha, infimum domain, raw quantity, attained field and degree bound, and preserves the nonuniform and basal limitations.
The review enumerated the quantified conclusion, actual-degree normalization, field and unit assertions, coefficient finiteness and original-Task limits before forming its findings.
The only inspected role of [C855 v2](../../claims/Yin_C_G0855_v2.md#raw-p-two-norm-descent) is its raw all-place definition SC16--SC17 and the comparison with the displayed equal-modulus norm fibers.
Its universal lower bound and analytic proof are not premises of this candidate and were not newly reviewed.
The [C866 v1 statement](../../claims/Yin_C_G0866_v1.md#statement) was checked only to confirm its explicit radical-monomial hypotheses; its theorem and dependencies are not invoked here.
The [G0001 contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) was read to check the original unrestricted positive total-Mahler-gap boundary, without reviewing its alternative entropy or growth equivalences.

The source edition is the [DD04 author manuscript dated 28 September 2004](../../literature/pdf/DD04--author-20040928.pdf), identified by its [edition explanation](../literature/DD04/readme.md#author-20040928) and [U001 scope](../literature/DD04/Yin_U001.md#dd04-u001).
The retained PDF has 24 pages.
The reviewer directly read Theorem 1 on p.2, Lemma 2(v)--(vii) and the displayed large-root-stabilizer proof on p.4, the basal definitions on p.5, Lemma 3 and its proof on p.6, and Theorems 4--5 and their displayed proofs on pp.6--8.
The unit specialization of Lemma 3 and the normal-subgroup and subset-labeling mechanisms were checked against the candidate.
Theorem 7 on p.9 and Corollary 8 with its counting proof on p.10 were read for the binomial comparison.
Rendered pp.6--8 were also inspected to resolve the displayed group notation and formulas.
These checks establish the stated source attribution, theorem scopes and basal distinction.
They are not a whole-paper audit or a new audit of the cited external ancestors or Theorem 1's entire original dependency chain.
The candidate supplies complete local proofs of its unit reduction, block construction and binomial bound; none of those conclusions relies solely on the source's existence theorem.
The inspected passages do not supply the claimed raw-M2 comparison or a raw-M2-monotone passage to a globally basal realization.

<a id="block-descent-whole"></a>
## Whole finding

The complete stated reduction BD1 and the finite-attainment conclusion BD11 are mathematically supported by the fixed argument.
No unresolved mathematical gap was found at this scope.
The following checks include the boundary cases and the logical interfaces that make this a whole finding.

### Starting unit and orientation

For a nonzero algebraic beta, the primitive irreducible polynomial has nonzero leading and constant coefficients.
The cases k=0 and k=n would make its Mahler measure a positive integer, incompatible with the assumed algebraic unit alpha>1.
Thus both exponents in BD2 are strictly positive integers: N/n is integral because F is the splitting field, and each conjugate occurs exactly Nk/n times in the Galois product.
Taking absolute norms gives the displayed product of integer coefficient powers equal to one, forcing both coefficient moduli to be one.
This establishes that every allowed beta is already an algebraic integer unit, including beta initially allowed to be nonintegral.

Inversion preserves the field, degree, Mahler measure and raw square norm of a unit.
Since the logarithmic moduli sum to zero and log alpha>0, there are both positive and negative entries.
Choosing the smaller of their two counts yields 1<=k<=n/2 even when some conjugates have modulus one.
No unit-circle root is incorrectly counted as large.

### Membership atoms and actual degree

The large-root product is real, up to a rational sign, because complex nonreal roots occur in conjugate pairs.
Among the k-subsets of the full conjugate set, the large-root set uniquely maximizes the absolute product: every replacement removes a modulus greater than one and inserts a modulus at most one.
An automorphism fixing alpha therefore fixes that set, which makes each Delta_a independent of the chosen automorphism.

The membership map is G-equivariant.
Its fibers form a G-invariant partition, and a compatible block of any other G-invariant partition lies in one fiber because every translate of Delta must also be a union of those blocks.
This proves the asserted coarsest property, rather than assuming that a minimum block count automatically gives a canonical partition.
Transitivity gives a common fiber size e and n=eb.

If two atom products were equal, grouping all atoms with a common product would be a G-invariant coarser partition.
Every such group stays entirely on one side of the large-root partition, since an atom product has modulus greater than one exactly for atoms inside Delta.
The coarser partition would therefore remain compatible, contradicting the established coarsest property.
Hence the b products are distinct.
Their transitive Galois orbit consists of algebraic integer units and has exactly b elements, so the output degree really is b.
There is no hidden multiplicity or leading-coefficient correction.

### Fields and the relative norm

The stabilizer of beta_tilde preserves its atom B_0.
The subgroup fixing L_alpha pointwise fixes every conjugate of alpha and therefore preserves every membership atom.
These two observations independently give gamma in Q(beta) and gamma in L_alpha.

Distinctness of atom products makes the stabilizer of gamma exactly the set stabilizer J of B_0.
For any xi in B_0, transitivity on roots gives an element sending beta_tilde to xi, and the block property forces that element to preserve B_0.
Thus the J-orbit of beta_tilde is exactly B_0.
The subgroup/field correspondence then gives extension degree e and the ordinary relative norm identity in BD5, with precisely the required embeddings.
Neither a radical nor an unaccounted root of unity is introduced.

### Mahler measure, raw norm and degree cap

Within each atom all logarithmic moduli are positive or all are nonpositive.
Consequently the positive part of the atom sum equals the sum of positive parts on that atom, including the possible mixture of negative and zero entries in an outside atom.
With the monic actual output polynomial this proves BD6 and M(gamma)=alpha.

The all-place definition in C866 v7 agrees with SC16 in C855 v2.
Once the input and output have been proved units, finite places vanish and complex places contribute both embeddings.
Applying Cauchy separately in each size-e atom and multiplying by the actual output degree b gives be=n and precisely BD7.
The stated equality condition, constant logarithmic modulus within every atom, is also correct.

Equivariance and transitivity make the cardinality r of Gamma_xi independent of xi.
Counting the incidence set in its two orders gives nr=dk.
Here r is a positive integer because k>0, and the explicit orientation gives r<=floor(d/2).
Different atoms have different r-subsets of the d-element set Sigma, so b<=binom(d,r)<=binom(d,floor(d/2)).
Together with b<=n and the independently checked field, measure and norm conclusions, this establishes all the quantifiers of BD1 for every starting realization.
There is no restriction to Salem alpha or to a globally degree-minimal input.

### Finite set and attainment

Every product of a subset of roots of a monic polynomial with Mahler measure alpha has modulus at most alpha.
The elementary symmetric coefficient bound BD10 therefore follows, including j=0 and j=b.
Since the possible degrees are bounded and every coefficient is integral, only finitely many polynomials satisfy those bounds.
The irreducibility, unit, splitting-field and exact-measure filters only reduce this finite set.
BD1 supplies at least one member because alpha is assumed to have a realization.

The raw M2 value is invariant under conjugacy and is therefore well defined for each irreducible polynomial in F_alpha.
Each original realization beta has an endpoint in this finite set with no larger value, whereas every root represented in the finite set is itself an allowed realization of alpha.
The first direction places the minimum raw value over F_alpha below the original infimum, and the second gives the reverse inequality.
This proves the exact equality BD11 and attainment in L_alpha at the stated actual degree.
No effective comparison algorithm for squared logarithmic sums is needed for the existence of a minimum over a finite nonempty set.

### Basal and original-Task boundaries

The source's basal irreducible polynomial minimizes degree over all irreducible realizations of the measure, subject to the orientation convention.
The atom argument minimizes only among compatible block constructions from the particular input.
These are different minimizations, and neither BD1 nor BD11 identifies its endpoint or raw minimizer with a globally basal realization.

For Salem alpha, M(alpha)=alpha gives a realization of degree d.
The source's Theorem 4(ii) applies to a globally basal irreducible unit realization because its leading and constant coefficients are units.
This provides the stated field and degree comparison, but supplies no raw-M2 monotonicity from an arbitrary beta.
BD12 consequently remains unproved here; no counterexample is asserted.

For any unit realization of degree at most d and measure alpha, the positive and negative logarithmic masses are both log alpha.
Bounding each of their square sums by the square of that mass gives M2<=sqrt(2d) log alpha.
The Salem realization has exactly two nonzero logarithmic moduli, of opposite signs, and hence attains that displayed square-root-degree cost.
The bound is degree dependent and supplies no uniform return to the original total-Mahler problem.

Finally, a product of conjugates of beta lying in L_alpha has not been proved to have the radical-monomial form in the conjugates of alpha assumed in C866 v1.
Neither the field inclusion nor the subset labels prove that form.
No earlier C866 result, unrestricted FM13 operator identity, uniform raw-to-total comparison, or resolution of the G0001 contract is imported by this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#block-descent-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#block-descent-whole) | [Exact statement](../../claims/Yin_C_G0866_v7.md#statement) | Complete quantified BD1 and explicit BD11 finite-attainment equality with the same linked F_alpha, all-place raw normalization, actual-degree convention, attained field and binomial degree bound, and nonuniform/basal limits for a degree-d algebraic integer unit measure alpha>1. |
| [Whole finding](#block-descent-whole) | [Complete argument](../../claims/Yin_C_G0866_v7.md#argument) | Entire local proof: starting unit and inversion, membership atoms, distinct products, field intersection and exact relative norm, Mahler preservation, Cauchy and binomial degree bound. |
| [Whole finding](#block-descent-whole) | [Finite attainment](../../claims/Yin_C_G0866_v7.md#finite-raw-attainment) | BD10--BD11: finite nonempty polynomial set, coefficient bounds, exact two-way infimum/minimum comparison and attained actual degree. |
| [Whole finding](#block-descent-whole) | [Basal boundary](../../claims/Yin_C_G0866_v7.md#basal-boundary) | BD12 remains unproved, globally basal and block minima are distinct, square-root-degree cost remains, and field membership does not give a radical monomial. |
| [Whole finding](#block-descent-whole) | [DD04 source scope](../literature/DD04/Yin_U001.md#dd04-u001) | Attribution and comparison at the inspected 2004 manuscript passages and displayed proofs stated above; no whole-paper or ancestor-proof audit. |
| [Whole finding](#block-descent-whole) | [Raw normalization comparison](../../claims/Yin_C_G0855_v2.md#raw-p-two-norm-descent) | SC16--SC17 normalization and the displayed equal-modulus fiber comparison only; no adoption or new audit of its universal lower bound or analytic dependencies. |
| [Whole finding](#block-descent-whole) | [Radical-monomial hypotheses](../../claims/Yin_C_G0866_v1.md#statement) | Statement-domain comparison only, showing why membership in L_alpha does not meet its separate radical-monomial hypothesis; no reliance on that theorem. |
| [Whole finding](#block-descent-whole) | [Original Task contract](../../tasks/Yin_T_G0001_v1.md#lehmer-entropy-growth) | Original unrestricted total-Mahler-gap and completion boundary only; the fixed-alpha finite reduction does not close this contract. |

## Conclusion and limits

This independently reviewed whole finding supports the exact C866 v7 block descent and finite raw-M2 attainment, with the stated basal, source and original-goal limits.
It supplies no assessment selection for C and no Task completion decision.
The verification is a complete textual mathematical review of this fixed argument and its stated interfaces, not formal verification or an exhaustive literature search.

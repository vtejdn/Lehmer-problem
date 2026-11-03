---
author: Yin
---
# Targeted independent review of the existing zero-gap direct-sum nonattainment argument

Date: 2026-10-18T10:40.
Human record author Yin.
The coordinating agent assigned an independent inspection of only the reverse-direction argument in Section 1 of [L1v1](../../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment), dated 2026-10-06.
That argument says that zero Mahler gap supplies a summable sequence of actual positive-entropy flows whose direct sum has finite entropy attained by no finite subset.
This reviewer did not develop or modify L1 or the root and entropy_attainment_bridge agents' present reconciliation.

The arrangement is non-blind.
The assignment supplied the proposed normalization checks and the observation that the existing argument avoids the exact-spectrum theorem.
The reviewer read the actual L1 paragraph, the Task's attainment and source-boundary wording, GBV15-U001, DGB16-U001 and the relevant DGB16-U004 passages, then checked R3's original scope against L2.
The finding below verifies the chain and makes its polynomial-to-flow interface explicit; it does not register a new theorem, audit the whole of L1, or adopt Task completion.
No mathematical program, new source search, numerical test or original external-proof audit was performed.
The account establishes a separate noncontributor but does not establish whether that agent inherited relevant substantive mathematical development context.
The proposed normalization checks identify the requested scope without resolving that historical isolation question.
The finding's current relationship is unknown; its original independent designation, actual inspection date, mathematical checks and limits remain historical facts rather than a new independent certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Targeted zero-gap finding](#zero-gap-direct-sum-independent-finding) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Targeted zero-gap finding](#zero-gap-direct-sum-independent-finding) | [L1 route assessment](../../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment) | Only Section 1's zero-gap to summable actual flows to same-automorphism nonattainment and failure of finite flow-module capture; not the preceding positive-gap implication, abstract countermodel or later sections. |
| [Targeted zero-gap finding](#zero-gap-direct-sum-independent-finding) | [Task entropy formulation](../../tasks/Yin_T_G0001_v1.md#algebraic-entropy-contract) | Exact finite-subset natural-log entropy and attainment for the same endomorphism; reconciliation of its printed-source warning with the separate local reverse argument, not review of the full Task contract or a completion claim. |
| [Targeted zero-gap finding](#zero-gap-direct-sum-independent-finding) | [GBV15 rational formula](../literature/GBV15/Yin_U001.md#gbv15-u001) | Only accepted rational Algebraic Yuzvinski Formula with primitive characteristic-polynomial rescaling and the full leading-coefficient term; no finite-set realization theorem is needed in this direction. |
| [Targeted zero-gap finding](#zero-gap-direct-sum-independent-finding) | [DGB16 basic entropy interfaces](../literature/DGB16/Yin_U001.md#dgb16-u001) | Exact trajectory convention, monotonicity, Proposition 2.8(c) directed invariant unions and 2.8(d) finite products, as inspected in that unit. |
| [Targeted zero-gap finding](#zero-gap-direct-sum-independent-finding) | [DGB16 printed reverse boundary](../literature/DGB16/Yin_U004.md#dgb16-u004) | The printed proof uses exact-spectrum Theorem 7.4, whose original passage/proof remains uninspected there; the present local argument does not use or upgrade that premise. |
| [Targeted zero-gap finding](#zero-gap-direct-sum-independent-finding) | [Existing R3 finding](Yin_R_G0003_v1.md#targeted-review) | Review-scope check only: the preserved finding concerns L2's rational-primary decomposition and capture implications, and does not provide whole review of L1's reverse equivalence chain. |

<a id="zero-gap-direct-sum-independent-finding"></a>
## Targeted zero-gap finding

**PASS for the specified existing conditional reverse argument in L1 Section 1.**
If the unrestricted primitive-polynomial Mahler infimum is zero, there exists one discrete abelian group and one automorphism with positive finite algebraic entropy for which no nonempty finite subset attains the entropy.
The argument requires arbitrarily small positive measures and summability, not the ability to prescribe every positive real entropy exactly.
Its conclusion is conditional on zero gap; no such sequence or nonattaining flow has been established unconditionally.

### Primitive polynomial selection and actual invertible rational blocks

Assume the infimum of positive logarithmic Mahler measures of nonzero primitive integer polynomials is zero.
For each integer n>=0, its defining property permits selection of a primitive polynomial f_n with

    0 < m(f_n) < 2^(-n-1).

Remove every factor t from f_n and change its overall sign if necessary.
The remaining polynomial is still primitive, its leading coefficient a_n is a positive integer, its constant coefficient is nonzero and its measure is unchanged.
Its degree d_n is at least one: a primitive constant is plus or minus one and has zero measure, contrary to the strict positivity.
Zero-root removal introduces neither a missing leading-coefficient term nor a discarded positive measure.
Reducibility and repeated nonzero roots do not obstruct this construction.

Let A_n be the rational companion matrix with monic characteristic polynomial f_n/a_n, acting additively on the discrete group Q^(d_n).
Its determinant is nonzero because f_n(0) is nonzero, so A_n is a rational automorphism.
The least positive integer clearing the coefficients of f_n/a_n is exactly a_n.
Indeed a_n is a clearing integer; conversely, if s clears them then a_n divides s times every coefficient of f_n.
Primitivity supplies an integer Bezout combination of those coefficients equal to one, so a_n divides s.
This verifies the required denominator normalization even for a nonmonic primitive polynomial.

The accepted GBV15-U001 formula therefore gives

    h_alg(A_n) = m(a_n(f_n/a_n)) = m(f_n) =: e_n.

All characteristic roots and their multiplicities, and the full term log a_n, are retained.
Entropy is total natural-log entropy, with no division by d_n.
The source theorem applies to arbitrary rational endomorphisms, so these particular invertible companion maps meet its hypotheses without any additional irreducibility or simplicity requirement.
Only this formula is needed; finite-set realization on each block is not required for the argument.

### One automorphism, a finite total and every finite subset

Take the external direct sum

    G = direct-sum_(n>=0) Q^(d_n),
    phi = direct-sum_(n>=0) A_n.

Both phi and the coordinatewise inverses preserve finite support, so phi is one automorphism of this discrete abelian group.
Let G_N be the sum of blocks indexed from zero through N.
The subgroups G_N form an increasing invariant union equal to G, and finite direct sums are finite direct products.
DGB16-U001 Proposition 2.8(d), iterated finitely, gives

    h_alg(phi restricted to G_N) = sum_(n=0)^N e_n.

Its Proposition 2.8(c), which applies to this actual directed union of invariant subgroups, then gives

    h_alg(phi) = sup_N sum_(n=0)^N e_n = S.

The bounds on e_n imply 0<S<1.
Positivity already follows from e_0>0.
For strictness of the upper bound, e_0<1/2 and sum_(n>=1)e_n<=sum_(n>=1)2^(-n-1)=1/2, so S<1.
No exact numerical value of S is required or asserted.
All sums are of nonnegative finite terms and the total is finite, so no subtraction of infinite entropies occurs.

Every nonempty finite subset F of G is contained in one G_N: each of its finitely many elements has finite coordinate support and the finite union of those supports is bounded in the index set.
Invariance makes every phi-trajectory of F remain in that same G_N, with identical cardinality when computed in G or in G_N.
Consequently

    H(phi,F) = H(phi restricted to G_N,F)
             <= sum_(n=0)^N e_n < S = h_alg(phi).

The last inequality is strict because the omitted tail contains the positive term e_(N+1).
This is nonattainment by every finite subset for the same automorphism phi.
It is stronger than merely producing different flows with the same entropy value and does not restrict finite subsets to subgroups or require that they contain zero.

Likewise, a finitely generated Z[t]-submodule for t acting by phi is generated by a finite set inside one G_N.
That invariant block contains the whole generated submodule, whose entropy is at most the block entropy by monotonicity and hence strictly below S.
This verifies the associated failure of finite flow-module capture in exactly the sense used in L1.

### Reconciliation with the printed-source boundary and prior reviews

DGB16-U004 accurately records that the printed reverse proof invokes Theorem 7.4 to select specified geometric entropy values, and that the cited original exact-spectrum source was not inspected.
Nothing in the present finding verifies that original theorem, changes the source audit or retroactively enlarges its inspected scope.
The local L1 argument instead chooses any sufficiently small positive values, realizes them by the normalized rational companions above and uses their convergent positive sum.
Thus it supplies the needed local reverse implication without the exact-spectrum premise.
The Task's warning about the printed source remains valid, while relying on this separately checked local chain need not inherit that particular uninspected premise.

R3's preserved review explicitly targets L2's rational-primary decomposition, positive multiplicities, directed continuity and capture criterion.
It supports that original material at its recorded scope and was not treated here as a whole review of L1 or of the present reverse chain.
The new targeted review supplies the actual missing inspection at this precise local scope.
The positive-gap to universal-attainment implication retains its separate existing audited inputs and repairs; it was not re-audited here.
In particular this finding alone is not a fresh whole review of all directions of the equivalence.

### Mathematical and source limits

The local chain has no remaining mathematical gap at the inspected scope.
Its only non-elementary realization input is the already accepted GBV15 rational formula, whose statement/applicability inspection and incomplete original p-adic proof audit remain exactly as recorded in GBV15-U001.
Directed unions, finite products, monotonicity and trajectory conventions are the explicitly inspected DGB16-U001 interfaces.
No unverified exact-spectrum assertion, full Addition Theorem, Bridge Theorem or finite-set realization theorem is needed in this reverse construction.
The companion and primitivity checks are elementary normalization details of the already retained route and are not claimed as a new entropy theorem.
The unchanged unrestricted problem of deciding positive versus zero gap remains unresolved.

---
author: Yin
---

# Yin_C_G0207 v1: Zero-Gap Argument Review and Statement-Quantifier Finding

Date: 2026-10-21T00:47.
Human record author: Yin.
Reviewer: a separately arranged AI subagent outside substantive development of the zero-gap direct-sum argument.
Target: the fixed [Yin_C_G0207 v1 Statement](../../claims/Yin_C_G0207_v1.md#statement) and [complete Argument](../../claims/Yin_C_G0207_v1.md#argument).
This review leaves that mathematical input, its decisions and every Task/execution record unchanged.

## Arrangement and actual input sequence

The first pass received only the fixed target, permitted necessary source units and review instructions, without the parent's target-development discussion, an author explanation or an old target-review conclusion.
The reviewer had previously performed an unrelated F-line review and did not develop this G-line construction.
A system-provided memory summary was visible, including general G0001 notes about auxiliary surplus versus a uniform Mahler gap, cyclic norms and determinant routes.
It contained no account of the companion-block, summable-entropy, same-direct-sum nonattainment mechanism reviewed here.
No persistent-memory file, blueprint, maintenance handbook or old L/R finding was consulted before the initial findings.

The initial inspection read only the target's Statement, lines 14-25, and its complete Argument, lines 49-129.
The latter itself contains the historical L/R pointers in lines 51-53; those pointers were not opened during the first pass.
The fixed [GBV15-U001](../literature/GBV15/Yin_U001.md#gbv15-u001) and [DGB16-U001](../literature/DGB16/Yin_U001.md#dgb16-u001) were the necessary source inputs.
A complete initial finding was reported before any old target finding was read: the argument has no identified reasoning gap, while the Statement does not explicitly quantify or type f_n.

The second pass explicitly compared [Yin_R_G0384's zero-gap finding](Yin_R_G0384_v1.md#zero-gap-direct-sum-independent-finding) with the reverse argument in [Yin_L_G0001 Section 1](../../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment).
The surrounding Section 1 text was read for scope identification, not audited as an additional proof.
Only the needed [DGB16-U004 source-boundary passages](../literature/DGB16/Yin_U004.md#dgb16-u004), the [old R3 scope account](Yin_R_G0003_v1.md#targeted-review) and the [Task's algebraic-entropy conventions](../../tasks/Yin_T_G0001_v1.md#algebraic-entropy-contract) were additionally inspected to compare the old finding's declared limits and adoption meaning.
The target's historical introduction and existing decision were read only at this comparison stage.
No old finding was used to establish the initial mathematical conclusion.
The arrangement supports independent inspection of this fixed v1 input; it neither authenticates an old reviewer's context isolation nor independently reviews a correction proposed by this reviewer.

<a id="zero-gap-v1-finding"></a>

## Findings on the fixed v1 input

The complete Argument proves the intended conditional zero-gap direct-sum assertion with the auxiliary polynomials selected in that Argument.
No gap was found in polynomial normalization, actual invertibility, the entropy formula, finite total entropy, finite-set nonattainment or failure of finite module capture.
There is a separate Statement precision defect: f_n occurs in the displayed existential conclusion without an explicit existential declaration or type.
This review therefore does not give an unqualified statement-completeness verdict for the current v1 text.
The proof and the Statement issue must not be conflated.

### Statement precision

Statement line 18 declares positive integers d_n, rational automorphisms A_n and positive numbers e_n=h(A_n)=m(f_n), for n>=0.
It does not explicitly declare the sequence f_n or say that its terms are nonzero primitive integer polynomials.
The earlier definition of m(f) and the infimum condition bind or describe f, not this new indexed sequence.

Argument lines 57-65 do make the needed choice and normalization, so no additional mathematical premise is missing from that reasoning.
The intended reading of the auxiliary sequence is recoverable from the proof.
Nevertheless the Statement alone does not supply the complete quantifier/type contract that its own m(f_n) uses.

The suggested correction is to declare the existence and type of f_n explicitly, consistently with the sequence actually chosen and normalized in the Argument.
That suggestion is a contribution of this review, not a change already made.
No revised wording, future physical version or adoption of such a revision is certified here.
A subsequent revision must be checked at its actual statement and interfaces by an appropriate review arrangement; this reviewer's suggestion does not itself provide independent acceptance of that correction.

### Positive primitive polynomials and actual rational automorphisms

Under the stated zero-infimum hypothesis, for every n>=0 one can choose a primitive integer polynomial with

\[
0<m(f_n)<2^{-n-1}.
\]

Removing every factor t preserves primitivity and Mahler measure and leaves a nonzero constant coefficient.
Changing the overall sign makes the leading coefficient a_n a positive integer.
The remaining degree d_n is positive: a primitive constant is plus or minus one and has measure zero.
Repeated nonzero roots and reducibility cause no obstruction.

The rational companion matrix of the monic polynomial f_n/a_n has that polynomial as its characteristic polynomial.
Its determinant is nonzero because f_n(0) is nonzero, so it is an actual automorphism of the discrete group Q^(d_n).
The least positive integer clearing the characteristic coefficients is exactly a_n.
If s clears them, a_n divides s times every coefficient of f_n; a Bezout combination of the primitive coefficients then gives a_n divides s.
Thus the source's primitive integral characteristic polynomial is precisely f_n.

The accepted rational Algebraic Yuzvinski Formula consequently gives h(A_n)=m(f_n)=e_n.
It retains the full log a_n term, all characteristic roots with multiplicity, and total natural-log entropy without division by degree.
The source interface applies to arbitrary rational endomorphisms, so these invertible companion maps satisfy it without an irreducibility or simplicity hypothesis.
Individual-block finite-set attainment is not needed.

### One automorphism and a finite positive entropy

Both the direct sum of the A_n and the coordinatewise inverse preserve finite support.
They define inverse maps on the same external direct-sum group G.
For the finite initial block G_N, finite direct sum and finite direct product agree, so finite-product addition gives

\[
h(\phi|_{G_N})=\sum_{n=0}^{N}e_n.
\]

The G_N form an increasing invariant union equal to G.
Directed-union continuity therefore gives

\[
h(\phi)=\sup_N h(\phi|_{G_N})
       =\sum_{n\ge0}e_n=S.
\]

The entropy convention is the positive finite-sum trajectory and its limiting normalized natural logarithm.
The limit exists because the logarithmic trajectory cardinalities are nonnegative and subadditive.
Product trajectories have exactly multiplied cardinalities, and product finite subsets are cofinal.
For an invariant directed union, each finite subset is in one subgroup and has the same trajectories there.
These directly checked mechanisms are the DGB16-U001 interfaces used here.

Positivity follows from e_0>0.
The estimate e_0<1/2 and the nonnegative tail bound sum_(n>=1)e_n<=1/2 imply S<1.
No particular numerical value of S is prescribed, and no subtraction of infinite entropies occurs.

### Every finite subset and every finitely generated flow module

A nonempty finite subset F of G has a finite union of coordinate supports, so F is contained in one G_N.
This remains true for F={0}, whose support is empty.
Invariance keeps every positive trajectory in the same subgroup, with unchanged cardinality.
Thus

\[
H(\phi,F)=H(\phi|_{G_N},F)
 \le\sum_{n=0}^{N}e_n<S=h(\phi).
\]

The strict inequality follows from the positive omitted term e_(N+1).
The argument applies to arbitrary nonempty finite subsets; it does not require a subgroup or the inclusion of zero.
It concerns the same automorphism phi and not a collection of different flows having matching numerical entropy.

For a finitely generated Z[t]-submodule, choose finitely many module generators in one G_N.
The block is forward invariant and therefore contains the generated submodule.
Restriction monotonicity bounds its entropy by the same strictly smaller block entropy.
Finite generation refers to the flow module, not the underlying abelian group.
The zero submodule also satisfies the conclusion.
No invariance under phi^{-1} is required for the restricted entropy.

## Source acceptance and exact boundaries

The only non-elementary realization input is the rational entropy formula retained in GBV15-U001.
This pass read and reused that unit's identified primary-statement, normalization and applicability evidence for arXiv:1111.1287v3.
It did not reopen the primary PDF or independently audit the complete p-adic proof.
The unit's deeper and separate finite-set-realization interface is not used.
No issue was found at the formula's actual interface to the primitive companion matrices.

For DGB16, this review uses only the finite-subset definition, monotonicity, Proposition 2.8(c) on directed unions of invariant subgroups and Proposition 2.8(d) on finite products.
The elementary mechanisms were directly reconstructed above.
The source unit's unrelated torsion, purification, splitting and essential-quotient limitations do not enter those mechanisms.
The Fekete lemma remains a standard foundational input with its required subadditivity checked; its historical original proof was not re-audited.

In the second pass, DGB16-U004's Theorem 1.7 discussion and retained external-input table confirmed the reported distinction: the printed reverse proof selects specified entropy values using Theorem 7.4, whose original primary passage and proof remain uninspected there.
This review accepts that as the unit's reported source-inspection boundary and does not verify the external theorem or perform a fresh original-source audit.
The present construction chooses arbitrary sufficiently small positive polynomial measures and their convergent sum instead.
It therefore does not inherit an exact-spectrum premise merely because the printed proof used one.

The positive-gap-to-attainment direction, the Addition Theorem, stabilization, torsion inputs, Bridge Theorem and individual-block realization are not required by this local reverse argument.
No claim is made here that positive gap, zero gap, a small-measure sequence or a nonattaining flow has been established unconditionally.

## Comparison with the old zero-gap finding and its adoption scope

| Old evidence or limitation | New comparison and actual coverage | Preserved boundary |
| --- | --- | --- |
| L_G0001 Section 1, lines 22-27: summably small positive flows, their direct sum and finite-support nonattainment. | The first pass reconstructed the complete current C argument, including actual primitive companion automorphisms and a finite total strictly between zero and one. It supplies the mechanism only sketched in the original paragraph. | The preceding positive-gap direction and later abstract length countermodel were read only as surrounding context and are not reviewed here. |
| R_G0384: zero-root removal, positive leading coefficient, least-denominator normalization and actual invertible rational blocks. | Every step was directly checked before reading R_G0384; the old details agree with the fixed C Argument. Reducibility and repeated roots need no additional premise. | This is not a new p-adic entropy-formula proof or a prescribed-entropy theorem. |
| R_G0384: finite products, invariant directed union, S finite and positive, and a strict omitted positive tail for every finite subset of the same flow. | The new check covers these steps and the full arbitrary-finite-subset domain, including sets without zero. | Finite-subgroup entropy is not substituted for finite-subset entropy, and no infinity subtraction is used. |
| R_G0384: failure of capture by finitely generated Z[t]-submodules. | The finite set of generators remains in one forward-invariant finite block, whose entropy is strictly below S. | No conclusion about all finite-entropy flows or the full Task follows. |
| R_G0384: printed exact-spectrum limitation and the separate local reverse proof. | The relevant DGB16-U004 passages confirm that the source warning is retained and that the local chain does not invoke that external theorem. | The original exact-spectrum statement and proof remain uninspected; neither the source unit nor that theorem is upgraded. |
| R_G0384: the Task's same-endomorphism finite-set convention. | Only the algebraic-entropy formulation was read for this comparison; its nonempty finite subsets, natural logs, total normalization and same-map attainment match the local argument. | No whole Task-contract or completion review was performed. |
| R_G0384: the old R3 finding concerns L_G0002 rather than the entire L_G0001 equivalence chain. | R_G0003's scope account was checked: it records rational-primary splitting, positive multiplicities, directed continuity and capture implications at its original L2 input. It is not used as proof of the present reverse argument. | Neither the L2 proof nor its old review arrangement is newly certified. |
| R_G0384's unknown relationship and original L1 input. | This new finding follows a separately arranged first pass and binds the actual C_G0207 v1 statement and argument. It does not transfer the old PASS to the later Claim wrapper. | The old relationship remains unknown and its original date, inspected input and limits remain historical facts. |

The current C introduction preserves the original L1 input and the older finding's unchanged input scope.
The current L1 wrapper explicitly says its historical review does not become a review of the later Claim wrapper.
The existing C decision dated 2026-10-21T00:08 selects R_G0644 as contributor self-review; it does not adopt R_G0384 as a newly performed isolated review of v1.
This review does not rewrite either adoption.
The new Statement precision issue is a finding about the v1 wrapper, not a demonstrated error in the old compact L1 reverse paragraph.
The current argument and the old targeted mathematical conclusion agree; no further reasoning gap was exposed in the comparison.
Global index publication and any subsequent adoption or historical-consumer reconciliation remain with the coordinating agent.

## Verification limits

The assigned Statement and complete Argument of C_G0207 v1 were inspected, and the old targeted reverse finding was compared only at its actual scope.
The conditional premise was not investigated or assumed to hold unconditionally.
No mathematical repair was made to the fixed input.
The proposed quantifier clarification has not been accepted or independently reviewed as a revised statement.
No new research computation, numerical experiment, source acquisition, formalization, proof assistant, external human review, correspondence, publication review or novelty assessment was performed.
No Task or execution record was resumed or changed.
A later substantive revision needs its actual scoped review rather than a retroactive extension of this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Fixed v1 Statement](../../claims/Yin_C_G0207_v1.md#statement) | Complete lines 14-25, with the finding that f_n is not explicitly quantified or typed in line 18. The intended conditional conclusion is supported by the Argument, but current v1 Statement completeness is not given an unqualified PASS and no future revision is certified. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Fixed v1 Argument](../../claims/Yin_C_G0207_v1.md#argument) | Complete lines 49-129: zero-gap polynomial choice, primitive normalization, actual rational automorphisms, accepted entropy formula, convergent direct sum, every finite subset, finite flow modules and exact source limits. No reasoning gap found. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Primitive companion blocks](../../claims/Yin_C_G0207_v1.md#primitive-polynomial-selection-and-actual-invertible-rational-blocks) | Whole polynomial-to-automorphism interface, including zero roots, degree positivity, nonzero determinant, least clearing denominator and leading-coefficient term. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Direct sum and finite supports](../../claims/Yin_C_G0207_v1.md#one-automorphism-a-finite-total-and-every-finite-subset) | Both directions preserve finite support; finite-product addition and directed continuity; 0<S<1; strict same-flow nonattainment and finite-module noncapture. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Source boundary](../../claims/Yin_C_G0207_v1.md#source-and-scope-boundary) | The local proof does not use the uninspected exact-spectrum theorem or the separate positive-gap direction. Original p-adic proof depth is retained. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [GBV15 formula](../literature/GBV15/Yin_U001.md#gbv15-u001) | Reused recorded primary-statement/applicability evidence for the rational Yuzvinski formula with primitive rescaling and log a_n; no new primary-PDF or complete original-proof audit and no finite-set-realization reliance. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [DGB16 basic interfaces](../literature/DGB16/Yin_U001.md#dgb16-u001) | Finite nonempty trajectories, limit convention, monotonicity and Proposition 2.8(c),(d), with the local mechanisms directly checked; no unrelated unit theorem is adopted. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Old reverse finding](Yin_R_G0384_v1.md#zero-gap-direct-sum-independent-finding) | Explicit second-pass comparison of the old mathematical checks, source limits, historical input and unknown relationship; not authentication or retroactive enlargement of that review. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Original L1 reverse paragraph](../../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment) | Only Section 1 lines 22-27 and their actual reverse-direction meaning; no positive-gap, abstract countermodel, later-section or whole-L1 review. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Printed reverse limitation](../literature/DGB16/Yin_U004.md#dgb16-u004) | Only the relevant Theorem 1.7 discussion and external-input limit for Theorem 7.4, as a source-record comparison; no independent audit of that external theorem or of the other realization direction. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Task entropy convention](../../tasks/Yin_T_G0001_v1.md#algebraic-entropy-contract) | Only local finite-subset, natural-log, same-endomorphism and printed-source-warning correspondence, not the full equivalence, Task contract, lifecycle or completion. |
| [Fixed v1 argument and Statement precision finding](#zero-gap-v1-finding) | [Old R3 scope](Yin_R_G0003_v1.md#targeted-review) | Second-pass scope comparison only: L2 rational-primary decomposition and capture implications do not provide a whole L1 reverse-chain review. Its mathematics and historical isolation are not newly audited. |

---
author: Yin
---

# Yin_C_G0207 v2: complete conditional proof and explicit sequence quantifiers

Date: 2026-10-21T00:57.
Human record author: Yin.
Reviewer: a separately arranged AI subagent outside substantive development of the zero-gap direct-sum construction and outside the v1-to-v2 correction.
Target: the fixed [Yin_C_G0207 v2 Statement](../../claims/Yin_C_G0207_v2.md#statement) and [complete Argument](../../claims/Yin_C_G0207_v2.md#argument).
This is a new inspection of that fixed revision, followed by a comparison with the specified older findings.

## Arrangement and actual input sequence

The first pass received the fixed target path, the review scope, applicable repository rules and permission to inspect necessary fixed mathematical sources.
It received no parent proof-development dialogue, mathematical summary of this construction or old target-review conclusion.
The reviewer did not develop the construction, identify the earlier quantifier defect or propose or implement the v2 correction.
A system-provided general memory summary was already visible.
That summary included other G0001 mathematics, including auxiliary surplus versus a uniform Mahler gap and cyclic-norm/determinant routes, and a general paused-status note.
It contained no account of this target's primitive companion blocks, summable positive block entropies or same-direct-sum finite-set nonattainment mechanism.
No persistent-memory file, blueprint or maintenance handbook was consulted, and those general notes were not used as mathematical evidence.

The initial display included target lines 1-28 and the complete Argument, lines 66-146, as numbered when inspected.
Thus the fixed target's own introductory revision/provenance sentences in lines 8-10 and its Argument's historical L/R pointers in lines 68-70 were visible.
The source-boundary description in lines 142-146 was also part of the fixed proof input.
These fixed-artifact descriptions were not a separately supplied author explanation or development narrative, and none of their old L/R links was opened before the first findings.
The Current assessment and Assessment history were not read.
The first pass read the fixed [GBV15-U001](../literature/GBV15/Yin_U001.md#gbv15-u001) and [DGB16-U001](../literature/DGB16/Yin_U001.md#dgb16-u001), then independently checked every substantive obligation and interface below.
Its complete first finding was reported before any old target finding was read: no mathematical or statement-quantifier gap was identified in this v2 input, subject to the stated accepted-source depth.

Only after that report did the second pass read the complete [R499 v1 finding](Yin_R_G0499_v1.md#zero-gap-v1-finding), the complete [R384 targeted finding and scope account](Yin_R_G0384_v1.md#zero-gap-direct-sum-independent-finding), and [L1 Section 1](../../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment).
The actual v1 Statement and complete Argument were then inspected to compare the old quantifier defect and the unchanged construction with v2.
Only the needed Theorem 7.4, Theorem 1.7 reverse-proof and external-input-table passages in [DGB16-U004](../literature/DGB16/Yin_U004.md#dgb16-u004) were additionally read for the reported source boundary.
R_G0499's comparisons to R_G0003, L_G0002 and the Task were read as that review's accounts; their original mathematical inputs were not reopened or newly audited.
The old conclusions did not establish or replace the independently formed first findings.
This arrangement supports an independent inspection of the present fixed v2 statement and proof; it does not establish an older reviewer's isolation or authenticate historical review dates.

<a id="zero-gap-v2-finding"></a>
## Finding on the complete fixed v2 input

The Statement and complete Argument establish the stated implication from zero infimum of positive primitive-polynomial Mahler measures.
The v2 Statement explicitly closes the auxiliary-sequence quantifiers and supplies the types and normalizations actually constructed in the Argument.
No gap was found in that statement contract, the polynomial-to-automorphism interface, the finite positive total entropy, nonattainment by every finite subset of the same automorphism, or the finite flow-module conclusion.
This does not assert that the conditional premise or any resulting small-measure sequence or nonattaining flow holds unconditionally.

### Explicit sequences, polynomial selection and the rational blocks

The hypothesis concerns nonzero primitive polynomials in Z[t] with positive unnormalized logarithmic Mahler measure.
For every integer n>=0, zero infimum supplies one such polynomial with 0<m(f_n)<2^(-n-1).
Removing all factors t leaves Mahler measure unchanged, since each removed zero root contributes log max(1,0)=0.
It preserves primitivity and makes the constant coefficient nonzero.
Changing the overall sign makes the leading coefficient a_n positive without changing the measure.
A primitive constant is plus or minus one, so positive measure forces d_n=deg(f_n)>=1.
The v2 conclusion explicitly quantifies all these f_n together with d_n, A_n and real e_n, on the same full index set n>=0.

The companion matrix of the monic rational polynomial f_n/a_n has that polynomial as its characteristic polynomial.
Its determinant is nonzero because f_n(0) is nonzero.
It therefore gives an actual automorphism of the discrete additive group Q^(d_n), including for reducible polynomials or repeated nonzero roots.
If a positive integer s clears the rational characteristic coefficients, a_n divides s times every integer coefficient of f_n.
A Bezout combination of the primitive coefficients equals one, hence a_n divides s.
Since a_n itself clears the coefficients, it is exactly the least positive clearing integer.
The accepted rational Algebraic Yuzvinski Formula therefore applies with primitive integral characteristic polynomial f_n and gives h(A_n)=m(f_n)=e_n.
The full log a_n contribution and all root multiplicities remain present.
The entropy is total natural-log entropy, without division by dimension.
No irreducibility, simplicity, nonzero-root loss or finite-set realization on the individual blocks is assumed.

### One automorphism with a finite positive total

The external direct sum of the A_n and the coordinatewise inverse both preserve finite support, so they are inverse maps on the same group G.
For G_N equal to the sum of blocks 0 through N, finite direct sums agree with finite direct products.
DGB16-U001 Proposition 2.8(d) thus gives

\[
h(\phi|_{G_N})=\sum_{n=0}^{N}e_n.
\]

These G_N are invariant, increase with N and have union G.
Proposition 2.8(c) applies to precisely this directed union of subgroups, yielding

\[
h(\phi)=\sup_N h(\phi|_{G_N})=\sum_{n\ge0}e_n=S.
\]

The first term is positive.
The bounds e_0<1/2 and sum_(n>=1)e_n<=1/2 give 0<S<1.
All terms are nonnegative and the total is finite, so no subtraction of infinite entropies or unsupported interchange occurs.
No prescribed value for S is needed.

The trajectory limit has the required domain of nonempty finite subsets and uses positive finite sums.
The identity T_(k+l)=T_k+phi^k(T_l) bounds its cardinality by the product of the two cardinalities, giving a nonnegative subadditive logarithmic sequence.
The Fekete lemma supplies the limit.
For finite products the product trajectory has exactly the product cardinality, and finite product sets are cofinal among all finite sets.
For a directed invariant union, every finite subset lies in one member and has the same trajectories there.
These mechanisms were directly rechecked, rather than inferred from an old PASS label.

### Every finite subset and finite flow-module

Every nonempty finite F in G is contained in some G_N because the finite union of its coordinate supports is bounded.
This includes F={0}, with empty coordinate support, and sets that do not contain zero.
Invariance keeps all its trajectories in that same G_N with unchanged cardinalities.
Consequently

\[
H(\phi,F)=H(\phi|_{G_N},F)
\le\sum_{n=0}^{N}e_n
<S=h(\phi),
\]

where the strict inequality follows from the omitted positive term e_(N+1).
This is a single automorphism with no attaining finite subset, not different automorphisms with the same numerical entropy.

A finitely generated Z[t]-submodule has finitely many module generators in one G_N.
All nonnegative iterates and integer linear combinations of those generators stay in that forward-invariant block.
The entropy of the restricted endomorphism is at most the block entropy by subgroup monotonicity, and is therefore strictly smaller than S.
The zero submodule also satisfies this conclusion.
Finite generation is that of the flow module, and inverse invariance of the submodule is unnecessary.
The full proof has no logical dependency on an old R/L verdict: its necessary construction and estimates are present in the selected C Argument.

## Necessary source use and inspection depth

GBV15-U001 records arXiv:1111.1287v3, its identified primary passages, the monic rational characteristic polynomial and least-clearing-integer normalization.
This review read and reused that fixed unit's recorded primary-statement and applicability evidence for the Algebraic Yuzvinski Formula.
The matched hypotheses are a finite positive dimension, the discrete rational additive group and a rational endomorphism, all supplied by the companion construction.
No new primary-PDF inspection or independent audit of the complete p-adic proof was performed.
The unit's separate finite-set-attainment interface is not a premise of this argument.
No objection was identified at the formula's actual polynomial-to-flow interface.

For DGB16-U001, the used inputs are the finite-subset trajectory convention, subgroup monotonicity, Proposition 2.8(c) on directed invariant unions and Proposition 2.8(d) on finite products.
The local proof mechanisms and their hypotheses were directly checked above.
The historical proof of the standard Fekete lemma was not reread.
The unit's torsion, purification, bounded splitting, essential-quotient and Addition-Theorem material is not needed.
Reading the whole fixed source unit does not amount to a new independent audit of all those other statements.

During the second pass, the specified DGB16-U004 passages confirmed what that source record reports: the printed reverse proof chooses specified geometric entropy values through an externally reported exact-spectrum Theorem 7.4, whose original passage and proof were not inspected there.
This review verifies the content of that retained source account, not the original PDF passage or that external theorem.
The C proof instead realizes any sufficiently small positive polynomial measures and uses their convergent sum, so it invokes no exact-spectrum premise.
The positive-gap direction, stabilization, the full Addition Theorem and its separate realization inputs are outside this review.
Necessary source identification and applicability were checked at the retained U-record depth; no whole-source or historical attribution audit is claimed.

## Comparison with the specified older findings

| Earlier input and actual scope | Comparison with this new inspection | Boundary retained |
| --- | --- | --- |
| R_G0499, fixed C_G0207 v1 Statement and complete Argument. | The actual v1 Statement uses f_n in m(f_n) without declaring its existence or type; the complete Argument supplies the intended primitive-polynomial choice. Its precision finding is confirmed by direct comparison. | The old finding concerns v1 and explicitly does not certify a future wording or physical version. |
| The v2 Statement, compared with the actual v1 Statement. | The existential sequences now explicitly include nonzero primitive f_n in Z[t], indexed by all n>=0, with d_n=deg(f_n)>0, positive leading coefficient, nonzero constant coefficient and 0<e_n=h(A_n)=m(f_n)<2^(-n-1). The complete construction supplies each condition. | This affirmative conclusion is the present independent check of v2, not a retroactive enlargement of R_G0499. |
| The actual complete v1 Argument and its v2 successor. | The primitive normalization, companion maps, total entropy and finite-support mechanisms agree; v2 makes the already constructed sequence part of the explicit Statement contract. All substantive obligations were checked in the first pass. | Agreement of the arguments does not remove the obligation to check the revised Statement and its interfaces. |
| R_G0384, targeted reverse finding at the original L1 input. | Its explicit normalization, summable positive total, finite-support strict tail and finite flow-module checks agree with the first findings here. L1 Section 1 lines 22-27 retain the compact original reverse mechanism. | R_G0384's current relationship is unknown; its old title, original date and original L1 target do not establish independent coverage of v2. |
| R_G0384 and R_G0499's printed-source warnings. | The needed DGB16-U004 passages retain the exact-spectrum inspection limitation. The current proof does not use that theorem. | Neither this comparison nor the local reverse proof verifies or upgrades the externally reported exact-spectrum theorem. |
| Older scope accounts concerning Task conventions, R_G0003 and L_G0002. | Their descriptions in the assigned R files were read to understand what those files claim to cover. They are not premises of the present C proof. | Those original Task/L2/R3 inputs and their historical review arrangements were not newly reviewed. |
| L1's dated original account and current provenance wrapper. | The current L1 wrapper preserves the original reverse paragraph and explicitly prevents transfer of its historical review to later Claim wrappers. The displayed R_G0384 account still names L1 and its original date. | This checks the current accounts, not historical bytes, the actual circumstances of an old inspection or a newly authenticated historical timestamp. |

The comparison leaves the independent first finding unchanged.
The v1 quantifier finding cannot be carried forward as an unqualified review of v2: it identifies a defect in a different fixed statement and expressly leaves any correction for subsequent review.
Conversely, the v1 defect is not an unresolved defect of the now explicit v2 sequence contract.
The present finding supplies the actual v2 statement-and-argument inspection without rewriting an old review or decision.

## Verification facts and limits

The exact v2 Statement and complete Argument were checked, including all sequence quantifiers, hypotheses, normalization terms, same-map requirements, arbitrary finite subsets and finite flow-module restrictions.
Historical L/R labels in the fixed target were provenance pointers rather than additional proof premises.
Their current accounts were compared only after the first findings; no claim is made that historical inspection circumstances or complete source-proof coverage have been independently authenticated.
The conditional zero-gap premise was not investigated or established.
No mathematical repair, new research calculation, numerical experiment, primary-source acquisition, formalization, proof-assistant check or external human review was performed.
No Claim assessment, Task contract, lifecycle or execution record was changed or resumed.
The review records evidence for possible later adoption; it does not select such an adoption or assert Task completion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Fixed v2 Statement](../../claims/Yin_C_G0207_v2.md#statement) | Complete conditional statement as inspected, lines 14-27: all existential sequences and types, polynomial degree/sign/constant normalization, each n>=0, entropy inequalities, same automorphism, every nonempty finite subset and every finitely generated Z[t]-submodule; no unconditional zero-gap claim. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Fixed v2 Argument](../../claims/Yin_C_G0207_v2.md#argument) | Complete lines 66-146: primitive polynomial choice, actual invertible companion blocks, accepted rational formula, finite positive direct-sum total, same-flow finite-set nonattainment, finite flow-module conclusion and source limits; no mathematical gap identified. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Primitive blocks](../../claims/Yin_C_G0207_v2.md#primitive-polynomial-selection-and-actual-invertible-rational-blocks) | Whole normalization and entropy interface, including zero-root removal, degree positivity, nonzero determinant, exact least clearing integer, multiplicities and leading-coefficient term. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Direct sum and finite supports](../../claims/Yin_C_G0207_v2.md#one-automorphism-a-finite-total-and-every-finite-subset) | Inverse support preservation, finite products and invariant directed union, 0<S<1, every finite subset and finitely generated flow-module strictness. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Source boundary](../../claims/Yin_C_G0207_v2.md#source-and-scope-boundary) | No exact-spectrum or separate positive-gap premise is used. The GBV15 p-adic proof depth and historical-source account limits remain explicit. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [GBV15 formula](../literature/GBV15/Yin_U001.md#gbv15-u001) | Reused retained primary-statement/version/normalization evidence for the rational Yuzvinski formula and checked its complete applicability here; no new original-PDF or full original-proof audit, and no reliance on finite-set realization. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [DGB16 basic interfaces](../literature/DGB16/Yin_U001.md#dgb16-u001) | Finite positive-sum trajectories and limit, subgroup monotonicity, Proposition 2.8(c),(d), with the needed elementary mechanisms directly rechecked; no other source-unit theorem adopted. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Old v1 finding](Yin_R_G0499_v1.md#zero-gap-v1-finding) | Complete second-pass reading and comparison of actual v1 scope, quantifier objection, source limits and correction-review reservation; not retroactive extension to v2 or authentication of the older review arrangement. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Actual v1 Statement](../../claims/Yin_C_G0207_v1.md#statement) | Second-pass direct comparison confirming f_n is used without its explicit existential declaration/type; the intended sequence is provided by its Argument. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Actual v1 Argument](../../claims/Yin_C_G0207_v1.md#argument) | Second-pass complete comparison of the already constructed sequence and unchanged local construction; no new v1 assessment or adoption is selected. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Old targeted reverse finding](Yin_R_G0384_v1.md#zero-gap-direct-sum-independent-finding) | Complete second-pass comparison of its normalization, direct-sum and support checks, original L1 target, current unknown relationship and inspection limits; no certification of its historical isolation. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Original L1 reverse argument](../../ledger/Yin_L_G0001_v1.md#lehmer-route-assessment) | Section 1 lines 22-27 only as the old reverse-proof comparison object; surrounding Section 1 and its wrapper were read for scope, not audited as positive-gap, abstract-countermodel or whole-L1 mathematics. |
| [Complete fixed v2 finding](#zero-gap-v2-finding) | [Reported printed-source boundary](../literature/DGB16/Yin_U004.md#dgb16-u004) | Only Theorem 7.4's reported interface, Theorem 1.7 reverse discussion and external-input-table boundary as source-record comparison; original PDFs, original exact-spectrum passage and proof remain uninspected in this review. |

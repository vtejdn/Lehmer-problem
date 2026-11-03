# BGH21: large-prime statements and the general-degree valuation boundary

<a id="bgh21-s8-discovery-screen"></a>
## Bounded S8 source screen, 2026-10-09

**Source/version:** [retained BGH21.pdf](../../../literature/pdf/BGH21.pdf).
The artifact is arXiv:2108.09857v5: submission stamp 2 October 2022, printed version date 4 October 2022.
Printed and PDF pages coincide.

**Trigger/intended use:** [S_G8](../../../strategies/Yin_S_G0008.md#next-coverage-test) needs actual primitive mass beyond an order-only existence floor, with controlled common exponent.
This screen asks whether a large-prime theorem supplies that missing input on an arbitrary-degree reciprocal core.

**Date/review and state:** 2026-10-09, Codex for Yin.
The assigned entropy_status AI read the online statement/model and scope remarks; the coordinating AI reread the retained artifact, pp.1--4 and 19.
This is a statement-and-applicability discovery screen, with the full proof and its external dependencies unreviewed.
No fixed source unit or accepted new proof dependency is created.

**Finding and hypotheses:** Theorems 1.1--1.3 on p.2 concern rational inputs, or degree-two inputs of norm plus or minus one.
Theorem 1.3 requires a nonzero non-root-of-unity input, uses n_0=exp(exp(max(10^9,3|D_K|))), and for every integer n>=n_0 guarantees a prime ideal pfrak with v_pfrak(gamma^n-1)>=1 and underlying rational prime p>=n exp(0.0002 log(n)/log(log(n))).
Its degree restriction prevents direct use on the remaining higher-degree reciprocal class.

Theorem 1.4, p.3, does allow every nonzero non-root-of-unity algebraic gamma of degree d.
Write log*=max(1,log) and Q=Norm(pfrak).
For Q>=exp(80000d(log* d)^2) and every integer n>=1, it gives the **upper** bound

    v_pfrak(gamma^n-1)
      <= Q exp[-(0.002/d) log(Q)/log(log(Q))] h(gamma) log* n.

Here pfrak is a prime ideal in Q(gamma), v_pfrak is its integral ideal valuation, and h is the absolute logarithmic height defined on p.4.
For the project's degree-d unit alpha, h(alpha)=m(alpha)/d.
The theorem supplies neither total mass nor a lower bound for m.

Remarks 1.6(1) and 9.1, pp.3 and 19, identify a residue-degree/congruence counting loss when trying to infer a general-degree large-prime result.
Remark 9.1's opening reference to a generally valid "Theorem 1.2" is inconsistent with that theorem's rational hypothesis; the preceding Remark 1.6 and the actual general theorem identify Theorem 1.4 as the relevant input.
This cross-reference discrepancy is retained explicitly.
The remarks describe this version's argument, not a current exhaustive claim about the literature.

**Dependencies/unchecked scope:** the p-adic logarithm estimates and proofs in Sections 3--10 are not adopted or independently audited here.
The source's statement of Stewart's earlier result is not a new audit of that earlier proof.
No formal verification was requested or performed.

**Local screening conclusion:** the stated lower bound on log p is of order log n and does not itself pay the [existing common-exponent budget](../../../ledger/Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion).
An upper bound for individual valuations additionally needs a justified total-mass lower bound and a sum over the actual prime ideals before it can force distributed mass.
Merely combining an m-proportional total estimate with this h=m/d bound is not a new m-independent lower input.
This is a limitation of the selected direct transfer, not a theorem that no further use of the valuation estimate is possible.
The [L_G152 actual-excess obligation](../../../ledger/Yin_L_G0152_v1.md#primitive-mass-next-obligation) remains unchanged.

**Search evidence:** the source was located by the assigned bounded largest-prime-factor search: `Stewart greatest prime factor algebraic number gamma n minus 1 degree height theorem` and `"Stewart" "prime factors" "algebraic" "degree" "Lehmer-Pierce"`.
The coordinator inspected the arXiv identity/history, the versioned artifact and the above passages.
The web reader failed on the versioned URL, while direct verified-TLS acquisition succeeded; there is a retained artifact, not an online-only acquisition exception.

The assigned AI subsequently checked this compact record against the retained statements and conventions.
Its two wording findings were applied: make all input/time quantifiers explicit, and distinguish the guaranteed logarithmic lower bound from the actual prime's size.
This is source/model verification, not an independent review of the source's complete mathematical proof.

**Next action:** stop the direct general-degree large-prime transfer from these statements.
Revisit Theorem 1.4 if a separate concrete mechanism supplies sufficient actual mass and pays the prime-ideal sum and common-exponent costs.
Do not repeat a fixed-input asymptotic or replace a primitive ideal by a new rational prime without proof.

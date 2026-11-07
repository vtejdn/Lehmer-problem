---
author: Yin
---

# Independent review of the binomial coefficient gaps and the one-step normalized derivative

Review time (UTC) 2026-11-07T16:57.
A reviewing agent for Yin independently examined the two working-copy v1 Claims identified below.
The reviewer took no part in their development and received the fixed arguments and their referenced inputs without development dialogue, author explanations or prior review conclusions about these Claims.
The review covers the complete local deductions and the stated applications of external results.

<a id="binomial-gaps-and-multipliers"></a>
## C872 coefficient windows, multipliers and positive descent

All five assertions hold with the stated degree, endpoint, height and integrality hypotheses.
For a window of grade \(n\) and actual positive degree \(m\), Mahler's derivative inequality gives \(M(W'/n)\le(m/n)M(W)\).
Reversal at grade \(n\) can add or remove zero roots, which contribute one, and exchanges each nonzero root with its inverse with the leading-coefficient factor exactly compensating.
This proves the bound for every contiguous window by deletion, including polynomials of actual degree zero and the zero polynomial under the stated convention.
The source interface is [Pri08, Corollary 1.2](../literature/Pri08/readme.md), as recorded in [L461](../../ledger/Yin_L_G0461_v1.md#normalized-derivative-descent).

Below two, the integral entries have modulus at most one, and a nonzero middle flanked by a zero gives measure at least two.
For opposite nonzero ends the quadratic formula gives \(1+\sqrt2\) for the measure.
For \(\eta=1+\sqrt2\), a middle of modulus two under the strict unit bound requires nonzero ends \(u,w\) with \(uw=4\), since the other possible products satisfy \(uw\le2\) and the leading modulus times the larger root modulus is \(2+\sqrt{4-uw}\).
Propagation then contradicts the unit endpoint.
With entries now bounded by one, the interior zero-neighbor case gives actual leading modulus three in the cubic window, except at the last interior slot.
There, reversal and sign changes produce \(x^3-3x^2+t\), whose value at \(\eta\) is at most \(-1-\sqrt2\), ensuring a larger positive real root.
The right-end argument also works if the reversed array begins with \(-1\), by an overall sign change.
Propagation gives precisely the endpoint-only and period-two arrays, including the empty interior for \(d=1\) and the two unit neighbors for \(d=2\).
The examples \(x(x+2)\) and \(x^2+2x-1\), and all the classified measure-one cases, have the stated measures by their roots.

On monic inputs each diagonal entry is tested by an integer coefficient one, and the last entry is a sign by the unit condition.
The image of \((x+1)^d\) has measure one, so the classification exhausts the possible arrays.
For the two endpoint maps the output measure is \(\max(1,|P(0)|)\le M(P)\).
The other two maps preserve all root moduli.
With \(a_i\) denoting ordinary coefficients of \(p\), the sign in [MSS15, Definition 1.4](../literature/MSS15/Yin_U001.md#finite-free-definitions) gives the output coefficient \(a_i e_i/\binom di\).
The roots of a monic unit \(q\) with measure one all have modulus one.
When \(|a_i|\le1\), an integral nonzero interior output forces equality in the triangle inequality for the \(i\)-subset products.
Comparing any two indices against a disjoint common subset of size \(i-1\) works also at \(i=1,d-1\) and forces all roots to coincide, hence the common root is real and equal to \(1\) or \(-1\).
Zero interior output gives an endpoint unit of measure one, so this also checks the application to the displayed [Lehmer polynomial](../../claims/Yin_C_G0007_v1.md#statement).
For unrestricted input height and at least two distinct kernel roots the strict triangle bound holds at each interior index.
Integrality makes the new interior height at most the old height minus one whenever that height was positive.
Whole substitutions preserve every old interior coefficient at a distinct interior position and insert zeros, and single-root kernels preserve absolute coefficients.
Every vertex of the positive chain has interior height at least one, proving the count for arbitrary interspersed substitutions and repeated or input-dependent kernels.
This count covers whole substitutions only and uses integrality at every convolution step.

<a id="integral-normalized-derivative"></a>
## C875 one integral derivative below Smyth's bound

The classification, converse and padding conclusion all hold for monic integer polynomials in the stated strict range.
For \(P=x^sH\) with \(H(0)\ne0\), the root product bounds the nonzero integer \(|H(0)|\) by \(M(P)<\theta<2\).
A mixed zero-root case \(0<s<d\) therefore contributes the noninteger coefficient \(\pm s/d\) to \(P'/d\).
For each remaining nonzero-root core, all its monic irreducible factors have measure at most the total.
The measure-one factors are cyclotomic, including \(x-1\) with negative reversal sign, and Smyth gives reciprocity for the positive-measure factors under the strict bound.
The sign of the product's reversal is its unit constant coefficient.
This checks the actual [C870 factor argument](../../claims/Yin_C_G0870_v1.md#reciprocity-of-the-nonzero-root-core), using [Smyth's theorem](../literature/Smy71/Yin_U001.md#smy71-statement-and-conventions) and the [Kronecker boundary](../literature/Smy08/Yin_U001.md#smy08-height-normalization).
Mahler's derivative inequality puts the integral monic \(Q=P'/d\) under the same bound, so the same argument applies to its core.

For \(Q=x^{k-1}R\), differentiating signed reversal gives \(P=xQ+\varepsilon\operatorname{rev}_{d-1}Q\) and \(\operatorname{rev}_{d-1}Q=\operatorname{rev}_{d-k}R=\eta R\).
The factor \(R\) cancels in \(\mathbb C(x)\), including any roots shared with \(x^k+\varepsilon\eta\).
The resulting logarithmic derivative has poles at exactly the \(k\) simple nonzero roots of that binomial, each of residue \(d/k\).
The logarithmic derivative of a polynomial has positive integral residues equal to its root multiplicities.
Hence \(k\mid d\), and monicity determines the polynomial.
This includes \(Q=1\) in degree one and \(R=1\) at \(k=d\).
The displayed normalized derivatives verify the converse for the powers, and the monomial gives \(x^{d-1}\).
Multiplicativity gives the same measure in \((1,\theta)\) after every monic integral measure-one padding, where the classification applies at the product's degree.
The classification uses the strict inequality at \(\theta\), and determining the infimum on the positive integral-derivative domain remains outside this review.
The review accepts Mahler's derivative inequality, Smyth's theorem and Kronecker's theorem at their stated interfaces without re-auditing their external proofs.
The author-hosted Pri08 PDF timed out on this review's direct request, so the chapter interface uses the retained statement-level inspection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | independently reviewed |
| [Integral normalized derivative](#integral-normalized-derivative) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | [C872 statement](../../claims/Yin_C_G0872_v1.md#statement) | All five conclusions, thresholds, domains and positive-chain restriction. |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | [Contiguous windows](../../claims/Yin_C_G0872_v1.md#windows) | Grade reversal, deletion from both ends and scalar bounds, including endpoint zeros. |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | [Threshold two](../../claims/Yin_C_G0872_v1.md#gap-two) | Quadratic alternatives, propagation and equality example. |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | [Unit threshold](../../claims/Yin_C_G0872_v1.md#sharp-unit-gap) | The modulus-two exclusion, cubic edge case, propagation and equality example. |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | [Universal operators](../../claims/Yin_C_G0872_v1.md#universal-diagonal-multipliers) | Necessity and sufficiency on the monic integral domain. |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | [Height-one inputs](../../claims/Yin_C_G0872_v1.md#height-one-input-dependent-kernels) | Signed convention, equality criterion, vanishing alternative and Lehmer example. |
| [Binomial gaps and multipliers](#binomial-gaps-and-multipliers) | [Positive-chain bound](../../claims/Yin_C_G0872_v1.md#descent-length) | Integral strict decrement, whole substitutions and positive endpoints. |
| [Integral normalized derivative](#integral-normalized-derivative) | [C875 statement](../../claims/Yin_C_G0875_v1.md#statement) | Full classification under the strict threshold, converse and padding. |
| [Integral normalized derivative](#integral-normalized-derivative) | [C875 proof](../../claims/Yin_C_G0875_v1.md#argument) | Both reciprocal cores, differential identity, logarithmic residues, divisibility and all boundary cases within the stated range. |

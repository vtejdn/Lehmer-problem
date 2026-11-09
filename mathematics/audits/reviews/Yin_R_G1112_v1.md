---
author: Yin
---

# Independent review of adjacent perturbations and fixed-support whole measure

<a id="scope"></a>
## Review act and exact scope

This independent review was performed at 2026-11-09T18:55 UTC by a separately arranged agent acting for Yin.
The reviewer did not develop [L464v19](../../ledger/Yin_L_G0464_v19.md#family), received no development discussion and made no proof repair.
The assignment supplied the fixed material and the requested inspection scope.
The reviewer already knew the independently checked single-term family and its finite census; those findings were not treated as evidence for the new two-term or fixed-support deductions.
This new R family concerns the distinct adjacent-perturbation and complete-measure argument.

The review covers every mathematical assertion in the selected L material: the two-term trace and lift, endpoint and profile formulas, general fixed-K completion, actual support bound, source applicability, both conductor-11 controls and the conditional prefix-bound combination.
The fixed C and L predecessors were used only at their directly invoked interfaces.
The current J157 survivor-measure section and its exact conductor-11 polynomial were checked at the supplied working revision, including one bounded reproduction at each of 128 and 256 bits.
No parameter scan or proof audit of the unrelated sampling experiment was performed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Adjacent-support finding](#adjacent-support-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Adjacent-support finding](#adjacent-support-review) | [L464v19 family](../../ledger/Yin_L_G0464_v19.md#family) | Exact two-term domain, integer trace/lift, common prefix, full-grid coordinate identity and distinct coefficient directions. |
| [Adjacent-support finding](#adjacent-support-review) | [L464v19 endpoint and profile](../../ledger/Yin_L_G0464_v19.md#endpoint-and-profile) | Endpoint, derivative, double-profile line, equal-amplitude identity and last-pole formula. |
| [Adjacent-support finding](#adjacent-support-review) | [L464v19 complete lift](../../ledger/Yin_L_G0464_v19.md#complete-lift) | Exact completion, at most twenty actual nonzero terms, nonzero integer object, full measure and accepted-source application. |
| [Adjacent-support finding](#adjacent-support-review) | [L464v19 general fixed K](../../ledger/Yin_L_G0464_v19.md#fixed-number-of-terms) | Every permitted index, exact K-term identity, 12+4K bound and necessary support escape. |
| [Adjacent-support finding](#adjacent-support-review) | [L464v19 conductor-11 controls](../../ledger/Yin_L_G0464_v19.md#small-control) | All-real equal-amplitude-line exclusion, changed-neutral-block identity and reuse of the identical survivor's complete measure. |
| [Adjacent-support finding](#adjacent-support-review) | [L464v19 conditional conclusion](../../ledger/Yin_L_G0464_v19.md#first-gap) | Prefix-bound hypothesis matching, exact length-140 comparison, fixed-support incompatibility at large length and unresolved scope. |
| [Adjacent-support finding](#adjacent-support-review) | [C884v1 input domain](../../claims/Yin_C_G0884_v1.md#inputs) | Original neutral trace, grid, strict chamber and endpoint conventions. |
| [Adjacent-support finding](#adjacent-support-review) | [C884v1 full-grid coordinates](../../claims/Yin_C_G0884_v1.md#all-r-pole-values) | Linear extension to two permitted indices, including unreduced coordinate representatives. |
| [Adjacent-support finding](#adjacent-support-review) | [L462v11 double-factor obstruction](../../ledger/Yin_L_G0462_v11.md#double-factor-obstruction) | Complete-measure-one consequence when the trace retains t squared and satisfies the original chamber and endpoint. |
| [Adjacent-support finding](#adjacent-support-review) | [DS17 accepted source scope](../literature/DS17/Yin_U001.md#ds17-u001) | Fixed-support univariate total logarithmic gap; primary statement checked, original foundational proofs not re-audited. |
| [Adjacent-support finding](#adjacent-support-review) | [C884v3 single-term result](../../claims/Yin_C_G0884_v3.md#statement) | Scope distinction and identification of the old conductor-11 survivor after the exact neutral-block change. |
| [Adjacent-support finding](#adjacent-support-review) | [J157 survivor measures](../../computations/programs/Yin_J_G0157/readme.md#survivor-measures) | Conductor-11 original coefficient list and its stated strict complete-measure enclosure only. |
| [Adjacent-support finding](#adjacent-support-review) | [J157 survivor source](../../computations/programs/Yin_J_G0157/survivor_measures.py) | Exact lift construction and rational enclosure checks used for the conductor-11 value. |
| [Adjacent-support finding](#adjacent-support-review) | [J156 complete-root evaluator](../../computations/programs/Yin_J_G0156/sampler.py) | certify_polynomial and its interval helpers: exact factor reconstruction, all roots and multiplicities, complete product and rational interval export. |
| [Adjacent-support finding](#adjacent-support-review) | [C881v3 prefix theorem](../../claims/Yin_C_G0881_v3.md#statement) | Exact x=0 hypotheses and complete-measure upper bound, applied conditionally without an existence conclusion. |

<a id="family-checks"></a>
## Trace, profile, endpoint and common prefix

The condition \(L\le n-2\) gives \(k\ge1\), so both \(B_k\) and \(B_{k-1}\) are defined and both coordinate indices lie in the recurrence's range.
Their perturbation degrees are below \(n\), preserving the neutral trace's original quotient by \(B_n\), monicity and integral domain.
The lift of \(tB_{n-\ell-1}\) starts at \(z^{\ell+1}\).
Thus \(\ell=L,L+1\) preserve the common prefix through \(L\), with no need to assume that the neutral prefix also reaches \(L+1\).
The optional stronger block-length condition is correctly separated from that common-prefix requirement.
The residue-coordinate formula follows by linearity from the unchanged recurrence congruence at both indices and is valid as a node-value identity for every allowed \(r\).

The neutral trace contains \(t^2\), and the perturbation contains \(t\), so \(Q(0)=0\) throughout.
Differentiation gives precisely \(Q'(0)=-AB_k(0)-CB_{k-1}(0)\).
The recurrence gives the stated period-four values at zero and the ratio \(B_k(0)/B_{k-1}(0)=(-1)^{k+1}\); hence \(t^2\mid Q\) exactly when \(C=(-1)^kA\).
The invoked double-factor argument applies with \(x=0\): division by the square preserves pole and endpoint signs, and its root count exhausts the degree of the remaining trace.
It therefore concerns every original root and gives complete measure one under the stated chamber and endpoint hypotheses.

The two lifted endpoint contributions have opposite signs, yielding \(4m+2(-1)^L(A-C)\).
The recurrence also verifies \(B_k+B_{k-1}=(t+2)E_{k-1}\), including \(k=1\).
On \(C=A\), the endpoint is unchanged; even \(k\) retains the double factor, while odd \(k\) and nonzero \(A\) give the stated nonzero derivative.
A simple root alone does not establish positive measure, as the material correctly states.
At the last pole, the parity of \(E_L\) and \(E_{L+1}\) gives the exact difference of the two sine terms in equation (5).
Both angles lie below \(\pi/2\), and the second sine is strictly larger.
Thus nonzero equal amplitudes preserve the endpoint without cancelling the last-pole perturbation; zero amplitude is the trivial neutral point.

<a id="completion-checks"></a>
## Completion, actual support and full measure

For every permitted \(\ell\), the exact lift is
\[
 z^{n+1}tB_{n-\ell-1}(z+z^{-1})
 =z^{\ell+1}(1+z^2)\frac{1-z^{p-2\ell-2}}{1-z}.
\]
Multiplying by \((1-z)^2(1+z)\) replaces its prefactor by \(1-z^4\), proving equations (6) and (9) term by term.
The endpoint index \(\ell=n-1\) still has positive binomial exponent one and uses \(B_0\); no omitted negative index is needed.
For the two adjacent terms, the corresponding exponents are at least three and one.
All displayed expressions are ordinary integer polynomials, and the constant coefficient of the completion is one.
They are therefore nonzero even when coefficients vanish or cancel.

The neutral numerator has at most \(3\cdot2\cdot2=12\) terms.
Each perturbation has at most four, before combining coincident exponents.
Summing cannot create additional exponent positions, so the actual support is at most twenty for two terms and at most \(12+4K\) for a fixed list of K terms.
Repeated indices, vanishing coefficients and cancellations only reduce these bounds.
The source application concerns this actual expanded polynomial, not a count of formal expression labels.

The multiplier is \(\Phi_1^2\Phi_2\) and has multiplicative Mahler measure one.
Multiplicativity therefore preserves the full \(M\) and total logarithmic \(m\), including every original factor and its multiplicity.
Neither a noncyclotomic factor nor an irreducible core is substituted for the complete polynomial.

<a id="source-check"></a>
## Accepted source and application boundary

The accepted DS17-U001 consequence was matched directly to [arXiv:1606.04376v2](https://arxiv.org/pdf/1606.04376v2), p.2, the definition of \(H_k\) and Theorem 2, with the normalization on p.1.
For fixed support bound, the primary statement isolates zero among total logarithmic measures of integer Laurent polynomials, without degree, coefficient-height or irreducibility restrictions.
Its nonzero univariate specialization therefore applies to the actual completion above.
The original foundational proofs were not re-audited; the source unit's accepted inspection limits are preserved.
No numerical value or uniform law for the gap is inferred.

Consequently each fixed K gives a positive gap for the complete P whenever its measure exceeds one.
Along a hypothetical positive-to-one sequence in this presentation, bounded actual completion support on any infinite subsequence would contradict that gap.
The number of effective perturbation terms must therefore escape fixed bounds as well, because a bounded number would imply the displayed uniform support bound.
An unbounded formal term list by itself supplies no such escape when cancellations keep actual support bounded.
The mentions of C221 and L19 credit the existing mechanism; the new application uses the source theorem directly and imports none of C221's irreducibility hypotheses.

<a id="controls"></a>
## Both exact conductor-11 controls

For \((p,r,s,L,k)=(11,6,5,3,1)\), the selected indices satisfy even the optional stronger neutral-block condition.
On \(A=C=-H\), the perturbation is \(Ht(t+2)\), so the endpoint is 12 and the derivative is \(2H\).
Its residue-coordinate change is \(Ht(E_3+E_4)=HtB_4\), giving the displayed value formula.

The sine representation of \(B_4\) gives its stated values at nodes 5, 2 and 4 exactly.
At the last node, the necessary magnitude exceeds one; the comparison follows already from \(c>\sqrt3/2\) and \(0<\sin(u/2)<1\).
At node 2, \(0<b_2<1\) and \(B_4(b_2)<-1\), so its negative-threshold magnitude is strictly below one.
Every H satisfying the necessary last sign therefore makes node 2 negative.
At node 4, both \(b_4\) and \(B_4(b_4)\) are negative, and that H is positive; hence the perturbation is strictly positive there while the neutral term is nonnegative.
The later positive node contradicts the chamber for every real H, without a parameter scan.

For the second control, independent exact polynomial arithmetic gives
\[
P^{(0)}_{6,5,0}-P^{(0)}_{4,7,0}=z^4(1+z^2)^2=z^6t^2,
\]
which verifies the neutral trace difference and equation (11).
In particular \((A,C)=(4,-1)\) produces exactly the old conductor-11 polynomial, with ascending coefficients
\[
(1,1,4,4,4,4,2,4,4,4,4,1,1).
\]
The exact two-term completion, constant coefficient, endpoint and equal-amplitude lift identity were also checked directly at this boundary case.

The retained survivor construction and the called complete-root evaluator were inspected at the functions actually used.
Exact factor reconstruction precedes root evaluation; all roots, factor exponents and root multiplicities enter the measure product, while exact cyclotomic factors contribute one.
Balls meeting the unit circle are retained conservatively rather than dropped.
A bounded reproduction for this same conductor-11 polynomial at 128 and 256 bits confirmed twelve roots with multiplicity and strict containment in
\[
2.759883858<M(P)<2.759883859.
\]
The two enclosures overlapped and agreed with the retained coefficients.
This checks the numerical value only for the already identified polynomial, not for an unsearched two-term family.
The source's ordinary arithmetic-library trust boundary remains; no separate implementation audit of Arb or FLINT was performed.

<a id="prefix-combination"></a>
## Conditional prefix consequence and unresolved scope

The family retains exactly the original \(x=0\) profile through \(L\), and its length ranges fall within C881v3's allowed range.
Thus, once the strict chamber and endpoint hold, the cited theorem bounds the complete measure by the stated expression.
No independent existence or nonneutrality premise is supplied by breaking the double profile factor.
The length-140 specialization was checked by the exact positive integer difference
\[
6^{35}-568\cdot5^{35}=65973229805948225794283176.
\]
It is a conditional finite-target implication, without selecting a conductor or cut that could conflict with C881v3's separate fixed-parameter obstruction.

For each fixed term count, the logarithm of the prefix upper bound tends to zero, while the completed polynomial has a fixed positive logarithmic gap away from zero.
For sufficiently large L, the two inequalities force \(m(P)=0\) at every such chamber point.
This uses neither a numerical gap estimate nor a monotonicity law in K.
It consequently does not exclude an individual two-term input with \(1<M(P)<6/5\), and it supplies no construction when effective support grows.

<a id="adjacent-support-review"></a>
## Finding and limitations

No substantive mathematical defect was found in L464v19 at the complete assigned scope.
The exact algebra, fixed-support bound, source applicability, complete-measure preservation, two conductor-11 controls and conditional prefix combination are supported as stated.
The whole family with any fixed number of these central perturbation terms has a positive total logarithmic gap away from zero whenever its complete measure is nonneutral.
The equal-amplitude conductor-11 line fails the chamber, while its separate \((4,-1)\) control is an identical representation of the old survivor and provides no small-measure improvement.

This review proves no effective value of the fixed-support gap, no exclusion of every finite \(1<M<1.2\) input, no growing-support construction and no completion of the unrestricted Task.
The accepted external theorem and the fixed prefix theorem retain their original proof-inspection boundaries.
Only this review material was authored; no L, S, T, E, program or Git modification and no mathematical adoption was made by the reviewer.

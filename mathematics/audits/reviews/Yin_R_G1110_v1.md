---
author: Yin
---

# Independent review of the finite signed central-amplitude census

<a id="scope"></a>
## Review act and exact scope

The review was performed at 2026-11-09T17:50 UTC by a separately arranged agent acting for Yin.
This reviewer did not develop the inspected mathematics or program and received no substantive development dialogue, author explanation or exploration summary.
The supplied context identified the assignment, fixed input locations and execution limits.
The reviewer read the fixed mathematical inputs directly and did not read D20 or any earlier R finding.
The dependency materials' own assessment prose was visible, but no earlier review was used as a substitute for checking the interfaces below.
This is an independent initial review of the complete signed finite reduction and computation in J157, including its positive-amplitude subset, rather than a review of an unrestricted all-conductor theorem or Task completion.

The inspected J README and native source are the working-checkout revisions supplied as stable inputs for this review at the stated minute.
The exact mathematical dependencies are C884v1, C881v3 and L462v11 at the anchors below.
No source repair was made.

## Inputs

- [J157 scope](../../computations/programs/Yin_J_G0157/readme.md#scope) defines the integral lift, signed amplitude reduction and original strict chamber.
- [J157 arithmetic](../../computations/programs/Yin_J_G0157/readme.md#method) describes the Arb and exact-gcd decisions.
- [J157 finite result](../../computations/programs/Yin_J_G0157/readme.md#results) states the complete finite counts and the two surviving inputs.
- [J157 native program](../../computations/programs/Yin_J_G0157/amplitudes.py) supplies the complete grid, parameter loops, sign checks, exact fallback and output accounting.
- [C884v1 pole values](../../claims/Yin_C_G0884_v1.md#all-r-pole-values) supplies the original-grid neutral and perturbed residue-coordinate interface, including unreduced representatives.
- [C884v1 endpoint](../../claims/Yin_C_G0884_v1.md#endpoint) and [amplitude argument](../../claims/Yin_C_G0884_v1.md#fixed-amplitude) supply the endpoint calculation and positive-amplitude comparison that J157 extends to signed amplitudes.
- [C881v3 original domain](../../claims/Yin_C_G0881_v3.md#original-domain) supplies the full odd grid, positive residue weights and strict endpoint convention.
- [C881v3 recurrence](../../claims/Yin_C_G0881_v3.md#prefix-coordinates) supplies the exact congruence defining the deformation in residue coordinates.
- [L462v11 neutral supply](../../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) supplies the integral neutral lift and its pole residues.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite signed-amplitude finding](#signed-amplitude-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [J157 signed reduction](../../computations/programs/Yin_J_G0157/readme.md#scope) | Every integer amplitude under the stated p,m,L hypotheses, the signed lower bound and independent strict endpoint. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [J157 arithmetic method](../../computations/programs/Yin_J_G0157/readme.md#method) | Strict Arb comparisons, exact gcd rejection, fallback and accounting semantics. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [J157 finite outcome](../../computations/programs/Yin_J_G0157/readme.md#results) | Both complete finite modes through odd conductor 101, exact coverage counts and success list. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [J157 native program](../../computations/programs/Yin_J_G0157/amplitudes.py) | Entire inspected source, all loops and sign decisions, output scope and both complete reruns. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [C884v1 pole interface](../../claims/Yin_C_G0884_v1.md#all-r-pole-values) | Actual original-grid h-values for every permitted r, including polynomial reduction modulo B_n. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [C884v1 endpoint](../../claims/Yin_C_G0884_v1.md#endpoint) | Neutral endpoint and linear perturbation evaluation used for arbitrary signed A. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [C884v1 amplitude bound](../../claims/Yin_C_G0884_v1.md#fixed-amplitude) | Positive-amplitude input comparison and its explicitly rechecked signed extension in J157. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [C881v3 original domain](../../claims/Yin_C_G0881_v3.md#original-domain) | Full simple odd grid, positive residue weights and endpoint equivalence used by this computation. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [C881v3 recurrence interface](../../claims/Yin_C_G0881_v3.md#prefix-coordinates) | Congruence D E_L = B_(n-L-1) modulo B_n in the permitted index range. |
| [Finite signed-amplitude finding](#signed-amplitude-review) | [L462v11 neutral supply](../../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) | Integral reciprocal trace lift, fixed quotient and exact neutral residues specialized to x=0. |

<a id="interface-checks"></a>
## Original polynomial and signed reduction

The neutral polynomial is integral because the even binomial supplies the factor \(1-z^2\) and the odd binomial supplies \(1-z\).
Its reciprocal trace is monic of degree \(n+1\), and the perturbation \(-AtB_{n-L-1}\) has degree \(n-L<n\).
It therefore leaves the original quotient by \(B_n\) unchanged.
Its lifted lowest power is \(z^{L+1}\), so it preserves the neutral prefix through index \(L\), the constant coefficient and the leading coefficient.
For integral \(A\), the trace and lift remain integral.

The exact recurrence congruence identifies the changed canonical coordinate with \(-AtE_L\) modulo \(B_n\).
The neutral residue formula and \(4-b_j^2=4\sin^2\theta_j\) give \(h^{(0)}(b_j)=b_j^2E_{m-1}(b_j)^2\).
Consequently the program evaluates the original residue coordinate at every original node, even when the displayed polynomial has degree at least \(n\).
The positive factors \(\nu_j\) preserve these signs.
The full grid is decreasing and consists of all \(n\) distinct real roots of the monic polynomial \(B_n\), for composite as well as prime odd \(p\).

At the last node, \(b_n=-2\cos(\pi/p)\), the parity formulas in the README give its displayed two-term expression exactly.
The neutral term is strictly positive because \(0<m\pi/p<\pi/2\).
The coefficient of \(A(-1)^L\) is also strictly positive because \(L+1\le n<p/2\).
Thus a strictly negative last value forces \(A=(-1)^{L+1}B\) with \(B>0\); zero and all opposite-sign amplitudes fail immediately.
For \(q=(L+1)/2\), the integer condition \(L<2m\) implies \(m\ge q\), including even \(L\) and half-integral \(q\).
Monotonicity of sine and \(\tan(qu)>q\tan u\), with \(u=\pi/p\), prove the strict bound \(B>q\) without an integer-parity assumption on \(q\).
Hence the first enumerated integer is exactly \(\lfloor q\rfloor+1\).

The neutral endpoint is \(4m\), and direct substitution in the lifted perturbation gives \(P(-1)=4m+2A(-1)^L\).
Under the necessary signed choice this is \(4m-2B\), so the independent strict endpoint is equivalent to \(B<2m\).
Equality at either excluded boundary cannot satisfy the required strict conditions.
The finite reduction therefore omits no successful integer amplitude for any permitted triple.

<a id="program-checks"></a>
## Program, arithmetic and coverage

The program enumerates every odd \(p\) from 9 through 101.
The upper bound \(m\le(p-5)/2\) is exactly the implied condition \(s=p-2m\ge5\), and \(m\ge2\) is exactly \(r\ge4\).
The exclusive upper bound \(\min(2m,s,n)\) on \(L\) implements both \(L<\min(r,s)\) and \(L\le n-1\).
The positive mode starts at 3 with step 2, covering every permitted odd \(L\); the signed mode uses step 1 and adds every permitted even \(L\) with negative \(A\).
The amplitude loop implements precisely the two integer bounds just established.
Parameter labels are retained separately even if some resulting algebraic objects coincide.

All grid inputs, sine ratios and subsequent sign expressions are Arb balls, with no conversion to ordinary floating-point signs.
The denominator sine is nonzero on the full grid.
The strict comparisons are sufficient sign certificates; a positive last value or negative first value already rejects a candidate, independently of uninspected nodes.
For the remaining candidates the program checks all nodes, identifies every unresolved ball, and uses an exact integer-polynomial gcd before accepting any complete sign pattern.
A nonconstant gcd with \(B_n\) certifies a genuine forbidden original-node zero, because all roots of \(B_n\) are exactly the simple real grid nodes.
A constant gcd sends the candidate to 512-bit evaluation, followed by an explicit error if a sign remains unresolved.
The return to 128-bit context is correctly placed after that fallback.

After zero exclusion, forbidding a transition from \(-1\) to \(+1\), together with a positive first and negative last value, is equivalent to one nonempty initial positive block followed by one nonempty terminal negative block.
The reported number of negative states is therefore the correct \(\kappa\).
Each enumerated amplitude receives one outcome, and each conductor's assertion checks the complete outcome sum.
Reason counts follow that priority order; they do not count every obstruction that might hold for the same input.
The output is constructed only after the calculation returns, and incomplete or unresolved calculations do not supply a new successful result.

<a id="reproduction"></a>
## Performed reproduction and auxiliary checks

Both native complete modes were rerun with CPython 3.14.7 and python-flint 0.9.0, using the following repository-root commands and the already available package location on PYTHONPATH:

~~~text
python -B mathematics/computations/programs/Yin_J_G0157/amplitudes.py --output mathematics/computations/outputs/Yin_J_G0157/amplitudes_review.json
python -B mathematics/computations/programs/Yin_J_G0157/amplitudes.py --signed --output mathematics/computations/outputs/Yin_J_G0157/amplitudes_signed_review.json
~~~

The reviewer outputs are [positive reproduction](../../computations/outputs/Yin_J_G0157/amplitudes_review.json) and [signed reproduction](../../computations/outputs/Yin_J_G0157/amplitudes_signed_review.json).
Every mathematical field matched the corresponding existing author output, including all 47 conductor rows; only elapsed-time fields were excluded from this comparison.
Neither run used a precision refinement.

| Mode | Triples | Amplitudes | Last positive | First negative | Extra transition | Exact zero | Success |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Positive | 9500 | 283200 | 250726 | 19350 | 12272 | 850 | 2 |
| Signed | 18424 | 561500 | 497394 | 19350 | 42198 | 2556 | 2 |

An independent domain enumeration used \(1\le m\le n\), \(3\le L<n\), the direct inequalities \(L<2m\) and \(L<p-2m\), and integer \(1\le B<2m\) satisfying \(2B>L+1\).
It reproduced every conductor's triple and amplitude count in both modes and verified every outcome sum.
Additional exact checks at every conductor verified \(\deg B_n=n\), \(\gcd(B_n,B_n')=1\), \(B_n(-2)=(-1)^n\), and the needed recurrence congruences for all permitted \(L\).
At 256-bit precision, independent recurrence evaluation of \(E_k(b_j)\) overlapped the sine formula for every node and every \(0\le k<n\) throughout the conductor range, and the recurrence evaluation of \(B_n(b_j)\) contained zero.
Those overlap checks are arithmetic consistency checks; the exact identities and root description are justified by the mathematical argument, not inferred from interval overlap.
For the two successful inputs, a separate direct evaluation of \(2b_j^2(3-b_j^2)\) verified the full patterns \((+,+,+,-)\) at conductor 9 and \((+,+,+,+,-)\) at conductor 11.

<a id="signed-amplitude-review"></a>
## Finding and limitations

No mathematical or computational defect was found in the inspected signed reduction, original-pole interface, finite enumeration, exact sign decisions or reported accounting.
The finite result is supported for every integer amplitude and every permitted triple with odd conductor from 9 through 101.
The complete success list is exactly
\[
(p,r,s,L,A,\kappa)=(9,4,5,3,3,1),\qquad(11,4,7,3,3,1),
\]
with \(P(-1)=2\) in each case.
The signed census includes the positive census, so their counts are not disjoint and must not be added.
The additional negative-amplitude cases supply no success in this finite range.

This finding does not prove an exclusion for conductors above 101, compute complete Mahler measures, prove nonreal residual pairs, or discharge the unrestricted integer-completion question.
The mathematical dependencies were checked at the interfaces declared above; this is not a fresh review of every theorem elsewhere in those materials.
The computation relies on the usual correctness of python-flint's Arb and exact polynomial arithmetic; no separate implementation audit or formal verification of that library was performed.
The retained source and its analytic reduction provide reproduction without the ignored output files.
Adoption belongs to the responsible mathematical decisions and is not made by this review.

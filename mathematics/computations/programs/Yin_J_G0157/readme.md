---
author: Yin
---

# Integer amplitudes in a central neutral-block deformation

This computation tests signed growing amplitudes using the exact pole interface in [C884v1](../../../claims/Yin_C_G0884_v1.md#all-r-pole-values).
The separate [all-conductor positive-amplitude theorem](../../../claims/Yin_C_G0884_v2.md#statement) classifies the positive sector.
The [independently reviewed signed theorem](../../../claims/Yin_C_G0884_v3.md#decision-signed-amplitudes-reviewed) now classifies the whole single-term family at every permitted conductor.
That analytic proof uses no finite-census premise; this computation retains its distinct reproducible finite scope.
It covers the explicit finite range of odd conductors from 9 through 101, all permitted block lengths and matching lengths, and every remaining integer amplitude.
The positive-amplitude and signed-amplitude modes have both been executed completely.
The [independent finite-computation review](../../../audits/reviews/Yin_R_G1110_v1.md#signed-amplitude-review) verifies the signed reduction, original-grid interfaces, complete parameter coverage, arithmetic and both reproduced outputs.

<a id="scope"></a>
## Exact domain and finite reduction

Put \(p=2n+1\), \(r=2m\), \(s=p-2m\), with \(3\le L<\min(r,s)\) and \(L\le n-1\).
The investigated integer polynomial is the original lift of
\[
 Q=Q^{(0)}_{r,s,0}-A tB_{n-L-1},\qquad A\in\mathbb Z.
\]
Its pole-coordinate values are
\[
 h(b_j)=b_j^2E_{m-1}(b_j)^2-A b_jE_L(b_j),
 \qquad b_j=2\cos(2\pi j/p).
\]
The strict chamber requires a nonempty initial positive block and a nonempty terminal negative block.
The independent endpoint is \(P(-1)>0\).

The finite amplitude reduction also covers negative amplitudes, beyond C884's fixed-positive-amplitude assertion.
Write \(u=\pi/p\), \(c=\cos u\), and \(q=(L+1)/2>1\), which may be a half integer.
The last value is
\[
 h(b_n)=\frac{4c^2\sin^2(mu)}{\sin^2u}
       +\frac{2A(-1)^L c\sin((L+1)u)}{\sin u}.
\]
All sine factors are positive because \(m<p/2\) and \(L+1\le n<p/2\).
Strict last negativity therefore forces \(A=(-1)^{L+1}B\) with \(B>0\).
Since \(m\ge q\), monotonicity of sine and strict convexity of tangent give
\[
 B>\frac{2c\sin^2(mu)}{\sin u\sin(2qu)}
   \ge\frac{c\tan(qu)}{\sin u}>q.
\]
The endpoint becomes \(P(-1)=4m-2B>0\), so \(B<2m\).
Thus every potentially successful integer amplitude is included in
\[
 A=(-1)^{L+1}B,\qquad
 \left\lfloor\frac{L+1}{2}\right\rfloor+1\le B<2m.
\]
The positive mode uses odd \(L\); the signed mode additionally includes every permitted even \(L\) with negative \(A\).
The zero amplitude has no negative pole and is excluded by the same argument.

<a id="method"></a>
## Arithmetic and coverage

The [native program](amplitudes.py) forms all grid values with 128-bit Arb balls using the sine formula for \(E_k\).
A strict Arb comparison proves the corresponding sign.
Necessary last and first signs are inspected before the remaining nodes.
When all inspected nonzero signs permit further consideration but a ball meets zero, the program computes the exact integer gcd of \(B_n\) and \(t^2E_{m-1}^2-A tE_L\).
A nonconstant gcd certifies a zero at an original grid node, since all roots of \(B_n\) are precisely those simple real grid nodes.
Such an input fails the strict chamber.
If that gcd is constant, the program recomputes the signs at 512 bits and aborts on any remaining undecided case.
No fallback precision increase was needed in either completed range.
Every candidate has one recorded outcome; reason counts follow the program's checking order and need not enumerate all possible failures of an input.
All sign-positive and sign-negative blocks are checked, with multiplicity of parameter labels retained.

<a id="results"></a>
## Complete finite outcome

| Mode | Parameter triples \((p,m,L)\) | Integer amplitudes tested | Strict chamber and endpoint successes |
| --- | ---: | ---: | ---: |
| Positive amplitudes | 9500 | 283200 | 2 |
| All signed amplitudes | 18424 | 561500 | 2 |

The signed mode includes the positive mode, so these counts must not be added as disjoint trials.
Both modes return exactly
\[
 (p,r,s,L,A,\kappa)=(9,4,5,3,3,1),\qquad(11,4,7,3,3,1).
\]
Both have \(P(-1)=2\).
The signed outcome classifies 497394 inputs by a positive last value, 19350 by a negative first value, 42198 by an extra sign transition, and 2556 by an exact zero grid value.
These counts plus the two successes total 561500.
The complete signed finite range contains no new feasible input.

This census is a finite pole-sign and endpoint result, not an all-conductor exclusion.
The all-conductor classification belongs to the separate [adopted C884v3 theorem](../../../claims/Yin_C_G0884_v3.md#decision-signed-amplitudes-reviewed).

<a id="survivor-measures"></a>
## Complete measures of the two survivors

The separate [survivor evaluator](survivor_measures.py) constructs the original integer lifts from the neutral product and the displayed perturbation, then certifies their complete Mahler measures.
It uses the [J156 all-root evaluator](../Yin_J_G0156/readme.md#arithmetic-and-fixed-settings) at both 128 and 256 bits, with exact factorization-product and root-multiplicity checks.
Both executions verify the following strict rational enclosures, with overlapping precision-refined intervals and the same exact normalized core.

| \(p\) | Original coefficients in ascending order | Certified total measure |
| --- | --- | --- |
| 9 | \((1,1,4,4,4,6,4,4,4,1,1)\) | \(2.853749309<M(P)<2.853749310\) |
| 11 | \((1,1,4,4,4,4,2,4,4,4,4,1,1)\) | \(2.759883858<M(P)<2.759883859\) |

Thus neither surviving chamber input meets the target \(1<M<6/5\).
These complete-measure computations are separate from the finite sign census and are not premises of C884v3's analytic proof.
They do not exclude integer deformations outside the single-term family classified there.

## Reproduction

Use Python with `python-flint==0.9.0` and run from the repository root:

~~~text
python -B mathematics/computations/programs/Yin_J_G0157/amplitudes.py
python -B mathematics/computations/programs/Yin_J_G0157/amplitudes.py --signed
python -B mathematics/computations/programs/Yin_J_G0157/survivor_measures.py
~~~

The sign-census program has no dependency on a previous generated result or on the sampler's proposal laws.
Its native exact coefficients are generated by the displayed recurrence.
The positive output is [amplitudes.json](../../outputs/Yin_J_G0157/amplitudes.json), and the signed output is [amplitudes_signed.json](../../outputs/Yin_J_G0157/amplitudes_signed.json).
These ignored results are reproducible from the retained source; `--max-p` supports smaller odd endpoints from 9 through 101, and `--output` chooses an explicit replacement output.
Only a complete calculation writes its result file.
The separate survivor evaluator imports J156's retained certifier, changes its precision only in its own process, and writes [survivor_measures.json](../../outputs/Yin_J_G0157/survivor_measures.json).
Its source contains both exact construction parameters and the rational interval checks, so no prior generated certificate is needed for reproduction.

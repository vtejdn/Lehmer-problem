---
author: Yin
---

# Integer pole completion of the first continuous cover

<a id="scope"></a>
## Exact finite scope and original implication

This calculation treats only \((O,V,W)=(10,18,27)\) at conductor 19683, cut 1990, and the original negative-one \(N=7,U=1\) branch.
The [integer-pole argument](../../../claims/Yin_C_G0882_v10.md#integer-pole) forces \(h(-1)=32\) under the original resultant and moment conditions.
The [partial-fraction argument](../../../claims/Yin_C_G0882_v10.md#pair-pole) then imposes
\[
 ((s+1)^2-d)(1-3s^2-d+2ys)>9(-1-y)32/19683,
 \qquad y=-161/100.
\]
For \(1<M(P)\le101/100\), the [adopted complete-domain reduction](../../../claims/Yin_C_G0882_v9.md#proof-boundary) puts the nonreal pair inside the closed rectangle used below.
The first two implications belong to the new Claim, whose assessment and independent review are separate from this computation record.

<a id="complete-result"></a>
## Fixed complete result

The native [pole_pair.py](pole_pair.py) retains the previous 4096 equal closed \(s\) cells on \([-6/5,-1/3]\), the entire \(d\) interval \([-1/10100,0]\), and the whole inherited cut enclosure.
It reuses the four [fixed rational duals](inputs/endpoint_first_duals.json) and the unchanged [continuous verifier](endpoint_dual.py) and [symmetric interval evaluator](endpoint_cover.py).
After the first four tests, the new pole inequality is checked on every remaining whole cell.
There is no numerical optimizer, new polynomial proposal, degree or conductor scan.

The single prescribed run completed with first-success counts
\[
                       (3739,203,66,17,71)
\]
and zero unresolved cells.
For the 71 cells requiring the integer-pole test, the minimum directed lower gap exceeds 0.0043619.
Every cell, including its boundary, is covered at 256-bit Arb precision; nonfinite values cause failure.
Interval multiplication handles the squared expression across zero without invoking a generic real power.
The old four-dual incomplete result remains correct at its old scope.

This finite result supports exclusion of \(1<M(P)\le101/100\) for the first triple once the new arithmetic proof is accepted.
It does not exclude \(M(P)=1\), test the four other triples, or settle any growing-conductor question.

<a id="reproduction"></a>
## Reproduction and retained inputs

With Python 3.14.7, SymPy and python-flint 0.9.0, run from the repository root:

~~~text
python -B mathematics/computations/programs/Yin_J_G0151/pole_pair.py
~~~

The program recomputes all required bounds directly from the retained programs and fixed coefficient JSON.
No previously generated cover file is required.
Its replaceable output is mathematics/computations/outputs/Yin_J_G0151/pole_pair_cover.json.
The exact five rational-pole bounds have their separate [rational reproduction](rational_pole.md).
The [independent complete finding](../../../audits/reviews/Yin_R_G1107_v27.md#integer-pole-shell-review) checks the new argument and full cover, and its [native finding](../../../audits/reviews/Yin_R_G1107_v27.md#integer-pole-native-review) records successful reproduction and the computational limits.

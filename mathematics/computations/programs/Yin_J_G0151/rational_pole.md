---
author: Yin
---

# The forced value at the rational pole in the five N=7 branches

<a id="scope"></a>
## Fixed arithmetic question

[rational_pole.py](rational_pole.py) checks only the original \(p=19683\), \(k=1990\), \(\Delta=2^{4391}\), \(K=3\), \(L=4\), \(N=7\), \(U=1\) setting.
Its five triples are \((10,18,27),(11,20,33),(11,20,34),(11,21,36),(11,21,37)\).
The [layer arithmetic in C882v3](../../../claims/Yin_C_G0882_v3.md#argument) is reused rather than reproved.
The degree-one positive layer gives \(h(-1)=2^{t_1}\).
The layer parities and total exponent imply \(t_1\equiv5\pmod6\), while the positive mass bound leaves only \(h(-1)\in\{32,2048\}\).
The [complete fixed-atom argument](../../../claims/Yin_C_G0882_v10.md#integer-pole) is retained in C882v10; [L464v17](../../../ledger/Yin_L_G0464_v17.md#forced-rational-value) owns the research question and remaining limits.

The computation checks five triples times two atom values, four small matrix forms per pair, and five inherited scalar layer costs.
The [independent native finding](../../../audits/reviews/Yin_R_G1107_v27.md#integer-pole-native-review) reproduces this fixed scope and checks the five matrix caps by a separate determinant calculation.
It uses standard-library rational arithmetic throughout, with no floating comparison, LP, conductor scan, higher-order moment search, or new dynamic program.
A 60-second limit is checked between the fixed cases and before completion; the cases contain only matrices of order at most three.
No result from the separate \(N=8\) certificate is used.

<a id="matrices"></a>
## Exact moments and atom removal

Let \(y=-161/100\), and use the positive weights \(\sigma_j=(2-b_j)(b_j-y)h(b_j)/p\).
Write \(s_i=\sum_j b_j^i\sigma_j\), and \(R=(K,L,N,O,V,W)\).
The six known moments are reconstructed from
\[
 s_0=261/100,\qquad s_{i+1}=R_{i+1}-yR_i-2s_i\quad(0\le i\le4).
\]
The rational pole has mass \(\lambda=183h(-1)/(100p)\), so its removal gives \(s_i'=s_i-\lambda(-1)^i\).
The four checked matrix forms are
\[
 [s_{i+j}]_{0\le i,j\le2},\quad
 [2s_{i+j}+s_{i+j+1}]_{0\le i,j\le2},\quad
 [2s_{i+j}-s_{i+j+1}]_{0\le i,j\le2},\quad
 [4s_{i+j}-s_{i+j+2}]_{0\le i,j\le1}.
\]
Every one must remain strictly positive definite after removing the rational pole from an actual input, since the remaining distinct poles retain strictly positive weights.
The program prints every exact leading principal minor.

For each matrix \(H\), the rank-one atom contribution is \(\lambda c\,vv^{\mathsf T}\), where \(v=(1,-1,\ldots)^{\mathsf T}\) and \(c=1,1,3,3\), respectively.
The program solves \(Hq=v\) by rational elimination, verifies the solution by direct multiplication, and gives the strict bound
\[
 h(-1)<\frac1{(183/(100p))c\,v^{\mathsf T}H^{-1}v}.
\]
For the second matrix, the exact upper bounds in triple order are
\[
 \frac{1890993681}{3916078},\quad
 \frac{35503342470}{58516507},\quad
 \frac{211554917910}{210917321},\quad
 \frac{30336347205}{97326293},\quad
 \frac{196053932115}{327346679}.
\]
All lie strictly between \(32\) and \(2048\).
These fractions were first supplied by the main agent's short probe and reproduced by this separate rational implementation as collaborating author work, not independent review.
The general point-mass mechanism has [checked Christoffel attribution](../../../audits/literature/Sim08/Yin_U001.md#point-mass-christoffel), with the source's finite-support limitation and the complete local squared-polynomial proof distinguished explicitly.

<a id="result"></a>
## Completed finite result

The default run completed every stated case and forces \(h(-1)=32\) in all five branches.
At this value all four reduced matrix forms are strictly positive definite for every triple, so these matrix tests exclude no further branch.
The atom is retained explicitly; it is not optimized away before reporting a joint test.

The five layer weight lists and their globally proved minima are inherited from [C882v3](../../../claims/Yin_C_G0882_v3.md#argument) and [C882v5](../../../claims/Yin_C_G0882_v5.md#higher-norm).
Their common attaining vector \((5,4,3,2,2,2,2,1,0)\) already has \(t_1=5\).
The program verifies the exponent sum, parity vector and all five attaining costs.
Consequently conditioning on \(t_1=5\) leaves those minima unchanged.
After subtracting the fixed first-layer contribution, the remaining-layer minima are \(1557027,1563411,1570827,215622,1570827\) in the program's LAYER_COSTS order.
This deduction uses the inherited global minima and a still-admissible attaining vector; it is not a new optimization.

<a id="reproduction"></a>
## Reproduction

Run from the repository root with Python 3:

~~~powershell
python -B mathematics/computations/programs/Yin_J_G0151/rational_pole.py
~~~

Only the standard library and the constants imported from [conductor19683.py](conductor19683.py) are required.
No generated output is an input; exact fractions and finite outcomes are printed to standard output.
The executed run used Python 3.14.7 and completed in less than one second.
The final COMPLETE line is printed only after every fixed case and attaining-cost identity passes.
Positive definiteness of these residual matrices does not prove existence of an integral \(h\), a root configuration, or an original branch.

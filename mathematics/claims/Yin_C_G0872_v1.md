---
author: Yin
---

# Sharp Mahler gaps for binomially divisible coefficients and rigidity of integral coefficient multipliers

Provenance: project deduction.
The argument uses the [binomial coefficient restriction](../ledger/Yin_L_G0460_v1.md#binomial-coefficient-classes) and [Mahler's normalized derivative inequality](../ledger/Yin_L_G0461_v1.md#normalized-derivative-descent).
The latter input is the statement of Corollary 1.2 on p. 256 of [Pri08](../audits/literature/Pri08/readme.md), at the existing statement-level inspection scope.
The developing agent checked the coefficient windows, the two sharp examples and the multiplier arguments for Yin.
The development checks preceded the independent review recorded in the assessment below.

<a id="statement"></a>
## Gaps and contraction bounds

Let \(d\ge1\) and let \(P(x)=\sum_{i=0}^d\binom di b_i x^{d-i}\), where \(b_0=1\) and all \(b_i\) are integers.
Write \(M\) for multiplicative Mahler measure.

1. If \(M(P)<2\), then \(P=x^d+b_d\) with \(b_d\in\{-1,0,1\}\), or \(P=(x+1)^d\), or \(P=(x-1)^d\).
   Each listed polynomial has measure one, and \(x^2+2x\) attains the positive-measure threshold \(M=2\).
2. If \(|b_d|=1\), the same classification holds under the larger bound \(M(P)<1+\sqrt2\).
   The unit polynomial \(x^2+2x-1\) attains \(M=1+\sqrt2\).
3. Fix \(d\) and a diagonal coefficient multiplier \(T(\sum a_i x^{d-i})=\sum \lambda_i a_i x^{d-i}\).
   Suppose \(T\) preserves monicity and integrality on all monic integer inputs, preserves constant term of modulus one on unit inputs, and satisfies \(M(TP)\le M(P)\) on all monic integer inputs.
   The complete list consists of the identity, \(P(x)\mapsto(-1)^dP(-x)\), and the endpoint projections \(P(x)\mapsto x^d\pm P(0)\).
   The entries in this list may coincide in degree one.
4. Let \(p=\sum a_i x^{d-i}\) be any monic integer unit polynomial with every \(|a_i|\le1\).
   Let \(q=\sum(-1)^i e_i x^{d-i}\) be a monic integer unit polynomial of degree \(d\) with \(M(q)=1\), possibly chosen depending on \(p\).
   If its finite free multiplicative convolution with \(p\) has integer coefficients, the resulting measure is either \(M(p)\) or one.
5. For an arbitrary monic integer unit polynomial \(p\), put \(A(p)=\max_{0<i<d}|a_i|\), taking the maximum over an empty set to be zero.
   Allow arbitrary substitutions \(p(x)\mapsto p(x^k)\), \(k\ge1\), and convolutions as in part 4 with the height restriction on \(p\) removed.
   Any chain starting at \(p\) and keeping positive logarithmic measure throughout has at most \(\max(0,A(p)-1)\) convolution steps whose kernel has two distinct roots.

<a id="windows"></a>
## Mahler contraction on contiguous coefficient windows

For an array \(c_0,\ldots,c_n\), use the polynomial of grade \(n\)
\[
 W(x)=\sum_{i=0}^n \binom ni c_i x^{n-i}.
\]
The grade counts the slots even when an endpoint is zero.
Use \(M(0)=0\) for the zero polynomial, so deleting coefficients from an identically zero window preserves every nonincrease assertion.
Grade reversal \(R_n W=x^nW(1/x)\) reverses the array and preserves \(M\), by the root-product formula and \(M(x)=1\).
For \(n\ge1\), \(W'/n\) deletes the last entry and has grade \(n-1\), by \((n-i)\binom ni/n=\binom{n-1}{i}\).
Its measure is at most \(M(W)\) by the derivative inequality with actual degree at most \(n\), including the constant case by convention.
Applying \(R_{n-1}\) after normalized differentiation of \(R_n W\) deletes the first entry with the same bound.
Successive deletions from the ends therefore give
\[
 M\!\left(\sum_{i=0}^k\binom ki b_{j+i}x^{k-i}\right)\le M(P)
 \qquad(0\le k\le d,\ 0\le j\le d-k).
\tag{1}
\]
In particular each \(|b_j|\le M(P)\).

<a id="gap-two"></a>
## Quadratic windows and the threshold two

Suppose \(M(P)<2\).
All entries have absolute value at most one.
In a triple \((u,b,w)\) with \(b\ne0\), the window polynomial is \(u x^2+2b x+w\).
If \(u=0\), its leading coefficient gives measure at least two.
If \(w=0\), removing the factor \(x\) gives the same bound from the resulting constant coefficient.
If \(uw=-1\), the two roots have absolute values \(1+\sqrt2\) and \(\sqrt2-1\).
Thus an interior nonzero entry forces both neighbors to be nonzero and equal.
It follows by induction along the array that either every interior entry vanishes, or all entries are nonzero and \(b_{i+2}=b_i\) throughout.
Since \(b_0=1\), the latter case gives coefficients \(b_i=1\) for all \(i\), or \(b_i=(-1)^i\) for all \(i\).
In degree one the interior is empty and the endpoint formula suffices.
The listed forms have measure one by the root-product formula, and the roots of \(x^2+2x\) give measure two.

<a id="sharp-unit-gap"></a>
## Unit inputs and the threshold \(1+\sqrt2\)

Write \(\eta=1+\sqrt2\) and suppose \(M(P)<\eta\) with \(|b_d|=1\).
By (1) all entries have absolute value at most two.
An interior entry of modulus two gives a quadratic \(u x^2+2b x+w\) with \(|b|=2\).
If either endpoint is zero, its measure is at least four by the preceding leading or constant coefficient argument.
Otherwise the larger root modulus multiplied by \(|u|\) is \(2+\sqrt{4-uw}\), a lower bound for its measure.
Unless \(uw=4\), the integer product \(uw\) is at most two, giving a bound greater than \(\eta\).
Thus an interior entry of modulus two forces both neighbors to have modulus two, which by propagation contradicts \(b_0=1\).
The unit endpoints now give \(|b_i|\le1\) for every index.

Suppose an interior \(b_j\ne0\) has \(b_{j-1}=0\).
For \(j\le d-2\), the cubic window starting at \(j-1\) has actual leading coefficient \(3b_j\), so its measure is at least three.
For \(j=d-1\), the unit left endpoint implies \(d\ge3\), and reversing the final cubic window gives the array \((b_d,b_j,0,s)\), where \(|s|\le1\).
Changing the overall sign and, if necessary, the sign of the variable and the overall sign together gives a monic cubic \(x^3-3x^2+t\) with \(|t|\le1\) and the same measure.
At \(x=\eta\) its value is at most \(\eta^2(\eta-3)+1=-1-\sqrt2<0\), so it has a real root strictly larger than \(\eta\).
These alternatives give contradictions.
Reversal of the whole unit array gives the same exclusion for a zero right neighbor.
If \(d=2\), both neighbors of its sole interior position are already nonzero.
Consequently any nonzero interior entry propagates nonzero entries throughout.
The quadratic window for opposite endpoints then has measure \(\eta\), which forces \(b_{i+2}=b_i\) as before.
The endpoint-only case includes \(d=1\).
Finally \(x^2+2x-1\) has roots \(-1\pm\sqrt2\) and has the claimed measure.

<a id="universal-diagonal-multipliers"></a>
## Classification of universal diagonal multipliers

Monicity gives \(\lambda_0=1\), and testing inputs whose \(i\)th coefficient is one gives \(\lambda_i\in\mathbb Z\).
The unit condition gives \(|\lambda_d|=1\).
Apply \(T\) to \((x+1)^d\).
The output has binomially divisible coefficients \(b_i=\lambda_i\) and measure one, because it is monic and the input has measure one.
Part 1 forces the constant or alternating sequence, or an array supported at the endpoints with last entry \(\pm1\).
These give exactly the displayed list in part 3.
The identity and sign change preserve the root moduli, and the endpoint maps have measure \(\max(1,|P(0)|)\le M(P)\) for monic \(P\).
They attain measure one on every unit input.
The classification already follows if the contraction condition is tested only on \((x+1)^d\), keeping the stated arithmetic hypotheses.

<a id="height-one-input-dependent-kernels"></a>
## Input-dependent kernels on height-one units

Use the [finite free multiplier convention](../ledger/Yin_L_G0461_v1.md#finite-free-contractive-kernels), in which the coefficient at index \(i\) of \(p\boxtimes_d q\) is \(a_i e_i/\binom di\).
Every root of \(q\) has modulus one because \(q\) has measure one, is monic and has constant coefficient of modulus one.
Thus \(|e_i|\le\binom di\), since \(e_i\) is a sum of that many products of unit-modulus roots, with roots indexed by multiplicity.
If any interior output coefficient is a nonzero integer, \(|a_i|\le1\) forces equality in this bound.
All the \(i\)-fold products have the same argument, hence all are identical.
For any two root indices, choose \(i-1\) indices outside both and compare the two products obtained by adjoining one of the chosen pair.
This is possible for \(1\le i\le d-1\) and proves that all the roots of \(q\) are equal.
The common root is real since \(q\) has real coefficients and is therefore \(1\) or \(-1\).
The coefficient multiplier becomes the identity or the normalized sign change and preserves \(M(p)\).
If every interior output coefficient vanishes, the output is \(x^d\pm1\), of measure one, including in degree one.
For the [original Lehmer polynomial](Yin_C_G0007_v1.md#statement), whose coefficients all have modulus at most one, both cases exclude a strict decrease to another positive logarithmic measure.
The argument allows arbitrary root geometry for \(p\) and requires the stated integrality of the actual convolution.

<a id="descent-length"></a>
## A bound on the number of steps allowing radical substitutions

If \(q\) has at least two distinct roots, the equality argument gives \(|e_i|<\binom di\) at every interior index.
Hence a zero interior input coefficient stays zero, while the absolute value of each nonzero interior input coefficient strictly decreases.
Integrality of the output forces \(A(p\boxtimes_d q)\le A(p)-1\) whenever \(A(p)>0\).
A kernel with only one distinct root acts by a sign change or the identity, preserving \(A\).
Substitution of \(x^k\) for \(x\) preserves \(A\) because it moves each old interior coefficient to a distinct interior position and inserts only zeros.
If \(A=0\), a monic unit polynomial is \(x^d\pm1\) and has measure one.
Thus a positive-logarithmic-measure chain keeps \(A\ge1\), which proves the bound in part 5 regardless of the substitution degrees or the choice of later kernels.
This count applies to whole radical substitutions.
Selecting a factor after substitution can change its coefficients, so the bound gives no limit on chains that also use that operation.

## Assessment history

### Decision binomial-gaps-and-multipliers

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:02 |
| status | proved |
| reason | The sharp binomial gaps and all integral-multiplier conclusions passed complete independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All five conclusions, sharp examples and the positive-chain bound. |
| argument | [Proof section](#windows) | Contraction on every contiguous coefficient window. |
| argument | [Proof section](#gap-two) | The sharp general threshold. |
| argument | [Proof section](#sharp-unit-gap) | The sharp unit threshold and boundary cases. |
| argument | [Proof section](#universal-diagonal-multipliers) | The classification of universal diagonal operators. |
| argument | [Proof section](#height-one-input-dependent-kernels) | The height-one input-dependent obstruction. |
| argument | [Proof section](#descent-length) | Integer descent with whole radical substitutions. |
| review | [Independent finding](../audits/reviews/Yin_R_G1100_v1.md#binomial-gaps-and-multipliers) | All of the selected statement and argument at the source scope specified in the finding. |

## Current assessment

[Selected decision](#decision-binomial-gaps-and-multipliers)


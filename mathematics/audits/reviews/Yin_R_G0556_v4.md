---
author: Yin
---

# Uniform cyclic norm estimates for varying Pisot seeds

<a id="moving-seed-transfer"></a>
## Transfer to the irreducible factor, including repeated torsion

At 2026-11-16T12:17 UTC a reviewer for Yin independently checked the full argument of C336v3 and its mathematical inputs at the scopes below.
The reviewer had previously audited the fixed plastic-seed result in C336v2 and received the fixed v3 text without its development discussion or author explanations.
The two-sided transfer estimate and both rate consequences follow under the stated hypotheses.

For \(R=(1+\theta_0)/2\), every interior root contributes a ratio of moduli at least one on \(|z|=R\).
For the exterior root the squared ratio is \((R^2+\theta^2-2R\theta\cos t)/(1+R^2\theta^2-2R\theta\cos t)\), minimized at \(t=0\).
Its resulting minimum before squaring increases with \(\theta\).
This gives a cutoff using \(\theta_0\) alone, including at zeros of the reversed polynomial by the cross-multiplied inequality.
The two circle counts give exactly one exterior root, counted with multiplicity.
Its inverse must belong to the same irreducible factor by the unit constant term.
The three torsion-conjugate equations have nonidentical rational sides by their exterior poles and yield at most \(4r+4r+2r\) distinct roots and order at most \(32r^2\) per root.
At a torsion zero of \(D\) of multiplicity \(v\), the derivative of \(z^Nf/g\) has a zero of order \(v-1\) if \(v>1\) and is nonzero if \(v=1\).
The cleared logarithmic derivative has nonzero constant term and degree at most \(2r\), giving \(\sum(v-1)\le2r\) over the torsion roots even when multiplicities vary with \(N\).

For each phase the integral upper bound \(M(Q_w)\le2\Theta\) gives a bound on the complete measure of the integral product \(V\).
Every nonzero phase root therefore has minimal-polynomial degree \(O_j(r)\) and logarithmic measure \(O_{j,\Theta}(1)\), including in the presence of leading-coefficient cancellation.
Reciprocal inversion preserves both quantities and removes exactly the exterior contribution from the logarithm of the distance.
The two-logarithm argument applies with exponent \(p=jd\) of either parity.
When the normalized modulus to power \(p\) is at least \(1/2\), the chosen logarithm has bounded modulus and the nearest multiple of \(2\pi\) gives an integer coefficient of magnitude at most \(p+1\).
The two modified algebraic heights each contribute \(O_{j,\Theta}(1/D)\) against the \(O(D^4\log(2D))\) theorem constant at field degree \(D\).
Thus the error per nontorsion root is \(O_{j,\Theta}(r^2\log(2r)\log(2d))\).
The other modulus range gives a constant lower bound, and the noncoincident torsion distances use only polynomially bounded orders.

In the retained-node product for \(Q_w\), removing the \(e=|E_w|\) nodes initially leaves a leading-coefficient power \(d-e\).
The factor \(|\operatorname{Res}(U_w,G_w)|\) in the denominator includes \(|l_w|^e\), which accounts for the power \(d\) in the displayed numerator.
Factoring each root with its multiplicity in \(Q_w\) and differentiating \(z^d-w\) at each shared node gives the remaining terms, also when the multiplicities in \(Q_w\) and \(H\) differ.
The removed power products are invariant under automorphisms fixing \(w\), and monic division keeps the residual coefficients integral over \(\mathbb Z\).
All phase resultants are nonzero and conjugation over \(\mathbb Q\) permutes them.
Their full product therefore has absolute value at least one, while the product of their elementary upper bounds has logarithm \(O_{j,\Theta}(r^2)\).

For the separate removal of \(H\) on retained nodes, distinct torsion points have separation \(\gg_j r^{-4}\), each occurrence in \(H\) is counted, and the derivative formula uses \(jd\) on the full grid.
For restoration on the omitted set, Galois stability gives the nonnegative lower bound on the *total* logarithm of \(|S(\eta)|\).
The Taylor coefficient \(D^{(v)}(\eta)/v!\) and the remaining torsion-root distances give its upper bound.
In summing this bound the derivative orders total at most \(12r\), and \(N+r=d+\deg H\le d+12r\).
Both removal and restoration cost \(O_{j,\Theta}(r\log(2d)+r^2\log(2r))\), including empty omitted sets.
The sum of the individual distance errors over \(O_j(r)\) phase roots gives the error in (1).

For offsets bounded below, the uniform phase limit gives \(m(V)/j\ge(\log\theta_0)/2\) for every sufficiently large \(j\).
Choosing one such \(j\) with \(j(\log\theta_0)/2>\log2+1\) leaves the stated margin after an \(o(d)\) transfer error.
The original-root product then gives \(m(S)\ge1/(2j)\).
The uniform phase argument uses compactness of the pole interval and of the bounded analytic functions, the nonzero integral linear coefficient at zero offset, and the surviving finite Blaschke product when the offsets are bounded below.
At every offset the eighth-power argument forces evenness of both \(A^2+B^2\) and \(A^4+B^4\) under the measure-one assumption, contradicting the seed parities or the zero-offset leading coefficient.
An integral polynomial with \(M(V)>1\) has either absolute leading coefficient at least two or, up to sign, a monic irreducible factor of measure greater than one and degree at most \(\deg V=O(r)\).
The cited weak Dobrowolski estimate applies to such a factor, with bounded degrees covered by finiteness.
The relative error in (2) is \(O_\Theta(r^3\log^4(2r)\log(2d)/d)\), which tends to zero throughout the given power range.
The review accepted the external logarithmic-form and Mahler-measure theorems at their recorded source scopes and checked their uses here.
Their original proofs lay outside this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Cyclic norm transfer](#moving-seed-transfer) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Cyclic norm transfer](#moving-seed-transfer) | [Statement](../../claims/Yin_C_G0336_v3.md#statement) | Both signs, the cutoff, the full two-sided uniform estimate, the single multiplier for bounded-below offsets, and the all-offset lower bound with its power range. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Torsion cofactor](../../claims/Yin_C_G0336_v3.md#cofactor) | Circle counts, irreducible factor, orders, degrees and total multiplicity of the cyclotomic cofactor. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Phase distances](../../claims/Yin_C_G0336_v3.md#distances) | Nonunit leading coefficients, degree and height of each phase root, inversion, nontorsion and noncoincident torsion estimates. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Shared torsion roots](../../claims/Yin_C_G0336_v3.md#transfer) | Full phase product, two distinct multiplicities, Galois-invariant integer resultants, removal of the cyclotomic cofactor and restoration of the original factors. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Rates](../../claims/Yin_C_G0336_v3.md#rates) | Exponent choice, original-unit certificate, weak degree-dependent measure and domination of the transfer error. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Uniform phase limit](../../ledger/Yin_L_G0462_v26.md#uniform-phase) | Analytic compactness proof and the fixed common multiplier on bounded-below offsets. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Eight-phase positivity](../../ledger/Yin_L_G0462_v27.md#eight-phases) | Positive complete measure at every offset for a coprime Pisot unit seed. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Height-normalized logarithmic form](../literature/Wus02/Yin_U001.md#wus02-u001) | External theorem statement, two height factors and degree dependence. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Power-distance argument](../../claims/Yin_C_G0895_v2.md#circle) | Direct complex-distance estimate at positive integer powers with variable field degree and bounded minimal-polynomial measure. |
| [Cyclic norm transfer](#moving-seed-transfer) | [Weak degree bound](../../claims/Yin_C_G0895_v1.md#transfer) | Positive-measure integral factor, actual irreducible degree and bounded-degree finiteness. |

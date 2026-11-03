---
author: Yin
---

# CFMZ26b-U001: finite Shannon deficit at the same quartic and the entropy-order direction

<a id="cfmz26b-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Cheng, Fang, Ma and Zhang, arXiv:2610.12072v1, 8 October 2026; [retained original HTML](../../../literature/pdf/CFMZ26b/arxiv-v1.html).
Public preprint, with no journal-publication assertion.

Passages: Introduction equations (1.1) and the finite entropy conventions, Theorems 1.1--1.2, Lemmas 6.1--6.2 and Proposition 6.3; surrounding explanation of the relation to the earlier collision paper.

Inspection: On 2026-10-26, salem_collision_literature directly read the selected statements, exact polynomial and finite-atom conventions, the congruence and Fourier-tail interfaces in Lemmas 6.1--6.2, and Proposition 6.3's hypotheses/conclusion. This is selected statement/applicability inspection, not a whole source-proof audit or quantitative verification. No new theorem from this sequel is accepted here.


## Exact potentially useful conclusion

The source uses independent fair signs, X_N=sum_(k<N)epsilon_k beta^(-k), and H_N=H(X_N) with natural logarithms and all coincident atoms merged.
Its P1 is exactly X^4-X^3-X^2-X+1.
The symbol R in this paper denotes beta/(beta-1), a support bound; it is NOT the project's exponential return radius.

Theorem 1.1 asserts Hausdorff dimension below one for every quartic Salem parameter.
More directly useful for the project, Proposition 6.3 supplies H_N<N log(beta) for one fixed finite N from its localized-orbit hypotheses.
Those hypotheses include the actual congruence Y_j^(k)=c_k beta^j modulo integers, a geometric localized right tail, 0<c_*<=|c_k|<=h<1/100, neutral amplitudes Delta_k decreasing to zero, and localized actions E_k=o(log(1/Delta_k)).
The surrounding construction is asserted to supply these conditions for P1 and P2.
This unit has not completed that construction's proof inspection.

For the SAME finite binary endpoint law, the elementary entropy-order comparison is H_2(X_N)<=H_1(X_N).
The exact conversion [CFMZ26-U001](../CFMZ26/Yin_U001.md#original-collision-and-energy-dimension) gives H_2(X_N)=-log(p_N).
Consequently a verified finite STRICT Shannon upper bound H_N<N log(beta) would imply p_N>beta^(-N), and hence R_project<beta.
This is the useful upper-bound direction; full Hausdorff dimension or a Shannon lower bound supplies no equality of the two entropy rates.
The sequel is therefore a genuinely relevant alternative strict-radius input, but the more direct collision paper already identifies the same original law.

The explicit deficits in Theorem 1.2 depend on separate finite verification materials and are not adopted here.
No selected passage classifies the critical first-return mean or supplies a positive linear conditioned-midpoint moment.
The accepted proof and verification scopes of the original collision paper and this sequel remain separate.

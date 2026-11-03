---
author: Yin
---

# Dim16-U001: the reported logarithmic-form bound and an all-index cyclic-norm consequence

Date: 2026-10-07.
Source inspection and direct specialization by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).
Bibliography and acquisition.

<a id="dim16-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Vesselin Dimitrov, *Convergence to the Mahler measure and the distribution of periodic points for algebraic Noetherian Z^d-actions*, arXiv:1611.04664v2, 1 January 2017; first public version 15 November 2016. Retained [Dim16.pdf](../../../literature/pdf/Dim16.pdf), 450537 bytes, 39 PDF pages.

Passages: Printed/PDF p.29, Section 9, equation (9.1) and its immediately preceding/following hypotheses; p.30 discussion of the degree dependence. Bibliographic identity and version are on p.1 and the versioned arXiv record.

Inspection: The retained identity page and pp.29--30 were rendered and visually read; text extraction was compared. The reported bound is accepted as an external Baker--Wustholz statement, not as a newly proved main theorem of Dim16. Its original transcendence proof and numerical absolute constant were not audited. The paper's main multivariable convergence theorem is not an input to this unit.


**Source interface read and accepted with the guards below.**
The direct specialization and finite-threshold deductions below are proved here.
This status does not claim a complete proof audit of the external logarithmic-form theorem, or a full-paper audit of Dim16.

<a id="dim16-reported-bound"></a>
## The exact adopted interface

For a nontorsion nonzero algebraic number beta of degree D with bounded absolute logarithmic Weil height, Dim16 (9.1) reports

    -log|beta^b-1| <= kappa D^4 log D max(h(beta),1/D) log b.       (1)

The source says the implied constant is absolute.
We use only D>=2, b>=2 and h(beta)<=1.
Increasing kappa if necessary, fix one absolute kappa>=1 valid on this bounded-height scope.
No numerical value of kappa is supplied or certified by this unit.

The displayed source discusses b in N, but its literal log b right side at b=1 is not a valid general upper bound.
We therefore adopt (1) only for b>=2; the n=1 cyclic-norm case below is established separately by integrality.
Degree-one nontorsion algebraic units do not occur.
The source's D in Section 9 is algebraic degree, whereas its d elsewhere often counts variables; they are not interchangeable.
The h(beta) in (1) is Weil height, not coefficient height.

The source attributes (1) to Baker--Wustholz, with its references [9] and [10].
We have read the reported specialization, not those original proofs.
Its p.30 discussion of a possible much stronger bound is explicitly hypothetical and is not adopted.
Historical statements there about the state of the art are not current-status conclusions.

<a id="dim16-cyclic-all-index"></a>
## Direct all-index specialization for the near-one unit domain

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P, degree d>=2 and 0<m=log M(P)<=1.
Set

    C_n=|Res(P,t^n-1)|=|Norm_(Q(alpha)/Q)(alpha^n-1)|,
    K=kappa d^4 log(2d),

where kappa>=1 may be enlarged from (1).
Then, for every n>=1,

    n m-K log(2n) <= log C_n <= n m+d log 2.                    (2)

To prove this, normalize each complex conjugate alpha_i separately:

    z_i=alpha_i        if |alpha_i|<=1,
        alpha_i^(-1)   if |alpha_i|>1.

Thus |z_i|<=1, and all d normalized numbers remain nontorsion, have degree d and have Weil height m/d.
Inverting selected roots does not require a common splitting-field degree in (1): apply that one-number statement separately to each z_i.
Directly,

    C_n=exp(nm) product_i |1-z_i^n|.                            (3)

For n>=2, (1) and max(h(z_i),1/d)=1/d give a total logarithmic loss at most kappa d^4 log d log n, which is bounded by the loss in (2).
The upper bound follows from |1-z_i^n|<=2.
No root on the unit circle is omitted.
For n=1, C_1 is a nonzero integer, so log C_1>=0; also K log 2>=m on the stated domain.
This proves the remaining lower-bound case without applying log b at b=1.

<a id="dim16-polynomial-threshold"></a>
## A finite threshold, and its limitation

Define

    x=K/m,
    N=ceil(8x log(8x)).                                        (4)

Then every integer n>=N satisfies

    log C_n >= n m/2,
    [log C_n-d log 2]/n >= m/4.                                (5)

Here x>=1 and K>=d log 2.
Since x log(8x)>=1,

    N<=9x log(8x),
    2N<=18x log(8x)<=144x^2<=(8x)^4.

Consequently K log(2N)<=4K log(8x)<=Nm/2.
The function log(2t)/t decreases for t>=2, so the same relative error bound holds for every n>=N.
Also N>=4x>=4d log 2/m, hence subtracting d log 2 costs at most nm/4.
This proves (5).

In particular the bound has order

    N=O((d^4 log(2d)/m) log(d^4 log(2d)/m))

on 0<m<=1, with an absolute but numerically uncalibrated constant from the external statement.
This is a bound polynomial in d and 1/m up to the displayed logarithms, and it pays the archimedean d log 2 cost explicitly.
It is not a numerically certified search cutoff until an explicit valid kappa is supplied.
No numerical transcendence-constant optimization was attempted.

The conclusion controls every sufficiently large n.
By contrast, the independently proved [finite prime witness](../../../claims/Yin_C_G0260_v1.md#finite-cyclic-norm-prime-witness) finds at least one prime exponent with a smaller degree dependence for each fixed positive lower entropy threshold, and requires no logarithmic-form theorem.
The two conclusions have different quantifiers.
Both certify a positive fraction of the input's m; neither establishes a common positive lower bound for m in the first place.
In particular (4) grows as m decreases, and (5)'s guaranteed lower certificate also decreases.
No bound on the arithmetic prime factors of C_n follows.

## Relation to retained sources and actual review

The retained War05 periodic-point interface supplies a per-input asymptotic limit and keeps its Baker input external.
The inspected Smy08 Fejer/Blanksby interfaces do not themselves supply the all-n rate (2).
Dim16 (9.1) is selected for its explicit degree and height dependence; reconstruction of a polynomial from finitely many cyclic resultants is a different question and is not used here.
Only this one additional source was selected in the bounded search.

The source agent performed the stated local PDF inspection and self-checked (2)--(5).
No original Baker--Wustholz proof, full Dim16 proof or numerical constant was independently verified.
The coordinator read the complete unit and independently inspected the rendered original pp.29--30, checking the reported formula, height and degree conventions, exponent-one guard, and hypothetical status of the proposed stronger bound.
It checked the complete direct specialization (2)--(5), including the all-n threshold and the numerically uncalibrated constant.
Assigned AI review_matrix_completion independently checked those direct deductions and the comparison with L G0076; the original transcendence estimate remained its stated external premise.
Neither check found a substantive defect.
This does not assert independent verification of the original Baker--Wustholz proof or of any uninspected Dim16 theorem.

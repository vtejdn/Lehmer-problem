---
author: Yin
---

<a id="tao26-u003"></a>
# Tao26-U003: Nondegenerate multidimensional stationary phase and uniform parameter bounds

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: [Retained Tao26 PDF](../../../literature/pdf/Tao26.pdf), Terence Tao, author-hosted Lecture notes8for247B, undated22-page artifact identified by the existing acquisition account. The provisional2026 key is access-year based and gives no publication date.

Source passages: Printed/PDFpp9--12: Section3, Lemma3.1 on p9, Lemma3.3 beginning on p10 and equation(12) on p11, and the uniform-dependence paragraph on p11 continuing with parameter remarks on p12. The quadratic Lemma3.2 on p10 was read as context only.

Inspection: 2026-10-24T04:45, Yin through phase_bands, direct complete text extraction/read of retained PDFpp9--12 after a focused source search. Exact statement, dimension, smooth amplitude, stationary-point and nondegeneracy hypotheses, exponent and uniform-dependence paragraph checked. Proof exposition on these pages was read, but its omitted integration-by-parts details, preceding Fresnel lemmas and whole-source proof were not independently reconstructed or audited.
No new acquisition or visual-page inspection.

## Exact accepted input

For a real smooth phase phi on R^d and a smooth compactly supported amplitude a, write

    I_(a,phi)(lambda)=integral_(R^d) a(x)exp(i lambda phi(x))dx,
    lambda>0.

Lemma3.3 assumes a stationary point x0 with det Hess(phi)(x0)!=0 and no other stationary point on the support of a.
It gives an expansion indexed by n=0,...,N, with leading order lambda^(-d/2) and remainder of order lambda^(-N-d/2-1), all leading terms carrying the oscillation exp(i lambda phi(x0)).
Correction recorded2026-10-24T04:52: the sum in equation(12) has N+1 terms; this corrects the earlier phrase "after N terms" without changing the accepted decay consequence or its inspection scope.
Only the consequence abs(I_(a,phi)(lambda))<=C lambda^(-d/2) for lambda>=1 is accepted for the intended use.
No exact leading coefficient, signature formula or numerical implicit constant is used.
The source's displayed leading-coefficient normalization is therefore outside this unit's accepted numerical interface.

The paragraph on p11 specifies dependence of the error constants on the dimension, support diameter, finitely many uniform derivative bounds of the amplitude and phase, the nondegeneracy determinant at the stationary point, and a lower bound for the phase gradient outside a suitable small ball about that point.
It explicitly concludes uniform control for families in which those data are uniformly controlled.
Combining this control with the leading-order term gives a uniform C in the preceding bound when those data and the leading amplitude/derivative data are controlled.
Stationary points may vary with the parameter; the statement does not require them to lie inside the amplitude support when the amplitude vanishes in their neighborhood.
If the stationary point is outside the support, the same estimate remains valid under the stated gradient conditions.

Lemma3.1 separately gives decay of every fixed inverse-power order when the phase gradient does not vanish on the compact amplitude support.
This is recognized nonstationary-phase context; the intended consumer supplies its required single integration-by-parts bound directly, including the uniform linear-frequency parameters.

## Intended local application and obligations

The intended application has d=2, a fixed smooth amplitude supported in a small phase chart, lambda=k>=1, and phases phi_q(x)=phi(x)-q dot x with q=n/k and n in Z^2.
The phase Hessian is unchanged by the linear term.
Uniformity over ALL such q is not supplied merely by observing Hessian nondegeneracy at one point.
The consumer must construct a patch with quantitative definite Hessian, prove uniqueness and control of any stationary point in a larger patch, and pay a uniform gradient lower bound on the complementary frequencies.
For parameters whose stationary point lies in that larger compact patch, bounded q and fixed higher derivatives give the required derivative control.
A uniform bound of the form abs(gradient phi(x)-gradient phi(x0))>=lambda_0 abs(x-x0) supplies the specified gradient control away from x0.
These are local applicability obligations, not conclusions asserted here about the weighted Salem phase.

The probability-Haar Fourier convention on a two-torus introduces a factor(2pi)^(-2) relative to the displayed Euclidean integral.
A smooth amplitude supported strictly inside one angular chart may be extended by zero and integrated in R^2; periodizing that amplitude back to the torus changes neither integral nor derivatives on its support.
The consumer must retain this normalization and all cutoff/convolution tails separately.

## Acceptance and inspection limits

The established nondegenerate stationary-phase estimate and its stated uniform-dependence interface are accepted as mathematical inputs at the checked primary-statement and applicability level.
This acceptance is not an original-proof audit, independent source review, stationary-phase expansion verification or numerical-constant certification.
The read proof reduces to quadratic phases and Taylor expansion with repeated integration by parts; the omitted estimates and the preceding source dependencies were not audited here.
The existing U001 and U002 retain their separate first-derivative and higher-derivative scopes and do not retroactively cover these pages.
The focused search found those existing bounded units, then the actual retained primary Section3 supplied the missing two-dimensional input, so no external search or source acquisition was needed.
No claim about the weighted phase, its band mass, original probability laws, actual polynomial family or G0001 completion is part of this source unit.

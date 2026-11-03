---
author: Yin
---
# DMS84-U001: attribution for matrix-power support and inverse decay

Date: 2026-10-18T10:53.
Human record author Yin.
The assigned G0001 author agent inspected this source to identify the established inverse-decay mechanism used in its fixed-seed projection proof.
This is a source statement and applicability reading, not independent project review or a complete audit of the external proof.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: DMS84, Demko, Moss and Smith, associated with Mathematics of Computation 43 (1984), 491--499. Actual inspected artifact: the first appended author manuscript in the Georgia Tech final-report bundle, PDF pages 6--28, manuscript pages 1--21 on PDF pages 8--28. The [report bundle](../../../literature/pdf/DMS84--report-bundle.pdf) is the selected source; equivalence with the published nine-page edition is not asserted.

Passages: Manuscript Section 2, pp.2--6 / PDF pp.9--13, especially Proposition 2.2 and its proof, and Theorem 2.4; Section 5, pp.17--18 / PDF pp.24--25, especially Proposition 5.1 and Example 2.

Inspection: Text-read the stated passages and visually checked PDF pp.11,24,25, covering the positive definite hypothesis, exact support sets, inverse-entry conclusion and periodic corner example. The title/author page and report introduction were text-read to establish the associated manuscript. No whole-paper proof audit, mathematical equivalence comparison or earliest-priority claim is made.


<a id="dms84-u001"></a>
<a id="dms84-matrix-power-support"></a>
## Matrix-power support and the inspected classical conclusion

For a positive definite bounded and boundedly invertible matrix A on l2(S), the manuscript defines

    S_n(A)=union_(k=0)^n {(i,j): (A^k)_(i,j)!=0},
    D_n(A)=(S times S) minus S_n(A).

Proposition 5.1 bounds the supremum of |(A^-1)_(i,j)| on D_n(A) by C_0 q^(n+1), with the spectral constants from Proposition 2.2.
For a spectral interval [a,b] with 0<a<b and r=b/a, those constants are q=(sqrt(r)-1)/(sqrt(r)+1) and C_0=(1+sqrt(r))^2/(2ar).
The source derives this mechanism by polynomial approximation to the inverse on the spectrum and the support of powers of the matrix.
The scalar case is immediate separately and is not needed for the present attribution.
Example 2 explicitly discusses a positive definite tridiagonal matrix with additional corner entries, whose inverse decays away from both the diagonal and those corners.

This identifies the relevant classical mechanism more accurately than a claim of ordinary linear bandwidth for a cyclic sparse matrix.
The G0001 author proof instead uses its own elementary series for I-G/36, its exact cyclic ball count 12j+1 and its own constants.
It does not invoke the source's Chebyshev constant, recursive external approximation inputs or the source statement as an unproved mathematical premise.
The specific two-end coefficient recovery, actual Salem factor, bounded cyclotomic-rank correction and cubic Fourier conclusion are not statements supplied by this source.

## Acceptance and limits

The matrix-power-support statement and its role as attribution for the inverse-decay mechanism are read and applicable at the above recorded manuscript scope.
This closes the previously unresolved identification for that mechanism; it does not make the project-specific bound an external known theorem.
The published PDF remained inaccessible through the attempted publisher requests.
The institutional bundle was obtained unchanged by a direct request after the web reader returned an access error.
Other appended papers in that bundle were not inspected or accepted as inputs.
No source original proof, complete monograph dependency, sharper quantitative constant or mathematical equivalence of editions is accepted by this reading.

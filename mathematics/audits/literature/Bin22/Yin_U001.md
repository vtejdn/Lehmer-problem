---
author: Yin
---

<a id="bin22-u001"></a>
# Bin22-U001: finite symmetric spectral decomposition and Rayleigh extrema

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Bin22](../../../literature/pdf/Bin22.pdf), David Bindel, Cornell Matrix Computations CS6210, eight-page lecture dated2022-10-27; artifact.

Passages: Section1 p.1, finite symmetric eigenvalue facts and displayed arguments; Section2 pp.3--4, Rayleigh quotient and its extrema.

Inspection: 2026-10-11, Yin; author and separate project reviewer directly read the selected primary passages. Root text-read them and visually inspected p.3. The reader also located Theorem1 p.5, but the local argument invokes only the stated finite spectral/Rayleigh interface.


A real symmetric matrix has real eigenvalues and an orthonormal eigenbasis.
Its Rayleigh quotient is a convex combination of its eigenvalues, so its extrema are the extreme eigenvalues; an extremizing vector is an eigenvector.
The selected displayed arguments and normalization were checked.
These classical finite statements are accepted at that scope.

The current Jacobi construction proves its own strict endpoint bounds by quadratic forms, simplicity by endpoint recurrence, one-outlier count by a codimension-one argument, and strict growth by extension of an eigenvector.
It does not infer a new theorem from an uninspected infinite-operator limit, general Jacobi result or numerical eigensolver.
The source supplies neither algebraic irreducibility, actual minimal-factor degree, field containment nor unit-norm information.
Those are separate project deductions.

The source was located for classical attribution after the finite path-matrix construction was proposed.
The first-page header supplies the course/date directly; the bibliography's descriptive title combines the course name and section headings.
No whole-course or full-notes audit, optimal perturbation theorem or numerical computation is claimed.

---
author: Yin
---

<a id="war05-u001"></a>
# War05-U001: toral periodic counts and fixed-input growth

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Thomas Ward, Group automorphisms with few and with many periodic points; selected public preprint arXiv:math/0306292v1,19 June2003, internal date16 June2003, as recorded with the retained [War05 PDF](../../../literature/pdf/War05.pdf). No full preprint/journal comparison is asserted.

Passages: Printed/PDF pp.1--2, equations2 and4, the cyclic root product and toral periodic-point growth interface, including the cited Baker input for algebraic unit-circle eigenvalues.

Inspection: Original2026-10-06 statement/applicability inspection retained from S4: title/author/version and complete rendered pp.1--2 were checked. Baker's proof and the general periodic-orbit construction were not audited. This organization performs no new PDF or network reading.


## Exact adopted toral interface

Let N>=1 be an integer and A in GL_N(Z), with eigenvalues lambda_i counted with algebraic multiplicity and no root-of-unity eigenvalue.
Let T_A be the induced automorphism of the torus R^N/Z^N and chi_A(t)=det(tI-A).
For every integern>=1, its fixed-point set is finite and

    F_n=card(Fix(T_A^n))
       =abs(det(A^n-I))
       =abs(Res(chi_A,t^n-1)).

At this exact domain the accepted source growth statement is

    lim_(n->infinity)log(F_n)/n
       =m(chi_A)=sum_i logmax(1,abs(lambda_i)).

Logarithms are natural and there is no dimension divisor.
No expansiveness assumption is required: algebraic eigenvalues on the unit circle are allowed provided none is a root of unity.
The full fixed-input limit in that case retains its accepted Baker input, without a new proof of that Diophantine estimate.
The elementary determinant-index and eigenvalue-product identifications were checked in the original [project interface](../../../strategies/Yin_S_G0004.md#periodic-resultant-interface); source acceptance and those local identities are distinct from an original-proof audit.
The total toral entropy normalization is separately retained in [Smy08-U004](../Smy08/Yin_U004.md#smy08-toral-entropy).

## Applicability and limits

This is an accepted established external statement at the exact inspected toral no-root-of-unity scope.
It supplies a pointwise limit for each fixed integral automorphism, not a convergence rate uniform in the matrix, dimension or original polynomial.
It supplies no degree-independent lower rate from integrality or from an isolated count exceeding one.
It does not identify periodic-point growth with entropy on every compact abelian group, and the torus is distinct from the compact dual of a rational vector space.
The original S4 scope warning and any local compact-group diagnostic are not assertions about a broader theorem in the source.
The general periodic-orbit construction, original Baker proof, remainder of the paper and published/preprint equivalence remain unchecked.

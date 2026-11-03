---
author: Yin
---

<a id="kor00-u001"></a>
# KOR00-U001: primitive nonnegative integer realization from all net traces

## Source and inspection

[Source and edition notes](readme.md).

Source edition: K.H. Kim, N.S. Ormes and F.W. Roush, The spectra of nonnegative integer matrices via formal power series, Journal of the American Mathematical Society13(2000),773--806; inspected published article text in the original [author-uploaded rendering](https://www.researchgate.net/publication/243782071_The_spectra_of_nonnegative_integer_matrices_via_formal_power_series).

Passages: Net-trace definition p.773, necessity explanation p.774 and Main Theorem2.2 p.776.

Inspection: Original2026-10-07 statement/applicability reading by assigned AI review_matrix_completion for Yin, retained from the original README. The displayed journal header, authors, exact definition and theorem were read in accessible HTML. Original proof Sections4--6 remain unreviewed. This organization performs no new source reading or acquisition.


## Exact accepted statement

Let Lambda=(lambda_1,...,lambda_d),d>=1, be a finite nonempty list of nonzero complex numbers, counted with multiplicity, and put

    q(t)=product_(i=1)^d(1-lambda_i t),
    tr_n(Lambda)=sum_(j|n)mu(n/j)sum_i lambda_i^j,
       n>=1.

Here mu is the ordinary Moebius function.
The net trace tr_n is not divided byn.
There exists a primitive nonnegative integer square matrixA, of an unspecified finite dimension, satisfying

    det(I-tA)=q(t)

if and only if all three conditions hold:

- q(t) has integer coefficients.
- lambda_1 is positive and strictly greater than the modulus of every other listed eigenvalue.
- tr_n(Lambda)>=0 for every positive integern.

Primitive means that some positive power ofA is strictly positive in every entry.
Additional zero eigenvalues are allowed, so the complete characteristic polynomial may have an extra power oft beyond the listed nonzero spectrum.
For an actual graph realization, tr_n/n is the number of primitive length-n orbits.
Ordinary trace nonnegativity cannot replace the required net-trace conditions at alln.

## Accepted use and proof boundary

The exact integer criterion is accepted for the local nonzero-spectrum realization problem after the original definition, necessity explanation and theorem statement were read.
The Main Theorem's sufficiency proof in Sections4--6 was not audited.
No dimension, zero-padding size, integral unimodularity or edge-excess bound follows from this adopted scope.
A necessary net-trace test alone does not supply those missing complexity controls.
The attribution is Kim--Ormes--Roush2000 for the integer case, rather than solely Boyle--Handelman1991.
The accessible rendering identifies the published article; no PDF was retained by the original reviewer and no local is claimed for this scope.
Exact failed requests and the empty TeX response remain at their existing acquisition accounts; they do not establish that every alternative source is unavailable.

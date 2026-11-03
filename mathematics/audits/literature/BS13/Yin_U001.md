---
author: Yin
---
# BS13-U001: the measurable-set Turan--Nazarov inequality

Date: 2026-10-15.
Human author Yin.
The f_unitary_scope source-only reader checked the actual primary PDF and its publication identity, text-read the relevant statement and surrounding conventions, and visually checked PDF pages 1 and 3.
Root separately read the matching retained text at the title and Theorem2.1.
Neither reading is a review of a new project proof.

<a id="bs13-u001"></a>
## Read; accepted established statement and applicability

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Bownik and Speegle, author-hosted journal-layout PDF, Bulletin of the London Mathematical Society45(3)(2013),554--566;13 PDF pages. No byte comparison with the publisher artifact.

Passages: Theorem2.1, PDF page3 / printed556; attribution immediately preceding it and reference13 on PDF13 / printed566.

Inspection: Direct primary statement and convention reading, with visual formula check by the source-only reader. State Read. Theorem2.1 is stated here and attributed to Nazarov[13,Theorem I]; neither its original proof nor the other BS13 proofs was audited.


For a positive integer m, complex a_j,c_j, and exponential polynomial u(x)=sum_(j=1)^m c_j exp(a_j x), Theorem2.1 states that for an interval I in R and any Lebesgue measurable E contained in I with positive measure,

    sup_(x in I)|u(x)|
      <=exp(|I| max_j |Re a_j|)
        (A |I|/|E|)^(m-1) sup_(x in E)|u(x)|,

where A is an absolute constant.
Accept the established theorem at this exact statement/applicability scope; enlarge A to at least 1 if necessary.
The source does not give a numerical A.
The intended project use has a finite nondegenerate interval, finitely many distinct pure imaginary frequencies and nonzero coefficients.
The exponential factor is then exactly 1.
No frequency-gap, largest-frequency, degree, coefficient-size or measurable-set regularity restriction is added.
Ordinary sup is the displayed convention.
The m=1 exponent is 0; m=0 is not a stated domain.

For an ordinary integer polynomial F with N nonzero terms, substitution u(x)=F(exp(ix)), I=[0,2pi], makes |E|/|I| the normalized circle measure of the corresponding set.
This is a direct notation conversion, not a new small-value or logarithmic-integrability theorem.
Such deductions and all resultant/angular transfers belong in the consuming mathematical material.
Proposition2.2 has a constant depending on the individual function and interval length; it is not a substitute for the absolute constant in Theorem2.1.

## Source and search limits

The concrete trigger was the current G0001 inquiry into uniform logarithmic regularization for auxiliaries with bounded numbers of terms.
Bounded local searches of retained G materials and the bibliography did not locate this exact accepted input; those searches do not establish novelty.
The [primary research article](https://pages.uoregon.edu/mbownik/papers/51.pdf) supplies the full theorem statement, and the [publisher identity](https://doi.org/10.1112/blms/bds119) matches the title, authors, year, volume and pages.

BS13 explicitly cites Nazarov's English publication in St. Petersburg Mathematical Journal5(1994),663--717.
The [original publication record](https://www.mathnet.ru/eng/aa397) identifies the Russian Algebra i Analiz5(4)(1993),3--66 and English version.
Attempts to retrieve the original MathNet PDF failed; an author-hosted TeX URL returned an HTML challenge rather than mathematical source.
Neither artifact was accepted, and no direct reading of Nazarov's original proof is asserted.
The accessible primary research paper resolves the established statement/applicability input; no original-proof audit is required or claimed for this ordinary use.

Source: [retained author-hosted journal edition](../../../literature/pdf/BS13--author-journal.pdf).
The PDF has no printed table of contents, so no contents transcription is fabricated.
The source reader inspected the homepage, theorem passage, adjacent Proposition2.2 and references; reading those passages does not constitute whole-paper review.
Uniform auxiliary existence, divisibility and any Mahler gap are not source conclusions.

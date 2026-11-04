---
author: Yin
---

<a id="tv07-u001"></a>
# TV07-U001: Circle-zero cost is a supremum-norm statement

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [TV07](../../../literature/pdf/TV07.pdf), published journal article, Acta Sci. Math. (Szeged)73(2007),593--611; retained artifact.

Passages: Theorem1(i), printed p.593/PDFp.1; surrounding conventions and Theorem3, pp.593--594/PDFpp.1--2; proof excerpt of Theorem1(i), pp.595--596/PDFpp.3--4.

Inspection: 2026-10-11T11:31, Yin, direct root AI reading and self-check. The retained PDF title/theorem page was rendered and visually inspected; all four relevant pages were text-read. Statement, norm type, monic normalization and current applicability checked. The proof excerpt was read but its Bernstein input and complete proof were not independently re-audited. Remaining pp.597--611 unreviewed.


## Exact statement and accepted comparison scope

There is an absolute c>0 such that every monic complex polynomial R of actual degree N with k unit-circle zeros, counted with multiplicity, satisfies

    ||R||_infinity,T >= 1+c k/N.

The paper explicitly defines its norm as the supremum norm.
It imposes no integer coefficient restriction.
For a polynomial with R(0)=1, conjugated coefficient reversal gives a monic polynomial of the same actual degree and identical pointwise circle modulus, so the same supremum-norm conclusion applies.
Ordinary coefficient reversal also preserves the circle supremum norm by reversing the angle; the pointwise comparison uses the conjugated convention.
This is accepted as an established external statement at the checked comparison scope; it is not an L2 estimate or an accepted premise for a stronger local theorem.

Theorem1(ii)'s excessive-arc count and Theorem3's separated-zero constructions were read only as context.
Their detailed proofs and the paper's potential-theoretic dependencies are not accepted or needed for this comparison.

## Boundary for finite single-Haar prediction

For degree<=N, Cauchy--Schwarz and Parseval give ||R||_infinity<=sqrt(N+1)||R||_2.
Combining this with Theorem1(i) produces only

    ||R||_2 >= (1+c k/N)/sqrt(N+1),

which is generally weaker than the normalization floor1.
The inequality ||R||_2<=||R||_infinity goes in the wrong direction to transfer the source's lower bound directly.
Neither changing the source norm label nor dropping sqrt(N+1) is legitimate.

The complete sharper L2 candidate failure is retained in [C_G394](../../../claims/Yin_C_G0394_v1.md#primitive-integer-sharp-constant-failure), with its original exploration and search account preserved separately.
No L2 or integer-gap conclusion is attributed to TV07.
A future norm conversion or integer strengthening requires its own proof and scope check.

## Search evidence and limits

The trigger was the G0001 finite multiplier question: whether actual circle zeros impose a useful paid prediction cost.
Bounded local G-ledger/bibliography searches did not supply a sufficient interface.
Two external queries on2026-10-11 for polynomial circle zeros versus L2 norm and finite prediction located this primary journal PDF and Totik's related curves paper.
The latter was a discovery lead; TV07 itself supplied the precise circle statement and norm distinction, so no second work was acquired or adopted.
The first ordinary artifact request failed DNS; a direct authorized journal retrieval subsequently succeeded and the exact retained artifact was registered.
Acquisition is separate from this source check.

No historical priority, whole-paper audit, independent review, formal verification or G0001 resolution is asserted.
The L2 statement with a universal constant and the monic-unit specialization remain separate research questions.

<a id="original-separate-statement-comparison"></a>
## Distinct original statement reading

At2026-10-11T11:38 the separate local reviewer directly text-read complete printed pp.593--594/PDFpp.1--2, including Theorem1(i), supremum norm, monic normalization and surrounding statements.
This was a distinct reader and occurrence from the root 11:31 UTC four-page statement/application and proof-excerpt inspection above.
The [original full local review](../../reviews/Yin_R_G0191_v1.md#circle-zero-whole-proof-outcome) retains that exact input and its unknown initial-context relationship; it does not establish independent review of TV07.
The original TV07 proof, Bernstein input and general Jordan-curve results were not audited by that reader.
This maintenance reads the retained account and performs no new primary-source reading or acquisition.

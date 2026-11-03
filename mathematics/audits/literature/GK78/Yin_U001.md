---
author: Yin
---

# GK78-U001: dimension-free concentration for Hilbert-space subset sums

Date: 2026-10-10.
Source inspection and acceptance by the coordinating AI for Yin within G0001.

<a id="gk78-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Greene and Kleitman, published1978 chapter, public two-page-per-image scan of printed22--79; [registered PDF](../../../literature/pdf/GK78.pdf),29PDFpages. Bibliographic year/venue confirmed against Greene's Haverford institutional record.

Passages: Section9, printed74--76, PDFpages27--28, especially the arbitrary-dimension proof beginning on75 and ending on76. Title/authors were visually checked on printed22, PDFpage1.

Inspection: Direct visual reading of the stated Hilbert-space problem and its dimension-free answer, and the complete geometric block-transfer argument on75--76. The earlier Section3 symmetric-chain enumeration was not separately audited; the local consuming proof supplies an explicit binomial-count induction instead. Coverage Read with selected proof inspection; accepted classical theorem at the strict-diameter convention below, not a claim of whole-chapter audit.


## Accepted statement and boundary convention

Let v_1,...,v_N lie in a real Hilbert space with norm at least a>0.
Count all2^N indexed sums sum_i epsilon_i v_i, epsilon_i in{0,1}, including repeated values with their multiplicity.
Any set of diameter strictly less than a contains at most binom(N,floor(N/2)) such sums.
No constant depends on the Hilbert-space dimension.
The complex Hilbert case is its realification.
Equivalently a fair-sign sum with coefficient norms strictly greater than r has probability at most2^(-N)binom(N,floor(N/2)) in any closed ball of radius r.
The strict inequality avoids endpoint ambiguity.

The source phrases its motivating question with a sphere of diameter one.
The geometric proof actually produces pairs at distance at least one; therefore the adopted convention is strict diameter, or coefficient norms strictly larger than the tested closed-ball radius in the fair-sign form.
No equality-endpoint claim is inferred from informal sphere wording.

## Mechanism and inspected limit

A block of mutually separated sums and its translate by the next vector are repartitioned: choose the old point of maximal projection along that vector, and transfer its translated copy into the old block.
Inner-product expansion proves it remains separated from every old point.
The resulting sizes are k+1 and k-1, and repeated splitting gives the central-binomial number of blocks.
The first sentence of printed76 displays k+1 for both sizes; its actual construction and later sentence correctly give k-1 and k+1.
The local argument states the correct recurrence explicitly; no reliance on that typographical repetition is made.

This standard result is accepted under the external-input rule after exact statement, dimension independence and local applicability were checked.
The project proof in [L_G220](../../../ledger/Yin_L_G0220_v1.md) also gives the full needed induction.
Original1970 article access was attempted via publisher/DOI and the web reader returned403/failure.
The inspected primary-author exposition is the1978 chapter coauthored by the theorem's author, not a claim to have read the inaccessible1970 article.
That earlier article is cited only through this chapter.

## Search scope and local use

A bounded search sought a dimension-independent concentration inequality for long sums of unit-length neutral increments.
It located the classical Hilbert theorem and distinguished it from fixed-dimension, fixed-radius asymptotics.
Tao--Vu arXiv1002.5028v2 was screened online, introduction and Theorem1.4: its displayed constants permit dimension dependence, so that result is not imported or accepted here.
The search stopped on finding and visually checking the required primary-author proof.
No literature-wide novelty, full errata search or proof-assistant verification is asserted.

The consuming argument uses independent symmetric block displacements, a fourth-moment bound, and this sign-sum theorem to obtain a large-radius estimate with explicit universal constants.
Its stationary information comparison, algebraic embedding specialization and actual controls are local deductions, not statements attributed to GK78.
The source alone establishes no Lehmer gap, stationary distribution estimate or actual return classification.

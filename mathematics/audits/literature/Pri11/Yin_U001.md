---
author: Yin
---

# Pri11-U001: finite Lipschitz discrepancy for algebraic conjugates

Date: 2026-10-09.
Statement and applicability checked by the coordinating AI for Yin for the G0001/S_G0008 general-unit product-cost transfer.
Source and artifact.

<a id="pri11-u001"></a>
## Read; accepted external statement

## Source and inspection

Source edition: Igor E. Pritsker, Distribution of algebraic numbers, J. reine angew. Math. 657 (2011), 57--80; retained arXiv:1307.5734v1, 22 July 2013, 22 pages.

Passages: Printed/PDF p.2 normalized circle measure and zero counting convention; p.7 Theorem3.1, equation(3.2); p.16 its deduction from Theorem4.2 for orientation.

Inspection: Coordinator read the retained definitions and theorem as text and visually checked the rendered p.7 statement, constant and N>=55 threshold. The p.16 deduction and pp.14--16 energy mechanism were read in the preceding bounded source inspection. This accepts the exact statement and application interface; the underlying potential-theory proof and its external inputs have not received a complete independent source-proof audit.


Let Q(z)=a product_(j=1)^N(z-beta_j) be a polynomial with integer coefficients, a!=0, and simple zeros, of degree N>=55.
Let phi:C->R satisfy the global Lipschitz bound

    |phi(z)-phi(w)|<=A|z-w|

and have support in {|z|<=R}.
Let mu be normalized arclength probability measure on the unit circle, and let M(Q) be ordinary multiplicative Mahler measure, including |a|.
The source states

    |(1/N)sum_j phi(beta_j)-integral phi dmu|
       <=A(2R+1)sqrt(log(max(N,M(Q)))/N).

All logarithms are natural.
The zeros need not lie in the unit disk, the polynomial need not be irreducible or monic, and no Salem or reciprocity hypothesis is present.
Integrality and simple zeros are required; the displayed finite estimate is not asserted here for N<55.
The radius is that of the test function's support, not a bound on the conjugates.

## Acceptance and local application boundary

The coordinator accepts this established theorem at checked statement/applicability scope.
For an algebraic unit beta, use its monic irreducible minimal polynomial with actual degree N and M(Q)=exp(N h(beta)).
The radicand becomes

    log(max(N,M(Q)))/N=max(log(N)/N,h(beta)).

For beta=alpha^n, h(beta)=nm(alpha)/d with d=deg(alpha).
Keep N separate from d and keep the field-norm multiplicity d/N.
The source supplies neither degree preservation nor a lower bound on N; any small-degree escape argument is a separate project deduction.
It also supplies no arithmetic norm income.

A logarithm singular at one is not inserted directly.
The local argument must exhibit a real, globally Lipschitz, compactly supported truncation and prove its actual constant and support radius.
If that radius is 2R, the source factor is 4R+1.
All truncation, circle-mean and radial-tail costs, as well as the local proof's degree and income consequences, require their own complete review.
Acceptance here does not certify those deductions.

This source unit newly accepts Theorem3.1 only.
The earlier [method reading](readme.md#pri11-actual-product-energy) and L G0167 remain at their original scope: L G0167 has a self-contained Salem proof and does not retroactively acquire this dependency.
No new search, download, version comparison, numerical run or formal verification occurred for this acceptance.

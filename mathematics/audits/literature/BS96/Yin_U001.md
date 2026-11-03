---
author: Yin
---

# BS96-U001: effective split-prime interface

Date: 2026-10-07.
Source inspection by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).
Bibliography and acquisition.

<a id="bs96-u001"></a>
## BS96: conditional upper bound, statement scope and access exception

**Read; accepted conditional external statement.**
No full analytic-proof or numerical-certificate audit is claimed.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Eric Bach and Jonathan Sorenson, *Explicit bounds for primes in residue classes*, Mathematics of Computation65(216)(1996),1717--1735, DOI10.1090/S0025-5718-96-00763-6. Readable online original journal article,19 pages; no retained local PDF.

Passages: Printed pp.1717,1720--1721: absolute degree/discriminant conventions, ERH condition, Theorem3.1 and Corollary3.3; p.1729/PDF13: Theorem5.1.

Inspection: Original article text read through the author-profile PDF endpoint after institutional full-text redirect retired. The stated hypotheses, theorem and nonabelian conjugacy-class reduction were checked at source-interface scope. No complete analytic-proof, table or program audit, no successful local rendering.


For E/F Galois, E!=Q, let n=[E:Q] and D_E be the absolute field discriminant.
Under the source's ERH condition there is a degree-one unramified prime ideal of F in the specified conjugacy class with norm at most

    (4 log D_E+2.5n+5)^2.

The stated ERH scope on p.1720 is that the relevant zeta functions of E and Q have no nontrivial zeros to the right of real part 1/2.
When F=Q the prime ideal norm is the rational prime.
The asymptotic rational-base statement and its Galois extension have bound (1+o(1))(log D_E)^2.
These are accepted external statements; the analytic proof and the calculations behind the explicit coefficients are not independently certified.

The identity class must be applied in the normal closure of a non-Galois field.
Substituting the original generator's degree or polynomial discriminant for n or D_E is not justified.
This is the consequential normalization finding; no defect in the source theorem is asserted.

Acquisition exception: publisher PDF web openings failed; one PowerShell direct attempt returned a null-reference failure and retained no artifact.
The university's full-text link redirected to its retired SelectedWorks service.
The original article at the author-profile ResearchGate PDF URL remained readable via the web index, but a direct CPython urllib request returned HTTP403 at 2026-10-06T23:04.
No hash or local PDF is claimed, and no further access attempts were made.

## Actual review

The source agent completed the stated inspection and self-checked the convention comparison and direct deductions.
The original analytic input is retained at external-statement scope.
The coordinator read and checked both assembled drafts in full; read the original Fiori publisher proof on printed2199--2202; visually inspected retained PDF4/printed2201, including Theorem6 and Lemma5;
The coordinator also read the original BS96 web PDF's p.1720 ERH condition, p.1721 asymptotic statement and p.1729 Theorem5.1.
That review acquired no local BS96 artifact and did not audit the external analytic proofs.
Assigned AI assess_shortness_route separately read both assembled drafts completely and checked their mathematical normalization, scope and direct deductions.
This independent written review found no substantive defect; it did not newly inspect the original articles, recalculate artifact metadata or reproduce the separate degree22 experiment.

---
author: Yin
---

# Fio19-U001: hard split-prime family and the generator-height boundary

Date: 2026-10-07.
Source inspection by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).
Bibliography and acquisition.

<a id="fio19-u001"></a>
## Fio19: general-field lower family and the bounded-Mahler boundary

**Audited within the stated finite interfaces**, retaining the analytic and class-field inputs externally as detailed below.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Andrew Fiori, *Lower bounds for the least prime in Chebotarev*, Algebra & Number Theory13(9)(2019),2199--2203, DOI10.2140/ant.2019.13.2199; first public preprint arXiv1810.09566,22 October2018. Retained publisher artifact [Fio19.pdf](../../../literature/pdf/Fio19.pdf),1180347 bytes,8 pages.

Passages: Printed2199/PDF2 Theorem1;2200/PDF3 Lemmas2--3 and family description;2201/PDF4 Lemma5 and Theorem6;2201--2202/PDF4--5 proof of Theorem1.

Inspection: Retained PDF identity, size, hash and readability checked; complete printed2199--2202 rendered and visually read. Source statement and elementary proof interfaces checked. External class-field reciprocity, analytic class-number formula and extreme-value theorem remain explicit external inputs. The numeric table on2203 was not checked or rerun.


Theorem1 gives infinitely many Galois fields with least completely split prime at least (log D_L)^(2+o(1)); the source gives its more precise iterated-log constant.
For the assessed use only the growth scale and the Hilbert-class-field construction matter.

Its selected imaginary quadratic fields of discriminant -D have class number h<=C sqrt(D)/log log D, with H their Hilbert class field.
The inspected interfaces give [H:Q]=2h, D_H=D^h and p_split(H)>=D/4.
The norm inequality for the last bound was checked directly; the class-field and analytic inputs remain external.
This unit does not claim a complete recursive proof audit of the paper's underlying analytic theorems.

Two direct consequences are proved in the [fixed cost assessment](../../../claims/Yin_C_G0259_v1.md#chebotarev-period-cost): p_split(H)/([H:Q]log p_split(H)) is unbounded, whereas every integral primitive generator of these H has Mahler measure tending to infinity.
Thus this selected lower family obstructs a field-uniform split-prime shortcut but does not contradict the small-Mahler coverage target.
Neither assertion bounds the actual residue period of an arbitrary generator at other primes.

The retained introduction also reports the standard unconditional Chebotarev shape p<=D_L^A for an absolute exponent.
That original analytic proof was not read and no latest-exponent claim is made.

## Actual review

The source agent completed the stated inspection and self-checked the convention comparison and direct deductions.
The original analytic input is retained at external-statement scope.
The coordinator read and checked both assembled drafts in full; read the original Fiori publisher proof on printed2199--2202; visually inspected retained PDF4/printed2201, including Theorem6 and Lemma5;
The coordinator also read the original BS96 web PDF's p.1720 ERH condition, p.1721 asymptotic statement and p.1729 Theorem5.1.
That review acquired no local BS96 artifact and did not audit the external analytic proofs.
Assigned AI assess_shortness_route separately read both assembled drafts completely and checked their mathematical normalization, scope and direct deductions.
This independent written review found no substantive defect; it did not newly inspect the original articles, recalculate artifact metadata or reproduce the separate degree22 experiment.

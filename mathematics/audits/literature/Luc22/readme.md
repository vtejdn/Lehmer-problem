# Luc22 source audit

The inspected edition is the retained [arXiv:1901.00827v2 artifact](../../../literature/pdf/Luc22.pdf), revised 16 September 2020.
The citation key uses the 2022 publication year.
All page locators below refer to this 25-page preprint; printed and PDF page numbers agree.
Coverage does not automatically transfer to the journal text.

## Reading map

| Mathematical scope | Responsible unit | Main reuse boundary |
| --- | --- | --- |
| Sections 0--5 and 9; Appendix 14 | [Luc22-U001](Yin_U001.md#luc22-u001) | Kernel-removed determinant, group/matrix trace, four Lehmer infima, finite-index transfers and torsion obstruction; corrected spectral domain, dimension formula and finite-scalar proof. |
| Sections 6,8,10--13 | [Luc22-U002](Yin_U002.md#luc22-u002) | Ore/Dieudonné interfaces, rectangular matrix specialization, free abelian equalities, free-group obstruction and geometric upper bound; complex-coefficient bridge and retained external inputs. |
| Section 7 | [Luc22-U003](Yin_U003.md#luc22-u003) | Conditional approximation and exact weak-constant hypotheses; counterexample to the printed sub-approximation hypothesis and correction of the three-manifold transfer inference. |

An assigned AI reviewer read the full mathematical body on 2026-10-06 and checked its in-paper proof mechanisms.
Bibliographic references were read for input identification, not recursively audited.
A separately assigned AI reviewer checked the late-section normalization, coefficient and approximation interfaces and independently confirmed the principal separation and transfer findings; the units disclose the actual scope and shared context.
The coordinating agent additionally inspected rendered p.14 and independently checked the elementary counterexample to the printed Theorem 7.8.
These are targeted AI checks, not an independent human review, second complete source-proof audit or formal proof.

The source uses a determinant that discards zero spectral mass.
It must not be substituted without qualification for the unmodified regularized Fuglede--Kadison determinant.
Its four constants remain distinct: Theorem 10.1 identifies the weak/scalar abelian constants across ranks, and separately identifies the unrestricted matrix constants, without equating the latter to the former or proving classical Lehmer positivity.

The principal actionable defect is the reversed finite-set implication in Theorem 7.8.
With the printed tautological hypothesis its inequality fails for the trivial maps $\mathbb Z\to\{1\}$ and $A=1+t$.
The units own the exact evidence, corrected statements and remaining external-proof boundaries.
No project Claim, Task, manuscript adoption or current-status update is created by this literature audit.

## Version and correction search

On 2026-10-06 the coordinator checked the arXiv version history and the author's publication list, whose entry 125 identifies the 2022 journal publication, *Journal of Topology and Analysis* 14, pp.901--932.
Publisher DOI access returned HTTP 403.
A bounded search using the exact title with “erratum” and “correction”, together with the author's website, located no applicable correction in the inspected results.
This is not an exhaustive absence claim.
The source findings attach only to retained v2; no assertion is made that the journal rendering contains the same defects.

---
author: Yin
---
# Sun18-U001: relative-regulator normalization and the high-rank intersection boundary

Date: 2026-10-18T13:12.
Human record author Yin.
The loglog_cyclic_review author performed this bounded source reading for G0001; no independent project review or source-wide proof audit is asserted.

<a id="sun18-u001"></a>
## Read: exact definitions, regulator-ratio identity and applicability scope

## Source and inspection

[Source and edition notes](readme.md).

Source edition: James Sundstrom, Lower bounds for generalized unit regulators, Journal de Theorie des Nombres de Bordeaux30(1) (2018),131--173; published rendering with one cover page, so printed131 is PDF2.

Passages: Introduction and Section2, printed131--135/PDF2--6: relative units, deleted-place regulator, ratio identity, the stated new theorem and intersection-group definition.

Inspection: Complete selected text read; printed132/PDF3 visually inspected to verify the absolute determinant, deleted places and norm-unit index. The high-rank theorem statement and its hypotheses were read; its analytic proof and the original Costa--Friedman/Friedman--Skoruppa proofs were not audited.


Source: [retained published source](../../../literature/pdf/Sun18--published.pdf).
The inspected front matter contains no supplied table of contents.

<a id="relative-units-and-deleted-place-regulator"></a>
### Complete convention

For a finite number-field extension L/K let A_K and A_L be their archimedean places, O_K^*,O_L^* their full integer-unit groups, and mu_K,mu_L their roots of unity.
Write e_v=1 for a real place and2 for a complex place, using the ordinary archimedean absolute value.
The relative-unit group is

    E_(L/K)={epsilon in O_L^*:N_(L/K)(epsilon) in mu_K}.

Its rank is r=|A_L|-|A_K|.
Choose free generators epsilon_1,...,epsilon_r modulo torsion.
For each w in A_K choose ONE archimedean place of L above w and delete it; call the remaining r places A'_L.
The source defines

    Reg(L/K)=abs det(e_v log abs(epsilon_j)_v)_(v in A'_L,1<=j<=r).

For rank zero the empty determinant convention is1.
This is the source's relative regulator, not the unnormalized Euclidean covolume of its logarithmic lattice.
It uses the full ring of integers, not an arbitrary order.
In particular Reg(L/Q)=R_L, the ordinary regulator with the same complex weight2.

The source attributes to Costa and Friedman the identity

    Reg(L/K)=(R_L/R_K)/i_(L/K),
    i_(L/K)=[O_K^*:mu_K N_(L/K)(O_L^*)].

The determinant and this exact ratio identity are accepted at the inspected statement/applicability scope.
The original proof of the identity is not newly audited.
The direction Reg(L/K)<=R_L/R_K must not be reversed when consuming a lower bound.
The Salem determinant specialization and explicit unit-index prices belong to the project argument, rather than being asserted by this source unit.

### The separate high-rank result

The paper's new group is E=E_(L/K1) intersect E_(L/K2), where K1,K2 are DISTINCT real quadratic subfields of L.
Its rank is |A_L|-3, and its regulator uses a different deleted-three-place determinant.
The introductory theorem reports, for [L:Q]>=4000,

    Reg_(K1,K2)(L)/|mu_L| > (4.28*10^(-9))*1.199^[L:Q].

This statement is recorded as a checked theorem interface, not as a proof audit.
A lower bound for this high-rank covolume is not automatically a lower bound for one Salem relative-unit direction inside the group.
The source supplies no bound for the remaining directions that would justify that inference.
No new Salem gap is adopted here.

<a id="original-salem-regulator-reviewer-reading"></a>
## Original Salem-regulator reviewer reading

Retention recorded 2026-10-22T00:30.
The separate original R_G399 reviewer directly text-read the published Sun18 introduction/Section2 at printed131--135/PDF2--6 and visually inspected printed132/PDF3 for the deleted places, absolute determinant and norm-unit index.
This is distinct from loglog_cyclic_review's original source-author reading retained above.
Only the actual relative-unit/deleted-place definition, ordinary-ratio identity and distinct high-rank intersection theorem statement/applicability were inspected; its analytic proof and the original Costa--Friedman/Friedman--Skoruppa proofs remain outside that scope.
The [original complete R_G399 account](../../reviews/Yin_R_G0399_v1.md#salem-regulator-whole-independent-finding) records this distinct occurrence.
No separate individual source-reading minute is supplied;21:52 is the original2026-10-18 whole-finding completion and21:12 is the existing source-document date, neither a replacement reading minute.
The original21:14 L400 document and21:54 S1 adoption are also distinct events.
This maintenance reads the adequate existing U and retains the original occurrence; it claims no new PDF passage, acquisition, source version or original proof audit.

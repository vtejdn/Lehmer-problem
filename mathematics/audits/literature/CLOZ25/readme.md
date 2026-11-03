# CLOZ25: exact Frobenius classes and prime-cost limits

<a id="cloz25-s8-frobenius-screen"></a>
## Bounded source screen, 2026-10-09

[Retained CLOZ25.pdf](../../../literature/pdf/CLOZ25.pdf); identity, acquisition and version.
The inspected artifact is arXiv:2512.24963v1, 31 December 2025; printed and PDF pages coincide.
The expected use is to test a complex-conjugation Frobenius class for an affordable common partial return in [S_G8](../../../strategies/Yin_S_G0008.md#next-coverage-test).
The assigned growth_arithmetic_status AI carried out the source screen.

**State: Read, statement/applicability screen.**

## Actual inspection

The versioned [official HTML](https://arxiv.org/html/2512.24963v1) was read at the introduction, Theorems1.1--1.3, definition(2.1), the rational-equivalence definition, Theorem2.1, Corollary2.2, Theorem2.3 and the immediately surrounding effectiveness discussion.
The corresponding printed/PDF pages1,2,6,7 were rendered locally and visually read in full; printed and PDF page numbers coincide.
The definition(2.1) on printed/PDF3 was also text-read and compared with HTML.
Standard local Frobenius conventions in HTML Section3.2 were read for normalization.
The coordinator separately compared Theorems1.1--1.3 and 2.1--2.3 with the primary versioned HTML and verified the retained PDF bytes.
No proof in Sections4--8 was audited, and no table computation or accompanying code was run.

## Statements and applicability

The source's notation K denotes the top Galois field; in the local candidate it is L.
Its discriminant is the absolute discriminant of that top field, not the original degree-d generator's polynomial discriminant.
In (2.1) the bound is

    Norm(p) <<_(|G|,[k:Q],epsilon)
                    |Disc(K)|^(a(G,C)+epsilon).

Theorem1.1 specifies a cycle type in the natural root permutation action.
For an involution its cycle-length least common multiple is two and the displayed exponent is 1/2.
The statement does not identify an exact G-conjugacy class or the inverse partner of each root.
Its implied constants depend on root degree, base degree and epsilon.
Its stated sufficient effectiveness alternatives are epsilon>2/(|G|[k:Q]), or odd base degree and no nontrivial quadratic character of G.

Theorems1.2--1.3 give stronger exponents for a symmetric Galois group.
Theorem1.3 displays 500/exp(n/4), but retains an implied constant depending on n and the base degree.
The reciprocal degree-d root action preserves nontrivial inverse-pair blocks and is not S_d for d>=4.
Neither these theorems nor their degree parameters can be transferred by simply naming that action S_d.

Theorem2.1 addresses an exact rational equivalence class, with

    a(G,C)=2^(omega(order(g))-1)/order(g).

For an involution, rational equivalence is exactly conjugacy and the exponent is 1/2.
Thus this statement does target the correct class in the candidate.
Its stated effectiveness alternatives are epsilon>2/(|G|[k:Q]), or that k has no quadratic subfield and no quadratic character chi of G has chi(g)=1 for g in C.
Over Q, the base-subfield condition is automatic but the character condition is not.
The G-dependent constant and splitting-field discriminant remain; no uniform linear prime budget follows from the statement.

Corollary2.2 concerns an inert prime in an extension of prime degree.
It does not itself select the involution needed by the candidate.
In Theorem2.3, a subgroup H meeting C gives the conditional exponent

    a(G,C)=sqrt(|C_H(g)|)/(2sqrt(|H|)),

provided every relevant nontrivial irreducible Artin L-function for H with chi(g) nonzero is entire.
The exact effectiveness clauses also retain the stated quadratic-subfield/character restrictions.
Taking H=<g> for an involution gives exponent 1/2; choosing a larger H can formally improve it but requires the additional holomorphy and subgroup data.
No such data or degree-uniform prime cost has been established for all relevant small-Mahler splitting fields.

This is a negative transfer screen, not a defect claim about any source theorem.
The exact local p+1 return mechanism is proved separately in [L G0160](../../../ledger/Yin_L_G0160_v1.md#inversion-matched-frobenius-return).
Its involution comparison assumes complex conjugation is nonidentity; the totally real identity case has zero matched mass in that mechanism.
No displayed result of this paper is adopted as a new input to that proof or used to assert near-one coverage.

## Exact bounded search record and stopping decision

The three actual public queries were:

1. `Salem numbers Frobenius complex conjugation primes splitting fields`
2. `least prime Frobenius conjugacy class order two effective Chebotarev discriminant`
3. `Peter Cho Asif Zaman least prime given cycle type`

Local reuse preceded these queries: L59, L70, L74, L75, L78, L80, L152, L159, BS96 and Fio19 source records, and the J10/J11 retained interfaces.
A theorem about a nonidentity or inert Frobenius class is not automatically a theorem for the particular matched class.
Only primary source pages were relied on for the selected new work.
The search found no qualifying uniform prime-cost theorem in the inspected scope.
It stops here without a broader survey, new scan, source-proof adoption.

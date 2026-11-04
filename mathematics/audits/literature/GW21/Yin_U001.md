---
author: Yin
---
# GW21-U001: uniform dyadic dense-GCD cardinality bound

Date: 2026-10-13T05:09.
Human author Yin.
The delegated direct_triple author directly read the published source online during the preceding G0001 round and records that statement/applicability inspection after explicit new-window continuation.
Root separately read the same theorem and registered GW21.
This unit does not claim an independent audit of the source proof or of the project's new weighted adaptation.

<a id="gw21-u001"></a>
## Read; accepted external statement

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Ben Green and Aled Walker, Extremal problems for GCDs, Combinatorics, Probability and Computing30(2021), no.6,922--929, DOI10.1017/S0963548321000092; actual eight-page published Cambridge PDF, first published online8 April2021. The published version is the inspected theorem source, distinct from arXiv:2012.02078v2 of16 December2020. No full published/preprint comparison was performed.

Passages: Published Theorem1.1 and the epsilon/p0 setup immediately preceding it, printed922/PDF1; surrounding interpretation and dyadic-decomposition remark5, printed923/PDF2.

Inspection: Direct online reading of the published PDF's text, checking the exact theorem, variables, inequalities, finite small-prime factor and dependence on epsilon. Accepted for mathematical use at statement and applicability scope. Source proof and its external inputs were not completely reviewed; this is Read, not Audited within scope.


Use the registered [published online PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D3BE6C493BF68649458DDED6D20AEB55/S0963548321000092a.pdf/extremal-problems-for-gcds.pdf).
Bibliographic identity is owned by GW21 in [references.bib](../../../literature/references.bib).
The [retained published PDF](../../../literature/pdf/GW21.pdf) is now available.
On 2026-10-14 its Theorem1.1/setup and p.923 remarks were directly compared with this unit and agree.
This does not retrospectively assign local bytes to the original online reading or broaden its statement/applicability scope.

### Exact statement and conventions

Fix epsilon in(0,1).
The source chooses a sufficiently large finite threshold p0=p0(epsilon), depending only on epsilon.
For a finite positive-integer set S, define P_small(S) to be the primes p<=p0 dividing at least one element of S.

Let A,B,D be real numbers in[1,infinity), with D<=min(A,B).
Let rho in(0,1], and let I subset[A,2A] and J subset[B,2B] be finite sets of integers.
If at least rho*|I|*|J| pairs(a,b) in I x J satisfy gcd(a,b)>=D, then Theorem1.1 states

    |I|*|J| <=1000^(1+#P_small(I union J))
                   *rho^(-2-epsilon)*A*B/D^2.          (1)

Pairs are ordered through the Cartesian product.
I and J need not be disjoint, and their common elements contribute diagonal pairs.
The source does not assume coprime elements, squarefree elements, bounded individual prime support or a bounded union of all primes.
Its relevant prime threshold is fixed by epsilon alone.
Empty sets give a vacuous zero product; consumers using a density ratio must handle them before dividing.

An immediate uniform consequence, used by the project, is that some finite K_epsilon>=1 satisfies

    |I|*|J| <=K_epsilon*rho^(-2-epsilon)*A*B/D^2.       (2)

For example take K_epsilon=1000^(1+pi(p0(epsilon))), where pi counts primes up to the threshold.
This constant is independent of A,B,D,rho,I,J.
The source does not provide a numerical p0 in the inspected statement, and this record neither computes one nor claims an effective optimal constant.
In particular epsilon must first be FIXED; sending epsilon to zero while keeping K_epsilon unchanged is not licensed.

### Acceptance and the consuming interface

Accept(1)--(2) as an established external mathematical input for the continuing [G0001 contract](../../../tasks/Yin_T_G0001_v1.md#contract).
This acceptance follows direct statement/version and applicability inspection, not a reproduction of the published proof.

The responsible [weighted root-capture author draft](../../../claims/Yin_C_G0101_v1.md#nonlinear-triple-weighted-two-band) uses subsets of actual dyadic order bands.
For a short-lcm pair with a>=A,b>=B and lcm(a,b)<=Y, the exact identity gcd(a,b)=ab/lcm(a,b) gives gcd(a,b)>=AB/Y.
If Y>=max(A,B), choose D=max(1,AB/Y); then1<=D<=min(A,B), as required.
If a band starts above Y, that short-lcm pair set is empty and no theorem application is needed.
The AB/Y<1 case is separately retained, rather than applying(1) at an excluded D<1.

This elementary conversion is not the substantive weighted theorem.
Equations(1)--(2) concern SET CARDINALITIES, not root multiplicity weights, global order distributions, compatible-third links, a maximum divisor mass or arithmetic norm income.
The project's finite level-set integration, summation over occupied bands, scale-mass factor, residual-bucket split and full original-norm transfer require their own mathematical argument and whole independent review.
This U does not prospectively certify any of those deductions.

### Proof inspection and version limits

The source's introduction describes a minimal-counterexample argument, prime-adic valuation concentration and a final combinatorial estimate.
The theorem/setup and selected contextual passages were read; some proof text was available in the online extraction, but no complete line-by-line source-proof check, recursive review of Koukoulopoulos--Maynard, erratum survey, or formal verification occurred.
None is implied by publication or by accepting the theorem at its checked interface.

The related arXiv identifier is2012.02078, with v2 dated16 December2020.
It is not substituted for the published edition in(1), and no statement-by-statement or whole-proof equivalence between editions is asserted.
The expected local artifact's unavailability does not mean the online theorem was inaccessible.
Bibliography and acquisition metadata remain with their canonical records.

The original author's global fixed-positive-triple-density question is not a statement of this source.
The paper supplies no actual near-one polynomial coverage, no uniform short-pair bound contradicted by C96, and no linear-in-density capture bound contradicted by C98.
Any downstream no-loss assertion requires an additional argument, which this source reading does not supply.

### Recorded use and remaining work

2026-10-13T05:09.
Exact source statement, published edition and parameter interface recorded after GW21 registration; online-only access and proof-inspection limits retained.
The consuming D24 is still an author draft and awaits a noncontributing whole review.
This source unit records the accepted external input only; it does not select a Claim assessment or update Task completion.

### Subsequent consumer organization

2026-10-13T05:29.
The entire former D24 is now preserved in [C_G101](../../../claims/Yin_C_G0101_v1.md#decision-organized-reviewed), adopted after the separate [original-whole R341](../../reviews/Yin_R_G0341_v1.md) and [actual-extraction R342](../../reviews/Yin_R_G0342_v1.md) findings.
Incoming locators above now point to that identical retained argument.
This changes the project consumer location and assessment, not the scope of this external-source inspection; the earlier13:09 pending status remains historical.
No whole GW21 proof audit is added.

<a id="original-scale-loss-reviewer-reading"></a>
### Original scale-loss reviewer occurrence

The2026-10-13 reviewer of the original L396 whole account, retained in [R695](../../reviews/Yin_R_G0695_v1.md#l396-and-r455), distinct from the direct_triple source author and the root source registration above, read the complete selected C101 statement and this unit for the actual fixed-epsilon equal-band density bound.
That original whole finding's source binding records published-statement/applicability and online source reading at that review's date; the whole finding explicitly inherits the accepted theorem and does not audit the full GW21 source proof.
No separate source-reading minute is recorded, and the13:32 whole-finding completion is not substituted for one.
The necessary theorem/setup, edition, finite epsilon-dependent constant, dyadic applicability and exclusions retain this unit's recorded depth; no new2026-10-22 PDF/source reading, whole-paper audit or preprint/published equivalence is asserted.
The original online access and later2026-10-14 retained-PDF comparison remain different provenance events.

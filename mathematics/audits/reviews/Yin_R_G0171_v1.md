---
author: Yin
---

# Retained project review: Actual repeated-cell congruences with full companion formulas and bounded-count asymptotics

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0346_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="repeated-cell-complete-independent-review"></a>

### Complete separately organized noncontributor proof and native review

Reviewer: root AI for Yin.
Review completed2026-10-10T13:16 against the complete frozen19,397-byte author body, Sections1--6/equations(1)--(12).
Root supplied the broad discovery assignment and bounded execution coordination, but none of the author's new congruence, determinant, coefficient or finite root arguments.
This is nonblind, separately organized noncontributor review of the ENTIRE new mathematical contribution.
The original body above is preserved unchanged; this finding does not replace it.

#### Scope, reused inputs and actual congruence

I read the entire D212 proof and author program, the actual L338 Q3/attachment/full-cycle identities, and the L340 full coefficient and circle estimates at their used scope.
L330's original scalar, full neutral factors and log lambda in(log4,log5) remain fixed inherited inputs; no new original irreducibility/root theorem is inferred from the finite computation.
The already retained D9/FW24 elementary transformation and cover conventions remain method attribution only.
The present proof uses no new uninspected external theorem or congruence classification.

The labelled old order is upper triangular with exactly four diamond edges per cell and k+2 endpoint/path edges, giving5k+2.
The complete Q is the displayed determinant-one block diagonal matrix.
Direct local multiplication sends(a,b,c) to(b,c,a+b+c), produces the stated proper block and retains all diagonal ones.
A right neighbor sees the old a coordinate only in r; a left changed cell sends(0,-1,+1) to(-1,+1,0).
Thus even two adjacent changed cells produce no omitted lower entry, no coupling to the wrong internal vectors and no new cross term.
The two exceptional a0 endpoint attachments transfer to r0; all z edges and the final ak column are accounted for.
Every subset, including empty and all-selected, therefore gives an actual integral congruence, not merely a same-scalar construction.

The full rank4k+1, height1, energy5k+2 and squared sum9k+3 follow from the explicitly preserved support.
The literal cover doubles rank/energy/squared sum and retains height1.
Integral determinant-one congruence preserves the complete signed polynomial.
Its q and e multiplicities remain explicit; the inherited full positive factor has the retained non-small measure.
No zero-measure factor is used to hide a positive expense.

#### Entire determinant and subset-count reduction

I checked the two eliminated b/c vertices and every external endpoint against the absolute pencil convention.
Unchanged cells give adjacent entries(-2t²,-2), and changed cells give(-2t,-2t) after the same q row clearing.
Diagonals and the product4t² of the two adjacent entries do not change.
Consequently the path matchings, endpoint corrections and corner transposition give the SAME full B_k.
The only affected permutations are the two full oriented cycles.
Each changed cell lowers the forward exponent by one and raises the reverse exponent by one, giving2k-s and s; multiplication by the unchanged two long-corner expressions supplies the remaining powers and the exact bracket in(2).

Restoring the eliminated q and path denominators yields the entire polynomial q^(k-1)G_(k,s); equality over Q(t) implies the polynomial identity at exceptional denominator roots as well.
Multiplication by the ENTIRE signed original gives(3).
The formula proves dependence only on s, without asserting congruence of the different absolute forms or an optimum over all integer bases.
The s0/s1 specializations are precisely the previously retained formulas, and s=k factors the cycle bracket as in(4).
Its degree2k+2 before the q^(k-1) restoration gives descending depth k in total degree4k+1; the leading-degree tie at this endpoint is included rather than counted as a fixed-depth exponential coefficient.

#### Full-circle upper cost and fixed-count lower cost

The L340 normalized recurrence T_j/(2t)^j has characteristic roots of modulus one on the unit circle, including the repeated endpoint, so |T_j|<=(j+1)2^j there.
The three common B terms have respective normalized bounds10k²+6k, (8k+4)(k-1) and2(k+1)(k-2), summing20k²-8.
Every s changes only unit-modulus powers in the remaining term, whose bound is2^k(4k+8).
Hence the complete G has sup norm at most2^k(20k²+4k).
Integrating its logarithm gives(6), with the full q factor charged at its exact zero Mahler measure.
Monicity gives nonnegativity.
The original full factor is added, not omitted, for the cover.

For fixed s and j=s+1, k>=j+2 gives the unique exponential contribution at depth j: q^k t^(2k-s)C_k has degree4k-s, while the extra constant in C_k+1 and both other cycle terms have strictly smaller degree.
Thus a_j=c_(k,j)-2^k with no cancellation by another full-cycle leading term.
I checked the explicit continuant expansion of T_l: a term indexed h begins at depth2h, and its coefficient at total depth v is bounded by k^h4^h(2k)^(v-2h)<=(4k)^v.
At most v+1 terms contribute.
The sparse seed quotient gives |coeff F_k|<=5, including k3 overlap; the other two bounded factors have coefficient bounds4 and1.
The three B products begin at depths0,2,4.
Their bounded convolutions, at most(j+2)^2 depth triples, therefore give exactly the sufficient factor53(j+1)(j+2)^2 4^j k^j.
This constant need not be sharp to establish(8).

The onset definition is finite: for k>=2j, (1+1/k)^j<=exp(1/2), so2^k/k^j increases by at least2exp(-1/2)>1.
The defining inequality then persists for every k>=K_j.
It implies |a_j|>=2^(k-1).
The full-root Vieta bound |a_j|<=binom(4k+1,j) exp(m(p)) proves(9), including its direction and every root multiplicity.
At fixed j its logarithmic binomial expense is O(log k); combining with(6) proves both limits in(10), since the original measure is bounded.
The proof explicitly does NOT hold uniformly in growing j or remove K_j's dependence on j.
Neither an all-selected asymptotic nor a class-wide obstruction has been smuggled into this fixed-count conclusion.

#### Complete finite evidence, root exhaustion and different method

The predeclared whole reviewer domain is exactly the author's k3..6/all120 subsets/all22 companions/all12 full selected objects.
The first and sole independent run (`mathematics/computations/outputs/Yin_J_G0082/repeated-cell-review-result.json`) began2026-10-10T13:12 and finished 2026-10-10T13:12.
Worker time3.6546084999863524seconds and supervisor time3.8466905999812298seconds are within the120second aggregate OUTER limit; Python3.12.14/SymPy1.14.0, exit0, no timeout.
The first report is PASS, with142,275 strictly typed scalar comparisons,120 subsets,22 complete companions,3,084 saved pencil values,12 full selected matrices,52 comparisons and149 rational Sturm intervals.
No failed run, retry, extra input or precision enlargement occurred.

The independently written reviewer imports no author code or older checker.
It constructs the labelled graph and complete Q from explicit basis columns, checks generic full congruences and determinants, and obtains the full pencil polynomial by solving for minus V^-1 V^T followed by a Berkowitz characteristic polynomial.
Evaluating these independently obtained entire polynomials checks EVERY saved Bareiss pencil value.
The complete cover is independently assembled from two block matrices and interleaved.
Every full coefficient array, exact factor product/multiplicity, irreducible factor and all actual size costs are checked.
This is a different complete method, not a rerun of the author's pointwise determinants.

Trace conversion independently eliminates descending Laurent powers using binomial coefficients.
It reconstructs the entire trace polynomial after removing exactly ONE forced t+1.
Every author's saved rational interval has the declared maximum width; squarefree polynomial-remainder Sturm sequences verify its exact root count and multiplicity, disjointness and exhaustive real-root coverage, while infinity-to-infinity counts check the missing nonreal roots.
The reviewer does not simply repeat the author's interval isolation or accept its root count.
Exact integer binary square-root search independently verifies every exterior-radius endpoint; the complete products include all multiplicities.
Full root coverage succeeds exactly for(k,s)=(3,0),(3,1),(3,2),(3,3),(4,0),(4,3),(5,4),(6,5).
The other14 trace polynomials each have two uncovered nonreal trace roots, so their full Mahler costs remain undecided.

I also checked that all displayed coarse terminating rational bounds in(11)--(12) are weaker than the native rational endpoints.
They certify s2<s1 and s2<s3 at k3, and s0<s3 at k4.
The complete factor patterns include all powers of t+1,t-1 and the t²+1 factor at k3s3.
The full covers multiply by the same entire original, so the comparison transfers with precisely the same logarithmic difference.
All52 pair decisions are accounted for: only the six k3 decisions and the k4 s0/s3 comparison are strict, and every other comparison remains undecided.
No largest-root substitution or equality from overlapping intervals is used.

All mathematical dictionaries, list lengths, types and expected keys are covered, including counts.
Historical author timestamps, versions, cap/exit and elapsed fields are checked for provenance consistency only, not claimed as recomputed past times.
The two native author files remained byte-identical during the run.
The frozen draft is not a runtime dependency, so fixed retention does not break reviewer reproduction.
J82 retains the full declaration, program and first report.

#### Whole finding and retained limitations

No mathematical defect or author repair is requested.
The complete new argument establishes an actual all-subset same-class construction, its full scalar reduction, a fixed-count leading-cost obstruction, and the fully priced finite nonmonotone improvement and worsening examples.
It does not solve the growing-count problem, price the14 uncovered trace cases, classify the integer congruence class or provide near-one uniform arithmetic income.
All original degrees, factors, dimensions, energies and actual full cover costs remain paid.
This is complete independent review of the frozen responsible material and native evidence; coordinator adoption is a separate act, and G0001 remains active and unresolved.

## Current relationship clarification

The original reviewer reports the complete author proof and native reconstruction, and no contribution to this target's new derivation.
The broad assignment, finite-domain coordination, upstream authorship or access to fixed source interfaces does not itself establish target contribution or inherited substantive proof-development context.
The initial substantive context of the original whole finding is not established by the retained account, so its current relationship is unknown.
Its original date, complete mathematical findings, original counters, different-method implementation and source/finite/uniformity limits remain unchanged.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original complete repeated-cell finding](#repeated-cell-complete-independent-review) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original complete repeated-cell finding](#repeated-cell-complete-independent-review) | [Original full proof](../../ledger/Yin_L_G0346_v1.md#repeated-cell-reuse) | Entire original Sections1–6/(1)–(12), all subset bases and attachments, complete companion/count reduction, all fixed-count coefficient/onset/full-circle costs, whole-root finite comparisons and all original source/failed-method/growing-count limits. |
| [Original complete repeated-cell finding](#repeated-cell-complete-independent-review) | [Output of the recorded run](../../computations/programs/Yin_J_G0082/readme.md#recorded-runs) | Original k3–6/all120 subsets/all22 companions/3084 pencils/12 full selected objects/52 pair comparisons/149 intervals, exactly eight fully priced companions and fourteen undecided nonreal-trace cases; original different-method run retained without a new historical-isolation assertion. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0082/repeated-cell-output.json`; this target locates that original run's computation account. |

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.

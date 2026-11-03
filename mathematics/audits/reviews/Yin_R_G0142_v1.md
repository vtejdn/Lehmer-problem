---
author: Yin
---

# Retained project review: Actual selected Hankel quotients, doubled invariant factors and modular recurrence loss

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0313_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="lower-boundary-complete-independent-review"></a>

### Complete noncontributor review of the selected integral quotient

Review completed 2026-10-10T09:39 by the coordinating AI for Yin.
This is a whole-proof noncontributor AI review of the frozen19699-byte author revision, Sections1--6 and equations(1)--(12).
Root assigned the broad question and source-completeness check but supplied no derivation.
The arrangement is nonblind and shares earlier route history; root reviewed L311 and other upstream work, so no independence from all historical premises is claimed.
Root read the complete new proof directly and reread the actual L63 coefficient pairing, L66 integral trace direct sum, L107 algebraic Lagrange coefficient identity, L300/L304 selected normalization and quadratic control, and the complete Hun74-U005 source audit.
This is not human or formal verification, a fresh audit of every upstream proof, or a review only of the author's summary.

**Whole finding: passed without mathematical repair.**
The full integral equivalence, duplicated invariants, nonreduced modular conclusions, primitive coefficient blocks and selected lower bounds are correct.
The same-invariants control disproves only a measure-free upper bound of the specified kind.
Neither a near-one upper estimate nor an unrestricted gap is proved.
The precise obligations and decisive checks follow.

**Actual domain, pairing and integral equivalence, Sections1--2/(1)--(3).**
The selected object is the same primitive w throughout, with a=S_Q w nonzero and primitive because S_Q is unimodular.
Both orders are the actual monogenic orders; their ranks are d=2s and s.
L107's displayed Lagrange interpolation implies lambda_P(h)=sum h(alpha)/P'(alpha) for the coefficient of degree d-1 of a remainder.
Its separate no-unit-circle dynamical claims are not used.
The original roots are distinct in characteristic zero and all are included.
For G_P, entries vanish at i+j<d-1 and equal1 on the antidiagonal, proving integral unimodularity without a discriminant hypothesis.
With column multiplication matrices, (G_P Mult_O(x))_(ij)=lambda_P(alpha^i x alpha^j), so the orientation in(3), exponent b+s-1 and every index are correct.
Alpha is a unit in O because P has constant1; its multiplication matrix and every integer power are unimodular.
Finally L66's B plus alpha B is an actual direct integral sum, so changing to its displayed basis loses no index.
Multiplication by a becomes two identical M_a blocks.
This verifies the full integer equivalence, not merely equality of determinants or an isomorphism over Q.

**Complete invariant factors, minors and local layers, Section3/(4)--(7).**
Hun74-U005 supplies exactly the finitely generated commutative-PID module statement with its recorded proof completions.
Here all groups are finite Z-modules since Norm(a) is nonzero.
The local Euclidean row/column derivation properly reduces a pivot that fails to divide a remaining entry: after clearing its row and column, adding a row containing that entry creates a smaller Euclidean remainder.
Positive pivot size strictly decreases until it divides the remaining block; recursion then gives the divisibility chain.
Every operation is unimodular.
Duplicating the already ordered list e_1,...,e_s gives a divisibility-ordered list of length2s, including trivial factors.
Its quotient is exactly the double quotient in(2), so finite-module uniqueness gives(4).
The primitive first column of M_a forces the gcd of all entries to be1, hence e_1=1; both initial K_b factors are therefore1, including the s=1 case.

The two-way integer-combination argument correctly preserves every minor gcd under row and column operations.
On the diagonal chain the first-r product divides every r-fold diagonal product and is itself attained.
This proves both formulas(5), including D_0=1, D_1=D_2=1 and the full determinant endpoint.
No assertion that all lower factors depend only on nu is made.
Modulo p, a is nonzero by primitivity.
Writing Q=g_p Q_1 and a=g_p a_1 in the polynomial PID leaves gcd(Q_1,a_1)=1 even when the original factors repeat.
The kernel condition becomes Q_1|f, giving exactly h_p independent residue classes Q_1 v.
Thus the rank and nullity in(6) hold at every prime, with h_p<=s-1.
Modulo p^H, integer unimodular transformations remain invertible and each scalar coordinate contributes p^min(H,v_p(e_j)) kernel elements.
Duplicating them proves(7).
No individual original root receives an unjustified average depth.

**Exact modular cancellation and coefficient content, Section4/(8)--(10).**
The lift t^h g_p(t+t^-1) is monic of degree2h and constant1.
Dividing B_a by it leaves t^(s-1-h) a_1(t+t^-1), which is a polynomial because deg a_1<=s-1-h.
A Bezout identity for Q_1,a_1 remains valid after Laurent substitution.
Powers of t are units in that Laurent ring, and the reduced denominator has constant1, so no ordinary polynomial factor at t=0 is lost.
This proves the entire gcd in(8), including all repeated multiplicities and characteristic2.
The reduced numerator has degree at most denominator degree minus2, remains nonzero, and is coprime to its constant-one denominator.
Every polynomial producing a finite product with the rational series must be divisible by that denominator.
The minimal recurrence degree is consequently the claimed2(s-h); it is a modular statement only.

The first s recurrence columns form a triangular unimodular system since U_0,...,U_(s-1) are monic of their successive degrees and have not required reduction.
Hence the initial coefficient block has content1.
The actual degree-d companion shifts the state by an integer automorphism, preserving its content in both directions.
This proves(9) for every b, without claiming each arbitrary s-block is primitive or any single coefficient equals1.
For n>=d, the first floor(n/d) disjoint blocks each have a nonzero integer coordinate; for s<=n<d, the initial primitive s-block supplies one.
This proves all three support/l1/l2 lower bounds.
Substitution of sum c_l^2=q^2 ell and ell<=s/n gives q^2>=n B_n/s in the stated direction, even for rational q.
The anti polynomial contributes two disjoint signed copies, giving the factors2 in(10).
Unequal coefficient sizes mean that a support bound alone does not give the rejected rho lower estimate.

**Actual selected control and complete expenses, Section5/(11)--(12).**
At P=t^2-A t+1, integer A>=3 and n=2, the recurrence row is(1,A).
Its projection diagonals are1/(1+A^2) and A^2/(1+A^2), so index1 is uniquely selected, w=1, q=L=1+A^2 and a=1.
The polynomial is exactly (t^2-1)(A t^2+t+A), hence M(F)=A because the second quadratic has its two roots on the unit circle; its leading A is retained.
Multiplication by P has low edge -A+(A^2-1)t, whose zero is inside the circle and whose full measure is A^2-1.
Its value at alpha is alpha^3, giving complete edge norm1.
The auxiliary resultant is (1+A^2)^2(4-A^2), including its negative sign; the complete coefficient norms, primitive content, degree4 and radial charge2m are correct.
The retained irreducibility can also be seen from (A-1)^2<A^2-4<A^2 for A>=3.
This is an actual unbounded-scale family with all invariant factors1, fixed d and n/s, but growing total measure.
It refutes only an upper bound determined by those invariant data; it says nothing against an estimate that uses small total m.

The small-m consequence delta=1 is reused at L300/L168's simultaneous degree-linear scope, not assumed for general inputs.
The new q bound becomes only a lower bound on L.
All original signed resultants, individual local depths, coefficient energy, rho, monomial-removal convention and complete leading/root/radial costs in(12) match their retained interfaces.
The integral basis maps in(3) have no asserted small metric norms.
Thus arithmetic module classification is not silently used to pay the original conjugate-coherence cost.

**Source and execution scope.**
Root read Hun74-U005 in full, including its exact source version, pp.225--226 locators, finite commutative-PID hypotheses, uniqueness completion, zero cases, self-review status and expressly uninspected cross-chapter foundations.
That existing accepted scope suffices for the current finite Z-module classification; no new original-PDF read or broader source acceptance is claimed.
L63/L66 supply their already fixed integral mechanisms and L107 only its algebraic interpolation identity.
All new transitions are proved in the author text.
No source identification is outstanding for a recognized theorem used here.
The author's pre-freeze wording clarification for G_P is retained and changes no formula.
No mathematical program, numerical scan, new J or external acquisition was needed or performed in this review.

Appending this finding preserves the entire19699-byte frozen author prefix.
Fixed adoption is a separate coordinator decision.
The full unrestricted G0001 contract and all eight active routes remain unresolved by this restricted theorem.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete lower-boundary review](#lower-boundary-complete-independent-review) | [Integral trace quotient](../../ledger/Yin_L_G0313_v1.md#selected-hankel-trace-quotient) | Entire Section2 and equations2--3, with all integral pairing and actual-order hypotheses. |
| [Complete lower-boundary review](#lower-boundary-complete-independent-review) | [All lower invariants](../../ledger/Yin_L_G0313_v1.md#doubled-lower-invariant-factors) | Entire Section3, equations4--7, finite PID-module input, all minors and prime-power layers. |
| [Complete lower-boundary review](#lower-boundary-complete-independent-review) | [Modular denominator and primitive block](../../ledger/Yin_L_G0313_v1.md#modular-selected-denominator) | Entire Section4, equations8--10, nonreduced cases, all windows and actual selected bounds. |
| [Complete lower-boundary review](#lower-boundary-complete-independent-review) | [Actual scale countercontrol](../../ledger/Yin_L_G0313_v1.md#lower-invariants-scale-boundary) | Entire Section5, equations11--12, actual selection, every original cost and small-total-measure limitations. |
| [Complete lower-boundary review](#lower-boundary-complete-independent-review) | [Reuse and self-check](../../ledger/Yin_L_G0313_v1.md#lower-boundary-reuse-and-domain) | Complete Sections1 and6, recognized source boundary, exact inputs and author-stage history. |
| [Original complete author SELF](#original-lower-boundary-author-self) | [Original L313 proof](../../ledger/Yin_L_G0313_v1.md#complete-retained-proof-and-review) | Whole original Sections1--6/equations1--12, exact integral pairing/direct-sum/quotient, every invariant/minor/prime layer/nonreduced recurrence/coefficient-block/control/source scope. Actual original author SELF/freeze2026-10-10T09:36, not later C617. |


## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete lower-boundary review](#lower-boundary-complete-independent-review) | independently reviewed |
| [Original complete author SELF](#original-lower-boundary-author-self) | self-reviewed |


<a id="original-lower-boundary-author-self"></a>
## Original whole author SELF finding

This complete original author act remains at its actual original L313 input/date, with every source/contribution/clarification/no-program boundary retained, not the later C617.
No new checking or arrangement is supplied by relocation.

<a id="lower-boundary-author-self-check"></a>
### 6. Whole author self-check and freeze

2026-10-10T09:36.
The joint_boundary_research AI for Yin completed a whole written self-check of Sections1--5 and equations(1)--(12).
The check covered the original coefficient/trace pairing, the exact orientation G_P Mult_O(x), the unit alpha^(b+s-1), both integral basis claims and the absence of discriminant division.
It verified the finite Z-module hypotheses of Hun74-U005, the elementary diagonal reduction, primitive first column, the complete duplicated divisibility list, and every even/odd minor-gcd formula including j=0 and j=s endpoints.

The modular check retained nonzero a mod p, all possible repeated factors of Q, the equivalence Q|af iff Q_1|f and dimension h_p, every higher p-power layer, and the Laurent-to-ordinary gcd step using denominator constant1.
The p=2/endpoints case is covered algebraically rather than by a squarefree-root argument.
The state-content proof uses the original degree-d unimodular companion and primitive initial s-block; it does not claim a shorter arbitrary s-block is primitive.
The support/energy count, selected ell<=s/n, rational q and all factors2 in the anti-polynomial norms were checked.

The reused quadratic control was recomputed directly from its row(1,A), including the unique selected index1, primitive scale1+A^2, full signed resultant, edge, all leading coefficients and actual radial degree.
Its measure grows, so it is only the explicitly stated obstruction to a bound based solely on integral invariants at fixed d,n.
No small-total-m counterexample, source novelty claim or measure-free upper bound is inferred.
The initial informal phrase locating the zero part of G_P by "below the anti-diagonal" was replaced before freeze by the unambiguous condition i+j<d-1; no formula changed.

All original root/local-depth and coefficient/leading/radial/coherence expenses in Section5 were reread.
No mathematical program, scan, new J or external-source acquisition was executed.
The scoped material check passed checked:1 before this final record and is rerun afterward.
The entire author text is now frozen for a separately organized complete noncontributor review; this is author self-review, not independent adoption.
G0001 remains active and unresolved.

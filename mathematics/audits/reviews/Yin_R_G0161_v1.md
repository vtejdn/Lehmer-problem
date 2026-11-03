---
author: Yin
---

# Retained project review: Complete sharp golden boundary profiles with overlapping all-window fibers

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0336_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="golden-boundary-complete-independent-review"></a>

### Complete separately organized noncontributor review

Completed2026-10-10T12:23 by root AI for Yin.
I read and checked the ENTIRE21,589-byte author body frozen 2026-10-10T12:20, including Sections1--6, Lemmas1--2, Theorem3, every equation(1)--(16), both exact induction controls, all source/reuse statements and complete author self-check.
The full author prefix is preserved before this appended finding.
Root assigned the broad all-window question and received progress descriptions but contributed no proof step to this draft.
This is separately organized noncontributor AI review, nonblind because shared project context was available, not human or formal verification.

The reviewer authored earlier retained L286 and has other upstream author/review roles.
Its parallel D206 was independently written from L251/L282/L286 and frozen before this review; neither its new conclusion nor any unfinished sibling result is used to check D205.
The common previously fixed bounded-support mechanism is openly reused by both drafts, with distinct claimed consequences.

**Whole finding.**
All claimed results pass at their exact scopes without a requested author correction.
The proof gives a general full-fiber forced-coordinate estimate and sharp C1 on explicit actual golden boundary regions at EVERY window length, including a family with unbounded overlapping accessible relations.
The two exact short-window calculations refute the stated envelope-only sufficient induction, not C1.
The complete interior all-window golden problem remains open.

#### Original law, source/reuse scope and general forced coordinates

I checked the actual full golden Gram and finite-window scope in [L331](../../ledger/Yin_L_G0331_v1.md#golden-carry-profile-fixed-scope), the original truncated-section and coordinate-invariance scope in [L290](../../ledger/Yin_L_G0290_v1.md), and the all-coefficient quadratic short-window statement in [L294](../../ledger/Yin_L_G0294_v1.md).
L286's full hyperbolic scaled support/Gram mechanism is an adequate retained input for the attribution statement; the explicit new bound is independently proved here from the displayed two-embedding formula.
No claim requires a new source theorem, full theta translation inequality, source-priority conclusion or rerun of J83.

Every digit has the original weights1,2,1 over4.
Q=XX^T is twice its stochastic covariance, and the energy is the minimum squared REAL preimage norm.
This remains the relevant metric for deficient rank by the inverse on the range.
The actual finite integer fibers, not a limiting projection, determine each probability.

For every subset of columns, the endpoint is the difference of two iid fair-binary endpoints.
Cauchy--Schwarz gives the maximum at zero, including noninjective maps and the empty subset.
If an entire attained fiber fixes r prescribed nonzero digits, its probability is exactly4^(-r) times the remaining endpoint probability, by independence and the full-fiber hypothesis.
The central event obtained by setting those r digits to zero and returning the remaining map has probability2^(-r)mu_J(0), and is included in the FULL central atom.
Dividing the upper numerator estimate by this lower central estimate gives2^(-r) in the correct direction.
The remaining map may contain arbitrary overlapping relations, and no conditional independence inside one of its fibers is assumed.

When E<=r, 2^(-r)<=2^(-E); when E<r this inequality is strict.
This verifies both versions of Lemma1, with r=0 and an empty remaining block permitted.
Merely finding one representation with r nonzero digits would not suffice; the manuscript explicitly requires those coordinates in EVERY representation.

The deficit identity(4) is a sum of nonnegative terms because digits lie in[-1,1].
A coordinate with absolute functional value strictly larger than the total deficit must use the maximizing sign: zero would already incur its full absolute value, and the opposite sign twice that value.
The strictness at the threshold is necessary and retained.
Unions of several such forced sets are valid; a common coordinate is counted once and an attained word rules out inconsistent sign assignments.
The statement remains sufficient rather than a claim to characterize all integer fibers.

#### Full two-embedding energy, every parity and every prefix

The real embedding matrix is invertible for the actual quadratic, so transforming Q by it preserves the preimage energy.
The complete geometric sums are
U=(phi^(2b)-1)/phi,
V=phi(1-phi^(-2b)), and the cross sum of(-1)^j is epsilon=(1-(-1)^b)/2.
In particular the off-diagonal entry is present before inversion.
Their product has square root phi^b-phi^(-b), giving the normalized correlation r_b used in(8).

The original support bounds follow by summing phi^j and |psi|^j separately.
After dividing their squares by U and V, BOTH upper bounds equal phi^3(y-1)/(y+1), with y=phi^b.
For the normalized correlation matrix, its inverse quadratic form is (a^2+h^2-2r_b a h)/(1-r_b^2).
The elementary inequality2|ah|<=a^2+h^2 gives at most(a^2+h^2)/(1-r_b), with0<=r_b<1.
Thus both coordinates and the odd-window cross term are fully accounted for.

At even b, r_b=0 and the strict factor(y-1)/(y+1)<1 proves the claimed threshold.
At odd b>=3, epsilon=1 and y>2.
Direct multiplication gives (y-1)/(y+1)<1-y/(y^2-1);
the difference has the sign of y-2.
It yields the same strict threshold after the correlation correction.
The deficient b=1 case has energies0 or1 and is treated separately.
Finally2phi^3=4+2sqrt5<9.
This proves Lemma2 at ALL b and every actual endpoint without enlarging a finite computation or presuming any all-window probability ratio.

For the expanding embedding, the functional with sign tau_+ has absolute column values phi^j and forces the common sign.
For the contracting embedding, it has absolute values phi^(-j) and forces tau_-(-1)^j.
If an embedding coordinate is zero, its deficit is the entire positive sum; no column exceeds it, so the arbitrary choice of sign at zero creates no false constraint.
The union convention in(9) is therefore correct.

If that union has at least nine coordinates, the complete energy is strictly below nine and hence strictly below or equal to the integer forced-coordinate count, with strict comparison.
This proves Theorem3.
At b>=9, delta_+<phi^(b-9) forces all last nine indices b-9,...,b-1; delta_-<phi^(-8) forces all first nine indices0,...,8.
The endpoints and strict inequalities in both conditions are correct.
Mixed unions may also supply nine even when neither region separately does.

Any nonzero algebraic power prefix is an invertible real output map.
It preserves all fibers under their bijective output relabeling and preserves the minimum-preimage norm.
Applying the tests after the inverse prefix is therefore legitimate.
No removal of the stable embedding, extension of the endpoint support or free determinant estimate is involved in this coordinate statement.

#### Actual all-window boundary fibers with overlapping relations

The prescribed endpoint z_* is in the actual order and is represented at every b>=12 by twelve alternating nonzero digits followed by zeros.
Its contracting value is the sum of the first twelve positive phi^(-j), exactly phi^2(1-phi^(-12)).
Subtracting it from the length-b maximal contracting coordinate gives the tail sum starting at12.
That finite sum is strictly below the infinite tail phi^(-12)/(1-phi^(-1))=phi^(-10), which is strictly below phi^(-8).
The empty tail at b=12 also meets the inequality.
Thus the contracting boundary theorem applies for every b>=12; no sign requirement on the expanding coordinate is needed.

For a triple, the zero word has integer weight2^3=8 and each signed shifted minimal-polynomial word has weight1.
Each gives the zero algebraic endpoint.
Disjoint triple choices therefore contribute(8+1+1)^k=10^k, the twelve prescribed nonzero prefix digits contribute1, and the remaining r zeros contribute2^r.
Division by4^b gives their exact original probability contribution.
This is only a lower bound on the COMPLETE fiber count; the proof neither replaces the full fiber by the selected product nor mistakes its multiplicity for the central normalization.

For every j=12,...,b-3, a single signed shift of t^2-t-1 fits in the zero tail, has ternary coefficients and preserves z_*.
Comparing it with the zero tail gives an ACTUAL fiber difference.
There are b-14 such shifts when b>=15; their distinct highest degrees prove linear independence.
Consecutive shifts overlap in two coordinates whenever consecutive indices are present.
Thus the full accessible relation span has unbounded dimension and genuine overlap.
The use of a disjoint-triple subfamily to count some words does not imply that the full fiber or full kernel has a disjoint decomposition, and the author does not assert one.

The algebraic degree remains two and total measure log phi.
Growing b, multiplicity and relation dimension are not a growing-degree near-one construction.

#### Both exact failures of the proposed envelope-only step

For b=3, the full power columns are(1,0),(0,1),(1,1).
The zero fiber consists of the zero word and the two signed relation words, with weights8,1,1, giving10.
At x_3=(1,2), the second coordinate forces eta_1=eta_2=1, and the first then forces eta_0=0; its count is2.
The negative fiber follows by sign symmetry.
Direct inversion of Q_3=[[2,1],[1,2]] gives E_3(x_3)=2.
The exact convolution for the new center is therefore2*10+2+2=24.
Replacing the two nonzero counts by their C1 upper bounds yields10*(2+2/4)=25 instead.
This fails to reproduce the required normalization, with ratio25/24, even though all three preceding endpoints are supported.

I separately checked the nonzero control rather than relying on the zero normalization.
At z=(1,0), the two listed words have counts4 and2, and there are no others: solving eta_0+eta_2=1, eta_1+eta_2=0 with ternary digits gives exactly those two cases.
At z-x_3=(0,-2) the listed single word is forced; at z+x_3=(2,2) all three digits are1.
Their counts are1 and1.
Adding x_3 x_3^T gives Q_4=[[3,3],[3,6]].
Its inverse gives E_4(z)=2/3, while the three Q_3 energies are2/3,8/3,8/3.
The exact new count is14, but the envelope yields
10[2*2^(-2/3)+2*2^(-8/3)]=25*2^(-2/3), strictly above24*2^(-2/3).
Hence separately treating the next center does not repair this particular proposed sufficient step.

These calculations are complete displayed hand fibers and exact arithmetic, with no numerical tolerance or unrecorded program.
They establish a failure of that SUFFICIENT bound.
The actual C1 inequalities in these short windows remain established by L294, and the draft does not confuse a loose upper bound with an actual counterexample.

For(16), substitute c_b(w)=c_b(0)H_b(w)2^(-E_b(w)) into the exact three-term convolution and divide by the ACTUAL next center.
The displayed weights2,1,1 and exponents are then exact.
The off-support H=0 convention preserves every missing endpoint without trying to assign it positive probability.
For b>=2, Q_b is invertible on the full plane, and x_b=x_(b-1)+x_(b-2) is itself attained by two distinct nonzero digit positions.
Center symmetry gives d_b=2+2*2^(-E_b(x_b))H_b(x_b).
At b=3 its actual H is(2/10)*4=4/5, exactly the deficit lost by setting it to1.
Thus the recurrence identifies the missing correlated deficit data, but does not prove they satisfy a preserving invariant at all later times.

#### Complete conclusion and remaining obligation

The whole proof retains the original weights, both golden embeddings, exact Gram convention, complete central atoms, all fiber words in each claimed inequality, parity/rank boundaries, strict exposed thresholds, prefix invariance and the proper distinction between a selected subfamily and a full fiber.
No defect or correction request was found.

The result supplies an infinite-window SHARP boundary class, and the obstruction rules out one explicitly formulated one-step proof strategy.
It supplies neither all-window C1 in the interior nor a full endpoint hypothesis for L286's sharp transfer.
The general interior comparison must preserve more information than the envelope alone; the exact recurrence or labelled carry product remains a possible starting point.
No computation/source scope was expanded in this review.
Fixed retention and coordinator adoption remain separate actions after this complete finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete retained finding](#golden-boundary-complete-independent-review) | unknown |

The whole original mathematical finding, original date and necessary positive/negative/source/cost limits above remain unchanged.
The account records visible progress descriptions or available shared project context but does not establish their actual substantive content and timing relative to initial inspection.
The prior accepted-input authorship and own earlier reviews do not alone imply contribution to this new proof; the historical noncontributor title does not establish initial isolation.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete retained finding](#golden-boundary-complete-independent-review) | [Original full mathematical input](../../ledger/Yin_L_G0336_v1.md#golden-boundary-profile-reuse) | Whole original Sections1--6/Lemmas1--2/Theorem3/(1)--(16), arbitrary-map forced-coordinate proof, full golden energy and strict boundary/overlapping fibers, both exact envelope-only countercontrols, recurrence and all complete-fiber/source/cost limits. |

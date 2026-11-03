---
author: Yin
---

# Retained project review: Unbounded single-column exclusions for the actual conference path basis

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0250_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="unbounded-column-complete-independent-review"></a>

### Complete separately organized noncontributor review

Review time: 2026-10-10T00:19.
Reviewer: structural_research AI for Yin, assigned by the coordinating AI after the author's explicit final freeze at08:14.
The reviewer read every part of Sections1--6 and equations(1)--(8), all fifteen native J54 author files, the complete consumed L246 proof/interface, L191's actual comparison, L238's reflection-product identity and the HPM22 scoped attribution record.
The assignment and shared conversation supplied the broad problem and the proposed conclusions; this is a non-blind review.
The reviewer contributed no new equation, substitution, modular obstruction, theorem or author program in D117.
The reviewer previously performed the separately retained full D113/L246 review and authored the earlier signed-cover construction; those upstream roles are disclosed, not counted as new independent reviews of the reviewer's own work.
The current author, orbit_research, did not participate in this review's derivation or implementation.

**Finding.**
The complete fixed-order, all-coordinate single-column exclusion passes.
No mathematical defect, required author correction, missing column or unsupported source transfer was found.
The conclusion is precisely(8), for the stated actual lattice, ordered path basis and one-column construction, with arbitrary integer replacement size.
It does not exclude arbitrary root bases, later column reorderings, two-column replacements, other lattices or other neutral multipliers.
The finite unsuccessful parameter search remains separate evidence and is not used to infer the unbounded theorem.

#### Actual basis, full determinant and target equivalence

Direct integer multiplication in the separate checker reconfirmed the displayed G0, C^2=5I, det G0=-1, det Q0=1 and every entry of H=Q0^T G0 Q0.
The path columns have norm two.
Replacing column i by Q0 c multiplies the determinant by exactly c_i, so c_i=+/-1 is necessary and sufficient for an integer basis.
Reversing its sign gives diagonal sign congruence of the reconstructed upper-unitriangular V; its full determinant polynomial is unchanged.
It is legitimate to impose c_i=1.
The remaining coordinates are unrestricted integers, and c^T H c=2 supplies exactly the one changed diagonal.
Reconstructing V from the upper half of the Gram retains the symmetric form, not the original bilinear polynomial, as the author explicitly states.

The determinant is monic reciprocal of degree six with both endpoint coefficients one.
For norm-two bases p_V(1)=det G0=-1, hence c_0=-3-2a-2b.
At -1 the matrix is V^T-V, with the same determinant as V-V^T in even dimension.
Its determinant is the square of the six-dimensional alternating Pfaffian; substitution in the reciprocal coefficient expression gives5+4b.
Thus a=-2 and Pf=+/-3 imply b=1 and c_0=-1, and conversely the full target forces these values.
This checks the WHOLE target, including middle coefficient, multiplicities and both endpoint identities.
No implication is based solely on matching modulo a prime.

Only one row and column of off-diagonal V entries vary, each linearly in the free coordinates; its diagonal remains one even at interpolation points failing the norm equation.
Each determinant term therefore has degree at most two in these coordinates.
Each Pfaffian term contains the varying index once, so its degree is at most one.
The norm is also quadratic.
These bounds justify the finite unisolvent identity certificates; they do not claim that non-norm-two interpolation points are admissible bases for the theorem.

#### Central columns and the complete lifting contradictions

All displayed general polynomials(2),(3),(6), both signs k=1,4, the eliminated coordinate formulas and the stated linear combinations were checked against independently recovered actual determinant identities, rather than assumed from the author's generator.
For column3 the unimodular change x2=y+2v and the Pfaffian substitution x1=5x+y-k lose no integer solutions.
Modulo3, D=(x-y)^2-(x-y)+1 forces y=x+1.
The norm then becomes the stated sum of two squares, giving v=-x-1 and z=x-1.
Each gradient is divisible by3 at every such residue, so the entire value modulo9 is unchanged by all lifts by multiples of3.
This follows from the exact quadratic Taylor expansion; it is not an assumption that a mod3 survivor automatically lifts.
The only x residue surviving D modulo9 is2 for k=1 or1 for k=4.
At the corresponding representatives N is3 modulo9.
This supplies the claimed all-integer contradiction for column3.

For column2, x3=k-3v-w is integral for both signs and N=0,R=A+3N=0 is equivalent to the original norm/coefficient system.
The exact reductions N=x(1+b)+kv+w and R=kv+w+1 modulo2 imply x odd, b even and kv+w odd.
At those residues every derivative of R-N is even, so its modulo4 value is invariant under all even-coordinate changes.
With x=1,b=0 and v,w reduced modulo2, the displayed value is2(kv+w) modulo4.
The remaining constant -k(3k+5) is divisible by4 for both1 and4.
Hence R-N is2 modulo4, contradicting the two zero equations.
The reviewer also checked that the author's output uses N=A=0, which is equivalent to N=R=0 at every modulus, including2,4,8 and9.
No division by3 was used.

The unsuccessful bounded test was separately checked as exactly two k values and41^3 triples, with no bound on the fourth coordinate.
For a nonzero coefficient of x in R, integer divisibility gives its only possible value.
In a singular case R is either a nonzero constant and impossible, or identically zero in x, when the monic norm quadratic is decided by its exact discriminant and parity.
All cases are covered.
The scope137842,838 singular cases and2953 nonsingular integral candidate cases is accurate.
This finite test is not an unbounded premise; the later modulo4 argument supplies that premise.

#### The other four columns and the parity model

The L246 reduced quadratic model was reread at its actual scope, including the even eight-coordinate space modulo all-ones.
Every quadratic-value-one class is represented by a two-element subset: even weights2 and6 are interchanged by complementation.
The six Q0 columns are the stated path edges0--1--...--6 with vertex7 isolated.
Deleting edge i leaves exactly the three component sizes i+1,6-i,1.
An edge inside a component gives a cycle relation or a repeated edge and cannot complete an independent reduced basis.
An edge joining two components gives a forest with two components.
The forest edge span consists of vectors with even parity on each component; thus all-ones is in that span precisely when both sizes are even.
After taking the quotient, independence is equivalent to both sizes odd.

At ends i=0,5, the only independent completion of1,6,1 therefore has sizes7+1.
In any edge order, successive edge transpositions merge cycles on distinct current forest components, so their product has a7-cycle and a fixed point.
Restriction to the even subspace followed by quotient by its invariant all-ones line removes two factors t-1, leaving Phi7.
This reasoning does not require semisimplicity in characteristic2.
The target reduces to Phi3 Phi5 and has a different t^5 coefficient.
End replacements are excluded at every integer size.
The same reasoning allows3+5 at the four internal positions and hence cannot replace their stronger arithmetic arguments.

For position1 the independently recovered signed Pfaffian is5-10x0.
Its divisibility by5 contradicts either target sign.
The rational values1/5 and4/5 are retained in the output as nonintegral exclusions, not falsely promoted to bases.
For position4 the substitution x5=-2b+2d+k is integral and complete.
Direct reduction of(6) gives exactly the two printed modulo2 equations.
Splitting d=1 and d=0 yields the unique common class(1,0,1,0).
At that class every derivative of A is even; quadratic lifting by2 preserves its value modulo4.
The exact value -4k^2+8k-6 is2 modulo4 for both signs.
This finishes all six positions with no omitted root, sign or coefficient-size case.

Independent sign changes do preserve the determinant by diagonal sign congruence.
Arbitrary new orderings need not preserve it, and are correctly outside the final theorem.
The known changed sextic in L246 has b=-1 and alternating endpoint1, so it does not contradict the target-specific obstruction with b=1 and endpoint9.

#### Genuinely separate exact implementation and actual execution

Reviewer-only [review_independent.py](../../computations/programs/Yin_J_G0054/review_independent.py) and review_result.json (`mathematics/computations/outputs/Yin_J_G0054/review_result.json`) retain the separate implementation and execution.
It imports no author implementation and does not run the author symbolic generator.
Full determinant polynomials are obtained by evaluating det(tV+V^T) at seven integer t values using fraction-free Bareiss elimination and recovering all seven coefficients by exact rational Newton interpolation.
This differs both from the author's nilpotent-inverse trace generator and from the author's subset polynomial determinant verifier.
The signed Pfaffian is computed from its6! alternating-sum definition divided by48, and its square is separately checked against the skew determinant.
All arithmetic making a mathematical decision is integer or Fraction/symbolic rational arithmetic.

A signed stencil0,+/-e_i,e_i+e_j, different from the author's0,e_i,2e_i,e_i+e_j stencil, reconstructs all constant, linear, square and mixed coefficients.
This requires84 full polynomials and588 scalar determinants for the four symbolic columns.
It verifies36 saved polynomial identities, including all sign eliminations and difference expressions.
A separate repeat of the author's84 stated sample inputs, using this different determinant method, confirms its exact24 norm-two endpoint count.
Every saved survivor LIST, not just count, was independently reproduced for all26568 mod3/mod9 tuples,8736 mod2/mod4/mod8 tuples and13828 final-column tuples.
The checks use polynomials recovered by the reviewer's determinant interpolation.
All nonempty mod3/mod9 survivor sets remain matched and are not misreported as exclusions.

The bounded solve is also independently organized: the reviewer first solves the monic norm quadratic in x by its exact discriminant for each of137842 triples and only then tests the linear R condition.
This reverses the author's primary linear-elimination procedure, reproduces the zero target count, and separately confirms838 singular linear cases and2953 nonsingular integral-x cases.
Every one of64 binary classes was examined at each of six positions.
The admissible class counts are12,12,16,16,12,12; all80 admitted classes have an independently computed full polynomial with exactly the predicted Phi7 or Phi3 Phi5 reduction.
In particular each end has only the7+1 partition.
This finite complete check corroborates, and does not replace, the written all-size quadratic-model argument.

The first full reviewer execution passed at 2026-10-10T00:17.
After making the optional future fixed-prose locator explicit, the unchanged mathematical checker passed again at 2026-10-10T00:18, in1.212 seconds under the repository Python3.12.14.
Operational timing is recorded only as such.
Fifteen native author J files, including their readme and seven outputs, compared byte-for-byte equal before and after each run.
The frozen D117 text was also unchanged.
These are within-run no-write observations, not new hashes or historical fingerprint gates.
D117 and the planned fixed L250 are OPTIONAL prose observations; neither's existence, size or historical bytes is a mathematical input or future execution precondition.
The checker remains directly runnable after draft retirement.
Its actual mathematical inputs are the explicit seed and native J54 evidence.
No original program/output was overwritten.

#### Costs, sources and scope disposition

The L191 comparison was checked at k=4: the actual B rows(1,1),(0,1),(0,1),(0,1) give rank6, height1, energy5 and Phi2^2 P4.
All B entries are nonnegative, so the absolute companion is identical; the literal cover has rank12, height1, energy10 and full polynomial Phi2^4 P4^2.
The retained L246 matrix, complete irreducible sextic, companion, and cover costs were checked at the reused interface: rank6/height2/energy24, complete companion coefficients1,-38,-61,-69,-61,-38,1, cover rank12/energy48, beta4<lambda<2,38<rho<40 and the stated strict ratios.
This review does not rerun J53 or represent its prior certificate as newly executed.
The earlier complete separate L246 review remains its retained evidence.

HPM22 remains only the prior, precisely limited conference-construction attribution.
The source readme and L246's retained direct matrix proof were read.
The reviewer previously inspected the actual HPM22 v3 pp.1--2 in the L246 review; that is reused historical source-inspection evidence, not a new PDF read or an enlarged external theorem adoption in this round.
No conference classification, E8 classification, McM02 spectral-gap theorem or source-wide proof audit is needed for D117.
The signed coordinate-update reflection identity is the direct retained L238/L246 matrix identity; its broader Coxeter theorem is not imported here.

All full target and companion factors remain charged.
The requested Phi6 P4 is still unrealized, and no unknown companion is assigned a small cost.
The two-column determinant-minor proposal is a legitimate next question, not a proved construction or reason to suspend other routes.
There is no unrestricted realization exclusion, optimized-cost theorem, varying-input near-one conclusion or G0001 completion.
The author-prefix bytes are preserved exactly by appending this review; no author repair was requested.
Fixed adoption and any navigation/retirement are later coordinator actions, separate from this completed proof and evidence review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original complete finding](#unbounded-column-complete-independent-review) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Original fixed L250](../../ledger/Yin_L_G0250_v1.md#complete-retained-proof-and-review) | Entire Sections1--6/equations1--8, all six positions, signs, complete modular/forest arguments, finite unsuccessful test, exact identity certificates and full costs. |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Original J54 group](../../computations/programs/Yin_J_G0054/readme.md) | All fifteen original author files and separately implemented reviewer code/output at the exact finite scopes detailed in the finding. |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Consumed L246](../../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) | Complete consumed conference seed, integral basis, reduced quadratic/reflection interface and actual sextic/companion/cover costs; no J53 rerun. |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Original quartic](../../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Actual k4 full Phi2-squared P4 comparison and complete signed-cover cost. |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Signed reflection interface](../../ledger/Yin_L_G0238_v1.md) | Reused coordinate-update reflection identity only, as explicitly described in the finding. |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Original source attribution](../literature/HPM22/readme.md#paley-conference-attribution) | Previously read v3 pp1--2 applicability/attribution, reused without a new PDF read or conference classification theorem. |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Reviewer implementation](../../computations/programs/Yin_J_G0054/review_independent.py) | Separate Bareiss/Newton/signed-stencil/Pfaffian implementation and all original stated residue, bounded-solve and binary-class checks. |
| [Original complete finding](#unbounded-column-complete-independent-review) | [Output of the recorded run](../../computations/programs/Yin_J_G0054/readme.md#recorded-runs) | Actual complete original native result, including nonempty survivor sets and all count/scope boundaries; no later execution is backdated. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0054/review_result.json`; this target locates that original run's computation account. |

The explicit relationship records the original account's known shared proposed conclusions and shared mathematical conversation before this check.
Its distinct implementation and lack of a new proof contribution remain true, but that disclosed shared substantive context makes the whole agent finding self-review under the current rule.
The upstream signed-cover authorship alone is not the basis for that classification.
The original date, verdict, whole mathematical scope, source depth and actual runs above remain unchanged; this administrative declaration performs no new review and binds no later Claim.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.

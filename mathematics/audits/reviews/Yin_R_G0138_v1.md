---
author: Yin
---

# Retained project review: Growing weighted cycles with linear positive irreducible degree and controlled companion ratio

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0295_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Entire original written finding](#weighted-cycle-complete-written-review) | self-reviewed |
| [Entire original computational finding](#weighted-cycle-complete-computational-review) | self-reviewed |

The written reviewer explicitly received candidate formulas before inspection, and the computational reviewer explicitly knew root's earlier whole finding before its check.
Both are SELF; separate implementation and noncontribution do not create isolation.
The original full no-defect findings, contribution/source boundaries, mathematical and native inputs, actual timings and finite costs below are retained without a new review.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Entire original written finding](#weighted-cycle-complete-written-review) | [Original full L295 proof](../../ledger/Yin_L_G0295_v1.md#complete-retained-proof-and-review) | Entire original Sections1--7, every formula, actual full matrices, all-index root/degree/limit/source/cost statements; actual review2026-10-10T05:52. No later C extraction is backfilled as input. |
| [Entire original computational finding](#weighted-cycle-complete-computational-review) | [Original full J74 scope](../../computations/programs/Yin_J_G0074/readme.md) | Every native mathematical field of six inputs a=3,...,8, all18 full arrays, 282 integer pencils and all declared secondary checks, exact original author results and no expansion; actual finding2026-10-10T05:58. Not an all-a proof by extrapolation. |

<a id="weighted-cycle-complete-written-review"></a>

### Complete separately organized noncontributor written review

Review completed2026-10-10T05:52 by the coordinating AI for Yin after orbit_research's2026-10-10T05:50 author freeze.
The review covers the entire author body, Sections1--7 and all formulas(1)--(13), including(11a)--(11c), actual matrices, all-root and all-index proofs, factor arithmetic, limiting and finite costs, source/reuse boundaries and computational claims at their stated role.
Root assigned the broad question and J allocation but contributed none of the construction or proof.
Candidate formulas and progress summaries were shared before this inspection; this is a separately organized NONBLIND noncontributor review, not historical independence from all project work.
Root earlier reviewed L291; that upstream role is disclosed.
J74's complete saved computational payload is assigned separately to resultant_research and is not certified by the present written review.
No human or formal verification is claimed.

**Whole written finding: the complete argument passes at its stated scope, with no defect or author repair required.**
It constructs changing full signed/absolute determinants with exactly one expanding pair each, companion-to-original logarithmic measure ratio tending to one, and positive irreducible-factor degrees bounded below linearly in the index.
The log4 limit is positive; this does not approach the unrestricted near-zero target or prove general representation or cost optimality.

#### Exact construction and complete determinant interface

The reviewer reread L184's matching/full-cycle determinant proof, the actual D9 interleaved proper-cover identity, and L203's retained monic-unit factor/circle-root scope.
For a>=3, the diagonal, superdiagonal and lower-left entries of B are distinct positions.
The associated bipartite support is a simple even cycle, including a=3.
There are2a-1 unit edges and one magnitude-two edge, so the squared energy is2a+3 and the actual height is2.
V has rank2a and unit diagonal; its absolute companion is precisely the D block.
The D9 cover doubles rank and energy while preserving height and gives the WHOLE product polynomial, without dividing the logarithmic measure by two.

In the determinant expansion every allowed nontrivial permutation is either a union of edge transpositions or one of the two full cycle traversals.
The transposition on the heavy edge changes its factor from -t to -4t; deleting its two endpoints leaves the unit path on2a-2 vertices, whose retained recurrence gives C_(2a-2).
The resulting difference is exactly -3t C_(2a-2).
The heavy signed edge product -2 and the even cycle's permutation sign -1 give +2 for each traversal; the all-negative absolute product +2 gives -2.
Bipartition order puts a factors t on each traversal.
This proves both complete formulas, including their middle signs.
Block elimination independently yields the polynomial identity t^a det((t+t^-1+2)I-B^T B); the apparent Laurent expression is polynomial after multiplication.
Multiplying by t-1 gives the displayed sparse numerators with constants4t-1.
Evaluating at1 gives9-6a and1-6a, both nonzero for the entire range; t-1 is an algebraic numerator multiplier, not a determinant factor.

#### Every root and the unique exceptional pair

For I plus the weighted cyclic shift, only identity and the complete a-cycle contribute to its determinant, yielding1+2(-1)^a and1-2(-1)^a.
These are nonzero.
Hence both Gram matrices are positive definite and no lambda=0 endpoint is concealed.
On the cycle with all edge magnitudes one, each coordinate occurs twice in the sum of2|x_i x_j|, proving the adjacency norm bound2 directly.
Restoring the heavy edge changes only a quadratic cross term and that change vanishes on x_u=0.
A two-dimensional negative spectral space for2I-H would meet this codimension-one subspace nontrivially, contradicting its nonnegativity there.
This proves at most ONE singular value greater than2 counted with multiplicity, equivalently at most one Gram eigenvalue above4; neither a simplicity assumption nor a classification theorem is being inserted.

The four exact signs in(5) are correct: with y=3^a>=27, -y^2+8y+11<0, and with y=5^a>=125, y^2-16y+19>0.
The two signs at4 follow immediately.
Each polynomial therefore has a root in its claimed interval, exhausting its one allowed exceptional Gram eigenvalue.
That eigenvalue has multiplicity one, so its two reciprocal positive roots are simple.
Every other positive Gram eigenvalue is below4 because values at1 are nonzero; zero was excluded already.
Its trace parameter lambda-2 is strictly between-2 and2, giving the complete remaining circle roots with any multiplicities preserved.
This justifies the exact full measures in(7), including the literal cover, rather than merely a largest-root estimate.

#### Monotonicity, limits, factor growth and exact expenses

Subtracting t^2 N_a from N_(a+1) cancels the leading sparse term and leaves exactly(8) and(9).
The original difference is strictly negative for t>1.
For the absolute difference at t>4, division by t-1 reduces to4t^(a+1)(t-1)>(4t-1)(t+1); the displayed elementary comparison is sufficient.
Each new numerator has exactly one root above1; its sign is negative between1 and that root and positive above it, by the preceding full root classification and positive leading coefficient.
Thus evaluation at the old roots yields both strict directions without an unjustified inference from only one endpoint value.
Dividing(3) by t^(2a) at roots in[3,5] makes both error terms uniformly tend to zero.
The only possible limit is4, proving the complete logarithmic ratios and positive limits.
No exchange of a singular logarithmic integral with a limit is used.

Every monic integer factor of a monic unit polynomial has constant term+/-1.
A factor containing the unique expanding beta must also contain its reciprocal because otherwise the product of the moduli of its roots would be beta rather than one.
All its other roots are on the circle.
The reciprocal polynomial shares that reciprocal root and irreducibility makes the factor reciprocal; all remaining monic integer factors are cyclotomic under the retained Kronecker interface.
This interface is accepted at its recorded scope, not newly proved or source-wide audited here.
Simplicity of beta gives multiplicity one of the positive factor.
The same proof applies to alpha.
Strict movement makes these factors pairwise different within each family, and the displayed coefficient bounds give finiteness at bounded degree and bounded root modulus.
Thus growing rank really does carry unbounded positive irreducible degree.

The stronger estimates follow from(3) at each root.
In the beta case the error is bounded by12*3^-a+15*3^-2a<13*3^-a for a>=3; in the alpha case omitting its negative term gives16*4^-a.
The integers F_a(4), G_a(4) are nonzero because4 lies strictly between the two exceptional roots and off every unit circle.
Their contracting root contributes a factor less than4, and each other conjugate a factor at most5.
This proves the constants52 and64 and the two stated strict linear degree bounds.
Finally log(alpha/beta)<(alpha-beta)/beta, beta>3 and log beta>log3 give exactly(11c).
Every factor and original rank remains present; none of these estimates converts log4 into a vanishing total input measure.

#### First index, reuse and finite-evidence limits

The sextic formulas at a=3 and both trace cubics were expanded directly.
The rational-root candidates and all six displayed values are correct.
Each cubic is therefore irreducible over Q.
The Gram classification makes its trace field totally real and supplies two embeddings in(-2,2); at either one, v^2-4 is negative.
A square in this totally real field cannot have a negative real embedding, so the quadratic lift has degree two and the complete sextic is irreducible.
This checks full irreducibility only at the specified first index, not all indices.
Rank6/6/12 and energies9/9/18 follow from the actual matrices, and no earlier exclusion of a different prescribed sextic is contradicted.

The cycle matching method, block identity, circle-factor criterion and broad bounded-measure phenomenon are explicitly reused from the responsible earlier materials.
This direct changed family imports no new Coxeter classification or uninspected source theorem and makes no novelty or universal realization claim.
The six J74 controls are declared finite supporting checks; their successful author reports cannot establish the all-a proof by extrapolation and are left for the separately assigned full computational review.
The whole written scope is supported without a numerical root solver, search coverage assumption, or discarded neutral multiplier.
G0001 remains active and unresolved.


<a id="weighted-cycle-complete-computational-review"></a>
### Separate complete native-computation review

At2026-10-10T05:58 the resultant_research AI for Yin completed the ENTIRE [J74 native-payload review](../../computations/programs/Yin_J_G0074/readme.md#weighted-cycle-complete-independent-payload-review), following root's separately recorded whole written-proof review.
The reviewer supplied none of this D162 mathematics or author code.
Shared progress, author freeze and root's finding were known; the review is nonblind and AI-based.
Its earlier J69/J72 review roles and reuse of its OWN standard-library primitives are disclosed, without importing an author implementation or a prior generated result.
The complete written argument and actual convention interfaces were read to determine what the computation must certify; root's preceding finding remains the full all-index proof review.

The sole independent run passed at2026-10-10T05:57 in0.0931965seconds under the predeclared120-second aggregate cap, for exactly a=3,4,5,6,7,8.
The different exact implementation uses integer Bareiss pencils and forward Newton interpolation for all18 complete original/absolute/literal-cover polynomial arrays; it uses no characteristic-polynomial routine, SymPy or author import.
All282 saved pencil times/values, twelve separate Fraction-elimination B/D determinants, full literal matrices, all ranks/heights/energies, every formal numerator/difference coefficient, all endpoint and trace arrays and both first-index rational-root lists/values match.
Whole cover products and neutral factors are retained.
Complete method and payload coverage are recorded in J74, not inferred from a single acceptance flag.

All three author-native files and the then-current full draft were directly byte-compared before and after execution and were unchanged.
The draft availability observation is optional and has no mathematical role, so fixed retirement creates no proof-program dependency.
There was no failed run, new parameter search, numerical root approximation or author correction.
This append preserves the author proof and root's entire review.
The complete native computational evidence passes without a defect; all-a root behavior, factor-degree estimates and limits retain their separately checked written proofs rather than an extrapolation from six cases.
No new mathematical conclusion or fixed adoption is asserted by this review.

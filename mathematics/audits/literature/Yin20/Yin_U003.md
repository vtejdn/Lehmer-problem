---
author: Yin
---

# Yin20: rational expressions, the free field and linear representations

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

<a id="yin20-u003"></a>
## Yin20-U003 — Chapter IV introduction and Sections IV.1–IV.3

- Source: [Yin20](../../../literature/pdf/Yin20.pdf), Chapter IV introduction and IV.1–IV.3, printed pp. 49–56 / PDF pp. 59–66.
- Source.
- Task: [Yin20 inner-rank source audit](readme.md#yin20-inner-rank-source-audit), assigned 2026-09-10.
- Author and source reconstruction: the rational-expression agent.
- State: complete source reconstruction; independent artifact review pending.
- Scope: every definition, numbered result and representation rule in the assigned pages, their supporting prose and the transition to IV.4 on printed p. 56.

This unit distinguishes the literal source, locally reconstructed arguments, necessary corrections, and retained external interfaces.
It does not certify a rereading of all cited books and papers.
The source PDF remains unchanged.

### 1. Reading evidence and result inventory

All eight assigned PDF pages were read freshly from the supplied artifact.
The arithmetic-circuit definition on printed p. 50, localization and representation definitions on pp. 54–55, and all algorithm blocks on p. 56 were additionally inspected as rendered pages.
In particular, the sign discrepancy in the inverse rule is present in the rendered source and is not an extraction error.
The source bibliography entries were checked on printed pp. 93–94 / PDF pp. 103–104.
The [primary Cohn book](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/cohnfr.pdf), registered in this repository as `Coh06` and cited by Yin20 as `[Coh06b]`, was additionally checked at the selected passages listed in §7.
This is distinct from the repository's `Coh06b` historical survey.

| Location | Complete item covered | Outcome |
| --- | --- | --- |
| IV introduction, p. 49 | Route from Sylvester domains to the free field; expressions, representations, evaluation and closures | Accurate roadmap; no boundedness conclusion |
| Definition IV.1.1, p. 50 | Rational-expression arithmetic circuit | Add acyclicity to the literal graph specification |
| IV.1 prose, pp. 50–51 | Syntactic examples and two rational identities | Correct as formal skew-field identities on their admissible domains; arbitrary-algebra scope needs care |
| Definition IV.1.2, p. 51 | Recursive evaluation and ambient-algebra domain | Correct; every inverse is taken in the specified ambient algebra |
| IV.1 closing prose, p. 52 | Evaluation equivalence, degeneracy, Amitsur and matrix constructions | Arbitrary-algebra overlap relation is not generally transitive; retain the appropriate-ambient construction interfaces |
| Definitions IV.2.1–IV.2.4, pp. 52–53 | Epic fields, subhomomorphisms, specializations and universal fields | Definitions and elementary implications reconstructed; specialization-category machinery retained from Cohn |
| IV.2 localization prose, pp. 53–54 | Scalar and matrix localization | Correct `φ(A)` to `φ(S)` in the scalar-localization sentence |
| Theorem IV.2.5, p. 54 | Sylvester-domain/universal-localization equivalences | Exact external theorem interface retained |
| IV.2 conclusion, p. 54 | Free algebra, free field and preservation of polynomial inner rank | Follows from Chapter III and Theorem IV.2.5 |
| Definition IV.3.1 and Theorem IV.3.2, pp. 54–55 | Algebraic linear representations and their existence | Existence reconstructed using corrected formal representations and the retained free-field interface |
| Definition IV.3.3, p. 55 | Formal representations with ambient-algebra domain preservation | Correct after interpreting matrix invertibility in the matrix algebra |
| Algorithm IV.3.4(i), p. 56 | Scalar and variable rules | Explicit inverse checked |
| Algorithm IV.3.4(ii), p. 56 | Sum and product rules | Both checked, including asymmetric product block sizes |
| Algorithm IV.3.4(iii), p. 56 | Inverse rule | Literal rule represents `−r⁻¹`; a one-sign repair is necessary and sufficient |
| IV.3 closing prose and IV.4 opening, p. 56 | Fullness for nondegenerate expressions and evaluation warning | Specify matrix-nondegeneracy or free-field admissibility; arbitrary ambient nonempty domain does not suffice |

### 2. Rational syntax and evaluation domains

Write `P=ℂ⟨x₁,…,x_d⟩` and use `B` for an ambient unital complex algebra, to avoid confusing that algebra with a matrix named `A`.
The source's expression syntax allows scalar and variable inputs, addition, ordered multiplication, and inversion.
An expression is syntactic data rather than merely its eventual value.
Thus `0⁻¹` and `(x−x)⁻¹` are permitted expressions with empty evaluation domains in every nonzero unital algebra.
The meaningful recursive definition is a finite directed **acyclic** arithmetic circuit with a unique output.
Definition IV.1.1 literally specifies a finite directed graph and vertex degrees, but does not impose acyclicity.
A graph containing a feedback cycle may satisfy those listed degree conditions and have no recursive evaluation.
Adding acyclicity repairs this omission; in a finite acyclic graph with a unique sink, every vertex already reaches that sink.

Definition IV.1.2 is reconstructed recursively as follows:

\[
\begin{aligned}
\operatorname{dom}_B(c)&=\operatorname{dom}_B(x_j)=B^d,\\
\operatorname{dom}_B(r+s)&=\operatorname{dom}_B(rs)
 =\operatorname{dom}_B(r)\cap\operatorname{dom}_B(s),\\
\operatorname{dom}_B(r^{-1})
 &=\{X\in\operatorname{dom}_B(r):r(X)\in B^\times\}.
\end{aligned}
\]

Evaluation uses the displayed operations in `B` at each circuit node.
Consequently, a final value belonging to a smaller subalgebra does not place the original expression in that subalgebra's evaluation domain.
For a finite von Neumann algebra `M`, membership in `dom_{𝒰(M)}(r)` and the additional fact `r(X)∈M` do not, by these definitions, imply membership in `dom_M(r)`.
The first domain permits intermediate affiliated inverses; the second requires every intermediate inverse to be bounded.

The source's first informal reduction,

\[
y(xy)^{-1}x=1,
\]

is valid in a skew field wherever `xy` is invertible: both `x` and `y` are then nonzero and invertible, so `(xy)⁻¹=y⁻¹x⁻¹`.
It is not an identity on every arbitrary-algebra domain; the example below gives the precise obstruction.
For the second reduction, assume all displayed inverses exist in a skew field and put `w=yx−1`.
Then

\[
x-y^{-1}=y^{-1}w,
\qquad xyx-x=xw,
\]

and hence

\[
\begin{aligned}
(x-y^{-1})^{-1}-x^{-1}
 &=w^{-1}y-x^{-1}\\
 &=w^{-1}\bigl(y-wx^{-1}\bigr)
 =w^{-1}x^{-1}
 =(xyx-x)^{-1}.
\end{aligned}
\]

This verifies the second displayed rational identity on its expression domain.

The p. 52 relation says that `r` and `s` are `B`-evaluation equivalent if their domains have a nonempty intersection and their values agree throughout that intersection.
For a general unital algebra, this overlap relation need not be transitive, even among expressions with nonempty domains.
Here is an explicit correction to the literal arbitrary-algebra prose, proposed independently by the coordinating reviewer and checked in this reconstruction.
Take `B=B(ℓ²(ℕ))`, let `S` be the unilateral shift, and consider

\[
r_1=1,\qquad r_0=x^{-1}x,\qquad r_2=y(xy)^{-1}x.
\]

On the domain of `r₀`, its value is `1`, so `r₁` and `r₀` are equivalent.
On the common domain of `r₀` and `r₂`, both `x` and `xy` are invertible, so `y=x⁻¹(xy)` is invertible and `r₂=1=r₀`.
This common domain is nonempty, for instance at `x=y=1`.
However, at `x=S*` and `y=S`, one has `xy=1`, while

\[
r_2(S^*,S)=SS^*\ne 1=r_1(S^*,S).
\]

Thus `r₁` is equivalent to `r₀`, and `r₀` to `r₂`, but `r₁` is not equivalent to `r₂`.
The source immediately proceeds to the need for an appropriate auxiliary algebra, citing Amitsur's skew-field construction and the construction using complex matrices of all sizes.
Those suitable-ambient constructions remain the retained interfaces; the counterexample does not refute them.
Degeneracy must likewise be read relative to the chosen ambient evaluation model.

### 3. Free fields and the retained localization interface

Definitions IV.2.1–IV.2.4 use the following distinctions.
An `A`-field is a skew field `K` equipped with a ring map `φ_K:A→K`.
It is epic when no proper subfield of `K` contains `φ_K(A)`.
It is a field of fractions when, in addition, `φ_K` is injective.
An ordinary `A`-homomorphism `K→L` between fields is injective, and its image is a subfield containing `φ_L(A)`.
If `L` is epic, that image is all of `L`, so such a homomorphism is an isomorphism.
This explains why specializations, rather than only everywhere-defined field homomorphisms, enter the universal property.

A subhomomorphism has domain an `A`-subring `K_f⊂K`, maps to `L`, and satisfies

\[
x\in K_f\setminus\ker f\quad\Longrightarrow\quad x^{-1}\in K_f.
\]

Every unit of `K_f` maps to a nonzero element of the field `L`, while the displayed condition makes every element outside `ker f` a unit.
Therefore the nonunits are exactly the ideal `ker f`; this is the unique maximal ideal and `K_f` is local.
Every nonzero element of `K_f/ker f` is invertible, so the quotient is a skew field isomorphic to `im f`.
If `L` is epic, `im f` contains `φ_L(A)` and hence equals `L`.

The source defines equivalent subhomomorphisms using a common restriction that is again a subhomomorphism, defines a specialization as such an equivalence class, and calls the intersection of its representatives the minimal subhomomorphism.
The facts that this gives the required equivalence relation, minimal representative and category are retained from Cohn's specialization framework; they are not proved in the assigned source pages.
These are primary-statement-checked at Cohn pp. 420–421, including the asserted minimal intersection and the displayed composition-domain argument.
A universal epic `A`-field is initial for these specializations, and is the universal field of fractions when the structure map is injective.
Once that category and universal property are supplied, uniqueness up to isomorphism follows from the usual initial-object argument: the unique maps in both directions have identity composites.

The scalar-localization paragraph on p. 54 has a literal substitution error.
For a multiplicative set `S`, localization makes the elements of `φ(S)` invertible, not every element of `φ(A)`.
The latter wording would in particular demand an inverse for `0` in a nonzero localization.
The subsequent matrix-localization interface is the standard one: for a set `Σ` of square matrices over `A`, the map `A→A_Σ` inverts every matrix in `Σ` and is universal among ring maps with that property.

Theorem IV.2.5 retains the equivalence, for a nonzero ring `A` and the set `Σ` of its full square matrices, of:

1. `A` being a Sylvester domain;
2. `Σ` being lower multiplicative, in Cohn's stated sense;
3. `A_Σ` being a skew field, necessarily the universal field of fractions;
4. the existence of an inner-rank-preserving homomorphism from `A` to its universal field of fractions.

The source cites Dicks–Sontag [DS78] and Cohn [Coh06b, Theorem 7.5.13], and points to the paragraph preceding Cohn's Proposition 7.1.1 for “lower multiplicative.”
The primary book, printed p. 450 / PDF p. 474, confirms that Yin20's four clauses are precisely clauses (a), (b), (e) and (f) of Theorem 7.5.13.
The book's definition on pp. 411–412 requires `1∈Σ` and closure under the block matrices `[[A,0],[C,B]]` for `A,B∈Σ` and every compatible `C`.
This audit retains the theorem with its nonzero-ring and full-matrix hypotheses; the primary theorem's proof was read, but its invoked localization and matrix-ideal results are not recursively reproved here.
Chapter III, particularly Example III.2.4 and its preceding discussion, supplies that the free algebra `P` is a Sylvester domain.
That chapter is audited in the separate Yin20-U002 unit.
Combining those inputs gives an injective map

\[
P\hookrightarrow F=\mathbb C(\!\langle x_1,\ldots,x_d\rangle\!),
\qquad
\rho_P(Q)=\rho_F(Q)
\]

for every polynomial matrix `Q`.
In particular, a full square polynomial matrix is invertible over `F`, and invertibility over `F` implies fullness over `P`.
These are algebraic statements about matrices over a skew field.
They assert neither boundedness nor a positive spectral gap after an operator evaluation.

### 4. Algebraic representations and formal representations

Definition IV.3.1 represents a rational function `r∈F` by a triple `(u,A,v)` with

\[
A\in M_n(P)\text{ full},\qquad
u\in M_{1,n}(\mathbb C),\qquad
v\in M_{n,1}(\mathbb C),\qquad
r=uA^{-1}v\text{ in }F.
\]

It is a linear representation when `A` is affine linear in the variables, in the sense of Definition III.3.2.
The source's missing letter `v` before the column-vector space on p. 55 is only a typographical omission.
Theorem IV.3.2 states existence for every rational function, citing Cohn–Reutenauer [CR99] and Cohn [Coh06b].
The source explicitly omits a detailed proof and instead turns to formal representations.
An independent reconstruction of the existence conclusion is given after checking those algorithms below.

Definition IV.3.3 applies to a syntactic rational expression `r` and requires a single scalar-row/linear-pencil/scalar-column triple satisfying, for **every** unital complex algebra `B`,

\[
\operatorname{dom}_B(r)
\subseteq
\{X\in B^d:A(X)\in M_n(B)^\times\},
\qquad
r(X)=uA(X)^{-1}v
\quad(X\in\operatorname{dom}_B(r)).
\]

Where the source says that the matrix is “invertible in `B`,” the well-typed meaning is invertibility in `M_n(B)`.
Fullness is not required in this formal definition, because degenerate expressions are permitted.
The definition only asserts an inclusion of domains; the pencil may be invertible at further tuples where the original expression is not defined.
It asserts the value identity on the original expression domain.
It does not supply a formula for identifying all admissible evaluations of the rational-function equivalence class.
That is part of the subsequent IV.4 discussion.

### 5. Algorithm IV.3.4: complete block verification and the inverse correction

All calculations below take place over an arbitrary unital complex algebra `B`.
No commutation between its elements is used.
At the relevant tuple, write `r_i=u_iA_i^{-1}v_i` and let `n_i` be the size of `A_i`.

**Scalars and variables, rule (i).**
For `a` equal to a scalar or a variable value, the source uses

\[
u=(0,1),\qquad
A=\begin{pmatrix}-a&1\\1&0\end{pmatrix},\qquad
v=\binom01.
\]

Both products with

\[
A^{-1}=\begin{pmatrix}0&1\\1&a\end{pmatrix}
\]

are the identity, and `uA⁻¹v=a`.
This matrix is invertible for every `a∈B`, as the expression-domain requirement demands.

**Addition, first part of rule (ii).**
Use row `(u₁,u₂)`, matrix `diag(A₁,A₂)` and column `(v₁,v₂)ᵀ`.
On the intersection of the two expression domains, its inverse is `diag(A₁⁻¹,A₂⁻¹)`, and the compression is `r₁+r₂`.

**Multiplication, second part of rule (ii).**
The source's less usual block ordering is valid:

\[
u=(0,u_1),\qquad
B=\begin{pmatrix}-v_1u_2&A_1\\A_2&0\end{pmatrix},\qquad
v=\binom0{v_2}.
\]

The row block sizes of `B` are `(n₁,n₂)` and its column block sizes are `(n₂,n₁)`.
Accordingly, the zero block in the outer row has length `n₂`, and the zero block in the outer column has length `n₁`.
On the common expression domain, direct multiplication on both sides verifies

\[
B^{-1}=
\begin{pmatrix}
0&A_2^{-1}\\
A_1^{-1}&A_1^{-1}v_1u_2A_2^{-1}
\end{pmatrix}.
\]

The inverse has row block sizes `(n₂,n₁)` and column block sizes `(n₁,n₂)`.
The resulting scalar compression is

\[
uB^{-1}v=u_1A_1^{-1}v_1u_2A_2^{-1}v_2=r_1r_2.
\]

Thus no sign or size repair is needed for the product rule.
Its matrix differs by a constant block-column permutation from the usual triangular product pencil.

**Inversion, rule (iii): literal failure and repair.**
The printed rule uses the first-coordinate selectors and the matrix

\[
B_{\mathrm{printed}}=\begin{pmatrix}0&u\\v&A\end{pmatrix}.
\]

When `A` and `r=uA⁻¹v` are invertible, the Schur complement of `A` is `−r`.
Consequently,

\[
e_1^\mathsf TB_{\mathrm{printed}}^{-1}e_1=-r^{-1},
\]

which is inconsistent with the positive convention in Definitions IV.3.1 and IV.3.3.
Already the formal representation `(1,[1],1)` of `r=1` gives the scalar matrix `[[0,1],[1,1]]`, whose inverse has top-left entry `−1`.
The source notes that its representation convention changes a sign from [HMS18]; this audit establishes the internal discrepancy in Yin20 and does not attribute the same error to HMS18.

One valid correction retains the outer selectors and uses

\[
B=\begin{pmatrix}0&-u\\v&A\end{pmatrix}.
\]

When `X∈dom_B(r⁻¹)`, the induction hypothesis makes `A(X)` invertible and the expression definition makes `r(X)` invertible.
Suppressing `X`, the explicit two-sided inverse is

\[
B^{-1}=
\begin{pmatrix}
r^{-1}&r^{-1}uA^{-1}\\
-A^{-1}vr^{-1}&A^{-1}-A^{-1}vr^{-1}uA^{-1}
\end{pmatrix}.
\]

For example, its upper-left product with `B` is `uA⁻¹vr⁻¹=1`, its lower-left product is `vr⁻¹−vr⁻¹=0`, and the remaining two entries reduce using `uA⁻¹v=r`.
Multiplication in the other order gives the identity by the same substitutions without reordering any factor.
The compression is now exactly `r⁻¹`.
Equivalently, one may keep the printed matrix and negate exactly one of the two outer selectors.

The repaired rules preserve affine linearity: the new off-diagonal products `v₁u₂`, as well as `u` and `v`, are scalar matrices.
Induction over an acyclic expression circuit therefore proves existence of a formal linear representation for every rational expression, including the exact ambient-algebra domain inclusion in Definition IV.3.3.
The source citation to [HMS18, Section 5] and [Mai17, Chapter III] is retained as the historical algorithm interface; the corrected block argument above supplies the proof used in this audit.

### 6. Fullness, existence, and the limits of the representation results

There are two direct routes from a formal representation to fullness, each with a specified admissibility hypothesis.
First, suppose the expression is evaluable at the canonical generators in the free field `F`.
The formal-domain property applied with ambient algebra `F` implies that its polynomial pencil is invertible over `F`.
The rank-preserving free-field interface from §3 then implies that the pencil is full over `P`.
Second, suppose the expression has a defined evaluation at a tuple of complex `m×m` matrices for some positive integer `m`.
If its size-`n` pencil factored over `P` through inner size `k<n`, evaluating that factorization would bound the ordinary complex rank of its `nm×nm` evaluation by `km<nm`.
This contradicts the invertibility required by the formal-domain property.
Hence the pencil is full in this case as well.

These arguments justify the p. 56 fullness assertion for free-field-admissible expressions or expressions nondegenerate in the all-finite-matrix evaluation model.
Nonempty domain in an arbitrary unital algebra alone is insufficient: such an algebra may allow invertible square matrices to factor through a smaller free module.
One must therefore not combine the arbitrary-ambient definition of degeneracy on p. 52 with the p. 56 sentence to infer fullness without an appropriate ambient rank condition.
For a concrete instance, let `S₁,S₂` be isometries on `ℓ²(ℕ)` with orthogonal ranges summing to the whole space, and put

\[
e=y_1(x_1y_1)^{-1}x_1+y_2(x_2y_2)^{-1}x_2-2.
\]

One can take `S₁e_n=e_{2n}` and `S₂e_n=e_{2n+1}` for the basis indexed by `n≥0`.
The expression `e` is evaluable at the free-field generators and equals `0` there.
At `x_i=S_i^*`, `y_i=S_i`, however, both `x_i y_i=1` and `e=S₁S₁*+S₂S₂*−2=−1`.
Thus `e⁻¹` has a nonempty `B(ℓ²(ℕ))`-domain.
In the corrected algorithm, the pencil for `e` is invertible over `F`, whereas the inverse-rule pencil for `e⁻¹` has Schur complement `e=0` over `F` and is therefore nonfull.
At the displayed operator tuple that latter pencil is nevertheless invertible by the domain-preserving algorithm.
This verifies the exact arbitrary-ambient failure; it makes no assertion of such a phenomenon in a finite von Neumann algebra.
The source's separate statement that pencils of degenerate expressions *may* fail to be full is unobjectionable.
For an expression with domain empty in every ambient algebra, the formal-domain condition is vacuous, so it cannot force fullness.

To reconstruct Theorem IV.3.2 without assuming an unproved operator-evaluation theorem, use that the universal field of fractions is an epic `P`-field.
The elements obtained from `P` by finite sums, products and inverses of nonzero elements form a subfield containing `P`, and therefore exhaust `F`.
Thus every `r∈F` has an expression that is evaluable at the canonical free-field generators.
Apply the corrected formal-representation algorithm to that expression.
The resulting affine-linear pencil is invertible over `F`, hence full by rank preservation, and its scalar compression equals `r`.
This proves the exact existence conclusion of Theorem IV.3.2 from the retained universal-field interface and the elementary block identities.

None of Definitions IV.3.1–IV.3.3, Theorem IV.3.2 or Algorithm IV.3.4 establishes minimality.
The algorithm can increase dimension at every operation and does not assert a monic normalization at an evaluation point, reachability, observability, or a minimal realization.
Fullness means maximal inner rank over the free algebra; it is not a synonym for minimal representation size.
No statement in these pages says that a bounded scalar compression forces a bounded inverse for its pencil, or that another realization with a bounded inverse must exist.

Precisely, the formal algorithm gives the valid implication

\[
X\in\operatorname{dom}_M(r)
\ \Longrightarrow\ A(X)^{-1}\in M_n(M).
\]

Applied with the larger ambient algebra, it instead gives

\[
X\in\operatorname{dom}_{\mathcal U(M)}(r)
\ \Longrightarrow\ A(X)^{-1}\in M_n(\mathcal U(M)).
\]

Adding `r(X)∈M` to the second implication does not change the ambient algebra in the conclusion.
Such a change would be an additional theorem, absent from this unit.
The elementary block form

\[
\begin{pmatrix}h&-Y\\0&h\end{pmatrix}^{-1}
=\begin{pmatrix}h^{-1}&h^{-1}Yh^{-1}\\0&h^{-1}\end{pmatrix}
\]

also makes clear how an affiliated inverse can have a bounded off-diagonal entry while its diagonal entries are unbounded.
This audit uses that block identity only to explain the distinction, not to import any old counterexample status as a substitute for the present source reading.
The opening of IV.4 on p. 56 explicitly warns that evaluating rational functions in arbitrary algebras requires further work, consistent with these limits.

### 7. External dependencies and exact retention

| Source interface named by Yin20 | What this unit retains | What is not claimed here |
| --- | --- | --- |
| Amitsur, *Rational identities and applications to algebra and geometry*, J. Algebra 3 (1966), 304–359 [Ami66] | Construction using a suitable auxiliary skew field, as invoked on p. 52 | Full proof of rational-identity construction or arbitrary-algebra overlap equivalence |
| Kaliuzhnyi–Verbovetskyi–Vinnikov, *Non-commutative rational functions, their difference-differential calculus and realizations*, Multidimens. Syst. Signal Process. 23 (2012), 49–77 [KV12] | The all-finite-matrix evaluation construction cited on p. 52 | An unrestricted bounded-operator evaluation theorem |
| Cohn, *Free ideal rings and localization in general rings* (2006), §7.2 and Chapter 7 [Coh06b], repository key `Coh06` | Primary-checked specialization definitions, Lemma 7.2.3 and universal-field property, pp. 419–421; universal-localization construction, p. 422 | A recursive proof of all specialization and localization foundations |
| Dicks–Sontag, *Sylvester domains*, J. Pure Appl. Algebra 13 (1978), 243–275 [DS78]; Cohn Theorem 7.5.13 | The four Yin20 clauses match primary Cohn clauses (a), (b), (e), (f), p. 450; lower-multiplicative definition checked on pp. 411–412 | Any analytic or norm-preserving interpretation of inner-rank preservation; a fresh DS78 audit |
| Cohn–Reutenauer, *On the construction of the free field*, Int. J. Algebra Comput. 9 (1999), 307–324 [CR99] | Algebraic linear-representation existence | Minimality or a bounded realization at a given operator tuple |
| Helton–Mai–Speicher, *Applications of realizations (aka linearizations) to free probability*, J. Funct. Anal. 274 (2018), 1–79, §5 [HMS18] | Formal-representation definitions and recursive construction as attributed by Yin20 | Attribution of Yin20's inverse-sign error to the primary paper |
| Mai, *On the analytic theory of non-commutative distributions in free probability* (2017), Chapter III [Mai17] | Source attribution for the formal-representation proof and fullness connection | An unqualified arbitrary-ambient nondegeneracy-to-fullness assertion |
| Yin20 Chapter III, especially Example III.2.4 and Definition III.3.2 | Free algebra is Sylvester; “linear” means affine-linear pencil | Replacement of the separate complete Chapter III audit |

The historical polynomial-linearization and realization references mentioned in the p. 55 survey are not independent premises of the reconstructed block proof.
Hrubeš–Wigderson [HW15] supplies the cited arithmetic-circuit viewpoint rather than a missing analytic boundedness conclusion.
The retained external theorems are explicit dependencies, not silently promoted to locally reproved results.
For the bounded Cohn check, the academic-hosted published PDF has 596 pages and.
Printed pp. 411–412, 419–422 and 450 / PDF pp. 435–436, 443–446 and 474 were read on 2026-09-10; printed pp. 420 and 450 were also rendered and inspected.
The inspection confirmed the theorem's exact statement, its displayed proof and imported dependencies, and the relevant specialization definitions; it did not recursively audit the entire Cohn book.
The Amitsur and KV12 construction claims remain source-statement interfaces reported by Yin20, without a fresh primary proof audit of either paper in this unit.

### 8. Corrections, usable outcome and review record

Four qualifications are necessary for literal reuse of the source pages:

1. Require acyclic arithmetic circuits in Definition IV.1.1.
2. Do not treat the overlap rule as an equivalence relation for every unital algebra; use the appropriate skew-field or all-matrix construction.
3. Replace `φ(A)` by `φ(S)` in the scalar-localization sentence on p. 54.
4. Correct the inverse sign in Algorithm IV.3.4(iii), and specify the ambient nondegeneracy hypothesis when deducing fullness.

With these repairs and the stated external inputs, the complete algebraic representation construction is justified.
It preserves the domain of a specified rational expression in the same ambient algebra and yields full affine-linear representations for free-field rational functions.
It supplies no passage from a bounded affiliated rational value to a bounded inverse of a representing matrix, and therefore does not by itself remove the outstanding small-core forward-domain issue.

Author disclosure: the rational-expression agent had previously investigated that forward-domain issue and the repository's bounded-compression examples.
For this unit, the assigned Yin20 pages were read freshly and the block constructions were recomputed without relying on an earlier MSY23 audit verdict.
The coordinating reviewer independently supplied the arbitrary-algebra nontransitivity and Cuntz-isometry nonfullness examples, and this author checked every domain, value and Schur-complement step in them.
The coordinating reviewer and another reviewer independently noticed the inverse-sign issue; the rendered source and explicit block inverse were used to resolve it here.
Independent review of this complete artifact is pending and must identify the exact mathematical content and source edition reviewed before this unit is marked fully reviewed.

### 9. Independent complete-unit review

Date: 2026-09-10; reviewer: the coordinating reviewer, independent review of the author's full written reconstruction.
The reviewer read all assigned Yin20 pages in extracted text and the entire reconstruction, then separately read the final Cohn-interface and Cuntz-example additions.
The author owns the recorded rendered-page and fresh Cohn-primary inspections; this review checked their exact mathematical interfaces without claiming another whole-book audit.
The reviewer's preliminary contributions to the nontransitivity and Cuntz examples are disclosed in Section 8, so this is not a claim of independent rediscovery of those examples.

The directed-acyclic repair suffices because a finite acyclic graph has a sink reachable from each vertex; uniqueness of the sink supplies a well-defined final expression.
The three overlap domains in Section 2 were checked separately, including the invertibility implication for y and the shift substitution witnessing failure of transitivity.
The local-ring argument uses the exact inverse condition outside the kernel and unital maps to nonzero fields, so its maximal-ideal and epic-surjectivity conclusions follow.
The full-matrix localization and rank-preserving field embedding are retained as the primary-checked Cohn foundation with the stated hypotheses; the local construction does not assume bounded evaluation or an analytic rank theorem.

For each algorithm block, the reviewer multiplied the displayed inverse in both orders with the displayed block sizes.
In the inverse rule, replacing the upper-right row by minus u gives Schur complement r and the stated two-sided inverse; the printed positive row gives minus r and is therefore wrong for the positive representation convention.
The corrected recursion preserves affine linearity and an existing expression domain in every ambient algebra.
Epic division-generation then supplies a finite expression for each free-field element; evaluating that recursion in the free field proves full linear representation existence without a dependency on the later evaluation-consistency theorem.

The Cuntz construction uses orthogonal even/odd ranges summing to the whole Hilbert space.
Its e equals zero formally but minus the identity at the operator tuple, so the inverse expression is ambient-nondegenerate although its inverse-rule pencil has zero Schur complement in the free field.
This establishes the exact arbitrary-ambient qualification and does not challenge finite-matrix or skew-field constructions.
The ambient-domain conclusions in Section 6 consequently have no missing boundedness upgrade or minimality assumption.

No unresolved mathematical correction remains in the unit under its stated retained inputs.
The verdict is independently reviewed within the assigned chapter scope.
Original proofs of the contextual Amitsur/KV12 constructions, a recursive Cohn-book audit, formal verification and external human review were not performed.

## Source and inspection

Source edition: Yin20, the supplied 109-page doctoral dissertation with title-page year 2019; its defense date 2020-01-27 and public repository metadata are separate facts. Printed Arabic page = PDF page minus 10. Other source editions retain their separate exact locators.

Source passages: Chapter IV introduction and Sections IV.1-IV.3, printed pp. 49-56 / PDF pp. 59-66, including the transition to IV.4 and representation rules.

Inspection: 2026-09-10: complete local reconstruction of expressions, the free-field interface and corrected recursive representations, followed by the appended independent artifact review. Selected Cohn primary theorem and proof interfaces were read with their earlier dependencies retained; arbitrary-ambient domain qualifications and reviewer contributions are disclosed. Contextual Amitsur/KV12 originals, the whole Cohn book, formal verification and external human review were not audited.

## Additional retained definition source recheck

<a id="yin20-definition-recheck"></a>

The following original 2026-09-10 selected-source reading was retained from L_F0098 at 2026-10-21T01:58.
It retains the exact source-definition/convention content, already sufficient linked U homes, actual primary and visual locators, original reader roles and unreviewed-proof limits.
The earlier unit proof review does not retrospectively cover this later definition-reading event.
References to unchanged files and a sidecar describe the original checkpoint; this maintenance performs no source reopening, new proof review or stronger historical attribution.

- Date and reviewer: 2026-09-10, the free-field algebra agent.
- Source: [Yin20.pdf](../../../literature/pdf/Yin20.pdf), the 109-page local dissertation.
  For the chapters used here, PDF page = printed page + 10.
- Existing units: [U001, division closure](Yin_U001.md#yin20-u001), [U002, Chapter III](Yin_U002.md#yin20-u002), [U003, IV.1–IV.3](#yin20-u003), and [U004, IV.4–IV.5](Yin_U004.md#yin20-u004).
  Exact old definition locations are linked below.
- Scope: source-definition and notation recheck, not a new U unit or project Claim.
  Existing definition sections and their correction boundaries were reread.
  The primary passages at the locators in the table were checked in extracted text; PDF pp. 60, 63, 65 and 70 were also rendered and visually inspected.
  No new complete proof audit of Chapters III–IV is claimed.
- Prior role disclosure: this reviewer authored the existing Chapter III unit and contributed to earlier algebraic interfaces.
  That history is not independent review of the present sidecar.
  All existing units and the source PDF remain unchanged.

## General Definition Homes and Primary Locators

| Entry | Exact existing location | Printed / PDF locator and current check |
| --- | --- | --- |
| Inner rank, rank factorization and fullness | [U002, III.1](Yin_U002.md#iii1-elementary-rank-and-the-schur-argument); general alternate [MSY23-U001 home](../MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definitions III.1.1–III.1.2, 38 / 48. The base algebra is specified. Fullness means maximal inner rank for the matrix dimensions, not bounded invertibility after evaluation. |
| Stable finiteness | [U002, stable finiteness](Yin_U002.md#example-iii14-and-stable-finiteness) | Definition III.1.5, 39 / 49. One-sided inverses are two-sided at every matrix size. |
| Sylvester domain | [U002, defining axiom](Yin_U002.md#the-defining-axiom-and-the-general-rank-inequality) | Definition III.2.1, 41 / 51: the nonzero ring's zero-product rank inequality. The equivalent general rank inequality and the later universal-field interface are results, not additional definitions requiring new project Claims. |
| Hollow and affine linear matrices | [U002, III.3](Yin_U002.md#iii3-linear-matrices-and-the-exact-degree-input); complete concise definitions at [MSY23-U001](../MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition III.3.1, 44 / 54; Definition III.3.2, 45 / 55. Hollow means a sufficiently large zero submatrix; “linear” allows a constant coefficient. |
| Central eigenvalue relative to \(\mathbb C\) | [U002, III.4](Yin_U002.md#iii4-central-eigenvalues-and-scope-corrections) | Definition III.4.1, 46 / 56. The scalar \(\lambda\in\mathbb C\) makes \(P-\lambda I\) nonfull over the stated algebra. |
| Rational expression; recursive evaluation domain | [U003, syntax and domains](#2-rational-syntax-and-evaluation-domains) | Definitions IV.1.1–IV.1.2, 50–51 / 60–61. Finite arithmetic syntax, including ordered multiplication and inversion, is distinguished from its evaluated value. Retain the acyclicity repair described below. |
| \(A\)-field, epic \(A\)-field, field of fractions | [U003, free fields](#3-free-fields-and-the-retained-localization-interface) | Definition IV.2.1, 52 / 62. A field carries a structure map from \(A\); epic means division-generation by its image, and a field of fractions additionally has injective structure map. |
| Subhomomorphism, specialization and universal field of fractions | [Same U003 section](#3-free-fields-and-the-retained-localization-interface) | Definitions IV.2.2–IV.2.4, 53 / 63. Universality concerns specializations of epic \(A\)-fields. The required category and equivalence facts are retained external inputs at that home. |
| Universal matrix localization and the free field | [Same U003 section](#3-free-fields-and-the-retained-localization-interface) | Discussion and Theorem IV.2.5, 54 / 64. The free field is the universal field of fractions of the free algebra. Rank preservation and full-matrix inversion are accepted structural results. |
| Algebraic representation; linear representation | [U003, algebraic and formal representations](#4-algebraic-representations-and-formal-representations) | Definition IV.3.1, 54–55 / 64–65. \(r=uA^{-1}v\), with \(A\) a full polynomial matrix and constant row and column; a linear representation additionally makes \(A\) affine linear. |
| Formal linear representation of an expression | [Same U003 section](#4-algebraic-representations-and-formal-representations) | Definition IV.3.3, 55 / 65. An affine pencil reproduces the expression on its original domain in every unital complex algebra. The definition promises domain inclusion, not equality, and need not impose fullness. |
| Representation and rational-function domains | [U004, representation domain](Yin_U004.md#32-definition-of-the-representation-domain) | Definition IV.4.2, 57 / 67, following Theorem IV.4.1. The function domain is a union over all full polynomial representations; consistency uses the preceding stably finite ambient hypothesis. |
| Rational closure of a tuple's polynomial evaluation algebra | [U004, rational closure](Yin_U004.md#4-rational-closure-is-an-algebra-in-every-unital-ambient) | Definition IV.5.1, 58 / 68. This is the general matrix rational-closure construction with the subalgebra chosen to be \(\mathbb C\langle X\rangle\). The general index home is [MSY23-U003](../MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra), not a second tuple-specific definition. |
| General division closure and its finite recursion | [U004, Definition IV.5.5 and Remark IV.5.6](Yin_U004.md#61-definition-iv55-and-all-parts-of-remark-iv56); earlier [U001](Yin_U001.md#yin20-u001) | 60 / 70. Scalar inverses are taken only when the element is a unit of the fixed ambient algebra. The recursive construction is a known characterization of this general closure. |

<a id="yin20-domain-and-representation-conventions"></a>
## Domain and Representation Conventions

The precise [existing syntax home](#2-rational-syntax-and-evaluation-domains) gives the recursive evaluation domain in a general unital complex algebra \(B\).
Every intermediate inverse must exist in \(B\).
An expression that evaluates in \(\mathcal U(M)\) and happens to have a bounded final value is not thereby an expression evaluable in \(M\).

Three constructions stay distinct:

1. A **syntactic expression** has the recursively determined domain just described, possibly empty.
2. A **formal linear representation of that expression** has a pencil domain containing the expression domain and agrees there, for every unital complex ambient algebra.
3. A **representation of a free-field element** uses a full matrix and gives one part of the union defining that element's domain in a chosen evaluation algebra.

Definition IV.4.2 takes the union over full polynomial representations.
MSY23 Definition 4.5 uses affine linear representations.
The sources' linearization results connect these classes with their domain hypotheses; no equivalence is silently inserted into either definition.
Neither formulation includes a minimality assumption or an invertible constant term.

Scalar zero being in a representation domain is an additional regularity condition.
A normalized pencil \(I-\sum A_jx_j\), an individual representation size, or a particular tuple is retained at its consumer, not registered as a new free-field definition.

<a id="yin20-retained-definition-corrections"></a>
## Retained Corrections and Accepted Inputs

The fresh checks confirm the following already documented boundaries.
They are not newly discovered project results and do not change the original assessments.

- Definition IV.1.1's literal finite-graph description omits acyclicity.
  The audited definition uses a finite directed acyclic arithmetic circuit, as needed for recursive evaluation.
- The arbitrary-algebra overlap relation on expressions discussed on p. 52 is not automatically transitive.
  It is not used as a general construction of the free field; U003 retains the appropriate auxiliary evaluation models and the separate universal-field framework.
- The scalar-localization passage on p. 54 should invert the image of the selected multiplicative set \(S\), rather than every element of \(A\).
  U003 records that correction before stating the matrix-localization interface.
- Matrix inverses in Definition IV.3.3 belong to \(M_N(B)\).
  The phrase “invertible in \(B\)” is read with this type correction.
- Inner rank computed over \(\mathbb C\) agrees with ordinary scalar rank.
  Preservation after embedding into an arbitrary algebra is a different assertion; the scalar-matrix and central-eigenvalue prose is read with the stable-finiteness corrections already recorded in U002.
  The chosen scalars \(\mathbb C\) are not asserted to be the entire center of every free algebra.

The free-algebra Sylvester property, specialization framework, and Theorem IV.2.5 are used at the [existing external-input boundary](#7-external-dependencies-and-exact-retention).
Their known equivalence and well-definedness consequences do not require project C identifiers or fresh foundational proofs just to use these definitions.
This recheck did not reopen those Cohn inputs or strengthen their reading status.

The old source-proof repairs in Algorithms IV.3.4 and the IV.4–IV.5 arguments remain visible in U003/U004.
This note does not replace those proof reviews with definition checking.

## Citation and Index Disposition

Candidate labels are **current formulation**, **notation**, and **exposition**, using the exact chapter numbers and printed/PDF pages above.
No first-introduction claim is made.
An alternative definition home is a navigation choice, not an instruction to duplicate it.

In particular, \(\operatorname{Div}_M(\mathbb C\langle X\rangle)\), \(\operatorname{Div}_{\mathcal U(M)}(\mathbb C\langle X\rangle)\), and the corresponding matrix rational closures are instances of the general operations.
Their difference is mathematically consequential, but it creates no new general definition.
Same-ambient Schur calculations and inverse-closure equivalences do not supply a change of ambient algebra.

Concrete adopted references and use scopes are in the Claim definition-use record, linked from the [concept-group index](../../../definitions/index.md#free-fields-and-representations).
Historical proof versions and their theorem dependencies are preserved.

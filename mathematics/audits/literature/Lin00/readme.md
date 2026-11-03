# Lin00: Complete Preprint Audit

Author: Yin.

Source: Peter A. Linnell, *A Rationality Criterion for Unbounded Operators*, registered as `Lin00`.
The actual proof-inspection artifact is [arXiv:math/9907075v1](../../../literature/pdf/Lin00--arxiv-v1.pdf), dated 1999-07-12, seven pages.
The journal publication is J. Funct. Anal. 171(1) (2000), 115--123.

Audit date: 2026-10-10.
Authorization: the user requested completion of the full article audit after the earlier Lin00 bounded-interface check.
The complete retained preprint, including both language summaries, all definitions, Lemmas 2.1--2.3 and 3.1--3.5, Theorem 1.1, Proposition 1.2 and bibliography, has now been read.
The coordinating agent visually inspected all seven pages.
Separate algebra, domain and interface agents reconstructed and cross-reviewed the arguments at the scopes below.
These are independent internal AI reviews, not external human review or formal verification.

## Outcome

For a **finitely generated free group**, the reconstructed proof supports both of the main results:

- Theorem 1.1: the affiliated division closure is exactly the class passing both cleared finite-rank tests for one, equivalently every, bounded left/right fraction pair.
  Its bounded intersection is the division closure in the reduced group C*-algebra, and rational affiliated elements admit fractions with coefficients in that bounded closure.
- Proposition 1.2: rationality is equivalent to equality of the two unbounded operators on an algebraic finite-codimension restriction, including equality of restriction domains.

Several literal steps in the preprint require the corrections recorded below.
Once repaired, no local implication gap remains in these finite-generator proof chains.
The accepted foundations are finite-tracial affiliated-operator spectral and polar calculus and the previously audited finite-generator DR97 bounded criterion; original proofs of all underlying foundations have not been recursively audited.

**The complete source reading also leaves a genuine scope boundary.**
Lin00 states its results for a free group without a finite-generation restriction.
The available DR97 proof audit only supplies the needed bounded criterion for finitely many free generators.
Its extension to arbitrary rank was not established in this audit.
The local algebraic and domain reductions work at arbitrary rank if that bounded input holds, but the unrestricted theorem is not certified by the present record.
This is a missing verified interface, not a counterexample or a declaration that the source theorem is false.

The journal PDF was not obtained.
The findings are about the retained preprint; they are not automatically findings about the typeset journal version.
No author-endorsed erratum is claimed.

<a id="f0001-common-denominator-comparison"></a>
### Common-denominator source comparison, 2026-10-12

At the user's request, the authoring AI agent reread and visually inspected the retained preprint's p.2.
Its Introduction explicitly states that every finite subset of U(G) has a common denominator, with a two-element left-fraction example.
This paragraph does not give a row/column functional-calculus proof.
The row/column construction recorded in Lin00-U001 is the local audit's reconstruction, not a displayed proof in Linnell's paper.
[Miy22 Lemma 4.1](../Miy22/readme.md#f0001-common-denominator-comparison) supplies an explicit two-element algebraic proof, extendable to finite families by induction.
Search scope: the adequate retained Lin00 and Miy22 artifacts, their existing source units, text searches for denominator/common/fraction and direct page inspection.
The comparison resolved the question; no journal/preprint equality or new whole-source audit is asserted.

## Coverage and responsible units

All locators in the table refer to the seven-page preprint, where printed and PDF page numbers coincide.

| Unit | Content and source locators | Assessment |
| --- | --- | --- |

## Findings and repairs

| Finding | Source passage and consequence | Resolution |
| --- | --- | --- |
| Scalar-summand nonadditivity | The p. 2 lift sends each operator to its edge amplification plus the identity on a scalar summand. It is multiplicative but not additive, so Lemma 3.2's displayed equalities are not exact. | U002 supplies the rank-one correction terms and the scalar-multiplication closure needed before applying scalar shifts. All required finite-rank conclusions survive. |
| Multiplication sign | The telescoping display in Lemma 3.3, p. 6, subtracts two defects instead of adding them. | The corrected plus sign gives exactly the defect for the product; U002 checks the compatible left and right fractions. |
| Unbounded element in the wrong algebra | Lemma 2.3, p. 5, calls $u-\lambda$ a nonzero divisor in $W(G)$ although $u$ may be unbounded. | U002 proves invertibility in $U(G)$ through kernel projections, the finite-trace bound and polar decomposition; it also states the bounded-numerator repair. |
| Infinite amplification domain | The Cartesian-product domain on p. 2 omits square summability of the output coordinates. | U001/U003 give the closed direct-sum domain and a counterexample to the unrestricted coordinatewise reading. This issue disappears for finite amplification. |
| French inverse-defect mismatch | The French synopsis p. 1 writes $sP^{-1}b-tP^{-1}a$; the English definition and proofs use $sP^{-1}b-aP^{-1}t$. | U001 retains the English definition and records the discrepancy. Minor ambient-set and one-point-action wording errors are also identified there. |
| Finite-codimension interpretation | Proposition 1.2 and its complement choices do not establish a closed finite-codimension subspace, or equality merely on an unspecified common core. | U003 supplies the complete proof with algebraic finite codimension and equality of restriction domains. This is a clarification of the valid statement, not a refutation. |
| Generator scope | Lin00 gives no finite-generation restriction, whereas the available DR97 proof uses a finite alphabet. | Finite-generator theorem accepted; arbitrary-rank bounded input remains explicitly unverified. No density or directed-union shortcut is asserted. |

The final regularization is made explicit on both sides in U002:

$$
s=(1+uu^*)^{-1},\quad t=(1+u^*u)^{-1},\quad
a=su=ut,\qquad u=s^{-1}a=at^{-1}.
$$

The functions involved make $a,s,t$ bounded; algebraic closure puts them in the bounded finite-rank class, and DR97 identifies that class with the required bounded rational closure.
This is the decisive step from the bounded theorem to the affiliated theorem.

## Independent review and verification evidence

- The algebra agent authored U002; the domain and interface agents each independently reviewed its entire local proof chain.
  Both checked the exact rank-one signs, both denominator changes, the trace argument, multiplication, inverses/adjoints and regularization.
  The coordinating agent also reviewed the complete unit.
  No local mathematical repair was requested after those checks.
- The domain agent authored U003; the algebra and interface agents independently checked its complete proof, and the coordinating agent reviewed it.
  Both domain inclusions, equality of values, algebraic complement construction and both reverse finite-rank conclusions passed.
  The expression suggesting that the preprint itself was a journal version was corrected to preserve the actual version scope.
- The coordinating agent authored U001.
  The algebra and domain agents independently checked the typed tests, scalar conventions, block formulation, French/English difference and domain quantifier.
  The later common-denominator supplement was separately checked by the algebra agent.
- The interface agent authored U004.
  The coordinating agent checked its dependency distinctions against DR97-U002--U004 and the reconstructed Lin00 chain, and directly verified the retained Lin91 statement pages.
  External original-proof limits and the arbitrary-rank boundary remain visible.

These review facts identify the actual checking relationships; publication in an audit directory does not itself establish independence.

On 2026-10-10, `material.py check` passed for all four new U files.
A scoped check passed all 40 local destinations and anchors in the five Lin00 Markdown files, confirmed unique Lin00/Lin91/Lin93 bibliography keys.
`git diff --check` passed for the new audit directory and the affected bibliography and navigation files.
These are structural and storage checks, separate from mathematical proof review; no whole-repository audit, commit or remote operation was performed.

## Relation to DR97 and Miy22

DR97's **free-group tree model** and Miy22's **semicircular Fock model** have related bounded proofs: finite-rank conditions control coefficient residuals, from which finite-dimensional representations and rational realizations are obtained.
This compares two models, rather than the bounded and unbounded cases of one theorem.

Lin00 provides the free-group extension to affiliated operators through bounded left/right fractions and regularization.
Miy22 carries this strategy into the semicircular setting.
Lin00 Theorem 1.1 retains the two tests and the actual free-group scope.
This audit does not insert a new theorem or change project Claim decisions.

The earlier [Miy26-U008](../Miy26/Yin_U008.md#miy26-u008) records only the Lin00 statement/applicability check actually performed on 2026-09-08.
That fixed evidence remains unchanged.
The present units supply new proof-inspection evidence for the retained v1; they do not retrospectively upgrade the earlier inspection or unrelated source audits.

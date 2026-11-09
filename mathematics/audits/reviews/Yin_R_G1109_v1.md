---
author: Yin
---

# Bounded-entropy homological gap and rotating-shear finite computation

The review act was completed at 2026-11-09T08:48 UTC for Yin.
A separately organized reviewing agent, outside development of the proof and program, inspected the fixed inputs directly, without proof-generation dialogue, exploration discussion or substantive author explanations.
The assignment identified assertions and finite outputs to check; these were treated as targets, not evidence.
The reviewer first read C883's exact statement and complete argument, enumerated its obligations and checked the primary-source interfaces before forming the conclusion, reusing the existing DS17 source inspection at its accepted scope.
The later computation assignment was checked separately through complete code inspection and fresh execution; the final same-site formulation in L462 v5 and J153 was reread after the author fixed it.
Neither finding is a completion review of the unrestricted Lehmer Task.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole topological proof and probability consequence](#whole-topological-gap) | independently reviewed |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole topological proof and probability consequence](#whole-topological-gap) | [C883 statement](../../claims/Yin_C_G0883_v1.md#statement) | Entire quantified conclusion and fixed finite mapping-torus intermediate assertion. |
| [Whole topological proof and probability consequence](#whole-topological-gap) | [C883 external inputs](../../claims/Yin_C_G0883_v1.md#external-inputs) | Exact primary-source statements and applicability; explicit original-proof inspection limits. |
| [Whole topological proof and probability consequence](#whole-topological-gap) | [C883 fixed-torus argument](../../claims/Yin_C_G0883_v1.md#fixed-mapping-torus) | Complete graph reduction, fixed group invariant, nonzero specialization, support bound and whole-measure identity. |
| [Whole topological proof and probability consequence](#whole-topological-gap) | [C883 filling argument](../../claims/Yin_C_G0883_v1.md#filling-punctures) | Complete meridian-kernel argument, including partial filling and one puncture. |
| [Whole topological proof and probability consequence](#whole-topological-gap) | [C883 entropy deduction](../../claims/Yin_C_G0883_v1.md#bounded-normalized-entropy) | Complete finite-source deduction, orientation and genus conditions, reciprocal output and conclusion limits. |
| [Whole topological proof and probability consequence](#whole-topological-gap) | [L462 v5 topological law](../../ledger/Yin_L_G0462_v5.md#topological-law) | Universal probability-zero consequence and necessary normalized-entropy escape. |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | [L462 v5 sampling law](../../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law) | Same-site balanced-sign law, atom probability, integral symplectic output and hypothetical asymptotic criterion. |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | [L462 v5 control](../../ledger/Yin_L_G0462_v5.md#separable-control) | Complete characteristic polynomial, boundary cases, expanding-root count and total measure. |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | [L462 v5 finite test](../../ledger/Yin_L_G0462_v5.md#discriminating-test) | Entire stated finite conclusion, separate from numerical diagnostics and asymptotic speculation. |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | [J153 matrices](../../computations/programs/Yin_J_G0153/readme.md#finite-sample) | Exact seeded parameters, integral construction, overflow bound and symplectic characteristic polynomials. |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | [J153 full measures](../../computations/programs/Yin_J_G0153/readme.md#full-measures) | All multiplicities, interval products, cyclotomic resolution, 24/48 split and minimum. |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | [J153 replay](../../computations/programs/Yin_J_G0153/readme.md#replay) | Fresh execution with documented runtime versions and the responsible local output. |
| [Sampling law, control and 72-case computation](#finite-shear-computation) | [J153 program](../../computations/programs/Yin_J_G0153/rotating_shears.py) | Complete program inspection and execution of all 72 exact characteristic polynomials and full root products. |

<a id="whole-topological-gap"></a>
## Whole topological proof and probability consequence

C883 v1's entire statement and local argument are mathematically supported at the stated accepted-external-input depth.
No unresolved mathematical or source-applicability objection was found.
This covers the whole characteristic polynomial, and gives no positive lower bound for each individual noncyclotomic factor.

The reviewer directly text-read the [FLM11 author edition](../literature/FLM11/readme.md), printed/PDF pages 1--2, and visually checked page 1.
The family uses the Euler characteristic of the original surface, so $P=e^C$ matches the claimed normalized-entropy bound exactly.
Theorem 1.1 makes the mapping-torus homeomorphism types finite after removal of the invariant singularity set.
That set is nonempty for $g\ge2$, since the closed-surface prong-index relation has total excess $4g-4>0$.
Replacing punctures by boundary circles preserves the necessary group and first-homology action; only the resulting finite set of groups is needed, without a uniform boundary parametrization.
The original finiteness proof was not audited.

The reviewer directly read the [DGT23 author edition](../literature/DGT23/readme.md), the graph-map definition on page 4, Sections 4.1--4.3 on page 12, and Corollary 4.10, its short proof and Remark 4.11 on pages 19--20.
The latter pages were visually checked for the inverse variable and rank-dependent factor.
Section 4 permits general finite graph maps and imposes no fully irreducible, train-track or invariant-foliation orientability condition on this corollary.
A boundary surface retracts to a finite graph spine, and its monodromy induces a homotopy equivalence with the same semidirect-product group, primitive dual class and integral first-homology action.
For nontrivial free groups a bouquet representative has nondegenerate edge images; the disk case has characteristic polynomial $1$ and is harmless separately.
Thus no low-rank or graph-map hypothesis is missing.

DGT23's precise formula is
$$
 \det(t^{-1}I-f_*)\doteq(1-t)^p\Delta_\Gamma^u(t),
 \qquad p=\mathbf 1_{\operatorname{rank}H\ge2},
 \qquad H=H_1(\Gamma;\mathbb Z)/\mathrm{torsion}.
$$
The short corollary proof follows from the cellular homology exact sequence and its characteristic-polynomial identity, together with Theorem 4.9.
That interface was checked; the full determinant proof and its earlier lemmas were not independently audited.
The corollary is accepted as an established external result at this explicit depth.

Transport all fibration classes to the same $H$ for a fixed source group.
Group isomorphisms and multiplication by $\pm h$ permute or translate the Alexander support without changing its size.
The characteristic determinant is nonzero, hence every relevant specialization is nonzero and the fixed support size is at least one.
Specialization only merges or cancels monomials, with no degree, coefficient-height or fibered-cone restriction needed.
The torus-integral definition gives $m(P(t^{-1}))=m(P(t))$, and the factors $\pm t^a$ and $1-t$ have measure zero.
This verifies the exact whole-measure identity, including an inverted dual class and both ranks of $H$.

The [DS17 fixed-support statement](../literature/DS17/Yin_U001.md#ds17-u001) applies after a monomial shift, with the monomial branch handled by the recorded direct bound $\log2$.
This finding reuses that accepted external theorem and its recorded source-proof limits, without a fresh audit of DS17 or Smyth's foundational closure/isolation results.
The minimum of the finitely many source constants is positive; an empty bounded-entropy class is vacuous.

The filling map on integral first homology is onto, and its free abelian kernel is generated by meridians modulo the surface relations.
Orientation preservation makes the action on those generators a permutation, so its induced kernel action has finite order.
Its monic integral characteristic polynomial therefore has only roots of unity, and the exact characteristic-polynomial product proves equality of whole measures.
For a closed filled surface the single meridian relation gives dimension $s-1$, including the zero kernel at $s=1$.
Partial filling uses the same finite-order argument without assuming that dimension formula.
The closed monodromy preserves the integral symplectic form, giving the asserted reciprocal polynomial with constant one.
No orientability of the invariant foliations or numerical gap value is assumed.

The strict event in [L462 v5](../../ledger/Yin_L_G0462_v5.md#topological-law) has $0<m(P_f)<\log(1+\varepsilon)$, so it is empty for $0<\varepsilon\le e^{\eta_C}-1$, including the endpoint.
Every probability law on the stated bounded-entropy collection consequently assigns it zero mass.
A sequence of positive measures tending to zero cannot have a bounded normalized-entropy subsequence, proving the asserted escape to infinity for its chosen pseudo-Anosov realizations.
Unbounded-entropy mixtures, separate irreducible factors and the unrestricted Task remain outside this conclusion.

<a id="finite-shear-computation"></a>
## Sampling law, control and 72-case computation

The final sampling law and exact separable control are correct, and the complete J153 replay reproduces the stated finite conclusions.
They are not premises of C883 or of the finding above.
No all-parameter gap, near-one witness, asymptotic sequence or positive probability in every shrinking strict shell follows.

The final law chooses one common $k$-element site set and two independently balanced sign vectors on it.
There are $\binom gk\binom{k}{k/2}^2$ equally likely elementary outcomes, giving the stated atom mass.
The program implements this same-site family; its 72 labelled seeds form a selected sample, not an enumeration of a full finite law.
Positive pair weights in a countable mixture give positive mass to each supplied output through a positive-mass elementary preimage, without asserting existence of a small-measure preimage.
Symmetry of $D,E$ gives the two shear identities against $J$, and $S^tS=I$ gives the rotation identity.
Multiplication yields exactly the block matrix in the program's shear_matrix function, with integral symplectic, monic reciprocal output and constant coefficient one.
Summing the individual positive radial logarithms proves $m(P)\le N_+\log\rho$; the proposed $O(k/g)$ and $o(g/k)$ bounds would suffice if true but are not established.

For the separable control, one circuit of the block shift gives $W$, with determinant one and trace $a=2+de$.
Hence the monic complete polynomial is $\det(t^gI_2-W)=t^{2g}-at^g+1$.
If $|a|\le2$, both quadratic roots and all their $g$-th roots have modulus one, including repeated endpoint cases.
If $|a|>2$, the quadratic root moduli are $r,r^{-1}$, with $\log r=\operatorname{arcosh}(|a|/2)$.
Exactly $g$ roots have modulus $r^{1/g}>1$, proving the house and constant total cost, including the negative-trace branch.

The reviewer read the complete J153 program and successfully ran:

~~~text
uv run --no-project --with sympy --with scipy --with python-flint python -B mathematics/computations/programs/Yin_J_G0153/rotating_shears.py
~~~

The actual runtime versions were Python 3.14.7, NumPy 2.5.4, SymPy 1.14.0 and python-flint 0.9.0.
The seeds and $3\cdot3\cdot8=72$ cases match the README.
Overflow is excluded in this finite range: $|D_{ij}|,|E_{ij}|\le8$, $|(DE)_{ij}|\le48\cdot64=3072$, and $|A_{ij}|\le3073$.
Even the coarse bound on an entry of the symplectic verification is $96\cdot3073^2<10^9$, below the signed 64-bit limit.
Every exact integer symplectic assertion and reciprocal coefficient assertion passed, and FLINT computed all 72 integer characteristic polynomials.

The installed FLINT documentation confirms complete complex roots with multiplicities and outward-rounded exact endpoint bounds from arb.lower and arb.upper.
The root API was also checked against the [python-flint documentation](https://python-flint.readthedocs.io/en/latest/fmpz_poly.html#flint.fmpz_poly.complex_roots).
Clipping both radius endpoints at one encloses $\max(1,|\alpha|)$, including balls meeting the unit circle, and multiplication with multiplicity encloses the full monic polynomial's measure.
Every case passed the total multiplicity $2g$ and final radius threshold $10^{-30}$.
Exact factorization proved all irreducible factors cyclotomic for every case whose interval did not certify strict positivity, resolving each to exactly $M=1$.
The arithmetic libraries are trusted implementations; their internals were not formally verified or independently reimplemented.

The replay produced 24 cyclotomic labelled outputs and 48 certified positive outputs.
The minimum occurs at $(g,k,s)=(12,8,6)$, with
$$
 1.75487766624669<M<1.75487766624670,
$$
and its reproduced coefficient list is exactly the degree-24 polynomial displayed in J153.
The floating-point ordering merely proposes this minimum; the final interval-separation assertion checks it against every other positive output, allowing identical exact polynomials.
The reported house near $1.15096393$ and six numerically expanding roots remain numerical diagnostics.
The strict-shell zero-probability conclusion applies to the uniform law on these 72 labelled inputs, not to an exhaustive law on the unbounded matrix family.

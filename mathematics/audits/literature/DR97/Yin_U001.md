---
author: Yin
---

<a id="dr97-u001"></a>
# DR97-U001: Formal Series and Minimal Representations

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

- Source: [DR97](../../../literature/pdf/DR97.pdf), local published version.
- Locator: Section 2.1, pp. 614-616, Definition 1 and Theorems 2-4; formula (2), p. 621.
- Record: 2026-09-08, the coordinating agent, local reconstruction and self-review for [DR97 rational-series source audit](readme.md#dr97-rational-series-source-audit).
- Kind and coverage: definitions and connected representation results, audited within the finite-alphabet, commutative-field scope specified below.
  The source's more general coefficient-ring statements and semiring discussion receive statement inspection only.

## Setting and notation

Let $A$ be a **finite** alphabet and $k$ a commutative field.
The formal series algebra $k\langle\!\langle A\rangle\!\rangle$ has coefficients indexed by words in $A^*$, with empty word $1$.
Its Cauchy product is

$$
(ST,w)=\sum_{uv=w}(S,u)(T,v).
$$

There are only $|w|+1$ summands.
This is a formal algebra, with coefficientwise convergence over discrete $k$; no operator norm or group cancellation is involved.
The coefficientwise product is denoted $S\odot T$.
Polynomials have finite support.

<a id="scalar-closure-terminology"></a>
DR97's rational closure means the smallest unital subalgebra closed under inverses **that exist in the stated ambient algebra**.
In this formal algebra, $S$ is invertible exactly when its constant coefficient is nonzero.
For a proper series $T$, $T^*=(1-T)^{-1}=\sum_{j\geq0}T^j$ is a well-defined formal sum.
Later papers may call scalar inverse closure the *division closure* and reserve *rational closure* for matrix inverses; the distinction must be translated explicitly.

For polynomials $P,Q$, the source's bimodule convention is

$$
(P\circ S\circ Q,w)=(S,QwP).
$$

In particular $v\circ S$ removes a suffix $v$, whereas $S\circ u$ removes a prefix $u$.
Products inside coefficient pairings are polynomial products extended bilinearly.

## Statements and their precise scope

For finite $A$ over $k$, the following are equivalent (Theorem 2): the suffix residuals of $S$ span a finite-dimensional space; the prefix residuals do so; $S$ has a finite linear representation

$$
(S,w)=\lambda\mu(w)\gamma,
\qquad \mu:A^*\longrightarrow M_n(k)
$$

with $\mu$ a unital monoid homomorphism; and $S$ belongs to the scalar inverse closure of $k\langle A\rangle$ in the formal series algebra.
The source phrases the first two properties as containment in a finitely generated invariant module, which also makes sense over a commutative ring.
Over a field this is equivalent to the finite-dimensional span condition above.

Theorem 3: the Hadamard product of two rational series is rational.
Coefficient conjugation also preserves rationality over $\mathbb C$.

Theorem 4: for a minimal representation of a nonzero series, there are polynomials $P_i,Q_j$ such that

$$
\mu(w)_{ij}=(S,P_iwQ_j)
             =(Q_j\circ S\circ P_i,w).
$$

Thus every matrix coefficient series is a finite linear combination of two-sided word residuals of $S$.
The zero series can be handled separately or by the zero-dimensional representation; later arguments need no nonzero-state assumption for it.

## Local reconstruction

**Residuals and states.**
Prefix residuals act by appending a letter to the removed prefix.
A finite-dimensional invariant span therefore supplies transition matrices, an initial state for $S$, and evaluation at the empty word as output.
Conversely, in a representation, the residual $S\circ u$ has coefficients $\lambda\mu(u)\mu(w)\gamma$, so the residual space has dimension at most $n$.
The suffix version follows by using column states, or by reversing words.

**Representations give scalar rational expressions.**
Put $M=\sum_{x\in A}\mu(x)x$, a finite matrix of degree-one polynomials.
Then

$$
S=\lambda(I-M)^{-1}\gamma
  =\lambda\left(\sum_{j\geq0}M^j\right)\gamma.
$$

Coefficientwise summation is valid because $M$ has no constant term.
The entries of $(I-M)^{-1}$ are scalar rational: recursively eliminate states using Schur complements.
Every pivot at this formal stage has constant term $1$, so the inverses required by elimination exist.
This explains why using a matrix realization does not enlarge the formal scalar inverse closure.

**Scalar rational expressions give finite residual spaces.**
Finite-dimensional spaces for polynomials and sums are immediate.
Let $L_x S=S\circ x$ and write $s_0=(S,1)$.
Then

$$
L_x(ST)=(L_xS)T+s_0L_xT.
$$

For rational-recognizable $S,T$, the span of $UT$ for $U$ in the prefix-residual space of $S$, together with the prefix-residual space of $T$, is finite-dimensional and invariant.
For invertible $S$, let $R=S^{-1}$.
Differentiating $SR=1$ by this residual identity gives

$$
L_xR=-s_0^{-1}(L_xS)R.
$$

The span of $R$ and $UR$, where $U$ runs over the residual space of $S$, is invariant under all $L_x$.
This proves closure under every permitted scalar inverse without assuming the desired rationality criterion.
Word reversal supplies the suffix criterion.

**Hadamard products.**
Tensoring two representations gives

$$
\lambda=\lambda_1\otimes\lambda_2,\quad
\mu(x)=\mu_1(x)\otimes\mu_2(x),\quad
\gamma=\gamma_1\otimes\gamma_2.
$$

Their word coefficients are precisely the products of the original coefficients.
Applying complex conjugation to every matrix and vector proves the conjugation assertion used in Lemma 10.

**Minimality and two-sided residuals.**
In a minimal representation, the reachable column span of $\mu(v)\gamma$ is $k^n$; otherwise restriction gives a smaller representation.
The unobservable subspace $\{z:\lambda\mu(u)z=0\ \forall u\}$ is zero; otherwise quotienting gives a smaller representation.
Consequently the rows $\lambda\mu(u)$ span $(k^n)^*$.
Choose polynomial combinations with $\lambda\mu(P_i)=e_i^T$ and $\mu(Q_j)\gamma=e_j$.
The formula in Theorem 4 follows directly.
This proof establishes the needed field interface without importing the full minimal-realization theory.

## Reduced support and the specialization boundary

For a free group $\Gamma=F_X$, let $A=X\sqcup\bar X$, $\bar x$ represent $x^{-1}$, $s:A^*\to\Gamma$ be word evaluation, and $m:\Gamma\to A^*$ select reduced words.
Extend $m$ coefficientwise: $m(a)$ has zero coefficients at nonreduced words.
For such an $S$, every word residual also has reduced support: if $w$ contains an adjacent inverse pair, so does $uwv$.
Theorem 4 consequently gives

$$
\mu(w)=0\quad\text{for every nonreduced }w.
$$

This is the key link between formal word length and group length in Proposition 9 and Theorem 12.
Minimality is essential to this inference: a nonminimal representation can contain states invisible to $\lambda$ and $\gamma$ with nonzero values on forbidden words.

The map $s$ is a polynomial algebra homomorphism, but **not an unrestricted map on all formal series**: an infinite coefficient sum may be required after cancellations.
On reduced-supported series it is a coefficient relabeling.
Products, matrix inverses, and infinite sums require separate analytic or Malcev-Neumann justification; those arguments belong in U004 and U005.

## Findings, dependencies, and limits

- **Finite alphabet is a real scope condition.**
  DR97 begins with an unspecified alphabet but explicitly uses finiteness on p. 618.
  If $A$ is infinite, the series $\sum_{x\in A}x$ has a two-dimensional representation (all letters use the same square-zero transition) but is not in the scalar inverse closure of finite-support polynomials: every finite rational expression uses only finitely many letters.
  Thus Theorem 2 as a universal equivalence needs the finite-alphabet convention or a changed notion of rational expression.
  The audited chain uses finite $X$ throughout; no infinite-rank extension is claimed.
- DR97 cites reference [2] for the proofs of Section 2.1 and [8,16,17] for named interfaces.
  The local field proofs above reconstruct the interfaces actually used.
  They do not audit all source results over arbitrary rings, representative functions on monoids, historical attributions, or the claimed semiring extension.
  In a semiring, the appropriate rational operation is a defined star; literal closure under ring inverses is not a direct substitution.
- No source unit here identifies group series with affiliated operators or with a universal free field.
  Those identifications require their own interfaces.

## Verification facts and revisions

On 2026-09-08 the coordinating agent read the extracted pp. 614-616 and 621 and visually inspected those pages, including residual orientation, Theorem 4, and formula (2).
The local reconstruction above received independent AI cross-review by the analytic reconstruction agent: inverse-residual span invariance, minimal reachable/unobservable constructions, polynomial row/column selection, formal pivots, and the infinite-alphabet counterexample were checked without an unresolved objection.
The Malcev-Neumann reconstruction agent separately inspected the field/minimality interfaces used by U005.
These are mathematical reviews, not audits of every original reference or formal verification.
This initial unit supplies the formal interface for U002, U004, and U005; no new project claim ID is assigned.

## Source and inspection

Source edition: DR97, the retained ten-page published Inventiones mathematicae 128 (1997), pp. 613-622, DOI 10.1007/s002220050154. Printed page equals PDF page plus 612. The separately retained 14-page author typeset version has an unstated preparation/revision date and was compared only at the selected passages recorded in U006; it does not replace the primary version.

Source passages: Section 2.1, printed pp. 614-616, Definition 1 and Theorems 2-4; formula (2), p. 621.

Inspection: 2026-09-08: finite-alphabet, commutative-field interfaces reconstructed from inspected source pages and independently cross-reviewed. Broader arbitrary-ring and semiring formulations and historical attributions have statement inspection only. Infinite-alphabet equivalence is not accepted; unrestricted formal-to-group substitution is excluded. No original-reference-wide proof audit or formal verification.

## Additional original definition reading

<a id="definition-recheck"></a>

This additional actual source-reading account was retained from L_F0063 at 2026-10-21T01:08.
This maintenance does not reopen the source or extend its original proof audit.

The unbounded-operator agent reread printed pp. 613-618 / PDF pp. 1-6 on 2026-09-10 and inspected full rendered pp. 615-618 / PDF pp. 3-6.
The separately retained author comparison version was not reopened, and the old proof-review scope is unchanged.
The complete formal-series/residual/representation definitions already belong to this unit; tree Hilbert spaces and the graded unitary belong to U002, regular representations and the reduced C*-algebra to U004.
Definition 1 p. 616 calls scalar inverse closure rational closure; Definition 6 p. 618 fixes the matrix size and its union, exactly as defined in U003.
Those are separate constructions before Theorem 7 proves their equality in its actual ambient algebra.
The full group word index uses reduced words, unlike an unrestricted 2d-letter Fock basis; the reduction map is not a homomorphism on arbitrary infinite series.
The extra scalar summand carries zero action and is not a unital scalar representation, so numerical tree-commutator ranks cannot silently be equated with normalized dual ranks.
These are source-instance/notation comparisons, without new proof edges into the general affiliated rationality theorem or historical-origin certification.

## Haar and tree normalization

DR97 uses the regular free-group model, rather than giving an abstract probability-space definition of a Haar unitary.
The project's exact free-Haar instance is already stated in [Miy26-U003, Theorem 3.5](../Miy26/Yin_U003.md#theorem-35-completing-the-haar-argument): \(u_i=\lambda(g_i)\) in \(L(F_d)\), with the regular trace.
Accordingly, this entry is a realization/notation reference for that instance, not a newly sourced general Haar definition.

The word index set for group coefficients is reduced words.
It is not the unrestricted \(2d\)-letter Fock basis.
The zero extension \(m(a)\) vanishes on nonreduced words, while the group involution reverses order and inverts letters.

The extra scalar vector in the tree representation is acted on by zero, as the rendered p. 617 explicitly shows.
It is not a unital copy of the scalar representation.
Consequently the full graded tree commutator and a normalized dual commutator need not have the same numerical rank or scalar behavior.
All finite ranks here mean ordinary algebraic/Hilbert image dimension, not a trace rank.
No affiliated rank metric is defined in these passages.

---
author: Yin
---

# Mercat's fixed Salem return core and exact finite quotient witnesses

Date: 2026-10-10T14:18.
Human author: Yin.
Mixed source-application, computational checkpoint and exploration history under [G0001](../tasks/Yin_T_G0001_v1.md), which remains paused.

## Organization and current scope

At the user's request, the completed D G0008 record is retained in L according to its role.
It contains a fixed-input source deduction and finite experiments, with distinct review scopes; it is not a single adopted Claim asserting all exploratory proposals.
The full original text, title, mathematical formulas, thirteen-witness table, failed bounded attempt and review disclosure follow unchanged except for heading depth and relocated links.
Programs and exact arrays remain in [J G0015](../computations/programs/Yin_J_G0015/readme.md).
The redundant D copy is retired only after full-text preservation and incoming-reference checks.

The source input is Mercat's polynomial \(P_M(t)=t^4-2t^3+t^2-2t+1\).
The accepted [Mer13 Proposition 4.23 interface](../audits/literature/Mer13/Yin_U001.md), together with the elementary source-to-core conversion and [L G0157](Yin_L_G0157_v1.md), yields the [complete fixed theorem now in C371](../claims/Yin_C_G0371_v1.md#statement): its infinite actual return core and the stated unbounded-norm/quotient consequences.
Mercat's geometric and residual calculations were not rerun in this project.

The different quartic \(P_Q(t)=t^4-t^3-t^2-t+1\) later received its own complete actual-return proof in [L G0169](Yin_L_G0169_v1.md).
The original degree-ten Lehmer input later received its corresponding complete chain in [L G0170](Yin_L_G0170_v1.md).
Neither result changes what the earlier J15 finite witnesses themselves proved; the L169/L170 narrow-strip conclusions are not automatically transferred to Mercat's quartic.
Their general interface still requires its explicit common-return hypotheses.

The historical review below, also retained as a precise [formal R finding](../audits/reviews/Yin_R_G0581_v1.md#historical-mercat-coordinator-finding), covers the source deduction and finite-witness interpretation.
It preserves its successful rerun of the author's verifier on thirteen witnesses, its absence of a new reviewer implementation, its accepted-external-input boundary, and its exclusion of the comparison sources.
No mathematical program or source proof was rerun for this organization.
FP16/FP18 remain comparison-only at their recorded scope.
The general Salem conjecture and weighted-tail questions are not settled by this retained record or the cited fixed results; the original future plans are dated history, partly superseded by the cited later work, and do not resume execution.

## Retained complete draft and historical review

### Original-digit Salem return cores: a source bridge and large-quotient probes

Date: 2026-10-09.
Exploratory G0001/S_G0001/S_G0007 work by the assigned orbit_research AI for Yin.
This is a working draft with no adopted Claim or fixed proof status.

#### Question and scope

Investigate original-digit returning states in [S G0007](../strategies/Yin_S_G0007.md), allowing both structural source reuse and finite counterexample-guided experiments under the current parallel exploration policy.
The main question is whether Salem neutral directions force infinitely many actual returning states, and what a successful full-law estimate would then need to retain.

The first candidate retained the full endpoint Gram projection row.
A reuse check found that the proposed cubic residual identity, Blaschke limit, and Salem geometric specialization are already established in [L G0098](Yin_L_G0098_v1.md#cubic-orthogonal-posterior-certificate) and [L G0101](Yin_L_G0101_v1.md#salem-endpoint-geometric-control).
No duplicate proof or new result is claimed for that candidate.
The present draft developed the distinct return-core direction below.
It alters no fixed material.

<a id="mercat-core-consequence"></a>
#### 1. An actual infinite original-digit Salem core from an existing theorem

Use

    P(t)=t^4-2t^3+t^2-2t+1,
    beta>1 its expanding real root,
    X_0=0, X_(j+1)=beta X_j+eta_j, eta_j in {-1,0,1}.

Let D contain exactly those states that occur on finite zero-to-zero words.
The state is an element of Z[beta], not merely its real projection.

[Mer13-U001](../audits/literature/Mer13/Yin_U001.md#mer13-u001) accepts Mercat's Proposition 4.23 at its exact statement and applicability scope: the binary affine monoid for this beta is not strongly automatic.
The unit checks that its trimmed relation states are exactly the above D and gives the finite-language normalization.
The source's geometric descent and finite computer-assisted residual check have not been independently reproduced here.
This is an established external premise, not a new theorem attributed to the project.

For completeness, the algebraic input satisfies every domain hypothesis of [L G0157](Yin_L_G0157_v1.md#global-prime-support-finite-core-equivalence).
Write u=t+t^(-1).
Then t^(-2)P(t)=u^2-2u-1, whose two roots are 1+sqrt(2)>2 and 1-sqrt(2) in (-2,2).
This quadratic is irreducible.
In its field Q(sqrt(2)), u^2-4 is negative under the embedding u=1-sqrt(2), hence is not a square.
Thus t^2-ut+1 is irreducible over that quadratic field, and beta has degree four with minimal polynomial P.
The roots over 1-sqrt(2) form a unit-circle pair; the other pair is beta,beta^(-1).
Hence beta is a nontorsion algebraic unit and a Salem number.
Since 1+sqrt(2)<5/2=2+1/2 and t+t^(-1) is strictly increasing for t>1, beta<2.
Its value approximately 1.8832 is orientation only; no numerical premise is used.

If D were finite, its exact digit transitions plus a rejecting state would give a finite automaton for the ternary zero language.
Replacing a digit by every binary pair having that difference would give a finite automaton for binary relations.
Because beta>1, equal affine maps must have the same number of generators.
This contradicts the accepted source proposition.
Therefore D is infinite.

L G0157 now gives the following deductions at this one fixed input:

1. The norms |N_(Q(beta)/Q)(x)| for x in D minus {0} are unbounded.
2. Infinitely many prime ideals occur among those states' principal ideal supports; no single finite S covers the complete returning core.
3. The integer quotients q of all height-one multiples Pq have unbounded coefficient height.

The source boundary matters: this is an actual original-digit Salem control, rather than the weaker fact that an ambient bounded spectrum is infinite.
It is separate from the earlier near-two complex-pair Mercat control in [L G0082](Yin_L_G0082_v1.md).
It does not prove the corresponding statements for Lehmer's number or for arbitrary sufficiently near-one reciprocal inputs.
It does not bound their weighted first-return tails.

<a id="finite-infinite-language-source-boundary"></a>
#### 2. A literature conjecture matches the unresolved finite-core question

The primary conference contribution [FP16, Numeration 2016](https://km.fjfi.cvut.cz/jn16/_files/jn16_proc.pdf), Christiane Frougny and Edita Pelantova, *Beta-Representations of 0 and Pisot Numbers*, printed pp.50--53, was located and read at printed p.52.
Its Conjecture 11 predicts nonregularity of the finite zero language at the canonical symmetric digit width, provided it is nontrivial and the algebraic base has a unit-circle conjugate.
For 1<beta<2 this is precisely width one.
It is a conjecture in that source, and is retained here only as a comparison and research lead; no assertion of its current resolution or novelty is made.
[Scoped FP16-U001 reading and actual proceedings holding](../audits/literature/FP16/Yin_U001.md#fp16-u001) are recorded separately.

Their [FP18, Two applications of the spectrum of numbers, arXiv:1512.04234v3](../literature/pdf/FP18.pdf), dated 18 March 2018, was checked at its definitions, Theorem 1.2 context, and Section 4 scope.
Its finite-Buchi-automaton conclusion concerns infinite zero expansions.
It is not a theorem giving nonregularity of the finite zero-word language.
In particular, spectrum density alone cannot discharge the actual finite-return condition.
The [scoped FP18-U001 reading record](../audits/literature/FP18/Yin_U001.md#fp18-u001) distinguishes the retained v3 preprint from the published journal metadata.
Neither comparison source is adopted as a proof input above; the accepted input is the original Mer13 proposition.

The bounded search used generic queries about Salem zero automata, finite zero representations and low-height multiples.
Local checks first read L G0157, L G0158, the registry and the existing Mercat/BV20 note.
No unpublished text was sent.
The search found a concrete theorem and an explicit conjectural boundary and stopped; it does not establish exhaustive literature coverage.

<a id="large-quotient-pilot"></a>
#### 3. Finite exact probes on the original Lehmer and Salem inputs

[J G0015](../computations/programs/Yin_J_G0015/readme.md) searches integer q with coefficient bounds and H(Pq)<=1, maximizing the middle coefficient.
Floating-point mixed-integer optimization only selects witnesses.
A separate standard-library verifier uses monic long division, exact Horner state recurrence and fraction-free multiplication-matrix determinants.
It establishes the retained witness identities and state norms, without accepting optimizer optimality claims.

The following are actual verified witnesses.
N is the number of permitted q coefficients; leading or trailing zeros are retained in the saved arrays.

| Minimal polynomial/input | N | H(q) | Largest absolute norm along the saved return word |
| --- | --- | --- | --- |
| t^4-t^3-t^2-t+1 | 20,40,80 | 2,3,5 | 17,69,101 |
| Mercat quartic P above | 20,40,80 | 1,3,4 | 4,23,151 |
| Lehmer polynomial | 20,40,80,160 | 6,11,19,30 | 379; 5666599; 116138093; 10323130327 |
| t^2-t-1 | 20,40,80 | 1,1,1 | 1,1,1 |

For the Lehmer N=160 witness, the only return times in the saved length-170 word are 1 and 170.
Removing the first zero digit therefore leaves a genuine first-return word of length 169.
At saved cut length 84 its state is

    4-3 beta^2-4 beta^3+5 beta^4-13 beta^5
      +5 beta^6-6 beta^7+beta^8+7 beta^9,

with absolute norm 10323130327.
This is one exact returning state.
Its existence refutes a global norm cap below that integer for this fixed input, but not the existence of some larger cap.
The N=320 search reached its eight-second limit without a feasible witness; that failed attempt is retained.
No infeasibility or optimizer-optimality conclusion is adopted.

These probes deliberately change the measured object relative to the old fixed-seed bounded-height loops: they explicitly find quotient height above one and actual large-norm states.
A finite sequence of such witnesses still does not prove unbounded height, an infinite prime support, or any entropy-rate assertion for Lehmer's number.

<a id="orbit-core-next-experiment"></a>
#### 4. Next experiments and a conjectural geometric model

The source proof suggests a concrete model for further work: separate the expanding/contracting strip from the neutral directions, and seek finite blocks of true digits that reduce a neutral size while keeping the strip admissible.
The existing full fixed-prime estimates then become local components of an infinite-state process rather than a hoped-for complete finite-prime covering.
A proof of unbounded core alone would diagnose state-space structure; a useful entropy estimate would additionally need quantitative original probabilities for every departure and reentry.

Two discriminating next experiments are available without presupposing the final gap:

1. For the fixed Lehmer input, replace pure maximization by a targeted neutral-coordinate objective and extract relationships between successive large-quotient witnesses.
   Seek a reusable block operation that raises quotient height while preserving H(Pq)<=1, or exhibit a concrete failure of that conjecture.
   The current witnesses do not yet provide such an operation.
2. Try a Mercat-style finite family of legal return blocks on the simpler quartic t^4-t^3-t^2-t+1, and test whether their neutral displacements surround zero over a covered expanding-coordinate interval.
   An interval table and its compact leftover states would need exact verification.
   Reusing the method does not transfer Mercat's successful table to another beta.

A bold working conjecture is that every Salem beta in (1,2) admitting a nontrivial height-one relation has an infinite actual core, with neutral coordinates of returning states unbounded.
The first assertion matches the identified older finite-language conjecture in this domain and is not claimed new.
A second, more speculative quantitative question is whether an original-law weighted excursion estimate can use neutral displacement rather than norm alone, avoiding L G0155's unit-constant-weight obstruction.
No contraction inequality is currently supplied.

#### Review status

The source applicability conversion, elementary polynomial domain check, use of L G0157, and computation interpretation were self-checked by the drafting agent.
The finite programs actually ran as recorded in J G0015.
No fixed L promotion or Claim adoption is asserted by this draft.

At 2026-10-09T15:16 the coordinating AI for Yin separately reviewed the source-to-core deduction in Section 1 and the interpretation of the finite witnesses in Section 3.
It directly read Mercat's primary published Proposition 4.23, Definition 3.2 and Lemma 4.4; checked the equal-length, difference-alphabet, composition-reversal and zero-to-zero domain conversion; rechecked the elementary degree/Salem argument and the exact L157 five-way interface; and found no gap at the stated fixed-input scope.
It read the complete J15 integer verifier and reran it successfully on all thirteen saved witnesses, reproducing the listed heights, norms and first-return times.
This rerun uses the author's separately implemented verifier, not a new reviewer implementation.
The reviewer received author progress explanations and the broad task context but contributed no derivation, witness or source mapping to this round.
It did not reproduce Mercat's geometric/finite proof or independently review the comparison sources in Section 2.
The local review therefore supports the indicated source applicability and finite witness interpretation, while retaining the source's original proof as an accepted external input and every stated generalization/tail limitation.
